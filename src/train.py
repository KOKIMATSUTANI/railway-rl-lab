import graph.build_pyg as build_pyg
import gnn.graph_encoder as graph_encoder

def main():

    data = build_pyg.data

    encoder = graph_encoder.RailwayGNN()

    embedding = encoder(data)

    print(embedding)


if __name__ == "__main__":
    main()