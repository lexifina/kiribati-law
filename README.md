# Kiribati: law history in git

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="Kiribati law in this repository: what it holds, changes by the year they took effect, completeness against the official sources, and the correctness of what is held" src="data/effort-light.svg" width="880">
</picture>

The law of Kiribati as a git history: one file per section, one commit per version on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to a section; picking a date gives the text this record holds for that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Kiribati's national law, which global-law reads at `kiribati/national/acts/`.

**What is in it now:** the Constitution of Kiribati in two versions (as made in 1979, and as amended by the Constitution (Amendment) Act 1995); 47 Acts as enacted, 1981 to 2019 (land, fisheries, local government, public utilities, shipping, limitation, state lands, telecommunications and others); and 3 pieces of subsidiary legislation, 1979 to 2025. 51 laws, 52 versions in all; the layout is in [STRUCTURE.md](STRUCTURE.md), and the texts not yet taken, with the reason for each, are in [`data/held.json`](data/held.json).

Each provision is one file in `constitution/`: `sec-006.md` is section 6, protection from slavery and forced labour; `chapter-02.md` is the title of Chapter 2, `preamble.md` the Preamble and `schedule-2.md` Schedule 2, the territory of Kiribati.

The text is in English, the language of the official texts. The Acts and subsidiary legislation are in `acts/<year>/<number>-<name>/` and `subsidiary/<year>/<name>/`, one file per section (`sec-001.md`), with `preamble.md` for the title, assent and long title.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to section 6 of the Constitution | `git log -p --word-diff -- constitution/sec-006.md` |
| Which law wrote each line of section 6? | `git blame constitution/sec-006.md` |
| Every version of section 6, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constitution/sec-006.md` |
| Section 6 on 1 January 1980 | `python tools/on.py 1980-01-01 constitution sec-006` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Kiribati law](https://global-law.lexifina.com/v1/try_claude?country=kiribati)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=kiribati)**: the same question in ChatGPT.
- **[Search Kiribati law on our site](https://lexifina.com/law?country=kiribati&q=forced+labour)**: a search for "forced labour", with each provision's text and its versions, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=forced+labour&jurisdiction=kiribati)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add kiribati/national/acts
python3 tools/law.py show 1980-01-01 kiribati/national/acts/constitution/sec-006.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Pacific/Tarawa, on the day the version took effect, and carries it in its `In-force:` trailer:

- the Constitution as made is dated 12 July 1979, independence day, when it came into force; its `Enacted:` trailer gives the day the Order was made (26 June 1979) and `Published:` 4 July 1979, both from legislation.gov.uk's record of the Order;
- the Constitution as amended in 1995 is dated 13 February 1995, the day the Constitution (Amendment) Act 1995 was assented to, because the Act leaves its commencement line blank;
- an Act or instrument is dated by its commencement line or section when it gives a day, or the day its source records it entered into force; where the Act leaves its commencement blank, by the day of assent printed under "I assent" (`Date-basis: assent`). Acts that commence on a day appointed by notice are held until the notice is found.

Each version is credited to the law that made it: the 1979 version to the Order (`SI 1979/719`, tagged `constitution/1979-07-12` and `law/si-1979-719`), the 1995 version to the Constitution (Amendment) Act 1995, and each Act to itself.

## How it is checked

- The versions added on 2026-11-26 each carry their source file's sha256 (`Source-sha256:`), so every text can be checked against the PDF it was read from; [`REPRODUCE.md`](REPRODUCE.md) says how they were built.
- For the 1979 version, `tools/check_repo.py` reads every version back from git on the day it took effect, and on the day before, and compares it, file by file, with the corpus it was built from (its sha256 is in [`data/corpus.sha256`](data/corpus.sha256)); every commit's trailers must parse.
- `tools/build.py` writes the history from that corpus in one pass, and the same corpus always gives the same commit hashes. [`REPRODUCE.md`](REPRODUCE.md) gives the builder's hashes; it does not yet record a check run or a second build.
- History is append-only: no merge commits, no rewriting, no commit dated in the future.
- [vulnerabilities/](vulnerabilities/): possible drafting mistakes in this law, found by global-law's detectors and checked by hand. Not run yet.

## What it does not show

- **The Constitution as amended after 1995.** The amendments of 2013, 2016 and 2018 are published only as page scans, and no consolidated text with a day is available, so the latest version here is the 1995 one, not the text in force today.
- **The Revised Editions of the Laws** (1977, 1979, 1980, 1992 and 1998), which hold the Penal Code and most older Ordinances: no day is known for the date to which each edition is consolidated, so these texts are held.
- **Most Acts since 2010**, which are published only as scans, or whose assent day the scan's text layer does not show, and Acts that commence by notice. Treaties and court decisions are not here.
- **Part headings** inside the Constitution's chapters; chapter titles are kept. In the 1979 version, Schedule 1 (the oaths) is missing because its source publishes it only as images; the 1995 version has it.
- **The Order itself.** Only its Schedule, the Constitution, is here, not the Order's own articles.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [legislation.gov.uk](https://www.legislation.gov.uk/uksi/1979/719/made) (The National Archives) | UK statutory instrument, as made: the Kiribati Independence Order 1979 | no, only as made | The Constitution is the Schedule to the Order |
| [Office of Te Beretitenti](https://www.president.gov.ki/resources/gazettes-instruments.html) | Official: Gazette instruments, 2025 to 2026 | as made | Most are page scans and are held; 2 instruments with a text layer are used |
| [FAOLEX](https://faolex.fao.org/) (FAO) | Secondary copy: Acts and regulations as published | as made | Tagged `Source-status: secondary copy (FAOLEX, ...)` |
| [WIPO Lex](https://www.wipo.int/wipolex/en/members/profile/KI) (WIPO) | Secondary copy: the Constitution as amended to 1995, Acts and regulations | as made, one consolidation | Tagged `Source-status: secondary copy (WIPO Lex, ...)` |

PacLII is not used. Kiribati has no government legislation portal online; the Maneaba ni Maungatabu's Acts page lists no documents.

## Licence

See [`LICENSE`](LICENSE). The law texts keep their sources' terms (Open Government Licence v3.0 for legislation.gov.uk; FAO and WIPO terms for their copies). Lexifina's own work in this repository (the arrangement of the history, the commit messages, the tables and the tools) is dedicated to the public domain under CC0 1.0.

No AI model wrote, translated or corrected legal text; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## Visualisations

- [visualisations/](visualisations/): charts drawn from this repository. Not drawn yet.

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
