import stable_baselines3
from stable_baselines3.common.callbacks import CheckpointCallback, CallbackList
from stable_baselines3.common.vec_env import SubprocVecEnv, DummyVecEnv, VecNormalize, VecFrameStack, VecTransposeImage
from src.environment import make_custom_env, make_custom_env_parallel
from src.save_winner import SaveOnSuccessCallback

def train_sequential(load_path=None, vec_path=None):
    env = DummyVecEnv([lambda: make_custom_env()])
    env = VecFrameStack(env, 4)
    env = VecTransposeImage(env)

    if load_path is None:
        env = VecNormalize(env, norm_obs=False, norm_reward=True, clip_reward=10.0)
        model = stable_baselines3.PPO(
            policy='CnnPolicy',
            env=env,
            n_steps=2048,
            n_epochs=4,
            batch_size=256,
            verbose=1,
            ent_coef=0.02,
            target_kl=0.03,
        )
    else:
        assert vec_path is not None, "vec_path is mandatory"
        env = VecNormalize.load(vec_path, env)
        model = stable_baselines3.PPO.load(load_path, env=env)

    checkpoint = CheckpointCallback(
        save_freq=100_000,
        save_path="../checkpoints/",
        name_prefix="ppo_smw_sequential",
        save_vecnormalize=True
    )
    success_callback = SaveOnSuccessCallback(
        check_freq=1,
        save_path="../trained_models/",
    )
    callback_chain = CallbackList([checkpoint, success_callback])

    print("Starting sequential training...")
    model.learn(
        total_timesteps=10_000_000,
        callback=callback_chain,
        progress_bar=True,
    )
    print("Training completed")

    env.save("../trained_models/vecnormalize_sequential.pkl")
    model.save("../trained_models/bot_sequential")


def train_parallel(cpus, load_path=None, vec_path=None):
    env = SubprocVecEnv([make_custom_env_parallel(rank=i, seed=42) for i in range(cpus)])
    env = VecFrameStack(env, 4)
    env = VecTransposeImage(env)

    if load_path is None:
        env = VecNormalize(env, norm_obs=False, norm_reward=True, clip_reward=10.0)
        model = stable_baselines3.PPO(
            policy='CnnPolicy',
            env=env,
            n_steps=2048,
            n_epochs=4,
            batch_size=256,
            verbose=1,
            ent_coef=0.02,
            target_kl=0.03,
        )
    else:
        assert vec_path is not None, "vec_path is mandatory"
        env = VecNormalize.load(vec_path, env)
        model = stable_baselines3.PPO.load(load_path, env=env)

    checkpoint = CheckpointCallback(
        save_freq=max(100_000 // cpus, 1),
        save_path="../checkpoints/",
        name_prefix="ppo_smw_parallel",
        save_vecnormalize = True
    )

    success_callback = SaveOnSuccessCallback(
        check_freq=1,
        save_path="../trained_models/",
    )

    callback_chain = CallbackList([checkpoint, success_callback])

    print(f"Starting parallel training using {cpus} CPUs...")
    model.learn(
        total_timesteps=10_000_000,
        callback=callback_chain,
        progress_bar=True,
    )
    print("Training completed")
    env.save("../trained_models/vecnormalize_parallel.pkl")
    model.save("../trained_models/bot_parallel")

if __name__ == "__main__":
    train_sequential()
