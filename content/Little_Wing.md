---
title: Little Wing
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Little Wing**



[ The Jimi Hendrix Experience <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Little Wing**,  

a free [open source chess engine](Category:Open_Source "Category:Open Source") by [Vincent Ollivier](Vincent_Ollivier "Vincent Ollivier"), written in [Rust](Rust "Rust"), supporting the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") as well as [UCI](UCI "UCI"), 
distributed under the terms of the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") version 3. 
Little Wing is work in progress started in December 2014 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
As [bitboard](Bitboards "Bitboards") engine, Little Wing relies on Rust primitive type **u64** <a id="cite-note-3" href="#cite-ref-3">[3]</a>, which also features [trailing zero count](BitScan#TrailingZeroCount "BitScan") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and [population count](Population_Count "Population Count") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 
So far, [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") - even for single pieces - are computed by a [generalized loop fill](Dumb7Fill#GeneralizedRays "Dumb7Fill") along the rays <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Staged Move Generation](Move_Generation#Staged "Move Generation")


### [Search](Search "Search")


* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")


 [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [MVV/LVA](MVV-LVA "MVV-LVA")
* [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [Quiescence Search](Quiescence_Search "Quiescence Search")


### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")
* [Mobility](Mobility "Mobility")


## See also


* [Purple Haze](Purple_Haze "Purple Haze")
* [Wing](Wing "Wing")
* [Winglet](Winglet "Winglet")


## Postings


* [Re: Learning to program in RUST, together](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=54780&start=5) by [Vincent Ollivier](Vincent_Ollivier "Vincent Ollivier"), [CCC](CCC "CCC"), December 29, 2014
* [Little Wing Chess Engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=56788) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 27, 2015
* [Little Wing v0.4.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65775) by [Vincent Ollivier](Vincent_Ollivier "Vincent Ollivier"), [CCC](CCC "CCC"), November 20, 2017
* [Little Wing 0.4.0 is out! - Vinc](https://vinc.cc/blog/2017/11/20/little-wing-0-4-0-is-out/) by [Vincent Ollivier](Vincent_Ollivier "Vincent Ollivier"), November 20, 2017
* [Little Wing 0.5.0 released - Vinc](https://vinc.cc/blog/2018/07/18/little-wing-0-5-0-released/) by [Vincent Ollivier](Vincent_Ollivier "Vincent Ollivier"), July 18, 2018
* [Little Wing 0.5.0 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68016) by [Vincent Ollivier](Vincent_Ollivier "Vincent Ollivier"), [CCC](CCC "CCC"), July 18, 2018


## External Links


### Chess Engine


* [Little Wing](https://vinc.cc/projects/littlewing.html)
* [GitHub - vinc/littlewing: Bitboard chess engine written in Rust](https://github.com/vinc/littlewing)


### Misc


* [Jimi Hendrix](Category:Jimi_Hendrix "Category:Jimi Hendrix") - Solo [Little Wing](https://en.wikipedia.org/wiki/Little_Wing), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
* [Nguyên Lê](Category:Nguy%C3%AAn_L%C3%AA "Category:Nguyên Lê") et [Cathy Renoir](https://www.discogs.com/artist/426356-Cathy-Renoir) - Little Wing, [ina.fr](https://en.wikipedia.org/wiki/Institut_national_de_l%27audiovisuel), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Promotional photo](https://commons.wikimedia.org/wiki/File:Jimi_Hendrix_experience_1968.jpg) of [The Jimi Hendrix Experience](https://en.wikipedia.org/wiki/The_Jimi_Hendrix_Experience), Back is stamped November 22, 1968, [Warner](https://en.wikipedia.org/wiki/Warner_Bros._Records)/[Reprise Records](https://en.wikipedia.org/wiki/Reprise_Records)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Little Wing](https://vinc.cc/projects/littlewing.html)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [u64 - Rust](https://doc.rust-lang.org/std/primitive.u64.html)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [u64 - Rust: trailing\_zeros](https://doc.rust-lang.org/std/primitive.u64.html#method.trailing_zeros)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [u64 - Rust: count\_ones](https://doc.rust-lang.org/std/primitive.u64.html#method.count_ones)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [littlewing/attack.rs at master · vinc/littlewing · GitHub](https://github.com/vinc/littlewing/blob/master/src/attack.rs)

**[Up one level](Engines "Engines")**







 
