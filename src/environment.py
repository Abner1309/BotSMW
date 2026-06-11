import stable_retro

def make_custom_env(game_name, state_name):
    actions_space = stable_retro.Actions.FILTERED
    observation_space = stable_retro.Observations.RAM
    custom_env = stable_retro.make(
        game=game_name,
        state=state_name,
        actions=actions_space,
        obs_type=observation_space
    )
    return custom_env
