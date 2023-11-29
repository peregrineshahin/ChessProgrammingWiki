---
title: Rybka
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Rybka**



 [](http://rybkachess.com.www52.your-server.de/index.php?auswahl=Purchase+Rybka) Rybka 4 Logo <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Rybka**,  

a chess engine by primary author [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), from 2007 until 2010 dominating and reigning [World Computer Chess Champion](World_Computer_Chess_Championship "World Computer Chess Championship") and holder of the [Shannon Trophy](Shannon_Trophy "Shannon Trophy"), winning the [WCCC 2007](WCCC_2007 "WCCC 2007") <a id="cite-note-2" href="#cite-ref-2">[2]</a> , [WCCC 2008](WCCC_2008 "WCCC 2008"), [WCCC 2009](WCCC_2009 "WCCC 2009") and [WCCC 2010](WCCC_2010 "WCCC 2010"), but in June 2011 [disqualified](Rybka#Disqualification "Rybka") by the [ICGA](ICGA "ICGA") from all previous and future World Computer Chess Championships. Rybka further won various [IPCCC](IPCCC "IPCCC"), [Dutch Open Computer Chess Championships](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"), [International CSVN Tournaments](International_CSVN_Tournament "International CSVN Tournament") and on-line tournaments such as [CCT Tournaments](CCT_Tournaments "CCT Tournaments") and [ACCA Americas' Computer Chess Championships](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship"). Rybka is a standalone chess engine supporting the [UCI](UCI "UCI") protocol. 



## Versions


Vasik Rajlich started developing Rybka in about 2003, and worked full-time on it since 2005. The appearance of the free *Rybka 1 beta* <a id="cite-note-4" href="#cite-ref-4">[4]</a> and the first commercial version, *Rybka 1* <a id="cite-note-5" href="#cite-ref-5">[5]</a> end of 2005 was a sensation, and Rybka soon became the dominating program leading [rating lists](Engine_Rating_Lists "Engine Rating Lists") by a huge margin <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a> . *Rybka 3* was developed in collaboration with [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), the most recent and strongest version *Rybka 4* and the parallel version *Deep Rybka 4* appeared in April 2010, market as standalone chess engine from RybkaChess.com <a id="cite-note-8" href="#cite-ref-8">[8]</a> , from [ChessOK](ChessOK "ChessOK") optional with the [Aquarium](Aquarium "Aquarium") [GUI](GUI "GUI") <a id="cite-note-9" href="#cite-ref-9">[9]</a> , or from [ChessBase](ChessBase "ChessBase") packaged with the [Fritz](Fritz "Fritz") [GUI](GUI "GUI") <a id="cite-note-10" href="#cite-ref-10">[10]</a> . The demo version *Rybka 2.3.2a* can be downloaded for free <a id="cite-note-11" href="#cite-ref-11">[11]</a> .



## Achievements




|  Year
 |  Tournament
 |  Rank/From
 |  Title/Remarks
 |
| --- | --- | --- | --- |
|  2004
 | [CCT6](CCT6 "CCT6") |  50/54
 |  |
|  2005
 | [IPCCC 2005 b](IPCCC_2005_b "IPCCC 2005 b") |  1/12
 |  |
|  2006
 | [CCT8](CCT8 "CCT8") |  1/38
 |  |
|  | [ICT 2006](ICT_2006 "ICT 2006") |  1
 |  |
|  | [WCCC 2006](WCCC_2006 "WCCC 2006") |  3/18
 | *as Rajlich*, disqualified 2011
 |
|  | [DOCCC 2006](DOCCC_2006 "DOCCC 2006") |  1
 |  |
|  | [IPCCC 2006](IPCCC_2006 "IPCCC 2006") |  1/10
 |  |
|  2007
 | [ACCA 2007](ACCA_2007 "ACCA 2007") |  1/16
 |  |
|  | [CCT9](CCT9 "CCT9") |  1/54
 |  |
|  | [ICT 2007](ICT_2007 "ICT 2007") |  1
 |  |
|  | [WCCC 2007](WCCC_2007 "WCCC 2007") |  1/12
 |  World Computer Chess Champion, disqualified 2011
 |
|  | [DOCCC 2007](DOCCC_2007 "DOCCC 2007") |  1/14
 |  |
|  | [IPCCC 2007](IPCCC_2007 "IPCCC 2007") |  2/10
 |  |
|  2008
 | [ACCA 2008](ACCA_2008 "ACCA 2008") |  1/18
 |  |
|  | [ICT 2008](ICT_2008 "ICT 2008") |  1
 |  |
|  | [WCCC 2008](WCCC_2008 "WCCC 2008") |  1/10
 |  World Computer Chess Champion, disqualified 2011
 |
|  | [DOCCC 2008](DOCCC_2008 "DOCCC 2008") |  1/10
 |  |
|  2009
 | [ACCA 2009](ACCA_2009 "ACCA 2009") |  1/12
 |  |
|  | [WCCC 2009](WCCC_2009 "WCCC 2009") |  1/10
 |  World Computer Chess Champion, disqualified 2011
 |
|  | [DOCCC 2009](DOCCC_2009 "DOCCC 2009") |  1/9
 |  |
|  2010
 | [ICT 2010](ICT_2010 "ICT 2010") |  1/14
 |  |
|  | [WCCC 2010](WCCC_2010 "WCCC 2010") |  1/10
 |  World Computer Chess Champion, disqualified 2011
 |
|  | [DOCCC 2010](DOCCC_2010 "DOCCC 2010") |  1/20
 |  |
|  2012
 | [ICT 2012](ICT_2012 "ICT 2012") |  1/8
 |  |


## Program Internals


Rybka is a [bitboard](Bitboards "Bitboards") engine, first versions [rotated](Rotated_Bitboards "Rotated Bitboards"), Rybka 4 apparently [magic bitboards](Magic_Bitboards "Magic Bitboards") for [sliding piece attack](Sliding_Piece_Attacks "Sliding Piece Attacks") and [move generation](Move_Generation "Move Generation"). Vasik once posted a snippet of Rybka source-code, a typical [bitboard serialization](Bitboard_Serialization "Bitboard Serialization") loop to generate white knight captures <a id="cite-note-12" href="#cite-ref-12">[12]</a> .




```C++
for (bb_t knights = Board.pieces [WN]; knights; knights &= knights-1)
{
    int knight_sq = bit_scan (knights);
    for (bb_t captures = knight_moves [knight_sq] & opponent_pieces; captures; captures &= captures - 1)
    {
        int capture_sq = bit_scan (captures);
        *moves ++ = move (knight_sq, capture_sq);
        *values++ = Board.sq [capture_sq] * 256 + 192;
    }
}

```

Due to the disputed [open source engines](Category:Open_Source "Category:Open Source") [Strelka 2.0](Strelka "Strelka") and later [Ippolit](Ippolit "Ippolit"), which accordant to Vasik Rajlich were both based on or heavily influenced by re-engineered Rybka executables <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a> , other implementation details were released to the public, such as [material-](Material_Tables "Material Tables") and material imbalance tables, aggressive [LMR](Late_Move_Reductions "Late Move Reductions"), [razoring](Razoring "Razoring") <a id="cite-note-15" href="#cite-ref-15">[15]</a> and some variation of [singular extensions](Singular_Extensions "Singular Extensions") <a id="cite-note-16" href="#cite-ref-16">[16]</a> . [Zach Wegner](Zach_Wegner "Zach Wegner") elaborated on [evaluation](Evaluation "Evaluation") issues, and compared *Rybka 1 beta* with [Fruit's](Fruit "Fruit") evaluation <a id="cite-note-17" href="#cite-ref-17">[17]</a> , continued by former anonymous author "BB+" alias [Mark Watkins](Mark_Watkins "Mark Watkins") in February 2011 <a id="cite-note-18" href="#cite-ref-18">[18]</a> .



## Release Dates


* Rybka 1.0 beta : 2005-12
* Rybka 1.0 :
* Rybka 1.1 : 2006-04
* Rybka 1.2 : 2006-06
* Rybka 1.5 :
* Rybka 1.6.1 :
* Rybka 2.0 :
* Rybka 2.2 : 2006
* Rybka 2.2n2 : 2006-12
* Rybka 2.3 : 2007-01
* Rybka 2.3.1 : 2007-02
* Rybka 2.3.2a : 2007-06
* Rybka 3 : 2008-08
* Rybka 4 : 2010-05
* Rybka 4.1 : 2011-3


## Controversies


### Rybka 1.0 and Fruit


Rajlich's interpretation of [nodes](Nodes_per_Second "Nodes per Second") and [depth](Depth "Depth") <a id="cite-note-19" href="#cite-ref-19">[19]</a> <a id="cite-note-20" href="#cite-ref-20">[20]</a> <a id="cite-note-21" href="#cite-ref-21">[21]</a> <a id="cite-note-22" href="#cite-ref-22">[22]</a> <a id="cite-note-23" href="#cite-ref-23">[23]</a> , and the [controversy](https://en.wikipedia.org/wiki/Rybka#Strelka_controversy) about [Strelka](Strelka "Strelka") <a id="cite-note-24" href="#cite-ref-24">[24]</a> <a id="cite-note-25" href="#cite-ref-25">[25]</a> raised suspicions about the initial origin of Rybka 1.0 <a id="cite-note-26" href="#cite-ref-26">[26]</a> <a id="cite-note-27" href="#cite-ref-27">[27]</a> , but Vasik Rajlich categorically denied Rybka 1.0 was based on [Fruit](Fruit "Fruit") <a id="cite-note-28" href="#cite-ref-28">[28]</a> <a id="cite-note-29" href="#cite-ref-29">[29]</a> , as initially confirmed by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") in 2005 <a id="cite-note-30" href="#cite-ref-30">[30]</a> after early rumors <a id="cite-note-31" href="#cite-ref-31">[31]</a> and questions <a id="cite-note-32" href="#cite-ref-32">[32]</a> arose, but despite confusing Fruit using [MTD(f)](MTD(f) "MTD(f)"), Donninger claimed Rybka was basically Fruit in 2007 <a id="cite-note-33" href="#cite-ref-33">[33]</a>.


Vasik Rajlich's most quoted statement in these discussions was probably from an interview in *uciengines.de*, December 20, 2005 <a id="cite-note-34" href="#cite-ref-34">[34]</a> :




```C++
Yes, the publication of Fruit 2.1 was huge. Look at how many engines took a massive jump in its wake: Rybka, Hiarcs, Fritz, Zappa, Spike, List, and so on. I went through the Fruit 2.1 source code forwards and backwards and took many things.
...
Anyway, if I really had to give a number - my wild guess is that Rybka would be 20 rating points weaker had Fruit not appeared. 

```

### Ippolit


The appearance of the [Ippolit](Ippolit "Ippolit") [open source program](Category:Open_Source "Category:Open Source") by pseudonymous authors in May 2009, and Rajlich's claim it is a [clone](Category:Clone "Category:Clone") of *Rybka 3* <a id="cite-note-35" href="#cite-ref-35">[35]</a> without any substantiation and evidence, caused further discussions <a id="cite-note-36" href="#cite-ref-36">[36]</a> .



### Open Letters


In January 2011, [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") confirmed that Strelka, the allegedly clone of Rybka, was not a verbatim copy of the source code from Fruit, but a [bitboard](Bitboards "Bitboards") re-write of Fruit with some other ideas, and not just an extraction of a couple of ideas <a id="cite-note-37" href="#cite-ref-37">[37]</a> <a id="cite-note-38" href="#cite-ref-38">[38]</a> <a id="cite-note-39" href="#cite-ref-39">[39]</a> .


On February 19, 2011 [ICGA](ICGA "ICGA") president [David Levy](David_Levy "David Levy") broached on [cloning](Category:Clone "Category:Clone") issues in a *ChessVibes* column <a id="cite-note-40" href="#cite-ref-40">[40]</a> . In March 2011, following computer chess programmers signed an open letter to [David Levy](David_Levy "David Levy"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") and the board of the [ICGA](ICGA "ICGA"), to support the claim Rybka 1.0 beta and subsequent versions were allegedly derivatives from [Fabien Letouzey’s](Fabien_Letouzey "Fabien Letouzey") program [Fruit 2.1](Fruit "Fruit"):



* [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey")
* [Zach Wegner](Zach_Wegner "Zach Wegner")
* [Mark Uniacke](Mark_Uniacke "Mark Uniacke")
* [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen")
* [Ed Schröder](Ed_Schroder "Ed Schroder") <a id="cite-note-41" href="#cite-ref-41">[41]</a> <a id="cite-note-42" href="#cite-ref-42">[42]</a>
* [Don Dailey](Don_Dailey "Don Dailey")
* [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron")
* [Richard Pijl](Richard_Pijl "Richard Pijl")
* [Amir Ban](Amir_Ban "Amir Ban")
* [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie")
* [Tord Romstad](Tord_Romstad "Tord Romstad")
* [Ralf Schäfer](Ralf_Sch%C3%A4fer "Ralf Schäfer")
* [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg")
* [Johannes Zwanzger](Johannes_Zwanzger "Johannes Zwanzger")
* [Shay Bushinsky](Shay_Bushinsky "Shay Bushinsky")
* [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm")


The letter was published in the private [ICGA Investigations Wiki](ICGA_Investigations "ICGA Investigations") <a id="cite-note-43" href="#cite-ref-43">[43]</a> and elsewhere <a id="cite-note-44" href="#cite-ref-44">[44]</a> <a id="cite-note-45" href="#cite-ref-45">[45]</a> . The German sites [Heise online](http://de.wikipedia.org/wiki/Heise_online) <a id="cite-note-46" href="#cite-ref-46">[46]</a> and [Spiegel Online](https://en.wikipedia.org/wiki/Der_Spiegel#Spiegel_Online) broached the issue <a id="cite-note-47" href="#cite-ref-47">[47]</a> .



## Pre-Beta Rybka and Crafty


In February and March 2011, evidence was found by [Zach Wegner](Zach_Wegner "Zach Wegner") and [Mark Watkins](Mark_Watkins "Mark Watkins") that pre-Beta Rybka, which played the [CCT6](CCT6 "CCT6") in January 2004, and competed in tournaments of [Engine Rating Lists](Engine_Rating_Lists "Engine Rating Lists") such as [ChessWar](ChessWar "ChessWar") <a id="cite-note-48" href="#cite-ref-48">[48]</a> <a id="cite-note-49" href="#cite-ref-49">[49]</a> and *Le Fou numérique* <a id="cite-note-50" href="#cite-ref-50">[50]</a> , contain a substantial amount of [Crafty](Crafty "Crafty") code <a id="cite-note-51" href="#cite-ref-51">[51]</a> , confirmed by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") <a id="cite-note-52" href="#cite-ref-52">[52]</a> <a id="cite-note-53" href="#cite-ref-53">[53]</a> . Beside other evidence there are the known bugs in the old Crafty code (if ms == 99999) <a id="cite-note-54" href="#cite-ref-54">[54]</a> that caused [El Chinito](Chinito "Chinito") by primary author [Eugenio Castillo Jiménez](Eugenio_Castillo_Jim%C3%A9nez "Eugenio Castillo Jiménez") to be exposed as a clone <a id="cite-note-55" href="#cite-ref-55">[55]</a> <a id="cite-note-56" href="#cite-ref-56">[56]</a> .




## Disqualification


In June 2011, the [ICGA](ICGA "ICGA") has disqualified and banned Rybka and its programmer [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich") from previous and future World Computer Chess Championships. The ICGA accuses Rajlich of plagiarizing two other programs, [Crafty](Crafty "Crafty") and [Fruit](Fruit "Fruit"), and demands that he returns the trophies and prize money of the World Computer Chess Championships in [2007](WCCC_2007 "WCCC 2007"), [2008](WCCC_2008 "WCCC 2008"), [2009](WCCC_2009 "WCCC 2009") and [2010](WCCC_2010 "WCCC 2010") <a id="cite-note-57" href="#cite-ref-57">[57]</a> .


In August 2011, the board of the Dutch Computer Chess Federation ([CSVN](CSVN "CSVN")) declared the most serious doubts as to the rightfulness of ICGA's decision. Therefore, they have chosen not to abide by their sanctions against Rybka <a id="cite-note-58" href="#cite-ref-58">[58]</a> , see [ICGA Investigations](ICGA_Investigations "ICGA Investigations")



## See also


* [Claims that Strelka is Rybka](Claims_that_Strelka_is_Rybka "Claims that Strelka is Rybka")
* [Crafty](Crafty "Crafty")
* [Fritz](Fritz "Fritz")
* [Fruit](Fruit "Fruit")
* [ICGA Investigations](ICGA_Investigations "ICGA Investigations")
* [Ippolit](Ippolit "Ippolit")
* [Rybka Controversy](Rybka_Controversy "Rybka Controversy")
* [Strelka](Strelka "Strelka")


## Publications


* [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2007**). *The 15th World Computer Chess Championship*. [ICGA Journal, Vol. 30, No. 2](ICGA_Journal#30_2 "ICGA Journal") » [WCCC 2007](WCCC_2007 "WCCC 2007")
* [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2007**). *Factors affecting diminishing returns for searching deeper*. [CGW 2007](CGW_2007 "CGW 2007") » [Crafty](Crafty "Crafty"), Rybka, [Shredder](Shredder "Shredder"), [Diminishing Returns](Depth#DiminishingReturns "Depth")
* [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2007**). *Factors affecting diminishing returns for searching deeper*. [ICGA Journal, Vol. 30, No. 2](ICGA_Journal#30_2 "ICGA Journal"), [pdf](http://www.ailab.si/matej/doc/Factors_Affecting_Diminishing_Returns.pdf)
* [Hans Secelle](Hans_Secelle "Hans Secelle"). [Eric van Reem](Eric_van_Reem "Eric van Reem") (**2007**). *Golden Summer for RYBKA*. [ICGA Journal, Vol. 30, No. 3](ICGA_Journal#30_3 "ICGA Journal")
* [Mark Watkins](Mark_Watkins "Mark Watkins") (**2010**). *A comparison of Rybka and IPPOLIT*. [pdf](http://www.open-chess.org/download/file.php?id=13) <a id="cite-note-59" href="#cite-ref-59">[59]</a> » [Ippolit](Ippolit "Ippolit")
* [Mark Watkins](Mark_Watkins "Mark Watkins") (**2011**). *A comparison of Rybka 1.0 Beta and Fruit 2.1*, [pdf, February 12, 2011 Version](http://www.open-chess.org/download/file.php?id=272) <a id="cite-note-60" href="#cite-ref-60">[60]</a>
* [Mark Watkins](Mark_Watkins "Mark Watkins") (**2011**). *A comparison of Rybka 1.0 Beta and Fruit 2.1*, [pdf, February 24, 2011 Version](http://www.open-chess.org/download/file.php?id=304)
* [Mark Watkins](Mark_Watkins "Mark Watkins") (**2011**). *A comparison of Rybka 1.0 Beta and Fruit 2.1*, [pdf, March 11, 2011 Version](http://www.open-chess.org/download/file.php?id=332) » [Fruit](Fruit "Fruit")
* [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") (**2011**). *The Future of Computer Chess*. [Selective Search](Selective_Search "Selective Search") 154, pp. 11, [pdf](http://www.chesscomputeruk.com/SS_154.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")
* [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Krzysztof Siewicz](index.php?title=Krzysztof_Siewicz&action=edit&redlink=1 "Krzysztof Siewicz (page does not exist)") (**2011**). *Open Source has a Price*. [ICGA Journal, Vol. 34, No. 2](ICGA_Journal#34_2 "ICGA Journal")
* [David Levy](David_Levy "David Levy") (**2011**). *Rybka Disqualified and Banned from World Computer Chess Championships*.[ICGA Journal, Vol. 34, No. 2](ICGA_Journal#34_2 "ICGA Journal")
* [David Levy](David_Levy "David Levy") (**2011**). *A Very Sad Case*. [ICGA Journal, Vol. 34, No. 2](ICGA_Journal#34_2 "ICGA Journal")
* [Mark Lefler](Mark_Lefler "Mark Lefler"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Harvey Williamson](Harvey_Williamson "Harvey Williamson"), [ICGA panel](Who%27s_Who "Who's Who") (**2011**). *Rybka Investigations and Survey of Findings for the ICGA*. [ICGA Journal, Vol. 34, No. 2](ICGA_Journal#34_2 "ICGA Journal")
* [Eric Hallsworth](Eric_Hallsworth "Eric Hallsworth") (**2011**). *Rybka disqualified and banned by ICGA from World Computer Chess Championships, Lifetime Ban for Vasik Rajlich*. [Selective Search](Selective_Search "Selective Search") 155, pp. 8, [pdf](http://www.chesscomputeruk.com/SS_155.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")
* [Mark Watkins](Mark_Watkins "Mark Watkins") (**2011**). *Review of the Rybka case*. [pdf](http://www.open-chess.org/download/file.php?id=489) from [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums") <a id="cite-note-61" href="#cite-ref-61">[61]</a>
* [Søren Riis](S%C3%B8ren_Riis "Søren Riis") (**2012**). *A Gross Miscarriage of Justice in Computer Chess*. [pdf](http://www.chessbase.com/news/2011/riis01.pdf) hosted by [ChessBase](ChessBase "ChessBase")
* [Arno Nickel](Arno_Nickel "Arno Nickel") (**2012**). *[Die schöne neue Welt der Schachengines](http://www.edition-marco-shop.de/epages/64079634.sf/de_DE/?ObjectPath=/Shops/64079634/Categories/Schachgeschehen/Computerschach)*. [SCHACH](http://www.zeitschriftschach.de/) 2,3,5,6 2012, [pdf](http://www.edition-marco-shop.de/WebRoot/Store14/Shops/64079634/5177/F0A3/C389/D0DD/3A71/C0A8/2935/25F6/Die_schoene_neue_Welt_der_Schachengines.pdf) (German) <a id="cite-note-62" href="#cite-ref-62">[62]</a>
* [Ed Schröder](Ed_Schroder "Ed Schroder") (**2012**). *Rybka reloaded*. [pdf](http://www.top-5000.nl/Rybka%20Reloaded.pdf)
* [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2012**). *Detecting Fortresses in Chess*. [Elektrotehniški vestnik](http://ev.fe.uni-lj.si/), Vol. 79, Nos. 1-2, [pdf](https://ailab.si/matej/doc/Detecting_Fortresses_in_Chess.pdf) » [Houdini](Houdini "Houdini")
* [Mark Watkins](Mark_Watkins "Mark Watkins") (**2013**). *Review of the Rybka case*. [pdf](http://magma.maths.usyd.edu.au/~watkins/papers/RybkaRecap.pdf)
* [Søren Riis](S%C3%B8ren_Riis "Søren Riis") (**2014**). *[What makes a chess program original? Revisiting the Rybka case](http://www.sciencedirect.com/science/article/pii/S1875952114000159)*. [Entertainment Computing](http://www.journals.elsevier.com/entertainment-computing/), Vol. 5, No. 3
* [Don Dailey](Don_Dailey "Don Dailey"), [Adam Hair](Adam_Hair "Adam Hair"), [Mark Watkins](Mark_Watkins "Mark Watkins") (**2014**). *[Move Similarity Analysis in Chess Programs](http://www.sciencedirect.com/science/article/pii/S1875952113000177)*. [Entertainment Computing](http://www.journals.elsevier.com/entertainment-computing/), Vol. 5, No. 3, [preprint as pdf](http://magma.maths.usyd.edu.au/~watkins/papers/DHW.pdf) <a id="cite-note-63" href="#cite-ref-63">[63]</a>
* [David Levy](David_Levy "David Levy") (**2014**). *The RYBKA Case – Progress and Verdict*. [ICGA Journal, Vol. 37, No. 4](ICGA_Journal#37_4 "ICGA Journal") » [Rybka Controversy](Rybka_Controversy "Rybka Controversy")


## Forum Posts


### 2004


* [Re: CCT6: Rybka /Bodo ???](https://www.stmintz.com/ccc/index.php?id=345143) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), January 27, 2004


### 2005


* [Rybka 1.0 beta release - need testers](https://www.stmintz.com/ccc/index.php?id=465686) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), November 30, 2005
* [Rybka 1.0 Announcement](https://www.stmintz.com/ccc/index.php?id=466792) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), December 05, 2005
* [Is Rybbka a fruit clone?](https://www.stmintz.com/ccc/index.php?id=467208) by Ziad Haddad, [CCC](CCC "CCC"), December 06, 2005
* [Rybka - How much Fruit is inside?](https://www.stmintz.com/ccc/index.php?id=469130) by [Daniel Mehrmann](Daniel_Mehrmann "Daniel Mehrmann"), [CCC](CCC "CCC"), December 11, 2005
* [Rybka test position](https://www.stmintz.com/ccc/index.php?id=469143) by K. Burcham, [CCC](CCC "CCC"), December 11, 2005 » [Ktulu](Ktulu "Ktulu")
* [Rybka uses PVS and not MTD(f). Its no Fruit-Clone](https://www.stmintz.com/ccc/index.php?id=469209) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), December 12, 2005
* [The Code for the Rybka-Mate-Bug](https://www.stmintz.com/ccc/index.php?id=469728) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), December 13, 2005
* [Unmasking the Secrets of Rybka and Fruit](https://www.stmintz.com/ccc/index.php?id=470607) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), December 15, 2005
* [Secrets of Rybka and Fruit from my point of view](https://www.stmintz.com/ccc/index.php?id=470647) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), December 15, 2005
* [Spike-Rybka](https://www.stmintz.com/ccc/index.php?id=474330) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), December 28, 2005 » [IPCCC 2005 b](IPCCC_2005_b "IPCCC 2005 b")
* [The man behind Rybka and his thoughts as posted here on CCC](https://www.stmintz.com/ccc/index.php?id=475888) by Mike Byrne, [CCC](CCC "CCC"), December 31, 2005


### 2006


* [Rybka and Fruit on Chessbase](https://www.stmintz.com/ccc/index.php?id=479366) by [Walter Faxon](Walter_Faxon "Walter Faxon"), [CCC](CCC "CCC"), January 14, 2006 » [Fruit](Fruit "Fruit"), [ChessBase](ChessBase "ChessBase")
* [The superior Rybka chess knowledge](https://www.stmintz.com/ccc/index.php?id=480599) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), January 18, 2006
* [Rybka's NPS - one presumption](https://www.stmintz.com/ccc/index.php?id=487223) by [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković"), [CCC](CCC "CCC"), February 16, 2006 » [Nodes per Second](Nodes_per_Second "Nodes per Second")
* [Rybka @ CCT8](https://www.stmintz.com/ccc/index.php?id=489891) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), February 26, 2006


### 2007


* [outlook and plans for Rybka 3](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=18) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 09, 2007
* [Rybka 2.3 release date now Monday February 12](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=194) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), February 04, 2007
* [Rybka 2.3 readme](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=246) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), February 13, 2007
* [Rybka @ Leiden ICT7](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=1041) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), May 20, 2007
* [Open Letter and $100,000 Challenge to FIDE](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=1126) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), May 31, 2007
* [How secure is the source code of Rybka?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=1170) by SR, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), June 05, 2007
* [Rybka 2.3.2a readme](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=1360) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), June 18, 2007
* [Rybka @ Amsterdam 15th WCCC](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=1373) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), June 19, 2007
* [Strelka = Rybka 1.0](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=1655) by DarkAvenger, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 07, 2007 » [Strelka](Strelka "Strelka")
* [What Strelka tells about Rybka's nodecount and depth](http://www.talkchess.com/forum/viewtopic.php?t=14959) by [Ernest Bonnem](index.php?title=Ernest_Bonnem&action=edit&redlink=1 "Ernest Bonnem (page does not exist)"), [CCC](CCC "CCC"), July 09, 2007
* [Longer comments by V. Rajlich](http://www.talkchess.com/forum/viewtopic.php?t=14988) by [Marc Lacrosse](index.php?title=Marc_Lacrosse&action=edit&redlink=1 "Marc Lacrosse (page does not exist)"), [CCC](CCC "CCC"), July 10, 2007
* [(Experimental) 64-bit Rybka on Linux](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=1690) by [Sesse](Steinar_H._Gunderson "Steinar H. Gunderson"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 10, 2007 » [Linux](Linux "Linux")
* [Re: Is Rybka a derivative of Fruit?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?pid=19118#pid19118) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 14, 2007
* [Fruit, Rybka, Strelka final conclusion! (I hope)](http://www.talkchess.com/forum/viewtopic.php?t=15076) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), July 13, 2007
* [Rybka vs Zappa in Mexico City](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=2297) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), September 28, 2007
* [Re: I know something of Dr.Donninger](https://www.hiarcs.net/forums/viewtopic.php?t=398&start=19) by [Harvey Williamson](Harvey_Williamson "Harvey Williamson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 16, 2007 <a id="cite-note-64" href="#cite-ref-64">[64]</a>
* [Rybka @ Leiden 27th Dutch CCC](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=2510) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 29, 2007


### 2008


* [Strelka 2.0](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=3006) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2008 » [Strelka](Strelka "Strelka")
* [Re: Strelka 2.0 pg 4](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=3006;pg=4) by [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2008
* [Rajlich/Osipov/Rybka/Strelka/Answers by Convekta](http://www.talkchess.com/forum/viewtopic.php?t=19008) by [Eduard Nemeth](index.php?title=Eduard_Nemeth&action=edit&redlink=1 "Eduard Nemeth (page does not exist)"), [CCC](CCC "CCC"), January 17, 2008 » [Strelka](Strelka "Strelka"), [Convekta](ChessOK "ChessOK")
* [Anthony Cozzie speak !](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=3172) by Silvian, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), February 03, 2008 <a id="cite-note-65" href="#cite-ref-65">[65]</a>
* [Rybka 3 with new GUI: are they serious?!](http://www.talkchess.com/forum/viewtopic.php?t=20531) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), April 05, 2008 » [Aquarium](Aquarium "Aquarium")
* [Retry: Rybka 1.0 Beta Node Count Patch](http://www.talkchess.com/forum/viewtopic.php?t=20740) by Rick Fadden, [CCC](CCC "CCC"), April 19, 2008
* [Strelka Reverse Engineered from Rybka: Details Examined](http://www.talkchess.com/forum/viewtopic.php?t=20936) by Rick Fadden, [CCC](CCC "CCC"), May 01, 2008
* [Rybka @ Leiden 8th ICT](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=4247) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), June 01, 2008
* [Rybka 3 -- a hundred elo!](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=4807) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 08, 2008
* [Rybka 3 - some info](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=5020) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 19, 2008
* [Rybka 3: The dark truth behind the hype](http://www.talkchess.com/forum/viewtopic.php?t=22581) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), July 25, 2008
* [Rybka 3 Release Notes](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=5547) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 04, 2008
* [Rybka 3 FAQ](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=5576) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 05, 2008
* [Rybka v2.2n2 download](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=5606) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 06, 2008
* [Rybka 1.0 vs. Strelka](http://www.talkchess.com/forum/viewtopic.php?t=23118) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), August 19, 2008
* [Rybka in the nolot suite](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=23157) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), August 21, 2008 » [The Nolot Suite](The_Nolot_Suite "The Nolot Suite")
* [Questions for Vas](http://www.talkchess.com/forum/viewtopic.php?t=23249) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), August 25, 2008
* [A very simple question to Vas that can end it all](http://www.talkchess.com/forum/viewtopic.php?t=23252) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), August 25, 2008
* [Rybka questions and answers](http://www.talkchess.com/forum/viewtopic.php?t=23239) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), August 25, 2008
* [question to vas on similarity of rybka 1.0 to fruit](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=6772) by duncan, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 25, 2008
* [split 3 from Zach technical thread](http://www.talkchess.com/forum/viewtopic.php?t=23307) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), August 27, 2008
* [My two cents](http://www.talkchess.com/forum/viewtopic.php?t=23313) by [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie"), [CCC](CCC "CCC"), August 27, 2008
* [To campaign or not](http://www.talkchess.com/forum/viewtopic.php?t=23341) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 28, 2008
* [How a court detects a derivative work](http://www.talkchess.com/forum/viewtopic.php?t=23386) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), August 30, 2008
* [Is It Me or is the Source Comparison Page Rigged?](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=214422&t=23424) by RegicideX, [CCC](CCC "CCC"), September 01, 2008 <a id="cite-note-66" href="#cite-ref-66">[66]</a> <a id="cite-note-67" href="#cite-ref-67">[67]</a>
* [Plagiarism and Rybka](http://www.talkchess.com/forum/viewtopic.php?t=23474) by [Enrique Irazoqui](Enrique_Irazoqui "Enrique Irazoqui"), [CCC](CCC "CCC"), September 03, 2008
* [Rybka @ 16th WCCC in Beijing](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=7738) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 04, 2008
* [Strelka = Rybka 1.0 =Fruit 2.1 = Toga?? Oh how disappointing](http://www.talkchess.com/forum/viewtopic.php?t=24504) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), October 21, 2008
* [Rybka @ 28th Dutch CCC](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=8478) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), November 18, 2008


### 2009


* [Rybka @ Pamplona 17th ICGA World Computer Chess Championship](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=11022) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich") from [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), May 17, 2009 » [WCCC 2009](WCCC_2009 "WCCC 2009")
* [Rybka @ 29th Open Dutch Computer Chess Championship](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=12960) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 19, 2009 » [DOCCC 2009](DOCCC_2009 "DOCCC 2009")
* [Official statement on [Deleted](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=12995)?] by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 21, 2009


### 2010


* [Rybka 4 update](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=16262) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), April 11, 2010
* [Rybka 4 is final. (select games for fun)](http://www.talkchess.com/forum/viewtopic.php?t=34497) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), May 25, 2010
* [Rybka 4 Release Notes](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=17010) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), May 26, 2010
* [ICT Leiden 2010: Rybka wins with 8/9. Opening report](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=17206) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), May 30, 2010 » [ICT 2010](ICT_2010 "ICT 2010")
* [Rybka @ 10th ICT Leiden 2010](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=17240) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), May 31, 2010 » [ICT 2010](ICT_2010 "ICT 2010")
* [BB's Rybka/Ippolit comparison](http://www.open-chess.org/viewtopic.php?f=3&t=119) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 13, 2010
* [Deep Blue vs Rybka](http://www.talkchess.com/forum/viewtopic.php?t=36058) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 13, 2010
* [Kanazawa Diary (Rybka operator in Japan)](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=18935) by [Hans van der Zijden](Hans_van_der_Zijden "Hans van der Zijden"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), September 24, 2010 » [WCCC 2010](WCCC_2010 "WCCC 2010")
* [WCCC 2010 in Kanzawa, Japan](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=19026) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 2, 2010 » [WCCC 2010](WCCC_2010 "WCCC 2010")
* [Rybka @ 30th Dutch Computer Chess Championship](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=19574) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), November 16, 2010 » [DOCCC 2010](DOCCC_2010 "DOCCC 2010")
* [Brief Q&A about Rybka 1.0 Beta and Fruit 2.1](http://www.open-chess.org/viewtopic.php?f=3&t=815) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 14, 2010
* [Rybka Cluster Rental Program](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=20058) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), December 30, 2010


### 2011


* [Node counting](http://www.open-chess.org/viewtopic.php?f=5&t=1004) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 20, 2011 » [Node](Node "Node")
* [Fabien's open letter to the community](http://www.talkchess.com/forum/viewtopic.php?t=37762) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), January 23, 2011
* [Fabien's open letter to the community](http://www.open-chess.org/viewtopic.php?f=3&t=1014) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 23, 2011
* [Revisiting Strelka/Rybka](http://www.open-chess.org/viewtopic.php?f=3&t=1023) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 25, 2011
* [Feb 12 version: Rybka 1.0 Beta / Fruit 2.1 document](http://www.open-chess.org/viewtopic.php?f=5&t=1104) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 12, 2011
* [Attack of the clones | ChessVibes](https://web.archive.org/web/20180828211326/http://www.chessvibes.com/?q=reports/attack-of-the-clones) by [David Levy](David_Levy "David Levy"), February 19, 2011 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Open letter to the ICGA about the Rybka-Fruit issue](http://www.hiarcs.net/forums/viewtopic.php?t=4038) by [Harvey Williamson](Harvey_Williamson "Harvey Williamson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), March 01, 2011
* [Programmers Open Letter to ICGA on Rybka/Fruit](http://www.open-chess.org/viewtopic.php?f=3&t=1175) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 01, 2011
* [Rybka 1.6.1](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=21216) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), March 13, 2011
* [Longer Article](http://www.talkchess.com/forum/viewtopic.php?t=38440) by [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie"), [CCC](CCC "CCC"), March 17, 2011
* [History of eval changes in Rybka versions](http://www.open-chess.org/viewtopic.php?f=5&t=1281) by[BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 23, 2011
* [Rybka disqualified and banned from World Computer Chess Cham](http://www.talkchess.com/forum/viewtopic.php?t=39520) by Tim Chan, [CCC](CCC "CCC"), June 29, 2011
* [Rybka disqualified and banned from World Computer Chess Cham](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22232) by TheHug, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), June 29, 2011
* [Rybka disqualified and banned from WCCC](http://hiarcs.net/forums/viewtopic.php?t=4264&sid=ec7a3d377b4ca501b364599914913668) by [Harvey Williamson](Harvey_Williamson "Harvey Williamson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), June 29, 2011
* [Rybka disqualified and banned from WCCC](http://www.open-chess.org/viewtopic.php?f=3&t=1463) by [Jeremy Bernstein](Jeremy_Bernstein "Jeremy Bernstein"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 29, 2011
* [Rybka ban thoughts](http://www.talkchess.com/forum/viewtopic.php?t=39531) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 29, 2011
* [My two cents on Rybka's disqualification](http://www.talkchess.com/forum/viewtopic.php?t=39544) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), June 30, 2011
* [Dismissed with prejudice](http://www.talkchess.com/forum/viewtopic.php?t=39546) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 01, 2011
* [Voir Dire](http://www.talkchess.com/forum/viewtopic.php?t=39545) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 01, 2011 <a id="cite-note-68" href="#cite-ref-68">[68]</a>
* [Vas say something](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22265) by siam, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 01, 2011
* [The ICGA Process](http://open-chess.org/viewtopic.php?f=3&t=1466) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 01, 2011
* [Progess (often) is ugly, a summary try](http://www.open-chess.org/viewtopic.php?f=3&t=1471) by [Rebel](Ed_Schroder "Ed Schroder"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 03, 2011
* [Is Rybka that needs ICGA or the opposite ?](http://www.talkchess.com/forum/viewtopic.php?t=39593) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), July 03, 2011
* [The Intellectual Property Oxymoron](http://www.talkchess.com/forum/viewtopic.php?start=0&t=39592) by Gary Belton, [CCC](CCC "CCC"), July 03, 2011
* [The Evidence against Rybka](http://www.open-chess.org/viewtopic.php?f=5&t=1475) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 04, 2011
* [Why did the ICGA ignore this advice?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22337) by [John Sidles](index.php?title=John_Sidles&action=edit&redlink=1 "John Sidles (page does not exist)"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 06, 2011
* [Minority Report Plagiarism - Quantifying Evaluation Features](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22370) by [Trotsky](Chris_Whittington "Chris Whittington"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 09, 2011
* [Back to R3/IPPOLIT(R4?)](http://www.open-chess.org/viewtopic.php?f=5&t=1497) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 14, 2011
* [In retrospect](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22421) by [Rebel](Ed_Schroder "Ed Schroder"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 14, 2011
* [Minority Report 2 - Unravelling the technical report](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22486) by [Trotsky](Chris_Whittington "Chris Whittington"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 22, 2011
* [Minority Report 3, PST + other lookup tables are they legal?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22502) by [Trotsky](Chris_Whittington "Chris Whittington"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 25, 2011
* [On Rybka/Crafty and licensing/copyright](http://www.open-chess.org/viewtopic.php?f=5&t=1519) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 28, 2011
* [Thoughts on Fruit=Rybka EVAL](http://www.open-chess.org/viewtopic.php?f=3&t=1559) by [Rebel](Ed_Schroder "Ed Schroder"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 16, 2011
* [Apology to Vas](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22679) by [Rebel](Ed_Schroder "Ed Schroder"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 17, 2011


### 2012


* [Rybka evidence recapitulation](http://www.open-chess.org/viewtopic.php?f=5&t=1772) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2012
* [A Big Thanks and a Small Update](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=23957) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 08, 2012
* [Fruit/Rybka timeline](http://www.open-chess.org/viewtopic.php?f=5&t=1795) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 09, 2012
* [Rybka 1.0 source code](http://www.talkchess.com/forum/viewtopic.php?t=42248) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 31, 2012 <a id="cite-note-69" href="#cite-ref-69">[69]</a>


### 2021


* [Rybka Forum Is Officially Closed?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78078) by [supersharp77](index.php?title=Supersharp77&action=edit&redlink=1 "Supersharp77 (page does not exist)"), [CCC](CCC "CCC"), September 02, 2021


## External Links


### Rybka


* [Welcome to RybkaChess.com!](http://www.rybkachess.com/index.php)
* [Rybka Cluster - for the elite chess player](http://cluster.rybkachess.com/)
* [Rybka from Wikipedia](https://en.wikipedia.org/wiki/Rybka)
* [Rybka's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=79)
* [Rybka Chess Community Forum](http://rybkaforum.net/cgi-bin/rybkaforum/forum_show.pl)
* [Interview with Vasik Rajlich](http://www.top-5000.nl/int/rybka.htm) by [Christopher Conkie](index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [Michael Diosi](index.php?title=Michael_Diosi&action=edit&redlink=1 "Michael Diosi (page does not exist)"), [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") & [Alexander Schmidt](index.php?title=Alexander_Schmidt&action=edit&redlink=1 "Alexander Schmidt (page does not exist)"), December 20, 2005, hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
* [ChessAssistance.com Rybka Review](http://chessok.com/files/bobpawlak/News/RybkaReview.html) by [Robert Pawlak](Robert_Pawlak "Robert Pawlak"), September 23, 2006
* [Rybka 3.0 – Not just the strongest chess program in the world](http://www.chessbase.com/newsdetail.asp?newsid=4772), July 18, 2008, [ChessBase News](ChessBase "ChessBase")
* [Rybka's Monte Carlo analysis](http://www.chessbase.com/newsdetail.asp?newsid=5075) by [Steve Lopez](index.php?title=Steve_Lopez&action=edit&redlink=1 "Steve Lopez (page does not exist)"), [ChessBase News](ChessBase "ChessBase"), February 03, 2009


### Controversy


* [Rybka banned by International Games Federation – Rybka Ruling](http://chess.business-news-blog.eu/2011/rybka-banned-by-international-games-federation-rybka-ruling/)
* [Rybka, the world’s best chess engine, outlawed and disqualified | ExtremeTech](http://www.extremetech.com/extreme/88610-rybka-the-worlds-best-chess-engine-outlawed-and-disqualified) by [Sebastian Anthony](http://www.mrseb.co.uk/) on June 29, 2011
* [Computer chess champ stripped of its four titles](http://m.washingtontimes.com/news/2011/jun/30/computer-chess-champ-stripped-of-its-four-titles/) by [Claire Courchane](http://www.linkedin.com/pub/claire-courchane/2a/857/3b), [Washington Times](https://en.wikipedia.org/wiki/The_Washington_Times), June 30, 2011
* [Rybka Disqualified, Banned On Plagiarism Charges | ITProPortal.com](http://www.itproportal.com/2011/06/30/rybka-disqualified-banned-on-plagiarism-charges/) by [Ravi Mandalia](http://www.itproportal.com/staff/ravimandalia/), June 30, 2011
* [Boylston Chess Club Weblog: Rybka banned from computer champs; stripped of all its titles](http://boylston-chess-club.blogspot.com/2011/06/rybka-banned-from-computer-champs.html), June 30, 2011
* [Weltmeisterprogramm Rybka verliert alle Titel](http://www.spiegel.de/netzwelt/games/0,1518,771620,00.html) by [Frank Patalong](http://www.spiegel.de/extra/0,1518,632080,00.html), [Spiegel Online](https://en.wikipedia.org/wiki/Der_Spiegel#Spiegel_Online), July 01, 2011 (German)
* [Geklontes Fischchen](http://diepresse.com/home/spectrum/spielundmehr/676421/Geklontes-Fischchen) by [Stefan Löffler](index.php?title=Stefan_L%C3%B6ffler&action=edit&redlink=1 "Stefan Löffler (page does not exist)"), July 08, 2011, [DiePresse.com](http://diepresse.com/home/index.do) (German)
* [Rybka vs ICGA a different view](http://www.top-5000.nl/Rybka.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder"), November 09, 2011
* [Rybka evidence](http://www.top-5000.nl/evidence.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder"), November 09, 2011
* [A Gross Miscarriage of Justice in Computer Chess (part one)](http://www.chessbase.com/newsdetail.asp?newsid=7791) by [Søren Riis](S%C3%B8ren_Riis "Søren Riis"), [ChessBase News](ChessBase "ChessBase"), January 02, 2012 <a id="cite-note-70" href="#cite-ref-70">[70]</a> <a id="cite-note-71" href="#cite-ref-71">[71]</a> <a id="cite-note-72" href="#cite-ref-72">[72]</a>


 [A Gross Miscarriage of Justice in Computer Chess (part two)](http://www.chessbase.com/newsdetail.asp?newsid=7807) by [Søren Riis](S%C3%B8ren_Riis "Søren Riis"), [ChessBase News](ChessBase "ChessBase"), January 03, 2012 <a id="cite-note-73" href="#cite-ref-73">[73]</a> 
 [A Gross Miscarriage of Justice in Computer Chess (part three)](http://www.chessbase.com/newsdetail.asp?newsid=7811) by [Søren Riis](S%C3%B8ren_Riis "Søren Riis"), [ChessBase News](ChessBase "ChessBase"), January 04, 2012
 [A Gross Miscarriage of Justice in Computer Chess (part four)](http://www.chessbase.com/newsdetail.asp?newsid=7813) by [Søren Riis](S%C3%B8ren_Riis "Søren Riis"), [ChessBase News](ChessBase "ChessBase"), January 05, 2012 <a id="cite-note-74" href="#cite-ref-74">[74]</a>
* [ICGA/Rybka controversy: An interview with David Levy (1)](http://www.chessbase.com/newsdetail.asp?newsid=7899), [ChessBase News](ChessBase "ChessBase"), February 06, 2012


 [ICGA/Rybka controversy: An interview with David Levy (2)](http://www.chessbase.com/newsdetail.asp?newsid=7908), [ChessBase News](ChessBase "ChessBase"), February 10, 2012
* [ICGA/Rybka controversy: Feedback](http://www.chessbase.com/newsdetail.asp?newsid=7926), [ChessBase News](ChessBase "ChessBase"), February 17, 2012


### Misc


* [Rybka (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Rybka_%28disambiguation%29)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Rybka - for the serious chess player - Purchase Rybka](http://rybkachess.com.www52.your-server.de/index.php?auswahl=Purchase+Rybka)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Bulletin Day 7 WCCC 2007 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/news_item.php?id=25)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Rybka - for the serious chess player - Rybka team](http://rybkachess.com.www52.your-server.de/index.php?auswahl=Rybka+team)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Rybka 1.0 beta release - need testers](https://www.stmintz.com/ccc/index.php?id=465686) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), November 30, 2005
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Rybka 1.0 Announcement](https://www.stmintz.com/ccc/index.php?id=466792) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), December 05, 2005
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [SSDF Rating List 2007-04-21](http://www.talkchess.com/forum/viewtopic.php?t=13289) by [Thoralf Karlsson](index.php?title=Thoralf_Karlsson&action=edit&redlink=1 "Thoralf Karlsson (page does not exist)"), [CCC](CCC "CCC"), April 21, 2007
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [CEGT Quad Versions 40/120 (AMD 3500+/4200+)](http://www.husvankempen.de/nunn/40_120_ratinglist/Quad/qratinglist.html)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Rybka - for the serious chess player - Purchase Rybka](http://www.rybkachess.com/index.php?auswahl=Purchase+Rybka)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Rybka & Aquarium - ChessOK shop](http://chessok.com/shop/index.php?Home=index&cPath=7_1)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Chess software - Rybka 4](http://www.chessbase.com/shop/product.asp?pid=506) from [ChessBase](ChessBase "ChessBase")
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Rybka - for the serious chess player - Download Rybka 2.3.2a](http://www.rybkachess.com/index.php?auswahl=Demo+version)
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [re: rybka source code](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?pid=20132#pid20132) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 24, 2007
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Strelka 2.0](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=3006) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2008
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [My recent correspondence with Vasik Rajlich](http://www.talkchess.com/forum/viewtopic.php?t=34908) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), June 13, 2010
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Re: Strelka 2.0 pg 4](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=3006;pg=4) by [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2008
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [A question to Larry Kaufman](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=14574), by Erik, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), December 30/31, 2009
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Re: What do you folks make of this ?](http://www.open-chess.org/viewtopic.php?f=3&t=301#p2658) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 27, 2010
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Mark Watkins](Mark_Watkins "Mark Watkins") (**2011**). *A comparison of Rybka 1.0 Beta and Fruit 2.1*, [pdf, February 24, 2011 Version](http://www.open-chess.org/download/file.php?id=304)
19. <a id="cite-ref-19" href="#cite-note-19">↑</a> [What Strelka tells about Rybka's nodecount and depth](http://www.talkchess.com/forum/viewtopic.php?t=14959) by [Ernest Bonnem](index.php?title=Ernest_Bonnem&action=edit&redlink=1 "Ernest Bonnem (page does not exist)"), [CCC](CCC "CCC"), July 09, 2007
20. <a id="cite-ref-20" href="#cite-note-20">↑</a> [Does Rybka Properly Count Positions Evaluated?](http://www.johnljerz.com/superduper/tlxdownloadsiteMAIN/id18.html) by [John L. Jerz](John_L._Jerz "John L. Jerz")
21. <a id="cite-ref-21" href="#cite-note-21">↑</a> [To Jeroen and interested minds, re. Tiger node count](http://www.talkchess.com/forum/viewtopic.php?t=23037) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), August 15, 2008
22. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Re: Question to Larry Kaufman about Rybka](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=328195&t=32335) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), February 05, 2010
23. <a id="cite-ref-23" href="#cite-note-23">↑</a> [Node counting](http://www.open-chess.org/viewtopic.php?f=5&t=1004) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 20, 2011
24. <a id="cite-ref-24" href="#cite-note-24">↑</a> [Strelka = Rybka 1.0](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=1655) by DarkAvenger, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 07, 2007
25. <a id="cite-ref-25" href="#cite-note-25">↑</a> [Strelka 2.0](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=3006) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2008
26. <a id="cite-ref-26" href="#cite-note-26">↑</a> [Rybka 1.0 vs. Strelka](http://www.talkchess.com/forum/viewtopic.php?t=23118) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), August 19, 2008
27. <a id="cite-ref-27" href="#cite-note-27">↑</a> [Questions for Vas](http://www.talkchess.com/forum/viewtopic.php?t=23249) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), August 25, 2008
28. <a id="cite-ref-28" href="#cite-note-28">↑</a> [Re: Is Rybka a derivative of Fruit?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?pid=19118#pid19118) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 14, 2007
29. <a id="cite-ref-29" href="#cite-note-29">↑</a> [question to vas on similarity of rybka 1.0 to fruit](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=6772) by duncan, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 25, 2008
30. <a id="cite-ref-30" href="#cite-note-30">↑</a> [Rybka uses PVS and not MTD(f). Its no Fruit-Clone](https://www.stmintz.com/ccc/index.php?id=469209) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), December 12, 2005
31. <a id="cite-ref-31" href="#cite-note-31">↑</a> [Is Rybbka a fruit clone?](https://www.stmintz.com/ccc/index.php?id=467208) by Ziad Haddad, [CCC](CCC "CCC"), December 06, 2005
32. <a id="cite-ref-32" href="#cite-note-32">↑</a> [Rybka - How much Fruit is inside?](https://www.stmintz.com/ccc/index.php?id=469130) by [Daniel Mehrmann](Daniel_Mehrmann "Daniel Mehrmann"), [CCC](CCC "CCC"), December 11, 2005
33. <a id="cite-ref-33" href="#cite-note-33">↑</a> [Re: I know something of Dr.Donninger](https://www.hiarcs.net/forums/viewtopic.php?t=398&start=19) by [Harvey Williamson](Harvey_Williamson "Harvey Williamson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 16, 2007, quoted with the kind permission of [Chrilly](Chrilly_Donninger "Chrilly Donninger") and [Enir](Enrique_Irazoqui "Enrique Irazoqui")
34. <a id="cite-ref-34" href="#cite-note-34">↑</a> [Interview with Vasik Rajlich](http://www.top-5000.nl/int/rybka.htm) by [Christopher Conkie](index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [Michael Diosi](index.php?title=Michael_Diosi&action=edit&redlink=1 "Michael Diosi (page does not exist)"), [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") & [Alexander Schmidt](index.php?title=Alexander_Schmidt&action=edit&redlink=1 "Alexander Schmidt (page does not exist)"), December 20, 2005, hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
35. <a id="cite-ref-35" href="#cite-note-35">↑</a> [Official statement on [Deleted](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=12995)?] by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 21, 2009
36. <a id="cite-ref-36" href="#cite-note-36">↑</a> [I'm in doubt if RobboLito is a clone](http://www.talkchess.com/forum/viewtopic.php?t=30296) by [Volker Pittlik](index.php?title=Volker_Pittlik&action=edit&redlink=1 "Volker Pittlik (page does not exist)"), [CCC](CCC "CCC"), October 24, 2009
37. <a id="cite-ref-37" href="#cite-note-37">↑</a> [Fabien's open letter to the community](http://www.talkchess.com/forum/viewtopic.php?t=37762) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), January 23, 2011
38. <a id="cite-ref-38" href="#cite-note-38">↑</a> [Fabien's open letter to the community](http://www.open-chess.org/viewtopic.php?f=3&t=1014) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 23, 2011
39. <a id="cite-ref-39" href="#cite-note-39">↑</a> [The Chess Mind Blog - More Computer Chess Controversy](http://www.thechessmind.net/blog/2011/1/24/more-computer-chess-controversy.html)
40. <a id="cite-ref-40" href="#cite-note-40">↑</a> [Attack of the clones | ChessVibes](https://web.archive.org/web/20180828211326/http://www.chessvibes.com/?q=reports/attack-of-the-clones) by [David Levy](David_Levy "David Levy"), February 19, 2011 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
41. <a id="cite-ref-41" href="#cite-note-41">↑</a> [In retrospect](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22421) by [Rebel](Ed_Schroder "Ed Schroder"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 14, 2011
42. <a id="cite-ref-42" href="#cite-note-42">↑</a> [Apology to Vas](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22679) by [Rebel](Ed_Schroder "Ed Schroder"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 17, 2011
43. <a id="cite-ref-43" href="#cite-note-43">↑</a> [ICGA Investigations Wiki](index.php?title=Icga/home&action=edit&redlink=1 "Icga/home (page does not exist)")
44. <a id="cite-ref-44" href="#cite-note-44">↑</a> [Open letter to the ICGA about the Rybka-Fruit issue](http://www.hiarcs.net/forums/viewtopic.php?t=4038) by [Harvey Williamson](Harvey_Williamson "Harvey Williamson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), March 01, 2011
45. <a id="cite-ref-45" href="#cite-note-45">↑</a> [Programmers Open Letter to ICGA on Rybka/Fruit](http://www.open-chess.org/viewtopic.php?f=3&t=1175) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 01, 2011
46. <a id="cite-ref-46" href="#cite-note-46">↑</a> [Plagiatsvorwurf gegen Computerschach-Weltmeister](http://www.heise.de/newsticker/meldung/Plagiatsvorwurf-gegen-Computerschach-Weltmeister-1200222.html), [Heise online](http://de.wikipedia.org/wiki/Heise_online), March 01, 2011 (German)
47. <a id="cite-ref-47" href="#cite-note-47">↑</a> [Schach-Software Rybka - Programmierer vermuten Intelligenzklau](http://www.spiegel.de/netzwelt/gadgets/0,1518,748616,00.html) by [Frank Patalong](http://www.spiegel.de/extra/0,1518,632080,00.html), [Spiegel Online](https://en.wikipedia.org/wiki/Der_Spiegel#Spiegel_Online), March 03, 2011 (German)
48. <a id="cite-ref-48" href="#cite-note-48">↑</a> RYBKA 1.6.1 in [Chess War V-VII](http://www.open-aurec.com/chesswar/Chesswar006/Chesswar006DSt.htm)
49. <a id="cite-ref-49" href="#cite-note-49">↑</a> [Re: Programmers Open Letter to ICGA on Rybka/Fruit](http://www.open-chess.org/viewtopic.php?f=3&t=1175&start=160#p11099) by [Olivier Deville](Olivier_Deville "Olivier Deville"), [Openchess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 05, 2011
50. <a id="cite-ref-50" href="#cite-note-50">↑</a> [Le Fou numérique - Le Système du Suisse 3 - T](http://americanfoot.free.fr/echecs/suisse/sui/sui3top200.htm)
51. <a id="cite-ref-51" href="#cite-note-51">↑</a> [Re: Programmers Open Letter to ICGA on Rybka/Fruit](http://www.open-chess.org/viewtopic.php?f=3&t=1175&start=140#p11066) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 05, 2011
52. <a id="cite-ref-52" href="#cite-note-52">↑</a> [Re: Programmers Open Letter to ICGA on Rybka/Fruit](http://www.open-chess.org/viewtopic.php?f=3&t=1175&start=160#p11081) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Openchess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 05, 2011
53. <a id="cite-ref-53" href="#cite-note-53">↑</a> [Rybka 1.6.1](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=21216) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), March 13, 2011
54. <a id="cite-ref-54" href="#cite-note-54">↑</a> [Re: Programmers Open Letter to ICGA on Rybka/Fruit](http://www.open-chess.org/viewtopic.php?f=3&t=1175&start=120#p10994) by[BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 04, 2011
55. <a id="cite-ref-55" href="#cite-note-55">↑</a> [Re: Correction: List and ElChinito as Crafty clones, ... etc](https://www.stmintz.com/ccc/index.php?id=383344) by [Paul H](index.php?title=Paul_H&action=edit&redlink=1 "Paul H (page does not exist)"), [CCC](CCC "CCC"), August 21, 2004
56. <a id="cite-ref-56" href="#cite-note-56">↑</a> [Open letter by Eugenio Castillo (ELChinito team) ...](https://www.stmintz.com/ccc/index.php?id=384790) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), August 28, 2004
57. <a id="cite-ref-57" href="#cite-note-57">↑</a> [Rybka disqualified and banned from World Computer Chess Championships | ChessVibes](https://web.archive.org/web/20160419082204/http://www.chessvibes.com/?q=reports/rybka-disqualified-and-banned-from-world-computer-chess-championships) by [Peter Doggers](Peter_Doggers "Peter Doggers"), June 29, 2011 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
58. <a id="cite-ref-58" href="#cite-note-58">↑</a> [Rybka and the ICGA](http://www.computerschaak.nl/index.php?option=com_content&view=article&id=514%3Arybka-en-de-icga&catid=18%3Avereniging&Itemid=28&lang=en), [CSVN Computerschaak](http://www.csvn.nl/)
59. <a id="cite-ref-59" href="#cite-note-59">↑</a> [BB's Rybka/Ippolit comparison](http://www.open-chess.org/viewtopic.php?f=3&t=119) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 13, 2010
60. <a id="cite-ref-60" href="#cite-note-60">↑</a> [Feb 12 version: Rybka 1.0 Beta / Fruit 2.1 document](http://www.open-chess.org/viewtopic.php?f=5&t=1104) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 12, 2011
61. <a id="cite-ref-61" href="#cite-note-61">↑</a> [Rybka evidence recapitulation](http://www.open-chess.org/viewtopic.php?f=5&t=1772) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2012
62. <a id="cite-ref-62" href="#cite-note-62">↑</a> Part 1 covers [Houdini](Houdini "Houdini"), Rybka, [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish"), [Critter](Critter "Critter"), [Naum](Naum "Naum"), [Chiron](Chiron "Chiron") and [Spike](Spike "Spike")
63. <a id="cite-ref-63" href="#cite-note-63">↑</a> [A Pairwise Comparison of Chess Engine Move Selections](http://www.top-5000.nl/clone.htm) by [Adam Hair](Adam_Hair "Adam Hair"), hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
64. <a id="cite-ref-64" href="#cite-note-64">↑</a> quoted with the kind permission of [Chrilly](Chrilly_Donninger "Chrilly Donninger") and [Enir](Enrique_Irazoqui "Enrique Irazoqui") » [Hydra](Hydra "Hydra")
65. <a id="cite-ref-65" href="#cite-note-65">↑</a> [Anthony Cozzie speaks about Rybka source code](http://www.stevelim.com/blog/?p=470) from [Steve Lim / SuperSteve3d - Home](http://www.stevelim.com/), February 04, 2008
66. <a id="cite-ref-66" href="#cite-note-66">↑</a> [Why did the ICGA ignore this advice?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22337) by [John Sidles](index.php?title=John_Sidles&action=edit&redlink=1 "John Sidles (page does not exist)"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 06, 2011
67. <a id="cite-ref-67" href="#cite-note-67">↑</a> [Re: A Big Thanks and a Small Update](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=23957;pg=5) by [John Sidles](index.php?title=John_Sidles&action=edit&redlink=1 "John Sidles (page does not exist)"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January, 08, 2012
68. <a id="cite-ref-68" href="#cite-note-68">↑</a> [Voir dire from Wikipedia](https://en.wikipedia.org/wiki/Voir_dire)
69. <a id="cite-ref-69" href="#cite-note-69">↑</a> [Fruit 2.1 and Rybka 1.0 Beta 1.0 decompiled source code](http://www.top-5000.nl/sourcecode.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder")
70. <a id="cite-ref-70" href="#cite-note-70">↑</a> [ChessBase: A Gross Miscarriage of Justice in Computer Chess](http://www.open-chess.org/viewtopic.php?f=3&t=1771) by [kingliveson](Franklin_Titus "Franklin Titus"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 02, 2012
71. <a id="cite-ref-71" href="#cite-note-71">↑</a> [Re: ChessBase: A Gross Miscarriage of Justice in Computer Chess](http://www.open-chess.org/viewtopic.php?f=3&t=1771#p15455) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 02, 2012
72. <a id="cite-ref-72" href="#cite-note-72">↑</a> [Re: Hyatt Is Gone!](http://www.open-chess.org/viewtopic.php?f=3&t=1763&p=15497#p15459) by [BB+](Mark_Watkins "Mark Watkins") [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), Jan 03, 2012
73. <a id="cite-ref-73" href="#cite-note-73">↑</a> [Rybka evidence recapitulation](http://www.open-chess.org/viewtopic.php?f=5&t=1772) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2012
74. <a id="cite-ref-74" href="#cite-note-74">↑</a> [Søren Riis](S%C3%B8ren_Riis "Søren Riis") (**2012**). *A Gross Miscarriage of Justice in Computer Chess*. [pdf](http://www.chessbase.com/news/2011/riis01.pdf) hosted by [ChessBase](ChessBase "ChessBase")

**[Up one Level](Engines "Engines")**







 
