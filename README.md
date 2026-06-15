# std-replacement-data

A curated dataset of Rust crates whose functionality is now available in the
standard library. crates.io reads it to point out when `std` already covers
what the crate provides and where to find the equivalent API.

Every entry is a checkable factual statement about `std`, never an opinion about
a competing crate.

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

## What qualifies

Standard-library replacements only. The dataset deliberately avoids "prefer this
nicer crate instead" recommendations.

Two kinds of entries qualify:

- **Full**: the crate's functionality is entirely available through a stable
  `std` API.
- **Partial**: the bulk of the crate's common use case has moved to `std`, but
  not all of it. The `description` must spell out what is still missing.

Coverage is judged by the dominant use case. If only a small slice of a crate's
purpose lives in `std`, it does not qualify. `itertools` is the canonical
exclusion: a handful of its adaptors have `std` equivalents, but the crate as a
whole is not replaced.

Before an entry lands, the maintainer(s) of the flagged crate get a window to
weigh in, either to object or to show that the replacement is less complete than
claimed, in which case the entry becomes partial or is dropped.

## Origin

The data started out inline in crates.io and moved here so other tools can
consume it too. See [rust-lang/crates.io#13855][pr] for the original
implementation.

[pr]: https://github.com/rust-lang/crates.io/pull/13855

## License

Licensed under either of these:

- Apache License, Version 2.0 ([LICENSE-APACHE](./LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](./LICENSE-MIT) or <https://opensource.org/licenses/MIT>)
