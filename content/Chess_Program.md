---
title: Chess Program
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chess - The Northwestern University Chess Program**

[](http://archive.computerhistory.org/projects/chess/related_materials/physical-object/3-1%20and%203-3.Chess_4.6_electronic_board_ACM_9_NACCC_Washington_1978_10264526.NEWBORN.jpg) Chess 4.6 [Chesstor](#chesstor), [ACM 1978](ACM_1978 "ACM 1978") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Chess**,

the [Northwestern University](Northwestern_University "Northwestern University") Chess Program by primary authors [Larry Atkin](Larry_Atkin "Larry Atkin") and [David Slate](David_Slate "David Slate") was the dominating program in the 70s, winning eight times the [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship") and the [second WCCC Toronto 1977](WCCC_1977 "WCCC 1977"). The version Chess **4.0** from [1973](Timeline#1973 "Timeline") was a complete re-write and [paradigm shift](https://en.wikipedia.org/wiki/Paradigm_shift) from [Shannon type B](Type_B_Strategy "Type B Strategy") to [type A](Type_A_Strategy "Type A Strategy"). Chess ran on [Control Data Corporation's](https://en.wikipedia.org/wiki/Control_Data_Corporation) line of supercomputers, [CDC 6600](CDC_6600 "CDC 6600") and [CDC Cyber](CDC_Cyber "CDC Cyber"), Chess 4.x was completely written in [COMPASS](https://en.wikipedia.org/wiki/COMPASS), the CDC [assembly](Assembly "Assembly") language.

## Photos

[](http://www.computerhistory.org/chess/full_record.php?iid=stl-430b9bbe30c92)
[Ruben](Ira_Ruben "Ira Ruben") and [Slate](David_Slate "David Slate"), [WCCC 1974](WCCC_1974 "WCCC 1974") <a id="cite-note-2" href="#cite-ref-2">[2]</a>

[](http://www.computerhistory.org/chess/full_record.php?iid=stl-431f4cc15f2c0)
[Slate](David_Slate "David Slate") and [Atkin](Larry_Atkin "Larry Atkin"), [ACM 1975](ACM_1975 "ACM 1975") <a id="cite-note-3" href="#cite-ref-3">[3]</a>

## History of Development

## Chess 1.0

In spring [1968](Timeline#1968 "Timeline") [Northwestern University](Northwestern_University "Northwestern University") engineering students [Larry Atkin](Larry_Atkin "Larry Atkin") and [Keith Gorlen](Keith_Gorlen "Keith Gorlen") launched a chess program in their spare time.

## Chess 2.0 - 3.6

By mid 1969, physics graduate student [David Slate](David_Slate "David Slate"), who already started his own effort of a computer chess program, joined the team to develop Chess **2.0**, which was gradually refined to Chess **3.6** during the following years by Slate and Atkin. While Gorlen left the team in 1970, he still contributed a few ideas for some time. The development and architecture of the early program is described in [Larry Atkin's](Larry_Atkin "Larry Atkin") Masters Thesis <a id="cite-note-4" href="#cite-ref-4">[4]</a> .

Chess, until 3.6, was a [Shannon Type B](Type_B_Strategy "Type B Strategy") kind of program, using a plausible move generator to select "best-n" moves. Due to their early success and obligation to prepare for the annual ACM event, the authors more and more stumbled over their initial design decisions and almost unmaintainable source code, and started a complete redesign and re-write in [1973](Timeline#1973 "Timeline").

Further quotes from *CHESS 4.5 - The Northwestern University Chess Program* <a id="cite-note-5" href="#cite-ref-5">[5]</a> :

```C++
We quickly ruled out entering Chess 3.6. If there is anything more useless than yesterday's newspaper, it is last year's chess program. Our interest in the tournament lay in the chance to test something new and different, not to find out whether the other programs had improved enough to smash our old program. We knew, despite our unbeaten record and well-developed myth about the "solidity" of our program, that our luck must soon give out. The bubble would burst, and the gross weakness of Chess 3.6 would suddenly pour out in a series of ridiculous, humiliating blunders. For Chess 3.6 was the latest in a series of evolutionary changes to our original chess program, written in 1968-1969, and it faithfully carried most of the original design deficiencies. Chess 3.6 was, like the dinosaur, a species about to become extinct. Basically a [Shannon](Claude_Shannon "Claude Shannon") type B program, it had a depth-first, alpha-beta, more-or-less fixed depth tree search. A primitive position evaluation function scored the endpoints and also doubled as a plausible move generator earlier in the tree by selecting "best-n" moves for further exploration. Rudimentary as they were, Chess 3.6's evaluation and tree search were just adequate to make "reasonable-looking" moves most of the time and not hang pieces to one- or two move threats. Apparently this was enough to play low class C chess and, for a while, to beat other programs.

```

```C++
In terms of organization, Chess 3.6 was a mess. Not only was it difficult to modify the evaluation function - it was difficult even to find it in the listing of the program.

```

## Chess 4.0 - 4.9

Chess **4.0** and it's successors were more simple and modular written [Tech](Tech "Tech") style [Shannon](Claude_Shannon "Claude Shannon") Type A programs.

```C++
Chess 3.6 was a mixture of [Fortran](Fortran "Fortran") and [Assembly](Assembly "Assembly") language (for CDC 6000/Cyber). Although we would have liked to use a high-level language, we felt that neither Fortran nor other languages available at the time offered the right combination of efficiency and power of expression. In writing Chess 4.0, we used assembly language so we could have complete control over the instructions that were generated. For Evalu8, which contains all of the "chess decisions", we used high-level assembly language macros, which give the "illusion" of a higher level language.

```

```C++
Although our plausible-move generator sounded plausible enough, and differed not very much from methods employed in several other chess programs, we had built up profound dissatisfactions with it over the years. A suggestion by [Peter W. Frey](Peter_W._Frey "Peter W. Frey") triggered some thoughts on the matter, and as a result we dumped selective searching in favor of full-width searching, ostensibly a more primitive algorithm. 

```

Several search and evaluation routines were separated in modules (Evalu8, BASE, FULL, MINI), basic data structures were [Bitboards](Bitboards "Bitboards") and [incremental updated](Incremental_Updates "Incremental Updates") square centric [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") for evaluation and move generation purpose. Chess 4.x used [iterative deepening](Iterative_Deepening "Iterative Deepening"), a sophisticated [Transposition Table](Transposition_Table "Transposition Table"), and the [Killer Heuristic](Killer_Heuristic "Killer Heuristic") (since 4.5). The basic design and detailed description of Chess 4.5 influenced and motivated a lot of other computer chess programmers and made Chess **4.5** an archetype of generations of computer chess programs. [David Slate](David_Slate "David Slate") made the source code of Chess **4.6** available from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

- [Chess 4.0](Evaluation_Overlap#Chess "Evaluation Overlap") from [Evaluation Overlap](Evaluation_Overlap "Evaluation Overlap") by [Mark Watkins](Mark_Watkins "Mark Watkins")
- [Material in Chess 4.5](Material_Hash_Table#ApproachOfChess "Material Hash Table") at [Material Hash Table](Material_Hash_Table "Material Hash Table")
- [Mobility in Chess 4.6](CDC_Cyber#Mobility "CDC Cyber") at [CDC Cyber](CDC_Cyber "CDC Cyber")

## Achievements

Chess **3.x** won the first three [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), [ACM 1970](ACM_1970 "ACM 1970"), [ACM 1971](ACM_1971 "ACM 1971") and [ACM 1972](ACM_1972 "ACM 1972"). Already by August [1973](Timeline#1973 "Timeline"), only a few month after the re-write, and without much testing and tuning, Chess **4.0** won it's first tournament, the [ACM 1973](ACM_1973 "ACM 1973"), but had less luck during the [first World Computer Chess Championship 1974](WCCC_1974 "WCCC 1974"), where it lost against [CHAOS](CHAOS "CHAOS") in round two.

Despite not winning the title in 1974, Chess **4.x** continued domination of CC events. Chess' hardware were the [Control Data Corporation](https://en.wikipedia.org/wiki/Control_Data_Corporation) (CDC) computers [CDC 6600](CDC_6600 "CDC 6600") and [CDC Cyber](CDC_Cyber "CDC Cyber") series, and CDC Cyber hardware consultant [David Cahlander](David_Cahlander "David Cahlander") joined the team. Chess **4.4** won the [ACM 1975](ACM_1975 "ACM 1975"), Chess **4.5** [ACM 1976](ACM_1976 "ACM 1976") and Chess **4.6** [ACM 1977](ACM_1977 "ACM 1977") as well the [second World Computer Chess Championship 1977](WCCC_1977 "WCCC 1977") in Toronto. Chess **4.9** won the 10th [ACM 1979](ACM_1979 "ACM 1979") with a record of now eight (out of ten) North American Championship titles. Chess **4.9** finally participated at the [WCCC 1980](WCCC_1980 "WCCC 1980") in Linz, Austria, already competing with Slate's new program [Nuchess](Nuchess "Nuchess").

## Man-Machine

Chess **4.x** delivered various man-machine matches, most notably the [David Levy](David_Levy "David Levy") versus Chess **4.7** [match in 1978](Levy_versus_Chess_1978 "Levy versus Chess 1978"), where Levy won his famous [bet](David_Levy#TheLevyBet "David Levy"). In 1979, a [Levy versus Chess 4.8 game](Levy_versus_Chess_1978#1979 "Levy versus Chess 1978") was introduced to a greater audience in the German television [ZDF](https://en.wikipedia.org/wiki/ZDF), featured by Journalists [Frederic Friedel](Frederic_Friedel "Frederic Friedel") and [Volker Arzt](http://de.wikipedia.org/wiki/Volker_Arzt) <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

- [Levy versus Chess 1978](Levy_versus_Chess_1978 "Levy versus Chess 1978")
- [Levy versus Chess 4.8 game](Levy_versus_Chess_1978#1979 "Levy versus Chess 1978")

## Chesstor

In 1978, Chess 4.6 was invited to play the [Minnesota's](https://en.wikipedia.org/wiki/Minnesota) [Twin Cities](https://en.wikipedia.org/wiki/Minneapolis%E2%80%93Saint_Paul) Open, won by Chess with a 5-0 score, further winning versus [Walter Browne](https://en.wikipedia.org/wiki/Walter_Browne) in a [simultaneous exhibition](https://en.wikipedia.org/wiki/Simultaneous_exhibition). A new [electronic chessboard](Sensory_Board "Sensory Board") was used for the first time. The micro-processor which controls the board senses the opponent's moves magnetically, transmits the move in algebraic via telephone to the [Cyber 176](CDC_Cyber "CDC Cyber"), and then indicates Cyber 176's responses by illuminating small lights on the square of the piece to be moved and the one to which it is to go. **Chesstor**, as this device was called, also senses the hitting of the chess clock <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## Namesakes

The 1978 program [Chess 0.5](Chess_0.5 "Chess 0.5") by [Larry Atkin](Larry_Atkin "Larry Atkin") and [Peter W. Frey](Peter_W._Frey "Peter W. Frey"), as published in [Byte Magazine](Byte_Magazine "Byte Magazine"), was a separate program written in [Pascal](Pascal "Pascal") for didactic purposes. [Chess 7.0](Chess_7.0 "Chess 7.0") by [Larry Atkin](Larry_Atkin "Larry Atkin") was a commercial program written in [6502](6502 "6502") [Assembly](Assembly "Assembly") published in 1982/83 for various [home computers](https://en.wikipedia.org/wiki/Home_computer). Another namesake was the strong Dutch program [Chess 0.5X](Chess_0.5X "Chess 0.5X") by [Wim Elsenaar](Wim_Elsenaar "Wim Elsenaar") in the 80s, winner of [DOCCC 1983](DOCCC_1983 "DOCCC 1983") and [1984](DOCCC_1984 "DOCCC 1984").

- [Chess 0.5](Chess_0.5 "Chess 0.5")
- [Chess 0.5X](Chess_0.5X "Chess 0.5X")
- [Chess 7.0](Chess_7.0 "Chess 7.0")

## See also

- [Bitboard History](Bitboards#BitboardHistory "Bitboards")
- [History of Computer Chess](History "History")
- [The Mind Machines - WCCC 1977 Video](WCCC_1977#Video "WCCC 1977")
- [WCCC 1986 Video](WCCC_1986#Video "WCCC 1986") at 3:52

## Publications

- [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin"), [Keith Gorlen](Keith_Gorlen "Keith Gorlen") (**1971**). *CHESS 3.5 User Guide*. [Northwestern University](Northwestern_University "Northwestern University")
- [Paul Rushton](Paul_Rushton "Paul Rushton"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1973**). *Current Chess Programs: A Summary of their Potential and Limitations*. INFOR Journal of the Canadian Information Processing Society Vol. 11, No. 1, [pdf](http://webdocs.cs.ualberta.ca/%7Etony/OldPapers/Rushton-Marsland-Feb73.pdf)
- [Larry Atkin](Larry_Atkin "Larry Atkin") (**1975**). *Chess 3.6: A Chess Playing Computer Program.* Masters Thesis, [Northwestern University](Northwestern_University "Northwestern University"), June 1975
- [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *Chess 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (1988) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
- [David Slate](David_Slate "David Slate"), [Ben Mittman](Ben_Mittman "Ben Mittman") (**1978**). *Chess 4.6 - Where Do We Go From Here?* [Jerusalem Conference on Information Technology 1978](http://www.informatik.uni-trier.de/%7Eley/db/conf/jcit/jcit78.html#SlateM78) 193-198
- Editor (**1978**). *Computer beats U.S. chess champ*. [Personal Computing, Vol. 2, No. 10](Personal_Computing#2_10 "Personal Computing"), pp. 84 » [Chesstor](#chesstor)
- [David Cahlander](David_Cahlander "David Cahlander") (**1979**). *Strength of a Chess Playing Computer*. [ICCA Newsletter](ICGA_Journal "ICGA Journal"), Vol. 2, No. 1
- [David J. Slate](David_Slate "David Slate") (**2020**). *CHESS 4.5’s participation in the Paul Masson Chess Classic Tournament of 1976*. [ICGA Journal, Vol. 42, Nos. 2-3](ICGA_Journal#42_23 "ICGA Journal")

## Forum Posts

- [Chess 4.5 from 1976](https://groups.google.com/d/msg/rec.games.chess.computer/8o8r3gVphqc/F3Yw4JuGUOAJ) by Robert Harrington, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 20, 1996
- [Re: CHESS 4.5 (1973)](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/26d01c343961296) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 07, 1997 » [Bitboards](Bitboards "Bitboards"), [C++](Cpp "Cpp"), [Evaluation](Evaluation "Evaluation")
- [Chess 4.0 vs Belle 1973](https://www.stmintz.com/ccc/index.php?id=113123) by Joshua Lee, [CCC](CCC "CCC"), May 31, 2000 » [Belle](Belle "Belle")

## External Links

- [Chess (Northwestern University) from Wikipedia](https://en.wikipedia.org/wiki/Chess_%28Northwestern_University%29)
- [Chess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=41)
- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Description of the computer programme CHESS 4.0](http://ershov.iis.nsk.su/archive/eaimage.asp?lang=2&did=38146&fileid=194303), [August 10, 1974](WCCC_1974 "WCCC 1974"), [IFIP](IFIP "IFIP") 74 Congress, [Andrey Ershov](Mathematician#Ershov "Mathematician") Archive
- [SCHACH: Computer bald Weltmeister?](http://www.spiegel.de/spiegel/print/d-40351942.html) [Der Spiegel](https://en.wikipedia.org/wiki/Der_Spiegel) 13/1979, March 26, 1979 (German) » [Frieder Schwenkel](Frieder_Schwenkel "Frieder Schwenkel")
- [The Slate/Atkin program and CHESS x.x](http://blog.chess.com/billwall/the-slateatkin-program-and-chess-xx) by [Bill Wall](index.php?title=Bill_Wall&action=edit&redlink=1 "Bill Wall (page does not exist)"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), September 23, 2011
- [Ars Electronica - Die Teilnehmer an der 3. Computerschach-Weltmeisterschaft - CHESS 4.9](http://90.146.8.18/de/archives/festival_archive/festival_catalogs/festival_artikel.asp?iProjectID=9497) (German)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess 4.6 electronic board](http://archive.computerhistory.org/projects/chess/related_materials/physical-object/) at [ACM 1978](ACM_1978 "ACM 1978"), Courtesy of [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Ruben and Slate at 1st World Computer Chess Championship in Stockholm](http://www.computerhistory.org/chess/full_record.php?iid=stl-430b9bbe30c92), [WCCC 1974](WCCC_1974 "WCCC 1974"), by [Monroe Newborn](Monroe_Newborn "Monroe Newborn") from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Slate and Atkin at the 6th ACM North American Computer Chess Tournament in Minneapolis, Minnesota](http://www.computerhistory.org/chess/full_record.php?iid=stl-431f4cc15f2c0), [ACM 1975](ACM_1975 "ACM 1975"), by [Monroe Newborn](Monroe_Newborn "Monroe Newborn") from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Larry Atkin](Larry_Atkin "Larry Atkin") (**1975**). *Chess 3.6: A Chess Playing Computer Program.* Masters Thesis, [Northwestern University](Northwestern_University "Northwestern University"), June 1975
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [David Slate](David_Slate "David Slate") and [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (1988) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Chess 4.6 source code](http://www.computerhistory.org/chess/full_record.php?iid=sft-431614f455002), gift of [David Slate](David_Slate "David Slate"), from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/software/3-3.Chess_4.6_Sourcecode.102645430/chess_4-6.sourcecode.102645430.pdf)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [ZDF: IM David Levy 1979 gegen Chess 4.8](http://www.schach-computer.info/wiki/index.php/Levy,_David#ZDF:_IM_David_Levy_1979_gegen_Chess_4.8) from [schach-computer wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> Editor (**1978**). *Computer beats U.S. chess champ*. [Personal Computing, Vol. 2, No. 10](Personal_Computing#2_10 "Personal Computing"), pp. 84
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one level](Engines "Engines")**

