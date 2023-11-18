---
title: EtherealEthereal 13 .28NNUE.29
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Ethereal**

\[ Ethereal night sky <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Ethereal**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") written by [Andrew Grant](Andrew_Grant "Andrew Grant") in [C](C "C"), licensed under the [GNU GPL](Free_Software_Foundation#GPL "Free Software Foundation") and first officially released in June 2016 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Ethereal is greatly influenced from [Crafty](Crafty "Crafty"), [Stockfish](Stockfish "Stockfish"), [TSCP](TSCP "TSCP"), [MadChess](MadChess "MadChess"), and [Fruit](Fruit "Fruit") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
On October 09, 2020, Andrew Grant initially announced his withdrawal from Ethereal's development with the releases of Ethereal **V12.75**
<a id="cite-note-4" href="#cite-ref-4">[4]</a>
and Ethereal **12.75 SF-NNUE**, the latter a [NNUE](NNUE "NNUE") implementation based on [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE"), to deliberately demonstrate how everybody may considerably improve the [playing strength](Playing_Strength "Playing Strength") of their engines without much effort
<a id="cite-note-5" href="#cite-ref-5">[5]</a>.
However, Andrew Grant voted for another direction, and announced a commercial release of Ethereal **13.00** (NNUE) ,
the free standard version still available on [Github](https://en.wikipedia.org/wiki/GitHub) [[6]](#cite-note-ethereal13nnue-6).

## Ethereal 13 (NNUE)

**Ethereal 13 (NNUE)**, the commercial Ethereal version for [AVX2](AVX2 "AVX2") systems was released on June 04, 2021. The program comes with two [NNUEs](NNUE "NNUE") for [evaluation](Evaluation "Evaluation"),
one for standard chess, and the secondary network trained exclusively for [Chess960](Chess960 "Chess960"). The NNUEs are not derived from, trained on, nor duplicated from the works of the [Stockfish](Stockfish "Stockfish") team [[6]](#cite-note-ethereal13nnue-6). Andrew Grant on his NNUE approach <a id="cite-note-7" href="#cite-ref-7">[7]</a>:

```C++
Ethereal is using the [HalfKP](Stockfish_NNUE#NNUE_Structure "Stockfish NNUE") paradigm, with a 40960x256 -> 512x32x32x1 Network. This is the textbook approach, but with some changes. Firstly, not all weights are quantized to int8 / int16 for the input layer. Instead, the network goes like this: int16_t => int16_t => (int32_t -> [float\_t](Float "Float")) => float_t => float_t. This approach allows us to never have to pack the data downwards, saving many operations, and also lets us take a slightly more expensive approach to the later layers in exchange for massively increased precision. If I eventually add support for [AVX](AVX "AVX") (not avx2) machines, it will be a significant gain as AVX does not have 256-bit vector support for integer types in a meaningful way.

```

```C++
During training the Network actually has 43850 input parameters, using a few factorization of the board to aid in training without having tens of billions of positions. In practice, each Net was trained somewhere between 2 and 4 billion positions total, evaluated by Ethereal / Ethereal NNUE. The networks are trained using a modified form of the [Adam](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam) optimizer, which allows better performance for datasets with extremely sparse input fields. For example, with a Batch Size of 16384, only about 50% of the 43,850 parameters are used on average.

```

```C++
Data generation for a given network takes about 3 weeks, completed on a 104 core machine. From there, processing that data down into a list of [FENs](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") and then into the format used by Ethereal's NNTrainer takes another 12 hours or so. Finally, training the actual Network can take a few days, with many stops and starts to drop the learning rate and find a global optima.

```

```C++
The trainer itself is a fully original work, written in [C](C "C") and making use of all 104 threads. It includes some AVX2 and even AVX512 code for use in updating the network parameters. This toolkit was used in training the Halogen networks as well. It is fairly flexible and trying things like HalfKA, changing layer sizes, adding layers, changing activation functions, or adding more factorizers is only a few minutes of effort in the code. It rivals speeds of [GPU](GPU "GPU") based trainers, by leveraging massive SMP and efficient implementations.

```

## Features

<a id="cite-note-8" href="#cite-ref-8">[8]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards")
- [8x8 Board](8x8_Board "8x8 Board")

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP") since 8.60 SMP <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [PVS](Principal_Variation_Search "Principal Variation Search") [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Delta Pruning](Delta_Pruning "Delta Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Razoring](Razoring "Razoring")
  - [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning") (Static Null Move Pruning)
  - [Static Exchange Evaluation Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Multi-Cut](Multi-Cut "Multi-Cut") (12.00)
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")

## [Evaluation](Evaluation "Evaluation")

- [NNUE](NNUE "NNUE") (Ethereal 13.00 NNUE)
- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
- [Outposts](Outposts "Outposts")
- [Rook on (Half) Open File](Rook_on_Open_File "Rook on Open File")
- [Rook on 7th Rank](Rook_on_Seventh "Rook on Seventh")
- [Castling Ability](Castling "Castling")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Automated Tuning](Automated_Tuning "Automated Tuning") by [Logistic Regression](Automated_Tuning#LogisticRegression "Automated Tuning"), [AdaGrad](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad) (12.50) <a id="cite-note-10" href="#cite-ref-10">[10]</a><a id="cite-note-11" href="#cite-ref-11">[11]</a>

## Misc

- [Syzygy Bases](Syzygy_Bases "Syzygy Bases") using [Fathom's](Syzygy_Bases#Fathom "Syzygy Bases") probing code (9.65), superseded by 7-men [Pyrrhic](Syzygy_Bases#Pyrrhic "Syzygy Bases") (12.50)

## Publications

- [Andrew Grant](Andrew_Grant "Andrew Grant") (**2020**). *Evaluation & Tuning in Chess Engines*. <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>

## Forum Posts

## 2016 ...

- [Re: How to speed up my engine](http://www.talkchess.com/forum/viewtopic.php?t=60023&start=18) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 03, 2016

[Re: How to speed up my engine](http://www.talkchess.com/forum/viewtopic.php?t=60023&start=19) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), May 03, 2016

- [Ethereal Bitboard 6.26 Chess Engine...a star is born!](http://www.talkchess.com/forum/viewtopic.php?t=60161) by AA Ross, [CCC](CCC "CCC"), May 14, 2016
- [Ethereal - Official Release](http://www.talkchess.com/forum/viewtopic.php?t=60596) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 25, 2016
- [Ethereal - Official Release](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=8645) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), June 25, 2016
- [Release of Ethereal7.78](http://www.talkchess.com/forum/viewtopic.php?t=61335) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 04, 2016

**2017**

- [Official release of Ethereal8.16](http://www.talkchess.com/forum/viewtopic.php?t=64162) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 03, 2017
- [Ethereal8.28 Release](http://www.talkchess.com/forum/viewtopic.php?t=65165) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 13, 2017
- [Ethereal8.37 Release](http://www.talkchess.com/forum/viewtopic.php?t=65685) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), November 10, 2017
- [Release of Ethereal 8.60 SMP](http://www.talkchess.com/forum/viewtopic.php?t=65968) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 10, 2017
- [Ethereal 8.61 -- Small bugfix to 8.60](http://www.talkchess.com/forum/viewtopic.php?t=65989) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 12, 2017
- [Time Managment translating to SMP](http://www.talkchess.com/forum/viewtopic.php?t=66099) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 23, 2017 » [Parallel Search](Parallel_Search "Parallel Search"), [Time Management](Time_Management "Time Management")

**2018**

- [Official Release of Ethereal9.00](http://www.talkchess.com/forum/viewtopic.php?t=66606) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), February 15, 2018
- [Official Release of Ethereal9.30](http://www.talkchess.com/forum/viewtopic.php?t=66882) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), March 20, 2018
- [Official Release of Ethereal9.65 with Syzygy Support](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67272&p=760110) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), April 29, 2018
- [Official Release of Ethereal 10.00 (Two-years Anniversary)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67602&p=763874) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), May 30, 2018
- [Official Release of Ethereal 10.55](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67993&p=76840) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), July 16, 2018
- [Ethereal 10.88 NUMA](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68293) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), August 24, 2018 » [NUMA](NUMA "NUMA")

**2019**

- [Official Release of Ethereal 11.25](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69669) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 21, 2019
- [For those that like to toy with Ethereal...](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72215) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 30, 2019
- [Official Release of Ethereal 11.75, supporting MultiPV](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72299) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), November 11, 2019

## 2020 ...

- [Official Release of Ethereal 12.00](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73233) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), February 29, 2020
- [Pawn structure tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73629) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), April 11, 2020 » [Pawn Structure](Pawn_Structure "Pawn Structure"), [Automated Tuning](Automated_Tuning "Automated Tuning")
- [Pyrrhic, Fathom for Humanoids](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74809) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), August 16, 2020 » [Pyrrhic](Syzygy_Bases#Pyrrhic "Syzygy Bases")
- [Evaluation & Tuning in Chess Engines](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74877) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), August 24, 2020 » [Automated Tuning](Automated_Tuning "Automated Tuning")
- [Official Release of Ethereal 12.50](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75047) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 08, 2020
- [Ethereal Pawn-King NN](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75159) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 19, 2020
- [Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 09, 2020

[Re: Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335&start=91) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 09, 2020
[Re: Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335&start=134) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), November 12, 2020

- [Request for someone to train an NNUE for Ethereal](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75345) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 09, 2020 » [NNUE](NNUE "NNUE")
- [Ethereal Tuning - Data Dump](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75350) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 10, 2020
- [Ethereal questions](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76049) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), December 12, 2020

**2021**

- [Commercial Release of Ethereal 13.00 (NNUE) for AVX2 Systems](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77438) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 04, 2021

[Re: Commercial Release of Ethereal 13.00 (NNUE) for AVX2 Systems](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77438&start=17) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 04, 2021

- [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021 » [NNUE](NNUE "NNUE")
- [I declare that HCE is dead...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77571) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 29, 2021 » [HCE](Evaluation "Evaluation"), [NNUE](NNUE "NNUE")

**2022**

- [Resolving once in a trillion crashes](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79160) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 18, 2022 » [Debugging](Debugging "Debugging")
- [Commercial Release of Ethereal 13.50](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79179) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 20, 2022

## External Links

## Chess Engine

- [Ethereal 13.00 (NNUE)](http://chess.grantnet.us/Ethereal/)
- [GitHub - AndyGrant/Ethereal: Ethereal UCI Chess Engine](https://github.com/AndyGrant/Ethereal)
- [Ethereal](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Ethereal&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")
- [Ethereal](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Ethereal&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")
- [Ethereal wins TCEC Division 4](http://www.chessdom.com/ethereal-wins-tcec-division-4/), Interview with [Andrew Grant](Andrew_Grant "Andrew Grant"), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), April 30, 2018 » [TCEC Season 12](TCEC_Season_12 "TCEC Season 12")
- [Ethereal chess engine leads TCEC Div 3 convincingly](http://www.chessdom.com/ethereal-chess-engine-leads-tcec-div-3-convincingly/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), August 12, 2018 » [TCEC Season 13](TCEC_Season_13 "TCEC Season 13")
- [Ethereal chess engine wins the gold at TCEC Div 3](http://www.chessdom.com/ethereal-chess-engine-wins-the-gold-at-tcec-div-3/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), August 17, 2018

## Misc

- [ethereal - Wiktionary](https://en.wiktionary.org/wiki/ethereal)
- [Ethereal from Wikipedia](https://en.wikipedia.org/wiki/Ethereal)
- [Ether from Wikipedia](https://en.wikipedia.org/wiki/Ether)
- [Ethereal wave from Wikipedia](https://en.wikipedia.org/wiki/Ethereal_wave)
- [Ethereal cardinal from Wikipedia](https://en.wikipedia.org/wiki/Subtle_cardinal)
- [The Ethereal](https://www.truth-is-beauty.com/blog/style-identities-the-ethereal) from [Truth is Beauty](https://www.truth-is-beauty.com/home.html), July 07, 2015
- [Jean-Luc Ponty](Category:Jean-Luc_Ponty "Category:Jean-Luc Ponty") - [Ethereal Mood](https://en.wikipedia.org/wiki/Cosmic_Messenger) (1978), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> A [total eclipse](https://en.wikipedia.org/wiki/Eclipse#Umbra,_penumbra_and_antumbra) of the [Moon](https://en.wikipedia.org/wiki/Moon) is an impressive spectacle. But it also provides another viewing opportunity: a dark, moonlight-free starry sky. At [Cerro Paranal](https://en.wikipedia.org/wiki/Cerro_Paranal) in the Chilean [Atacama Desert](https://en.wikipedia.org/wiki/Atacama_Desert), one of the most remote places in the world, the distance from sources of light pollution makes the night sky all the more remarkable during a total [lunar eclipse](https://en.wikipedia.org/wiki/Lunar_eclipse). This [panoramic photo](https://en.wikipedia.org/wiki/Panoramic_photography), taken by [ESO](https://en.wikipedia.org/wiki/European_Southern_Observatory) Photo Ambassador [Yuri Beletsky](https://www.facebook.com/yuribeletskyphoto), shows the view of the starry sky from the site of ESO’s [Very Large Telescope](https://en.wikipedia.org/wiki/Very_Large_Telescope) (VLT) at Cerro Paranal during the total lunar eclipse of December 21, 2010. The reddish disc of the Moon is seen on the right of the image, while the [Milky Way](https://en.wikipedia.org/wiki/Milky_Way) arches across the heavens in all its beauty. Another faint glow of light is also visible, surrounding the brilliant planet [Venus](https://en.wikipedia.org/wiki/Venus) in the bottom left corner of the picture. This phenomenon, known as [zodiacal light](https://en.wikipedia.org/wiki/Zodiacal_light), is produced by sunlight reflecting off dust in the plane of the planets. It is so faint that it’s normally obscured by moonlight or light pollution. [Image](http://www.eso.org/public/images/potw1119a/) by ESO, Yuri Beletsky, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Beauty from Wikipedia](https://en.wikipedia.org/wiki/Beauty)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Ethereal - Official Release](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=8645) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), June 25, 2016
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Ethereal/README.md at master · AndyGrant/Ethereal · GitHub](https://github.com/AndyGrant/Ethereal/blob/master/README.md)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 09, 2020
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335&start=91) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 09, 2020
1. ↑ [6.0](#cite-ref-ethereal13nnue-6-0) [6.1](#cite-ref-ethereal13nnue-6-1) [Commercial Release of Ethereal 13.00 (NNUE) for AVX2 Systems](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77438) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 04, 2021
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Commercial Release of Ethereal 13.00 (NNUE) for AVX2 Systems](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77438&start=17) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 04, 2021
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> Features based on [GitHub - AndyGrant/Ethereal: Ethereal UCI Chess Engine](https://github.com/AndyGrant/Ethereal)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> Ethereal's 8.60 [Lazy SMP](Lazy_SMP "Lazy SMP") inspired by [Demolito](Demolito "Demolito") by Lucas Braesch, see [Release of Ethereal 8.60 SMP](http://www.talkchess.com/forum/viewtopic.php?t=65968) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 10, 2017
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Evaluation & Tuning in Chess Engines](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74877) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), August 24, 2020
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Ethereal Tuning - Data Dump](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75350) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 10, 2020
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Evaluation & Tuning in Chess Engines](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74877) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), August 24, 2020
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Ethereal Tuning - Data Dump](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75350) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 10, 2020

**[Up one Level](Engines "Engines")**

