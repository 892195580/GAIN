from collections import defaultdict

import dgl
import torch
import networkx as nx
import matplotlib.pyplot as plt
# data_dict = {
#     ('user', 'follows', 'user'): (torch.tensor([0, 1]), torch.tensor([1, 2])),
#     ('user', 'follows', 'topic'): (torch.tensor([1, 1]), torch.tensor([1, 2])),
#     ('user', 'plays', 'game'): (torch.tensor([0, 3]), torch.tensor([3, 4]))
# }
# g = dgl.heterograph(data_dict)
# print(g)
# print(g.nodes('user'))
# print(g.nodes('topic'))
# print(g.nodes('game'))
# print(g.number_of_src_nodes('user'))
entity_feat = torch.tensor([[1, 1, 2, 3, 1], [2, 1, 2, 3, 2], [3, 1, 2, 3, 3]])
etype_feat = torch.tensor([[1, 6, 7, 8, 1], [2, 6, 7, 8, 2], [3, 6, 7, 8, 3]])
rel_feat = torch.tensor([[1, 11, 12, 13, 1], [2, 11, 12, 13, 2], [3, 11, 12, 13, 3]])
d = defaultdict(list)
# print(feat)
d[('entity', 'type', 'etype')].append((0, 0))
d[('entity', 'type', 'etype')].append((1, 1))
d[('entity', 'type', 'etype')].append((2, 2))

d[('etype', 'relation', 'rel')].append((0, 0))
d[('etype', 'relation', 'rel')].append((1, 0))
d[('etype', 'relation', 'rel')].append((1, 1))
d[('etype', 'relation', 'rel')].append((2, 1))
d[('etype', 'relation', 'rel')].append((0, 2))
d[('etype', 'relation', 'rel')].append((2, 2))

num_nodes_dict = {'rel': 4}  # 'entity': 3, 'etype': 3,
g = dgl.heterograph(d, num_nodes_dict=num_nodes_dict)
print(g.nodes('rel'))
# g.nodes['entity'].data['f'] = entity_feat
# g.nodes['etype'].data['f'] = etype_feat
# g.nodes['rel'].data['f'] = rel_feat
# print(g.nodes['entity'].data['f'][1])
# print(g.nodes['etype'].data['f'][1])
# print(g.nodes['rel'].data['f'][1])

