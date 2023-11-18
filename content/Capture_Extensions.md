---
title: Capture Extensions
---

**[Home](Main_Page "Main Page") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* [Extensions](Extensions "Extensions") \* Capture Extensions**

**Capture Extensions** were used early in [brute-force](Brute-Force "Brute-Force") chess programs to minimize some [horizon effects](Horizon_Effect "Horizon Effect"). Due to the self-restricting nature of [captures](Captures "Captures") in Chess (max. 30 pieces may be captured per game), one may consider this a good idea. However, extending every capture was discarded by most programmers, and some constrains or conditions were applied, i.e. to extend only forced [recaptures](Recapture_Extensions "Recapture Extensions") on the same [target square](Target_Square "Target Square").

[Hans Berliner](Hans_Berliner "Hans Berliner") suggested to extend only those (re)captures, which restore the [material balance](Material#Balance "Material") at the [root](Root "Root"). Furthermore, capture extensions are often restricted to [PV-nodes](Node_Types#PV "Node Types"), or some programs assign [fractional extensions](Extensions#FractionalExtensions "Extensions") to different kinds of captures, considering [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), [distance](Distance "Distance") of target square to the opponent [king](King "King"), recapturing on the same square, and material balance as mentioned.

A lot of todays programs, more focused on [reductions](Reductions "Reductions") rather than extensions in the [Scout](Scout "Scout") part of their [PVS](Principal_Variation_Search "Principal Variation Search"), most often don't reduce captures, which makes it a kind of implicit extension relative to reduced late [quiet moves](Quiet_Moves "Quiet Moves"). It also seems worth a try to reduce even captures with negative SEE while performing [LMR](Late_Move_Reductions "Late Move Reductions").

However, it seems important to extend captures if a transition to certain late endgames occurs. [Ed Schröder](Ed_Schroder "Ed Schroder") for instance extends **three** [plies](Ply "Ply") in [Rebel](Rebel "Rebel") if entering the [pawn endgame](Pawn_Endgame "Pawn Endgame"), and the static, [incremental updated](Incremental_Updates "Incremental Updates") [score](Score "Score") dominated by [material](Material "Material") is not outside a +-3 pawn window around zero: The extension is very powerful, it will often avoid REBEL entering a lost ending and vice versa.

## See also

*   [Check Extensions](Check_Extensions "Check Extensions")
*   [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
*   [Zwischenzug](Zwischenzug "Zwischenzug")

## Publications

*   [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). _The SEX Algorithm in Computer Chess_. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 12, No. 1, pp. 10-21.
*   [Don Beal](Don_Beal "Don Beal") and [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1995**). _Quantification of Search-Extension Benefits._ [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 18, No. 4, pp. 205-218.
*   [Yoshimasa Tsuruoka](Yoshimasa_Tsuruoka "Yoshimasa Tsuruoka"), [Daisaku Yokoyama](Daisaku_Yokoyama "Daisaku Yokoyama"), [Takashi Chikayama](Takashi_Chikayama "Takashi Chikayama") (**2002**). _[Game-Tree Search Algorithm based on Realization Probability](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.2.9258)_. [ICGA Journal](ICGA_Journal "ICGA Journal"), Vol. 25, No. 3, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.2.9258&rep=rep1&type=pdf), [pdf](http://www-tsujii.is.s.u-tokyo.ac.jp/~tsuruoka/papers/icga02.pdf)
*   [David Levy](David_Levy "David Levy") (**2002**) _[SOME COMMENTS ON REALIZATION PROBABILITIES AND THE SEX ALGORITHM](http://ilk.uvt.nl/icga/journal/contents/content25-3.htm#SOME%20COMMENTS%20ON%20REALIZATION%20PROBABILITIES)_. [ICGA Journal](ICGA_Journal "ICGA Journal"), Vol. 25, No. 3

## Forum Posts

*   [Capture/recapture extensions](https://www.stmintz.com/ccc/index.php?id=35984) by [Andrew Williams](Andrew_Williams "Andrew Williams"), [CCC](CCC "CCC"), December 14, 1998
*   [Search extensions at promising trajectories](http://www.talkchess.com/forum/viewtopic.php?t=21403) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), May 28, 2008

## External Links

*   [Search Extension](http://web.archive.org/web/20070607151732/www.brucemo.com/compchess/programming/extensions.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)

**[Up one Level](Extensions "Extensions")**