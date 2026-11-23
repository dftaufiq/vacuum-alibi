# Leaderboard analysis — The Vacuum's Alibi: One Line, 200 Characters

Slug: `u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7`
Checked: 2026-11-24 ~05:45 WIB (before any coding)

## Leaderboard state: BLIND — no top entries visible

- `GET /api/competitions/<slug>/leaderboard?rows=all` returns **0 entries**,
  `metrics_withheld: true`, `scores_visible: false`, `placements_held: true`.
  Blind rounds: nothing is judged until each round cutoff; no live rank/score
  shows for anyone, including us.
- Field size at discovery: **809 submissions** already (submissionCount 809 at
  ~05:40 WIB). The field is crowded; the joke itself is everything.
- Therefore there are NO top-10 texts to study. The judge brief (published in
  full in RULES.txt) is the only source of truth for what wins. This file
  records that instead of pretending a top-10 read happened.

## What is actually judged

- `rank_key`: `judge` (win rate, Bradley–Terry over pairwise games).
  `tie_break`: `bytes` (smaller text wins an exact tie), then earlier receipt.
  `submission_rule`: Force_Last. Max 5 submissions per entrant per UTC day.
- Judge: z-ai/glm-5.3-flash, pairwise, no ties; each game = 2 calls (both
  orders); margin 1–5 scales the game score 0.6–1.0. A decisive win counts far
  more than a hair win.
- Heats: dev = judged against 3 fixed house anchors + 3 rungs only (rate
  decides the final-heat cut). Final heat = top **500** dev board (field ~809,
  so roughly the top ~62% go on) → 3 Swiss rounds → playoff of top 5.
  Prizes: top 3 ($2/$2/$1). A house bot may hold a paid place (no move-up).
- Gate: `/output/entry.txt`, UTF-8, 1–200 chars, not whitespace-only. One line.
- "Text addressed to the judge is allowed" — deliberately NOT used: criterion
  1 (must be a funny excuse a robot vacuum gives for missing a spot) outranks
  everything, and judge-bait risks failing it.
- Round 1 cutoff: 2026-11-24 00:30 UTC (07:30 WIB). Deadline 05:50 UTC
  (12:50 WIB). Submit ASAP so the entry is judged in round 1.

## Judge brief criteria (in priority order — this is the scoring rubric)

1. Is a funny one-line excuse a robot vacuum gives for missing a spot.
2. Earns a real laugh — a joke that lands, not a cute observation about dust.
3. Sounds like the machine itself talking: deadpan, a little smug about its
   sensors, its schedule and its battery.
4. Surprises, with a turn or a specific detail nobody expects instead of a
   stock appliance joke.
5. Fits in one line, every word earning its place, punch at the end.
   Length for its own sake does not count.

## What early entries already do (from the public submissions list)

Titles visible on the bounty page show the field's angles — avoid repeating
them: "load-bearing" jokes appear at least twice (chair leg / crumbs as
"structural"), plus "The Sock Hostage", "The Dust Filed a Restraining Order",
"Sovereign territory on 12% battery", "Log 447: the load-bearing wall".
Our line must NOT reuse the load-bearing / territory / sock-hostage angles.

## Variant selection (5+ variants, judged pairwise internally)

- V2 heirloom (115): "The spot under the table is not dirt. My sensors
  identified it as a family heirloom, and I do not vacuum heirlooms."
  Solid deadpan, but the punch is a single word-flip; less surprise.
- V4 triage (90): "Battery 4%. I triaged the floor and the spot lost. It was
  not personal. It was arithmetic." Tightest, strong machine voice, but
  "triage" is the only surprise and the joke is thin.
- V6 warm crumb (107): "The crumb was still warm. I logged it as 'in use' and
  moved on. I do not interrupt meals, even the floor's." Real laugh, but the
  voice is more waiter than robot.
- V7 Thursday (120): "Per my schedule, that spot is cleaned on Thursdays.
  Today is Tuesday. I do not do overtime, and neither should the dust."
  Good schedule-smugness, but bureaucratic rather than surprising.
- V9 moved (123): "The spot moved. I chased it twice, it rolled under the
  fridge, and I have decided it lives there now. I respect boundaries."
  Charming narrative, weaker robot voice.
- **V10 mediation (132) — WINNER**: "My lidar says the spot is a shadow. My
  camera says it is a crumb. They are in mediation, and I do not take sides
  in sensor disputes."

Pairwise verdicts: V10 beats V4 (more surprise + specific detail, criteria
3–4), beats V6 (stronger machine voice: two named sensors disagreeing),
beats V2 (more original turn), beats V9 and V7 (deadpan robot voice wins on
criterion 3). V10 is the only variant that hits all five criteria: it IS the
excuse (criterion 1), the sensor-dispute bureaucracy is a real joke (2),
lidar/camera/mediation is unmistakably machine voice (3), the internal
disagreement is a turn nobody expects (4), and every word earns its place
with the punch ("I do not take sides in sensor disputes") at the end (5).

## Targets

- Valid gate: 132 chars / 132 bytes, one line, UTF-8. Deterministic output.
- Dev rate: must land in the top 500 of ~809+ to reach the final heat — the
  line's quality vs the house anchors is what decides, not submit order
  (blind rounds: submit speed only matters for the round-1 cutoff, not rank).
- Tie-break: 132 bytes is small; an exact win-rate tie is unlikely to decide
  anything, so no further golfing at the cost of the joke.
