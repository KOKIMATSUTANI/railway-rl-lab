import graph.build_pyg as build_pyg

class RailwayEnv:

    def __init__(self):

        self.graph = None

    def reset(self):

        self.graph = build_pyg()

        return self.graph

    def step(self, action):

        reward = self.calculate_reward()

        done = True

        return (
            self.graph,
            reward,
            done
        )

    def calculate_reward(self):

        return 1