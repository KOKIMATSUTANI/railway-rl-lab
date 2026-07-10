import graph.build_pyg as build_pyg
from gnn.graph_state_encoder import RailwayGNN
from rl.agent import RailwayAgent
from rl.railway_env import RailwayEnv


def main():

    data = build_pyg.data

    env = RailwayEnv()

    encoder = RailwayGNN()

    embedding = encoder(data)

    print(embedding)

    agent = RailwayAgent()

    action = agent.select_action(data)

    print(action)



if __name__ == "__main__":
    main()