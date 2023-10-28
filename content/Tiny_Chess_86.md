---
title: Tiny Chess 86
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Tiny Chess 86**



 [](https://en.wikipedia.org/wiki/File:MYSTEM_86.JPG) Intel SDK-86 <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Tiny Chess 86** (TC86),  

a chess program by [Jan Kuipers](Jan_Kuipers "Jan Kuipers") written in [8086](8086 "8086") [assembly](Assembly "Assembly"). Tiny Chess 86 played the [Second PCW Microcomputer Chess Championship](PCW-MCC_1979 "PCW-MCC 1979") 1979 in [London](https://en.wikipedia.org/wiki/London) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, where it ran on an [Intel](Intel "Intel") [SDK-86](https://en.wikipedia.org/wiki/Intel_System_Development_Kit#SDK-86) <a id="cite-note-3" href="#cite-ref-3">[3]</a> with the program in a 4 KB [EPROM](Memory#ROM "Memory") only taking 1 KB of [RAM](Memory#RAM "Memory"), and became tied third. A slightly modified version was used by [Murray Lane](index.php?title=Murray_Lane&action=edit&redlink=1 "Murray Lane (page does not exist)") to play the [Microcomputer-Chess Tournament 1980](MCC_1980 "MCC 1980") in [San Jose, California](https://en.wikipedia.org/wiki/San_Jose,_California), which was the most powerful unit there, but finished last also due to the weak [evaluation](Evaluation "Evaluation") only based on [material](Material "Material") - causing weak random [opening](Opening "Opening") play <a id="cite-note-4" href="#cite-ref-4">[4]</a>. At the first [DOCCC 1981](DOCCC_1981 "DOCCC 1981") it ran on an [Elektuur](https://en.wikipedia.org/wiki/Elektor) processor board with an 8088 CPU <a id="cite-note-5" href="#cite-ref-5">[5]</a>. A special version of TC86 dubbed "Intellect" was published in Elektuur March 81. 



### Contents


* [1 Move Generation](#move-generation)
* [2 Selected Games](#selected-games)
* [3 Publications](#publications)
* [4 External Links](#external-links)
* [5 References](#references)






TC86 applies [alpha-beta](Alpha-Beta "Alpha-Beta") and performs [move generation](Move_Generation "Move Generation") using a [0x88](0x88 "0x88") board representation, as shown in the listing, published in a June 1981 *Databus* article <a id="cite-note-6" href="#cite-ref-6">[6]</a>:




```

                  104            ;ROUTINE TO GENERATE ALL LEGAL MOVES
                  105            ;FOR KNIGHT OR KING
                  106
062F 8BFB         107    GETDES: MOV    DI,BX           ;DST=ORG
0631 2EBA14       108            MOV    DL,CS:[SI]      ;GET DIRECTION
0634 03FA         109            ADD    DI,DX           ;CALC. SQ. MOVING TO
0636 F7C78800     110            TEST   DI,88H          ;OFF BOARD?
063A 750C         111            JNZ    G4              ;YES
063C 81E77706     112            AND    DI,677H         ;NO, CLEAN UP DI
0640 803D00       113            CMP    BYTE PTR [DI],COL       ;WHAT IS ON THAT
0643 7F03         114            JNLE   G4              ;OCCUPIED BY MYSELF
0645 E89700       115            CALL   MOVPOS          ;EMPTY OR OPPONENT
0648 46           116    G4:     INC    SI              ;NEXT DIRECTION
0649 2EF60499     117            TEST   BYTE PTR CS:[SI],99H    ; END OF TABLE?
064D 75E0         118            JNZ    GETDES          ;NOT YET
064F EBAE         119            JMP    M3              ;YES, STOP IT
                  120
                  121            ;ROUTINE TO GENERATE ALL LEGAL MOVES FOR PIECES
                  122            ;MOVING ALONG A LINE:BISHOP,ROOK AND QUEEN
                  123
0651 8BFB         124    PATH:   MOV    DI,BX           ;DST=SRC
0653 2E8A14       125            MOV    DL,CS:[SI]      ;GET DIRECTION
0656 03FA         126    S2:     ADD    DI,DX           ;NEXT SQ. IN THAT DIRECTION
0658 F7C78800     127            TEST   DI,88H          ;OFF BOARD?
065C 7511         128            JNZ    S3              ;YES
065E 81E77706     129            AND    DI,677H         ;NO, CLEAN UP DI
0662 803D00       130            CMP    BYTE PTR [DI],COL       ;WHAT IS THERE?
0665 7F03         131            JG     S4              ;OCCUPIED BY MYSELF
0667 E89700       132            CALL   MOVPOS          ;EMPTY OR OPPONENT
066A 803D00       133    S4:     CMP    BYTE PTR [DI],0 ;IF IT WAS EMPTY,
066D 74E7         134            JNZ    S2              ;CONTINUE THAT DIRECTION
066F 46           135    S3:     INC    SI              ;GET NEXT DIRECTION
0670 2EF60499     136            TEST   BYTE PTR CS:[SI],99H ;ALL DIRECTIONS DONE?
0674 75DB         137            JNZ    PATH            ;NO, CONTINUE
0676 EB87         138    S1:     JMP    M3              ;YES, STOP IT

```

## Selected Games


[MCC 1980](MCC_1980 "MCC 1980"), round 1, [Lane's](index.php?title=Murray_Lane&action=edit&redlink=1 "Murray Lane (page does not exist)") Tiny Chess 86 vs. [Boris 2.5](Boris#2.5 "Boris") <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "Microcomputer Chess Championship 1980"]
[Site " San Jose, CA"]
[Date "1980.09.05"]
[Round "1"]
[White "Lane's Tiny Chess 86"]
[Black "Boris 2.5"]
[Result "0-1"]

1.a3 Nc6 2.h4 Nf6 3.g3 d5 4.Bh3 Bg4 5.Nf3 Bxh3 6.Rxh3 e5 7.b3 e4 8.Nh2 Qd7 9.g4 
Nxg4 10.Nxg4 Qxg4 11.Rh1 Qg2 12.Rf1 Qh3 13.Nc3 O-O-O 14.d3 Qxh4 15.dxe4 d4 16.Nb5 
a6 17.Nxd4 Rxd4 18.Bd2 Bd6 19.Rg1 Bf4 20.e3 Bxe3 21.Qg4+ Qxg4 22.Rxg4 Bxd2+ 23.Ke2 
Bc3 24.Ra2 f5 25.Rxg7 Rxe4+ 26.Kf3 Bxg7 27.a4 Nb4 28.Ra3 Bb2 29.c3 Bxa3 30.cxb4 Rxb4 
31.a5 Rxb3+ 32.Kf4 Rb5 33.f3 Bc1+ 34.Kg3 Rxa5 35.Kh4 Bf4 36.Kh3 Ra2 0-1

```

## Publications


* Editor (**1980**). *A Chess Program & Random Openings*. [Personal Computing, Vol. 4, No. 12](Personal_Computing#4_12 "Personal Computing"), pp. 75 » [Murray Lane](index.php?title=Murray_Lane&action=edit&redlink=1 "Murray Lane (page does not exist)")
* [Jan Kuipers](Jan_Kuipers "Jan Kuipers") (**1981**). *Tiny Chess 86 - Een schaakprogramma voor de 8088/8086*. [Databus](http://home.kpn.nl/a.dikker1/museum/databus.html) 06-81, [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/06-1981,%20Databus,%20Jan%20Kuipers,%20Tiny%20Chess%2086.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis")


## External Links


* [World's smallest Handmade Chess Set ever](http://thelongestlistofthelongeststuffatthelongestdomainnameatlonglast.com/smallest146.html), November 18, 2006
* [Tiny chess set built between heartbeats](http://arbroath.blogspot.de/2008/05/tiny-chess-set-built-between-heartbeats.html), May 01, 2008
* [Fidelity Tiny Chess (1991)](http://www.spacious-mind.com/html/tiny.html) by [Eric van Riet Paap](Eric_van_Riet_Paap "Eric van Riet Paap"), from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
* [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa") - [City of Tiny Lites](http://globalia.net/donlope/fz/songs/City_Of_Tiny_Lites.html), 1979, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa"), [Adrian Belew](Category:Adrian_Belew "Category:Adrian Belew"), [Tommy Mars](https://en.wikipedia.org/wiki/Tommy_Mars), [Peter Wolf](https://en.wikipedia.org/wiki/Peter_Wolf_%28producer%29), [Patrick O'Hearn](https://en.wikipedia.org/wiki/Patrick_O%27Hearn), [Terry Bozzio](Category:Terry_Bozzio "Category:Terry Bozzio"), [Ed Mann](https://en.wikipedia.org/wiki/Ed_Mann)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Image](https://en.wikipedia.org/wiki/File:MYSTEM_86.JPG) of [Intel](Intel "Intel") [SDK-86](https://en.wikipedia.org/wiki/Intel_System_Development_Kit#SDK-86) from [Wikipedia](https://en.wikipedia.org/wiki/Home)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1979**). *Second Annual European Microcomputer Chess Championship - Results and Authors*. [ICCA Newsletter, Vol. 2, No. 2](ICGA_Journal#2_2 "ICGA Journal")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Prehistorie van het Nederlandse Computerschaak](http://old.csvn.nl/pre_hist.html) (Dutch)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Editor (**1980**). *A Chess Program & Random Openings*. [Personal Computing, Vol. 4, No. 12](Personal_Computing#4_12 "Personal Computing"), pp. 75
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Eerste Nederlands Kampioenschappen Computerschaken](http://www.csvnsupplementsite.nl/csvnp2.html) (Dutch)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Jan Kuipers](Jan_Kuipers "Jan Kuipers") (**1981**). *Tiny Chess 86 - Een schaakprogramma voor de 8088/8086*. [Databus](http://home.kpn.nl/a.dikker1/museum/databus.html) 06-81, [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/06-1981,%20Databus,%20Jan%20Kuipers,%20Tiny%20Chess%2086.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> Editor (**1980**). *A Chess Program & Random Openings*. [Personal Computing, Vol. 4, No. 12](Personal_Computing#4_12 "Personal Computing"), pp. 75

**[Up one level](Engines "Engines")**







 
