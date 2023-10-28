---
title: Y
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Y!**



[](File:TurboKit20.jpg) [TurboKit TK20](6502#TK20 "6502") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
  

**Y!** (Why Not),   

a chess program written by primary author [Ulf Rathsman](Ulf_Rathsman "Ulf Rathsman"), supported by [Lars Hjörth](Lars_Hj%C3%B6rth "Lars Hjörth") and [book author](Category:Opening_Book_Author "Category:Opening Book Author") [Sandro Necchi](Sandro_Necchi "Sandro Necchi"). It was written in [6502](6502 "6502") [assembly](Assembly "Assembly") and played tournaments on the [TurboKit TK20](6502#TK20 "6502") by *Schaetzle+Bsteh* <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Y! competed the [WMCCC 1988](WMCCC_1988 "WMCCC 1988") as Y!88 and the [WMCCC 1989](WMCCC_1989 "WMCCC 1989") and [WCCC 1989](WCCC_1989 "WCCC 1989") as Y!89 (Why Not 89).



### Contents


* [1 Photos](#photos)
* [2 Description](#description)
* [3 See also](#see-also)
* [4 External Links](#external-links)
* [5 References](#references)






[](File:WMCCC88YNot.jpg)
[Ulf Rathsman](Ulf_Rathsman "Ulf Rathsman") and [Sandro Necchi](Sandro_Necchi "Sandro Necchi") of Y!88 at the [WMCCC 1988](WMCCC_1988 "WMCCC 1988") in [Almería](https://en.wikipedia.org/wiki/Almer%C3%ADa) <a id="cite-note-3" href="#cite-ref-3">[3]</a>



## Description


based on the [WCCC 1989](WCCC_1989 "WCCC 1989") booklet <a id="cite-note-4" href="#cite-ref-4">[4]</a>:




```
Y!89 uses a full, partly extended, width iterative [principal variation search](Principal_Variation_Search "Principal Variation Search") with [capture](Captures "Captures") and [promotion](Promotions "Promotions") [searches](Quiescence_Search "Quiescence Search") in [terminal nodes](Quiescent_Node "Quiescent Node"). The program is designed to be used in a cheap commercial environment, thus the work [memory](Memory "Memory") is still just 4 kbytes of [RAM](Memory#RAM "Memory"), and the good old [6502](6502 "6502") eight bit processor is used in tournaments emulated by the also commercially available [Turbo kit](6502#TK20 "6502"). The [search](Search "Search") is fast for a micro, and includes detection of [repeated positions](Repetitions "Repetitions") (actual as well as potential), and performs [extensions](Extensions "Extensions") for [check evasions](Check_Extensions "Check Extensions"), [passed pawn moves](Passed_Pawn_Extensions "Passed Pawn Extensions") and some king moves in [pawn endgames](Pawn_Endgame "Pawn Endgame").

```


```
Most of the [material](Material "Material") and [positional evaluation](Evaluation_of_Pieces "Evaluation of Pieces") is made [incrementally](Incremental_Updates "Incremental Updates") by the means of material value tables and [positional score boards](Piece-Square_Tables "Piece-Square Tables") for each piece type, created once for each position of the game with the computer to move. Some "absolute" evaluation is also done, e.g. for static evaluation of [unstoppable passed pawns](Unstoppable_Passer "Unstoppable Passer") and [pawn structure](Pawn_Structure "Pawn Structure"). 

```

## See also


* [Conchess](Conchess "Conchess")
* [Princhess](Princhess "Princhess")


## External Links


* [Y!'s ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=356)
* [Why Not 89's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=455)
* [Conchess](http://www.schach-computer.info/wiki/index.php/Conchess) – [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German) <a id="cite-note-5" href="#cite-ref-5">[5]</a>


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Image from [ICT 2006](ICT_2006 "ICT 2006") and 13th Chess Computer Users (Gebruikers) tournament old [CSVN](CSVN "CSVN") site [Photo Gallery 24](http://old.csvn.nl/gallery24.html), Photos by [Eric van Reem](Eric_van_Reem "Eric van Reem") and [Kees Sio](index.php?title=Kees_Sio&action=edit&redlink=1 "Kees Sio (page does not exist)")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [TurboKit – Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/TurboKit)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Image by [László Lindner](L%C3%A1szl%C3%B3_Lindner "László Lindner") from [László Lindner](L%C3%A1szl%C3%B3_Lindner "László Lindner") (**1989**).*Die wiederauferstandene Mikro-Weltmeisterschaft - 8.Mikroschachcomputer - WM 1988 in Almeria*. [Europa-Rochade](https://de.wikipedia.org/wiki/Rochade_Europa), 01/02-1989, [pdf](http://schaakcomputers.nl/hein_veldhuis/database/files/11-1988,%20Europa-Rochade,%20Die%208.%20Mikroschachcomputer-WM%201988%20in%20Almeria.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis") (German)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Karsten Bauermeister](Karsten_Bauermeister "Karsten Bauermeister") (**1998**). *Die Geschichte der Conchess-Schachcomputer*. [Computerschach und Spiele](Computerschach_und_Spiele "Computerschach und Spiele"), Heft 4, August-September 1998

**[Up one level](Engines "Engines")**







 
