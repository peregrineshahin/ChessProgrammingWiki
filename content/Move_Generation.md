---
title: Move Generation
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* Move Generation**



 [](https://commons.wikimedia.org/wiki/File:Zeche_Zollern_Kompressormotor.jpg?uselang=en) Blast Generation <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Generation** of [moves](Moves "Moves") is a basic part of a chess engine with many variations concerning a [generator](https://en.wikipedia.org/wiki/Generator_%28computer_programming%29) or an [iterator](https://en.wikipedia.org/wiki/Iterator_pattern) to loop over moves inside the [search](Search "Search") routine. The implementation heavily depends on the [board representation](Board_Representation "Board Representation"), and it can be generalized into two types, pseudo-legal and legal move generation. 



### Pseudo-legal


In Pseudo-legal move generation [pieces](Pieces "Pieces") obey their normal rules of movement, but they're not checked beforehand to see if they'll leave the [king](King "King") in [check](Check "Check"). It is left up to the [move-making function](Make_Move "Make Move") to test the move, or it is even possible to let the king remain in check and only test for the capture of the king on the next move.




### Legal


In Legal move generation, as the name implies, only [legal moves](Legal_Move "Legal Move") are generated, which means extra time must be spent to make sure the [king](King "King") isn't going to be left or placed [in check](Check "Check") after each move. [Pins](Pin "Pin") are the main difficulty, particularly when [en passant](En_passant "En passant") is involved.



## Special Generators


Most programs use special move generators for the [quiescence search](Quiescence_Search "Quiescence Search"), sometimes supplemented by one for getting out of [check](Check "Check"). These special cases can be made more efficient than generating and testing each possible move to fit specific criteria. For example, if the king is in check, the only possible legal moves are to capture the attacking piece, block the attacker if it is a "ray" piece, or move the king to safety. Special generators for the quiescence search might want to generate checks in addition to [captures](Captures "Captures") and [promotions](Promotions "Promotions"). They can use the fact that a knight or bishop must start off on the [same color square](Color_of_a_Square#SameColor "Color of a Square") as the opponent king if they are to attack it. And rooks can only generate at most 2 checking moves...to the [squares](Intersection_Squares "Intersection Squares") with the rook's column and the king's row or the king's column and the rooks row. 


Similar tricks can be used for generating possible moves out of check, which must be by the king, capturing the opponent's checking piece, or blocking its attack if it is a ray piece. When in [double check](Double_Check "Double Check"), only king moves are permitted.



## Chunk Move Generation


With [move ordering](Move_Ordering "Move Ordering") in mind, chess programs, while traversing pieces and their move-target sets once, store and buffer generated moves inside one or two [move lists](Move_List "Move List") (i.e. for [tactical](Tactical_Moves "Tactical Moves") and [quiet moves](Quiet_Moves "Quiet Moves")), which is convenient for book-keeping and assigning scores based on [MVV-LVA](MVV-LVA "MVV-LVA"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), [history](History_Heuristic "History Heuristic"), [piece square table](Piece-Square_Tables "Piece-Square Tables") etc., to later perform a [selection sort](https://en.wikipedia.org/wiki/Selection_sort) before actually [making the move](Make_Move "Make Move").




## Staged Move Generation


Some programs do not generate all moves at once, but do it in several stages (i.e. [hash move](Hash_Move "Hash Move") first, then [captures](Captures "Captures"), then [killer moves](Killer_Move "Killer Move"), then all the rest in a chunk) on the premise that if one of the early moves causes a cutoff, then we may save on the effort of generating the rest of the moves <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



## Debugging


It is important to ensure that the move generator works properly. Although this could be tested by playing many games, a better approach is to write a [Perft](Perft "Perft") function. This function [recursively](Recursion "Recursion") generates moves for the current position and all children up to a certain depth, and by counting all the leaf nodes, it can be compared to a [table of values](Perft_Results "Perft Results") to test its accuracy.




## Un-Move Generation


**Un-Move Generation** produces a list of all possible moves (including [captures](Captures "Captures") and [promotions](Promotions "Promotions")) which could be [un-made](Unmake_Move "Unmake Move") from a target position to reach all possible legal predecessor or parent positions for [retrograde analysis](Retrograde_Analysis "Retrograde Analysis") tasks. 



## See also


### General


* [Encoding Moves](Encoding_Moves "Encoding Moves")
* [Mate-in-two](Mate-in-two "Mate-in-two")
* [Monochrome Move Generation](Color_Flipping#Monochrome "Color Flipping")
* [Move List](Move_List "Move List")
* [Move Ordering](Move_Ordering "Move Ordering")
* [Perft](Perft "Perft")


### Board Array


* [Mailbox](Mailbox "Mailbox")


 [0x88](0x88 "0x88")
 [Vector Attacks](Vector_Attacks "Vector Attacks")
* [Move Generation with 256 bytes RAM or less?](Sensor_Chess#MoveGeneration "Sensor Chess")
* [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation")


### Bitboards


* [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization")
* [DirGolem](DirGolem "DirGolem")
* [Pieces versus Directions](Pieces_versus_Directions "Pieces versus Directions")
* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks")






### Hardware


* [Belle](Belle#Hardware "Belle")
* [Berkeley Chess Microprocessor](Berkeley_Chess_Microprocessor "Berkeley Chess Microprocessor")
* [Brutus](Brutus#MoveGeneration "Brutus")
* [CHEOPS](CHEOPS "CHEOPS")
* [ChipTest](ChipTest#MoveGeneration "ChipTest")


### Chess Programs


* [Move Generation in Atlas](Atlas#MoveGeneration "Atlas")
* [Move Generation in CPW-Engine](CPW-Engine_movegen(0x88) "CPW-Engine movegen(0x88)")
* [Move Generation in MadChess](MadChess#MoveGeneration "MadChess")
* [Move Generation in Rajah](Rajah#0x88 "Rajah")
* [Move Generation in Thor's Hammer](Thor%27s_Hammer#MoveGeneration "Thor's Hammer")
* [Move Generation in Tinker](Tinker#MoveGeneration "Tinker")
* [Move Generation in TSCP](10x12_Board#OffsetMG "10x12 Board")
* [Move Generation in Vanilla Chess](Vanilla_Chess#MoveGeneration "Vanilla Chess")
* [Table-driven Move Generation in Ferret](Table-driven_Move_Generation#Ferret "Table-driven Move Generation")
* [Table-driven Move Generation in GNU Chess](Table-driven_Move_Generation#GNUChess "Table-driven Move Generation")


## Publications


### 1950 ...


* [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") (**1952**). *Robot Chess*. Research, Vol. 6, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")


### 1970 ...


* [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
* [Gerard Zieliński](Gerard_Zieli%C5%84ski "Gerard Zieliński") (**1976**). *[Arrays for Programming Chess](http://www.emeraldinsight.com/doi/abs/10.1108/eb005412)*. [Kybernetes](http://www.emeraldinsight.com/loi/k), Vol. 5, No. 2
* [Ozalp Babaoglu](Ozalp_Babaoglu "Ozalp Babaoglu") (**1977**). *Hardware implementation of the legal move generation and relative ordering functions for the game of chess*. Master's thesis, [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley")
* [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**1977**). *An Introduction to Computer Chess*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine") pp. 54-81


### 1980 ...


* [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1982**). *Belle Chess Hardware*, [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3"), Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Greg Bakker](index.php?title=Greg_Bakker&action=edit&redlink=1 "Greg Bakker (page does not exist)"), [Jim Jonkman](index.php?title=Jim_Jonkman&action=edit&redlink=1 "Jim Jonkman (page does not exist)"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Tom Schultz](index.php?title=Tom_Schultz&action=edit&redlink=1 "Tom Schultz (page does not exist)") (**1982**). *VLSI Implementation of a Chess Legal Move Generator*. EE755S-1, [University of Waterloo](University_of_Waterloo "University of Waterloo") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Patrick A.D. Powell](index.php?title=Patrick_A.D._Powell&action=edit&redlink=1 "Patrick A.D. Powell (page does not exist)"), [Jim Jonkman](index.php?title=Jim_Jonkman&action=edit&redlink=1 "Jim Jonkman (page does not exist)") (**1983**). *[A VLSI legal move generator for the game of chess](https://link.springer.com/chapter/10.1007/978-3-642-95432-0_19)*. in [Randal E. Bryant](Mathematician#REBryant "Mathematician") (eds.) [Third Caltech Conference on Very Large Scale Integration](https://link.springer.com/book/10.1007%2F978-3-642-95432-0)
* [Carl Ebeling](Carl_Ebeling "Carl Ebeling"), [Andrew James Palay](Andrew_James_Palay "Andrew James Palay") (**1984**). *The Design and Implementation of a VLSI Chess Move Generator*. Proceedings of the 11th Annual International Symposium on Computer Architecture. [IEEE](IEEE "IEEE") and [ACM](ACM "ACM").
* [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft") (**1984**). *Bitmap move generation in Chess*. [ICCA Journal, Vol. 7, No. 3](ICGA_Journal#7_3 "ICGA Journal")
* [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1985**). *Attack Detection and Move Generation on the [X-MP/48](http://www.cisl.ucar.edu/computers/gallery/cray/xmp.jsp).* [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal")
* [Carl Ebeling](Carl_Ebeling "Carl Ebeling") (**1986**). *[All the Right Moves: A VLSI Architecture for Chess](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=7692)*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), MIT Press, Cambridge, MA. ISBN 0-262-05035-8.
* [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1986**). *[Two designs of functional units for VLSI based chess machines](http://repository.cmu.edu/compsci/1566/)*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), Computer Science Department. Paper 1566.
* [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1987**). *A Two-Million Moves/Sec CMOS Single-Chip Chess Move Generator*. IEEE J. of Solid-state Circuits, Vol. 22, No. 5, pp. 841-846.


### 1990 ...


* [James Testa](James_Testa "James Testa"), [Alvin M. Despain](Alvin_M._Despain "Alvin M. Despain") (**1990**). *[A CMOS VLSI chess microprocessor](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&arnumber=124744&contentType=Conference+Publications&searchWithin%3Dp_Authors%3A.QT.Testa%2C+J..QT.)*. [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley"), [IEEE](IEEE "IEEE") Custom Integrated Circuit Conference
* [Chun Ye](Chun_Ye "Chun Ye") (**1992**). *Experiments in Selective Search Extensions*. MSc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1)
* [Yi-Fan Ke](Yi-Fan_Ke "Yi-Fan Ke"), [Tai-Ming Parng](Tai-Ming_Parng "Tai-Ming Parng") (**1996**). *Parallel Move Generation System for Computer Chess*. [IEICE Transactions on Information and Systems](http://search.ieice.org/bin/index.php?category=D&lang=E&curr=1), April, 1996, pp. 290-296
* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1997**). *[How DarkThought Plays Chess](http://people.csail.mit.edu/heinz/dt/node2.html).* [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Rotated Bitmaps, a New Twist on an Old Idea](http://www.cis.uab.edu/hyatt/bitmaps.html)*. [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#24_4 "ICGA Journal")
* [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1999**). *IBM’s Deep Blue Chess Grandmaster Chips*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.126.5392&rep=rep1&type=pdf)


### 2000 ...


* [Reijer Grimbergen](Reijer_Grimbergen "Reijer Grimbergen"), [Hitoshi Matsubara](Hitoshi_Matsubara "Hitoshi Matsubara") (**2001**). *Plausible Move Generation in Two-Player Complete Information Games Using Static Evaluation*. Transactions of the Japanese Society for Artificial Intelligence, Vol.16, pp. 55-62. [pdf](http://www.teu.ac.jp/gamelab/RESEARCH/jsai2001.pdf)
* [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn")), [pdf](http://www.iml.ece.mcgill.ca/%7Emboule/files/mbthesis02.pdf)
* [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [McGill University](McGill_University "McGill University"), [pdf](http://www.iml.ece.mcgill.ca/%7Emboule/files/cicc02.pdf) » [FPGA](FPGA "FPGA")
* [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [ICGA Journal, Vol. 25, No. 2](ICGA_Journal#25_2 "ICGA Journal"), [pdf](http://iml.ece.mcgill.ca/~mboule/files/icga02.pdf)
* [Reijer Grimbergen](Reijer_Grimbergen "Reijer Grimbergen") (**2007**). *Using Bitboards for Move Generation in Shogi*. [ICGA Journal, Vol. 30, No. 1](ICGA_Journal#30_1 "ICGA Journal"), [pdf](http://www2.teu.ac.jp/gamelab/RESEARCH/ICGAJournal2007.pdf), was topic of the [11th Game Programming Workshop](Conferences#GPW "Conferences")
* [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. Thesis, [pdf](http://www.personeel.unimaas.nl/uiterwijk/Theses/PhD/Reul_thesis.pdf)


### 2010 ...


* [Adrien Couetoux](index.php?title=Adrien_Couetoux&action=edit&redlink=1 "Adrien Couetoux (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Hassen Doghmen](index.php?title=Hassen_Doghmen&action=edit&redlink=1 "Hassen Doghmen (page does not exist)") (**2012**). *Learning a Move-Generator for Upper Confidence Trees*. [ICS 2012](http://ics2012.ndhu.edu.tw/), [Hualien](https://en.wikipedia.org/wiki/Hualien_City), [Taiwan](https://en.wikipedia.org/wiki/Taiwan), December 2012 » [Learning](Learning "Learning"), [UCT](UCT "UCT")


## Forum Posts


### 1990 ...


* [move generators in computer chess](http://groups.google.com/group/rec.games.chess/browse_frm/thread/2a726f0678600ca5) by [Deniz Yuret](Deniz_Yuret "Deniz Yuret"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 11, 1994


 [Re: move generators in computer chess, Tricky bit tricks](http://groups.google.com/group/rec.games.chess/msg/f4f0751cc8b928c8) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 20, 1994 » [Traversing Subsets of a Set](Traversing_Subsets_of_a_Set "Traversing Subsets of a Set")
* [bitboard move generation](https://groups.google.com/d/msg/rec.games.chess/vvl1nLv1MD8/oHVKdLXuiaUJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 25, 1994
* [move generators in computer chess](https://groups.google.com/d/msg/rec.games.chess/Kl1MCF9tmpA/7tY-FfFSJDMJ) by [Joël Rivat](Jo%C3%ABl_Rivat "Joël Rivat"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 26, 1994
* [bitboard move generator](https://groups.google.com/d/msg/rec.games.chess/106wKFeI8BA/zNuzu-2aMowJ) by [Joël Rivat](Jo%C3%ABl_Rivat "Joël Rivat"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), November 13, 1994
* [Speed of Move Generator](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/33c57503391f3a89) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 15, 1995
* [Move generator design choices](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/4b0a4302870bf6ac) by [Martin Borriss](Martin_Borriss "Martin Borriss"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 26, 1996
* [Sane numbers](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/3601d68c3678dc7f) by [Martin Borriss](Martin_Borriss "Martin Borriss"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 26, 1996
* [GNU move generation](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7292bfb78152b40b) by [Jan Willem de Kort](index.php?title=Jan_Willem_de_Kort&action=edit&redlink=1 "Jan Willem de Kort (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 18, 1998 » [GNU Chess](GNU_Chess "GNU Chess")


### 2000 ...


* [Fast BB move generation](https://www.stmintz.com/ccc/index.php?id=109588) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), May 08, 2000
* [move\_generation + hash](https://www.stmintz.com/ccc/index.php?id=112809) by [Georg von Zimmermann](Georg_von_Zimmermann "Georg von Zimmermann"), [CCC](CCC "CCC"), May 28, 2000
* [Pre-calculated move generation](https://www.stmintz.com/ccc/index.php?id=116593) by Ujecrh, [CCC](CCC "CCC"), June 26, 2000
* [Move generation question for the big boys](https://www.stmintz.com/ccc/index.php?id=188901) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), September 15, 2001
* [Precomputed move information](https://www.stmintz.com/ccc/index.php?id=238333) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), July 02, 2002
* [Natural move generation with bitboards (was Re:significant math)](https://www.stmintz.com/ccc/index.php?id=266381) by [Alessandro Damiani](Alessandro_Damiani "Alessandro Damiani"), [CCC](CCC "CCC"), November 20, 2002
* [Strength question](https://www.stmintz.com/ccc/index.php?id=275167) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), January 05, 2003
* [Which open source chess program has the fastest move generator?](https://www.stmintz.com/ccc/index.php?id=294549) by [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [CCC](CCC "CCC"), April 25, 2003
* [Improvements in BF makes my MoveGen suck =(](https://www.stmintz.com/ccc/index.php?id=303316) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), June 26, 2003 » [Branching Factor](Branching_Factor "Branching Factor")
* [Speed improvement in split move generation](https://www.stmintz.com/ccc/index.php?id=311601) by [Federico Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](CCC "CCC"), August 16, 2003
* [Move Generation Speed](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=331) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 21, 2004


### 2005 ...


* [Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2006 » [Titboards](Titboards "Titboards")


 [Re: Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623&start=6) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 01, 2006 <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* [Is it time for another new move generator?](http://www.talkchess.com/forum/viewtopic.php?t=17790) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), November 11, 2007
* [Did someone mention the GNUChess move Generator?](http://www.talkchess.com/forum/viewtopic.php?t=17820) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), November 12, 2007 » [GNU Chess](GNU_Chess "GNU Chess")
* [compact bitboard move generator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=19837) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), February 25, 2008 » [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization")
* [Move generator](http://www.talkchess.com/forum/viewtopic.php?t=20630) by [kongsian](Chua_Kong_Sian "Chua Kong Sian"), [CCC](CCC "CCC"), April 12, 2008
* [Bitboards / move generation on larger boards](http://www.talkchess.com/forum/viewtopic.php?t=25917) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), January 09, 2009
* [Move generation: staged vs all-at-once](http://www.talkchess.com/forum/viewtopic.php?t=27657) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 30, 2009


 [Re: Move generation: staged vs all-at-once](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=264380) by [Lance Perkins](Lance_Perkins "Lance Perkins"), [CCC](CCC "CCC"), April 30, 2009
### 2010 ...


* [Assembly move generation in Freccia](http://www.talkchess.com/forum/viewtopic.php?t=39873) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), July 26, 2011


**2012**



* [move generation speed](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52125&sid=d3919159e42267a64891e4e0e3bfbaf0) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2012
* [Is there such a thing as branchless move generation?](http://www.talkchess.com/forum/viewtopic.php?t=43971) by [John Hamlen](John_Hamlen "John Hamlen"), [CCC](CCC "CCC"), June 07, 2012 » [DirGolem](DirGolem "DirGolem"), [GPU](GPU "GPU")
* [hyper threading and move generation](http://www.talkchess.com/forum/viewtopic.php?t=44658) by [Gabor Buella](Gabor_Buella "Gabor Buella"), [CCC](CCC "CCC"), August 01, 2012
* [What's the fastest move generator?](http://www.talkchess.com/forum/viewtopic.php?t=44939) by Marcel Fournier, [CCC](CCC "CCC"), August 29, 2012
* [Re: Question About CPP-C#, Performance, and Square Representation](http://talkchess.com/forum/viewtopic.php?p=485936#485936) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), October 03, 2012 » [MadChess](MadChess "MadChess") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>
* [Plausible move generator](http://www.talkchess.com/forum/viewtopic.php?t=45926) by Jorge Garcia, [CCC](CCC "CCC"), November 09, 2012
* [Diepeveen's move generator](http://www.talkchess.com/forum/viewtopic.php?t=46056) by Hrvoje Horvatic, [CCC](CCC "CCC"), November 18, 2012 » [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation")


**2014**



* [Just another movegen](http://www.talkchess.com/forum/viewtopic.php?t=54337) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), November 14, 2014
* [How to call the Satana move generation](http://www.talkchess.com/forum/viewtopic.php?t=54368) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), November 17, 2014 » [Satana](Satana "Satana")
* [Black/White symmetry in move generation](http://www.talkchess.com/forum/viewtopic.php?t=54465) by Jeffery A Esposito, [CCC](CCC "CCC"), November 25, 2014 » [Color Flipping](Color_Flipping "Color Flipping")
* [Symmetric move generation using bitboards](http://www.talkchess.com/forum/viewtopic.php?t=54704) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), December 20, 2014
* [Reverse move generation](http://www.talkchess.com/forum/viewtopic.php?t=54796) by Kostas Oreopoulos, [CCC](CCC "CCC"), December 30, 2014 » [Un-Move Generation](Move_Generation#Reverse "Move Generation"), [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis")


### 2015 ...


* [On bitboard legal move generation](http://www.talkchess.com/forum/viewtopic.php?t=55275) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), February 09, 2015
* [Questions about chess programming from a newbie](http://www.talkchess.com/forum/viewtopic.php?t=56049) by Matt Palmer, [CCC](CCC "CCC"), April 18, 2015
* [Caching generated moves list in recursive searches](http://www.talkchess.com/forum/viewtopic.php?t=56299) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), May 10, 2015
* [An approach to precomputed move generation bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=58433) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 01, 2015


**2016**



* [speed up your engine part 4](http://www.talkchess.com/forum/viewtopic.php?t=61020) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), August 03, 2016 » [Staged move generation](Move_Generation#Staged "Move Generation")
* [Performance diff between legal / illegal move generator](http://www.talkchess.com/forum/viewtopic.php?t=61797) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 22, 2016


**2017**



* [Most efficient way to generate legal king moves?](http://www.open-chess.org/viewtopic.php?f=5&t=3081) by notachessplayer, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 04, 2017
* [Back to the basics, generating moves on gpu in parallel...](http://www.talkchess.com/forum/viewtopic.php?t=63346) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), March 05, 2017 » [GPU](GPU "GPU")
* [Fastest pawn quiet move generation I was able to come with](http://www.talkchess.com/forum/viewtopic.php?t=64242) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), June 10, 2017 » [Duff's Device](C#Duff "C")
* [History heuristic and quiet move generation](http://www.talkchess.com/forum/viewtopic.php?t=64619) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 16, 2017 » [History Heuristic](History_Heuristic "History Heuristic")
* [Skipping duplicat moves](http://www.talkchess.com/forum/viewtopic.php?t=65900) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 03, 2017


**2019**



* [Opinions requested for new move gen idea](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70082) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 03, 2019 » [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation")
* [My newest almost bb move generator is wonderful](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70508) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), April 17, 2019
* [Efficient capture generation in the game of Thud](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70515) by koedem, [CCC](CCC "CCC"), April 18, 2019


### 2020 ...


* [Comparing 4 move generators: 0x88 vs 10x12 vs 10x12 + bitboards HYBRID vs Pure MAGIC BITBOARDS](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74917) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), August 28, 2020


**2021**



* [Staged move generation?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76835) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), March 10, 2021 » [Staged Move Generation](Move_Generation#Staged "Move Generation")
* [Being silly with perft and legal move generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77350) by [Jakob Progsch](index.php?title=Jakob_Progsch&action=edit&redlink=1 "Jakob Progsch (page does not exist)"), [CCC](CCC "CCC"), May 19, 2021 » [Perft](Perft "Perft"), [Legal Move Generation](#Legal), [En passant](En_passant "En passant")
* [Advice on optimizing my move generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77465) by Christian Dean, [CCC](CCC "CCC"), June 11, 2021
* [Efficiently Generated Legal moves question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77671) by Pedro Duran, [CCC](CCC "CCC"), July 08, 2021 » [Legal Move](Legal_Move "Legal Move")
* [Move generator advice](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77906) by Ellie Moore, [CCC](CCC "CCC"), August 08, 2021
* [Legal or pseudolegal move generator?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=78084) by Pier Carlo, [CCC](CCC "CCC"), September 03, 2021
* [Distinguish rook and bishop move efficiently](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=78164) by [Guido Flohr](index.php?title=Guido_Flohr&action=edit&redlink=1 "Guido Flohr (page does not exist)"), [CCC](CCC "CCC"), September 14, 2021
* [Fast reverse move generation](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78913) by koedem, [CCC](CCC "CCC"), December 18, 2021 » [Un-Move Generation](Move_Generation#Reverse "Move Generation"), [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis")


 [Re: Fast reverse move generation](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78913&start=1) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), December 18, 2021 » [Texel](Texel "Texel")
**2022**



* [Move generation for bitboards](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79365) by [Elias Nilsson](index.php?title=Elias_Nilsson&action=edit&redlink=1 "Elias Nilsson (page does not exist)"), [CCC](CCC "CCC"), February 16, 2022


## External Links


* [Chapter 3: Board Games - 3.1 CHESS](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p003.htm) from [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. Allen & Unwin, ISBN-13: 978-0080212227
* [Description of 0x88 method](http://web.archive.org/web/20070716111804/www.brucemo.com/compchess/programming/0x88.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Move Table move generation](http://web.archive.org/web/20070715002634/www.brucemo.com/compchess/programming/movetable.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [How Zarkov Plays Chess](http://john.stanback.net/zarkov/zarkov_methods.html) by [John Stanback](John_Stanback "John Stanback")
* [Monsoon/Typhoon Homepage](http://perl.guru.org/scott/hobbies/chess/) by [Scott Gasch](Scott_Gasch "Scott Gasch"), covers [0x88](0x88 "0x88") move generation
* [Buzz - A Winboard Chess Playing Program](http://www.pradu.us/old/Nov27_2008/Buzz/) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan") - Source of [magic](Magic_Bitboards "Magic Bitboards") Move Generator
* [Chess Programming Part III: Move Generation](https://www.gamedev.net/tutorials/_/technical/artificial-intelligence/chess-programming-part-iii-move-generation-r1126/) by [François-Dominic Laramée](Fran%C3%A7ois-Dominic_Laram%C3%A9e "François-Dominic Laramée"), [gamedev.net](https://en.wikipedia.org/wiki/GameDev.net), July 2000
* [Chess Move Generator - Computer Architecture and Languages Laboratory](https://labraj.feri.um.si/en/Chess_Move_Generator), [University of Maribor](University_of_Maribor "University of Maribor")
* [Engine - Hispanic Chess Engines | The move generator](https://sites.google.com/site/hispanicchessengines/programs--interface---engines/engine) by [Pedro Castro](Pedro_Castro "Pedro Castro")
* [Generating Legal Chess Moves Efficiently](https://peterellisjones.com/posts/generating-legal-chess-moves-efficiently/) by [Peter Ellis Jones](index.php?title=Peter_Ellis_Jones&action=edit&redlink=1 "Peter Ellis Jones (page does not exist)"), February 09, 2017


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [electric driven air compressor](https://commons.wikimedia.org/wiki/File:Zeche_Zollern_Kompressormotor.jpg?uselang=en) in the [machine hall](https://commons.wikimedia.org/wiki/File:Zeche_Zollern_Dortmund_-_Maschinenhalle.jpg?uselang=en) of [Zollern II/IV Colliery](Category:Zollern "Category:Zollern"), [Dortmund](https://en.wikipedia.org/wiki/Dortmund) [Bövinghausen](https://de.wikipedia.org/wiki/B%C3%B6vinghausen_(Dortmund)), Germany - part of [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail"), Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), September 18, 2016
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Move generation: staged vs all-at-once](http://www.talkchess.com/forum/viewtopic.php?t=27657) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 30, 2009
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [1983 | Waking up to change](https://uwaterloo.ca/water-under-the-bridge/1983) in [Chris Redmond and Simon the Troll](https://uwaterloo.ca/water-under-the-bridge/about-authors) (**1998**). *[Water Under the Bridge](https://uwaterloo.ca/water-under-the-bridge/)*. [University of Waterloo](University_of_Waterloo "University of Waterloo") » [VLSI Move Generation](#Waterloo1982)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: multi-dimensional piece/square tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=52861&start=8) by Tony P., [CCC](CCC "CCC"), January 28, 2020
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [yield - MSDN C# Reference](http://msdn.microsoft.com/en-us/library/9k7k7cf0.aspx)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Behind the scenes of the C# yield keyword | Struggles](http://startbigthinksmall.wordpress.com/2008/06/09/behind-the-scenes-of-the-c-yield-keyword/) by [Lars Corneliussen](http://startbigthinksmall.wordpress.com/), June 9, 2008

**[Up one level](Board_Representation "Board Representation")**







 
