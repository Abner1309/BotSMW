import stable_retro
import stable_baselines3
import time
from src.reward import CustomRewardWrapper

def watch_agent(brain_path):
    # Create the environment.
    env = stable_retro.make(
        game="SuperMarioWorld-Snes-v0",
        state="YoshiIsland1",
        use_restricted_actions=stable_retro.Actions.FILTERED,
        obs_type=stable_retro.Observations.RAM,
        render_mode="human"
    )

    # Apply the personalized reward function.
    env = CustomRewardWrapper(env)

    # Load the intelligence.
    model = stable_baselines3.PPO.load(brain_path, env=env)

    # Gameplay Loop.
    obs, info = env.reset()
    done = False
    total_reward = 0

    print("Starting the game.")
    try:
        while not done:
            # Prediction of the agent's action.
            action, _states = model.predict(obs, deterministic=True)

            # Advance one frame.
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            total_reward += reward

            # Frame adjustment.
            time.sleep(1.0 / 60.0)
        print(f"End of episode. Total Reward: {total_reward}")
    except KeyboardInterrupt:
        print("Closing the environment.")
    finally:
        env.close()


