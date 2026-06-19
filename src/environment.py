import stable_retro
import stable_baselines3

env = stable_retro.make(
    game="SuperMarioWorld-Snes-v0",
    state="YoshiIsland1",
    use_restricted_actions=stable_retro.Actions.FILTERED,
    obs_type=stable_retro.Observations.RAM
)

initial_obs, initial_info = env.reset()

model = stable_baselines3.PPO("MlpPolicy", env, verbose=0, tensorboard_log="./ppo_retro_logs/")

action_array = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

while True:
    if action_array[0] > 1:
        action_array[0] = 0
        action_array[7] = 0
    observation, reward, terminated, truncated, info = env.step(action_array)
    action_array[0] += 1
    action_array[7] += 1
    if info["lives"] < 4:
        break
env.close()
