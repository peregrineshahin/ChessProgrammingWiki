---
title: SpaceTime Tradeoff
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* Space-Time Tradeoff**



 [](http://www.physorg.com/news8256.html) Space-time Vortex <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Space-Time Tradeoff** refers to providing [knowledge](Knowledge "Knowledge"), information or [data](Data "Data"), where [memory](Memory "Memory") size competes with computation time. This tradeoff is a frequent issue in computer chess programming, for instance low level stuff to calculate or lookup single populated [bitboards](Bitboards "Bitboards") by square index, or a [distance](Distance "Distance") between two [squares](Squares "Squares"). Lookup tables are [non-volatile](https://en.wikipedia.org/wiki/Non-volatile_memory) tables or initialized once at program startup, various [hash tables](Hash_Table "Hash Table") and caches. Space-time tradeoff is also an issue in determining (almost) perfect knowledge from [interior node recognizers](Interior_Node_Recognizer "Interior Node Recognizer") by [retrograde analysis](Retrograde_Analysis "Retrograde Analysis"), that is the application of [endgame bit-](Endgame_Bitbases "Endgame Bitbases") or [tablebases](Endgame_Tablebases "Endgame Tablebases") and various [compression](https://en.wikipedia.org/wiki/Data_compression) techniques. 



### Contents


* [1 Space-Time Tradeoffs](#space-time-tradeoffs)
* [2 See also](#see-also)
* [3 Publications](#publications)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
* [6 References](#references)






There are multiple CPW pages where memory competes with computation:



* [Bit by Square](General_Setwise_Operations#BitbySquare "General Setwise Operations")
* [BitScan](BitScan "BitScan")
* [Distance](Distance "Distance")
* [Encoding Moves](Encoding_Moves "Encoding Moves")
* [Endgame Bitbases](Endgame_Bitbases "Endgame Bitbases")
* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [Hash Table](Hash_Table "Hash Table")
* [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
* [KPK](KPK "KPK")
* [Legality Test](Square_Attacked_By#LegalityTest "Square Attacked By")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [Manhattan-Distance](Manhattan-Distance "Manhattan-Distance")
* [Material Tables](Material_Tables "Material Tables")
* [Population Count](Population_Count "Population Count")
* [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")
* [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation")
* [The Switch Approach](The_Switch_Approach "The Switch Approach")
* [Transposition Table](Transposition_Table "Transposition Table")


## See also


* [Algorithms](Algorithms "Algorithms")
* [Best-First](Best-First "Best-First")
* [Data](Data "Data")
* [Depth-First](Depth-First "Depth-First")
* [Dispersion and Distortion](Dispersion_and_Distortion "Dispersion and Distortion")
* [Knowledge](Knowledge "Knowledge")
* [Learning](Learning "Learning")
* [Memory](Memory "Memory")
* [Sequential Logic](Sequential_Logic "Sequential Logic")


## Publications


* [Burton H. Bloom](https://en.everybodywiki.com/Burton_Howard_Bloom) (**1970**). *[Space/time trade-offs in hash coding with allowable errors](https://dl.acm.org/doi/10.1145/362686.362692)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 13, No. 7 <a id="cite-note-2" href="#cite-ref-2">[2]</a>
* [Albert Zobrist](Albert_Zobrist "Albert Zobrist"), [Frederic Roy Carlson](Frederic_Roy_Carlson "Frederic Roy Carlson") (**1977**). *Detection of Combined Occurrences*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 20, No. 1


## Forum Posts


* [Stockfish and latest +6 ELO patch!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73273) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), March 05, 2020 » [Distance](Distance "Distance"), [Stockfish](Stockfish "Stockfish") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Removing Large Arrays](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73319) by Deberger, [CCC](CCC "CCC"), March 10, 2020


## External Links


* [Space-time tradeoff from Wikipedia](https://en.wikipedia.org/wiki/Space-time_tradeoff)
* [Blum's speedup theorem from Wikipedia](https://en.wikipedia.org/wiki/Blum%27s_speedup_theorem)
* [Algorithmic efficiency from Wikipedia](https://en.wikipedia.org/wiki/Algorithmic_efficiency)
* [Shannon entropy from Wikipedia](https://en.wikipedia.org/wiki/Entropy_%28Information_theory%29)
* [Computer memory from Wikipedia](https://en.wikipedia.org/wiki/Computer_memory)
* [Cache from Wikipedia](https://en.wikipedia.org/wiki/Cache)
* [Lookup table from Wikipedia](https://en.wikipedia.org/wiki/Lookup_table)
* [Database from Wikipedia](https://en.wikipedia.org/wiki/Database)
* [Memory management unit from Wikipedia](https://en.wikipedia.org/wiki/Memory_management_unit)
* [Volatile memory from Wikipedia](https://en.wikipedia.org/wiki/Volatile_memory)
* [Non-volatile memory from Wikipedia](https://en.wikipedia.org/wiki/Non-volatile_memory)
* [Random-access memory from Wikipedia](https://en.wikipedia.org/wiki/Random-access_memory)
* [Read-only memory from Wikipedia](https://en.wikipedia.org/wiki/Read-only_memory)
* [Memory footprint from Wikipedia](https://en.wikipedia.org/wiki/Memory_footprint)
* [Moore's law from Wikipedia](https://en.wikipedia.org/wiki/Moore%27s_law)
* [Computation, Memory, Nature, and Life](http://www.fourmilab.ch/documents/comp_mem_nat_life/) - Is digital storage the secret of life? by [John Walker](https://en.wikipedia.org/wiki/John_Walker_%28programmer%29)
* [Spacetime from Wikipedia](https://en.wikipedia.org/wiki/Spacetime)
* [Philosophy of space and time from Wikipedia](https://en.wikipedia.org/wiki/Philosophy_of_space_and_time)
* [Einstein Minkowski Space-Time Diagram](http://www.quantonics.com/Einstein_Minkowski_Space_Time_Diagram.html)
* [Art of memory from Wikipedia](https://en.wikipedia.org/wiki/Art_of_memory)
* [Eureka: A Prose Poem from Wikipedia](https://en.wikipedia.org/wiki/Eureka:_A_Prose_Poem)
* [Time in Space](Category:Time_in_Space "Category:Time in Space") - God Bless the Child, [Domicil](https://de.wikipedia.org/wiki/Domicil), [Dortmund](https://en.wikipedia.org/wiki/Dortmund), February 3, 2017, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 In Memoriam [Wolf Escher](https://de.wikipedia.org/wiki/Wolf_Escher)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Space-time Vortex](http://www.physorg.com/news8256.html) from [PhysOrg.com](http://www.physorg.com/)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Bloom filter from Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Use equations for PushAway and PushClose · official-stockfish/Stockfish@5a7b45e · GitHub](https://github.com/official-stockfish/Stockfish/commit/5a7b45eac9dedbf7ebc61d9deb4dd934058d1ca1#diff-4cd6bcdb505b124d7bdc612c4789dc26L57-R59)

**[Up one Level](Programming "Programming")**







 
