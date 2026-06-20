import stable_baselines3
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.vec_env import SubprocVecEnv
from src.environment import make_custom_env, make_custom_env_parallel

def train_sequential(load_path=None):
    env = make_custom_env()

    if load_path is None:
        model = stable_baselines3.PPO(
            policy='MlpPolicy',
            env=env,
            verbose=1,
        )
    else:
        model = stable_baselines3.PPO.load(load_path, env=env)

    checkpoint = CheckpointCallback(
        save_freq=10_000,
        save_path="./checkpoints/",
        name_prefix="ppo_smw"
    )
    print("Starting the training...")
    model.learn(
        total_timesteps=100_000,
        callback=checkpoint,
        progress_bar=True,
    )
    print("Training completed")
    model.save("./trained_models/bot")

def train_parallel(cpus, load_path=None):
    env = SubprocVecEnv([make_custom_env_parallel() for _ in range(cpus)])

    if load_path is None:
        model = stable_baselines3.PPO(
            policy='MlpPolicy',
            env=env,
            verbose=1,
        )
    else:
        model = stable_baselines3.PPO.load(load_path, env=env)

    print("Starting the training...")
    model.learn(
        total_timesteps=100_000,
        progress_bar=True,
    )
    print("Training completed")
    model.save("./trained_models/")
