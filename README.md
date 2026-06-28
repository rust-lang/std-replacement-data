# std-replacement-data

A curated dataset of Rust crates whose functionality is now available and
stable in the standard library. crates.io reads it to point out when `std`
already covers what the crate provides and where to find the equivalent API.

Every entry is a checkable factual statement about `std`, never an opinion about
a competing crate.

> [!NOTE]
> This dataset is maintained by the crates.io team. Other tools are welcome to
> consume the published JSON. We aim to make it a stable data source, but until
> then its contents and format may still change without warning.

## Data

Each crate lives in its own file at `data/<crate>.toml`:

```toml
description = """
The standard library provides `std::sync::LazyLock` (stable since Rust 1.80), \
which lets you replace the `lazy_static!` macro with a plain `static`.
"""
url = "https://doc.rust-lang.org/std/sync/struct.LazyLock.html"
```

- `description`: Markdown explaining the replacement. It must cite the stable
  `std` API(s) and the Rust version(s) that stabilized them.
- `url`: a docs or release-notes link, shown as a "Learn more" link.

## Consuming the data

`build.py` bundles every TOML file into a single `build/all.json`, keyed by
crate name. That file is published to GitHub Pages:

```
https://rust-lang.github.io/std-replacement-data/all.json
```

To build it locally (Python 3.11+ for `tomllib`):

```sh
python3 build.py
```

## Contributing

New entries are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) for what
qualifies as a std replacement and how to add one.

## Origin

The data started out inline in crates.io and moved here so other tools can
consume it too. See [rust-lang/crates.io#13855][pr] for the original
implementation.

[pr]: https://github.com/rust-lang/crates.io/pull/13855

## License

Licensed under either of these:

- Apache License, Version 2.0 ([LICENSE-APACHE](./LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](./LICENSE-MIT) or <https://opensource.org/licenses/MIT>)
