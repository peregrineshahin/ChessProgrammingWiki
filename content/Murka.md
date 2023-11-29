---
title: Murka
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Murka**



[ Murka’s silhouette <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Murka**, (Мурка)  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compliant by [Igor Korshunov](Igor_Korshunov "Igor Korshunov"), written in [C++](Cpp "Cpp"). 
Since his [WildCat](WildCat "WildCat") sources became no longer maintainable, Igor decited to start a new engine from scratch, first released in May 2010 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
In July 2013, the significant improved Murka 3.0 was released <a id="cite-note-3" href="#cite-ref-3">[3]</a>, [tuned](Automated_Tuning "Automated Tuning") with a modified [Nelder–Mead method](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



### Bitboard Infrastructure


Initially starting with [rotated bitboards](Rotated_Bitboards "Rotated Bitboards"), Murka now uses [magic bitboards](Magic_Bitboards "Magic Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). [Bitscan forward](BitScan#Bitscanforward "BitScan") is either done by even [De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan") or [x86-64](X86-64 "X86-64") [processor instruction](BitScan#bsfbsr "BitScan") via the \_BitScanForward64 intrinsic. 
However, on [x86-64](X86-64 "X86-64") for scalar integers with appropriate reduced value range, it is not recommended to use [8-bit](Byte "Byte") or [16-bit](Word "Word") types, but 32-bit [double words](Double_Word "Double Word").




```C++
##ifdef _M_X64
inline uint8 LSB(BitBoard b) // Least Significant Bit
{
   register unsigned long index;
   _BitScanForward64(&index, b);
   return index;
}
##else
const uint8 deBruijnIndex64[64] =
{
   63,  0, 58,  1, 59, 47, 53,  2,
   60, 39, 48, 27, 54, 33, 42,  3,
   61, 51, 37, 40, 49, 18, 28, 20,
   55, 30, 34, 11, 43, 14, 22,  4,
   62, 57, 46, 52, 38, 26, 32, 41,
   50, 36, 17, 19, 29, 10, 13, 21,
   56, 45, 25, 31, 35, 16,  9, 12,
   44, 24, 15,  8, 23,  7,  6,  5
};

inline uint8 LSB(const BitBoard b)
{
   return deBruijnIndex64[((b & -b) * 0x07EDD5E59A4E28C2) >> 58];
}
##endif

```

### Move Generation


The staged [move generator](Move_Generation "Move Generation") uses five routines, one for all moves, and further for [captures](Captures "Captures") and [queening](Promotions "Promotions"), [check evasions](Check#CheckEvasion "Check"), [quiet moves](Quiet_Moves "Quiet Moves"), and finally [checks](Quiescence_Search#Checks "Quiescence Search"), which has a mask to exclude already generated captures.



### Search


Murka applies [fail-soft](Fail-Soft "Fail-Soft") [PVS](Principal_Variation_Search "Principal Variation Search") with [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework at the [root](Root "Root"). [Selectivity](Selectivity "Selectivity") is realized by [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") with [R](Depth_Reduction_R "Depth Reduction R") increased with [depth](Depth "Depth") and on [evaluation](Evaluation "Evaluation") [score](Score "Score") by margin worse than [alpha](Alpha "Alpha"), and [LMR](Late_Move_Reductions "Late Move Reductions") with verification, very aggressively at [Cut-nodes](Node_Types#cut-nodes "Node Types"). [Checks](Check_Extensions "Check Extensions") and [good recaptures](Recapture_Extensions "Recapture Extensions") are [extended](Extensions "Extensions") at [PV-nodes](Node_Types#pv-node "Node Types") only, while [pruning](Pruning "Pruning") is done at shallow depths in too good and too bad positions. [Move ordering](Move_Ordering "Move Ordering") considers [hash move](Hash_Move "Hash Move"), [MVV/LVA](MVV-LVA "MVV-LVA") for good [captures](Captures "Captures") with [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") >= 0, two [killer moves](Killer_Move "Killer Move"), [quiet moves](Quiet_Moves "Quiet Moves") by [history heuristic](History_Heuristic "History Heuristic"), and remaining captures. 
The [quiescence search](Quiescence_Search "Quiescence Search") looks for good captures in MVV/LVA order and [queen promotions](Promotions "Promotions"). At the [horizon](Horizon_Node "Horizon Node"), the first ply of quiescence, [check giving moves](Quiescence_Search#Checks "Quiescence Search") are tried.



### Evaluation Features


* [Material](Material "Material") with adjustment
* [Piece-square tables](Piece-Square_Tables "Piece-Square Tables")
* Recognizing [draw material](Draw_Evaluation "Draw Evaluation")
* [Rooks on open/halfopen files](Rook_on_Open_File "Rook on Open File")
* [Mobility](Mobility "Mobility")
* [King Safety](King_Safety "King Safety")
	+ [Square control](King_Safety#SquareControl "King Safety")
	+ [Pawn shield](King_Safety#PawnShield "King Safety")
	+ [Possibility of castling](Castling_Rights "Castling Rights")
* [Pawn structure](Pawn_Structure "Pawn Structure")
	+ [Open/closed pawns](Open_Pawns_(Bitboards) "Open Pawns (Bitboards)")
	+ [Isolated pawns](Isolated_Pawns_(Bitboards) "Isolated Pawns (Bitboards)")
	+ [Backward pawns](Backward_Pawns_(Bitboards) "Backward Pawns (Bitboards)")
* [Passed pawns](Passed_Pawns_(Bitboards) "Passed Pawns (Bitboards)")
	+ Friendly/opponent piece(s) on passer's [frontspan](Pawn_Spans "Pawn Spans")
	+ [Squares attacked](Square_Control "Square Control") on passer's [frontspan](Pawn_Spans "Pawn Spans") exclusively by opponent
	+ [King passer tropism](King_Pawn_Tropism "King Pawn Tropism")
	+ [Candidates](Candidates_(Bitboards) "Candidates (Bitboards)")
* [Trapped bishop](Trapped_Pieces "Trapped Pieces")
* [Bad bishop](Bad_Bishop "Bad Bishop")
* [Opposite colors bishops ending](Bishops_of_Opposite_Colors "Bishops of Opposite Colors")
* [Side to move bonus](Tempo "Tempo")


## Etymology


Murka (Мурка) is a Russian common pet name for a [cat](https://en.wikipedia.org/wiki/Cat), 
and one of the most famous [Russian chansons](https://en.wikipedia.org/wiki/Russian_chanson) <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 
The original version of the lyrics played by [Konstantin Sokolsky](https://en.wikipedia.org/wiki/Konstantin_Sokolsky) was apparently written by [Odessa](https://en.wikipedia.org/wiki/Odessa) poet [Jacob Yadov](http://ru.wikipedia.org/wiki/%D0%AF%D0%B4%D0%BE%D0%B2,_%D0%AF%D0%BA%D0%BE%D0%B2_%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%87) in 1923 .



## See also


* [CookieCat](CookieCat "CookieCat")
* [WildCat](WildCat "WildCat")


## Forum Posts


* [Murka 3.0 released](http://www.talkchess.com/forum/viewtopic.php?t=48673) by Günther Höhne, [CCC](CCC "CCC"), July 17, 2013
* [You are from Russia !!!!!](http://www.talkchess.com/forum/viewtopic.php?t=48775) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), July 28, 2013


## External Links


### Chess Engine


* [Downloads](http://www.sdchess.ru/download_engines.htm) from [sdchess.ru](http://www.sdchess.ru/)
* [Murka](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Murka&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/15](CCRL "CCRL")


### Misc


* [Мурка — Википедия](http://ru.wikipedia.org/wiki/%D0%9C%D1%83%D1%80%D0%BA%D0%B0) (Russian)
* [Мурка (значения, disambiguation) — Википедия](http://ru.wikipedia.org/wiki/%D0%9C%D1%83%D1%80%D0%BA%D0%B0_%28%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%29) (Russian)
* [Murka – Wikipedia.de](http://de.wikipedia.org/wiki/Murka) (German)
* [Леонид Утёсов](http://ru.wikipedia.org/wiki/%D0%A3%D1%82%D1%91%D1%81%D0%BE%D0%B2,_%D0%9B%D0%B5%D0%BE%D0%BD%D0%B8%D0%B4_%D0%9E%D1%81%D0%B8%D0%BF%D0%BE%D0%B2%D0%B8%D1%87): не спетая "Мурка" вторая половина 1920х, ([Leonid Utyosov](https://en.wikipedia.org/wiki/Leonid_Utyosov) - Murka, late 20s), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Силуэт сидящей кошки Мурки, [Sitting cat Murka’s silhouette](http://commons.wikimedia.org/wiki/File:Cat_Murka_silhouette.svg) by [AVRS](http://commons.wikimedia.org/wiki/User:AVRS), January 2007
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> Мурка / Murka by [Wildcat](Igor_Korshunov "Igor Korshunov"), [immortalchess](Computer_Chess_Forums "Computer Chess Forums"), May 31, 2010 (Russian, no longer available)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Murka 3.0 released](http://www.talkchess.com/forum/viewtopic.php?t=48673) by Günther Höhne, [CCC](CCC "CCC"), July 17, 2013
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> Re: Мурка / Murka # 852 by [Wildcat](Igor_Korshunov "Igor Korshunov"), [immortalchess](Computer_Chess_Forums "Computer Chess Forums"), December 11, 2011 (Russian, no longer available)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> Description based on Murka\_3.rar/Murka\_3/description\_eng.txt
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Мурка (значения, disambiguation) — Википедия](http://ru.wikipedia.org/wiki/%D0%9C%D1%83%D1%80%D0%BA%D0%B0_%28%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%29) (Russian)

**[Up one Level](Engines "Engines")**







 
