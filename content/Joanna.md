---
title: Joanna
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Joanna**


**Joanna**,  

the first Polish chess program developed from 1992 to 1994 by [Adam Kujawski](Adam_Kujawski "Adam Kujawski") as part of his masters thesis at [University of Warsaw](University_of_Warsaw "University of Warsaw") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. First written in [Turbo Pascal](Pascal "Pascal") and re-written in [C](C "C"), Joanna has been revived by [Jim Ablett](Jim_Ablett "Jim Ablett"), who added [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") support to the version which played the [PCCC 2002](PCCC_2002 "PCCC 2002"). The published source applies plain [alpha-beta search](Alpha-Beta "Alpha-Beta") with [aspiration windows](Aspiration_Windows "Aspiration Windows") at the [root](Root "Root"), but no classical [iterative deepening](Iterative_Deepening "Iterative Deepening"). Instead, a leading two [ply](Ply "Ply") search is used to calibrate the final depth of the main search, dependent on the [average thinking time](Time_Management "Time Management"). Its [evaluation](Evaluation "Evaluation") concepts such as [king-piece tropism](King_Safety#KingTropism "King Safety"), are partly adopted in [Evaluation Function Draft](Evaluation_Function_Draft "Evaluation Function Draft"). Following [point values](Point_Value "Point Value") were defined to determine the [material balance](Material#Balance "Material"): [Pionek](Pawn "Pawn") = 100, [Skoczek](Knight "Knight") = 290, [Goniec](Bishop "Bishop") = 310, [Wieża](Rook "Rook") = 500, [Hetman](Queen "Queen") = 950 and [Król](King "King") = 20.000. The thesis further mentions a [learning approach](Learning "Learning") adopted from [Bebe](Bebe "Bebe"), dubbed BeBe+, utilizing a [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### Contents


* [1 Selected Games](#selected-games)
* [2 Publications](#publications)
* [3 External Links](#external-links)
	+ [3.1 Chess Engine](#chess-engine)
	+ [3.2 Misc](#misc)
* [4 References](#references)






[PCCC 2002](PCCC_2002 "PCCC 2002"), round 7, Joanna 2002 - [Bread Chess](index.php?title=Bread_Chess&action=edit&redlink=1 "Bread Chess (page does not exist)") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "PCCC 2002"]
[Site "Lodz"]
[Date "2002.09.15"]
[Round "7"]
[White "Joanna 2002"]
[Black "Bread Chess"]
[Result "1/2-1/2"]

1.e4 d5 2.Nc3 dxe4 3.Nxe4 e5 4.Qh5 Nd7 5.Bc4 g6 6.Qg5 Be7 7.Qg3 f5 8.Qf3 Nh6 9.Qe3 Nb6 
10.Bb5+ c6 11.Qxh6 fxe4 12.Be2 Bg5 13.Qg7 Bf6  14.Qh6 Bg5 15.Qg7 Bf6 16.Qh6 Bg5 1/2-1/2

```

## Publications


* [Adam Kujawski](Adam_Kujawski "Adam Kujawski") (**1994**). *Programowanie gry w szachy*. Masters thesis, [University of Warsaw](University_of_Warsaw "University of Warsaw"), [pdf](http://mkarasinski.pl/_cms/files/Adam%20Kujawski%20szachy.pdf)


## External Links


### Chess Engine


* [Index of /chess/engines/Jim Ablett/JOANNA 2002](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/JOANNA%202002/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Armageddon Chess - joanna\_EXE.zip](http://www.armageddonchess.com/download.htm)


### Misc


* [Joanna from Wikipedia](https://en.wikipedia.org/wiki/Joanna)
* [Joanna (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Joanna_%28disambiguation%29)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Adam Kujawski](Adam_Kujawski "Adam Kujawski") (**1994**). *Programowanie gry w szachy*. Masters thesis, [University of Warsaw](University_of_Warsaw "University of Warsaw") (Polish)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") (**1991**). *Learning in Bebe.* [ICCA Journal, Vol. 14, No. 4](ICGA_Journal#14_4 "ICGA Journal")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [I Mistrzostwa Polski Programów Szachowych - Partie (PGN)](http://mpps.maciej.szmit.info/mpps-1/)

**[Up one Level](Engines "Engines")**







 
