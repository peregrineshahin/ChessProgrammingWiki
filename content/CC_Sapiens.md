---
title: CC Sapiens
---
**[Home](Home "Home") * [Engines](Engines "Engines") * CC Sapiens**

\[ Wisdom Emblem <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**CC Sapiens**, (Chess Computer Sapiens)

a computer chess project headed by [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") during the early 90s after the [dissolution of the Soviet Union](https://en.wikipedia.org/wiki/Dissolution_of_the_Soviet_Union). Further contributors, specially on the application of [economic planning](https://en.wikipedia.org/wiki/Economic_planning) (EC Sapiens) were mathematician [Vasily Vladimirov](Vasily_Vladimirov "Vasily Vladimirov"), and the economists [Evgeniĭ Dmitrievich Cherevik](Evgeni%C4%AD_Dmitrievich_Cherevik "Evgeniĭ Dmitrievich Cherevik") and [Vitaly Vygodsky](Vitaly_Vygodsky "Vitaly Vygodsky").
CC Sapiens was a trial to resurrect the [Pioneer](Pioneer "Pioneer") project with the aim to develop a chess program to model a Chess Master's Mind - ultimately terminated with Botvinnik's death in May 1995. Botvinnik's attempt to demonstrate the ability of CC Sapiens on three selected positions with narrow [search trees](Search_Tree "Search Tree") in [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal") <a id="cite-note-2" href="#cite-ref-2">[2]</a> was criticized by [Hans Berliner](Hans_Berliner "Hans Berliner") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> and Botvinnik's old chess rival [David Bronstein](David_Bronstein "David Bronstein") <a id="cite-note-5" href="#cite-ref-5">[5]</a>, due to obvious flaws and allegation of forged results <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Contents

- [1 A Muse A-Musing](#a-muse-a-musing)
- [2 Kasparov - Ribli](#kasparov---ribli)
- [3 Solving Shannon's Problem](#solving-shannon.27s-problem)
  - [3.1 Abstract](#abstract)
  - [3.2 Chains](#chains)
- [4 See also](#see-also)
- [5 Selected Publications](#selected-publications)
- [6 Forum Posts](#forum-posts)
- [7 External Links](#external-links)
  - [7.1 Chess Program](#chess-program)
  - [7.2 Misc](#misc)
- [8 References](#references)

## A Muse A-Musing

Excerpt of the Editorial, [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal") by [Bob Herschberg](Bob_Herschberg "Bob Herschberg") and [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") <a id="cite-note-7" href="#cite-ref-7">[7]</a>:

```C++
[Controversy](https://en.wikipedia.org/wiki/Controversy) is not only not harmful, it is the only way to recognize the eventual [truth](https://en.wikipedia.org/wiki/Truth) which is fated to have its origin as a dispute between [heretics](https://en.wikipedia.org/wiki/Heretic_%28disambiguation%29) and the current [orthodoxy](https://en.wikipedia.org/wiki/Orthodoxy), the latter only recently absolved itself from the charge of [heresy](https://en.wikipedia.org/wiki/Heresy). It is therefore that we welcome an unusual amount of controversy arising out of the last issue of our Journal. Whether it is Botvinnik being challenged by Berliner, or by his former comrade-in-arms, Bronstein, whether it is one of your Editors taking up the cudgels against proponents of Chinese Chess-by-program, a double heresy, - all are welcome. Their discussions may not be among the most edifying of exchanges - well, neither was the language in which heresy was discussed and orthodoxy arrived at on many famous occasions, Church counsels among them.

```

```C++
Yet, we maintain: the discussion, even the confrontation is helpful and conducive to the health of computer chess. Following this belief, we feel a duty to extend the hospitality of our columns generously to all heretics. [Caïssa](https://en.wikipedia.org/wiki/Ca%C3%AFssa), still smiling, will be amused.  

```

## Kasparov - Ribli

The first one of Botvinnik's *Three Positions* <a id="cite-note-8" href="#cite-ref-8">[8]</a> and most criticized analysis is from the [Garry Kasparov](Garry_Kasparov "Garry Kasparov") vs. [Zoltán Ribli](https://en.wikipedia.org/wiki/Zolt%C3%A1n_Ribli) game <a id="cite-note-9" href="#cite-ref-9">[9]</a>, [Skellefteå](https://en.wikipedia.org/wiki/Skellefte%C3%A5) [World Cup 1989](https://en.wikipedia.org/wiki/1989_in_chess#Grandmasters_Association_World_Cup) <a id="cite-note-10" href="#cite-ref-10">[10]</a>, after 26.Rxb5 Bxe3 <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a>:

|  |
| --- |
|                                                                                    ♜♚      ♟♟♟♟ ♕ ♟    ♖      ♛           ♝ ♙ ♙  ♖♙♙ ♙      ♔  |

```C++
5rk1/5ppp/p1Q1p3/1R6/q7/4b1P1/P2RPP1P/6K1 w - - 

```

CC Sapiens produced an analysis of a mere 18 nodes, and determined that this position is a win for White with Rd8. Botvinnik gives one variation with 1.Rd8! Qxb5 2.Qd6! Bxf2 3.Kxf2 Re8 4.Qe7, satisfying the stated goal, but missed to consider other alternatives of Black's first (1... Bxf2) and third move. Berliner: "Presumably the beckoning 3. ...Qf5+ is dismissed since it can't possibly lead to a win for Black. Botvinnik knows that, and I know that, but can a computer program figure this out without searching?". The blunder 4.Qe7 was apparently discovered by Botvinnik or his team just before press time, given in a footnote, but due to mistake of the editors, three pages apart.

[Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), who already analyzed the position with [Deep Thought](Deep_Thought "Deep Thought") along with [Garry Kasparov](Garry_Kasparov "Garry Kasparov") in 1990, posted the winning lines of 3. ... Re8 4.a4 or more difficult 3 ...Qf5+! 4.Kg1! in [rgc](Computer_Chess_Forums "Computer Chess Forums") <a id="cite-note-13" href="#cite-ref-13">[13]</a> as reply to Berliner's [B\*](B* "B*") [HiTech](HiTech "HiTech") analysis with the wrong 3 ...Qf5+! 4.Kg2 line <a id="cite-note-14" href="#cite-ref-14">[14]</a>. As admitted by Berliner in his *Playing Computer Chess in the Human Style* [ICCA](ICCA "ICCA") correspondence <a id="cite-note-15" href="#cite-ref-15">[15]</a>, it was possible to identify a serious bug in B\* HiTech's [search](Search "Search") algorithm thanks to Hsu's information.

## Solving Shannon's Problem

## Abstract

from *Solving Shannon's Problem: Ways and Means*, [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), July 01, 1993 <a id="cite-note-16" href="#cite-ref-16">[16]</a> <a id="cite-note-17" href="#cite-ref-17">[17]</a>:

```C++
A proposal by [Shannon](Claude_Shannon "Claude Shannon") (1950) indicated two styles of constructing computer-chess programs: [brute-force](Brute-Force "Brute-Force") and following the experience of chess masters. Of the first style examples abound, of the second only CC Sapiens, as yet incomplete, exists. From the experience with CC Sapiens and its economical analogue, it is confidently predicted that methods based on making the computer *understand* the problem may well gain the upper hand, both in computer chess and in high-dimensional search programs related to it, following the master's style. 

```

## Chains

Excerpt from *Solving Shannon's Problem: Ways and Means*:

```C++
In the program CC Sapiens, the intermediate step of the model is identified with the analysis of a chain of [pieces](Pieces "Pieces"). An attacking piece L0 and an attacked piece L2 constitute the basis of the chain; the remaining pieces oppose or support it. Whereas a chain of pieces connects material entities, there is also, as an intermediate step, a positional chain. The latter is composed of links relating [squares](Squares "Squares") to specific other squares, such as [holes](Holes "Holes") and weak squares, and to properties enjoyed by the totality of squares and their subsets, such as [ranks](Ranks "Ranks"), [files](Files "Files") and [diagonals](Diagonals "Diagonals"). 

```

## See also

- [Pioneer](Pioneer "Pioneer")

## Selected Publications

<a id="cite-note-18" href="#cite-ref-18">[18]</a>

- [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") (**1993**). *Three Positions*. [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal")
- [Bob Herschberg](Bob_Herschberg "Bob Herschberg"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1993**). *[A Muse A-Musing](http://ilk.uvt.nl/icga/journal/contents/node4.html)*. (Editorial) [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1993**). *Playing Computer Chess in the Human Style*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
- [David Bronstein](David_Bronstein "David Bronstein") (**1993**). *Mimicking Human Oversight*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
- [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik"), [Evgeniĭ Dmitrievich Cherevik](Evgeni%C4%AD_Dmitrievich_Cherevik "Evgeniĭ Dmitrievich Cherevik"), [Vasily Vladimirov](Vasily_Vladimirov "Vasily Vladimirov"), [Vitaly Vygodsky](Vitaly_Vygodsky "Vitaly Vygodsky") (**1994**). *Solving Shannon's Problem: Ways and Means*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), English translation by Igor Botvinnik <a id="cite-note-19" href="#cite-ref-19">[19]</a> <a id="cite-note-20" href="#cite-ref-20">[20]</a> and the Editors

## Forum Posts

- [Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/83d0wqxy-VoJ) by [Hans Berliner](Hans_Berliner "Hans Berliner"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 9, 1993

[Re: Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/nZWR2BkOlFsJ) by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 10, 1993

- [Botvinnik article](https://groups.google.com/d/msg/rec.games.chess.computer/ZWQ5ZwvXx_s/EgXPrz6jZFYJ) by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 23, 1996

## [Re: Botvinnik article](https://groups.google.com/d/msg/rec.games.chess.computer/ZWQ5ZwvXx_s/Cozl-N5kZkMJ) by [Peter Gillgasch](Peter_Gillgasch "Peter Gillgasch"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 23, 1996 External Links

## Chess Program

- [Hans Berliner against Mikhail Botvinnik](http://atimopheyev.narod.ru/AfterPIONEER/info/PIONEER/2-Berliner.htm) by [Alexander Timofeev](Alexander_Timofeev "Alexander Timofeev")

## Misc

- [sapiens - Wiktionary](https://en.wiktionary.org/wiki/sapiens)
- [Sapiens from Wikipedia](https://en.wikipedia.org/wiki/Sapiens)
- [Sapience from Wikipedia](https://en.wikipedia.org/wiki/Wisdom#Sapience)
- [Homo sapiens from Wikipedia](https://en.wikipedia.org/wiki/Homo_sapiens)
- [RoboSapien from Wikipedia](https://en.wikipedia.org/wiki/RoboSapien)
- [FemiSapien from Wikipedia](https://en.wikipedia.org/wiki/FemiSapien)
- [Endgame – the mating habits of homo sapiens](http://en.chessbase.com/post/endgame-the-mating-habits-of-homo-sapiens) | [ChessBase News](ChessBase "ChessBase"), April 08, 2004
- [Nuno Ferreira Septeto](https://nunoferreirajazz.wordpress.com/) - Cromo Sapiens, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Wisdom Emblem](https://commons.wikimedia.org/wiki/File:Wither_-_Emblem_Wisdom.jpg), from [George Wither](https://en.wikipedia.org/wiki/George_Wither) (**1635**). *[A Collection of Emblemes Anciente and Moderne](https://archive.org/details/collectionofembl00withe)*. London, [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Wisdom from Wikipedia.simple](http://simple.wikipedia.org/wiki/Wisdom): The words of this old print read, in modern English: 'He over all the stars does reign That unto wisdom can attain', in other words: 'Whoever can become wise will rule over everything'.
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") (**1993**). *Three Positions*. [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1993**). *Playing Computer Chess in the Human Style*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/83d0wqxy-VoJ) by [Hans Berliner](Hans_Berliner "Hans Berliner"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 9, 1993
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [David Bronstein](David_Bronstein "David Bronstein") (**1993**). *Mimicking Human Oversight*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Botvinnik article](https://groups.google.com/d/msg/rec.games.chess.computer/ZWQ5ZwvXx_s/EgXPrz6jZFYJ) by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 23, 1996
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a>  [Bob Herschberg](Bob_Herschberg "Bob Herschberg"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1993**). *[A Muse A-Musing](http://ilk.uvt.nl/icga/journal/contents/node4.html)*. (Editorial) [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") (**1993**). *Three Positions*. [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal")
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Garry Kasparov vs Zoltan Ribli (1989)](http://www.chessgames.com/perl/chessgame?gid=1070471) from [chessgames.com](http://www.chessgames.com/index.html)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Skelleftea World Cup 1989](http://www.chessgames.com/perl/chesscollection?cid=1015939) from [chessgames.com](http://www.chessgames.com/index.html)
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Kasparov-Ribli, 1989](https://www.stmintz.com/ccc/index.php?id=46260) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), March 19, 1999
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Test position ==> Kasparov-Ribli,1989](https://www.stmintz.com/ccc/index.php?id=201865) by [José Antônio Fabiano Mendes](Jos%C3%A9_Ant%C3%B4nio_Fabiano_Mendes "José Antônio Fabiano Mendes"), [CCC](CCC "CCC"), December 14, 2001
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Re: Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/nZWR2BkOlFsJ) by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 10, 1993
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/83d0wqxy-VoJ) by [Hans Berliner](Hans_Berliner "Hans Berliner"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 9, 1993
1. <a id="cite-ref-15" href="#cite-note-15">[15]</a>  [Hans Berliner](Hans_Berliner "Hans Berliner") (**1993**). *Playing Computer Chess in the Human Style*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
1. <a id="cite-ref-16" href="#cite-note-16">[16]</a>  [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik"), [Evgeniĭ Dmitrievich Cherevik](Evgeni%C4%AD_Dmitrievich_Cherevik "Evgeniĭ Dmitrievich Cherevik"), [Vasily Vladimirov](Vasily_Vladimirov "Vasily Vladimirov"), [Vitaly Vygodsky](Vitaly_Vygodsky "Vitaly Vygodsky") (**1994**). *Solving Shannon's Problem: Ways and Means*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
1. <a id="cite-ref-17" href="#cite-note-17">[17]</a> [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](https://www.pi.infn.it/~carosi/chess/shannon.txt)*.
1. <a id="cite-ref-18" href="#cite-note-18">[18]</a> [ICGA Reference Database](ICGA_Journal#RefDB "ICGA Journal")
1. <a id="cite-ref-19" href="#cite-note-19">[19]</a> [Igor Botvinnik Has Passed Away](http://chess-news.ru/en/node/5190) | [chess-news.ru](http://chess-news.ru/en), December 06, 2011
1. <a id="cite-ref-20" href="#cite-note-20">[20]</a> [Interview mit Igor Botvinnik](http://de.chessbase.com/post/interview-mit-igor-botvinnik), [ChessBase](ChessBase "ChessBase"), January 04, 2007 (German)

**[Up one Level](Engines "Engines")**

