import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """
    Map graph embedding to Q-values.
    """
    def __init__(self,
                 embedding_dim=64,
                 hidden_dim=128,
                 num_actions=3):

        super().__init__()

        self.fc1 = nn.Linear(
            embedding_dim,
            hidden_dim
        )

        self.fc2 = nn.Linear(
            hidden_dim,
            num_actions
        )

    def forward(self, graph_embedding):

        x = F.relu(
            self.fc1(graph_embedding)
        )

        q_values = self.fc2(x)

        return q_values