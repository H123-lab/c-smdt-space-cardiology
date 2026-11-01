function [HR_next, R_prox_next, C_vessel_next, G_baro_next] = autonomic_feedback(MAP, CVP, G_baro_current, gravity_regime, dt_days)
    % AUTONOMIC_FEEDBACK Models closed-loop baroreflex resets and ANS deconditioning.
    %
    % Inputs:
    %   MAP              - Mean Arterial Pressure (mmHg) from current cycle
    %   CVP              - Central Venous Pressure (mmHg) from current cycle
    %   G_baro_current   - Active baroreflex sensitivity gain coefficient
    %   gravity_regime   - String identifier: '1G', '0.38G', or '0G'
    %   dt_days          - Simulated time increment stepped in fractional days
    %
    % Outputs:
    %   HR_next          - Calculated target Heart Rate (bpm) for the next cycle
    %   R_prox_next      - Adjusted proximal arterial Windkessel resistance
    %   C_vessel_next    - Adjusted systemic vascular compliance matrix property
    %   G_baro_next      - Updated baroreflex gain following regulatory drift

    %% 1. Nominal Base Constants (Verified Terrestrial Baselines)
    MAP_setpoint = 93.3;       % Target homeostatic arterial pressure (mmHg)
    HR_nominal   = 70.0;       % Baseline resting heart rate (bpm)
    R_prox_base  = 16.2;       % Baseline proximal resistance (mmHg * min / L)
    C_vessel_base = 0.015;     % Baseline arterial compliance (mL / mmHg)
    
    % Gain decay time constant (Tau) for spaceflight deconditioning
    tau_adaptation = 180.0;    % 6-month characteristic decay constant (days)

    %% 2. Gravity-Dependent Parameter Shifts & Gain Setpoints
    switch upper(gravity_regime)
        case '1G'
            G_target = 1.0;            % Maintained full baroreflex sensitivity
            G_space_reset = 1.0;
            
        case '0.38G' % Martian Intermediate State
            G_target = 0.85;           % 15% partial blunting target
            G_space_reset = 0.85;
            
        case '0G' % Microgravity / Spaceflight Regime
            % Cephalad fluid shift causes a chronic downregulation of gain
            G_target = 0.40;           % Up to 60% chronic blunting target
            G_space_reset = 0.35;      
            
        otherwise
            error('Invalid gravity_regime parameter. Use ''1G'', ''0.38G'', or ''0G''.');
    end

    %% 3. Dynamic Baroreflex Gain Drift Execution (Longitudinal Timeline)
    % Computes the progressive loss of vagal tone using a differential decay step
    dG = -(1.0 / tau_adaptation) * (G_baro_current - G_space_reset) * dt_days;
    G_baro_next = max(G_baro_current + dG, G_space_reset);

    %% 4. Error Mapping & Sign-Agnostic Sigmoidal Compensation Loop
    % Calculate systemic deviation from baseline pressure homeostatic values
    pressure_error = MAP - MAP_setpoint;
    
    % Apply a standard logistics sigmoid model to prevent unphysiological infinity loops
    % Compensatory adjustment scaling parameter maps to current degraded baroreflex gain
    activation_factor = 2.0 / (1.0 + exp(-0.05 * pressure_error * G_baro_next)) - 1.0;

    %% 5. Actuator System Updates (Next-Step Outputs generation)
    % Sympathetic up-regulation triggers tachycardia if MAP drops
    HR_next = HR_nominal * (1.0 - 0.35 * activation_factor);
    
    % Ensure limits sit within valid clinical parameters (40 bpm to 160 bpm bounds)
    HR_next = max(min(HR_next, 160.0), 40.0);

    % Peripheral vasoconstriction updates modifying proximal afterloads
    R_prox_next = R_prox_base * (1.0 - 0.25 * activation_factor);
    
    % Distal smooth muscle compliance adjustments mapping vessel wall tone variations
    C_vessel_next = C_vessel_base * (1.0 + 0.15 * activation_factor);

    %% 6. Microgravity Venous Engorgement Overlay
    if strcmp(upper(gravity_regime), '0G') && CVP > 8.0
        % Central fluid pooling induces structural venous compliance stretching overrides
        C_vessel_next = C_vessel_next * 1.08; 
    end
end
