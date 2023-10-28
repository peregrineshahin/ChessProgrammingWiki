---
title: RDChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* RDChess**



 [](https://web.archive.org/web/20050309185315/http://www.rdchess.com/) RDChess [GUI](GUI "GUI") <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> 
**RDChess**,  

a [freeware](https://en.wikipedia.org/wiki/Freeware) [open source chess program](Category:Open_Source "Category:Open Source") by [Rudolf Posch](Rudolf_Posch "Rudolf Posch"), written in [Object Pascal](Pascal "Pascal") with [x86](X86 "X86")/[MMX](MMX "MMX") [inline assembly](Assembly#InlineAssembly "Assembly"). 
RDChess comes with an own [Windows](Windows "Windows") [GUI](GUI "GUI"), written in [Delphi](Delphi "Delphi"), and also has a [WinBoard](WinBoard "WinBoard") mode. 



### Contents


* [1 Description](#description)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
* [4 References](#references)






<a id="cite-note-3" href="#cite-ref-3">[3]</a>



### Board Representation


The board is [represented](Board_Representation "Board Representation") by a 12x12 [mailbox](Mailbox "Mailbox") [array](Array "Array") in conjunction with [piece-lists](Piece-Lists "Piece-Lists"). 
An [attack table](Attack_and_Defend_Maps "Attack and Defend Maps") utilizes [square control](Square_Control "Square Control") and a cheap [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), and is calculated from scratch once per node - one [byte](Byte "Byte") per square and color in "ppbbrrqk" order, indicating which pieces control that square including bishop/rook [x-rays](X-ray "X-ray") through queen and king. The two-bit bb counter includes knight and bishop attacks. 
Strictly [legal](Legal_Move "Legal Move") [move generation](Move_Generation "Move Generation") requires determination of [pinned pieces](Pin "Pin"), also used in [evaluation](Evaluation "Evaluation"). 



### Search


The [search](Search "Search") applies [NegaScout](NegaScout "NegaScout") with [TT](Transposition_Table "Transposition Table"), [AEL-pruning](AEL-Pruning "AEL-Pruning"), [quiescence](Quiescence_Search "Quiescence Search") and various [extensions](Extensions "Extensions") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows"). 
[Move ordering](Move_Ordering "Move Ordering") considers [hash move](Hash_Move "Hash Move"), [re-captures](Captures "Captures"), two [killers](Killer_Move "Killer Move"), captures with positive [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), [quiet moves](Quiet_Moves "Quiet Moves") with priority from attacked squares to none attacked or defended squares, pawn moves, losing captures, and remaining. 



### Evaluation


[Evaluation](Evaluation "Evaluation") focuses on [material balance](Material#Balance "Material") with trade down bonus if ahead. 
Positional feature terms, considering [pawn structure](Pawn_Structure "Pawn Structure"), [piece development](Development "Development"), [king safety](King_Safety "King Safety"), [hanging pieces](Hanging_Piece "Hanging Piece"), etc., 
rarely exceed the value of one pawn, except [unstoppable passers](Unstoppable_Passer "Unstoppable Passer") in [pawn endgames](Pawn_Endgame "Pawn Endgame") due to implementation of the [rule of the square](Rule_of_the_Square "Rule of the Square").



## Forum Posts


* [Freeware chess program RDCHESS V2](https://groups.google.com/d/msg/rec.games.chess.computer/7M2Pe1LUWIY/g3uKxbx8fpkJ) by [Rudolf Posch](Rudolf_Posch "Rudolf Posch"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 31, 2001
* [Freeware chess program RDCHESS V2](https://www.stmintz.com/ccc/index.php?id=172719) by [Rudolf Posch](Rudolf_Posch "Rudolf Posch"), [CCC](CCC "CCC"), May 31, 2001
* [Last Winboard engine updates: Comet B46 (Leiden) and RDChess v3.0.](https://www.stmintz.com/ccc/index.php?id=234744) by [Leo Dijksman](Leo_Dijksman "Leo Dijksman"), [CCC](CCC "CCC"), June 09, 2002


## External Links


* [RDChess](https://web.archive.org/web/20050309185315/http://www.rdchess.com/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), March 09, 2005)
* [RDChess - RDChess Übersicht](http://members.aon.at/rposch/page_2_1.html) (German)
* [RDChess 3.23](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=RDChess%203.23) in [CCRL Blitz](CCRL "CCRL")
* [RDChess 3.23](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=RDChess%203.23) in [KCEC](KCEC "KCEC")
* [Schachclub Leinzell Schachprogramm RDChess](http://scleinzell.schachvereine.de/p_themen/freewared.shtml#3) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner") - Dezember 2001 (German)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Screenshot from [RDChess](https://web.archive.org/web/20050309185315/http://www.rdchess.com/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), March 09, 2005)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Kasparov versus Deep Junior 2003, Game 1](Kasparov_versus_Deep_Junior_2003#Game_1 "Kasparov versus Deep Junior 2003"), 23... Ba6
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [RDChess: RDChess Technical Program Description](https://web.archive.org/web/20050414085626/http://groups.msn.com/RudolfPosch/technicalprogamdescription1.msnw)

**[Up one Level](Engines "Engines")**







 
