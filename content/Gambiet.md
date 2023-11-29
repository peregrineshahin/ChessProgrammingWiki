---
title: Gambiet
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Gambiet**

[](http://www.necoma.nl/chess.html) Gambiet 80 cover <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Gambiet**,

a chess program by [Wim Rens](Wim_Rens "Wim Rens"), initially written in [Z80](Z80 "Z80") [assembly](Assembly "Assembly") to run on a [TRS-80](TRS-80 "TRS-80") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and the first Dutch commercial chess program, merchandised through [Microtrend](Microtrend "Microtrend") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Gambiet **80** played the first [WMCCC 1980](WMCCC_1980 "WMCCC 1980") in [London](https://en.wikipedia.org/wiki/London), where it finished third with 3/5, and further the [European MCC 1981](European_MCC_1981 "European MCC 1981") and [European MCC 1982](European_MCC_1982 "European MCC 1982") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and the first three [Dutch Computer Chess Championships](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"). Gambiet **81** was runner-up behind [YNCT 1.0](YNCT "YNCT") at the [DOCCC 1981](DOCCC_1981 "DOCCC 1981"), and Gambiet **82** did even better, winning the [DOCCC 1982](DOCCC_1982 "DOCCC 1982") <a id="cite-note-5" href="#cite-ref-5">[5]</a> running on a [Xerox Star](https://en.wikipedia.org/wiki/Xerox_Star). Gambiet **83** played the [DOCCC 1983](DOCCC_1983 "DOCCC 1983") with a fifth place.

Gambiet was base of [Microtrend Experimental](Microtrend_Experimental "Microtrend Experimental"), which also played the [European MCC 1981](European_MCC_1981 "European MCC 1981") with its brother, and was further commercialized in 1982 for the [Philips](https://en.wikipedia.org/wiki/Philips) [Videopac G7000](https://en.wikipedia.org/wiki/Magnavox_Odyssey%C2%B2) [video game console](https://en.wikipedia.org/wiki/Video_game_console), as [Videopac C 7010](Videopac_C_7010 "Videopac C 7010") chess module <a id="cite-note-6" href="#cite-ref-6">[6]</a> with its own Z80-compatible *NSC800* [CMOS](https://en.wikipedia.org/wiki/CMOS) microprocessor <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Description

Gambiet is a [Shannon Type-A Stategy](Type_A_Strategy "Type A Strategy") program, performing [alpha-beta](Alpha-Beta "Alpha-Beta") with a classical [mailbox](Mailbox "Mailbox") board representation and following [byte-wise](Byte "Byte") [piece coding](Pieces#PieceCoding "Pieces") optimized for efficiency <a id="cite-note-8" href="#cite-ref-8">[8]</a> :

```C++
        7654 3210
king    x110 1111
queen   x000 1001
rook    x000 0101
bishop  x000 0011
knight  x011 0011
pawn    x001 0001
border  1100 0000
empty   0000 0000

```

[MSB](https://en.wikipedia.org/wiki/Most_significant_bit), [bit](Bit "Bit") 7 is the piece color, x = 0 for white and x = 1 for black pieces. While [LSB](https://en.wikipedia.org/wiki/Least_significant_bit), bit 0, acts as piece indicator - set for any piece, the lower [nibble](Nibble "Nibble") already contains their [point value](Point_Value "Point Value") equivalence in a {1,3,3,5,9,15} solution, luckily all values odd. The bits 1 to 4 (or even 0 to 4) may act as table index for [move generation](Move_Generation "Move Generation") purpose, similar, bit 4 and 5 enumerate to the four possibly useful states of {[sliding piece](Sliding_Pieces "Sliding Pieces"), [pawn](Pawn "Pawn"), [king](King "King"), [knight](Knight "Knight")}. However, the leading code saving trick in conjunction with bit 6 after loading the code into the [accumulator](https://en.wikipedia.org/wiki/Accumulator_%28computing%29) and shifting it left one (SLA) , is to use disjoint [Z80](Z80 "Z80") [processor flags](https://en.wikipedia.org/wiki/Flag_%28computing%29) <a id="cite-note-9" href="#cite-ref-9">[9]</a> with four [conditional jumps](https://en.wikipedia.org/wiki/Conditional_jump) in the right order for up to five cases to distinguish. [Zero flag](https://en.wikipedia.org/wiki/Zero_flag) is set for empty squares, [parity](https://en.wikipedia.org/wiki/Parity_flag) (odd) for squares off the board, [sign flag](https://en.wikipedia.org/wiki/Sign_flag) in case of a king, [carry](https://en.wikipedia.org/wiki/Carry_flag) for black pieces and white pieces otherwise.

```C++
LDA  A,(SQUARE)    ; get piece code to Accu (A)
SLA  A             ; A := A << 1
JP   Z, EMPTY      ; if ( A == 0 ) empty square 
JP   PO, OFFBOARD  ; else if ( parity(A) is odd ) off the board
JP   M, KING       ; else if ( A < 0 ) occupied by king
JP   C, BLACK      ; else if ( carry ) occupied by black piece
JP   WHITE         ; else occupied by white piece

```

## How it began

[Wim Rens](Wim_Rens "Wim Rens") in his June 1981 Databus article *Grondslagen van computerschaak* on how it began with [Microtrend](Microtrend "Microtrend") and Gambiet <a id="cite-note-10" href="#cite-ref-10">[10]</a>:

```C++
The second milestone of Gambiet's triumph <a id="cite-note-11" href="#cite-ref-11">[11]</a> was achieved under the watchful eye of the firm Microtrend. At home of one of their directors were two [TSR-80's](TRS-80 "TRS-80"), one running [Sargon II](Sargon "Sargon"), the other Gabmol <a id="cite-note-12" href="#cite-ref-12">[12]</a>. Microtrend was looking for a chess game in their collection, and end of June a decision was made and a contract placed. The result was impressive: two equally fast Tandy computers and Gambiet had no trouble with the once-famous Sargon. 

```

## Microtrend

According to [Trademarkia](https://en.wikipedia.org/wiki/Trademarkia), GAMBIET was trademark by [Microtrend International B.V.](Microtrend "Microtrend") in [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam), filed October 26, 1981, as [United States trademark](https://en.wikipedia.org/wiki/United_States_trademark_law), canceled September 13, 1989 <a id="cite-note-13" href="#cite-ref-13">[13]</a>.

[](http://books.google.com/books?id=Cz4EAAAAMBAJ&pg=PA11&lpg=PA11&source=bl&ots=NNPeGit1RW&sig=OJkQ8pLSOju5EpW1DBOGPrfQXlI&hl=en&sa=X&ei=X9B0T-WTJofesgacma29DQ&sqi=2&redir_esc=y#v=onepage&q&f=false)
Gambiet order form by [Microtrend](Microtrend "Microtrend"), U.S.A., [InfoWorld](https://en.wikipedia.org/wiki/InfoWorld), May 1981 <a id="cite-note-14" href="#cite-ref-14">[14]</a>

## Selected Games

## WMCCC 1980

[WMCCC 1980](WMCCC_1980 "WMCCC 1980"), round 3, Gambiet 80 - [Sargon 2.5 Auto RB](Sargon "Sargon") <a id="cite-note-15" href="#cite-ref-15">[15]</a>

```

[Event "WMCCC 1980"]
[Site "London, United Kingdom"]
[Date "1980.09.05"]
[Round "3"]
[White "Gambiet 80"]
[Black "Sargon 2.5 Auto RB"]
[Result "1-0"]

1.e4 c5 2.Nf3 d6 3.Bb5+ Bd7 4.a4 Bxb5 5.axb5 Nf6 6.Nc3 Nbd7 7.O-O e5 8.d3 Be7 
9.Be3 O-O 10.Qc1 Nb6 11.Kh1 Qd7 12.Bg5 Qe6 13.Rd1 Ng4 14.Be3 Rfc8 15.b3 d5 
16.exd5 Qd7 17.d6 Bxd6 18.h4 Qe6 19.h5 Nf6 20.h6 Nbd5 21.Nxd5 Nxd5 22.hxg7 Nc3 
23.Re1 Kxg7 24.Bd2 Nxb5 25.Bf4 f6 26.Bd2 Bf8 27.c4 Nd4 28.Bh6+ Kg6 29.Nxd4 cxd4 
30.Bxf8 Rxf8 31.Kh2 Qb6 32.Qd1 h5 33.Kh3 Rac8 34.Kg3 Kg5 35.Qd2+ Kf5 36.Kh2 Rg8 
37.b4 a6 38.c5 Qb5 39.Kh3 b6 40.cxb6 Rc3 41.Qa2 Rxd3+ 42.g3 Rb8 43.Qxa6 Rxb6 
44.Qc8+ Kg5 45.Qc1+ Kg6 46.Rb1 Rc3 47.Qd1 Rc4 48.g4 hxg4+ 49.Qxg4+ Kf7 50.Qf5 Rxb4 
51.Rxb4 Qxb4 52.Rxe5 Qc3+ 53.f3 d3 54.Qd7+ Kg6 55.Rd5 Rb3 56.Qe8+ Kg7 57.Qe7+ Kg6 
58.Qe4+ Kg7 59.Rd7+ Kh6 60.Rh7+ Kg5 61.f4# 1-0 

```

## DOCCC 1982

[DOCCC 1982](DOCCC_1982 "DOCCC 1982"), round 8, upcoming tournament winner Gambiet 82 loses from newcomer [Rebel](Rebel "Rebel") <a id="cite-note-16" href="#cite-ref-16">[16]</a>

```

[Event "DOCCC 1982"]
[Site "Wageningen NED"]
[Date "1982.10.??"]
[Round "8"]
[White "Gambiet 82"]
[Black "Rebel"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 
10.Bc2 c5 11.d4 Qc7 12.Nbd2 Bd7 13.d5 Rfc8 14.Qe2 Rab8 15.b3 Qb6 16.Qe3 Ra8 17.Bb2 Rc7 
18.Bd3 Nh5 19.Bf1 Nf4 20.c4 Rb7 21.cxb5 Bxb5 22.Rac1 Bxf1 23.Kxf1 Qb5+ 24.Nc4 h6 
25.Qc3 Nxc4 26.Qxc4 Nd3 27.Re2 Nxc1 28.Qxc1 Qd3 29.Ne1 Qb5 30.Qe3 Bg5 31.Qc3 Rbb8
32.Nd3 Qe8 33.Rc2 f6 34.a4 Qg6 35.Qc4 Rb7 36.b4 cxb4 37.Nxb4 Qh5 38.Re2 a5 39.Nd3 Qf7 
40.Qc6 Qd7 41.Rc2 Rab8 42.Qc4 Rb3 43.Kg1 g6 44.Kh1 f5 45.Kg1 fxe4 46.Qxe4 Qf5 
47.Qxf5 gxf5 48.Nxe5 Rxb2 49.Rxb2 Rxb2 50.Nc6 Kf7 51.g3 Kf6 52.f4 Rb1+ 53.Kf2 Bxf4 
54.gxf4 Ra1 55.Ke3 Rxa4 56.h4 h5 57.Nd4 Ra1 58.Nb5 Rd1 59.Nxd6 Rxd5 60.Nc4 a4 
61.Nb6 Ra5 62.Nc4 Rc5 63.Kd4 Rc8 64.Kd3 0-1

```

## See also

- [Gambit](index.php?title=Gambit&action=edit&redlink=1 "Gambit (page does not exist)")
- [GambitVB](GambitVB "GambitVB")
- [Kasparov's Gambit](Kasparov%27s_Gambit "Kasparov's Gambit")
- [Microtrend](Microtrend "Microtrend")
- [Microtrend Experimental](Microtrend_Experimental "Microtrend Experimental")
- [Videopac C 7010](Videopac_C_7010 "Videopac C 7010")

## Publications

- [Wim Rens](Wim_Rens "Wim Rens") (**1981**). *Grondslagen van computerschaak*. [Databus](http://home.kpn.nl/a.dikker1/museum/databus.html) 06-81, pp. 13-15, [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/06-1981,%20Databus,%20Wim%20Rens,%20Grondslagen%20van%20computerschaak.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis") (Dutch)
- [John F. White](John_F._White "John F. White") (**1982**). *[Review-Chess Computers - Software packages](http://yourcomputeronline.wordpress.com/2011/01/31/review-chess-computers/)*. [Your Computer](Your_Computer "Your Computer"), [March 1982](http://yourcomputeronline.wordpress.com/2011/01/30/march-1982-contents-and-editorial/)
- [Peter van Grijfland](http://www.necoma.nl/) (**1982**). *Gambiet-82 Kampion van Nederland - Gambiet afgeslacht*. [Hoogeveen](http://www.schaakclub-hoogeveen.nl/), p. 16-18, [pdf](http://schaakclub-hoogeveen.nl/archief/aanzet/aanzet_okt1982.pdf) (Dutch)

## External Links

- [Gambiet's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=462)
- [GambitVB Chess - History](http://gambitvb.info/History.aspx) by [Willem Rens](Wim_Rens "Wim Rens")
- [Free Game Downloads|Tandy-Radio-Shack|TRS-80-Model-III ROMs](http://www.theoldcomputer.com/roms/index.php?folder=Tandy-Radio-Shack/TRS-80-Model-III/Various/g)
- [Gambiet from Wikipedia.nl](http://nl.wikipedia.org/wiki/Gambiet) (Dutch)
- [Gambit from Wikipedia](https://en.wikipedia.org/wiki/Gambit)
- [The United Jazz + Rock Ensemble](Category:The_United_Jazz_%2B_Rock_Ensemble "Category:The United Jazz + Rock Ensemble") - Circus Gambet, [Donauinsel](https://en.wikipedia.org/wiki/Donauinsel), [Vienna](https://en.wikipedia.org/wiki/Vienna), Austria, June 22, 1991, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Dave King](<https://de.wikipedia.org/wiki/Dave_King_(Bassist)>), [Jon Hiseman](Category:Jon_Hiseman "Category:Jon Hiseman"), [Barbara Thompson](Category:Barbara_Thompson "Category:Barbara Thompson"), [Volker Kriegel](Category:Volker_Kriegel "Category:Volker Kriegel"), [Wolfgang Dauner](Category:Wolfgang_Dauner "Category:Wolfgang Dauner"),

[Charlie Mariano](Category:Charlie_Mariano "Category:Charlie Mariano"), [Albert Mangelsdorff](Category:Albert_Mangelsdorff "Category:Albert Mangelsdorff"), [Ian Carr](Category:Ian_Carr "Category:Ian Carr"), [Ack van Rooyen](https://en.wikipedia.org/wiki/Ack_van_Rooyen), [Kenny Wheeler](https://en.wikipedia.org/wiki/Kenny_Wheeler)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Gambiet 80 cover from [Computerschaak](http://www.necoma.nl/chess.html) by [Peter van Grijfland](http://www.necoma.nl/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Eerste Nederlands Kampioenschappen Computerschaken](http://www.csvnsupplementsite.nl/csvnp2.html) (Dutch)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [GAMBIET - Reviews & Brand Information - Microtrend International B.V. Amsterdam , Serial Number: 73334547](http://www.trademarkia.com/gambiet-73334547.html) by [Trademarkia](https://en.wikipedia.org/wiki/Trademarkia)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Tony Harrington](Tony_Harrington "Tony Harrington") (**1983**). *[The third European Microcomputer Chess tournament](http://www.atarimagazines.com/creative/v9n1/123_The_third_European_Microc.php)*. [Creative Computing](Creative_Computing "Creative Computing"), Vol. 9, No. 1
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Gambiet '82, de nieuwe Nederlandse computerschaak kampioen! - Nieuwe pagina 1](http://www.csvnsupplementsite.nl/CSVNPAGINA1.html), [CSVN](CSVN "CSVN") supplement site
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Philips](https://en.wikipedia.org/wiki/Philips), [Videopac C 7010](Videopac_C_7010 "Videopac C 7010"), French Manual, [pdf](http://www.6502man.com/tempo/VIDEOPAC%20CHESS%20%20C7010.pdf)

© 1982 [N.V. Philips Gloeilampenfabrieken](https://en.wikipedia.org/wiki/Philips#History) - Holland

© 1982 [Wim Rens](Wim_Rens "Wim Rens"), [Microtrend International](Microtrend "Microtrend") - Holland
7\. <a id="cite-ref-7" href="#cite-note-7">↑</a> [National Semiconductor NSC800](http://www.cpu-world.com/CPUs/NSC800/index.html) from [CPU-World: Microprocessor news, benchmarks, information and pictures](http://www.cpu-world.com/index.html)
8\. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Wim Rens](Wim_Rens "Wim Rens") (**1981**). *Grondslagen van computerschaak*. [Databus](http://home.kpn.nl/a.dikker1/museum/databus.html) 06-81, pp. 13-15, [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/06-1981,%20Databus,%20Wim%20Rens,%20Grondslagen%20van%20computerschaak.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis")
9\. <a id="cite-ref-9" href="#cite-note-9">↑</a> same flags as [8080](8080 "8080"), and even [8086](8086 "8086"), [x86](X86 "X86") and [x86-64](X86-64 "X86-64") with [parity](https://en.wikipedia.org/wiki/Parity_flag) for the least significant byte
10\. <a id="cite-ref-10" href="#cite-note-10">↑</a> Free translation from Dutch, excerpt from: [Wim Rens](Wim_Rens "Wim Rens") (**1981**). *Grondslagen van computerschaak*. [Databus](http://home.kpn.nl/a.dikker1/museum/databus.html) 06-81, pp. 13-15, [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/06-1981,%20Databus,%20Wim%20Rens,%20Grondslagen%20van%20computerschaak.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis") (Dutch)
11\. <a id="cite-ref-11" href="#cite-note-11">↑</a> first milestone was winning a match from [IGM](IGM "IGM") in early 1980
12\. <a id="cite-ref-12" href="#cite-note-12">↑</a> Gabmol was Gambiet's initial name
13\. <a id="cite-ref-13" href="#cite-note-13">↑</a> [GAMBIET - Reviews & Brand Information - Microtrend International B.V. Amsterdam , Serial Number: 73334547](http://www.trademarkia.com/gambiet-73334547.html)
14\. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Gambiet order form](http://books.google.com/books?id=Cz4EAAAAMBAJ&pg=PA11&lpg=PA11&source=bl&ots=NNPeGit1RW&sig=OJkQ8pLSOju5EpW1DBOGPrfQXlI&hl=en&sa=X&ei=X9B0T-WTJofesgacma29DQ&sqi=2&redir_esc=y#v=onepage&q&f=false), [InfoWorld](https://en.wikipedia.org/wiki/InfoWorld), Vol. 3, No. 9, May 11, 1981, from [Google Books](https://en.wikipedia.org/wiki/Google_Books)
15\. <a id="cite-ref-15" href="#cite-note-15">↑</a> [London 1980 - Chess - Round 3 - Game 4 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=13&round=3&id=4)
16\. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Downloads | Open Dutch Computer Chess Championships | Games](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=37&Itemid=26&lang=en&limitstart=30)

**[Up one level](Engines "Engines")**

