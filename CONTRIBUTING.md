# Contributing

Thank you for helping keep the std-replacement dataset accurate and useful.

## Adding or changing an entry

Each crate lives in its own file at `data/<crate>.toml` with two fields:

- `description`: Markdown explaining the replacement. It must cite the stable
  `std` API(s) and the Rust version(s) that stabilized them.
- `url`: a docs or release-notes link, shown as a "Learn more" link.

Open one pull request per crate. `build.py` validates the dataset in CI, so run
it locally first:

```sh
python3 build.py
```

## What qualifies

Standard-library replacements only. The dataset deliberately avoids "prefer this
nicer crate instead" recommendations. Every entry is a checkable factual
statement about `std`, never an opinion about a competing crate.

Two kinds of entries qualify:

- **Full**: the crate's functionality is entirely available through a stable
  `std` API.
- **Partial**: the bulk of the crate's common use case has moved to `std`, but
  not all of it. The `description` must spell out what is still missing.

Coverage is judged by the dominant use case. If only a small slice of a crate's
purpose lives in `std`, it does not qualify. Some canonical examples of
exclusions are `itertools`, `libc`, and `rustix`. Some of their functionality
has been added to `std`, but the crates are not replaced, in whole or in part.

## Maintainer notice-and-comment

Before an entry lands, the maintainer(s) of the flagged crate get a window to
weigh in, either to object or to show that the replacement is less complete than
claimed, in which case the entry becomes partial or is dropped.
