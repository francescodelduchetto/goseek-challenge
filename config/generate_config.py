import random
import yaml

k = 10  # number of episodes to generate
l = 400  # episode length
f = 30  # number of fruit
scenes = [1, 2, 3, 4, 5]  # scenes (1 through 5 are provided)

data = {}
data['ENV'] = {'sim_path': 'simulator/goseek-v0.1.4.x86_64'}

data['EPISODE'] = {'scenes': random.choices(scenes, k=k),
                   'n_targets': [f for _ in range(k)],
                   'episode_length': [l for _ in range(k)],
                   'random_seeds': [random.randint(1, 1e6) for _ in range(k)]
                   }

with open('example.yaml', 'w') as outfile:
    yaml.dump(data, outfile)