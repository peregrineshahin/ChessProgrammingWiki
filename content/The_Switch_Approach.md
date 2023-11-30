---
title: The Switch Approach
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") \* The Switch Approach**


The **Switch Approach** was proposed by [Dann Corbit](Dann_Corbit "Dann Corbit"). It was not exclusively in the context of sliding attacks but [move generation](Move_Generation "Move Generation") and determining [pins](Pin "Pin") and all stuff possible on a line. The idea was to use a 64-bit [switch statement](https://en.wikipedia.org/wiki/Switch_statement) on the masked relevant bits and to immediate return appropriate constants. With up to 32, 64 or 128 cases per switch, the compiler will likely divide and conquer by compare or test and conditional jump chain. The switch on square is usually translated as indirect jump, alternatively one may use a explicit table of function pointers in [C](C "C")/[C++](Cpp "Cpp").


This is how it works for pure attacks, considering the [inner six](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") occupied bits. The source code is intended to be generated, using [all subsets of a set](Traversing_Subsets_of_a_Set "Traversing Subsets of a Set") for the cases and one of the mentioned attack-getters to calculate the return values. Since only the nearest blocker define the relevant attack-sets, a lot of switches share a common case and reduce the number of tests and compares far below log2 of all cases.





|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](Square_Mapping_Considerations "Square Mapping Considerations")  | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*.
 |



```C++

U64 diagonalAttacks(U64 occ, enumSquare sq)
{
   switch (sq)
   {
   ...
   case 36: return diagonalAttacksE5(occ);
   ...
   }
}

U64 diagonalAttacksE5(U64 occ)
{
   switch (occ & C64(0x0040200008040200))
   {
   // all 32 cases for all inner six occupied bits excluding e5
   case C64(0x0040200008040200): return C64(0x0000200008000000);
   case C64(0x0040200008040000): return C64(0x0000200008000000);
   ...
   case C64(0x0000000000000000): return C64(0x8040200008040201);
   }
}

...

```

An "average" case requires one indirect jump by square, and 2.x tests or compares with jump above, jump below and that like. If the relevant occupancy don't change that randomly per square used, the prediction rate should be quite fine on todays processors. Of course at some point it may pollute branch prediction resources. On the other hand it does not stall on memory reads and needs no further computation but only moving a immediate 64-bit constant into one register (which takes of course about ten code bytes).


**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**







 
