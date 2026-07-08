import graph.build_pyg as build_pyg

class RailwayEnv:

    def __init__(self):

        self.graph = None

    def reset(self):

        self.graph = build_pyg()

        return self.graph

    def step(self, action):

        """
        Actionに応じてgraph.xを書き換える
        """

        # TODO:
        # delay更新
        # occupancy更新
        # route更新

        reward = ...

        done = ...

        return self.graph, reward, done