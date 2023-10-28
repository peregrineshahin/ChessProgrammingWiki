---
title: Andscacs
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Andscacs**

[](http://www.andscacs.com/) Andscacs Logo <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Andscacs**,

an [UCI](UCI "UCI") compliant chess engine by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"). Its development started in September 2013, and the first release was published in February 2014 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Andscacs soon evolved to a top engine, becoming runner-up at the [IGWT III](IGWT_III "IGWT III") losing the final from [Chiron](Chiron "Chiron") with the narrowest margin of 4½ - 5½, but taking revenge one year later at the [IGWT IV](IGWT_IV "IGWT IV"), this time with 6½ - 5½ to its favour. At the [Tenth Annual ACCA World Computer Rapid Chess Championship 2016](WCRCC_2016 "WCRCC 2016"), Andscacs emphasized its ambitions, and became runner-up without losing a single game, but 12 wins and 3 draws, and thus the only program preventing later winner [Komodo](Komodo "Komodo") from a 100% score.

## Contents

- [1 Description](#description)
  - [1.1 Search](#search)
  - [1.2 Evaluation](#evaluation)
  - [1.3 Tuning](#tuning)
- [2 Forum Posts](#forum-posts)
  - [2.1 2014](#2014)
  - [2.2 2015](#2015)
  - [2.3 2016](#2016)
  - [2.4 2017](#2017)
  - [2.5 2018](#2018)
  - [2.6 2020](#2020)
  - [2.7 2021](#2021)
- [3 External Links](#external-links)
  - [3.1 Chess Engine](#chess-engine)
  - [3.2 Misc](#misc)
- [4 References](#references)

## Description

Being a [bitboard](Bitboards "Bitboards") engine, Andscacs determines [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") ray-wise, quite similar to the [classical approach](Classical_Approach "Classical Approach") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Since version **0.70**, Andscacs uses [magic bitboards](Magic_Bitboards "Magic Bitboards") to speed the attack calculations <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Search

Andscacs applies a [principal variation search](Principal_Variation_Search "Principal Variation Search") with [tranposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Beside [quiescence](Quiescence_Search "Quiescence Search"), [selectivity](Selectivity "Selectivity") is due to [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [late move reductions](Late_Move_Reductions "Late Move Reductions"), [check extensions](Check_Extensions "Check Extensions"), [singular extensions](Singular_Extensions "Singular Extensions"), [razoring](Razoring "Razoring") and [futility pruning](Futility_Pruning "Futility Pruning"). [Move ordering](Move_Ordering "Move Ordering") is further improved by the [killer heuristic](Killer_Heuristic "Killer Heuristic"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening") and [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation"), the latter also used to [prune](Pruning "Pruning") bad [captures](Captures "Captures") in quiescence and futile moves near the horizon. Since version **0.70**, a [hash move](Hash_Move "Hash Move") is tried in [quiescence search](Quiescence_Search "Quiescence Search") even if it’s a [quiet move](Quiet_Moves "Quiet Moves"). Trying only [captures](Captures "Captures") and [promotions](Promotions "Promotions") was clearly weaker <a id="cite-note-6" href="#cite-ref-6">[6]</a>. Version 0.80 in Apil 2015 introduced a [threaded](Thread "Thread") [parallel search](Parallel_Search "Parallel Search") <a id="cite-note-7" href="#cite-ref-7">[7]</a>, a [Lazy SMP](Lazy_SMP "Lazy SMP") approach <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## Evaluation

The [evaluation](Evaluation "Evaluation") considers [material imbalances](Material_Tables "Material Tables"), and has [piece-square tables](Piece-Square_Tables "Piece-Square Tables") for [middlegame](Middlegame "Middlegame") and [endgame](Endgame "Endgame"), [piece values](Point_Value "Point Value") adapted by type of positions (open, closed), different types of [piece mobility](Mobility "Mobility"), [king safety](King_Safety "King Safety") and sophisticated [pawn structure](Pawn_Structure "Pawn Structure") evaluation with focus on [passed pawns](Passed_Pawn "Passed Pawn"), most features smoothed out between [game phases](Game_Phases "Game Phases") by a [tapered eval](Tapered_Eval "Tapered Eval"). Since version 0.62u, evaluation scores are cached with a small [evaluation hash table](Evaluation_Hash_Table "Evaluation Hash Table") <a id="cite-note-9" href="#cite-ref-9">[9]</a>.

## Tuning

The about 200 evaluation features were [tuned](Automated_Tuning "Automated Tuning") with 750.000 positions to minimize the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of [Stockfish's](Stockfish "Stockfish") and Andscacs' static evaluation, which initially added a nice Elo boost to Andscacs <a id="cite-note-10" href="#cite-ref-10">[10]</a>, without playing too similar.

## Forum Posts

## 2014

- [New engine - Andscacs](http://www.talkchess.com/forum/viewtopic.php?t=51182) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), February 06, 2014
- [Andscacs - New version](http://www.talkchess.com/forum/viewtopic.php?t=51218) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), February 09, 2014
- [Andscacs - New version](http://www.talkchess.com/forum/viewtopic.php?t=51475) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), March 03, 2014
- [Andscacs - New version 0.62w](http://www.talkchess.com/forum/viewtopic.php?t=51937) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 10, 2014
- [Andscacs - New version 0.62x](http://www.talkchess.com/forum/viewtopic.php?t=52233) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), May 05, 2014
- [Andscacs - New version 0.64](http://www.talkchess.com/forum/viewtopic.php?t=52572) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), June 07, 2014
- [Andscacs - New version 0.70](http://www.talkchess.com/forum/viewtopic.php?t=54257) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), November 05, 2014
- [Changes in Andscacs 0.70](http://www.talkchess.com/forum/viewtopic.php?t=54290) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), November 08, 2014
- [Andscacs - New version 0.71](http://www.talkchess.com/forum/viewtopic.php?t=54679) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), December 17, 2014
- [Changes in Andscacs 0.71](http://www.talkchess.com/forum/viewtopic.php?t=54700) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), December 19, 2014

## 2015

- [Andscacs - New version 0.72](http://www.talkchess.com/forum/viewtopic.php?t=55177) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), February 01, 2015
- [Andscacs - Test version 74024](http://www.talkchess.com/forum/viewtopic.php?t=55950) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 09, 2015
- [Trying to improve lazy smp](http://www.talkchess.com/forum/viewtopic.php?t=55970) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 11, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Empirical results with Lazy SMP, YBWC, DTS](http://www.talkchess.com/forum/viewtopic.php?t=56019) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 16, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), [DTS](Dynamic_Tree_Splitting "Dynamic Tree Splitting")
- [Andscacs - New version 0.80](http://www.talkchess.com/forum/viewtopic.php?t=56030) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 17, 2015
- [Andscacs - New version 0.81](http://www.talkchess.com/forum/viewtopic.php?t=56724) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), June 20, 2015

[Andscacs - New version 0.81 - Detailed changes](http://www.talkchess.com/forum/viewtopic.php?t=56724&start=3) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), June 20, 2015

- [Andscacs - New version 0.82](http://www.talkchess.com/forum/viewtopic.php?t=57281) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), August 16, 2015
- [Andscacs - New version 0.83](http://www.talkchess.com/forum/viewtopic.php?t=58220) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), November 10, 2015
- [Andscacs - New version 0.84](http://www.talkchess.com/forum/viewtopic.php?t=58512) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), December 07, 2015
- [Re: Why computing K that minimizes the sigmoid func. value?](http://www.talkchess.com/forum/viewtopic.php?t=58298&start=52) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), December 07, 2015 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")

## 2016

- [Andscacs - New version 0.85](http://www.talkchess.com/forum/viewtopic.php?t=59011) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), January 22, 2016
- [Andscacs - New version 0.86](http://www.talkchess.com/forum/viewtopic.php?t=59615) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), March 24, 2016
- [Singular extension](http://www.talkchess.com/forum/viewtopic.php?t=60435) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), June 11, 2016 » [Singular Extensions](Singular_Extensions "Singular Extensions")
- [Andscacs 0.86.196 BMI2 is available ...](http://www.talkchess.com/forum/viewtopic.php?t=60500) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), June 15, 2016 » [BMI2](BMI2 "BMI2")
- [Andscacs - New version 0.87](http://www.talkchess.com/forum/viewtopic.php?t=60533) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), June 19, 2016
- [Andscacs - New version 0.872](http://www.talkchess.com/forum/viewtopic.php?t=60913) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 23, 2016
- [Detailed changes in Andscacs from 0.86 to 0.872](http://www.talkchess.com/forum/viewtopic.php?t=60940) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 25, 2016
- [Andscacs, developing version](http://www.talkchess.com/forum/viewtopic.php?t=61795) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), October 22, 2016
- [Andscacs - New version 0.88](http://www.talkchess.com/forum/viewtopic.php?t=61868) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), October 28, 2016

## 2017

- [Andscacs - New version 0.90](http://www.talkchess.com/forum/viewtopic.php?t=63552) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), March 25, 2017
- [Andscacs - New version 0.91](http://www.talkchess.com/forum/viewtopic.php?t=63944) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), May 09, 2017
- [Andscacs new PH feature: first impressions](http://www.talkchess.com/forum/viewtopic.php?t=64557) by [Rodolfo Leoni](index.php?title=Rodolfo_Leoni&action=edit&redlink=1 "Rodolfo Leoni (page does not exist)"), [CCC](CCC "CCC"), July 08, 2017 » [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
- [Andscacs - New version 0.92](http://www.talkchess.com/forum/viewtopic.php?t=65204) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), September 17, 2017
- [Andscacs - New version 0.921 with source](http://www.talkchess.com/forum/viewtopic.php?t=65632) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), November 04, 2017

[Re: Andscacs - New version 0.921 with source](http://www.talkchess.com/forum/viewtopic.php?t=65632&start=63) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 09, 2017 » [TCEC Season 10](TCEC_Season_10 "TCEC Season 10")
[Re: Andscacs - New version 0.921 with source](http://www.talkchess.com/forum/viewtopic.php?t=65632&start=80) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), November 11, 2017

- [Andscacs delta += delta / 3 + 4](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=66142) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), December 27, 2017
- [Andscacs, test version](http://www.talkchess.com/forum/viewtopic.php?t=66189) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), December 31, 2017

## 2018

- [Andscacs - New version 0.93](http://www.talkchess.com/forum/viewtopic.php?t=66320) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), January 14, 2018
- [Andscacs - New version 0.94](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67961) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 11, 2018
- [Andscacs - New version 0.95](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69302) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), December 17, 2018

## 2020

- [Andscacs](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73096) by menniepals, [CCC](CCC "CCC"), February 14, 2020

[Re: Andscacs](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73096&start=6) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), February 15, 2020

- [Andscacs (34 versions) available ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74775) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), August 13, 2020

## 2021

- [Andscacs nnue 0.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76346) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), January 17, 2021 » [NNUE](NNUE "NNUE")

## External Links

## Chess Engine

- [Andscacs Homepage](http://web.archive.org/web/20190808104616/http://andscacs.com/en/en_index.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Andscacs](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Andscacs&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Jorge Retamoza Cuarteto](http://www.retamoza.com.ar/wp/proyectos/jorge-retamoza-cuarteto/) - [La Cachila](https://tango.info/eng/T0370004800), [Andorra Jazz Hivern Fest 2013](http://jazzstamps.blogspot.de/2013/08/jazzstamp-jazz-hivern-andorra.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Claudio Constantini](https://en.wikipedia.org/wiki/Claudio_Constantini), [Alejandro Di Costanzo](http://www.apoloybaco.com/jazz/index.php?option=com_content&view=article&id=2630&Itemid=277), [Hernán Hock](http://www.argentjazz.com.ar/hernan-hock-lleva-su-nuevo-disco-a-boris/), [Jorge Retamoza](http://www.retamoza.com.ar/inicio.htm)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Andscacs Logo based on [Flag of Andorra](https://en.wikipedia.org/wiki/Flag_of_Andorra), from [Andscacs Homepage](http://www.andscacs.com/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [New engine - Andscacs](http://www.talkchess.com/forum/viewtopic.php?t=51182) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), February 06, 2014
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Andscacs - New version](http://www.talkchess.com/forum/viewtopic.php?t=51475&start=11) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), March 03, 2014
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a>  [Andscacs - New version 0.70](http://www.talkchess.com/forum/viewtopic.php?t=54257) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), November 05, 2014
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [New engine - Andscacs](http://www.talkchess.com/forum/viewtopic.php?t=51182) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), February 06, 2014
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Changes in Andscacs 0.70](http://www.talkchess.com/forum/viewtopic.php?t=54290) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), November 08, 2014
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Andscacs - New version 0.80](http://www.talkchess.com/forum/viewtopic.php?t=56030) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 17, 2015
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Trying to improve lazy smp](http://www.talkchess.com/forum/viewtopic.php?t=55970) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 11, 2015
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Andscacs Homepage](http://www.andscacs.com/)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Re: New engine - Andscacs](http://www.talkchess.com/forum/viewtopic.php?t=51182&start=2) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), February 06, 2014

**[Up one level](Engines "Engines")**

