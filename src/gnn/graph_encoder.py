import graph.build_pyg as build_pyg

import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv


data = build_pyg.data

class RailwayGNN(torch.nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = GCNConv(3, 16)
        self.conv2 = GCNConv(16, 8)

    def forward(self, data):

        x = data.x
        edge_index = data.edge_index

        x = self.conv1(x, edge_index)
        x = F.relu(x)

        x = self.conv2(x, edge_index)

        return x


model = RailwayGNN()

embedding = model(data)

print(embedding)
print(embedding.shape)