---
title: Evaluation Hash Table
---
**[Home](Home "Home") * [Evaluation](Evaluation "Evaluation") * Evaluation Hash Table**

An **Evaluation Hash Table** may be used in a similar fashion as the [transposition table](Transposition_Table "Transposition Table"), that is using [Zobrist-](Zobrist_Hashing "Zobrist Hashing") or [BCH-hashing](BCH_Hashing "BCH Hashing"), to cache various computational expensive positional evaluation scores and flags. Despite the fact that the transposition table entries may contain evaluation scores as well, a tighter, dedicated evaluation hash table with its own replacement policy may gain a considerable amount of additional hits.

## Contents

- [1 See also](#see-also)
- [2 Forum Posts](#forum-posts)
  - [2.1 1998 ...](#1998-...)
  - [2.2 2000 ...](#2000-...)
  - [2.3 2010 ...](#2010-...)

## See also

- [BCH Hashing](BCH_Hashing "BCH Hashing")
- [Hash Table](Hash_Table "Hash Table")
- [Material Hash Table](Material_Hash_Table "Material Hash Table")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")

## Forum Posts

## 1998 ...

- [Hash tables and data-cache, some programmer stuff...](https://www.stmintz.com/ccc/index.php?id=14226) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 17, 1998

## 2000 ...

- [Pawn and Eval hash tables](https://www.stmintz.com/ccc/index.php?id=151211) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), January 21, 2001
- [Evaluation cache](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4620&p=23957) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 03, 2006 » [Snitch](Snitch "Snitch")
- [What is the Difference between Mainhash, Evalhash, Pawnhash?](http://www.hiarcs.net/forums/viewtopic.php?p=2921) by Thomas Wallendik, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 13, 2007

## 2010 ...

- [Stockfish 1.8 - eval cache](http://www.talkchess.com/forum/viewtopic.php?t=35496) by [Ralph Stoesser](index.php?title=Ralph_Stoesser&action=edit&redlink=1 "Ralph Stoesser (page does not exist)"), [CCC](CCC "CCC"), July 18, 2010 » [Stockfish](Stockfish "Stockfish")
- [crafty eval cache](http://www.talkchess.com/forum/viewtopic.php?t=58758) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), January 01, 2016 » [Crafty](Crafty "Crafty")
- [hash eval, hash pawn or twice ?](http://www.talkchess.com/forum/viewtopic.php?t=59566) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), March 19, 2016 » [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Using evaluation hash score as current bestscore (initial guess)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70938) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 06, 2019
- [Eval hashtable replacement scheme](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72030) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), October 08, 2019

**[Up one level](Evaluation "Evaluation")**

