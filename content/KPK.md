---
title: KPK
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* [Game Phases](Game_Phases "Game Phases") \* [Endgame](Endgame "Endgame") \* [Pawn Endgame](Pawn_Endgame "Pawn Endgame") \* KPK**


A very common pattern in chess games is to be up exactly one [pawn](Pawn "Pawn") and then try to trade down to a won KP vs K endgame. So this is a very fundamental ending that good chess programs should understand.



## Perfect Heuristics


This ending can also be determined perfectly with a set of heuristics <a id="cite-note-1" href="#cite-ref-1">[1]</a>.



## Imperfect Heuristics


There is also an imperfect solution that yields reasonably good results - using [interior node recognizers](Interior_Node_Recognizer "Interior Node Recognizer") detecting positions that are obviously won or drawn, but leaving "unclear" positions to evaluation and/or further [search](Search "Search"). An example of such a set of heuristics is given below:



### KPK is drawn


* In the case that the pawn can be immediately captured, might be delegated to the [quiescence search](Quiescence_Search "Quiescence Search")
* Defending king stands directly in front of the pawn, the other king - directly behind it, weaker side to move
* Defending king as above, the other king diagonally behind the pawn, stronger side to move
* Kings stand in the vertical [opposition](Opposition "Opposition") and the pawn is on the right/left side of the king of the stronger side, which is about to move
* In the above position the stronger side moves a pawn, giving check
* Assuming the squares are numbered 0..63, H1 being 0, the following code marks positions as drawn:



```C++

// a feeble attempt at using corresponding squares
if ( isPiece(WHITE,KING, pawn_sq-7) || isPiece(WHITE,KING, pawn_sq-8) || isPiece(WHITE,KING, pawn_sq-9) ) {
   if ( isPiece(BLACK,KING, pawn_sq+15) || isPiece(BLACK,KING, pawn_sq+16) || isPiece(BLACK,KING, pawn_sq+17) ) {
     if (to_move == WHITE && ROW(blackKingLoc) != ROW_8 ) return DRAW;
   }
}

```

Please note that the code **must** exclude positions where the defending king is on the last rank. Additionally there are drawn rook pawn cases where the defender prevents the king on the pawn's [frontspan](Pawn_Spans "Pawn Spans") from leaving the rook file.



### KPK is won


* Stronger king defends **all** [stop](Stop_Square "Stop Square") and [telestop(s)](Pawn_Spans#StopandDistantStop "Pawn Spans"), including the [promotion square](Promotion_Square "Promotion Square") up to three squares. With defender to move, one has to consider whether the pawn can be captured, since defended stop square does not necessarily imply the pawn is defended as well. Additionally, there is a [stalemate](Stalemate "Stalemate") [exception](https://en.wikipedia.org/wiki/Key_square#An_exception) with the knight pawn.
* Defending king is (leaves after moving) outside the [square of the pawn](Rule_of_the_Square#TheSquareofthePawn "Rule of the Square") <a id="cite-note-2" href="#cite-ref-2">[2]</a>


 if the own king blocks the [frontspan](Pawn_Spans "Pawn Spans"), it is still won. However the defending king may further reach the "square of the pawn" due to the extra [tempo](Tempo "Tempo") and one needs to apply some more rules to avoid knowledge holes in that cases.
## See also


* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis")
* [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")






## Selected Publications


### 1970 ...


* [Soei Tan](Soei_Tan "Soei Tan") (**1972**). *Representation of knowledge for very simple pawn endings in chess*. Report MIP-R-98; School of Artificial Intelligence, [University of Edinburgh](University_of_Edinburgh "University of Edinburgh")
* [Max Bramer](Max_Bramer "Max Bramer") (**1977**) *KPK: using effective distance.* [Open University](https://en.wikipedia.org/wiki/Open_University), [Milton Keynes](https://en.wikipedia.org/wiki/Milton_Keynes)
* [Max Bramer](Max_Bramer "Max Bramer") (**1977**). *KPK: Some Quantitative Data.* Technical Report, [Open University](https://en.wikipedia.org/wiki/Open_University), Faculty of Mathematics.
* [Mike Clarke](Mike_Clarke "Mike Clarke") (**1977**). *A quantitative study of KPK*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1"), pp. 108-118
* [Pericles Negri](index.php?title=Pericles_Negri&action=edit&redlink=1 "Pericles Negri (page does not exist)") (**1977**). *Inductive Learning in a Hierarchical Model for Representing Knowledge in Chess End Games*. [pdf](http://www.mli.gmu.edu/papers/69-78/77-2.pdf)
* [Ryszard Michalski](Ryszard_Michalski "Ryszard Michalski"), [Pericles Negri](index.php?title=Pericles_Negri&action=edit&redlink=1 "Pericles Negri (page does not exist)") (**1977**). *An experiment on inductive learning in chess endgames*. [Machine Intelligence 8](http://www.doc.ic.ac.uk/~shm/MI/mi8.html), [pdf](http://www.mli.gmu.edu/papers/69-78/77-1.pdf)
* [Max Bramer](Max_Bramer "Max Bramer") (**1978**). *A Note on KPK.* Technical Report, the [Open University](https://en.wikipedia.org/wiki/Open_University): Faculty of Mathematics, [Milton Keynes](https://en.wikipedia.org/wiki/Milton_Keynes), England.


### 1980 ...


* [Don Beal](Don_Beal "Don Beal"), [Mike Clarke](Mike_Clarke "Mike Clarke") (**1980**). *The Construction of Economical and Correct Algorithms for King and Pawn against King*. [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")
* [Max Bramer](Max_Bramer "Max Bramer") (**1980**). *An Optimal Algorithm for KPK using Pattern Knowledge.* [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")
* [Alen Shapiro](Alen_Shapiro "Alen Shapiro"), [Tim Niblett](Tim_Niblett "Tim Niblett") (**1982**). *Automatic Induction of Classification Rules for Chess End game.* [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
* [David Slate](David_Slate "David Slate") (**1984**). *Interior-node Score Bounds in a Brute-force Chess Program.* [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal")
* [Ard van Bergen](Ard_van_Bergen "Ard van Bergen") (**1985**). *An Ulti-Mate Look at the KPK Data Base*. [ICCA Journal, Vol. 8, No. 4](ICGA_Journal#8_4 "ICGA Journal")
* [Ard van Bergen](Ard_van_Bergen "Ard van Bergen"), [Theo van der Storm](Theo_van_der_Storm "Theo van der Storm") (**1986**). *The KPK Endgame: a Unit Correction*. [ICCA Journal, Vol. 9, No. 1](ICGA_Journal#9_1 "ICGA Journal")
* [Max Bramer](Max_Bramer "Max Bramer") (**1986**). *KPK Endgame Databases: a Response From the Source.* [ICCA Journal, Vol. 9, No. 3](ICGA_Journal#9_3 "ICGA Journal")
* [Hans Zellner](Hans_Zellner "Hans Zellner") (**1989**). *The KPK Database Revisited*. [ICCA Journal, Vol. 12, No. 2](ICGA_Journal#12_2 "ICGA Journal")


### 1990 ...


* [Guy Haworth](Guy_Haworth "Guy Haworth"), [Meel Velliste](Meel_Velliste "Meel Velliste") (**1998**). *[Chess Endgames and Neural Networks](http://centaur.reading.ac.uk/4569/)*. [ICCA Journal, Vol. 21, No. 4](ICGA_Journal#21_4 "ICGA Journal")
* [Ulrich Thiemonds](Ulrich_Thiemonds "Ulrich Thiemonds") (**1999**). *Ein regelbasiertes Spielprogramm für Schachendspiele*. [University of Bonn](https://en.wikipedia.org/wiki/University_of_Bonn), Diplom thesis, [pdf](https://www.idb.uni-bonn.de/publications/da/da_thiemonds_1999.pdf) (German)


## Forum Posts


### 2005 ...


* [Is this rule safe (how has K&Ps vs K&Ps databases? ...)](http://www.talkchess.com/forum/viewtopic.php?t=14578) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), June 20, 2007 » [Now](Now "Now"), [Pawn Endgame](Pawn_Endgame "Pawn Endgame")


### 2010 ...


* [KPK](http://www.talkchess.com/forum/viewtopic.php?t=46651) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), December 30, 2012
* [KPK bitbase](http://www.talkchess.com/forum/viewtopic.php?t=46893) by [Maarten Bults](index.php?title=Maarten_Bults&action=edit&redlink=1 "Maarten Bults (page does not exist)"), [CCC](CCC "CCC"), January 16, 2013
* [How to implement KPK ?](http://www.talkchess.com/forum/viewtopic.php?t=47557) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [CCC](CCC "CCC"), March 21, 2013


### 2015 ...


* [Yet another KPK endgame table generator: pfkpk](http://www.talkchess.com/forum/viewtopic.php?t=57517) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), September 05, 2015 » [Endgame Bitbases](Endgame_Bitbases "Endgame Bitbases") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Test position that requires KKP evaluation](http://www.talkchess.com/forum/viewtopic.php?t=59928) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), April 22, 2016
* [kpk bitbase, worthless?](http://www.talkchess.com/forum/viewtopic.php?t=60151) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), May 12, 2016
* [Eucalyptus - KPK Bitbases Generator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70815) by [Toni Helminen](Toni_Helminen "Toni Helminen"), [CCC](CCC "CCC"), May 24, 2019
* [The Poor Man's KP Bitbase](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70942) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), June 07, 2019


### 2020 ...


* [Syzygy bases from memory](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77499) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 16, 2021 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")


## External Links


* [King and pawn versus king endgame from Wikipedia](https://en.wikipedia.org/wiki/King_and_pawn_versus_king_endgame)


 [Key square from Wikipedia](https://en.wikipedia.org/wiki/Key_square)
* [kervinck/pfkpk · GitHub](https://github.com/kervinck/pfkpk) » KPK [Bitbase](Endgame_Bitbases "Endgame Bitbases") by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") <a id="cite-note-4" href="#cite-ref-4">[4]</a>


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Max Bramer](Max_Bramer "Max Bramer") (**1977**) *KPK: using effective distance.* [Open University](https://en.wikipedia.org/wiki/Open_University), [Milton Keynes](https://en.wikipedia.org/wiki/Milton_Keynes)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Set-wise Rule of the Square](King_Pattern#SetwiseRuleoftheSquare "King Pattern") with [Bitboards](Bitboards "Bitboards")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [kervinck/pfkpk · GitHub](https://github.com/kervinck/pfkpk)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Yet another KPK endgame table generator: pfkpk](http://www.talkchess.com/forum/viewtopic.php?t=57517) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), September 05, 2015

**[Up one Level](Pawn_Endgame "Pawn Endgame")**







 
