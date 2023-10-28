---
title: Material Hash Table
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* [Material](Material "Material") \* Material Hash Table**


A **Material Hash Table** is used to cache once calculated material values for certain material constellations, considering not only the dot-product of the piece values, but material imbalance and even [insufficient material](Material#InsufficientMaterial "Material"). Of course, one has to take care the effort of [hashing](Hash_Table "Hash Table") is not more expensive than the full calculation, assuming [incremental update](Incremental_Updates "Incremental Updates") only for [captures](Captures "Captures") or [promotions](Promotions "Promotions"). Another pragmatical approach with todays computers and memory sizes is to use precomputed [material tables](Material_Tables "Material Tables").




### Contents


* [1 Chess 4.5](#chess-4.5)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
* [5 References](#references)






The Material Hash Table was first described by [David Slate](David_Slate "David Slate") and [Larry Atkin](Larry_Atkin "Larry Atkin") as used in [Chess 4.5](Chess_(Program) "Chess (Program)") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. Chess had following fairly complicated function of only the number of each type of piece on the board, to modify the material difference by a "trade down" bonus that encourages the winning side to trade pieces but no pawns:



 [](File:ChessMaterial1.jpg) 
and



 [](File:ChessMaterial2.jpg) 
with MD as material difference computed by adding the [standard values](Point_Value "Point Value") {100, 325, 350, 500, 900} of each piece and subtracting the total of the side with the least material from the side with the most, the winning side. PA is the number of pawns of the winning side, MT is the total material on the board. 


The hash function must have three desired characteristics. First, it should be obviously faster than the function it is replacing. Second, it should distribute the positions that are likely occur in a single search, and third, it should be symmetric with respect to Black and White. [Chess 4.5](Chess_(Program) "Chess (Program)") had a material signature word, containing five [nibble counters](Nibble "Nibble") per piece type for each side, interpreted as 20-bit number each and also stored inside the hash entry to verify material signature when probing. The hash function used is the sum of the white side and black side, exclusive ored with the absolute value of their difference, folded over by further exclusive or to get a 7-bit number, the hash.



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







 
