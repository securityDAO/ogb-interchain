# ogb-interchain
## Open Graph Benchmark
The [Open Graph Benchmark (OGB)](https://ogb.stanford.edu/) aims to provide graph datasets that cover important graph machine learning tasks, diverse dataset scale, and rich domains.

[In the original paper](https://arxiv.org/abs/2005.00687), OGB is described by the authors as:

__{...} a diverse set of challenging and realistic benchmark datasets to facilitate scalable, robust, and reproducible graph machine learning (ML) research. OGB datasets are large-scale, encompass multiple important graph ML tasks, and cover a diverse range of domains, ranging from social and information networks to biological networks, molecular graphs, source code ASTs, and knowledge graphs. For each dataset, we provide a unified evaluation protocol using meaningful application-specific data splits and evaluation metrics. In addition to building the datasets, we also perform extensive benchmark experiments for each dataset. Our experiments suggest that OGB datasets present significant challenges of scalability to large-scale graphs and out-of-distribution generalization under realistic data splits, indicating fruitful opportunities for future research. Finally, OGB provides an automated end-to-end graph ML pipeline that simplifies and standardizes the process of graph data loading, experimental setup, and model evaluation. OGB will be regularly updated and welcomes inputs from the community. OGB datasets as well as data loaders, evaluation scripts, baseline code, and leaderboards are publicly available {...}__

Since being released, OGB was used in a Large-Scale Challenge at the [KDD Cup 2021](https://ogb.stanford.edu/kddcup2021/results/), and OGB-LSC is now part of the [NeurIPS 2022 Competitions](https://blog.neurips.cc/2022/05/31/neurips-2022-competitions-announced/).
## GraphHack 2022
The aim of `obg-interchain` is to use Junø chain data to build tooling that will integrate blockchain data into the OBG benchmark that future generations of graph learning researchers will cut their teeth on. Over time, we hope exposure to the specific properties of this data will lead to serendipitous discoveries and birth new types of graph-level, node-level, and link-level tasks specific to L-1 chains in IBC.

Crucially, by standardizing common stages of the graph ML model exploration into the `Dataset`, `Loader`, `Evaluator` components, as well as a `Leaderboard` that is shared across researchers in the field - OGB allows for researchers to try novel architectures on a variety of datasets quickly. 

If `ogb-interchain`is successful - the third iteration of OGB-LSC will include blockchain datasets into the competition.
## Why Junø?
[Junø](https://www.junonetwork.io/) is the first and thus far the largest _permissionless_ [CosmWasm](https://docs.cosmwasm.com/docs/1.0/) smart contract chain in [Cosmos / IBC ecosystem](https://hub.mintscan.io/ibc-network). Its existence alongside other chains in the greater Interchain presents an additional set of interesting possibilities to be analyzed (e.g. [IBC assets](https://github.com/CosmosContracts/junoswap-asset-list/blob/main/ibc_assets.json) like `$EEUR` that are swapped on [JunøSwap](https://junoswap.com), and then get converted to their native counterparts).

As a chain, Junø has innovated in areas of cross-chain scalability of interoperable smart contracts, governance (bringing "DAOs all the way down" vision for L-1s closer to reality), and explored the security space of WebAssembly runtimes for smart contracts - all of which can benefit from timely understanding of the geometry of the power and value [manifold](https://www.youtube.com/watch?v=w6Pw4MOzMuo) formed by chain's state over time.

## How
Practically, within the limited scope of the GraphHack 2022, the aim is to achieve the following:

- build a [OBG Data Loader](https://ogb.stanford.edu/docs/home/#dataloader) for Junø data and prepare a reference dataset in the correct format
- [submit](https://docs.google.com/document/d/e/2PACX-1vS1hBTYLONRwAU9UxK42USTuRKrt_Yk4H0EhpLvJC_eOrGxbJUtrzDqlIStAFpnwZt2N28B3MuSxgqj/pub) the reference dataset to OBG / Stanford for inclusion in OBG v3 at NeurIPS 2023
- run out of the box [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/) tasks appropriate to the data and shortlist ones that make it into the final demo
- structure the loader process in a way that other IBC chains like Cosmos Hub and Osmosis can begin adapting for their chain's data as well, ultimately resulting in the benchmark dataset that includes several chains interacting

## Team

- Barton Rhodes [@bmorphism](https://github.com/bmorphism)
- Jake Hartnell [@JakeHartnell](https://github.com/JakeHartnell)
- Logan Cerkovnik

w/ help from Patrycja Zawadka of Figment who are doing excellent foundational work on bringing Cosmos to Graph Protocol
(we can all choose to play positive sum games! 🕹)
