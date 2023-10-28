---
title: Hash TablePerfectHashing
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * Hash Table**

\[ A small phone book as a hash table [[1]](#cite_note-1)
A **Hash Table**, or a Hash Map, is a data structure that associates identifiers or keys (names, chess positions) with values (i. e. phone number, score of a position). A [hash function](https://en.wikipedia.org/wiki/Hash_function) is used for turning the key into a relatively small integer, the hash, that serves as an index into an [array](Array "Array").

In a well-dimensioned hash table, the average cost for each lookup is independent of the number of elements stored in the table. In general programming as well in computer chess, hash tables often serve as [cache](https://en.wikipedia.org/wiki/Cache) for once calculated values, to save relative expensive computations over and over again.

## Contents

- [1 Perfect Hashing](#Perfect_Hashing)
- [2 Minimal Perfect Hashing](#Minimal_Perfect_Hashing)
- [3 Search Tables](#Search_Tables)
- [4 Class Libraries](#Class_Libraries)
- [5 Publications](#Publications)
  - [5.1 1968](#1968)
  - [5.2 1970 ...](#1970_...)
  - [5.3 1980 ...](#1980_...)
  - [5.4 1990 ...](#1990_...)
  - [5.5 2000 ...](#2000_...)
  - [5.6 2010 ...](#2010_...)
  - [5.7 2020 ...](#2020_...)
- [6 Forum Posts](#Forum_Posts)
  - [6.1 1998 ...](#1998_...)
  - [6.2 2000 ...](#2000_..._2)
  - [6.3 2005 ...](#2005_...)
  - [6.4 2010 ...](#2010_..._2)
  - [6.5 2015 ...](#2015_...)
  - [6.6 2020 ...](#2020_..._2)
- [7 External Links](#External_Links)
- [8 References](#References)

## Perfect Hashing

\[ A perfect hash function [[2]](#cite_note-2)
If all of the keys are known at compile or initialization time and their cardinality is reasonable small, a perfect hash table can be created, in which there will be no collisions, since each key has an unique index. Opposed to Minimal Perfect Hashing, the lookup [array](Array "Array") contains either gaps or multiple entries.

Applications in computer chess are hashing of masked [occupied bitboards](Occupancy "Occupancy"), to map for instance [attack sets of sliding pieces](Sliding_Piece_Attacks "Sliding Piece Attacks") ([rooks](Rook "Rook"), [bishops](Bishop "Bishop")) on a particular [square](Squares "Squares"), or [pawn shield](King_Safety#PawnShield "King Safety") stuff. [Another application](Material_Tables "Material Tables"), despite a reversible hash function, is a precomputed table indexed by some [material](Material "Material") key, likely an [incremental updated](Incremental_Updates "Incremental Updates") [dot-product](https://en.wikipedia.org/wiki/Dot_product) of all piece-type counts in some fixed order, by a vector of cumulated maximum count products of pieces ordered below, usually ignoring unusual material configurations due to [promotions](Promotions "Promotions") [[3]](#cite_note-3) . Persistent, or on the fly generated [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases") and [Bitbases](Endgame_Bitbases "Endgame Bitbases") containing [perfect knowledge](Knowledge#PerfectKnowledge "Knowledge") by [retrograde analyses](Retrograde_Analysis "Retrograde Analysis") of certain [material](Material "Material") constellations with a few pieces in late endings might be considered as a kind of perfect hashing as well.

- [Walter Faxon's Magic BitScan](BitScan#WalterFaxonsmagicBitscan "BitScan")
- [BitScan by Modulo](BitScan#BitscanByModulo "BitScan")
- [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [Hashing Dictionaries](Hashing_Dictionaries "Hashing Dictionaries")
- [Congruent Modulo Bitboards](Congruent_Modulo_Bitboards "Congruent Modulo Bitboards")
- [Material Tables](Material_Tables "Material Tables")
- [Pawn Shield Tables](index.php?title=Pawn_Shield_Tables&action=edit&redlink=1 "Pawn Shield Tables (page does not exist)")
- [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")

## Minimal Perfect Hashing

\[ Minimal perfect hash function [[4]](#cite_note-4)
If the hash [array](Array "Array") has no gaps and unique, distinct values, so called Minimal Perfect Hashing is applied, like in following [bitboard](Bitboards "Bitboards") hashing for [bitscan](BitScan "BitScan") purpose or determining pre-calculated [move lists](Move_List "Move List") by [move target](Target_Square "Target Square") sets of [knights](Knight "Knight") and [king](King "King").

- [De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan")
- [Matt Taylor's Folding trick](BitScan#MattTaylorsFoldingtrick "BitScan")
- [Hashing Multiple Bits](Bitboard_Serialization#HashingMultipleBits "Bitboard Serialization") for [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization")

## Search Tables

The classical hash table implementation in computer chess are the [transposition tables](Transposition_Table "Transposition Table"), indexed by [Zobrist](Zobrist_Hashing "Zobrist Hashing")- or [BCH keys](BCH_Hashing "BCH Hashing") of the position, modulo number of entries inside the table, to store [search](Search "Search") results, [evaluation](Evaluation "Evaluation"), [pawn structure](Pawn_Structure "Pawn Structure") related stuff and [repetitions](Repetitions "Repetitions").

- [Transposition Table](Transposition_Table "Transposition Table")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [Material Hash Table](Material_Hash_Table "Material Hash Table")
- [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
- [Repetition Hash Table](Repetitions#RepetitionHashTable "Repetitions")
- [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")

## Class Libraries

- [QMap Class Reference](http://doc.trolltech.com/2.3/qmap.html), [C++](Cpp "Cpp") from [Qt On-line Reference Documentation](http://doc.trolltech.com/2.3/index.html)
- [CMap Class](http://msdn.microsoft.com/en-us/library/s897094z%28VS.80%29.aspx), [C++](Cpp "Cpp") from [MFC Library Reference](http://msdn.microsoft.com/en-us/library/d06h2x6e%28VS.80%29.aspx)
- [Interface Map](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Map.html) from the [Java](Java "Java") package [java.util](http://java.sun.com/j2se/1.4.2/docs/api/java/util/package-summary.html)
- [UserDict - Class wrapper for dictionary objects](http://docs.python.org/lib/module-UserDict.html) from [Python Library Reference](http://docs.python.org/lib/lib.html)
- [defaultdict objects](http://docs.python.org/lib/defaultdict-objects.html) from [Python Library Reference](http://docs.python.org/lib/lib.html)

## Publications

## 1968

- [Ward Douglas Maurer](Ward_Douglas_Maurer "Ward Douglas Maurer") (**1968**). *[An Improved Hash Code for Scatter Storage](http://dl.acm.org/citation.cfm?id=357995)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 11, No. 1
- [Elwyn Berlekamp](Elwyn_Berlekamp "Elwyn Berlekamp") (**1968**). *Algebraic Coding Theory*, New York: McGraw-Hill. Revised ed., Aegean Park Press, (**1984**), ISBN 0894120638. [amazon](http://www.amazon.com/Algebraic-Coding-Theory-Revised-M-6/dp/0894120638)
- [F R A Hopgood](http://www.bahfrah.org.uk/bio/index.htm) (**1968**). *[A Solution to the table overflow problem for Hash Tables](http://www.chilton-computing.org.uk/acl/literature/reports/p008.htm)*. [Literature: Reports](http://www.chilton-computing.org.uk/acl/literature/reports/overview.htm) hosted by [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory")

## 1970 ...

- [Albert Zobrist](Albert_Zobrist "Albert Zobrist") (**1970**). *A New Hashing Method with Application for Game Playing*. Technical Report #88, Computer Science Department, The University of Wisconsin, Madison, WI, USA. Reprinted (**1990**) in [ICCA Journal, Vol. 13, No. 2](ICGA_Journal#13_3 "ICGA Journal"), [pdf](http://www.cs.wisc.edu/techreports/1970/TR88.pdf)
- [Burton H. Bloom](https://en.wikipedia.org/wiki/Bloom_filter) (**1970**). *[Space/time trade-offs in hash coding with allowable errors](http://portal.acm.org/citation.cfm?id=362692)*. Comm. of the ACM, Vol. 13, No. 7, [pdf](http://www.lsi.upc.edu/%7Ediaz/p422-bloom.pdf) [[5]](#cite_note-5)
- [F R A Hopgood](http://www.bahfrah.org.uk/bio/index.htm), [J. Davenport](http://people.bath.ac.uk/masjhd/) (**1972**). *[The quadratic hash method when the table size is a power of 2](http://www.chilton-computing.org.uk/acl/literature/reports/p012.htm)*. [Literature: Reports](http://www.chilton-computing.org.uk/acl/literature/reports/overview.htm) hosted by [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory")
- [F R A Hopgood](http://www.bahfrah.org.uk/bio/index.htm) (**1974**). *[Computer Animation used as a Tool in Teaching Computer Science](http://www.chilton-computing.org.uk/acl/literature/reports/p007.htm)*. [Literature: Reports](http://www.chilton-computing.org.uk/acl/literature/reports/overview.htm) hosted by [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory")
- [Ole Amble](http://www.informatik.uni-trier.de/~ley/pers/hd/a/Amble:Ole.html), [Donald Knuth](Donald_Knuth "Donald Knuth") (**1974**). *Ordered Hash Tables*. [The Computer Journal](https://en.wikipedia.org/wiki/The_Computer_Journal), Vol. 17
- [Ward Douglas Maurer](Ward_Douglas_Maurer "Ward Douglas Maurer"), [Ted G. Lewis](http://www.informatik.uni-trier.de/~ley/pers/hd/l/Lewis:Ted_G=) (**1975**). *[Hash Table Methods](http://dl.acm.org/citation.cfm?doid=356643.356645)*. [ACM Computing Surveys](ACM#Surveys "ACM"), Vol. 7, No. 1
- [J. Lawrence Carter](Mathematician#JLCarter "Mathematician"), [Mark N. Wegman](Mathematician#MNWegman "Mathematician") (**1977**). *[Universal classes of hash functions](http://dl.acm.org/citation.cfm?id=803400)*. [STOC '77](http://dl.acm.org/citation.cfm?id=800105)

## 1980 ...

- [Harry Nelson](Harry_Nelson "Harry Nelson") (**1985**). *Hash Tables in Cray Blitz*. [ICCA Journal, Vol. 8, No. 1](ICGA_Journal#8_1 "ICGA Journal") » [Cray Blitz](Cray_Blitz "Cray Blitz")
- [Tony Warnock](Tony_Warnock "Tony Warnock"), [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1988**). *Search Tables in Computer Chess*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
- [Ivan Damgård](Mathematician#IDamgard "Mathematician") (**1989**). *A Design Principle for Hash Functions*. [CRYPTO '89](http://www.informatik.uni-trier.de/~ley/db/conf/crypto/crypto89.html)
- [Ralph C. Merkle](Mathematician#RMerkle "Mathematician") (**1989**). *One Way Hash Functions and DES*. [CRYPTO '89](http://www.informatik.uni-trier.de/~ley/db/conf/crypto/crypto89.html) [[6]](#cite_note-6)

## 1990 ...

- [Zbigniew J. Czech](http://sun.aei.polsl.pl/~zjc/), [George Havas](http://itee.uq.edu.au/~havas/), [Bohdan S. Majewski](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Majewski:Bohdan_S=.html) (**1992**). *An Optimal Algorithm for Generating Minimal Perfect Hash Functions*. Information Processing Letters, Vol. 43, pp. 257–264. [pdf](http://cmph.sourceforge.net/papers/chm92.pdf)
- [Warren D. Smith](Warren_D._Smith "Warren D. Smith") (**1992**). *Hash functions for Binary and Ternary Words*. [NEC Research Institute](https://en.wikipedia.org/wiki/NEC_Corporation_of_America), [ps](http://scorevoting.net/WarrenSmithPages/homepage/gohash.ps)
- [Martin Dietzfelbinger](Mathematician#MDietzfelbinger "Mathematician"), [Anna Karlin](https://en.wikipedia.org/wiki/Anna_Karlin), [Kurt Mehlhorn](Mathematician#KMehlhorn "Mathematician"), [Friedhelm Meyer auf der Heide](Mathematician#FMeyerAdH "Mathematician"), [Hans Rohnert](https://plus.google.com/105803273623353288634/posts), [Robert E. Tarjan](Mathematician#RETarjan "Mathematician") (**1994**). *[Dynamic Perfect Hashing: Upper and Lower Bounds](http://epubs.siam.org/doi/abs/10.1137/S0097539791194094)*. [SIAM Journal on Computing](https://en.wikipedia.org/wiki/SIAM_Journal_on_Computing), Vol. 23, Nr. 4
- [Zbigniew J. Czech](http://sun.aei.polsl.pl/~zjc/), [George Havas](http://itee.uq.edu.au/~havas/), [Bohdan S. Majewski](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Majewski:Bohdan_S=.html) (**1997**). *Perfect Hashing*. Theoretical Computer Science, Vol. 182, Nos. 1-2, pp. 1-143
- [Bob Jenkins](Bob_Jenkins "Bob Jenkins") (**1997**). *Hash functions*. [Dr. Dobb's Journal](https://en.wikipedia.org/wiki/Dr._Dobb%27s_Journal), September 1997 [[7]](#cite_note-7)
- [Donald E. Knuth](Donald_Knuth "Donald Knuth") (**1998**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/~knuth/taocp.html)*. Volume 3 - Sorting and Searching, 6.4 about universal hashing, (second edition), [amazom](http://www.amazon.com/Art-Computer-Programming-Sorting-Searching/dp/0201896850)
- [Dennis Breuker](Dennis_Breuker "Dennis Breuker") (**1998**). *[Memory versus Search in Games](http://www.dennisbreuker.nl/thesis/)*. Ph.D. Thesis, [Universiteit Maastricht](Maastricht_University "Maastricht University"), The Netherlands. ISBN 90-9012006-8.
- [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Harald Prokop](Harald_Prokop "Harald Prokop"), [Keith H. Randall](Keith_H._Randall "Keith H. Randall") (**1998**). *Using de Bruijn Sequences to Index a 1 in a Computer Word*, [pdf](http://supertech.csail.mit.edu/papers/debruijn.pdf) » [BitScan](BitScan "BitScan")

## 2000 ...

- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Tim Mann](Tim_Mann "Tim Mann") (**2002**). *[A lock-less transposition table implementation for parallel search chess engines](http://www.cis.uab.edu/hyatt/hashing.html)*. [ICGA Journal, Vol. 25, No. 1](ICGA_Journal#25_1 "ICGA Journal") » [Shared Hash Table - Lock-less](Shared_Hash_Table#Lockless "Shared Hash Table")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") (**2005**). *[The Effect of Hash Signature Collisions in a Chess Program](http://www.cis.uab.edu/hyatt/collisions.html)*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal")
- [Dimitris Fotakis](Mathematician#DFotakis "Mathematician"), [Rasmus Pagh](Mathematician#RPagh "Mathematician"), [Peter Sanders](Peter_Sanders "Peter Sanders"), [Paul Spirakis](Mathematician#PGSpirakis "Mathematician") (**2005**). *[Space Efficient Hash Tables with Worst Case Constant Access Time](https://link.springer.com/article/10.1007/s00224-004-1195-x)*. [Theory of Computing Systems](https://en.wikipedia.org/wiki/Theory_of_Computing_Systems), Vol. 38, No. 2
- [Sam Tannous](Sam_Tannous "Sam Tannous") (**2007**). *Avoiding Rotated Bitboards with Direct Lookup*. [ICGA Journal, Vol. 30, No. 2](ICGA_Journal#30_2 "ICGA Journal"), [pdf](http://arxiv.org/PS_cache/arxiv/pdf/0704/0704.3773v2.pdf) » [Hashing Dictionaries](Hashing_Dictionaries "Hashing Dictionaries")
- [Kumar Chellapilla](index.php?title=Kumar_Chellapilla&action=edit&redlink=1 "Kumar Chellapilla (page does not exist)"), [Anton Mityagin](Mathematician#AMityagin "Mathematician"), [Denis Xavier Charles](Mathematician#DXCharles "Mathematician") (**2007**). *[GigaHash: scalable minimal perfect hashing for billions of urls](http://www2007.org/poster1018.php)*. [WWW 2007](http://www.informatik.uni-trier.de/%7Eley/db/conf/www/www2007.html#ChellapillaMC07)
- [Trevor Fenner](Trevor_Fenner "Trevor Fenner"), [Mark Levene](Mark_Levene "Mark Levene") (**2008**). *Move Generation with Perfect Hashing Functions.* [ICGA Journal, Vol. 31, No. 1](ICGA_Journal#31_1 "ICGA Journal"), [pdf](http://www.dcs.bbk.ac.uk/~mark/download/bitboard_sliding_icga_final.pdf) » [Congruent Modulo Bitboards](Congruent_Modulo_Bitboards "Congruent Modulo Bitboards")

## 2010 ...

- [Maurizio Monge](Maurizio_Monge "Maurizio Monge") (**2010**). *On perfect hashing of numbers with sparse digit representation via multiplication by a constant*. [arXiv:1003.3196](https://arxiv.org/abs/1003.3196) » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [Jiao Wang](Jiao_Wang "Jiao Wang"), [Si-Zhong Li](index.php?title=Si-Zhong_Li&action=edit&redlink=1 "Si-Zhong Li (page does not exist)"), [Xin-He Xu](Xinhe_Xu "Xinhe Xu") (**2010**). *A Minors Hash Table in Chinese-Chess Programs*. [ICGA Journal, Vol. 33, No. 1](ICGA_Journal#33_1 "ICGA Journal")
- [Mihai Pătrașcu](Mathematician#MPatrascu "Mathematician"), [Mikkel Thorup](Mathematician#MThorup "Mathematician") (**2011**). *The Power of Simple Tabulation Hashing*. [arXiv:1011.5200v2](http://arxiv.org/abs/1011.5200)
- [Dan Anthony Feliciano Alcantara](index.php?title=Dan_Anthony_Feliciano_Alcantara&action=edit&redlink=1 "Dan Anthony Feliciano Alcantara (page does not exist)") (**2011**). *Effcient Hash Tables on the GPU*. Ph.D. thesis, [University of California, Davis](https://en.wikipedia.org/wiki/University_of_California,_Davis), [pdf](http://idav.ucdavis.edu/~dfalcant//downloads/dissertation.pdf) » [GPU](GPU "GPU")
- [John Tromp](John_Tromp "John Tromp") (**2014**). *[Cuckoo Cycle: a memory-hard proof-of-work system](https://github.com/tromp/cuckoo/blob/master/cuckoo.pdf)*. [IACR Cryptology ePrint Archive](http://www.informatik.uni-trier.de/~ley/db/journals/iacr/iacr2014.html#Tromp14) [[8]](#cite_note-8) [[9]](#cite_note-9)
- [David Eppstein](David_Eppstein "David Eppstein"), [Michael T. Goodrich](Mathematician#MTGoodrich "Mathematician"), [Michael Mitzenmacher](Mathematician#MMitzenmacher "Mathematician"), [Paweł Pszona](https://dblp.uni-trier.de/pers/hd/p/Pszona:Pawel) (**2014**). *Wear Minimization for Cuckoo Hashing: How Not to Throw a Lot of Eggs into One Basket*. [arXiv:1404.0286](https://arxiv.org/abs/1404.0286)
- [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [Martin Aumüller](Mathematician#MAumueller "Mathematician"), [Rasmus Pagh](Mathematician#RPagh "Mathematician") (**2016**). *Parameter-free Locality Sensitive Hashing for Spherical Range Reporting*. [arXiv:1605.02673](https://arxiv.org/abs/1605.02673) [[10]](#cite_note-10)
- [Tobias Maier](https://dblp.uni-trier.de/pers/hd/m/Maier:Tobias), [Peter Sanders](Peter_Sanders "Peter Sanders"), [Roman Dementiev](https://dblp.uni-trier.de/pers/hd/d/Dementiev:Roman) (**2016**). *Concurrent Hash Tables: Fast and General?(!)*. [arXiv:1601.04017](https://arxiv.org/abs/1601.04017)
- [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle") (**2017**). *Optimal Set Similarity Data-structures Without False Negatives*. Master thesis, [University of Copenhagen](https://en.wikipedia.org/wiki/University_of_Copenhagen), [pdf](http://www.itu.dk/people/thdy/papers/minhash.pdf) [[11]](#cite_note-11)
- [Tobias Maier](https://dblp.uni-trier.de/pers/hd/m/Maier:Tobias), [Peter Sanders](Peter_Sanders "Peter Sanders") (**2017**). *Dynamic Space Efficient Hashing*. [arXiv:1705.00997](https://arxiv.org/abs/1705.00997)
- [Peter Sanders](Peter_Sanders "Peter Sanders") (**2018**). *Hashing with Linear Probing and Referential Integrity*. [arXiv:1808.04602](https://arxiv.org/abs/1808.04602)

## 2020 ...

- [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas") (**2020**). *[The Hashtable Packing Problem](https://backscattering.de/chess/hashtable-packing/)*. (Draft)
- [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [Jakob Tejs Bæk Knudsen](https://dblp.uni-trier.de/pid/236/4491.html), [Mikkel Thorup](Mathematician#MThorup "Mathematician") (**2020**). *The Power of Hashing with Mersenne Primes*. [arXiv:2008.08654](https://arxiv.org/abs/2008.08654) [[12]](#cite_note-12)

## Forum Posts

## 1998 ...

- [Fast hash algorithm](https://www.stmintz.com/ccc/index.php?id=13810) by John Scalo, [CCC](CCC "CCC"), January 08, 1998 » [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
- [Fast hash key method - Revisited!](https://www.stmintz.com/ccc/index.php?id=14053) by John Scalo, [CCC](CCC "CCC"), January 14, 1998
- [Hash tables and data-cache, some programmer stuff...](https://www.stmintz.com/ccc/index.php?id=14226) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 17, 1998

## 2000 ...

- [A fast hash -- assuming you are not planning to do incremental updates](https://www.stmintz.com/ccc/index.php?id=175221) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 15, 2001
- [Non power of two hash table sizes](https://www.stmintz.com/ccc/index.php?id=214125) by [Alvaro Jose Povoa Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), February 18, 2002

## 2005 ...

- [Hash table and O(1)](https://www.stmintz.com/ccc/index.php?id=484874) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), February 06, 2006
- [What is the Difference between Mainhash, Evalhash, Pawnhash?](http://www.hiarcs.net/forums/viewtopic.php?p=2921) by Thomas Wallendik, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 13, 2007
- [Cache pollution when reading/writing hash table](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=285407) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), August 09, 2009

## 2010 ...

- [Cache-friendier material index](http://www.talkchess.com/forum/viewtopic.php?t=33561) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 31, 2010
- [how to measure frequency of hash collisions](http://www.talkchess.com/forum/viewtopic.php?t=44082) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 16, 2012 » [Key Collisions](Transposition_Table#KeyCollisions "Transposition Table"), [Transposition Table](Transposition_Table "Transposition Table")
- [Hashing based on move lists](http://www.talkchess.com/forum/viewtopic.php?t=48479) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), June 30, 2013

## 2015 ...

- [Hash cache](http://www.talkchess.com/forum/viewtopic.php?t=57924) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 12, 2015 » [Transposition Table](Transposition_Table "Transposition Table")
- [On-the fly hash key generation?](http://www.talkchess.com/forum/viewtopic.php?t=58890) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 12, 2016
- [Crafty's four hash tables](http://www.talkchess.com/forum/viewtopic.php?t=58944) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), January 17, 2016 » [Crafty](Crafty "Crafty")
- [Hashed repetition table](http://www.talkchess.com/forum/viewtopic.php?t=61328) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), September 04, 2016 » [Repetition Hash Table](Repetitions#RepetitionHashTable "Repetitions")
- [Hashing a quadboard from scratch](http://www.talkchess.com/forum/viewtopic.php?t=62239) by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), [CCC](CCC "CCC"), November 23, 2016 » [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards")
- [Magic end-game material hash?](http://www.talkchess.com/forum/viewtopic.php?t=65870) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 30, 2017
- [hashing in chess4j](http://www.talkchess.com/forum/viewtopic.php?t=66183) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), December 30, 2017 » [chess4j](Chess4j "Chess4j"), [Transposition Table](Transposition_Table "Transposition Table")

## 2020 ...

- [hash collisions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72932) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 28, 2020 » [Key Collisions](Transposition_Table#KeyCollisions "Transposition Table")
- [Dense board representation as hash code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72964) by koedem, [CCC](CCC "CCC"), February 01, 2020
- [Hashtable packing (e.g. to optimize magic bitboards) is strongly NP-complete](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73071) by [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas"), [CCC](CCC "CCC"), February 13, 2020 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards") [[13]](#cite_note-13)
- [Zobrist key independence](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73110) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 17, 2020 » [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")

## External Links

- [Hash Table from Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [Hash function from Wikipedia](https://en.wikipedia.org/wiki/Hash_function)
- [Perfect hash function from Wikipedia](https://en.wikipedia.org/wiki/Perfect_hash_function)
- [Cryptographic hash function from Wikipedia](https://en.wikipedia.org/wiki/Cryptographic_hash_function)

[Secure Hash Algorithm from Wikipedia](https://en.wikipedia.org/wiki/Secure_Hash_Algorithm)
[Merkle–Damgård construction from Wikipedia](https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction)

- [gperf - GNU Project](http://www.gnu.org/software/gperf/) - [Free Software Foundation](Free_Software_Foundation "Free Software Foundation")
- [Transposition table from Wikipedia](https://en.wikipedia.org/wiki/Transposition_table)
- [Tabulation hashing from Wikipedia](https://en.wikipedia.org/wiki/Tabulation_hashing)
- [Zobrist hashing from Wikipedia](https://en.wikipedia.org/wiki/Zobrist_hashing)
- [Cuckoo hashing from Wikipedia](https://en.wikipedia.org/wiki/Cuckoo_hashing)
- [Distributed hash table from Wikipedia](https://en.wikipedia.org/wiki/Distributed_hash_table)

[Koorde](https://en.wikipedia.org/wiki/Koorde) based on [Chord](https://en.wikipedia.org/wiki/Chord_%28peer-to-peer%29) and [De Bruijn Sequence](De_Bruijn_Sequence "De Bruijn Sequence")

- [Transposition-driven scheduling - Wikipedia](https://en.wikipedia.org/wiki/Transposition-driven_scheduling)
- [Hashlife from Wikipedia](https://en.wikipedia.org/wiki/Hashlife) by [Bill Gosper](Bill_Gosper "Bill Gosper") [[14]](#cite_note-14)
- [Integer Hash Function](http://www.concentric.net/~Ttwang/tech/inthash.htm) by [Thomas Wang](http://www.concentric.net/~ttwang/index.html)
- [Hash functions](http://www.azillionmonkeys.com/qed/hash.html) by [Paul Hsieh](Paul_Hsieh "Paul Hsieh")
- [Hash Functions and Block Ciphers](http://burtleburtle.net/bob/hash/index.html) by [Bob Jenkins](Bob_Jenkins "Bob Jenkins")
- [A Hash Function for Hash Table Lookup](http://burtleburtle.net/bob/hash/doobs.html) by [Bob Jenkins](Bob_Jenkins "Bob Jenkins")
- [Perfect Hashing](http://burtleburtle.net/bob/hash/perfect.html) by [Bob Jenkins](Bob_Jenkins "Bob Jenkins")
- [Jenkins hash function from Wikipedia](https://en.wikipedia.org/wiki/Jenkins_hash_function)
- [Fowler–Noll–Vo hash function from Wikipedia](https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function)
- [General Purpose Hash Function Algorithms](http://www.partow.net/programming/hashfunctions/index.html) by [Arash Partow](http://www.partow.net/about/index.html)
- [Hash Functions](http://www.cse.yorku.ca/~oz/hash.html)
- [7. Wahl einer geeigneten Hash-Funktion](http://www.fantasy-coders.de/projects/gh/html/x435.html) from [Guugelhupf - Design und Implementation](http://www.fantasy-coders.de/projects/gh/html/index.html) (German)
- [Association P.C.](Category:Association_P.C. "Category:Association P.C.") - Soft Time in a Life Machine, [Berliner Jazztage](https://en.wikipedia.org/wiki/JazzFest_Berlin), November 7, 1971, [NDR](https://en.wikipedia.org/wiki/Norddeutscher_Rundfunk)-[RB](https://en.wikipedia.org/wiki/Radio_Bremen)-[SFB](https://en.wikipedia.org/wiki/Sender_Freies_Berlin) 3 Broadcast, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Pierre Courbois](Category:Pierre_Courbois "Category:Pierre Courbois"), [Jasper van 't Hof](Category:Jasper_van_%27t_Hof "Category:Jasper van 't Hof"), [Toto Blanke](Category:Toto_Blanke "Category:Toto Blanke"), [Sigi Busch](https://de.wikipedia.org/wiki/Sigi_Busch)

## References

1. [↑](#cite_ref-1) [Hash function from Wikipedia](https://en.wikipedia.org/wiki/Hash_function)
1. [↑](#cite_ref-2) [Hash function from Wikipedia](https://en.wikipedia.org/wiki/Hash_function)
1. [↑](#cite_ref-3) [Cache-friendier material index](http://www.talkchess.com/forum/viewtopic.php?t=33561) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 31, 2010
1. [↑](#cite_ref-4) [Hash function from Wikipedia](https://en.wikipedia.org/wiki/Hash_function)
1. [↑](#cite_ref-5) [Bloom filter from Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)
1. [↑](#cite_ref-6) [Merkle–Damgård construction from Wikipedia](https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction)
1. [↑](#cite_ref-7) [A Hash Function for Hash Table Lookup](http://burtleburtle.net/bob/hash/doobs.html) by [Bob Jenkins](Bob_Jenkins "Bob Jenkins"), updated [Dr. Dobb's](https://en.wikipedia.org/wiki/Dr._Dobb%27s_Journal) article
1. [↑](#cite_ref-8) [Cuckoo Cycle: a new memory-hard proof-of-work system](https://bitcointalk.org/index.php?topic=405483.0) by [John Tromp](John_Tromp "John Tromp"), [Bitcoin Forum](https://bitcointalk.org/index.php), January 08, 2014
1. [↑](#cite_ref-9) [Cuckoo hashing from Wikipedia](https://en.wikipedia.org/wiki/Cuckoo_hashing)
1. [↑](#cite_ref-10) [Locality-sensitive hashing from Wikipedia](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)
1. [↑](#cite_ref-11) [MinHash from Wikipedia](https://en.wikipedia.org/wiki/MinHash)
1. [↑](#cite_ref-12) [Mersenne prime from Wikipedia](https://en.wikipedia.org/wiki/Mersenne_prime)
1. [↑](#cite_ref-13) [Strong NP-completeness from Wikipedia](https://en.wikipedia.org/wiki/Strong_NP-completeness)
1. [↑](#cite_ref-14) [Gosper's Algorithm (Hashlife) explained](http://www-users.cs.york.ac.uk/~jowen/hashlife.html)

**[Up one Level](Data "Data")**

