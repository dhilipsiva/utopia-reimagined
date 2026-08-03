# registry/data — upstream-licensed snapshots

Files here are merged snapshots of upstream datasets kept so a reader can
reproduce a derivation without refetching. **They are not CC0** — unlike
`../claims.json` and the scripts, each snapshot carries its upstream licence:

- `vdem-happiness-*.csv` — merged from four Our World in Data grapher series
  (CC BY 4.0; OWID's processing of V-Dem [Regimes of the World, electoral
  democracy index], the World Happiness Report [Cantril ladder], and the World
  Bank [GDP per capita, PPP]). Attribution: Our World in Data; V-Dem Institute;
  World Happiness Report; World Bank. Regenerate with
  `python3 registry/fetch/vdem_happiness.py --snapshot registry/data`.
