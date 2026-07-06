import stable_retro
from gymnasium.wrappers import TimeLimit
from src.reward import CustomRewardWrapper
from src.skip_frame import SkipFrameWrapper

'''
    YOSHI'S ISLAND 1 - COMPLETE
    if 0 <= i <= 10:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if i == 11:
        action = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 12 <= i <= 90:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if i == 91:
        action = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 92 <= i <= 130:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if i == 133:
        action = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 134 <= i <= 140:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 141 <= i <= 200:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if i == 201:
        action = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 202 <= i <= 267:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 268 <= i <= 272:
        action = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 273 <= i <= 290:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 291 <= i <= 355:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 356 <= i <= 450:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 451 <= i <= 457:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 458 <= i <= 480:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 481 <= i <= 486:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 487 <= i <= 530:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 531 <= i <= 536:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 537 <= i <= 570:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 571 <= i <= 600:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 601 <= i <= 660:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 661 <= i <= 676:
        action = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 677 <= i <= 720:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 721 <= i <= 780:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 781 <= i <= 810:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 811 <= i <= 850:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 851 <= i <= 895:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 896 <= i <= 910:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 911 <= i <= 920:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 921 <= i <= 970:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 971 <= i <= 980:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 981 <= i <= 990:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 991 <= i <= 1010:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1011 <= i <= 1050:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 1061 <= i <= 1080:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1081 <= i <= 1120:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1121 <= i <= 1130:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1131 <= i <= 1140:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 1141 <= i <= 1150:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1151 <= i <= 1190:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1191 <= i <= 1200:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1201 <= i <= 1290:
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1291 <= i <= 1300:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1301 <= i <= 1310:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 1311 <= i <= 1320:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1321 <= i <= 1330:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 1331 <= i <= 1340:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1341 <= i <= 1350:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if 1351 <= i <= 1380:
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if 1381 <= i:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

def main():
    env = stable_retro.make(
        game="SuperMarioWorld-Snes-v0",
        state="YoshiIsland1",
        use_restricted_actions=stable_retro.Actions.FILTERED,
        obs_type=stable_retro.Observations.RAM,
        render_mode="human",
    )

    env = SkipFrameWrapper(env)
    env = CustomRewardWrapper(env)
    env = TimeLimit(env, max_episode_steps=1800)

    env.reset()
    action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while True:
        observation, reward, terminated, truncated, info = env.step(action)
        print(reward)
        env.render()
        i += 1
        if terminated or truncated:
            env.close()

if __name__ == "__main__":
    main()