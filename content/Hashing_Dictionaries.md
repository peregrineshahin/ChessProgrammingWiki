---
title: Hashing Dictionaries
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") * Hashing Dictionaries**

This approach using associate arrays or [hash tables](Hash_Table "Hash Table") was introduced in the [ICGA Journal](ICGA_Journal "ICGA Journal") (June 2007) by [Sam Tannous](Sam_Tannous "Sam Tannous") [[1]](#cite-note-icgaj-1). Like other [occupancy](Occupancy "Occupancy") lookup approaches it works line-wise for ranks, files, diagonals and anti-diagonals. It uses hash arrays from an interpreted, high level language, [Python](Python "Python"):

```C++
Many high level programming languages (notably [Python](Python "Python") (van Rossum, 1993)) have useful predefined data structures (e.g. associative arrays) which are dynamically resizable hash tables that resolve collisions by probing techniques. The basic lookup function used in Python is based on Algorithm D: Open Addressing with Double Hashing from Section 6.4 in Knuth <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 

```

## Avoiding Rotated Bitboards

Sam Tannous compared this approach to a [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards") implementation in Python and found direct lookup favorable for move generation. In languages like [C](C "C"), targeting 64-bit cpus like [x86-64](X86-64 "X86-64"), or even in [Java](Java "Java"), it is likely another story if one compares *Open Addressing with Double Hashing* with [rotated](Rotated_Bitboards "Rotated Bitboards") or [perfect hashing](Hash_Table#PerfectHashing "Hash Table") techniques like [Kindergarten](Kindergarten_Bitboards "Kindergarten Bitboards") or even [Magic Bitboards](Magic_Bitboards "Magic Bitboards").

## Abstract

Quoted from *Avoiding Rotated Bitboards with Direct Lookup* [[1]](#cite-note-icgaj-1):

```C++
This paper describes an approach for obtaining direct access to the attacked squares of sliding pieces without resorting to rotated bitboards. The technique involves creating four [hash tables](Hash_Table "Hash Table") using the built in hash arrays from an interpreted, high level language. The rank, file, and diagonal occupancy are first isolated by masking the desired portion of the board. The attacked squares are then directly retrieved from the hash tables. Maintaining incrementally updated rotated bitboards becomes unnecessary as does all the updating, mapping and shifting required to access the attacked squares. Finally, rotated bitboard move generation speed is compared with that of the direct hash table lookup method. 

```

## Toolkit

- [Shatranj (Toolkit)](</Shatranj_(Toolkit)> "Shatranj (Toolkit)")

## Forum Posts

- [Re: Explain like I'm five - what is the 'n' in right shift 6](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=40503&start=10) by Bayowulf, [CCC](CCC "CCC"), September 24, 2011
- [What is the point of magic hashing over simply using masked occupancy as index ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77648) by Gautier Blandin, [CCC](CCC "CCC"), July 06, 2021 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")

## References

1. ↑ [1.0](#cite-ref-icgaj-1-0) [1.1](#cite-ref-icgaj-1-1) [Sam Tannous](Sam_Tannous "Sam Tannous") (**2007**). *Avoiding Rotated Bitboards with Direct Lookup*. [ICGA Journal, Vol. 30, No. 2](ICGA_Journal#30_2 "ICGA Journal"), [arXiv:0704.3773](https://arxiv.org/abs/0704.3773)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Donald Knuth](Donald_Knuth "Donald Knuth") (**1998**). *The Art of Computer Programming*. Volume 3, Sorting and Searching. Addison Wesley. ISBN 0201896850

**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**

