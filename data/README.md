# Data dir structure
`just data` from repository root to result in the following:

```
.
└── data
    ├── application.db
    ├── blockstore.db
    ├── cs.wal
    ├── evidence.db
    ├── snapshots
    │   └── metadata.db
    ├── state.db
    └── wasm
        ├── cache
        │   └── modules
        │       └── v3-wasmer1
        └── state
            └── wasm
```

# Data loading
Note: the database files for `juno-1-phoenix-genesis.tgz` come as `.ldb` on-disk
https://github.com/tendermint/tm-db to load

# KVStore -> Graph
Information about how the `KVStore` is structured:
https://docs.cosmos.network/master/core/store.html

We begin with the `Multistore` 
