---
title: Pawn Hash Table
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* [Pawn Structure](Pawn_Structure "Pawn Structure") \* Pawn Hash Table**



 [](http://www.elke-rehder.de/Chess_Woodcuts.htm) Pawns threaten the King <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
A **Pawn Hash Table** is often used inside a chess programs to [cache](https://en.wikipedia.org/wiki/Cache) purely [pawn](Pawn "Pawn") related [pattern](Pawn_Pattern_and_Properties "Pawn Pattern and Properties") and [evaluation](Pawn_Structure "Pawn Structure") stuff. Compared to the [main transposition table](Transposition_Table "Transposition Table"), since the [pawn structure](Pawn_Structure "Pawn Structure") inside the [search](Search "Search") changes rarely or transpose, the number of cached entries required might be quite low (a few K) to get a sufficient hit rate above 95% or even 99% for most positions, specially if the pawn structure is settled or relatively fixed after the [opening](Opening "Opening"). On the other hand, most programmers store not only pure aggregated pawn evaluation scores, but other computation expensive pawn structure stuff which is used in second pass [evaluation](Evaluation "Evaluation") considering [pieces](Pieces "Pieces") and [king](King "King"). Terms for various [game phases](Game_Phases "Game Phases") and king origins for all possible wings/center per side are often calculated [speculatively](https://en.wikipedia.org/wiki/Speculative_execution), i.e. pawn shield or pawn storm stuff later used by [king safety](King_Safety "King Safety").


While the content of the pawn hash table entry varies a lot between different chess programs and their implementation, it is not uncommon that one entry exceeds 1/2 K-Byte. Some programs store sets or [bitboards](Bitboards "Bitboards") of strong pawns ([passers](Passed_Pawn "Passed Pawn"), [candidates](Candidate_Passed_Pawn "Candidate Passed Pawn")), square of most advanced passer, different kind of [weak pawn sets](Weak_Pawns "Weak Pawns") and whatever else. Despite, some programs cache pawn-king stuff separately which requires king squares included inside the index calculation as well table entry for verifications. 



### Contents


* [1 Pawn Hash Index](#pawn-hash-index)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
	+ [3.1 1999](#1999)
	+ [3.2 2000 ...](#2000-...)
	+ [3.3 2005 ...](#2005-...)
	+ [3.4 2010 ...](#2010-...)
	+ [3.5 2015 ...](#2015-...)
* [4 External Links](#external-links)
* [5 References](#references)






Most simple, common and recommend is to keep an [incremental updated](Incremental_Updates "Incremental Updates"), dedicated [Zobrist](Zobrist_Hashing "Zobrist Hashing")- or [BCH-keys](BCH_Hashing "BCH Hashing") similar to the [main transposition table](Transposition_Table "Transposition Table"), initialized from all squares occupied by pawns only, [side to move](Side_to_move "Side to move") does not matter. The update of that key is therefor only necessary for the relative rare pawn moves or captures with pawns as aggressor or victim. The hash table index is computed by key modulo number of entries, which might be a cheap and-instruction from the key for power of two sized tables.


Alternatively, considering hits from the [transposition table](Transposition_Table "Transposition Table"), or a dedicated [evaluation hash table](Evaluation_Hash_Table "Evaluation Hash Table"), one may use a fast [hash function](Hash_Table "Hash Table") to compute an index from the white and black pawn bitboards on the fly, i.e. either a modulo or a multiplication and shift à la [magic bitboards](Magic_Bitboards "Magic Bitboards") by the difference of the disjoint pawn sets <a id="cite-note-2" href="#cite-ref-2">[2]</a> . To verify correct entries while probing, one needs either to store (a part) of the dedicated Zobrist/BCH key, or for 100% correctness 2\*48 bits from the pawn occupancy bitboards. This value could be further compressed with the expense of more calculation overhead by means of n-like men:



 [](File:PawnHashFormla.jpg) 
This can be further reduced by mirroring the board, considering symmetric positions or detecting illegal positions. 



## See also


* [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [Hash Table](Hash_Table "Hash Table")
* [Material Hash Table](Material_Hash_Table "Material Hash Table")
* [Material Tables](Material_Tables "Material Tables")
* [Transposition Table](Transposition_Table "Transposition Table")


## Forum Posts


### 1999


* [Q: pawn hash?](https://www.stmintz.com/ccc/index.php?id=61063) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), July 20, 1999
* [regular hash key & pawn hash key together - good idea?](https://www.stmintz.com/ccc/index.php?id=68872) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), September 16, 1999


### 2000 ...


* [A question about pawn hash tables](https://www.stmintz.com/ccc/index.php?id=129406) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [CCC](CCC "CCC"), September 13, 2000
* [A few hashing questions](https://www.stmintz.com/ccc/index.php?id=200037) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 02, 2001
* [Pawn Hash Collisions in Crafty](https://www.stmintz.com/ccc/index.php?id=200496) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), December 05, 2001
* [Crafty's 32-bit pawn hash collision figures?](https://www.stmintz.com/ccc/index.php?id=200800) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 06, 2001
* [Pawn hash table: need some helps?](https://www.stmintz.com/ccc/index.php?id=237159) by [Pham Hong Nguyen](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), June 23, 2002
* [Ultra small pawn hash efficiency](https://www.stmintz.com/ccc/index.php?id=266544) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), November 21, 2002
* [programmers: pawn hash tables](https://www.stmintz.com/ccc/index.php?id=288402) by Joel, [CCC](CCC "CCC"), March 08, 2003
* [pawn hash tables](https://www.stmintz.com/ccc/index.php?id=309379) by Joshua Lee, [CCC](CCC "CCC"), August 01, 2003
* [The key of pawn hash tables is based on what exactly?](https://www.stmintz.com/ccc/index.php?id=314386) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), September 06, 2003
* [Pawn hashing without Zobrist keys](https://www.stmintz.com/ccc/index.php?id=315478) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), September 12, 2003
* [Pawn Hash Question](https://www.stmintz.com/ccc/index.php?id=354696) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), March 15, 2004
* [Which pawn positions go into a pawn hash table?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/cfe3b4da78ee890b/928457251da6ff40) by pd42, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 26, 2004
* [pawn hash](https://www.stmintz.com/ccc/index.php?id=373656) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), July 03, 2004
* [Initialization of pawn hash table](https://www.stmintz.com/ccc/index.php?id=389201) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), September 26, 2004


### 2005 ...


* [About pawn hash tables](http://www.talkchess.com/forum/viewtopic.php?t=13673) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 10, 2007
* [An interesting bug in Hamsters](http://www.talkchess.com/forum/viewtopic.php?t=15540) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), August 02, 2007 » [Hamsters](Hamsters "Hamsters")


### 2010 ...


* [Pawn Hash](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=32509) by [Philippe Gailhac](Philippe_Gailhac "Philippe Gailhac"), [CCC](CCC "CCC"), February 10, 2010
* [Pawn Hash](http://www.talkchess.com/forum/viewtopic.php?t=33334) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 18, 2010
* [Possible pawn hash speed optimization?](http://www.talkchess.com/forum/viewtopic.php?t=40470) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), September 19, 2011
* [Is there a reasonable number of pawn hash entries?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=44369) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), July 10, 2012


### 2015 ...


* [pawn hash and ep](http://www.talkchess.com/forum/viewtopic.php?t=59126) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), February 01, 2016
* [Buckets for pawn hash?](http://www.talkchess.com/forum/viewtopic.php?t=59154) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), February 04, 2016
* [pawn hash and eval tuning](http://www.talkchess.com/forum/viewtopic.php?t=59319) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), February 21, 2016 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [hash eval, hash pawn or twice ?](http://www.talkchess.com/forum/viewtopic.php?t=59566) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), March 19, 2016 » [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [Pawn hash](http://www.talkchess.com/forum/viewtopic.php?t=61621) by [Karlo Balla](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), October 06, 2016
* [pawn hash](http://www.talkchess.com/forum/viewtopic.php?t=62160&start=10) by [Volker Annuss](Volker_Annuss "Volker Annuss"), [CCC](CCC "CCC"), November 18, 2016
* [A pre-calculated pawn hash table ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71190) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 05, 2019
* [Pawn hash table, a little disappointment](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72195) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), October 28, 2019


## External Links


* [Transposition table - Related techniques, from Wikipedia](https://en.wikipedia.org/wiki/Transposition_table#Related_techniques)
* [Chess Engine Anomalies, evidently caused by hash-table collisions and effects of multithreading](http://www.cse.buffalo.edu/~regan/chess/computer/anomalies/DF10anomalies.htm) by [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess Woodcuts Graphic Arts Woodcut Art](http://www.elke-rehder.de/Chess_Woodcuts.htm) by [Elke Rehder](Arts#Rehder "Arts")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Pawn hashing without Zobrist keys](https://www.stmintz.com/ccc/index.php?id=315478) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), September 12, 2003

**[Up one level](Pawn_Structure "Pawn Structure")**







 
