---
title: Bitboards
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * Bitboards**

[](File:BoardsMeeting.jpg) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Boards Meeting [[1]](#cite_note-1)
**Bitboards**,

also called bitsets or bitmaps, or better **Square Sets**, are among other things used to represent the [board](Chessboard "Chessboard") inside a chess program in a **piece centric** manner. Bitboards, are in essence, [finite sets](https://en.wikipedia.org/wiki/Finite_set) of up to [64](https://en.wikipedia.org/wiki/64_%28number%29) [elements](https://en.wikipedia.org/wiki/Element_%28mathematics%29) - all the [squares](Squares "Squares") of a [chessboard](Chessboard "Chessboard"), one [bit](Bit "Bit") per square. Other board [games](Games "Games") with greater board sizes may be use set-wise representations as well [[2]](#cite_note-2), but classical chess has the advantage that one [64-bit word](Quad_Word "Quad Word") or register covers the whole board. Even more bitboard friendly is [Checkers](Checkers "Checkers") with 32-bit bitboards and less [piece-types](Pieces#PieceTypeCoding "Pieces") than chess [[3]](#cite_note-3) [[4]](#cite_note-4).

## The Board of Sets

To [represent the board](Board_Representation "Board Representation") we typically need one bitboard for each [piece-type](Pieces#PieceTypeCoding "Pieces") and [color](Color "Color") - likely encapsulated inside a class or structure, or as an [array](Array "Array") of bitboards as part of a position object. A one-bit inside a bitboard implies the existence of a piece of this piece-type on a certain square - one to one associated by the bit-position.

- [Square Mapping Considerations](Square_Mapping_Considerations "Square Mapping Considerations")
- [Standard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition")

## Bitboard Basics

Of course bitboards are not only about the existence of pieces - it is a general purpose, **set-wise** data-structure fitting in one 64-bit register. For example, a bitboard can represent things like attack- and defend sets, move-target sets and so on.

## General Bitboard Techniques

The fundamental bitboard basics.

- [General Setwise Operations](General_Setwise_Operations "General Setwise Operations")
- [Population Count](Population_Count "Population Count")
- [BitScan](BitScan "BitScan")
- [Flipping Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
- [Fill Algorithms](Fill_Algorithms "Fill Algorithms")

## Pattern and Attacks

This is basically about chess, how to calculate attack-sets and various pattern for [evaluation](Evaluation "Evaluation") and [move generation](Move_Generation "Move Generation") purposes.

- [Pawn Pattern and Properties](Pawn_Pattern_and_Properties "Pawn Pattern and Properties")
- [Knight Pattern](Knight_Pattern "Knight Pattern")
- [King Pattern](King_Pattern "King Pattern")
- [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") including [rotated](Rotated_Bitboards "Rotated Bitboards") and [magic bitboards](Magic_Bitboards "Magic Bitboards")
- [Square Attacked By](Square_Attacked_By "Square Attacked By")
- [X-ray Attacks](</X-ray_Attacks_(Bitboards)> "X-ray Attacks (Bitboards)")
- [Checks and Pinned Pieces](</Checks_and_Pinned_Pieces_(Bitboards)> "Checks and Pinned Pieces (Bitboards)")
- [Design Principles](Design_Principles "Design Principles")

## Move Generation Issues

Bitboard aspects on [move generation](Move_Generation "Move Generation") and [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") (SEE).

- [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization")
- [Pieces versus Directions](Pieces_versus_Directions "Pieces versus Directions")
- [DirGolem](DirGolem "DirGolem")
- [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")
- [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")

## Miscellaneous

- [Backtracking - Eight Queens puzzle with Bitboards](Backtracking#8QinBitboards "Backtracking")
- [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator")
- [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards")
- [Traversing Subsets of a Set](Traversing_Subsets_of_a_Set "Traversing Subsets of a Set")

## Defining Bitboards

*To be aware of their scalar 64-bit origin, we use so far a type defined unsigned integer U64 in our [C](C "C") or [C++](Cpp "Cpp") source snippets, the scalar 64-bit long in [Java](Java "Java"). Feel free to define a distinct type or wrap U64 into classes for better abstraction and type-safety during compile time. The macro C64 will append a suffix to 64-bit constants as required by some compilers*:

```C++
typedef unsigned __int64 U64;    // for the old microsoft compilers 
typedef unsigned long long  U64; // supported by MSC 13.00+ and C99 
##define C64(constantU64) constantU64##ULL

```

## Bitboard-History

The general approach of [bitsets](Mikhail_R._Shura-Bura#Bitsets "Mikhail R. Shura-Bura") was proposed by [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") in 1952 [[5]](#cite_note-5) [[6]](#cite_note-6). The bitboard method for holding a board game appears to have been invented also in 1952 by [Christopher Strachey](Christopher_Strachey "Christopher Strachey") using White, Black and King bitboards in his checkers program for the [Ferranti Mark 1](Ferranti_Mark_1 "Ferranti Mark 1"), and in the mid 1950's by [Arthur Samuel](Arthur_Samuel "Arthur Samuel") in his checkers program as well. In computer chess, bitboards were first described by [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky") et al. in 1967 [[7]](#cite_note-7), reprinted 1970 [[8]](#cite_note-8) . Bitboards were used in [Kaissa](Kaissa "Kaissa") and in [Chess](</Chess_(Program)> "Chess (Program)"). The invention and publication of [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards") by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") [[9]](#cite_note-9) and [Peter Gillgasch](Peter_Gillgasch "Peter Gillgasch") with [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") in the 90s was another milestone in the history of bitboards. [Steffan Westcott's](Steffan_Westcott "Steffan Westcott") innovations, too expensive on 32-bit [x86](X86 "X86") processors, should be revisited with [x86-64](X86-64 "X86-64") and [SIMD instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") in mind. With the advent of fast 64-bit multiplication along with faster [memory](Memory "Memory"), [Magic Bitboards](Magic_Bitboards "Magic Bitboards") as proposed by [Lasse Hansen](Lasse_Hansen "Lasse Hansen") [[10]](#cite_note-10) and refined by [Pradu Kannan](Pradu_Kannan "Pradu Kannan") [[11]](#cite_note-11) have surpassed Rotated.

## Analysis

The use of bitboards has spawned numerous discussions about their costs and benefits. The major points to consider are:

- Bitboards can have a high information density.
- Single populated or even empty Bitboards have a low information density.
- Bitboards are weak in answering questions like what piece if any resides on square x. One reason to keep a redundant [mailbox](Mailbox "Mailbox") board representation with some additional [update](Incremental_Updates "Incremental Updates") costs during [make](Make_Move "Make Move")/[unmake](Unmake_Move "Unmake Move").
- Bitboards can operate on all squares in parallel using bitwise instructions. This is one of the main arguments used by proponents of bitboards, because it allows for a flexibility in [evaluation](Evaluation "Evaluation").
- Bitboards are rather handicapped on 32 bit processors, as each bitwise computation must be split into two or more instructions [[12]](#cite_note-12) . As most modern processors are now 64 bit, this point is somewhat diminished [[13]](#cite_note-13) .
- Bitboards often rely on [bit-twiddling](Bit-Twiddling "Bit-Twiddling") and various optimization tricks and special instructions for certain hardware architectures, such as [bitscan](BitScan "BitScan") and [population count](Population_Count "Population Count"). Optimal code requires machine dependent [header-files](http://en.wikipedia.org/wiki/Header_file) in [C](C "C")/[C++](Cpp "Cpp"). Portable code is likely not optimal for all processors.
- Some operations on bitboards are less general, f.i. shifts. This requires additional code overhead.

## Publications

## 1970 ...

- [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Alexander Bitman](Alexander_Bitman "Alexander Bitman"), [Alexander Zhivotovsky](Alexander_Zhivotovsky "Alexander Zhivotovsky"), [Anatoly Uskov](Anatoly_Uskov "Anatoly Uskov") (**1970**). *[Programming a Computer to Play Chess](http://iopscience.iop.org/0036-0279/25/2/R07)*. [Russian Mathematical Surveys, Vol. 25](http://iopscience.iop.org/0036-0279/25/2), pp. 221-262.
- [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") » [Chess](</Chess_(Program)> "Chess (Program)")

## 1980 ...

- [Zdenek Zdráhal](Zdenek_Zdrahal "Zdenek Zdrahal"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Alen Shapiro](Alen_Shapiro "Alen Shapiro") (**1981**). *[Recognition of Complex Patterns Using Cellular Arrays](http://comjnl.oxfordjournals.org/content/24/3/263.abstract)*. [The Computer Journal, Vol. 24, No. 3](http://comjnl.oxfordjournals.org/content/24/3.toc), pp. 263-270
- [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft") (**1984**). *Bitmap move generation in Chess*. [ICCA Journal, Vol. 7, No. 3](ICGA_Journal#7_3 "ICGA Journal")
- [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1985**). *Attack Detection and Move Generation on the X-MP/48*. [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal")
- [Arch D. Robison](index.php?title=Arch_D._Robison&action=edit&redlink=1 "Arch D. Robison (page does not exist)"), [Brian J. Hafner](index.php?title=Brian_J._Hafner&action=edit&redlink=1 "Brian J. Hafner (page does not exist)"), [Steven Skiena](Steven_Skiena "Steven Skiena") (**1989**). *[Eight Pieces Cannot Cover a Chess Board](http://comjnl.oxfordjournals.org/content/32/6/567.abstract)*. [The Computer Journal](https://en.wikipedia.org/wiki/The_Computer_Journal), Vol. 32, No. 6, [pdf](http://comjnl.oxfordjournals.org/content/32/6/567.full.pdf)

## 1990 ...

- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1997**). *[How DarkThought Plays Chess](http://people.csail.mit.edu/heinz/dt/node2.html)*. [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal") » [DarkThought](DarkThought "DarkThought")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Rotated Bitmaps, a New Twist on an Old Idea](http://www.craftychess.com/hyatt/bitmaps.html)*. [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal") » [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards") [[14]](#cite_note-14)

## 2000 ...

- [David Rasmussen](David_Rasmussen "David Rasmussen") (**2004**). *Parallel Chess Searching and Bitboards*. Master's thesis, [ps](http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/3267/ps/imm3267.ps) » [Parallel Search](Parallel_Search "Parallel Search")
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2005**). *[The Representation of Chess Game](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1491153)*. Proceedings of the 27th International Conference on Information Technology Interfaces
- [Pablo San Segundo](Pablo_San_Segundo "Pablo San Segundo"), [Ramón Galán](Ram%C3%B3n_Gal%C3%A1n "Ramón Galán") (**2005**). *[Bitboards: A New Approach](http://www.actapress.com/Abstract.aspx?paperId=18953)*. [AIA 2005](http://www.informatik.uni-trier.de/~ley/db/conf/aia/aia2005.html#SegundoG05)
- [Pablo San Segundo](Pablo_San_Segundo "Pablo San Segundo"), [Ramón Galán](Ram%C3%B3n_Gal%C3%A1n "Ramón Galán"), [Fernando Matía](Fernando_Mat%C3%ADa "Fernando Matía"), [Diego Rodríguez-Losada](Diego_Rodr%C3%ADguez-Losada "Diego Rodríguez-Losada"), [Agustín Jiménez](Agust%C3%ADn_Jim%C3%A9nez "Agustín Jiménez") (**2006**). *[Efficient Search Using Bitboard Models](http://dl.acm.org/citation.cfm?id=1191130)*. [ICTAI 2006](http://www.informatik.uni-trier.de/~ley/db/conf/ictai/ictai2006.html#SegundoGMRJ06), [pdf](http://www.intelligentcontrol.es/diego/publications/SanSegundo_Ictai06.pdf)
- [Fridel Fainshtein](Fridel_Fainshtein "Fridel Fainshtein") (**2006**). *An Orthodox k-Move Problem-Composer for Chess Directmates*. M.Sc. thesis, [Bar-Ilan University](Bar-Ilan_University "Bar-Ilan University"), [pdf](http://www.problemschach.de/KMOVEComposer.pdf), Appendix D - 64-bit Representation, pp. 105
- [Fridel Fainshtein](Fridel_Fainshtein "Fridel Fainshtein"), [Yaakov HaCohen-Kerner](Yaakov_HaCohen-Kerner "Yaakov HaCohen-Kerner") (**2006**). *A Chess Composer of Two-Move Mate Problems*. [ICGA Journal, Vol. 29, No. 1](ICGA_Journal#29_1 "ICGA Journal"), [pdf](http://homedir.jct.ac.il/~kerner/pdf_docs/ICGA_computer_composer.pdf), Appendix E: 64-bit representation, pp. 22
- [Reijer Grimbergen](Reijer_Grimbergen "Reijer Grimbergen") (**2007**). *Using Bitboards for Move Generation in Shogi*. [ICGA Journal, Vol. 30, No. 1](ICGA_Journal#30_1 "ICGA Journal"), [pdf](http://www2.teu.ac.jp/gamelab/RESEARCH/ICGAJournal2007.pdf) » [Move Generation](Move_Generation "Move Generation"), [Shogi](Shogi "Shogi")
- [James Glenn](James_Glenn "James Glenn"), [David Binkley](http://www.cs.loyola.edu/~binkley/) (**2008**) *An Investigation of Hierarchical Bit Vectors*. [New Topics in Theoretical Computer Science](https://www.novapublishers.com/catalog/product_info.php?products_id=6555), [pdf](http://www.cs.loyola.edu/~binkley/papers/tcsrt08-hbit-vectors.pdf)
- [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang") (**2009**). *The Bitboard Design and Bitwise Computing in Connect Six*. [14th Game Programming Workshop](Conferences#GPW "Conferences") » [Connect6](Connect6 "Connect6")
- [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. Thesis, [pdf](https://pure.uvt.nl/ws/files/1098572/Proefschrift_Fritz_Reul_170609.pdf)

## 2010 ...

- [Stefano Carlini](index.php?title=Stefano_Carlini&action=edit&redlink=1 "Stefano Carlini (page does not exist)") (**2010**). *Arimaa, a New Challenge for Artificial Intelligence*. M.Sc. thesis, [University of Modena and Reggio Emilia](https://en.wikipedia.org/wiki/University_of_Modena_and_Reggio_Emilia), [pdf](http://arimaa.com/arimaa/papers/StefanoCarlini/Arimaa2.pdf) » Chapter 4, Bitboards in [Arimaa](Arimaa "Arimaa")
- [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang"), [Kuo-Yuan Kao](Kuo-Yuan_Kao "Kuo-Yuan Kao"), [Tai-Ning Yang](index.php?title=Tai-Ning_Yang&action=edit&redlink=1 "Tai-Ning Yang (page does not exist)") (**2012**). *[Bitboard Knowledge Base System and Elegant Search Architectures for Connect6](http://www.sciencedirect.com/science/article/pii/S0950705112001293)*. [Knowledge-Based Systems](https://www.journals.elsevier.com/knowledge-based-systems/), Vol. 34 » [Connect6](Connect6 "Connect6")
- [Cameron Browne](Cameron_Browne "Cameron Browne"), [Stephen Tavener](index.php?title=Stephen_Tavener&action=edit&redlink=1 "Stephen Tavener (page does not exist)") (**2013**). *[Life in the Fast Lane](http://www.aifactory.co.uk/newsletter/2012_02_fast_lane.htm)*. [AI Factory](AI_Factory "AI Factory") » [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) within a Bitboard
- [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang"), [Ping-Jung Tseng](https://dblp.uni-trier.de/pers/hd/t/Tseng:Ping=Jung) (**2013**). *[Bitboard Connection Code Design for Connect6](https://ieeexplore.ieee.org/document/6783902)*. [TAAI 2013](index.php?title=TAAI_2013&action=edit&redlink=1 "TAAI 2013 (page does not exist)") » [Connect6](Connect6 "Connect6")
- [Cameron Browne](Cameron_Browne "Cameron Browne") (**2014**). *Bitboard Methods for Games*. [ICGA Journal, Vol. 37, No. 2](ICGA_Journal#37_2 "ICGA Journal")
- [Yen-Chi Chen](Yen-Chi_Chen "Yen-Chi Chen"), [Shun-Shii Lin](Shun-Shii_Lin "Shun-Shii Lin") (**2019**). *A fast nonogram solver that won the TAAI 2017 and ICGA 2018 tournaments*. [ICGA Journal, Vol. 41, No. 1](ICGA_Journal#41_1 "ICGA Journal") » [Nonogram](Nonogram "Nonogram")

## Forum Posts

## 1994

- [bitboard move generation](https://groups.google.com/d/msg/rec.games.chess/vvl1nLv1MD8/oHVKdLXuiaUJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 25, 1994
- [bitboard move generator](https://groups.google.com/d/msg/rec.games.chess/106wKFeI8BA/zNuzu-2aMowJ) by [Joël Rivat](Jo%C3%ABl_Rivat "Joël Rivat"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), November 13, 1994
- [bitboard position evaluations](https://groups.google.com/d/msg/rec.games.chess/M4CKCmqDNkI/TjVJEQY0GC0J) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), November 17, 1994 » [Evaluation](Evaluation "Evaluation")

## 1995 ...

- [Chess programming using bitboards](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/71f7b5ee3764f082) by [Joël Rivat](Jo%C3%ABl_Rivat "Joël Rivat"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 18, 1995
- [Bit Board Bonkers??](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/834fa3c273fafffe/cab7c12ea99e9a35) by Dave, [rec.games.chess.computer](Computer_Chess_Forums "Computer Chess Forums"), July 28, 1997
- [Efficient Bitboard Implementation on 32-bit Architecture](http://www.stmintz.com/ccc/index.php?id=30562) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), October 25, 1998
- [Bitboard question](http://www.stmintz.com/ccc/index.php?id=34506) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), December 02, 1998
- [Bitboards](http://www.stmintz.com/ccc/index.php?id=34852) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), December 05, 1998
- [bitboards in java?](http://www.stmintz.com/ccc/index.php?id=48176) by vitor, [CCC](CCC "CCC"), April 06, 1999 » [Java](Java "Java")
- [BitBoards](http://www.stmintz.com/ccc/index.php?id=53446) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), May 29, 1999
- [Bitboard user's information request](http://www.stmintz.com/ccc/index.php?id=71880) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), October 05, 1999 » [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards") [[15]](#cite_note-15)

## 2000 ...

- [To bitboard or not to bitboard?](http://www.stmintz.com/ccc/index.php?id=313504) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 30, 2003
- [How important are Bitboards?](http://www.stmintz.com/ccc/index.php?id=352040) by [Martin Schreiber](index.php?title=Martin_Schreiber&action=edit&redlink=1 "Martin Schreiber (page does not exist)"), [CCC](CCC "CCC"), February 29, 2004
- [questions for bitboard experts](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=516Two) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 06, 2004 » [In Between](Square_Attacked_By#InBetween "Square Attacked By"), [Piece-Lists](Piece-Lists "Piece-Lists")

## 2005 ...

- [Bitboard question](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4521) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 14, 2006
- [Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2006 » [Titboards](Titboards "Titboards")

[Re: Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623&start=6) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 01, 2006 [[16]](#cite_note-16)

- [Speedup with bitboards on 64-bit CPUs](http://www.talkchess.com/forum/viewtopic.php?t=13426) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), April 27, 2007
- [Speedup by bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6651) by [Onno Garms](Onno_Garms "Onno Garms"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 13, 2007
- [BitBoard representations of the board](http://www.talkchess.com/forum/viewtopic.php?t=17138) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 14, 2007
- [compact bitboard move generator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=19837) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), February 25, 2008 » [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization"), [Move Generation](Move_Generation "Move Generation")
- [Bitboards / move generation on larger boards](http://www.talkchess.com/forum/viewtopic.php?t=25917) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), January 09, 2009
- [Bitboard techniques in Xiangqi](http://www.talkchess.com/forum/viewtopic.php?t=26527) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 12, 2009 » [Chinese Chess](Chinese_Chess "Chinese Chess")
- [Bitboards using 2 DOUBLE's ?](http://www.talkchess.com/forum/viewtopic.php?t=28207) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), June 02, 2009 » [Double](Double "Double")

## 2010 ...

- [Bitboard implementation, how much time?](http://www.talkchess.com/forum/viewtopic.php?t=42108) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 22, 2012
- [64 bits for 64 squares ?](http://macechess.blogspot.de/2013/04/64-bits-for-64-squares.html) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [mACE Chess](http://macechess.blogspot.de/), April 28, 2013 » [Population Count](Population_Count "Population Count")
- [Bitboard Tricks for Large Chess Variants](http://www.talkchess.com/forum/viewtopic.php?t=54208) by [Ed Trice](index.php?title=Ed_Trice&action=edit&redlink=1 "Ed Trice (page does not exist)"), [CCC](CCC "CCC"), November 01, 2014

## 2015 ...

- [Bitboard database code samples](http://www.talkchess.com/forum/viewtopic.php?t=56476) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 25, 2015 » [Symbolic](Symbolic "Symbolic")
- [M42 - A C++ library for Bitboard attack mask generation](http://www.talkchess.com/forum/viewtopic.php?t=60007) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), April 30, 2016
- [Checkers Bitboard representation](http://www.talkchess.com/forum/viewtopic.php?t=64487) by Pranav Deshpande, [CCC](CCC "CCC"), July 02, 2017 » [Checkers](Checkers "Checkers")
- [Bitboards and Java](http://www.talkchess.com/forum/viewtopic.php?t=65724) by [Fred Hamilton](index.php?title=Fred_Hamilton&action=edit&redlink=1 "Fred Hamilton (page does not exist)"), [CCC](CCC "CCC"), November 14, 2017 » [Java](Java "Java")
- [Re: Pawn move generation in bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72461&start=3) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), December 05, 2019 » [C++](Cpp "Cpp"), [Pawn Pattern and Properties](Pawn_Pattern_and_Properties "Pawn Pattern and Properties")

## 2020 ...

- [M42 - C++ Library for Bitboard Attack Mask Generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73830) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), May 04, 2020 [[17]](#cite_note-17)
- [Bitboard board representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76083) by [Elias Nilsson](index.php?title=Elias_Nilsson&action=edit&redlink=1 "Elias Nilsson (page does not exist)"), [CCC](CCC "CCC"), December 17, 2020
- [Thought bitboards was faster :-)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76548) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), February 10, 2021
- [Are Bitboards More Intoxicating Than They Are Good?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76690) by [Mike Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), February 24, 2021
- [Best bitboard design?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77299) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), May 13, 2021
- [The cost of check & discovered check in bitboards](https://www.talkchess.com/forum3/viewtopic.php?t=78160) by Bill Beame, [CCC](CCC "CCC"), September 13, 2021
- [Bitboards ?: C# vs C++](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78680) by Bill Beame, [CCC](CCC "CCC"), November 17, 2021 » [C#](C_sharp "C sharp"), [C++](Cpp "Cpp")
- [Move generation for bitboards](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79365) by [Elias Nilsson](index.php?title=Elias_Nilsson&action=edit&redlink=1 "Elias Nilsson (page does not exist)"), [CCC](CCC "CCC"), February 16, 2022

## Viewer & Calculator

- [Bibob](Bibob "Bibob")
- [Bitboard Calculator](https://gekomad.github.io/Cinnamon/BitboardCalculator) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella")
- [Free Chess Bitboard Viewer - Computer Chess Programming](http://www.chessprogramming.net/computerchess/free-chess-bitboard-viewer/) by [Steve Maughan](Steve_Maughan "Steve Maughan")
- [New free tool : Bitboards Helper](http://www.chess2u.com/t2159-new-free-tool-bitboards-helper) by [Julien Marcel](Julien_Marcel "Julien Marcel")

## External Links

## Descriptions

- [Bitboards from Wikipedia](https://en.wikipedia.org/wiki/Bitboard)
- [Bit-Array from Wikipedia](https://en.wikipedia.org/wiki/Bit_array)
- [Bitboard-History from Wikipedia](https://en.wikipedia.org/wiki/Bitboard#History)
- [Chess board representations](https://craftychess.com/hyatt/boardrep.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
- [Bitboards (aka bitmaps)](https://web.archive.org/web/20081007034904/http://webpages.charter.net/tlikens/bitmaps/bit_intro.html) by [Tom Likens](Tom_Likens "Tom Likens") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), 2008)
- [An Introduction to BITBOARDS](http://www.fzibi.com/cchess/bitboards.htm) by [Franck Zibi](Franck_Zibi "Franck Zibi")
- [Bitwise Optimization in Java: Bitfields, Bitboards, and Beyond](https://web.archive.org/web/20050205014648/http://www.onjava.com/pub/a/onjava/2005/02/02/bitsets.html) by [Glen Pepicelli](Glen_Pepicelli "Glen Pepicelli"), ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), 2005), [O'Reilly's](http://en.wikipedia.org/wiki/O%27Reilly_Media) [OnJava.com](https://web.archive.org/web/20050203015229/http://onjava.com/) » [Java](Java "Java"), [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling")
- [Chess and Bitboards](https://pages.cs.wisc.edu/~psilord/blog/data/chess-pages/index.html) by [Peter Keller](https://pages.cs.wisc.edu/~psilord/)
- [Position Representation - Computer Architecture and Languages Laboratory](https://labraj.feri.um.si/en/Position_Representation), [University of Maribor](University_of_Maribor "University of Maribor")
- [Newest 'bitboard' Questions](https://stackoverflow.com/questions/tagged/bitboard) - [Stack Overflow](http://en.wikipedia.org/wiki/Stack_Overflow)

## Libraries

- [GitHub - sinandredemption/M42: C++ Library for Bitboard Attack Mask Generation](https://github.com/sinandredemption/M42) by [Syed Fahad](Syed_Fahad "Syed Fahad")
- [GitHub - kz04px/libchess: C++ chess library](https://github.com/kz04px/libchess)

## Misc

- [Setunion](https://www.halloherne.de/artikel/1-september-setunion-in-den-flottmann-hallen-38570.htm?k=tick) - [Malletmania](https://inherne.net/weltspitze-des-vibraphon-jazz/), [Flottmann-Hallen](Category:Flottmann "Category:Flottmann") [[18]](#cite_note-18), March 10, 2019, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Kerstin Fabry](http://www.saxophonquartett-quattro-venti.de/#about), [Christian Ribbe](https://www.lokalkompass.de/tag/christian-ribbe), [Elmar Dissinger](https://www.folkwang-uni.de/home/theater/studiengaenge/physical-theatre/lehrende/detail-lehrende/personen-detail/elmar-dissinger/), [Martin Siehoff](https://de.wikipedia.org/wiki/Pee_Wee_Bluesgang), [Carlotta Ribbe](https://www.halloherne.de/artikel/carlotta-ribbe-und-setunion-31511.htm), [Ludger Bollinger](http://guitartist-quartett.com/quartett_ludger.htm)

## References

1. [↑](#cite_ref-1)  [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Boards Meeting, Oil on Canvas, 39 x 32". [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bcf), [Center for Holocaust & Genocide Studies](http://chgs.elevator.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
1. [↑](#cite_ref-2) [Reijer Grimbergen](Reijer_Grimbergen "Reijer Grimbergen") (**2007**). *Using Bitboards for Move Generation in Shogi*. [ICGA Journal, Vol. 30, No. 1](ICGA_Journal#30_1 "ICGA Journal"), [pdf](http://www2.teu.ac.jp/gamelab/RESEARCH/ICGAJournal2007.pdf)
1. [↑](#cite_ref-3) [Checker Bitboards Tutorial](http://www.3dkingdoms.com/checkers/bitboards.htm) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer")
1. [↑](#cite_ref-4) [Checkers Bitboard representation](http://www.talkchess.com/forum/viewtopic.php?t=64487) by Pranav Deshpande, [CCC](CCC "CCC"), July 02, 2017
1. [↑](#cite_ref-5) [Lazar A. Lyusternik](https://en.wikipedia.org/wiki/Lazar_Lyusternik), [Aleksandr A. Abramov](http://www.mathnet.ru/php/person.phtml?personid=30351&option_lang=eng), [Victor I. Shestakov](https://en.wikipedia.org/wiki/Victor_Shestakov), [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") (**1952**). *Programming for High-Speed Electronic Computers*. (Программирование для электронных счетных машин)
1. [↑](#cite_ref-6) [Andrey Ershov](Mathematician#Ershov "Mathematician"), [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") (**1980**). *[The Early Development of Programming in the USSR](http://ershov.iis.nsk.su/archive/eaindex.asp?lang=2&gid=910)*. in [Nicholas C. Metropolis](http://en.wikipedia.org/wiki/Nicholas_C._Metropolis) (ed.) *[A History of Computing in the Twentieth Century](http://dl.acm.org/citation.cfm?id=578384)*. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press), [preprint pp. 43](http://ershov.iis.nsk.su/archive/eaimage.asp?did=28792&fileid=173670)
1. [↑](#cite_ref-7) [Early Reference on Bit-Boards](http://groups.google.com/group/rec.games.chess/browse_frm/thread/0e3a93f45ff07d31#) by [Tony Warnock](Tony_Warnock "Tony Warnock"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), October 29, 1994
1. [↑](#cite_ref-8) [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Alexander Bitman](Alexander_Bitman "Alexander Bitman"), [Alexander Zhivotovsky](Alexander_Zhivotovsky "Alexander Zhivotovsky"), [Anatoly Uskov](Anatoly_Uskov "Anatoly Uskov") (**1970**). *[Programming a Computer to Play Chess](http://iopscience.iop.org/0036-0279/25/2/R07)*. [Russian Mathematical Surveys, Vol. 25](http://iopscience.iop.org/0036-0279/25/2), pp. 221-262.
1. [↑](#cite_ref-9) [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Rotated Bitmaps, a New Twist on an Old Idea](http://www.craftychess.com/hyatt/bitmaps.html)*. [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")
1. [↑](#cite_ref-10) [Fast(er) bitboard move generator](http://www.open-aurec.com/wbforum/viewtopic.php?t=5015) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 14, [2006](Timeline#2006 "Timeline")
1. [↑](#cite_ref-11) [List of magics for bitboard move generation](http://www.open-aurec.com/wbforum/viewtopic.php?t=5441) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 23, [2006](Timeline#2006 "Timeline")
1. [↑](#cite_ref-12) [Efficient Bitboard Implementation on 32-bit Architecture](http://www.stmintz.com/ccc/index.php?id=30562) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), October 25, 1998
1. [↑](#cite_ref-13) [Speedup by bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6651) by [Onno Garms](Onno_Garms "Onno Garms"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 13, 2007
1. [↑](#cite_ref-14) [Bitboard user's information request](http://www.stmintz.com/ccc/index.php?id=71880) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), October 05, 1999
1. [↑](#cite_ref-15) [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Rotated Bitmaps, a New Twist on an Old Idea](http://www.craftychess.com/hyatt/bitmaps.html)*. [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")
1. [↑](#cite_ref-16) [Re: multi-dimensional piece/square tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=52861&start=8) by Tony P., [CCC](CCC "CCC"), January 28, 2020
1. [↑](#cite_ref-17) [GitHub - sinandredemption/M42: C++ Library for Bitboard Attack Mask Generation](https://github.com/sinandredemption/M42)
1. [↑](#cite_ref-18) [Flottmann-Hallen](Category:Flottmann "Category:Flottmann") in [Herne](https://en.wikipedia.org/wiki/Herne,_North_Rhine-Westphalia), [North Rhine-Westphalia](https://en.wikipedia.org/wiki/North_Rhine-Westphalia), [Germany](https://en.wikipedia.org/wiki/Germany), part of [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail") of the [Ruhr area](https://en.wikipedia.org/wiki/Ruhr)

**[Up one level](Board_Representation "Board Representation")**

