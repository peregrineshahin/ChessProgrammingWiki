---
title: Amazons
---
**[Home](Home "Home") * [Games](Games "Games") * Amazons**

[](File:Amazon2.JPG) Position after 1.d1-d6/g9 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Amazons**, (Game of the Amazons, El Juego de las Amazonas)

a [two-player](https://en.wikipedia.org/wiki/Two-player_game) [abstract strategy game](https://en.wikipedia.org/wiki/Abstract_strategy_game) invented in 1988 by [Walter Zamkauskas](index.php?title=Walter_Zamkauskas&action=edit&redlink=1 "Walter Zamkauskas (page does not exist)") of Argentina <a id="cite-note-2" href="#cite-ref-2">[2]</a> . *El Juego de las Amazonas* is a trademark of [Ediciones de Mente](http://es.wikipedia.org/wiki/Ediciones_de_Mente). In 1998 and 1999, [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") organized the first two computer Amazons championships, which were held at the Computer Games Research Institute of [Shizuoka University](https://en.wikipedia.org/wiki/Shizuoka_University) <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> . Computer Amazons is played at the [Computer Olympiad](Computer_Olympiad "Computer Olympiad") since [London 2000](5th_Computer_Olympiad#Amazons "5th Computer Olympiad"). Amazons is usually played on a 10 x 10 board, but can be played on boards of arbitrary size.

The two players, White and Black are each given four **amazons** in predefined locations. A supply of markers (checkers, poker chips, etc.) is also required. White makes the first move with one of his amazons, which move like a [queen](Queen "Queen") in chess, except captures. Each move contains **two** mandatory parts, moving the amazon and throwing an **arrow** from its [target square](Target_Square "Target Square") to one of its attacked empty squares, which is marked and permanently blocked. Amazon and the arrow can't land on or cross over any own or opponent amazon or arrow. The last player to be able to make a move, which includes throwing an arrow, wins.

## [Computer Olympiads](Computer_Olympiad "Computer Olympiad")

- [5th Computer Olympiad, London 2000](5th_Computer_Olympiad#Amazons "5th Computer Olympiad")
- [6th Computer Olympiad, Maastricht 2001](6th_Computer_Olympiad#Amazons "6th Computer Olympiad")
- [7th Computer Olympiad, Maastricht 2002](7th_Computer_Olympiad#Amazons "7th Computer Olympiad")
- [8th Computer Olympiad, Graz 2003](8th_Computer_Olympiad#Amazons "8th Computer Olympiad")
- [9th Computer Olympiad, Ramat Gan 2004](9th_Computer_Olympiad#Amazons "9th Computer Olympiad")
- [10th Computer Olympiad, Taipei 2005](10th_Computer_Olympiad#Amazons "10th Computer Olympiad")
- [12th Computer Olympiad, Amsterdam 2007](12th_Computer_Olympiad#Amazons "12th Computer Olympiad")
- [13th Computer Olympiad, Beijing 2008](13th_Computer_Olympiad#Amazons "13th Computer Olympiad")
- [14th Computer Olympiad, Pamplona 2009](14th_Computer_Olympiad#Amazons "14th Computer Olympiad")
- [15th Computer Olympiad, Kanazawa 2010](15th_Computer_Olympiad#Amazons "15th Computer Olympiad")
- [16th Computer Olympiad, Tilburg 2011](16th_Computer_Olympiad#Amazons "16th Computer Olympiad")
- [17th Computer Olympiad, Yokohama 2013](17th_Computer_Olympiad#Amazons "17th Computer Olympiad")
- [18th Computer Olympiad, Leiden 2015](18th_Computer_Olympiad#Amazons "18th Computer Olympiad")
- [19th Computer Olympiad, Leiden 2016](19th_Computer_Olympiad#Amazons "19th Computer Olympiad")
- [20th Computer Olympiad, Leiden 2017](20th_Computer_Olympiad#Amazons "20th Computer Olympiad")

## Selected Programs

*Gold medalists from the [Computer Olympiad](Computer_Olympiad "Computer Olympiad")*

- [8 Queens Problem](https://www.game-ai-forum.org/icga-tournaments/program.php?id=164) by [Johan de Koning](Johan_de_Koning "Johan de Koning")
- [Amazong](https://www.game-ai-forum.org/icga-tournaments/program.php?id=253) by [Jens Lieberum](Jens_Lieberum "Jens Lieberum")
- [Invader](https://www.game-ai-forum.org/icga-tournaments/program.php?id=249) by [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz"), et al.

## Photos

## Maastricht 2002

[](https://ilk.uvt.nl/icga/games/amazons/OlympiadMedalWinners%28LorentzLieberumDeKoning%29.JPG)
[Maastricht 2002](7th_Computer_Olympiad#Amazons "7th Computer Olympiad") winners, [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz"), [Jens Lieberum](Jens_Lieberum "Jens Lieberum"), [Johan de Koning](Johan_de_Koning "Johan de Koning") <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## Yokohama 2013

[](https://icga.leidenuniv.nl/?page_id=869)
[Yokohama 2013](17th_Computer_Olympiad "17th Computer Olympiad") award ceremony <a id="cite-note-6" href="#cite-ref-6">[6]</a> , [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz"), [Johan de Koning](Johan_de_Koning "Johan de Koning"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## Branching Factor

*excerpt of [Patrick Hensgens'](index.php?title=Patrick_Hensgens&action=edit&redlink=1 "Patrick Hensgens (page does not exist)") 2001 master's thesis* <a id="cite-note-8" href="#cite-ref-8">[8]</a> :

```C++In the initial position the first player has 2176 possible moves. This is a huge number, especially when compared to other AI games, where most games have a branching factor below 50 in the initial position (e.g., [Chess](Chess "Chess") 20, [Lines of Action](Lines_of_Action "Lines of Action") 36, [Checkers](Checkers "Checkers") 7, [Draughts](Draughts "Draughts") 9). Fortunately the [branching factor](Branching_Factor "Branching Factor") in the game of Amazons decreases rapidly as the game progresses. In the endgame the branching factor is usually below 50.

```

```C++Investigating the average branching factor of Amazons, we encounter a strange phenomenon. From the experiments we performed for finding the average branching factor we observed that this number is quite different for both players. The first player has an average branching factor of 374 while the second player has an average branching factor of 299. This means that to compute the game-tree complexity we need a formula that takes into account that both players have a different branching factor.

```

```C++Furthermore, we observed that the average branching factor for both players increases with decreasing playing strength of both players. 

```

## Selected Publications

<a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a>

## 1999

- [Nobusuke Sasaki](Nobusuke_Sasaki "Nobusuke Sasaki"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**1999**). *Report on the First Open Computer-Amazons Championship*. [ICCA Journal, Vol. 22, No. 1](ICGA_Journal#22_1 "ICGA Journal")

## 2000 ...

- [Patrick Hensgens](index.php?title=Patrick_Hensgens&action=edit&redlink=1 "Patrick Hensgens (page does not exist)"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2000**). *A Knowledge-Based Approach of Amazons*. [5th Computer Olympiad Workshop](5th_Computer_Olympiad#Workshop "5th Computer Olympiad")
- [Michael Buro](Michael_Buro "Michael Buro") (**2000**). *[Simple Amazons Endgames and Their Connection to Hamilton Circuits in Cubic Subgrid Graphs](http://link.springer.com/chapter/10.1007/3-540-45579-5_17)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://skatgame.net/mburo/ps/amaend.pdf)
- [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2000**). *Report on the Second Open Computer-Amazons Championship*. [ICGA Journal, Vol. 23, No. 1](ICGA_Journal#23_1 "ICGA Journal")
- [Elwyn Berlekamp](Elwyn_Berlekamp "Elwyn Berlekamp") (**2000**). *Sums of 2 X N Amazons*. in F. Thomas Bruss and Lucien le Cam, eds. *GameTheory, Optimal Stopping, Probability and Statistics: Papers in honor of Thomas S. Ferguson*. [Institute of Mathematical Statistics Lecture Notes - Monograph Series](http://projecteuclid.org/DPubS?service=UI&version=1.0&verb=Display&handle=euclid.lnms), Vol. 35

**2001**

- [Tsuyoshi Hashimoto](Tsuyoshi_Hashimoto "Tsuyoshi Hashimoto"), [Yoichiro Kajihara](Yoichiro_Kajihara "Yoichiro Kajihara"), [Nobusuke Sasaki](Nobusuke_Sasaki "Nobusuke Sasaki"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jin Yoshimura](Jin_Yoshimura "Jin Yoshimura") (**2001**). *An Evaluation Function for Amazons*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
- [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2001**). *Solving 5x5 Amazons*. [6th Game Programming Workshop](Conferences#GPW "Conferences")
- [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2001**). *8QP wins Amazons tournament*. [ICGA Journal, Vol. 24, No. 3](ICGA_Journal#24_3 "ICGA Journal") » [6th Computer Olympiad](6th_Computer_Olympiad#Amazons "6th Computer Olympiad")
- [Patrick Hensgens](index.php?title=Patrick_Hensgens&action=edit&redlink=1 "Patrick Hensgens (page does not exist)") (**2001**). *A Knowledge-based Approach of the Game of Amazons*. Master's thesis, [Maastricht University](Maastricht_University "Maastricht University"), [pdf](http://www.personeel.unimaas.nl/uiterwijk/Theses/MSc/Hensgens_thesis.pdf)

**2002**

- [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**2002**). *First-time entry Amazong wins Amazons tournament*. [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal") » [7th Computer Olympiad](7th_Computer_Olympiad#Amazons "7th Computer Olympiad")
- [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**2002**). *Finding Territory in Amazons*. [7th Computer Olympiad Workshop](7th_Computer_Olympiad#Workshop "7th Computer Olympiad")
- [Raymond Georg Snatzke](index.php?title=Raymond_Georg_Snatzke&action=edit&redlink=1 "Raymond Georg Snatzke (page does not exist)") (**2002**). *Exhaustive search in the game amazons*. in [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski") (ed) (**2002**). *[More Games of No Chance](http://library.msri.org/books/Book42/)*. [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press), [pdf](http://library.msri.org/books/Book42/files/snatzke.pdf)
- [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Theodore Tegos](index.php?title=Theodore_Tegos&action=edit&redlink=1 "Theodore Tegos (page does not exist)") (**2002**). *Experiments in Computer Amazons*. in [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski") (ed) (**2002**). *[More Games of No Chance](http://library.msri.org/books/Book42/)*. [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
- [Henry Avetisyan](index.php?title=Henry_Avetisyan&action=edit&redlink=1 "Henry Avetisyan (page does not exist)"), [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**2002**). *[Selective Search in an Amazons Program](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_9)*. [CG 2002](CG_2002 "CG 2002")
- [Theodore Tegos](index.php?title=Theodore_Tegos&action=edit&redlink=1 "Theodore Tegos (page does not exist)") (**2002**). *Shooting the last arrow*. Master's thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://webdocs.cs.ualberta.ca/~jonathan/PREVIOUS/Grad/tegos.msc.pdf)

**2003**

- [Jens Lieberum](Jens_Lieberum "Jens Lieberum") (**2003**). *Amazong wins Amazons tournament*. [ICGA Journal, Vol. 26, No. 4](ICGA_Journal#26_4 "ICGA Journal") » [8th Computer Olympiad](8th_Computer_Olympiad#Amazons "8th Computer Olympiad")
- [Jens Lieberum](Jens_Lieberum "Jens Lieberum") (**2003**). *[An Evaluation Function for the Game of Amazons](http://www.sciencedirect.com/science/article/pii/S0304397505005979)*. [Advances in Computer Games 10](Advances_in_Computer_Games_10 "Advances in Computer Games 10")

**2004**

- [Akop Karapetyan](index.php?title=Akop_Karapetyan&action=edit&redlink=1 "Akop Karapetyan (page does not exist)"), [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**2004**). *[Generating an Opening Book for Amazons](http://link.springer.com/chapter/10.1007/11674399_11)*. [CG 2004](CG_2004 "CG 2004")
- [Johan de Koning](Johan_de_Koning "Johan de Koning") (**2004**). *8QP regains Amazons title*. [ICGA Journal, Vol. 27, No. 3](ICGA_Journal#27_3 "ICGA Journal") » [9th Computer Olympiad](9th_Computer_Olympiad#Amazons "9th Computer Olympiad")
- [Raymond Georg Snatzke](index.php?title=Raymond_Georg_Snatzke&action=edit&redlink=1 "Raymond Georg Snatzke (page does not exist)") (**2004**). *New results of exhaustive search in the game Amazons*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol. 303, No. 3

## 2005 ...

- [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**2005**). *8QP wins Amazons tournament*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal") » [10th Computer Olympiad](10th_Computer_Olympiad#Amazons "10th Computer Olympiad")
- [Yoshinori Higashiuchi](index.php?title=Yoshinori_Higashiuchi&action=edit&redlink=1 "Yoshinori Higashiuchi (page does not exist)"), [Reijer Grimbergen](Reijer_Grimbergen "Reijer Grimbergen") (**2005**). *[Enhancing Search Efficiency by Using Move Categorization Based on Game Progress in Amazons](http://link.springer.com/chapter/10.1007/11922155_6)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11")
- [Jens Lieberum](Jens_Lieberum "Jens Lieberum") (**2005**). *An evaluation function for the game of Amazons*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol. 349, No. 2
- [Julien Kloetzer](index.php?title=Julien_Kloetzer&action=edit&redlink=1 "Julien Kloetzer (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Bruno Bouzy](Bruno_Bouzy "Bruno Bouzy") (**2007**). *The Monte-Carlo approach in Amazons*. [CGW 2007](CGW_2007 "CGW 2007"), [pdf](http://www.mi.parisdescartes.fr/~bouzy/publications/KIB-MCAmazons-CGW07.pdf)
- [Mark Winands](Mark_Winands "Mark Winands") (**2007**). *8QP wins Amazons tournament*. [ICGA Journal, Vol. 30, No. 3](ICGA_Journal#30_3 "ICGA Journal") » [12th Computer Olympiad](12th_Computer_Olympiad#Amazons "12th Computer Olympiad")
- [Julien Kloetzer](index.php?title=Julien_Kloetzer&action=edit&redlink=1 "Julien Kloetzer (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Bruno Bouzy](Bruno_Bouzy "Bruno Bouzy") (**2008**). *A Comparative Study of Solvers for Amazons Endgames*. [CIG'08](http://www.csse.uwa.edu.au/cig08/Proceedings/toc.html), [pdf](http://www.csse.uwa.edu.au/cig08/Proceedings/papers/8033.pdf)
- [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**2008**). *[Amazons Discover Monte-Carlo](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_2)*. [CG 2008](CG_2008 "CG 2008")
- [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**2009**). *Invader wins Amazons Tournament*. [ICGA Journal, Vol. 32, No. 1](ICGA_Journal#32_1 "ICGA Journal") » [13th Computer Olympiad](13th_Computer_Olympiad#Amazons "13th Computer Olympiad")
- [Julien Kloetzer](index.php?title=Julien_Kloetzer&action=edit&redlink=1 "Julien Kloetzer (page does not exist)") (**2009**). *Invader wins Amazons Tournament*. [ICGA Journal, Vol. 32, No. 2](ICGA_Journal#32_2 "ICGA Journal") » [14th Computer Olympiad](14th_Computer_Olympiad#Amazons "14th Computer Olympiad")
- [Julien Kloetzer](index.php?title=Julien_Kloetzer&action=edit&redlink=1 "Julien Kloetzer (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Bruno Bouzy](Bruno_Bouzy "Bruno Bouzy") (**2009**). *Playing Amazons Endgames*. [ICGA Journal, Vol. 32, No. 3](ICGA_Journal#32_3 "ICGA Journal"), [pdf](http://www.math-info.univ-paris5.fr/%7Ebouzy/publications/Kloetzer-AmazonsEndgames-ICGAJournal-Sep2009.pdf)

## 2010 ...

- [Julien Kloetzer](index.php?title=Julien_Kloetzer&action=edit&redlink=1 "Julien Kloetzer (page does not exist)") (**2010**). *Monte-Carlo Opening Books for Amazons*. [CG 2010](CG_2010 "CG 2010")
- [Julien Kloetzer](index.php?title=Julien_Kloetzer&action=edit&redlink=1 "Julien Kloetzer (page does not exist)") (**2010**). *[Monte-Carlo Techniques: Applications to the Game of the Amazons](https://dspace.jaist.ac.jp/dspace/handle/10119/8867?locale=en)*. Ph.D. thesis, [JAIST](JAIST "JAIST")
- [Johan de Koning](Johan_de_Koning "Johan de Koning") (**2011**). *Invader prolongs Amazons Title*. [ICGA Journal, Vol. 34, No. 2](ICGA_Journal#34_2 "ICGA Journal") » [15th Computer Olympiad](15th_Computer_Olympiad#Amazons "15th Computer Olympiad")
- [Johan de Koning](Johan_de_Koning "Johan de Koning") (**2012**). *Invader wins Amazons Tournament*. [ICGA Journal, Vol. 35, No. 4](ICGA_Journal#35_4 "ICGA Journal") » [16th Computer Olympiad](16th_Computer_Olympiad#Amazons "16th Computer Olympiad")
- [Jiaxing Song](index.php?title=Jiaxing_Song&action=edit&redlink=1 "Jiaxing Song (page does not exist)") (**2013**). *An enhanced solver for the game of Amazons*. Master's thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/files/00000038x/Song_Jiaxing_Spring2013.pdf)
- [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**2013**). *INVADER Wins Amazons Tournament*. [ICGA Journal, Vol. 36, No. 4](ICGA_Journal#36_4 "ICGA Journal") » [17th Computer Olympiad](17th_Computer_Olympiad#Amazons "17th Computer Olympiad")

## 2015 ...

- [Jiaxing Song](index.php?title=Jiaxing_Song&action=edit&redlink=1 "Jiaxing Song (page does not exist)"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2015**). *An Enhanced Solver for the Game of Amazons*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 7, No. 1, [pdf preprint](https://webdocs.cs.ualberta.ca/~mmueller/ps/2014/2014-TCIAIG-amazons_solver-preprint.pdf)
- [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**2017**). *Invader wins eighth Amazons gold medal*. [ICGA Journal, Vol. 39, Nos. 3-4](ICGA_Journal#39_34 "ICGA Journal") » [20th Computer Olympiad 2017](20th_Computer_Olympiad#Amazons "20th Computer Olympiad")

## External Links

## Game

- [ICGA: Amazons](http://icga.leidenuniv.nl/icga/games/amazons/) by [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz")
- [Amazons (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/game.php?id=15)
- [Game of the Amazons from Wikipedia](https://en.wikipedia.org/wiki/Game_of_the_Amazons)
- [Amazons](http://www.chessvariants.org/other.dir/amazons.html) from [The Chess Variant Pages](http://www.chessvariants.org/Gindex.html)
- [Tabletop: Amazons](http://www.tbltop.com/2009/05/amazons.html)
- [Research Related to the Game of Amazons](http://webdocs.cs.ualberta.ca/~mmueller/amazons/index.html) by [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [University of Alberta](University_of_Alberta "University of Alberta")
- [Invader - A Program that Plays the Game of Amazons](http://www.csun.edu/~lorentz/amazon.htm) by [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz")

## Misc

- [Amazon (Fairy chess piece) from Wikipedia](https://en.wikipedia.org/wiki/Amazon_%28chess%29)
- [Amazons (female warriors) from Wikipedia](https://en.wikipedia.org/wiki/Amazons)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Game of the Amazons from Wikipedia](https://en.wikipedia.org/wiki/Game_of_the_Amazons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Game of the Amazons from Wikipedia](https://en.wikipedia.org/wiki/Game_of_the_Amazons)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Nobusuke Sasaki](Nobusuke_Sasaki "Nobusuke Sasaki"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**1999**). *Report on the First Open Computer-Amazons Championship*. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 22, No. 1
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2000**). *Report on the Second Open Computer-Amazons Championship*. [ICGA Journal](ICGA_Journal "ICGA Journal"), Vol 23, No. 1
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [ICGA: Amazons](https://ilk.uvt.nl/icga/games/amazons/) by [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Games Tournament 2013 - Amazons](https://icga.leidenuniv.nl/?page_id=627#amazons), [ICGA](ICGA "ICGA")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Photos 2013 Events: day 6](https://icga.leidenuniv.nl/?page_id=869), [ICGA](ICGA "ICGA")
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Patrick Hensgens](index.php?title=Patrick_Hensgens&action=edit&redlink=1 "Patrick Hensgens (page does not exist)") (**2001**). *A Knowledge-based Approach of the Game of Amazons*. Master's thesis, [Maastricht University](Maastricht_University "Maastricht University"), [pdf](http://www.personeel.unimaas.nl/uiterwijk/Theses/MSc/Hensgens_thesis.pdf)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Publications related to the game of Amazons](http://webdocs.cs.ualberta.ca/~mmueller/amazons/amazons-publications.html), [University of Alberta](University_of_Alberta "University of Alberta")
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [ICGA: Amazons](https://ilk.uvt.nl/icga/games/amazons/) by [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz")

**[Up one Level](Games "Games")**

