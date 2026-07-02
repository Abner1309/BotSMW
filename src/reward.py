import gymnasium as gym

class CustomRewardWrapper(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self.refresh = True
        self.punishment = 0
        self.previous_score = 0
        self.previous_coins = 0
        self.previous_lives = 0
        self.previous_x = 0

    def _assignment(self, score, coins, lives, x):
        self.previous_score = score
        self.previous_coins = coins
        self.previous_lives = lives
        self.previous_x = x

    def reset(self, **kwargs):
        self.refresh = True
        self.punishment = 0
        obs, info = self.env.reset(**kwargs)
        return obs, info

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        custom_reward = 0.0
        self.punishment += 1

        actual_score = info.get("score", 0)
        actual_coins = info.get("coins", 0)
        actual_lives = info.get("lives", 5)
        actual_x = info.get("x", 0)

        mario_status = info.get("mario_status", 0)
        end_of_level = info.get("endOfLevel", 0)

        if self.refresh:
            self._assignment(actual_score, actual_coins, actual_lives, actual_x)
            self.refresh = False
            self.punishment = 0
            return obs, float(custom_reward), terminated, truncated, info

        if end_of_level == 1:
            custom_reward += 10.0
            terminated = True
            return obs, float(custom_reward), terminated, truncated, info

        if mario_status == 9:
            custom_reward -= 4.0
            terminated = True
            return obs, float(custom_reward), terminated, truncated, info

        if actual_coins > self.previous_coins:
            custom_reward += 0.4
            self.punishment = 0
            self.previous_coins = actual_coins

        if actual_lives > self.previous_lives:
            custom_reward += 4.0
            self.punishment = 0
            self.previous_lives = actual_lives

        if actual_score > self.previous_score:
            custom_reward += 0.6
            self.punishment = 0
            self.previous_score = actual_score

        if actual_x > self.previous_x:
            custom_reward += 0.2
            self.punishment = 0
            self.previous_x = actual_x

        if self.punishment > 10:
            custom_reward -= 0.2

        return obs, float(custom_reward), terminated, truncated, info
