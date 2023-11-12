---
title: MicroChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* MicroChess**



 [](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d7c21) llustration from Microchess, 1977 ca. <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**MicroChess**,  

the first commercially successful chess program for [6502](6502 "6502") <a id="cite-note-2" href="#cite-ref-2">[2]</a> and [8080](8080 "8080")/[Z80](Z80 "Z80") <a id="cite-note-3" href="#cite-ref-3">[3]</a> based microcomputers, such as [KIM-1](KIM-1 "KIM-1") and [TRS-80](TRS-80 "TRS-80") <a id="cite-note-4" href="#cite-ref-4">[4]</a> , developed by [Peter Jennings](Peter_Jennings "Peter Jennings") in [1976](Timeline#1976 "Timeline") <a id="cite-note-5" href="#cite-ref-5">[5]</a> . MicroChess 1.5 was base for the programs for the [dedicated](Dedicated_Chess_Computers "Dedicated Chess Computers") [Commodore ChessMate](Commodore_ChessMate "Commodore ChessMate") (1978) and the [Novag](Novag "Novag") [Chess Champion MK II](Chess_Champion_MK_II "Chess Champion MK II") (1979) <a id="cite-note-6" href="#cite-ref-6">[6]</a> . 



### KIM-1


 [](http://www.digibarn.com/collections/games/microchess/index.html) 
MicroChess on the [KIM-1](KIM-1 "KIM-1") <a id="cite-note-7" href="#cite-ref-7">[7]</a>



### TRS-80


 [](http://www.computerhistory.org/chess/full_record.php?iid=stl-431e1a0807480) 
Microchess 1.5 on [TRS-80](TRS-80 "TRS-80") <a id="cite-note-8" href="#cite-ref-8">[8]</a>



## Development


[Peter Jennings](Peter_Jennings "Peter Jennings") in his Oral History about the development of MicroChess on the [KIM-1](KIM-1 "KIM-1") <a id="cite-note-9" href="#cite-ref-9">[9]</a> :




```C++
And if people were using the KIM-1 they weren't going to have it, the majority of people who had a KIM-1 that’s what they had, was just the KIM-1. So I mean I never thought about it in terms of could I put it on some bigger computer, I really at that point was saying “Okay this is what I'm going to do,” and so I treated the problem that way and looked at okay, how do you store the [positions](Board_Representation "Board Representation"), how do you store the [moves](Encoding_Moves "Encoding Moves"), how do you do it with the minimum amount of [memory](Memory "Memory"), how do you store the [tree](Search_Tree "Search Tree") of what you’ve created, and ...

```


```C++
Well I know I didn't store the whole board, because it was simpler to just store the number of [pieces](Piece-Lists#MicroChess "Piece-Lists"), there are fewer pieces than there are [squares](Squares "Squares") on the board, and then what I would do is I would make a move, so I would only store the tree of moves and moves would always be done in a certain order, so you always knew that you could sort of start with this move, then go to that move, then go to that move, go through a sequence of potential types of moves. So the order of how moves would be [generated](Move_Generation "Move Generation") was always the same. So you could then go through one move at a time and I would store the first move and then I would [reverse the board](Color_Flipping#MicroChess "Color Flipping") and then just give it to the computer, give it to the program in the same way that it had looked at the first position, so all I had to store at that point was the position and one move. So the amount of storage was kept pretty small and you were basically giving it back to the computer and saying “Okay, reverse the board,” see what that does until you’ve lost something or you’ve gained something and analyze that against the [algorithm](Minimax "Minimax") and give it a [score](Score "Score").

```


```C++
You start with exactly the same thing, one [point](Point_Value "Point Value") for [pawns](Pawn "Pawn") and two points for [knights](Knight "Knight") , three points for [bishops](Bishop "Bishop"), five for [rooks](Rook "Rook"), that’s exactly where it started. 

```





## Point Values


The [point values](Point_Value "Point Value") for 16 pieces, king (11), queen (10), rooks (6), bishops (4), knights (4), and pawns (2) were defined as preinitialized [array](Array "Array") of 16 bytes, apparently in half pawn units, which overestimates pawns by todays standards <a id="cite-note-10" href="#cite-ref-10">[10]</a> :




```C++

POINTS     db  $0B, $0A, $06, $06, $04, $04, $04, $04
           db  $02, $02, $02, $02, $02, $02, $02, $02

```

## Programming Topics


* [Color Flipping - MicroChess](Color_Flipping#MicroChess "Color Flipping")


 [6502 Assembly](6502#MicroChess "6502")
* [Piece-Lists - MicroChess](Piece-Lists#MicroChess "Piece-Lists")


## Namesake


The [namesake](Category:Namesake "Category:Namesake") **Microchess 3**, released in 1983 by *Norgayer Software* for the [Commodore 64](Commodore_64 "Commodore 64") and [Commodore 128](Commodore_128 "Commodore 128") <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a> , is an alias of the 1981 program [PetChess](PetChess "PetChess"), developed by [Philidor Software](Philidor_Software "Philidor Software") <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a> , which was, according to [Mike Watters](Mike_Watters "Mike Watters"), written by [Mark Taylor](Mark_Taylor "Mark Taylor") <a id="cite-note-16" href="#cite-ref-16">[16]</a> .



## See also


* [6502](6502 "6502")
* [8080](8080 "8080")
* [Arduino](Arduino "Arduino")
* [Chess Champion MK II](Chess_Champion_MK_II "Chess Champion MK II")
* [Commodore ChessMate](Commodore_ChessMate "Commodore ChessMate")
* [KIM-1](KIM-1 "KIM-1")
* [Novag Micro Chess](Novag_Micro_Chess "Novag Micro Chess")
* [TRS-80](TRS-80 "TRS-80")
* [Z80](Z80 "Z80")


## Publications


* [Peter Jennings](Peter_Jennings "Peter Jennings") (**1976**). *[MicroChess, a Chess playing program for the 6502 Microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d8478)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-1.MicroChess_%20Manual_for_6502.Micro-Ware/MicroChessManual.PETER_JENNINGS.062303071.sm.pdf), Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Peter Jennings](Peter_Jennings "Peter Jennings") (**1977**). *[MicroChess, a Chess playing program for the 8080 Microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fe976ea550)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-1.MicroChess_Manual_for_8080/Microchess_for_8080_062302029.sm.pdf), Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Microchess Load Instructions](http://www.computerhistory.org/chess/full_record.php?iid=doc-431e199ab22e1), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/software/4-1.MicroChess_%20Load_%20Instructions.JENNINGS.062303074/4-1.MicroChess_%20Load_%20Instructions.JENNINGS.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Microchess Order Form](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d8cda), 1976 ca, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-1.MicroChess_Order_Form/MicroChess%20Order-2.PETER_JENNINGS.062303033.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Microchess source code](http://www.computerhistory.org/chess/full_record.php?iid=sft-431e19dae0914), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/software/4-1.MicroChess_%20Source.1976.JENNINGS/4-1.MicroChess_%20Source.1976.JENNINGS.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Peter Jennings](Peter_Jennings "Peter Jennings") (**1978**). *Microchess 1.5 Versus Dark Horse*. [BYTE, Vol. 3, No. 3](Byte_Magazine#BYTE303 "Byte Magazine") » [Dark Horse](Dark_Horse "Dark Horse")
* *[What's New? Computer chess; Microchess 1.5; Boris](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d74a1)*, [BYTE, Vol. 3, No. 10](Byte_Magazine#BYTE310 "Byte Magazine"), pp. 193, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-1%20and%204-2.Whats_New_Byte_Magazine/Whats_New.Microchess_1-5.Boris.Byte_Magazine.Oct-1978.062303032.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") » [Boris](Boris "Boris")
* Editor (**1981**). *[Chess And Checkers Programs For Atari Personal Computers](https://www.atarimagazines.com/compute/issue10/084_2_NEW_PRODUCTS_CHESS_AND_CHECKERS_PROGRAMS_FOR_ATARI_PERSONAL_COMPUTERS.php)*. [Compute!](Compute! "Compute!"), Issue 010
* [John F. White](John_F._White "John F. White") (**1981**). *[Survey-Chess Games](http://yourcomputeronline.wordpress.com/2010/12/10/survey-chess-games/)*. [Your Computer](Your_Computer "Your Computer"), [August/September 1981](http://yourcomputeronline.wordpress.com/2010/10/31/augustseptember-1981-contents-and-editorial/)


## External Links


* [Microchess](http://www.benlo.com/microchess/index.html) by [Peter Jennings](Peter_Jennings "Peter Jennings")


 [Microchess for the Kim-1](http://benlo.com/microchess/index.html)
 [Manual](http://benlo.com/microchess/Kim-1Microchess.html)
 [6502 source code](http://benlo.com/files/Microchess6502.txt)
* [Microchess from Wikipedia](https://en.wikipedia.org/wiki/Microchess)
* [DigiBarn Games: MicroChess 1.5 on the TRS-80 Model 1](http://www.digibarn.com/collections/games/microchess/index.html) » [TRS-80](TRS-80 "TRS-80")
* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-17" href="#cite-ref-17">[17]</a>
* [Aart's Commodore 64 Page](http://www.aartbik.com/MISC/c64.html) by [Aart Bik](Aart_Bik "Aart Bik") » [Commodore 64](Commodore_64 "Commodore 64")
* [Secret Weapons of Commodore: Microchess](http://www.floodgap.com/retrobits/ckb/secret/microchess.html) by [Cameron Kaiser](https://twitter.com/doctorlinguist)
* [Computer Schach](http://www.andreadrian.de/schach/index.html) by [Andre Adrian](Andre_Adrian "Andre Adrian") (German)
* [Commodore 64 Emulator - Computer Chess Game Collection - Microchess](http://www.spacious-mind.com/html/c64_emu_-_microchess.html), [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
* [Early Copy Protection on the Apple II](http://www.fadden.com/techmisc/cassette-protect.htm), [Fadden.com](http://www.fadden.com/index.htm) » [Apple II](Apple_II "Apple II"), [Sargon](Sargon "Sargon")
* [6502 Microchess on an Arduino](http://obsolescenceguaranteed.blogspot.ch/2014/06/6502-microchess-on-arduino.html) » [Arduino](Arduino "Arduino")
* [KIM Uno - Summary](http://obsolescence.wix.com/obsolescence#!kim-uno-summary/chcm) - [KIM-1](KIM-1 "KIM-1") replica with MicroChess


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Illustration from Microchess: A Chess Playing Program for the 8080 Microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d7c21), 1977, from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Peter Jennings](Peter_Jennings "Peter Jennings") (**1976**). *[MicroChess, a Chess playing program for the 6502 Microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d8478)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-1.MicroChess_%20Manual_for_6502.Micro-Ware/MicroChessManual.PETER_JENNINGS.062303071.sm.pdf), Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Peter Jennings](Peter_Jennings "Peter Jennings") (**1977**). *[MicroChess, a Chess playing program for the 8080 Microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fe976ea550)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-1.MicroChess_Manual_for_8080/Microchess_for_8080_062302029.sm.pdf), Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Microchess running on Radio Shack TRS-80 microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=stl-431e1a0807480), 1976, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings") and [Digibarn](http://www.digibarn.com/), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Sellam Ismail](http://www.sellam.com/) (**2005**). *Oral History of Peter Jennings*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/oral-history/jennings.oral_history.2005.102630656/jennings.oral_history_transcrit.2005.102630656.pdf) and [Video](http://www.computerhistory.org/chess/related_materials/oral-history/jennings.oral_history.2005.102630656/index.php?iid=orl-4334404555680) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Scisys and Novag : The Early Years](http://www.chesscomputeruk.com/html/scisys_and_novag___the_early_y.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [DigiBarn Games: MicroChess 1.5 on the TRS-80 Model 1](http://www.digibarn.com/collections/games/microchess/index.html)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Microchess running on Radio Shack TRS-80 microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=stl-431e1a0807480), 1976, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings") and [Digibarn](http://www.digibarn.com/), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Sellam Ismail](http://www.sellam.com/) (**2005**). *Oral History of Peter Jennings*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/oral-history/jennings.oral_history.2005.102630656/jennings.oral_history_transcrit.2005.102630656.pdf) and [Video](http://www.computerhistory.org/chess/related_materials/oral-history/jennings.oral_history.2005.102630656/index.php?iid=orl-4334404555680) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), pp. 15, 16
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [6502 source code](http://benlo.com/files/Microchess6502.txt)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Microchess – C64-Wiki](http://www.c64-wiki.de/index.php/Microchess) (German)
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Commodore 64 Emulator - Computer Chess Game Collection - Microchess 3](http://www.spacious-mind.com/html/c64_emu_-_microchess_3.html), [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Game music base - database of Games, Games music and soundtracks | Pet Chess 4000 aka Microchess 3.0](http://www.mirsoft.info/gmb/game_info.php?id_ele=MTQ3MDM=)
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Commodore 64 Emulator - Computer Chess Game Collection - Petchess 4000](http://www.spacious-mind.com/html/c64_emu_-_petchess_4000.html), [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [John F. White](John_F._White "John F. White") (**1982**). *[Review-Chess Computers](http://yourcomputeronline.wordpress.com/2011/01/31/review-chess-computers/)*. [Your Computer](Your_Computer "Your Computer"), [March 1982](http://yourcomputeronline.wordpress.com/2011/01/30/march-1982-contents-and-editorial/)
16. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [Chess Computers - The UK Story](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html) by [Mike Watters](Mike_Watters "Mike Watters")
17. <a id="cite-ref-17" href="#cite-note-17">[17]</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one Level](Engines "Engines")**







 
