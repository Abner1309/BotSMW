import gymnasium as gym

class CustomRewardWrapper(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self.previous_score = None
        self.previous_coins = None
        self.previous_yoshiCoins = None
        self.previous_lives = None
        self.previous_x = None
        self.max_x = None
        self.was_dead = None
        self.was_level_cleared = None

    def _reset_variables(self):
        self.previous_score = None
        self.previous_coins = None
        self.previous_yoshiCoins = None
        self.previous_lives = None
        self.previous_x = None
        self.max_x = None
        self.was_dead = None
        self.was_level_cleared = None

    def reset(self, **kwargs):
        self._reset_variables()
        obs, info = self.env.reset(**kwargs)
        return obs, info

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)

        actual_score = info.get("score", 0)
        actual_coins = info.get("coins", 0)
        actual_yoshi_coins = info.get("yoshiCoins", 0)
        actual_lives = info.get("lives", 0)
        actual_x = info.get("x", 0)
        actual_level_cleared = info.get("endOfLevel", 0)
        dead_value = info.get("dead", 1)
        is_dead_now = (dead_value == 0)

        if self.previous_x is None:
            self.previous_score = actual_score
            self.previous_coins = actual_coins
            self.previous_yoshiCoins = actual_yoshi_coins
            self.previous_lives = actual_lives
            self.previous_x = actual_x
            self.max_x = actual_x
            self.was_dead = is_dead_now
            self.was_level_cleared = actual_level_cleared
            return obs, float(reward), terminated, truncated, info

        custom_reward = reward
        custom_reward -= 0.1

        if actual_x > self.max_x:
            custom_reward += (actual_x - self.max_x) * 2.0
            self.max_x = actual_x

        if actual_coins > self.previous_coins:
            custom_reward += 25.0

        if actual_yoshi_coins > self.previous_yoshiCoins:
            custom_reward += 50.0

        if actual_lives > self.previous_lives:
            custom_reward += 100.0

        if actual_score > self.previous_score:
            custom_reward += 20.0

        if is_dead_now and not self.was_dead:
            custom_reward -= 250.0
            terminated = True

        if actual_level_cleared > 0 and self.was_level_cleared == 0:
            custom_reward += 10000.0
            terminated = True

        self.previous_score = actual_score
        self.previous_coins = actual_coins
        self.previous_yoshiCoins = actual_yoshi_coins
        self.previous_lives = actual_lives
        self.previous_x = actual_x
        self.was_dead = is_dead_now
        self.was_level_cleared = actual_level_cleared

        return obs, float(custom_reward), terminated, truncated, info