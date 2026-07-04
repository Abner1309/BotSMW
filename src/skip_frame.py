import gymnasium as gym

class SkipFrameWrapper(gym.Wrapper):
    def __init__(self, env, skip=4):
        super().__init__(env)
        self._skip = skip

    def step(self, action):
        obs = None
        reward = None
        terminated = False
        truncated = False
        info = {}

        for i in range(self._skip):
            obs, reward, terminated, truncated, info = self.env.step(action)
            if terminated or truncated:
                break
        return obs, reward, terminated, truncated, info
