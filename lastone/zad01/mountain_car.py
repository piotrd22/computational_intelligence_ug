import gym

env = gym.make("MountainCar-v0", render_mode="human")
env.reset(seed=2)

for _ in range(300):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()


# Stan gry jest ciągły (pozycja samochodu, prędkość), ale dostępne akcje to jedynie "przyspiesz" w lewo, "przyspiesz" w prawo lub "nie rób nic".
# Przykład gry z kategorią "Stan gry jest ciągły, ale zestaw akcji jest dyskretny"
