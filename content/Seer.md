---
title: Seer
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Seer**



[ Greek Seer <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Seer**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), written in [C++](Cpp "Cpp"), 
licensed under the [GNU GPL](Free_Software_Foundation#GPL "Free Software Foundation") and first released in October 2020. 
Seer uses a custom [NNUE](NNUE "NNUE") implementation based on [32-bit float](Float "Float") weights with training code written in [PyTorch](https://en.wikipedia.org/wiki/PyTorch) and inference code relying on [OpenMP](https://en.wikipedia.org/wiki/OpenMP) [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") for auto vectorization <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Due to [PEXT Bitboards](BMI2#PEXTBitboards "BMI2"), Seer requires [BMI2](BMI2 "BMI2") for a reasonable performance, as well as either [SSE](SSE "SSE"), [AVX](AVX "AVX"), [AVX2](AVX2 "AVX2") or [AVX-512](AVX-512 "AVX-512") to calculate the NNUE. More recently, Seer supports [ARM NEON](index.php?title=ARM_NEON&action=edit&redlink=1 "ARM NEON (page does not exist)") via **sse2neon** <a id="cite-note-3" href="#cite-ref-3">[3]</a> to run on many [Android](Android "Android") devices <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [PEXT Bitboards](BMI2#PEXTBitboards "BMI2")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
	+ [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
	+ [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") for [Captures](Captures "Captures")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Counter Moves History](History_Heuristic#CMHist "History Heuristic")
	+ [Follow Up History](History_Heuristic#CMHist "History Heuristic")
* [Selectivity](Selectivity "Selectivity")
	+ [Check Extensions](Check_Extensions "Check Extensions") if [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") >= 0
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")


### [Evaluation](Evaluation "Evaluation")


* [NNUE](NNUE "NNUE")


## See also


* [Oracle](Oracle "Oracle")
* [Prophet](Prophet "Prophet")
* [Minic 3](Minic#Minic_3 "Minic")


## Forum Posts


### 2020


* [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=427) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), October 18, 2020
* [Seer](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75433) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), October 18, 2020


 [Re: Seer](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75433&start=58) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 02, 2020 » Seer 1.1
 [Re: Seer](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75433&start=109) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 18, 2020 » Seer 1.2
* [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=469) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 02, 2020
* [Re: Minic version 3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75665&start=9) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 03, 2020 » [Minic 3](Minic#Minic_3 "Minic") <a id="cite-note-6" href="#cite-ref-6">[6]</a>
* [Re: Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890&start=6) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 12, 2020 » [Dragon by Komodo Chess](Dragon_by_Komodo_Chess "Dragon by Komodo Chess"), [Halogen](Halogen "Halogen")


 [Re: Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890&start=9) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 12, 2020
### 2021 ...


* [Seer 2.0.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77187) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), April 27, 2021


 [Re: Seer 2.0.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77187&start=32) by Archimedes, [CCC](CCC "CCC"), August 06, 2021 » Seer 2.2.0 for [Android](Android "Android")
 [Re: Seer 2.0.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=77187&start=60) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), April 25, 2022 » Seer 2.5.0
* [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021 » [NNUE](NNUE "NNUE")


## External Links


### Chess Engine


* [GitHub - connormcmonigle/seer-nnue: UCI chess engine using NNUE for position evaluation](https://github.com/connormcmonigle/seer-nnue)
* [Release seer-v2.5.0 · connormcmonigle/seer-nnue · GitHub](https://github.com/connormcmonigle/seer-nnue/releases/tag/v2.5.0)


### Misc


* [seer - Wiktionary](https://en.wiktionary.org/wiki/seer)
* [Seer from Wikipedia](https://en.wikipedia.org/wiki/Seer)
* [Hypnotic Brass Ensemble](https://en.wikipedia.org/wiki/Hypnotic_Brass_Ensemble) - Seer, [Sound Rhythm & Form](https://www.birdistheworm.com/recommended-hypnotic-brass-ensemble-sound-rhythm-form/) (2016), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video



## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Detail](https://commons.wikimedia.org/wiki/File:GR_08-04-23_Olympia_Museum_Zeustempel_Ostgiebel2.JPG) of [Temple of Zeus, Olympia](https://en.wikipedia.org/wiki/Temple_of_Zeus,_Olympia), author [Monika Angela Arnold, Berlin](https://commons.wikimedia.org/wiki/Category:Fotos_by_Monika_Angela_Arnold,_Berlin), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [GitHub - connormcmonigle/seer-nnue: UCI chess engine using NNUE for position evaluation](https://github.com/connormcmonigle/seer-nnue)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [GitHub - DLTcollab/sse2neon: A translator from Intel SSE intrinsics to Arm/Aarch64 NEON implementation](https://github.com/DLTcollab/sse2neon)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Seer 2.0.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77187&start=32) by Archimedes, [CCC](CCC "CCC"), August 06, 2021
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [seer-nnue/README.md at master · connormcmonigle/seer-nnue · GitHub](https://github.com/connormcmonigle/seer-nnue/blob/master/README.md)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Gao Huang](index.php?title=Gao_Huang&action=edit&redlink=1 "Gao Huang (page does not exist)"), [Zhuang Liu](index.php?title=Zhuang_Liu&action=edit&redlink=1 "Zhuang Liu (page does not exist)"), [Laurens van der Maaten](index.php?title=Laurens_van_der_Maaten&action=edit&redlink=1 "Laurens van der Maaten (page does not exist)"), [Kilian Q. Weinberger](index.php?title=Kilian_Q._Weinberger&action=edit&redlink=1 "Kilian Q. Weinberger (page does not exist)") (**2016**). *Densely Connected Convolutional Networks*. [arXiv:1608.06993](https://arxiv.org/abs/1608.06993)

**[Up one level](Engines "Engines")**







 
