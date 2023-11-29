---
title: HeavyChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * HeavyChess**

[](https://www.flickr.com/photos/teosaurio/4531534307/in/photostream/) Heavy Chess <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**HeavyChess**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Chispa](Chispa "Chispa") author [Federico Andrés Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), written in [C++](Cpp "Cpp"), released in 2007 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Description

## Board Representation

HeavyChess is a [bitboard](Bitboards "Bitboards") engine and uses compact [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). It performs eight [byte lookups](Population_Count#Lookup "Population Count") to [count populations](Population_Count "Population Count"), and [bitscan](BitScan "BitScan") by conditional 64k lookups, where the most significant bit on the chess board maps the least significant arithmetical one <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```C++
// Devuelve el Most Significant Bit de un Bitboard
inline Casilla Bitboards::MSB(const Bitboard &b) {
   if (b&65535) return static_cast<Casilla>(TablaMSB[b&65535]);
   if (b&MSBMask1) return static_cast<Casilla>(TablaMSB[(b>>16)&65535]+16);
   if (b&MSBMask2) return static_cast<Casilla>(TablaMSB[(b>>32)&65535]+32);
   return static_cast<Casilla>(TablaMSB[b>>48]+48);
}

```

## Search

HeavyChess applies [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table") and [null move pruning](Null_Move_Pruning "Null Move Pruning"), [mate theat](Mate_Threat_Extensions "Mate Threat Extensions") and [check extensions](Check_Extensions "Check Extensions") inside a [fractional ply](Depth#FractionalPlies "Depth") [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows").

## Evaluation

The [evaluation](Evaluation "Evaluation") seems not that heavy as the program's name suggests. Beside obligatory, [incremental updated](Incremental_Updates "Incremental Updates") [material balance](Material#Balance "Material"), HeavyChess utilizes [piece-square tables](Piece-Square_Tables "Piece-Square Tables") and considers various piece terms, such as [bishop pair](Bishop_Pair "Bishop Pair"), [rook on (half) open file](Rook_on_Open_File "Rook on Open File"), and [rook on 7th rank](Rook_on_Seventh "Rook on Seventh").

## See also

- [Chispa](Chispa "Chispa")

## Forum Posts

- [HeavyChess](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=49475) by [Ron Murawski](Ron_Murawski "Ron Murawski"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 09, 2008
- [Heavychess](http://www.talkchess.com/forum/viewtopic.php?t=29307) by Mark Mason, [CCC](CCC "CCC"), August 09, 2009

## External Links

- [Index of /fedecorigliano/ajedrez/heavychess](http://www.oocities.org/ar/fedecorigliano/ajedrez/heavychess/)
- [Index of /chess/engines/Norbert's collection/HeavyChess 0.13 beta/HeavyChess](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/HeavyChess%200.13%20beta/HeavyChess/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [HeavyChess 0.13 beta](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=HeavyChess+0.13+beta) in [CCRL 40/2](CCRL "CCRL")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chessboard](Chessboard "Chessboard") and [pieces](Pieces "Pieces") made out of [mining](https://en.wikipedia.org/wiki/Mining) tools and parts in [Cerro Sombrero](https://en.wikipedia.org/wiki/Cerro_Sombrero), [Chile](https://en.wikipedia.org/wiki/Chile). [Flickr Photo](https://www.flickr.com/photos/teosaurio/4531534307/in/photostream/) by [Mr. Hicks](https://www.flickr.com/photos/teosaurio/), March 08, 2010
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [HeavyChess](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=49475) by [Ron Murawski](Ron_Murawski "Ron Murawski"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 09, 2008
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> HeavyChess 0.13 \\BitBoards.h

**[Up one Level](Engines "Engines")**

