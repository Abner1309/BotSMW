import gymnasium as gym

class CustomRewardWrapper(gym.RewardWrapper):
    def __init__(self, env):
        super().__init__(env)
        self.previous_coins = None
        self.previous_lives = None
        self.previous_score = None

    def reward(self, reward):
        if hasattr(self.env.unwrapped, 'data'):
            info = self.env.unwrapped.data.lookup_all()
        else:
            info = {}

        actual_coins = info.get("coins")
        actual_lives = info.get("lives")
        actual_score = info.get("score")

        custom_reward = reward

        # Reward the agent for collecting coins.
        if self.previous_coins is not None and actual_coins > self.previous_coins:
            custom_reward += 10.0

        # Reward the agent for increasing lives.
        if self.previous_lives is not None and actual_lives > self.previous_lives:
            custom_reward += 100.0

        # Punish the agent for losing lives.
        if self.previous_lives is not None and actual_lives < self.previous_lives:
            custom_reward -= 100.0

        # Reward the agent for increasing the score.
        if self.previous_score is not None and actual_score > self.previous_score:
            custom_reward += 10.0

        # Updating the control variables.
        self.previous_coins = actual_coins
        self.previous_lives = actual_lives
        self.previous_score = actual_score

        return float(custom_reward)
