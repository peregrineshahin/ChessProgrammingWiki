---
title: Data
---
**[Home](Home "Home") * [Programming](Programming "Programming") * Data**

[](http://historyofeconomics.wordpress.com/2008/10/) [Data mining](https://en.wikipedia.org/wiki/Data_mining) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Data** is anything in a form suitable for use with a [computer](https://en.wikipedia.org/wiki/Computer) to represent [information](https://en.wikipedia.org/wiki/Information) or [knowledge](Knowledge "Knowledge"). [Bits](Bit "Bit"), [bytes](Byte "Byte"), [characters](https://en.wikipedia.org/wiki/Character_%28computing%29), [strings](https://en.wikipedia.org/wiki/String_%28computer_science%29), [numbers](https://en.wikipedia.org/wiki/Number), [codes](https://en.wikipedia.org/wiki/Code), [sets](https://en.wikipedia.org/wiki/Set_%28computer_science%29), [sequences](https://en.wikipedia.org/wiki/Sequence) and [structures](https://en.wikipedia.org/wiki/Structure), as well as [references](https://en.wikipedia.org/wiki/Reference_%28computer_science%29) ([pointers](https://en.wikipedia.org/wiki/Pointer_%28computing%29), [addresses](https://en.wikipedia.org/wiki/Memory_address)) to related data, retrievable stored in [memory](Memory "Memory") of any kind of [hardware](Hardware "Hardware").

A [variable](https://en.wikipedia.org/wiki/Variable_%28programming%29) in the context of [programming languages](Languages "Languages"), associates a symbolic name with a [memory address](https://en.wikipedia.org/wiki/Memory_address).

## Contents

- [1 Processor's View](#processor.27s-view)
- [2 Lifetime of Data](#lifetime-of-data)
  - [2.1 Static Data](#static-data)
  - [2.2 Dynamic Data](#dynamic-data)
  - [2.3 Automatic Data](#automatic-data)
- [3 Algorithms + Data](#algorithms-.2b-data)
- [4 Primitive Types](#primitive-types)
  - [4.1 General Purpose](#general-purpose)
  - [4.2 Chess Specific](#chess-specific)
- [5 Structured Data](#structured-data)
  - [5.1 General Purpose](#general-purpose-2)
  - [5.2 Chess Specific](#chess-specific-2)
  - [5.3 Persistent Data](#persistent-data)
- [6 Endianness](#endianness)
- [7 See also](#see-also)
- [8 Publications](#publications)
  - [8.1 1960 ...](#1960-...)
  - [8.2 1970 ...](#1970-...)
  - [8.3 1980 ...](#1980-...)
  - [8.4 1990 ...](#1990-...)
  - [8.5 2000 ...](#2000-...)
  - [8.6 2010 ...](#2010-...)
- [9 External Links](#external-links)
- [10 References](#references)

## Processor's View

From processor's point of view, an atomic fixed sized data item with a unique memory address is a primitive data item, today usually with a size of one, two, four, or up to eight bytes, sometimes even 16 or 32 bytes. One of these data items may represent numbers in various formats and value ranges, finite sets, codes like a character of a text or a piece on the chessboard, or even instruction codes and memory addresses. It fits into one processor register and is subject of arithmetical or logical operations, or, if interpreted as (part of an) address, to perform random memory access, that is to store and retrieve primitive data items. Program code is decoded and interpreted as instruction to control the [combinatorial](Combinatorial_Logic "Combinatorial Logic") and [sequential logic](Sequential_Logic "Sequential Logic") while executing a program within its processor, usually distinct from application specific data, if the application is not an [assembler](https://en.wikipedia.org/wiki/Assembly_language#Assembler), [compiler](https://en.wikipedia.org/wiki/Compiler) or [debugger](https://en.wikipedia.org/wiki/Debugger) or anything related to [self-modifying code](https://en.wikipedia.org/wiki/Self-modifying_code) or [self-replication](https://en.wikipedia.org/wiki/Self-replication) <a id="cite-note-2" href="#cite-ref-2">[2]</a> .

A collection of primitive data types, located consecutively in memory may be accessed relative to the address of its first element via another data item, an index, or - specially if the primitive data items have different sizes, via constant offsets. From machine perspective, this covers [array](Array "Array") (vector) and structure, while the latter may be interpreted as concrete implementation of abstract objects.

## Lifetime of Data

Data may resist in [persistent](https://en.wikipedia.org/wiki/Persistence_%28computer_science%29) [non-volatile memory](https://en.wikipedia.org/wiki/Non-volatile_memory) or [volatile](https://en.wikipedia.org/wiki/Volatile_memory) [random-access memory](Memory#RAM "Memory"). The [lifetime](https://en.wikipedia.org/wiki/Object_lifetime) of volatile data depends on the data [declaration](https://en.wikipedia.org/wiki/Declaration_%28computer_science%29) of various [programming languages](Languages "Languages"), in [C](C "C") related to storage class specifiers <a id="cite-note-3" href="#cite-ref-3">[3]</a> .

## Static Data

[Global](https://en.wikipedia.org/wiki/Global_variable) or [static data](https://en.wikipedia.org/wiki/Static_variable) as determined and may be initialized at [compile time](https://en.wikipedia.org/wiki/Compile_time) requires [static memory allocation](https://en.wikipedia.org/wiki/Static_memory_allocation). Static data resides in an [object file](https://en.wikipedia.org/wiki/Object_file) or in [segmentated memory](https://en.wikipedia.org/wiki/Segmentation_%28memory%29) in a [data-](https://en.wikipedia.org/wiki/Data_segment) or [bss-segment](https://en.wikipedia.org/wiki/.bss), dependent on their [initialization](https://en.wikipedia.org/wiki/Initialization_%28programming%29). For instance, some chess programs keep [material-](Material_Tables "Material Tables") and other lookup tables initialized in their object file and data segment, for huge tables likely by generated [source code](https://en.wikipedia.org/wiki/Source_code) with appropriate data declarations and static initialization. Assuming the initialization code is (much) shorter than the generated data, others prefer to reduce the size of the object file to initialize stuff located in the bss-segment or elsewhere after program startup.

## Dynamic Data

Dynamic data is created during the [runtime](https://en.wikipedia.org/wiki/Run_time_%28computing%29) of a [process](Process "Process"), it might be [allocated](https://en.wikipedia.org/wiki/Dynamic_memory_allocation) from a [memory pool](https://en.wikipedia.org/wiki/Memory_pool) (heap), and freed if no longer needed, depending on the framework or [programming languages](Languages "Languages"), either explicitly, or implicitly by [garbage collection](https://en.wikipedia.org/wiki/Garbage_collection_%28computer_science%29).

## Automatic Data

Automatic data and variables like [local variables](https://en.wikipedia.org/wiki/Local_variable) and [actual parameters](https://en.wikipedia.org/wiki/Parameter_%28computer_science%29) have a limited lifetime inside the [scope](https://en.wikipedia.org/wiki/Scope_%28programming%29) of a [subroutine](https://en.wikipedia.org/wiki/Subroutine) or [block](https://en.wikipedia.org/wiki/Block_%28programming%29). Automatic variables either reside on the processor [stack](Stack "Stack"), or inside a [processor register](https://en.wikipedia.org/wiki/Processor_register).

## Algorithms + Data

Data structures are inherently related to [algorithms](Algorithms "Algorithms") and their efficiency, as for instance elaborated by [Niklaus Wirth](https://en.wikipedia.org/wiki/Niklaus_Wirth) in *[Algorithms + Data Structures = Programs](https://en.wikipedia.org/wiki/Algorithms_%2B_Data_Structures_%3D_Programs)* <a id="cite-note-4" href="#cite-ref-4">[4]</a> .

## Primitive Types

## General Purpose

- [Bit](Bit "Bit")
- [Nibble](Nibble "Nibble")
- [Byte](Byte "Byte")
- [Word](Word "Word")
- [Double Word](Double_Word "Double Word")
- [Quad Word](Quad_Word "Quad Word")
- [Integer](index.php?title=Integer&action=edit&redlink=1 "Integer (page does not exist)")
- [Float](Float "Float")
- [Double](Double "Double")

## Chess Specific

Scalar integers as numbers, enumerations or simple structures related to [Chess](Chess "Chess") and [Search](Search "Search") basics.

- [Bitboards](Bitboards "Bitboards")
- [Pieces](Pieces "Pieces")
- [Squares](Squares "Squares")
- [Moves](Moves "Moves")

[Encoding Moves](Encoding_Moves "Encoding Moves")

- [Depth](Depth "Depth")

[Ply](Ply "Ply")

- [Score](Score "Score")

## [Centipawns](Centipawns "Centipawns") [Millipawns](Millipawns "Millipawns") Structured Data

## General Purpose

- [Array](Array "Array")
- [De Bruijn Sequence](De_Bruijn_Sequence "De Bruijn Sequence")
- [Hash Table](Hash_Table "Hash Table")
- [Linked List](Linked_List "Linked List")
- [Priority Queue](index.php?title=Priority_Queue&action=edit&redlink=1 "Priority Queue (page does not exist)")
- [Queue](Queue "Queue") (FIFO)
- [Stack](Stack "Stack") (LIFO)

## Chess Specific

- [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")
- [Butterfly Boards](Butterfly_Boards "Butterfly Boards")
- [Move List](Move_List "Move List")
- [Piece-Lists](Piece-Lists "Piece-Lists")
- [Search Tree](Search_Tree "Search Tree")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table")

## Persistent Data

- [Chess Databases](Databases "Databases")
- [Endgame Bitbases](Endgame_Bitbases "Endgame Bitbases")
- [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [Extended Position Description](Extended_Position_Description "Extended Position Description") (EPD)
- [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") (FEN)
- [Opening Book](Opening_Book "Opening Book")
- [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
- [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") (PGN)

## [Endianness](Endianness "Endianness")

- [Little-endian](Little-endian "Little-endian")
- [Big-endian](Big-endian "Big-endian")

## See also

- [Algorithms](Algorithms "Algorithms")
- [Knowledge](Knowledge "Knowledge")
- [Memory](Memory "Memory")
- [Recursion](Recursion "Recursion")
- [Space-Time Tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff")

## Publications

## 1960 ...

- [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Evgenii Landis](Mathematician#Landis "Mathematician") (**1962**). *An algorithm for the organization of information*. [Proceedings of the USSR Academy of Sciences](https://en.wikipedia.org/wiki/Proceedings_of_the_USSR_Academy_of_Sciences), 146: 263–266. (Russian) English translation by Myron J. Ricci in [Soviet Mathematics Doklady](https://en.wikipedia.org/wiki/Proceedings_of_the_USSR_Academy_of_Sciences#Soviet_Mathematics_-_Doklady), No. 3 <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## 1970 ...

- [Burton H. Bloom](https://en.wikipedia.org/wiki/Bloom_filter) (**1970**). *[Space/time trade-offs in hash coding with allowable errors](http://portal.acm.org/citation.cfm?id=362692)*. Comm. of the ACM, Vol. 13, No. 7, [pdf](http://www.lsi.upc.edu/%7Ediaz/p422-bloom.pdf) <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Niklaus Wirth](https://en.wikipedia.org/wiki/Niklaus_Wirth) (**1976**). *[Algorithms + Data Structures = Programs](https://en.wikipedia.org/wiki/Algorithms_%2B_Data_Structures_%3D_Programs)*

## 1980 ...

- [Guy Jacobson](index.php?title=Guy_Jacobson&action=edit&redlink=1 "Guy Jacobson (page does not exist)") (**1989**). *[Succint Static Data Structures](http://dl.acm.org/citation.cfm?id=915547)*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), CMU-CS-89-112, [pdf](http://www.research.att.com/export/sites/att_labs/people/Jacobson_Guy_J/library/publications/JacobsonThesis.pdf)
- [Guy Jacobson](index.php?title=Guy_Jacobson&action=edit&redlink=1 "Guy Jacobson (page does not exist)") (**1989**). *Space-efficient Static Trees and Graphs*. [SFCS'89](http://dl.acm.org/citation.cfm?id=1398514&picked=prox), [pdf](https://www.computer.org/csdl/proceedings/focs/1989/1982/00/063533.pdf)

## 1990 ...

- [Keith E. Gorlen](Keith_Gorlen "Keith Gorlen"), [Sanford M. Orlow](http://um2017.org/faculty-history/faculty/sanford-m-orlow), [Perry S. Plexico](http://arnetminer.org/viewperson.do?naid=614566&name=Perry%20Plexico) (**1990**). *[Data abstraction and object-oriented programming in C++](http://www.goodreads.com/book/show/3108432-data-abstraction-and-object-oriented-programming-in-c)*. [Wiley](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons) <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a> » [C++](Cpp "Cpp")
- [Bernhard Balkenhol](Bernhard_Balkenhol "Bernhard Balkenhol") (**1994**). *Data Compression in Encoding Chess Positions.* [ICCA Journal, Vol. 17, No. 3](ICGA_Journal#17_3 "ICGA Journal"), [zipped ps](http://www.balkenhol.net/papers/icca94.ps.gz) » [Chess Position](Chess_Position "Chess Position")
- [Robert Levinson](Robert_Levinson "Robert Levinson") (**1994**). *[UDS: A Universal Data Structure](http://www.researchgate.net/publication/2821395_UDS_A_Universal_Data_Structure)*. UCSC CRL-94-15
- [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal") (**1996**). *[Algorithms and Data Structures in C++](http://home.planet.nl/%7Eammeraal/algds.html)*. ISBN 0-471-96355-0, Chichester: [John Wiley](http://eu.wiley.com/WileyCDA/Section/id-300022.html)
- [Liwu Li](Liwu_Li "Liwu Li") (**1998**). *[Java - Data Structures and Programming](https://link.springer.com/book/10.1007%2F978-3-642-95851-9)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

## 2000 ...

- [Julio César Hernández-Castro](Julio_C%C3%A9sar_Hern%C3%A1ndez-Castro "Julio César Hernández-Castro"), [Ignacio Blasco-López](index.php?title=Ignacio_Blasco-L%C3%B3pez&action=edit&redlink=1 "Ignacio Blasco-López (page does not exist)"), [L.Javier Garcéa-Villalba](index.php?title=L.Javier_Garc%C3%A9a-Villalba&action=edit&redlink=1 "L.Javier Garcéa-Villalba (page does not exist)") (**2004**). *Hiding Data in Games*. [ICGA Journal, Vol. 27, No. 2](ICGA_Journal#27_2 "ICGA Journal")
- [Dominique Duval](https://genealogy.math.ndsu.nodak.edu/id.php?id=56337), [Rachid Echahed](https://dblp.uni-trier.de/pers/hd/e/Echahed:Rachid), [Frédéric Prost](Fr%C3%A9d%C3%A9ric_Prost "Frédéric Prost") (**2005**). *Data-Structure Rewriting*. [arXiv:cs/0503065](https://arxiv.org/abs/cs/0503065)
- [Julio César Hernández-Castro](Julio_C%C3%A9sar_Hern%C3%A1ndez-Castro "Julio César Hernández-Castro"), [Ignacio Blasco-López](index.php?title=Ignacio_Blasco-L%C3%B3pez&action=edit&redlink=1 "Ignacio Blasco-López (page does not exist)"), [Juan M. Estevez-Tapiador](index.php?title=Juan_M._Estevez-Tapiador&action=edit&redlink=1 "Juan M. Estevez-Tapiador (page does not exist)"), [Arturo Ribagorda-Garnacho](index.php?title=Arturo_Ribagorda-Garnacho&action=edit&redlink=1 "Arturo Ribagorda-Garnacho (page does not exist)") (**2006**). *Steganography in games: A general methodology and its application to the game of Go*. [Computers & Security](http://www.journals.elsevier.com/computers-and-security/), Vol. 25, [pdf](http://www.azlaha.com/stegogo.pdf) <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Erik D. Demaine](Erik_D._Demaine "Erik D. Demaine"), [Dion Harmon](Mathematician#DHarmon "Mathematician"), [John Iacono](Mathematician#JIacono "Mathematician"), [Mihai Pătrașcu](Mathematician#MPatrascu "Mathematician") (**2007**). *[Dynamic Optimality—Almost](http://erikdemaine.org/papers/Tango_SICOMP/)*. [SIAM Journal on Computing](https://en.wikipedia.org/wiki/SIAM_Journal_on_Computing), Vol. 37, No. 1 <a id="cite-note-10" href="#cite-ref-10">[10]</a>
- [Carl Burch](http://ozark.hendrix.edu/%7Eburch/), *[Data & Procedure](http://www.toves.org/books/data/index.html)*. On-line Book
- [Kurt Mehlhorn](Mathematician#KMehlhorn "Mathematician"), [Peter Sanders](Peter_Sanders "Peter Sanders") (**2008**). *[Data Structures and Algorithms: The Basic Toolbox](http://www.mpi-inf.mpg.de/~mehlhorn/Toolbox.html)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), ISBN 978-3540779773
- [Denis Xavier Charles](Mathematician#DXCharles "Mathematician"), [Kumar Chellapilla](index.php?title=Kumar_Chellapilla&action=edit&redlink=1 "Kumar Chellapilla (page does not exist)") (**2008**). *[Bloomier Filters: A Second Look](http://arxiv.org/abs/0807.0928)*. [ESA 2008](http://www.informatik.uni-trier.de/%7Eley/db/conf/esa/esa2008.html#CharlesC08) <a id="cite-note-11" href="#cite-ref-11">[11]</a>
- [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie"), [Frank Stratton](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/s/Stratton:Frank.html), [Hui Xue](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/x/Xue:Hui.html), [Samuel T. King](http://spqr.cs.umass.edu/events/2011-king-sam/) (**2008**). *Digging for Data Structures*. [OSDI 2008](http://www.informatik.uni-trier.de/~ley/db/conf/osdi/osdi2008.html#CozzieSXK08), [pdf](http://www.usenix.org/event/osdi08/tech/full_papers/cozzie/cozzie.pdf)
- [Bernhard Haeupler](Mathematician#BHaeupler "Mathematician"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Robert Tarjan](Mathematician#RETarjan "Mathematician") (**2009**). *Heaps Simplified*. [arXiv:0903.0116](https://arxiv.org/abs/0903.0116)
- [Bernhard Haeupler](Mathematician#BHaeupler "Mathematician"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Robert Tarjan](Mathematician#RETarjan "Mathematician") (**2009**). *[Rank-Balanced Trees](https://link.springer.com/chapter/10.1007/978-3-642-03367-4_31)*. [WADS 2009](https://dblp.org/db/conf/wads/wads2009.html#HaeuplerST09)
- [Bernhard Haeupler](Mathematician#BHaeupler "Mathematician"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Robert Tarjan](Mathematician#RETarjan "Mathematician") (**2009**). *[Rank-Pairing Heaps](https://link.springer.com/chapter/10.1007/978-3-642-04128-0_59)*. [ESA 2009](https://dblp.org/db/conf/esa/esa2009.html#HaeuplerST09)
- [Felix Putze](http://csl.ira.uka.de/~felix/), [Peter Sanders](Peter_Sanders "Peter Sanders"), [Johannes Singler](http://algo2.iti.kit.edu/english/singler.php) (**2009**). *Cache-, hash-, and space-efficient bloom filters*. [ACM Journal of Experimental Algorithmics](ACM#JEA "ACM") Vol. 14
- [Mark A. Hall](https://dblp.uni-trier.de/pers/hd/h/Hall:Mark_A=), [Eibe Frank](https://dblp.uni-trier.de/pers/hd/f/Frank:Eibe), [Geoffrey Holmes](index.php?title=Geoffrey_Holmes&action=edit&redlink=1 "Geoffrey Holmes (page does not exist)"), [Bernhard Pfahringer](Bernhard_Pfahringer "Bernhard Pfahringer"), [Peter Reutemann](https://dblp.uni-trier.de/pers/hd/r/Reutemann:Peter), [Ian H. Witten](Ian_H._Witten "Ian H. Witten") (**2009**). *The WEKA data mining software: an update*. [SIGKDD Explorations](https://dblp.uni-trier.de/db/journals/sigkdd/sigkdd11.html), Vol. 11, No. 1, [pdf](https://www.kdd.org/exploration_files/p2V11n1.pdf) <a id="cite-note-12" href="#cite-ref-12">[12]</a>

## 2010 ...

- [Eibe Frank](https://dblp.uni-trier.de/pers/hd/f/Frank:Eibe), [Mark A. Hall](https://dblp.uni-trier.de/pers/hd/h/Hall:Mark_A=), [Geoffrey Holmes](index.php?title=Geoffrey_Holmes&action=edit&redlink=1 "Geoffrey Holmes (page does not exist)"), [Richard Kirkby](https://dblp.uni-trier.de/pers/hd/k/Kirkby:Richard), [Bernhard Pfahringer](Bernhard_Pfahringer "Bernhard Pfahringer"), [Ian H. Witten](Ian_H._Witten "Ian H. Witten"), [Len Trigg](https://dblp.uni-trier.de/pers/hd/t/Trigg:Leonard_E=) (**2010**). *[Weka-A Machine Learning Workbench for Data Mining](https://link.springer.com/chapter/10.1007/978-0-387-09823-4_66)*. [Data Mining and Knowledge Discovery Handbook](https://link.springer.com/book/10.1007/978-0-387-09823-4), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Erik D. Demaine](Erik_D._Demaine "Erik D. Demaine"), [John Iacono](Mathematician#JIacono "Mathematician"), [Stefan Langerman](index.php?title=Stefan_Langerman&action=edit&redlink=1 "Stefan Langerman (page does not exist)"), [Özgür Özkan](Mathematician#OOzkan "Mathematician") (**2013**). *Combining Binary Search Trees*. [arXiv:1304.7604](https://arxiv.org/abs/1304.7604)
- [Bernhard Haeupler](Mathematician#BHaeupler "Mathematician"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Robert Tarjan](Mathematician#RETarjan "Mathematician") (**2015**). *[Rank-Balanced Trees](https://dl.acm.org/doi/10.1145/2689412)*. [ACM Transactions on Algorithms](ACM#TALG "ACM"), Vol. 11, No. 4
- [Ian H. Witten](Ian_H._Witten "Ian H. Witten"), [Eibe Frank](https://dblp.uni-trier.de/pers/hd/f/Frank:Eibe), [Mark A. Hall](https://dblp.uni-trier.de/pers/hd/h/Hall:Mark_A=), [Christopher Pal](http://www.professeurs.polymtl.ca/christopher.pal/) (**2016**). *[Data Mining: Practical Machine Learning Tools and Techniques](https://www.cs.waikato.ac.nz/~ml/weka/book.html)*. 4th Edition, [Morgan Kaufmann](https://en.wikipedia.org/wiki/Morgan_Kaufmann_Publishers)
- [David Eppstein](David_Eppstein "David Eppstein") (**2016**). *Cuckoo Filter: Simplification and Analysis*. [arXiv:1604.06067](https://arxiv.org/abs/1604.06067) <a id="cite-note-13" href="#cite-ref-13">[13]</a>
- [Erik D. Demaine](Erik_D._Demaine "Erik D. Demaine"), [John Iacono](Mathematician#JIacono "Mathematician"), [Grigorios Koumoutsos](https://dblp.uni-trier.de/pers/hd/k/Koumoutsos:Grigorios), [Stefan Langerman](index.php?title=Stefan_Langerman&action=edit&redlink=1 "Stefan Langerman (page does not exist)") (**2019**). *Belga B-trees*. [arXiv:1903.03560](http://export.arxiv.org/abs/1903.03560)

## External Links

- [Data (computing) from Wikipedia](https://en.wikipedia.org/wiki/Data_%28computing%29)
- [Data (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Data_%28disambiguation%29)
- [Information from Wikipedia](https://en.wikipedia.org/wiki/Information)
- [Lookup table from Wikipedia](https://en.wikipedia.org/wiki/Lookup_table)
- [Cache from Wikipedia](https://en.wikipedia.org/wiki/Cache)
- [Data type from Wikipedia](https://en.wikipedia.org/wiki/Data_type)
- [Initialization from Wikipedia](https://en.wikipedia.org/wiki/Initialization_%28programming%29)
- [Data compression from Wikipedia](https://en.wikipedia.org/wiki/Data_compression)
- [Data segment from Wikipedia](https://en.wikipedia.org/wiki/Data_segment)
- [Addressing mode from Wikipedia](https://en.wikipedia.org/wiki/Addressing_mode)
- [Data structure from Wikipedia](https://en.wikipedia.org/wiki/Data_structure)
- [Succinct data structure from Wikipedia](https://en.wikipedia.org/wiki/Succinct_data_structure)
- [List of data structures from Wikipedia](https://en.wikipedia.org/wiki/List_of_data_structures)
- [Dictionary of Algorithms and Data Structures](http://xlinux.nist.gov/dads/) by [Paul E. Black](http://hissa.nist.gov/~black/), [National Institute of Standards and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)
- [Dictionary of Algorithms and Data Structures from Wikipedia](https://en.wikipedia.org/wiki/Dictionary_of_Algorithms_and_Data_Structures)
- [Data Structures and Programming Lecture 1](http://www.cs.sunysb.edu/%7Eskiena/214/lectures/lect1/lect1.html) by [Steven S. Skiena](Steven_Skiena "Steven Skiena")
- [Serialization from Wikipedia](https://en.wikipedia.org/wiki/Serialization)
- [Marshalling (computer science) from Wikipedia](https://en.wikipedia.org/wiki/Marshalling_%28computer_science%29)
- [Data mining from Wikipedia](https://en.wikipedia.org/wiki/Data_mining)
- [Star Trek](https://en.wikipedia.org/wiki/Star_Trek) [TNG](http://memory-alpha.wikia.com/wiki/Category:TNG_episodes): [S5E14 Conundrum](<http://memory-alpha.wikia.com/wiki/Conundrum_(episode)>), [Deanna Troi](https://en.wikipedia.org/wiki/Deanna_Troi) beats [Data](https://en.wikipedia.org/wiki/Data_%28Star_Trek%29) in [Tri-D Chess](https://en.wikipedia.org/wiki/Three-dimensional_chess#Star_Trek_Tri-Dimensional_Chess), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [History of Economics Playground - October « 2008](http://historyofeconomics.wordpress.com/2008/10/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Reflections on Trusting Trust](http://cm.bell-labs.com/who/ken/trust.html) [ACM](ACM "ACM") Classic by [Ken Thompson](Ken_Thompson "Ken Thompson")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Storage-Class Specifiers](http://msdn.microsoft.com/en-us/library/ash6ess9.aspx) from [MSDN Library](http://msdn.microsoft.com/en-us/library/ms123401.aspx)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Niklaus Wirth](https://en.wikipedia.org/wiki/Niklaus_Wirth) (**1976**). *[Algorithms + Data Structures = Programs](https://en.wikipedia.org/wiki/Algorithms_%2B_Data_Structures_%3D_Programs)*
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [AVL tree from Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Bloom filter from Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [NIH Class Library — Software Preservation Group](http://www.softwarepreservation.org/projects/c_plus_plus/library/nihcl), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [NIH Class Library Revision 3.0 - Release Notes](http://www.softwarepreservation.org/projects/c_plus_plus/library/nihcl/3.0-readme.pdf) (pdf)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [steganography from Wikipedia](https://en.wikipedia.org/wiki/Steganography)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Tango tree from Wikipedia](https://en.wikipedia.org/wiki/Tango_tree)
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Bloom filter - Bloomier filters from Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter#Bloomier_filters)
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Weka (machine learning) from Wikipedia](<https://en.wikipedia.org/wiki/Weka_(machine_learning)>)
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Cuckoo filter from Wikipedia](https://en.wikipedia.org/wiki/Cuckoo_filter)

**[Up one Level](Programming "Programming")**

