---
title: Material Hash Table
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* [Material](Material "Material") \* Material Hash Table**


A **Material Hash Table** is used to cache once calculated material values for certain material constellations, considering not only the dot-product of the piece values, but material imbalance and even [insufficient material](Material#InsufficientMaterial "Material"). Of course, one has to take care the effort of [hashing](Hash_Table "Hash Table") is not more expensive than the full calculation, assuming [incremental update](Incremental_Updates "Incremental Updates") only for [captures](Captures "Captures") or [promotions](Promotions "Promotions"). Another pragmatical approach with todays computers and memory sizes is to use precomputed [material tables](Material_Tables "Material Tables").




## See also


* [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [Hash Table](Hash_Table "Hash Table")
* [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
* [Material Tables](Material_Tables "Material Tables")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Transposition Table](Transposition_Table "Transposition Table")


## Forum Posts


* [Accessing Material Imbalance Information?](http://www.talkchess.com/forum/viewtopic.php?t=50550) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 19, 2013


## External Links


* [Xiaoji Chen's Design Weblog » HashTable: An Algorithm for Material Reuse](http://xiaoji-chen.com/blog/2010/hashtable-an-algorithm-for-material-reuse/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine") (ed. [Peter W. Frey](Peter_W._Frey "Peter W. Frey")), pp. 82-118. Springer-Verlag, New York, N.Y. 2nd ed. 1983. ISBN 0-387-90815-3. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")

**[Up one level](Material "Material")**







 
