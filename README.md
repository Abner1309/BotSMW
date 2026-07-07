# Super Mario World - Reinforcement Learning

![Super Mario World - Image](img/SuperMarioWorld.webp)

## 🌐 Overview:
This project aims to create a bot that will be trained through reinforcement learning to complete the first scenario of the "Yoshi's Island" map in the game "Super Mario World".

## 🧩 Key Mapping:
The "actions" parameter of env.step() expects a binary array of 12 positions. In the case of the Super Nintendo (SNES), the exact order of the positions in this array represents the following buttons:

* i[0] = B
* i[1] = Y
* i[2] = SELECT
* i[3] = START
* i[4] = UP
* i[5] = DOWN
* i[6] = LEFT
* i[7] = RIGHT
* i[8] = A
* i[9] = X
* i[10] = Left Corner
* i[11] = Right Corner

![Super Nintendo Control](img/SNES-Control.webp)

## 🧠 Proximal Policy Optimization (PPO)
The Proximal Policy Optimization (PPO) from stable-baselines3 (SB3) is one of the most popular and efficient implementations for Reinforcement Learning. It is an On-Policy algorithm, meaning it learns directly from the experiences it is collecting in real time, rather than reusing old memories.

## 💰 Reward Function:
The reward function works as follows:
1. If Mario moves to the right, he earns a score.
2. If Mario collects regular coins or Yoshi coins, he receives points.
3. If Mario dies, he receives a penalty.
4. If Mario completes the level, he will receive the highest possible score.

# 🏆 Training:
It took 7,200,000 timesteps for the agent to complete the game's first scenario.
The agent's performance can be observed using the "watch.py" module in conjunction with the file located at "/trained_models/winner.zip".

<video src="/video/winner.mkv" controls width="100%">
  Your browser does not support video playback.
</video>

## ⚠️ Warnings:
It is extremely important to update the "data.json" file located in the "stable_retro/data/stable/SuperMarioWorld-Snes" folder; otherwise, the custom reward function will not work, and training will fail.

## 🎲 Scenario:
The levels in Super Mario World (Dinosaur Land) are divided into 7 main worlds and 2 secret areas, totaling 96 exits. The locations are:

1. Yoshi's Island.
2. Donut Plains.
3. Vanilla Dome.
4. Twin Bridges.
5. Forest of Illusion.
6. Chocolate Island.
7. Valley of Bowser.

## 🐍 Python Version:
3.10.16

## 🔨 Tools:
* Stable Retro.
* Stable Baselines3.
