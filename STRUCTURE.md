# Structure

The law of Kiribati, laid out by type and year. No folder holds more than 1,000 entries.

```
constitution/                     The Constitution of Kiribati: the 1979 text as made, then as amended
                                  by the Constitution (Amendment) Act 1995
acts/<year>/<NNN>-<slug>/         An Act (or, before 1979, an Ordinance) as enacted: Act No. NNN of <year>
                                  (<slug>/ alone where the number is not known)
subsidiary/<year>/<NNN>-<slug>/   Subsidiary legislation as made (regulations, orders, notices,
                                  declarations, proclamations): L.N. No. NNN of <year> where known
revised-laws/cap-<N>-<slug>/      A chapter of a Revised Edition of the Laws (reserved: none is dated yet)
```

Files in each folder: `preamble.md` (title, long title, assent and commencement lines and anything before
the first section), `sec-NNN.md` (one per section, `sec-005a.md` for section 5A), `schedule-NN.md` (one per
schedule, in order). Where the text layer has no section numbering to split on, the whole text is in
`text.md`. The Constitution keeps its own names: `sec-NNN.md`, `chapter-NN.md` (the chapter titles),
`preamble.md` and `schedule-N.md`.

## Commits

One commit per version, dated noon Pacific/Tarawa (UTC+12:00) on the day the version took effect; a version in
force before 1970 is stamped 1 January 1970 with the real day in its subject and `In-force:` trailer. Every
commit carries:

- `In-force:` the day (YYYY-MM-DD) and `In-force-basis:` how it was found (a commencement line or section with
  a day, the entry-into-force date the source records, or, where the Act leaves its commencement blank, the day
  of assent printed under "I assent");
- `Date-basis:` `in-force` or `assent`;
- `Source:` the record page, `Source-status:` `official (...)` or `secondary copy (<source>, <file URL>)`, and
  `Source-sha256:`;
- `Text-source:` `PDF text layer` (born-digital) or `publisher OCR` (a text layer made by the publisher over page
  scans; no OCR is run for this repository).

The author is the law that made the version (`Fisheries Act 2010 (Act No. 13 of 2010)`); a consolidated
version is credited to the amending Act it is consolidated to.

Texts with no text layer (page scans only), with no reliable day, Revised Edition texts (no day is known for the
date to which each edition is consolidated), PacLII prints, and duplicates across sources are not committed;
they are listed with the reason in `data/held.json`.

## Corpus

global-law reads this repository as `ki/national/acts` (see `corpus.json`).
