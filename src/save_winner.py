import os
from stable_baselines3.common.callbacks import BaseCallback

class SaveOnSuccessCallback(BaseCallback):
    def __init__(self, check_freq: int = 1, save_path: str = "../trained_models", verbose: int = 1):
        super(SaveOnSuccessCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.save_path = save_path
        os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self) -> bool:
        if self.n_calls % self.check_freq == 0:
            for idx, info in enumerate(self.locals.get("infos", [])):
                if info.get("endOfLevel", 0) == 1:
                    if self.verbose > 0:
                        print("The agent has completed the scenario!")
                    model_path = os.path.join(self.save_path, "mario_winner")
                    self.model.save(model_path)
                    return False
        return True
