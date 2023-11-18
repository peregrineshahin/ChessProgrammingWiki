---
title: Bitfoot
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bitfoot**

**Bitfoot**,

a version of [Clubfoot](Clubfoot "Clubfoot"), the [UCI](UCI "UCI") [open source chess engine](Category:Open_Source "Category:Open Source") written by [Shawn Chidester](Shawn_Chidester "Shawn Chidester") in [C++](Cpp "Cpp"), that uses [bitboards](Bitboards "Bitboards") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. The [search](Search "Search") mechanics of this engine are identical to those used in Clubfoot. The differences are [board representation](Board_Representation "Board Representation"), [move generation](Move_Generation "Move Generation"), and [positional evaluation](Evaluation "Evaluation"). Bitfoot uses bitboard for board representaion, Clubfoot uses [0x88](0x88 "0x88") board representation. Move generation is strongly tied to board representation so move generation between the two engines is implicitly different. Positional evaluation in Bitfoot takes advantage of the capabilities enabled by using bitboards. So Bitfoot's positional evaluation is much more advanced than Clubfoot's. That being said, Bitfoot's positional evaluation is still relatively dump compared to many of today's top engines.

## A/B Bitboards

Bitfoot applies an own technique to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") dubbed **A/B Bitboards** or Above/Below Bitboards <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Similar to the [classical approach](Classical_Approach "Classical Approach"), it works ray-wise and uses pre-calculated [ray-attacks](On_an_empty_Board#RayAttacks "On an empty Board") for each of the eight [ray-directions](Rays#RayDirections "Rays") and each of the 64 [squares](Squares "Squares"). It has to distinguish between [positive](On_an_empty_Board#PositiveRays "On an empty Board") and [negative](On_an_empty_Board#NegativeRays "On an empty Board") directions, because it has to [isolate](General_Setwise_Operations#LS1BIsolation "General Setwise Operations") or [bitscan](BitScan "BitScan") the first blocker (if any) from the ray-attack intersection with the [occupancy](Occupancy "Occupancy") in different orders. The exclusion of squares behind the first blocker works by intersection with its appropriate [below or above separation](General_Setwise_Operations#LS1BSeparation "General Setwise Operations"). This is how the routines look like conform to the [classical approach](Classical_Approach "Classical Approach") prototype:

```C++

U64 rayAttacks[8][64];

U64 getPositiveRayAttacks(U64 occupied, enumDir dir8, enumSquare square) {
  U64 x = rayAttacks[dir8][square] & occupied;
  x = x & -x; // LSB (if any)
  return x | (rayAttacks[dir8][square] & (x-1)); // BELOW
}

U64 getNegativeRayAttacks(U64 occupied, enumDir dir8, enumSquare square) {
  U64 x = rayAttacks[dir8][square] & occupied;
  x = x ? C64(1) << bitScanReverse(x) : C64(0); // MSB (if any)
  return x | (rayAttacks[dir8][square] & (x^-x)); // ABOVE
}

```

There are further versions of the routines leaving distinct sets of attacked blocker (and possible [capture](Captures "Captures") targets) or attacked empty squares, target of [quiet moves](Quiet_Moves "Quiet Moves"). In a February 2020 [CCC](CCC "CCC") discussion, [Martin Sedlak](Martin_Sedlak "Martin Sedlak") came up with a similar idea <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## See also

- [Clubfoot](Clubfoot "Clubfoot")

## Forum Posts

- [Introducing Bitfoot](http://www.talkchess.com/forum/viewtopic.php?t=56625) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), June 08, 2015
- [New Clubfoot and Bitfoot release builds available](http://www.talkchess.com/forum/viewtopic.php?t=57536) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), September 07, 2015

## External Links

- [zd3nik/Bitfoot · GitHub](https://github.com/zd3nik/Bitfoot)
- [Brecker Brothers](https://en.wikipedia.org/wiki/Brecker_Brothers) - Above and Below, ..., from [Return of the Brecker Brothers](<https://en.wikipedia.org/wiki/Return_of_the_Brecker_Brothers#Return_of_the_Brecker_Brothers_%E2%80%93_Live_in_Barcelona_(VHS)>), [Barcelona](https://en.wikipedia.org/wiki/Barcelona), 1992, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Michael Brecker](Category:Michael_Brecker "Category:Michael Brecker"), [Randy Brecker](Category:Randy_Brecker "Category:Randy Brecker"), [Mike Stern](Category:Mike_Stern "Category:Mike Stern"), [Dennis Chambers](Category:Dennis_Chambers "Category:Dennis Chambers"), [George Whitty](https://en.wikipedia.org/wiki/George_Whitty), [James Genus](https://en.wikipedia.org/wiki/James_Genus)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Bitfoot/README.md at master · zd3nik/Bitfoot · GitHub](https://github.com/zd3nik/Bitfoot/blob/master/README.md)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [A/B Bitboards from Bitfoot/README.md at master · zd3nik/Bitfoot · GitHub](https://github.com/zd3nik/Bitfoot/blob/master/README.md#ab-bitboards)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [scan-cut slider attack generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73082) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 13, 2020

**[Up one Level](Engines "Engines")**

