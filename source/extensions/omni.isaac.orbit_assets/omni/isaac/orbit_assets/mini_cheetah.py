# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for MIT Mini Cheetah robots.

The following configurations are available:

* :obj:`MINI_CHEETAH_CFG`: MIT Mini Cheetah robot with DC motor model for the legs

Reference: 
"""
import os 
import omni.isaac.orbit.sim as sim_utils
from omni.isaac.orbit.actuators import DCMotorCfg, ActuatorBaseCfg
from omni.isaac.orbit.assets.articulation import ArticulationCfg

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = '../../../../../../data/cheetah_description/cheetah_stiff.usd'
file_path = os.path.join(script_dir, relative_path)

##
# Configuration
##

MINI_CHEETAH_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path = file_path,
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=20.0,
            max_angular_velocity=20.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.4),
        joint_pos = {
            "LB_JOINT1": 0.01, 
            "LF_JOINT1": 0.01, 
            "RB_JOINT1": 0.01,
            "RF_JOINT1": 0.01,
            "LF_JOINT2": 0,
            "RF_JOINT2": 0,
            "LB_JOINT2": 0,
            "RB_JOINT2": 0,
            "LB_JOINT3": 0,
            "LF_JOINT3": 0,
            "RB_JOINT3": 0,
            "RF_JOINT3": 0,
        }, 
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "base_legs": DCMotorCfg(
            joint_names_expr=[".*_JOINT1", ".*_JOINT2", ".*_JOINT3"],
            effort_limit=23.5,
            saturation_effort=23.5,
            velocity_limit=30.0,
            stiffness=25.0,
            damping=0.5,
            friction=0.0,
        ),
    }
)
"""Configuration of MIT Mini Cheetah using MLP-based actuator model."""


   