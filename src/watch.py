import stable_retro
import stable_baselines3
from stable_baselines3.common.atari_wrappers import WarpFrame
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack, VecTransposeImage
from src.reward import CustomRewardWrapper
from src.skip_frame import SkipFrameWrapper
from gymnasium.wrappers import TimeLimit


def make_watch_env():
    env = stable_retro.make(
        game="SuperMarioWorld-Snes-v0",
        state="YoshiIsland1",
        use_restricted_actions=stable_retro.Actions.FILTERED,
        obs_type=stable_retro.Observations.IMAGE,
        render_mode="human"
    )
    env = SkipFrameWrapper(env)
    env = CustomRewardWrapper(env)
    env = WarpFrame(env)
    env = TimeLimit(env, max_episode_steps=1800)
    return env

def watch_agent(brain_path):
    env = DummyVecEnv([make_watch_env])
    env = VecFrameStack(env, n_stack=4)
    env = VecTransposeImage(env)

    # Load the intelligence.
    model = stable_baselines3.PPO.load(brain_path, env=env)

    # Gameplay Loop.
    obs = env.reset()
    total_reward = 0.0
    print("Starting the game.")
    try:
        while True:
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, dones, infos = env.step(action)
            total_reward += reward[0]
            if dones[0]:
                break
        print(f"End of episode. Total Reward: {total_reward}")
    except KeyboardInterrupt:
        print("Closing the environment.")
    finally:
        env.close()

if __name__ == "__main__":
    watch_agent("../trained_models/winner.zip")
