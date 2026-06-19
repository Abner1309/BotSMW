import gymnasium as gym

class CustomRewardWrapper(gym.RewardWrapper):
    def __init__(self, env):
        super().__init__(env)
        self.previous_coins = None
        self.previous_yoshiCoins = None
        self.previous_lives = None
        self.previous_score = None
        self.previous_x = None
        self.was_dead = 0

    def reward(self, reward):
        if hasattr(self.env.unwrapped, 'data'):
            info = self.env.unwrapped.data.lookup_all()
        else:
            info = {}

        actual_coins = info.get("coins")
        actual_yoshi_coins = info.get("yoshiCoins")
        actual_lives = info.get("lives")
        actual_score = info.get("score")
        actual_x = info.get("x")
        is_alive = info.get("dead", 0)

        custom_reward = reward

        # Reward the agent for collecting coins.
        if self.previous_coins is not None and actual_coins > self.previous_coins:
            custom_reward += 30.0

        # Reward the agent for collecting Yoshi Coins.
        if self.previous_yoshiCoins is not None and actual_yoshi_coins > self.previous_yoshiCoins:
            custom_reward += 50.0

        # Reward the agent for increasing lives.
        if self.previous_lives is not None and actual_lives > self.previous_lives:
            custom_reward += 100.0

        # Punish the agent for dying.
        if is_alive > 0 and self.was_dead == 0:
            custom_reward -= 100.0

        # Punish the agent for losing lives.
        if self.previous_lives is not None and actual_lives < self.previous_lives:
            custom_reward -= 100.0

        # Reward the agent for increasing the score.
        if self.previous_score is not None and actual_score > self.previous_score:
            custom_reward += 10.0

        # Reward the agent for walking forward.
        if self.previous_x is not None and actual_x > self.previous_x:
            custom_reward += 0.01

        # Updating the control variables.
        self.previous_coins = actual_coins
        self.previous_yoshiCoins = actual_yoshi_coins
        self.previous_lives = actual_lives
        self.previous_score = actual_score
        self.previous_x = actual_x
        self.was_dead = is_alive

        return float(custom_reward)
