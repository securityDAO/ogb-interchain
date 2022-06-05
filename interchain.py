# Format to follow for node-level classification task on a heterogeneous graph
# Heterogeneous structure is seleceted based on the results from https://arxiv.org/abs/2203.12363

from ogb.io import DataSaver
import numpy as np
import networkx as nx
import os

saver = DatasetSaver(dataset_name = "ogbn-interchain", is_hetero = True, version = 1)

# Graph list with heterogeneous graph objects
graph_list = []
num_data = 100
for i in range(num_data):
    g = nx.fast_gnp_random_graph(10, 0.5)
    graph = dict()
    graph['edge_index'] = np.array(g.edges).transpose() 
    num_edges = graph['edge_index'].shape[1]

    graph['num_nodes'] = len(g.nodes)

    graph['node_feat'] = np.random.randn(graph['num_nodes'], 3)
    graph['edge_feat'] = np.random.randn(num_edges, 3) 
    
    graph_list.append(graph)

# Target labels
num_classes = 3
labels = np.random.randint(num_classes, size = (num_data,1))
saver.save_target_labels(labels)

# Dataset split
split_idx = dict()
perm = np.random.permutation(num_data)
split_idx['train'] = perm[:int(0.8*num_data)]
split_idx['valid'] = perm[int(0.8*num_data): int(0.9*num_data)]
split_idx['test'] = perm[int(0.9*num_data):]
saver.save_split(split_idx, split_name = 'random')

# Mapping dir
mapping_path = 'mapping/'
os.makedirs(mapping_path)
os.mknod(os.path.join(mapping_path, 'README.md'))

saver.copy_mapping_dir(mapping_path)

# Task information - classification
saver.save_task_info(task_type = 'classification', eval_metric = 'acc', num_classes = num_classes)


# Meta information dictionary
meta_dict = saver.get_meta_dict()

