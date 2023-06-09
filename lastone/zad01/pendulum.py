import gym

env = gym.make("Pendulum-v1", render_mode="human")
env.reset(seed=2)

for _ in range(300):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()

# Stan gry jest ciągły (kąt wahadła, prędkość), a akcje to wartość siły, jaką gracz chce przyłożyć do wahadła w kierunku obrotu.
# Przyład gry z ciągłym stanem gry i ciągłym zestawem akcji
