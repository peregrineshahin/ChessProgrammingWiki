---
title: Extensions
---
**[Home](Home "Home") * [Search](Search "Search") * [Selectivity](Selectivity "Selectivity") * Extensions**

Many programs **extend** certain moves to try and find better moves faster, or to resolve tactical "noise" resulting from the [horizon effect](Horizon_Effect "Horizon Effect"). To extend a move, its [search depth](Depth "Depth") (draft) is incremented by some amount, typically one [ply](Ply "Ply").

## Contents

- [1 Inside the Loop](#inside-the-loop)
- [2 Classification](#classification)
- [3 Types](#types)
- [4 Fractional Extensions](#fractional-extensions)
- [5 Conditions/Restrictions](#conditions.2frestrictions)
  - [5.1 Non-reductions](#non-reductions)
- [6 See also](#see-also)
- [7 Publications](#publications)
  - [7.1 1980 ...](#1980-...)
  - [7.2 1990 ...](#1990-...)
  - [7.3 2000 ...](#2000-...)
  - [7.4 2010 ...](#2010-...)
- [8 Forum Posts](#forum-posts)
  - [8.1 1996 ...](#1996-...)
  - [8.2 2000 ...](#2000-...-2)
  - [8.3 2005 ...](#2005-...)
  - [8.4 2010 ...](#2010-...-2)
  - [8.5 2015 ...](#2015-...)
- [9 External Links](#external-links)
  - [9.1 Search Extension](#search-extension)
  - [9.2 Misc](#misc)
- [10 References](#references)

## Inside the Loop

Some extensions may be determined inside the move loop before or after [making the move](Make_Move "Make Move"), the latter case often delayed to the recursively called search routine by some programs:

```C++

for each move m € of all moves {
  makeMove(m);
  int ext = determineExtension( m, depth, node_type, ...); /* 0 or 1 */
  score = -search(ply + 1, depth + ext - 1, -beta, -alpha);
  unmakeMove(m);
  ...
}

```

## Classification

[Bruce Moreland](Bruce_Moreland "Bruce Moreland") has classified extensions as either win-seeking, loss-seeking, or neutral <a id="cite-note-1" href="#cite-ref-1">[1]</a> :

1. Win-seeking extension: If I stop searching now I'll fail low, but I think there might be something good here if I look a little further.
1. Loss-seeking extension: If I stop searching now I'll fail high, but I think I'm in trouble.
1. Neutral extension: This is a forcing sequence, and if I stop searching now I won't know how it ends.

## Types

|  type
|  typical class
|
| --- | --- |
| [Botvinnik-Markoff Extension](Botvinnik-Markoff_Extension "Botvinnik-Markoff Extension") |  loss-seeking
|
| [Capture Extensions](Capture_Extensions "Capture Extensions") |  neutral
|
| [Check Extensions](Check_Extensions "Check Extensions") |  neutral
|
| [Mate Threat Extensions](Mate_Threat_Extensions "Mate Threat Extensions") |  win-seeking
|
| [One Reply Extensions](One_Reply_Extensions "One Reply Extensions") |  loss-seeking
|
| [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") |  neutral
|
| [PV Extensions](PV_Extensions "PV Extensions") |  neutral
|
| [Recapture Extensions](Recapture_Extensions "Recapture Extensions") |  neutral
|
| [Singular Extensions](Singular_Extensions "Singular Extensions") |  neutral
|

## Fractional Extensions

This technique involves passing fractional [depths](Depth "Depth") to the search function. This is typically implemented by defining one [ply](Ply "Ply") to be a number greater than one. Then an extension can be added that does not yet extend the search, but further down the tree may cause an extension when another fractional extension causes the net extension to exceed one ply. Fractional extensions were first described by [David Levy's](David_Levy "David Levy"), [David Broughton's](David_Broughton "David Broughton") and [Mark Taylor's](Mark_Taylor "Mark Taylor") paper on their [SEX Algorithm](SEX_Algorithm "SEX Algorithm"), in conjunction with "negative" extensions aka. fractional reductions and even [LMR](Late_Move_Reductions "Late Move Reductions") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Conditions/Restrictions

Some programs restrict extensions, with either a maximum limit, or via other conditions, such as depth or iteration. Care must be taken so that the search is not extended infinitely (see [search explosion](Search_Explosion "Search Explosion")). Some programs vary the extension based on the expected [node type](Node_Types "Node Types"). For example, in an expected [All-node](Node_Types#ALL "Node Types"), it might use 1/2 a ply extension for a pawn to the 7th, but a full ply on the [PV-node](Node_Types#PV "Node Types") research.

## Non-reductions

In contemporary, heavily reducing programs former typical extensions are often used in an inverted manner: to flag moves as exempt from reductions.

## See also

- [Reductions](Reductions "Reductions")

[Late Move Reductions](Late_Move_Reductions "Late Move Reductions")

- [Pre-Search](Markian_Hlynka#PreSearching "Markian Hlynka")
- [Pruning](Pruning "Pruning")
- [SEX Algorithm](SEX_Algorithm "SEX Algorithm")

## Publications

## 1980 ...

- [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1983**). *Searching to Variable Depth in Computer Chess.* Proceedings of [IJCAI 83](http://www.informatik.uni-trier.de/~ley/db/conf/ijcai/ijcai83.html), pp. 760-762. Karlsruhe. [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-83-VOL-2/PDF/039.pdf)
- [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1988**). *Singular extensions: Adding Selectivity to Brute-Force Searching*. AAAI Spring Symposium, Computer Game Playing, pp. 8-13. Also published in [ICCA Journal, Vol. 11, No. 4](ICGA_Journal#11_4 "ICGA Journal"), republished (1990) in [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1, pp. 99-109. ISSN 0004-3702.
- [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")

## 1990 ...

- [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). *Extension Heuristics*. [ICCA Journal, Vol. 14, No. 2](ICGA_Journal#14_2 "ICGA Journal")
- [Chun Ye](Chun_Ye "Chun Ye") (**1992**). *Experiments in Selective Search Extensions*. MSc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1)
- [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Experiments in Forward Pruning with Limited Extensions.* [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal")
- [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Selective Extensions in Game-Tree Search.* [Heuristic Programming in AI 3](3rd_Computer_Olympiad#Workshop "3rd Computer Olympiad")
- [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1995**). *Quantification of Search-Extension Benefits.* [ICCA Journal, Vol. 18, No. 4](ICGA_Journal#18_4 "ICGA Journal")

## 2000 ...

- [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2001**). *Learning Search Control in Adversary Games*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), pp. 157-174. [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM01b.pdf)
- [Yoshimasa Tsuruoka](Yoshimasa_Tsuruoka "Yoshimasa Tsuruoka"), [Daisaku Yokoyama](Daisaku_Yokoyama "Daisaku Yokoyama"), [Takashi Chikayama](Takashi_Chikayama "Takashi Chikayama") (**2002**). *[Game-Tree Search Algorithm based on Realization Probability](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.2.9258)*. [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.2.9258&rep=rep1&type=pdf), [pdf](http://www-tsujii.is.s.u-tokyo.ac.jp/~tsuruoka/papers/icga02.pdf)
- [David Levy](David_Levy "David Levy") (**2002**) *[SOME COMMENTS ON REALIZATION PROBABILITIES AND THE SEX ALGORITHM](http://ilk.uvt.nl/icga/journal/contents/content25-3.htm#SOME%20COMMENTS%20ON%20REALIZATION%20PROBABILITIES)*. [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal")

## 2010 ...

- [Pálmi Skowronski](index.php?title=P%C3%A1lmi_Skowronski&action=edit&redlink=1 "Pálmi Skowronski (page does not exist)"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Mark Winands](Mark_Winands "Mark Winands") (**2010**). *[Automated Discovery of Search-Extension Features](http://www.sciweavers.org/publications/automated-discovery-search-extension-features)*. [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [pdf](http://www.hr.is/faculty/yngvi/pdf/SkowronskiBW09.pdf) <a id="cite-note-3" href="#cite-ref-3">[3]</a>

## Forum Posts

## 1996 ...

- [Fractional depth increments](https://groups.google.com/d/msg/rec.games.chess.computer/1uVIWZFB41k/VUcAUkzyFd0J) by S. Read, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 18, 1996
- [Crafty V11.3](https://groups.google.com/d/msg/rec.games.chess.computer/tcjwWnFhXt4/ifkLE7GwfSEJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 22, 1996 » [Crafty](Crafty "Crafty")
- ["Suspicious move" extension](https://www.stmintz.com/ccc/index.php?id=12201) by [David Eppstein](David_Eppstein "David Eppstein"), [CCC](CCC "CCC"), November 20, 1997
- [Extensions?!](https://www.stmintz.com/ccc/index.php?id=13993) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 13, 1998
- [Move Extensions](https://www.stmintz.com/ccc/index.php?id=17954) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), May 04, 1998
- [Extend or not extend in a nullmove tree](https://www.stmintz.com/ccc/index.php?id=20167) by [Roland Pfister](Roland_Pfister "Roland Pfister"), [CCC](CCC "CCC"), June 08, 1998 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
- [Selective deepening and Hashtables](https://www.stmintz.com/ccc/index.php?id=21654) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), June 30, 1998
- [search extension](https://www.stmintz.com/ccc/index.php?id=21888) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), July 08, 1998
- [King danger extensions](https://www.stmintz.com/ccc/index.php?id=43380) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), February 16, 1999
- [full-ply search extension leads to crash city!](https://www.stmintz.com/ccc/index.php?id=45304) by [Dave Gomboc](Dave_Gomboc "Dave Gomboc"), [CCC](CCC "CCC"), March 07, 1999
- [Extensions and Futility Pruning](https://www.stmintz.com/ccc/index.php?id=50627) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), May 04, 1999 » [Futility Pruning](Futility_Pruning "Futility Pruning")
- [Q. about Rebel extensions](https://www.stmintz.com/ccc/index.php?id=52090) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), May 18, 1999 » [Rebel](Rebel "Rebel")

## 2000 ...

- [What is the use of extensions?](https://www.stmintz.com/ccc/index.php?id=87191) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 09, 2000
- [No explosions](https://www.stmintz.com/ccc/index.php?id=206802) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), January 11, 2002 » [Search Explosion](Search_Explosion "Search Explosion")
- [Extensions](https://www.stmintz.com/ccc/index.php?id=208272) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), January 18, 2002
- [I need help with Search/Selective Extension](https://www.stmintz.com/ccc/index.php?id=247564) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), August 24, 2002
- [wacnew.epd & single search improvements (extensions)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43060) by [Stefan Knappe](Stefan_Knappe "Stefan Knappe"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 19, 2003 » [Matador](Matador "Matador"), [Win at Chess](Win_at_Chess "Win at Chess")
- [Problem with extending to maxdepth](https://www.stmintz.com/ccc/index.php?id=303131) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), June 26, 2003
- [Evaluation-based Reductions and/or Extensions](https://www.stmintz.com/ccc/index.php?id=338851) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), December 28, 2003 » [Reductions](Reductions "Reductions")
- [extensions + reductions + pruning = confusion](https://www.stmintz.com/ccc/index.php?id=356488) by [Johan de Koning](Johan_de_Koning "Johan de Koning"), [CCC](CCC "CCC"), March 24, 2004 (was [Shredder 8 secret: search depth?](https://www.stmintz.com/ccc/index.php?id=356109))

## 2005 ...

- [Limiting extensions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=1754&p=8190) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 23, 2005 » [GES](GES "GES")
- [Worthless extension ideas...](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4952) by [mjlef](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 06, 2006
- [PVS extension up](http://www.talkchess.com/forum/viewtopic.php?t=14594) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 21, 2007
- [Delaying Extensions Idea (does anyone do this)?](http://www.talkchess.com/forum/viewtopic.php?t=14860) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), July 03, 2007
- [Threat extension](http://www.talkchess.com/forum/viewtopic.php?t=20680) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 15, 2008
- [Search extensions at promising trajectories](http://www.talkchess.com/forum/viewtopic.php?t=21403) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), May 28, 2008
- [extensions](http://www.open-aurec.com/wbforum/viewtopic.php?t=49446) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard programming Forum](Computer_Chess_Forums "Computer Chess Forums"), August 26, 2008
- [Extensions, anyone?](http://www.talkchess.com/forum/viewtopic.php?t=26632) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), February 20, 2009
- [Extensions: everywhere or near the tips?](http://www.talkchess.com/forum/viewtopic.php?t=27017) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), March 15, 2009
- [Stupid Extension Problem/Question](http://www.talkchess.com/forum/viewtopic.php?t=31220) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), December 23, 2009 » [Repetitions](Repetitions "Repetitions")

## 2010 ...

- [Problem with exploding tree because of extensions](http://www.talkchess.com/forum/viewtopic.php?t=31505) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 05, 2010 » [Search Explosion](Search_Explosion "Search Explosion")
- [Restricting extensions to the left most branches?](http://www.talkchess.com/forum/viewtopic.php?t=32940) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), February 27, 2010
- ["Automated Discovery of Search Extensions"](http://www.open-chess.org/viewtopic.php?f=5&t=248) by [Mark Watkins](Mark_Watkins "Mark Watkins"), [OpenChess - Programming and Technical Discussions](Computer_Chess_Forums "Computer Chess Forums"), June 22, 2010
- [Loss-seeking extension/threatened pieces](http://www.talkchess.com/forum/viewtopic.php?t=40984) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), November 03, 2011
- [search extensions](http://www.talkchess.com/forum/viewtopic.php?t=54281) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 08, 2014 » [Singular Extensions](Singular_Extensions "Singular Extensions")

## 2015 ...

- [Adding an Extension Results in Deeper General Search!](http://www.talkchess.com/forum/viewtopic.php?t=56311) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), May 10, 2015 » [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
- [Search extensions](http://www.open-chess.org/viewtopic.php?f=5&t=2968) by ppyvabw, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 17, 2016
- [Extensions in the days of LMR?](http://www.talkchess.com/forum/viewtopic.php?t=59598) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), March 22, 2016 » [LMR](Late_Move_Reductions "Late Move Reductions")
- [Depth extensions and effect on transposition queries](http://www.talkchess.com/forum/viewtopic.php?t=67131) by [Kenneth Jones](index.php?title=Kenneth_Jones&action=edit&redlink=1 "Kenneth Jones (page does not exist)"), [CCC](CCC "CCC"), April 16, 2018 » [Transposition Table](Transposition_Table "Transposition Table")
- [Horizon effect and extensions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67823) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 25, 2018 » [Horizon Effect](Horizon_Effect "Horizon Effect")
- [delaying tactics: prune or extend?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70165) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 10, 2019 » [Selectivity](Selectivity "Selectivity"), [Tactics](Tactics "Tactics")

## External Links

## Search Extension

- [Search Extension](http://web.archive.org/web/20070607151732/www.brucemo.com/compchess/programming/extensions.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
- [Computer Chess Programming Theory - Search Extensions](http://www.frayn.net/beowulf/theory.html#extend) by [Colin Frayn](Colin_Frayn "Colin Frayn")
- [Programming Details - Slow Chess | Extensions Used, Detailed Description](http://www.3dkingdoms.com/chess/implementation.htm) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer") » [Slow Chess](Slow_Chess "Slow Chess")

## Misc

- [Extension from Wikipedia](https://en.wikipedia.org/wiki/Extension)
- [Extension (metaphysics) from Wikipedia](https://en.wikipedia.org/wiki/Extension_%28metaphysics%29)
- [Extension (music) from Wikipedia](https://en.wikipedia.org/wiki/Extension_%28music%29)
- [Jazz chord - Extensions from Wikipedia](https://en.wikipedia.org/wiki/Jazz_chord#Extensions)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Search Extension](http://web.archive.org/web/20070607151732/www.brucemo.com/compchess/programming/extensions.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> ["Automated Discovery of Search Extensions"](http://www.open-chess.org/viewtopic.php?f=5&t=248) by [Mark Watkins](Mark_Watkins "Mark Watkins"), [OpenChess - Programming and Technical Discussions](Computer_Chess_Forums "Computer Chess Forums"), June 22, 2010

**[Up one level](Selectivity "Selectivity")**

