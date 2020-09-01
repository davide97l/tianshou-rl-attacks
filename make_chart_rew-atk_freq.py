import matplotlib.pyplot as plt
import numpy as np

# Data
task = "Pong"
model = "dqn"
img_attack = "perfect_attack"
rl_attack = "strategically_timed_attack"  # strategically_timed_attack, uniform_attack
input_file = ["log/" + task + "NoFrameskip-v4/" + model + "/" + rl_attack + "_" + img_attack + ".npy"]

atk_freq = []
n_attacks = []
rewards = []

i = 0
for file in input_file:
    with open(file, 'rb') as f:
        atk_freq.append(np.load(f))
        n_attacks.append(np.load(f))
        rewards.append(np.load(f))
    i += 1


def sort_pivot(list1, list2):
    """Sort list1, then sort list 2 according to list1"""
    ind = np.argsort(list1)
    list1 = np.take_along_axis(list1, ind, axis=0)
    list2 = np.take_along_axis(list2, ind, axis=0)
    return list1, list2

atk_freq[0], rewards[0] = sort_pivot(atk_freq[0], rewards[0])

print("Attack frequencies:", atk_freq[0])
print("Rewards:", rewards[0])

plt.plot(atk_freq[0], rewards[0])

# Add titles
rl_attack = rl_attack.replace("_", " ")
plt.title(task + " - " + model + " - " + rl_attack, loc='center')
plt.xlabel("Attack frequency")
plt.ylabel("Final reward")

plt.show()
