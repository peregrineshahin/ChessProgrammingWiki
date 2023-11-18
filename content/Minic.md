---
title: Minic
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Minic**


**Minic**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), initially squashed inside a single [C++](Cpp "Cpp") source file licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation").
As a weekend project, it started as 2000 [lines of code](https://en.wikipedia.org/wiki/Source_lines_of_code) [mailbox](Mailbox "Mailbox") approach using [PVS](Principal_Variation_Search "Principal Variation Search") with [TT](Transposition_Table "Transposition Table"), [NMP](Null_Move_Pruning "Null Move Pruning"), [LMP](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") and [eval](Evaluation "Evaluation") based on [psts](Piece-Square_Tables "Piece-Square Tables"), and evolved to a [bitboard](Bitboards "Bitboards") engine using [HQ](Hyperbola_Quintessence "Hyperbola Quintessence"), [lazy SMP](Lazy_SMP "Lazy SMP"), and [Texel tuning](Texel%27s_Tuning_Method "Texel's Tuning Method") to optimize its [tapered eval](Tapered_Eval "Tapered Eval") <a id="cite-note-1" href="#cite-ref-1">[1]</a>.



## Minic 3


Minic **3.00**, announced on November 03, 2020, detached the [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") dependency, and came with an own [NNUE](NNUE "NNUE") implementation adopted from the [Seer](Seer "Seer") engine by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), which allows to easily change the net architecture and to apply engine-independent [PyTorch](https://en.wikipedia.org/wiki/PyTorch) training code <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Minic **3.02** released on December 19, 2020, supports the new **Seer**  like NNUE **Narcotized Nightshift**, which seems to be nearly 90 Elo better than the former **Nefarious Nucleus** <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



## See also


* [Weini](Weini "Weini")


## Forum Posts


### 2018 ...


* [A complete 2000 lines of code engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68701) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), October 20, 2018
* [Asus tuf z390 + core i7 9700k](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70052) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 28, 2019
* [Feature score use in search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71325) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), July 20, 2019
* [Minic raw speed](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72285) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), November 09, 2019


### 2020 ...


* [Minic version 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73521) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), March 31, 2020


 [Re: Minic version 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73521&start=59) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), August 08, 2020 » [NNUE](NNUE "NNUE")
* [Black crushing white, weird ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75393) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), October 14, 2020 » [NNUE](NNUE "NNUE")
* [Minic version 3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75665) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), November 03, 2020


 [Re: Minic version 3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75665&start=9) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 03, 2020 <a id="cite-note-6" href="#cite-ref-6">[6]</a>
 [Re: Minic version 3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75665&start=189) (Minic 3.08) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 04, 2021
* [Effect of adjudication and TC on testing process](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76536) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 09, 2021 » [Engine Testing](Engine_Testing "Engine Testing")
* [HCE and NNUE and vectorisation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76556) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 11, 2021 » [Evaluation](Evaluation "Evaluation"), [NNUE](NNUE "NNUE")
* [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021 » [NNUE](NNUE "NNUE")


 [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=68) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 18, 2021
## External Links


* [GitHub - tryingsomestuff/Minic: A simple chess engine to learn and play with](https://github.com/tryingsomestuff/Minic)
* [GitHub - tryingsomestuff/NNUE-Nets](https://github.com/tryingsomestuff/NNUE-Nets)
* [Minic](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Minic&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL").


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [GitHub - tryingsomestuff/Minic: A simple chess engine to learn and play with](https://github.com/tryingsomestuff/Minic)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Minic version 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73521&start=59) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), August 08, 2020
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Minic/README.md at master · tryingsomestuff/Minic · GitHub - NNUE (from Stockfish)](https://github.com/tryingsomestuff/Minic/blob/master/README.md#nnue-from-stockfish)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a>  [Minic version 3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75665) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), November 03, 2020
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [GitHub - tryingsomestuff/NNUE-Nets for Seer like NNUE](https://github.com/tryingsomestuff/NNUE-Nets#for-seer-like-nnue)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Gao Huang](index.php?title=Gao_Huang&action=edit&redlink=1 "Gao Huang (page does not exist)"), [Zhuang Liu](index.php?title=Zhuang_Liu&action=edit&redlink=1 "Zhuang Liu (page does not exist)"), [Laurens van der Maaten](index.php?title=Laurens_van_der_Maaten&action=edit&redlink=1 "Laurens van der Maaten (page does not exist)"), [Kilian Q. Weinberger](index.php?title=Kilian_Q._Weinberger&action=edit&redlink=1 "Kilian Q. Weinberger (page does not exist)") (**2016**). *Densely Connected Convolutional Networks*. [arXiv:1608.06993](https://arxiv.org/abs/1608.06993)

**[Up one level](Engines "Engines")**







 
