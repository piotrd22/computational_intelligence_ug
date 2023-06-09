import gym
import numpy as np

env = gym.make('FrozenLake8x8-v1', render_mode="human")


observation, info = env.reset(seed=42)

for _ in range(60):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()

# Gra "FrozenLake8x8-v1" jest przykładem gry z dyskretnym stanem gry i dyskretnym zestawem akcji.
# W tej grze, stan gry jest reprezentowany przez numer pola na planszy 8x8.
# Natomiast akcja jest reprezentowana jako pola, w ktorych mozna sie poruszac (gora, dol, lewo, prawo).
