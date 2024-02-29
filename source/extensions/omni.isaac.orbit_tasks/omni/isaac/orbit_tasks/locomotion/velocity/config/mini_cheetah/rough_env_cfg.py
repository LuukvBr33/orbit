# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from omni.isaac.orbit.utils import configclass

from omni.isaac.orbit_tasks.locomotion.velocity.velocity_env_cfg import LocomotionVelocityRoughEnvCfg

##
# Pre-defined configs
##
from omni.isaac.orbit_assets.mini_cheetah import MINI_CHEETAH_CFG  # isort: skip


@configclass
class MiniCheetahRoughEnvCfg(LocomotionVelocityRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # switch robot to Mini Cheetah
        self.scene.robot = MINI_CHEETAH_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")


        # Randomization
        self.randomization.add_base_mass.params["asset_cfg"].body_names = "base"
        self.randomization.base_external_force_torque.params["asset_cfg"].body_names = "base"

        # # Rewards 
        # self.rewards.feet_air_time.params["contact_forces"].body_names = ".*_foot"
        # self.rewards.undesired_contacts.params["contact_forces"].body_names = "*._calf"
        
        # Terminations
        #self.terminations.base_contact.params["contact_forces"].body_names = "base"

        


@configclass
class MiniCheetahRoughEnvCfg_PLAY(MiniCheetahRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # make a smaller scene for play
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        # spawn the robot randomly in the grid (instead of their terrain levels)
        self.scene.terrain.max_init_terrain_level = None
        # reduce the number of terrains to save memory
        if self.scene.terrain.terrain_generator is not None:
            self.scene.terrain.terrain_generator.num_rows = 5
            self.scene.terrain.terrain_generator.num_cols = 5
            self.scene.terrain.terrain_generator.curriculum = False

        # disable randomization for play
        self.observations.policy.enable_corruption = False
        # remove random pushing
        self.randomization.base_external_force_torque = None
        self.randomization.push_robot = None
