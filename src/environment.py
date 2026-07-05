import stable_retro
from gymnasium.wrappers import TimeLimit
from stable_baselines3.common.atari_wrappers import WarpFrame
from stable_baselines3.common.monitor import Monitor
from src.reward import CustomRewardWrapper
from src.skip_frame import SkipFrameWrapper

def make_custom_env(rank: int = 0, seed: int = 0):
    env = stable_retro.make(
        game="SuperMarioWorld-Snes-v0",
        state="YoshiIsland1",
        use_restricted_actions=stable_retro.Actions.FILTERED,
        obs_type=stable_retro.Observations.IMAGE,
        render_mode=None,
    )

    env = SkipFrameWrapper(env)
    env = CustomRewardWrapper(env)
    env = WarpFrame(env)
    env = TimeLimit(env, max_episode_steps=1800)
    env = Monitor(env)

    if seed is not None:
        env.action_space.seed(seed + rank)
    return env


def make_custom_env_parallel(rank: int = 0, seed: int = 0):
    def _init():
        return make_custom_env(rank=rank, seed=seed)
    return _init