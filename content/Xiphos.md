---
title: Xiphos
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Xiphos**



[ Xiphos and Makhaira <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Xiphos**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Milos Tatarevic](Milos_Tatarevic "Milos Tatarevic"), written in [C](C "C"), licensed under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") v3.0, first released on February 28, 2018. Xiphos utilizes [bitboards](Bitboards "Bitboards") with BERLEF [mapping](Square_Mapping_Considerations "Square Mapping Considerations") (a1=56, a8=63, h1=0, h8=7) <a id="cite-note-2" href="#cite-ref-2">[2]</a>. [Sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") are determined by either [magic bitboards](Magic_Bitboards "Magic Bitboards"), or if compiled for [BMI2](BMI2 "BMI2") capable [x86-64](X86-64 "X86-64") processors, by [PEXT bitboards](BMI2#PEXTBitboards "BMI2"). Xiphos executables are available to run under [Linux](Linux "Linux"), [Mac OS](Mac_OS "Mac OS") and [Windows](Windows "Windows"). Still work in progress with a relatively simple [evaluation](Evaluation "Evaluation") function, the first Xiphos release should already be on par with engines rated around 3000 Elo on [CCRL 40/4](CCRL "CCRL") scale <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Selected Features


### [Search](Search "Search")


<a id="cite-note-7" href="#cite-ref-7">[7]</a>



* [Parallel Search](Parallel_Search "Parallel Search") using [Threads](Thread "Thread")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")


 [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
* [Move Ordering](Move_Ordering "Move Ordering")


 [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
 [History Heuristic](History_Heuristic "History Heuristic")
 [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
 [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
 [MVV/LVA](MVV-LVA "MVV-LVA")
 [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Singular Extensions](Singular_Extensions "Singular Extensions") (0.2)
* [Pruning](Pruning "Pruning")


 [Futility Pruning](Futility_Pruning "Futility Pruning")
 [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
 [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
 [ProbCut](ProbCut "ProbCut")
* [Reductions](Reductions "Reductions")


 [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
 [Razoring](Razoring "Razoring")
* [Quiescence Search](Quiescence_Search "Quiescence Search")


### [Evaluation](Evaluation "Evaluation")


<a id="cite-note-8" href="#cite-ref-8">[8]</a>



* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")


 [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Pawn Structure](Pawn_Structure "Pawn Structure")


 [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
 [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
 [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
 [Passed Pawn](Passed_Pawn "Passed Pawn")
* [Mobility](Mobility "Mobility")
* [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
* [King Safety](King_Safety "King Safety")


### Misc


* [Perft](Perft "Perft")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [PEXT Bitboards](BMI2#PEXTBitboards "BMI2")


## Forum Posts


### 2018


* [New engine: Xiphos](http://www.talkchess.com/forum/viewtopic.php?t=66709) by [Milos Tatarevic](Milos_Tatarevic "Milos Tatarevic"), [CCC](CCC "CCC"), February 28, 2018
* [Xiphos 0.2](http://www.talkchess.com/forum/viewtopic.php?t=67105) by [Milos Tatarevic](Milos_Tatarevic "Milos Tatarevic"), [CCC](CCC "CCC"), April 14, 2018
* [Xiphos 0.2.2](http://www.talkchess.com/forum/viewtopic.php?t=67179) by [Milos Tatarevic](Milos_Tatarevic "Milos Tatarevic"), [CCC](CCC "CCC"), April 20, 2018
* [Xiphos 0.3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67820) by [Milos Tatarevic](Milos_Tatarevic "Milos Tatarevic"), [CCC](CCC "CCC"), June 25, 2018
* [Xiphos 0.4](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68508) by [Milos Tatarevic](Milos_Tatarevic "Milos Tatarevic"), [CCC](CCC "CCC"), September 24, 2018
* [The Xiphos Material Evaluator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68842) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), November 05, 2018 » [Material](Material "Material")


### 2019


* [xiphos 64 bit random number](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70050) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), February 28, 2019 » [Pseudorandom Number Generator](Pseudorandom_Number_Generator "Pseudorandom Number Generator")
* [Xiphos 0.5](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70172) by [Milos Tatarevic](Milos_Tatarevic "Milos Tatarevic"), [CCC](CCC "CCC"), March 11, 2019


## External Links


### Chess Engine


* [GitHub - milostatarevic/xiphos: UCI chess engine](https://github.com/milostatarevic/xiphos)
* [Xiphos](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Xiphos&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


### Misc


* [Xiphos from Wikipedia](https://en.wikipedia.org/wiki/Xiphos)
* [The SWORD Project from Wikipedia](https://en.wikipedia.org/wiki/The_SWORD_Project)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Graphic of [Bronze Age swords](https://en.wikipedia.org/wiki/Bronze_Age_sword), [Xiphos](https://en.wikipedia.org/wiki/Xiphos) (fig. 1-3 left) and [Makhaira](https://en.wikipedia.org/wiki/Makhaira) (fig. 4), Image from the 4th edition of [Meyers Konversationslexikon](https://en.wikipedia.org/wiki/Meyers_Konversations-Lexikon) (1885–90), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [xiphos/game.h at master · milostatarevic/xiphos · GitHub](https://github.com/milostatarevic/xiphos/blob/master/src/game.h)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [New engine: Xiphos](http://www.talkchess.com/forum/viewtopic.php?t=66709) by [Milos Tatarevic](Milos_Tatarevic "Milos Tatarevic"), [CCC](CCC "CCC"), February 28, 2018
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [“Deep Thinking” | Kasparov](http://www.kasparov.com/deep-thinking-ai/)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Garry Kasparov](Garry_Kasparov "Garry Kasparov") (**2017**). *Deep Thinking: Where Machine Intelligence Ends and Human Creativity Begins*. with contributions by [Mig Greengard](index.php?title=Mig_Greengard&action=edit&redlink=1 "Mig Greengard (page does not exist)"), [amazon.com](https://www.amazon.com/Deep-Thinking-Machine-Intelligence-Creativity/dp/161039786X/ref=sr_1_3?ie=UTF8&qid=1487863915&sr=8-3&keywords=kasparov)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [xiphos/README.md at master · milostatarevic/xiphos · GitHub](https://github.com/milostatarevic/xiphos/blob/master/README.md)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [xiphos/search.c at master · milostatarevic/xiphos · GitHub](https://github.com/milostatarevic/xiphos/blob/master/src/search.c)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [xiphos/eval.c at master · milostatarevic/xiphos · GitHub](https://github.com/milostatarevic/xiphos/blob/master/src/eval.c)

**[Up one Level](Engines "Engines")**







 
