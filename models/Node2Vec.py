import torch_cluster
import torch
from torch_geometric.nn import Node2Vec
from torch_geometric.data import Data

from tqdm.auto import tqdm, trange
import os
import polars as pl
batch_size = 256
num_epochs = 20
embedding_dim = 128
walk_length = 80
context_size = 10
walks_per_node = 10
num_negative_samples = 1
p_parameter = 1
q_parameters = [ 0.5,1., 2.]
eth_edges = torch.from_numpy(pl.read_csv("from_to.csv").to_numpy().T)
dev = "cuda" if torch.cuda.is_available()  else "cpu"
device = torch.device(dev)

data = Data(eth_edges)

path = "./"
for q_idx, q in enumerate(q_parameters):
  # can be used for finding the best params
  break

model = Node2Vec(eth_edges, embedding_dim=embedding_dim,
                  walk_length=walk_length, context_size=context_size,
                  walks_per_node=walks_per_node,
                  num_negative_samples=num_negative_samples,
                  p=p_parameter, q=q, sparse=True).to(device)

loader = model.loader(batch_size=batch_size, shuffle=True, num_workers=2)
optimizer = torch.optim.SparseAdam(list(model.parameters()), lr=0.01)

def train():
    model.train()
    total_loss = 0
    for pos_rw, neg_rw in loader:
        optimizer.zero_grad()
        loss = model.loss(pos_rw.to(device), neg_rw.to(device))
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(loader)

for epoch in trange(num_epochs):
    loss = train()
    print(f'Epoch: {epoch:02d}, Loss: {loss:.4f}')
    torch.save(model, os.path.join(path, f"node2vec_emb_{q_idx}.pth"))

nodes = eth_edges.ravel().unique().sort().values.to(device)
embeddings = model(nodes).detach().cpu()
torch.save(embeddings,"embeddings")