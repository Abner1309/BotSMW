import stable_retro
from src.reward import CustomRewardWrapper

def make_custom_env():
    env = stable_retro.make(
        game="SuperMarioWorld-Snes-v0",
        state="YoshiIsland1",
        use_restricted_actions=stable_retro.Actions.FILTERED,
        obs_type=stable_retro.Observations.RAM,
        render_mode="None"
    )
    env = CustomRewardWrapper(env)
    return env

def make_custom_env_parallel():
    def _init():
        return make_custom_env()
    return _init

