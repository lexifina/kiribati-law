# How this repository was made (Kiribati)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| legislation.gov.uk: The Kiribati Independence Order 1979 (SI 1979/719), as made | <https://www.legislation.gov.uk/uksi/1979/719/made> | 2026-10-29 | Open Government Licence v3.0 |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of Kiribati (as made, 1979) | 1 | 1979-07-12 to 1979-07-12 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 2 tags.

## Dates

Each commit is dated at noon (Pacific/Tarawa) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Constitution came into force at independence on 12 July 1979 (Kiribati Independence Order 1979, article 1 and section 1 of the Kiribati Act 1979 context; legislation.gov.uk records the coming-into-force date). https://www.legislation.gov.uk/uksi/1979/719/made

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `71cc8b7285bb0002f3fcf2ae96b379700c64e1676f11fb46e8ca5eeb6c90076d` (177163 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `6229396f41c9d7f1d6f405becfbe4097b35b82da`, `check.py` `5e112e6a33b7e93d00112e55f01fbb4fb3fdd8da`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Only the Constitution as made (Schedule to the Order, in force 12 July 1979) is built; it is the only official text found online. The Kiribati government site and PacLII were not used.
- Schedule 1 (oaths and affirmations) is published only as images, so it is left out (no OCR). Part headings inside chapters are left out; chapter titles are kept.
- Order date 26 June 1979 and publication date 4 July 1979 are from the legislation.gov.uk metadata; the Constitution took effect at independence on 12 July 1979.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the parser; it did not write or alter any legal text.
