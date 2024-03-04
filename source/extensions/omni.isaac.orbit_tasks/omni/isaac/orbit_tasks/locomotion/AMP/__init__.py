# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Locomotion environments with velocity-tracking commands.

These environments are based on the `legged_gym` environments provided by Rudin et al.

Reference:
    https://github.com/leggedrobotics/legged_gym
"""

import gymnasium as gym

from .amp_env_cfg import AMPFlatEnvCfg
from .agents.rsl_amp_cfg import MiniCheetahAmpPpoRunnerCfg 



##
# Register Gym environments.
##


gym.register(
    id="Isaac-AMP-Flat-MiniCheetah-v0",
    entry_point="omni.isaac.orbit.envs:RLTaskEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": AMPFlatEnvCfg,
        "rsl_rl_cfg_entry_point": MiniCheetahAmpPpoRunnerCfg,
    },
)