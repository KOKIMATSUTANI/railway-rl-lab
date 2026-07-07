import torch
import torch.nn as nn

from gnn.graph_state_encoder import RailwayGNN 
from rl.q_network import QNetwork


class RailwayAgent(nn.Module):

    def __init__(
        self,
        embedding_dim=8,
        hidden_dim=32,
        num_actions=3
    ):
        super().__init__()

        self.encoder = RailwayGNN()

        self.q_network = QNetwork(
            embedding_dim,
            hidden_dim,
            num_actions
        )

    def forward(self, data):

        graph_embedding = self.encoder(data)

        q_values = self.q_network(graph_embedding)

        return q_values

    def select_action(self, data):

        q_values = self.forward(data)

        action = torch.argmax(
            q_values,
            dim=1
        )

        return action