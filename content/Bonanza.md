---
title: Bonanza
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bonanza**

\[ Bonanza team performs distributed tree search <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Bonanza**, (Bonanza Feliz)

an [XBoard](XBoard "XBoard") compliant [open source](Category:Open_Source "Category:Open Source") [Shogi](Shogi "Shogi") engine developed by primary author [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), started in 2004, at times supported by [Takuya Obata](Takuya_Obata "Takuya Obata"), [Takuya Sugiyama](Takuya_Sugiyama "Takuya Sugiyama"), and [Takeshi Ito](Takeshi_Ito "Takeshi Ito")
<a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Bonanza is top contender at [Computer Olympiads](Computer_Olympiad "Computer Olympiad") and [World Computer Shogi Championships](World_Computer_Shogi_Championship "World Computer Shogi Championship")
and so far two times champion, winning the [WCSC16](index.php?title=WCSC16&action=edit&redlink=1 "WCSC16 (page does not exist)") in 2006, and the [WCSC23](index.php?title=WCSC23&action=edit&redlink=1 "WCSC23 (page does not exist)") in 2013 <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Description

Bonanza is written in [C](C "C") and utilizes 9x9 [Bitboards](Bitboards "Bitboards") in form of three 32-bit unsigned integers.
It is a [fractional ply](Depth#FractionalPlies "Depth") [alpha-beta](Alpha-Beta "Alpha-Beta") engine performing a [principal variation search](Principal_Variation_Search "Principal Variation Search") with [transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning"),
[recursive iterative-deepening](Internal_Iterative_Deepening "Internal Iterative Deepening") for [PV-nodes](Node_Types#PV "Node Types"), various [extensions](Extensions "Extensions"), [reductions](Reductions "Reductions"), and [futility pruning](Futility_Pruning "Futility Pruning").
Bonanza pioneered in large-scale [machine learning](Learning "Learning") of static [evaluation functions](Evaluation "Evaluation"),
a [supervised](Supervised_Learning "Supervised Learning") [tuning method](Automated_Tuning "Automated Tuning") based on [move adaptation](Automated_Tuning#MoveAdaption "Automated Tuning"),
dubbed the **Bonanza Method** which evolved to [Minimax Tree Optimization](Minimax_Tree_Optimization "Minimax Tree Optimization") (MMTO).
Bonanza utilizes and tuned [piece-square tables](Piece-Square_Tables "Piece-Square Tables") indexed by king location and further two-piece locations and side to move (turn), dubbed **KPP**, **KKP** or **KPPT**, which was used in many other Shogi programs <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and has influenced the design of [NNUE](NNUE "NNUE") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

Beside a [parallel tree search](Parallel_Search "Parallel Search"), Bonanza is able to apply parallelization by the so called **Consensus** method
<a id="cite-note-6" href="#cite-ref-6">[6]</a>,
a kind of **triple-brain** approach where multiple, slightly modified instances of the same engine vote for the best move <a id="cite-note-7" href="#cite-ref-7">[7]</a>
<a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## Publications

- [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2006**). *Optimal control of minimax search result to learn positional evaluation*. [11th Game Programming Workshop](Conferences#GPW "Conferences") (Japanese)
- [Takuya Obata](Takuya_Obata "Takuya Obata"), [Takuya Sugiyama](Takuya_Sugiyama "Takuya Sugiyama"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito") (**2010**). *[Consultation Algorithm for Computer Shogi: Move Decisions by Majority](https://link.springer.com/chapter/10.1007%2F978-3-642-17928-0_15)*. [CG 2010](CG_2010 "CG 2010")
- [Takuya Sugiyama](Takuya_Sugiyama "Takuya Sugiyama"), [Takuya Obata](Takuya_Obata "Takuya Obata"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito") (**2010**). *[Optimistic Selection Rule Better Than Majority Voting System](https://link.springer.com/chapter/10.1007%2F978-3-642-17928-0_16)*. [CG 2010](CG_2010 "CG 2010")
- [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2011**). *Analysis of Evaluation-Function Learning by Comparison of Sibling Nodes*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
- [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2011**). *The Global Landscape of Objective Functions for the Optimization of Shogi Piece Values with a Game-Tree Search*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
- [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Masakazu Muramatsu](Masakazu_Muramatsu "Masakazu Muramatsu") (**2012**). *[Efficiency of three Forward-Pruning Techniques in Shogi: Futility Pruning, Null-move Pruning, and Late Move Reduction (LMR)](https://www.semanticscholar.org/paper/Efficiency-of-three-forward-pruning-techniques-in-Hoki-Muramatsu/206099961f401c8693e071c2b739f164ae5ffa6c)*. [Entertainment Computing](https://www.journals.elsevier.com/entertainment-computing), Vol. 3, No. 3
- [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2014**). *[Large-Scale Optimization for Evaluation Functions with Minimax Search](https://www.jair.org/papers/paper4217.html)*. [JAIR Vol. 49](https://www.jair.org/vol/vol49.html), [pdf](https://pdfs.semanticscholar.org/eb9c/173576577acbb8800bf96aba452d77f1dc19.pdf) <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Seiya Omori](index.php?title=Seiya_Omori&action=edit&redlink=1 "Seiya Omori (page does not exist)"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito") (**2014**). *Analysis of Performance of Consultation Methods in Computer Chess*. [Journal of Information Science and Engineering](https://jise.iis.sinica.edu.tw/), Vol. 30, [pdf](https://www.iis.sinica.edu.tw/page/jise/2014/201405_10.pdf)
- [Takenobu Takizawa](Takenobu_Takizawa "Takenobu Takizawa"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito"), [Takuya Hiraoka](Takuya_Hiraoka "Takuya Hiraoka"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2015**). *[Contemporary Computer Shogi](https://link.springer.com/referenceworkentry/10.1007/978-3-319-08234-9_22-1)*. [Encyclopedia of Computer Graphics and Games](https://link.springer.com/referencework/10.1007/978-3-319-08234-9)

## Forum Posts

- [Source file of Bonanza 4.0.3 became available to downloadable](https://groups.google.com/d/msg/shogi-l/Pl1fLHngPAk/iYV8pnnLqQIJ) by Takodori, [SHOGI-L](Computer_Chess_Forums "Computer Chess Forums"), January 29, 2009
- [XBoard version of Bonanza](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=36436) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 20, 2010
- [The Japan Times on-line 20111102 and Shogi](https://groups.google.com/d/msg/shogi-l/0H3BhhXiMXY/J_MM40w0unwJ) by Alain Van hentenryck, [SHOGI-L](Computer_Chess_Forums "Computer Chess Forums"), November 02, 2011
- [Bonanza wins Computer Shogi Championship](https://groups.google.com/d/msg/shogi-l/lauO5HQFQNw/FHtovUqEwBEJ) by [Hiroshi Yamashita](Hiroshi_Yamashita "Hiroshi Yamashita"), [SHOGI-L](Computer_Chess_Forums "Computer Chess Forums"), May 06, 2013
- [Bonanza version adapted for interactive analysis (release)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=49354) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 14, 2013
- [Bonanza version adapted for interactive analysis](https://groups.google.com/d/msg/shogi-l/qRt55wwPp6U/gRsFDUCNKrkJ) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [SHOGI-L](Computer_Chess_Forums "Computer Chess Forums"), September 14, 2013
- [better appearance of BONANZA](https://groups.google.com/d/msg/shogi-l/GNsLsYo9SgQ/oAeH2nnTirAJ) by shogipl..., [SHOGI-L](Computer_Chess_Forums "Computer Chess Forums"), October 21, 2014

## External Links

## Shogi Engine

- [GitHub - ianfab/bonanza: strong shogi engine (with support for XBoard protocol)](https://github.com/ianfab/bonanza) hosted by [Fabian Fichter](index.php?title=Fabian_Fichter&action=edit&redlink=1 "Fabian Fichter (page does not exist)")
- [Bonanza Shogi Engine](http://hgm.nubati.net/bonanza.html) hosted by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
- [Bonanza's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=215)
- Famous Shogi Games: [Bonanza vs Watanabe](<https://en.wikipedia.org/wiki/Computer_shogi#Bonanza_versus_Watanabe_(2007)>) (March 21, 2007), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## Misc

- [bonanza - Wiktionary](https://en.wiktionary.org/wiki/bonanza)
- [Bonanza (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Bonanza_(disambiguation)>)
- [Bonanza from Wikipedia](https://en.wikipedia.org/wiki/Bonanza)
- [Feliz from Wikipedia](https://en.wikipedia.org/wiki/Feliz)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Photo](https://commons.wikimedia.org/wiki/File:Bonanza_main_cast_1959.JPG) of the main cast of [Bonanza](https://en.wikipedia.org/wiki/Bonanza). From left - [Dan Blocker](https://en.wikipedia.org/wiki/Dan_Blocker) (Hoss), [Michael Landon](https://en.wikipedia.org/wiki/Michael_Landon) (Little Joe), [Lorne Greene](https://en.wikipedia.org/wiki/Lorne_Greene) (Ben), [Pernell Roberts](https://en.wikipedia.org/wiki/Pernell_Roberts) (Adam), September 20, 1959, Author: [NBC Television](https://en.wikipedia.org/wiki/NBC). [Category:Bonanza (TV series) - Wikimedia Commons](<https://commons.wikimedia.org/wiki/Category:Bonanza_(TV_series)>)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [WCSC20 Participant List](https://groups.google.com/d/msg/shogi-l/bazz1reADOY/KB8UvBZQf_cJ) by [Nobu](Takenobu_Takizawa "Takenobu Takizawa"), [SHOGI-L](Computer_Chess_Forums "Computer Chess Forums"), February 02, 2010
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Takenobu Takizawa](Takenobu_Takizawa "Takenobu Takizawa"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito"), [Takuya Hiraoka](Takuya_Hiraoka "Takuya Hiraoka"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2015**). *[Contemporary Computer Shogi](https://link.springer.com/referenceworkentry/10.1007/978-3-319-08234-9_22-1)*. [Encyclopedia of Computer Graphics and Games](https://link.springer.com/referencework/10.1007/978-3-319-08234-9)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [The 25th World Computer Shogi Championships](https://groups.google.com/d/msg/shogi-l/c4-dY44P8Mw/M3z-RtFR-tsJ) by [Reijer Grimbergen](Reijer_Grimbergen "Reijer Grimbergen") on behalf of [Takenobu Takizawa](Takenobu_Takizawa "Takenobu Takizawa"), [SHOGI-L](Computer_Chess_Forums "Computer Chess Forums"), February 11, 2015
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [機械学習エンジニアのための将棋AI開発入門その1 Introduction to Shogi AI development for machine learning engineers Part 1](http://yaneuraou.yaneu.com/2020/05/03/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E5%B0%86%E6%A3%8Bai%E9%96%8B%E7%99%BA%E5%85%A5%E9%96%80%E3%81%9D%E3%81%AE1/), May 03, 2020 (Japanese)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Bonanzaの特徴は、 Characteristics of Bonanza - wcsc23 2013](http://www2.computer-shogi.org/wcsc23/appeal/Bonanza/ap.txt)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Takuya Obata](Takuya_Obata "Takuya Obata"), [Takuya Sugiyama](Takuya_Sugiyama "Takuya Sugiyama"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito") (**2010**). *[Consultation Algorithm for Computer Shogi: Move Decisions by Majority](https://link.springer.com/chapter/10.1007%2F978-3-642-17928-0_15)*. [CG 2010](CG_2010 "CG 2010")
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Seiya Omori](index.php?title=Seiya_Omori&action=edit&redlink=1 "Seiya Omori (page does not exist)"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito") (**2014**). *Analysis of Performance of Consultation Methods in Computer Chess*. [Journal of Information Science and Engineering](https://jise.iis.sinica.edu.tw/), Vol. 30, [pdf](https://www.iis.sinica.edu.tw/page/jise/2014/201405_10.pdf)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [MMTO for evaluation learning](http://www.talkchess.com/forum/viewtopic.php?t=55084) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 25, 2015

**[Up one Level](Engines "Engines")**

