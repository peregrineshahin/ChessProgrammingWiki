---
title: Futility PruningMoveCountBasedPruning
---
**[Home](Home "Home") * [Search](Search "Search") * [Selectivity](Selectivity "Selectivity") * [Pruning](Pruning "Pruning") * Futility Pruning**

[](http://www.mcescher.com/Gallery/back-bmp/LW389.jpg) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Relativity, 1953 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Futility Pruning**,

in its pure form implemented at the [frontier nodes](Frontier_Nodes "Frontier Nodes") ([depth](Depth "Depth") == 1) with one [ply](Ply "Ply") left to the horizon. It discards the moves that have no potential of raising [alpha](Alpha "Alpha"), which in turn requires some estimate of a potential value of a move. This is calculated by adding a futility margin (representing the largest conceivable positional gain) to the evaluation of the current position. If this does not exceed alpha then the futility pruning is triggered to skip this move (which further means setting a flag like *f_prune = 1* to indicate not all moves were tried).

## Conditions

For [tactical](Tactics "Tactics") stability, even in such a node we ought to search the following moves:

- [captures](Captures "Captures") (either all or less typically only those that are capable of raising the score above alpha + margin)
- moves that give [check](Check "Check")

Futility pruning is not used when the [side to move](Side_to_move "Side to move") is in [check](Check "Check") , or when either [alpha](Alpha "Alpha") or [beta](Beta "Beta") are close to the [mate value](Checkmate#MateScore "Checkmate"), since it would leave the program blind to certain [checkmates](Checkmate "Checkmate"). [Tord Romstad](Tord_Romstad "Tord Romstad") reported that in his early program [Gothmog](Gothmog "Gothmog") one more condition was necessary - namely that futility pruning requires checking for the existence of at least one legal move <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> to avoid returning erroneous stalemate scores. As replied by [Omid David](Eli_David "Eli David"): then simply return alpha (to fail [low](Fail-Low "Fail-Low") but [hard](Fail-Hard "Fail-Hard")).

## Extended Futility Pruning

[Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") advocated using so-called **extended futility pruning** <a id="cite-note-4" href="#cite-ref-4">[4]</a>. It means employing similar algorithm at [pre frontier nodes](Pre_Frontier_Node "Pre Frontier Node") at depth == 2, only with the greater margin. If at depth 1 the margin does not exceed the value of a minor piece, at depth 2 it should be more like the value of a rook.

## Move Count Based Pruning

A further variation of Extended Futility Pruning combining the ideas of [Fruit's](Fruit "Fruit") [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning") and [Late Move Reductions](Late_Move_Reductions "Late Move Reductions") is called **Move Count Based Pruning** or **Late Move Pruning** (LMP) as implemented in [Stockfish](Stockfish "Stockfish") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Deep Futility Pruning

Deep Futility Pruning was proposed by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. It is applied at depths of 1\<d\<=3+[R](Depth_Reduction_R "Depth Reduction R"), i.e. with two moves to go:

```C++

if ( CurEval <= Alpha - PVal[FirstPiece(Opponent)] - PVal[SecondPiece(Opponent)] - 2*PosMargin )
   prune

```

## See also

- [AEL-Pruning](AEL-Pruning "AEL-Pruning")
- [Delta Pruning](Delta_Pruning "Delta Pruning")
- [Frontier Node](Frontier_Nodes "Frontier Nodes")
- [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Ostrich's Gamma-Algorithm](Ostrich#GammaAlgorithm "Ostrich")
- [Pre Frontier Node](Pre_Frontier_Node "Pre Frontier Node")
- [Razoring](Razoring "Razoring")
- [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
- [Sibling Prediction Pruning](Sibling_Prediction_Pruning "Sibling Prediction Pruning")

## Publications

- [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1986**). *Experiments in Search and Knowledge*. Ph.D. Thesis, [University of Waterloo](University_of_Waterloo "University of Waterloo"). Reprinted as Technical Report TR 86-12, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta")
- [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Experiments in Forward Pruning with Limited Extensions.* [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal")
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[Extended Futility Pruning](http://people.csail.mit.edu/heinz/dt/node18.html).* [ICCA Journal, Vol. 21, No. 2](ICGA_Journal#21_2 "ICGA Journal")
- [Jeroen Carolus](Jeroen_Carolus "Jeroen Carolus") (**2006**). *Alpha-Beta with Sibling Prediction Pruning in Chess*. Masters thesis, [pdf](http://homepages.cwi.nl/%7Epaulk/theses/Carolus.pdf)
- [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Masakazu Muramatsu](Masakazu_Muramatsu "Masakazu Muramatsu") (**2012**). *[Efficiency of three Forward-Pruning Techniques in Shogi: Futility Pruning, Null-move Pruning, and Late Move Reduction (LMR)](https://www.semanticscholar.org/paper/Efficiency-of-three-forward-pruning-techniques-in-Hoki-Muramatsu/206099961f401c8693e071c2b739f164ae5ffa6c)*. [Entertainment Computing](https://www.journals.elsevier.com/entertainment-computing), Vol. 3, No. 3

## Forum Posts

## 1995 ...

- [futility cut-offs](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/375e65821715995f) by [Alessandro Damiani](Alessandro_Damiani "Alessandro Damiani"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 14, 1997
- [Extended Futility Pruning - anyone tried it?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/9a16d1cfe8d042bc) by [Tom King](Tom_King "Tom King"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 16, 1998
- [Extensions and Futility Pruning](https://www.stmintz.com/ccc/index.php?id=50627) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), May 04, 1999 » [Extensions](Extensions "Extensions")
- [Extended futility pruning and hashtables](https://www.stmintz.com/ccc/index.php?id=85079) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), December 30, 1999 » [Transposition Table](Transposition_Table "Transposition Table")

## 2000 ...

- [Futility Pruning (I think) Question](https://www.stmintz.com/ccc/index.php?id=104283) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), April 02, 2000
- [Caution K v KBN and lazy eval or futility](https://www.stmintz.com/ccc/index.php?id=110681) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), May 14, 2000 » [KBNK Endgame](KBNK_Endgame "KBNK Endgame"), [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Something wrong with my futility pruning?](https://www.stmintz.com/ccc/index.php?id=143040) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 05, 2000
- [About history heuristics, killers and my futil. pruning code](https://www.stmintz.com/ccc/index.php?id=143331) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 06, 2000 » [History Heuristic](History_Heuristic "History Heuristic"), [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
- [question about futility pruning and positional evaluation](https://www.stmintz.com/ccc/index.php?id=143506) by Bert van den Akker, [CCC](CCC "CCC"), December 07, 2000  » [Evaluation](Evaluation "Evaluation")
- [Futility Cutoff futile?](https://www.stmintz.com/ccc/index.php?id=186225) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), August 29, 2001
- [Futility + WAC](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=34982) by [Stefan Knappe](Stefan_Knappe "Stefan Knappe"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 07, 2001 » [Matador](Matador "Matador"), [Win at Chess](Win_at_Chess "Win at Chess")
- [Re: Futility Pruning](https://www.stmintz.com/ccc/index.php?id=271983) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), December 20, 2002
- [To Stefan Knappe](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43088) by [Rahman Paidar](Rahman_Paidar "Rahman Paidar"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 21, 2003 » [Stefan Knappe](Stefan_Knappe "Stefan Knappe")
- [futility pruning?](https://www.stmintz.com/ccc/index.php?id=326340) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), November 09, 2003
- [Unexpected problem with futility pruning ?](https://www.stmintz.com/ccc/index.php?id=339041) by Geoff, [CCC](CCC "CCC"), December 29, 2003
- [Question for Tom Likens](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46383) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 07, 2004 » [Djinn](Djinn "Djinn")
- [Extended futility pruning not working](https://www.stmintz.com/ccc/index.php?id=380679) by Cesar Contreras, [CCC](CCC "CCC"), August 03, 2004
- [Futility](https://www.stmintz.com/ccc/index.php?id=391540) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), October 14, 2004
- [Futility Prune question](https://www.stmintz.com/ccc/index.php?id=392021) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), October 17, 2004
- [Futility @ 1/Extended Futility @ 2/Limited Razoring @ 3 = % node reduce?](https://www.stmintz.com/ccc/index.php?id=392248) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), October 19, 2004

## 2005 ...

- [Does simple futility prune work](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2101) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 27, 2005
- [Selective Futlity Condition at Quiescence Nodes](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3734) by [Pradu](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 26, 2005
- [Null move, futility and LMR](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5648) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 26, 2006 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [LMR](Late_Move_Reductions "Late Move Reductions")
- [Hash Table handling with LMR/Futility pruning](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5779) by [Pradu](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 21, 2006
- [Extended futility reduction](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5890) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 18, 2006
- [How much elo from futility?](http://www.talkchess.com/forum/viewtopic.php?t=16290) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), September 05, 2007
- [LMR and futility](http://www.talkchess.com/forum/viewtopic.php?t=17442) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), October 28, 2007
- [Draw recognizers, futility... mess](http://www.talkchess.com/forum/viewtopic.php?t=24371) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), October 14, 2008
- [futility pruning - razoring](http://www.talkchess.com/forum/viewtopic.php?t=29777) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 16, 2009 » [Razoring](Razoring "Razoring")
- [Futility pruning, Ext futility pruning and Limited Razoring](http://www.talkchess.com/forum/viewtopic.php?t=30802) by [Jesper Nielsen](index.php?title=Jesper_Nielsen&action=edit&redlink=1 "Jesper Nielsen (page does not exist)"), [CCC](CCC "CCC"), November 26, 2009

## 2010 ...

- [Futility Idea based on total score](http://www.talkchess.com/forum/viewtopic.php?t=32407) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), February 06, 2010
- [Confused by futility pruning](http://www.talkchess.com/forum/viewtopic.php?t=33033) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), March 03, 2010
- [move count based pruning](http://www.talkchess.com/forum/viewtopic.php?t=35955) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), September 02, 2010
- [LMR, Razoring, Futility.... with chess variant with drops?](http://www.talkchess.com/forum/viewtopic.php?t=37360) by Justin Madru, [CCC](CCC "CCC"), December 30, 2010
- [Futility Methods](http://www.talkchess.com/forum/viewtopic.php?t=37731) by kenny stanley, [CCC](CCC "CCC"), January 21, 2011
- [futility pruning in stockfish](http://www.talkchess.com/forum/viewtopic.php?t=39169) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [CCC](CCC "CCC"), May 25, 2011 » [Stockfish](Stockfish "Stockfish")
- [Reverse Futility Pruning](http://www.talkchess.com/forum/viewtopic.php?t=41302) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), December 02, 2011 » [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
- [How to get futility pruning to work?](http://www.talkchess.com/forum/viewtopic.php?t=42749) by [Robert Purves](index.php?title=Robert_Purves&action=edit&redlink=1 "Robert Purves (page does not exist)"), [CCC](CCC "CCC"), March 05, 2012
- [futility pruning, razoring question](http://www.talkchess.com/forum/viewtopic.php?t=43165) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), April 04, 2012 » [Razoring](Razoring "Razoring")
- [A search enhancement?](http://www.talkchess.com/forum/viewtopic.php?t=43513) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), April 30, 2012 » [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
- [LMP in PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=54761) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), December 27, 2014 » [PV-Node](Node_Types#PV "Node Types"), [Texel](Texel "Texel")

## 2015 ...

- [Problem understanding futility pruning](http://www.talkchess.com/forum/viewtopic.php?t=56323) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), May 11, 2015
- [Razoring vs Futility pruning](http://www.talkchess.com/forum/viewtopic.php?t=57287) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), August 16, 2015 » [Razoring](Razoring "Razoring")

**2016**

- [futility pruning](http://www.talkchess.com/forum/viewtopic.php?t=59315) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), February 20, 2016
- [Futile attempts at futility pruning](http://www.talkchess.com/forum/viewtopic.php?t=59661) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), March 27, 2016 » [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
- [Futility prunning](http://www.talkchess.com/forum/viewtopic.php?t=61093) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), August 11, 2016 » [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
- [Futility Pruning](http://www.talkchess.com/forum/viewtopic.php?t=61682) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), October 11, 2016

**2017 ...**

- [Futility pruning ?](http://www.talkchess.com/forum/viewtopic.php?t=63344) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), March 04, 2017 » [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
- [futile futility pruning attempt](http://www.talkchess.com/forum/viewtopic.php?t=63368) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), March 07, 2017
- [Futility pruning...](http://www.open-chess.org/viewtopic.php?f=5&t=3099) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 07, 2017
- [increasing futility prunning depth](http://www.talkchess.com/forum/viewtopic.php?t=63852) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 28, 2017
- [Tuning Futility Margin](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64343) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), June 19, 2017
- [A question about futility prunning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68081) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), July 26, 2018

## 2020 ...

- [Futility Pruning Issues](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74403) by Cheney, [CCC](CCC "CCC"), July 07, 2020
- [Futility Pruning and its Relation to Quiescence Search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77451) by [Jakob Progsch](index.php?title=Jakob_Progsch&action=edit&redlink=1 "Jakob Progsch (page does not exist)"), [CCC](CCC "CCC"), June 06, 2021 » [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Futility reductions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77644) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), July 05, 2021

## External Links

## Pruning

- [MadChess 3.0 Beta 6f3d17a (Late Move Pruning)](https://www.madchess.net/2020/02/08/madchess-3-0-beta-4478cb8-late-move-pruning/) by [Erik Madsen](Erik_Madsen "Erik Madsen"), February 8, 2020 » [LMP](Futility_Pruning#MoveCountBasedPruning "Futility Pruning"), [MadChess](MadChess "MadChess")
- [Deep Futility Pruning](http://home.hccnet.nl/h.g.muller/deepfut.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")

## Misc

- [futility - Wiktionary](https://en.wiktionary.org/wiki/futility)

[futile - Wiktionary](https://en.wiktionary.org/wiki/futile)

- [Futility from Wikipedia](https://en.wikipedia.org/wiki/Futility)
- [The Wreck of the Titan: Or, Futility - Wikipedia](https://en.wikipedia.org/wiki/The_Wreck_of_the_Titan:_Or,_Futility)
- [Porcupine Tree](Category:Porcupine_Tree "Category:Porcupine Tree") - [Futile](<https://en.wikipedia.org/wiki/Futile_(EP)>), [Zeche](https://de.wikipedia.org/wiki/Zeche_Bochum) [Bochum](https://en.wikipedia.org/wiki/Bochum), November 18, 2003, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Picture gallery "Back in Holland 1941 - 1954"](http://www.mcescher.com/Gallery/gallery-back.htm) from [The Official M.C. Escher Website](http://www.mcescher.com/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Serious bug in Gothmog 0.2.6!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43669&p=166791) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 04, 2003
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Unexpected problem with futility pruning?](https://www.stmintz.com/ccc/index.php?id=339076) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), December 29, 2003
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[Extended Futility Pruning](http://people.csail.mit.edu/heinz/dt/node18.html).* [ICCA Journal, Vol. 21, No. 2](ICGA_Journal#21_2 "ICGA Journal")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [move count based pruning](http://www.talkchess.com/forum/viewtopic.php?t=35955) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), September 02, 2010
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Deep Futility Pruning](http://home.hccnet.nl/h.g.muller/deepfut.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")

**[Up one Level](Pruning "Pruning")**

