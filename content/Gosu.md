---
title: Gosu
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Gosu**

\[ [Pansori](https://en.wikipedia.org/wiki/Pansori) [Gosu](https://en.wikipedia.org/wiki/Pansori_gosu) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Gosu**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess engine by [Arkadiusz Paterek](Arkadiusz_Paterek "Arkadiusz Paterek"), originated as a part of his masters thesis. In [Korean](https://en.wikipedia.org/wiki/Korean_language) [its name](https://en.wikipedia.org/wiki/Gosu) means expert or master.

## Description

In Arkadiusz Paterek's paper *Modeling of an evaluation function in games* <a id="cite-note-2" href="#cite-ref-2">[2]</a>, referring his thesis *Modeling of an evaluation function in chess*, the [evaluation](Evaluation "Evaluation") is mentioned using a [single-layer perceptron](Neural_Networks#Perceptron "Neural Networks") design inspired by [Michael Buro's](Michael_Buro "Michael Buro") [general linear evaluation model](Michael_Buro#GLEM "Michael Buro") (GLEM) <a id="cite-note-3" href="#cite-ref-3">[3]</a> in the domain of [Othello](Othello "Othello"). Gosu performs [logistic regression](Automated_Tuning#LogisticRegression "Automated Tuning") to optimize weights of corresponding features aka minimize the [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) [loss function](https://en.wikipedia.org/wiki/Loss_function) by [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) over a set of 6.2 million quiet positions from master games. For each position, it squares the difference of an [oracle](Oracle "Oracle") score from the outcome of the game, of 0.999 for a win, 0.5 for a draw, 0.0013 for a loss, and the [dot product](https://en.wikipedia.org/wiki/Dot_product) of the weight and [feature vector](<https://en.wikipedia.org/wiki/Feature_(machine_learning)>), squashed by a [logistic function](https://en.wikipedia.org/wiki/Logistic_function) into a 0.0 to 1.0 range of a [winning probability](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"). To speed up matters after [tuning](Automated_Tuning "Automated Tuning"), an [evaluation cache](Evaluation_Hash_Table "Evaluation Hash Table") is used along with [lazy evaluation](Lazy_Evaluation "Lazy Evaluation"), which performed well in Gosu's [MTD(f)](</MTD(f)> "MTD(f)") framework.

## Tournament Play

Gosu played four [Polish Computer Chess Championships](Polish_Computer_Chess_Championship "Polish Computer Chess Championship"), after a strong debut at the [PCCC 2004](PCCC_2004 "PCCC 2004"), it won the [PCCC 2005](PCCC_2005 "PCCC 2005"), and became third at the [PCCC 2006](PCCC_2006 "PCCC 2006") and played the [IOPCCC 2007](IOPCCC_2007 "IOPCCC 2007") where it lost the final rounds versus later winner [Glaurung](Glaurung "Glaurung") and runner up [WildCat](WildCat "WildCat").
Gosu further performed at the [CCT7](CCT7 "CCT7") with 4½/8.

## Publications

- [Arkadiusz Paterek](Arkadiusz_Paterek "Arkadiusz Paterek") (**2004**). *Modelowanie funkcji oceniającej w szachach*. Masters thesis, [University of Warsaw](University_of_Warsaw "University of Warsaw") (Polish, Modeling of an evaluation function in chess)
- [Arkadiusz Paterek](Arkadiusz_Paterek "Arkadiusz Paterek") (**2004**). *Modelowanie funkcji oceniającej w grach*. [University of Warsaw](University_of_Warsaw "University of Warsaw"), [zipped ps](https://www.mimuw.edu.pl/~paterek/mfog.ps.gz) (Polish, Modeling of an evaluation function in games)

## Forum Posts

## 2004

- [Gosu](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48925) by [Grzegorz Sidorowicz](Grzegorz_Sidorowicz "Grzegorz Sidorowicz"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 15, 2004
- [gosu v.0.2](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48980) by [Arek Paterek](Arkadiusz_Paterek "Arkadiusz Paterek"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 20, 2004
- [Gosu does not find the mate in 1...](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=127) by [Dr. Axel Schumacher](index.php?title=Dr._Axel_Schumacher&action=edit&redlink=1 "Dr. Axel Schumacher (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 03, 2004 » [Checkmate](Checkmate "Checkmate")

## 2005

- [Gauntlet Gosu v0.6 with games](https://www.stmintz.com/ccc/index.php?id=409382) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), February 04, 2005
- [Gauntlet Gosu v0.7 with clear improvement - games](https://www.stmintz.com/ccc/index.php?id=420582) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), April 12, 2005
- [Gosu 0.8](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2422) by Telmo Escobar, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 29, 2005
- [Gauntlet Gosu v0.8 - games](https://www.stmintz.com/ccc/index.php?id=425209) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), May 10, 2005
- [Gauntlet Gosu v0.9 - games - Fafis was removed](https://www.stmintz.com/ccc/index.php?id=428984) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), May 30, 2005

## 2006 ...

- [Problem with new Gosu](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5317) Postby Tony Thomas, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 05, 2006
- [Gosu loosing on time](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5323) by [Volker Pittlik](index.php?title=Volker_Pittlik&action=edit&redlink=1 "Volker Pittlik (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 06, 2006
- [Gosu 0.16 v Thor's Hammer 2.28 (queen sac)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=25286) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), December 06, 2008 » [Thor's Hammer](Thor%27s_Hammer "Thor's Hammer")

## External Links

## Chess Engine

- [Index of /chess/engines/Norbert's collection/Gosu (Compilation)](<http://kirr.homeunix.org/chess/engines/Norbert's%20collection/Gosu%20(Compilation)/>) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")

## Misc

- [Gosu from Wikipedia](https://en.wikipedia.org/wiki/Gosu)
- [Gosu (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Gosu_%28disambiguation%29)

## [Gosu (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Gosu_%28programming_language%29) References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Pansori gosu from Wikipedia](https://en.wikipedia.org/wiki/Pansori_gosu)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Arkadiusz Paterek](Arkadiusz_Paterek "Arkadiusz Paterek") (**2004**). *Modelowanie funkcji oceniającej w grach*. [University of Warsaw](University_of_Warsaw "University of Warsaw"), [zipped ps](https://www.mimuw.edu.pl/~paterek/mfog.ps.gz) (Polish, Modeling of an evaluation function in games)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Michael Buro](Michael_Buro "Michael Buro") (**1998**). *[From Simple Features to Sophisticated Evaluation Functions](http://link.springer.com/chapter/10.1007/3-540-48957-6_8)*. [CG 1998](CG_1998 "CG 1998"), [pdf](https://skatgame.net/mburo/ps/glem.pdf)

**[Up one Level](Engines "Engines")**

