---
title: Bebe
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bebe**

[](Linda_Scherzer "Linda Scherzer") [Linda Scherzer](Linda_Scherzer "Linda Scherzer") and Bebe <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Bebe**, (Be-Be)

a chess program running on a customized, special purpose [bit slice](https://en.wikipedia.org/wiki/Bit_slicing) [hardware](Hardware "Hardware") developed by [Tony](Tony_Scherzer "Tony Scherzer") and [Linda Scherzer](Linda_Scherzer "Linda Scherzer") as [testbed](https://en.wikipedia.org/wiki/Testbed) for their company's *SYS-10, Inc.* mini- and mainframe processors <a id="cite-note-2" href="#cite-ref-2">[2]</a> . It was originally written on a [Z80](Z80 "Z80") basis, as **BB-1** already standby at the [ACM 1978](ACM_1978 "ACM 1978") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and was ported to run on a *SYS-10* computer <a id="cite-note-5" href="#cite-ref-5">[5]</a> , based on [AMD 2900](https://en.wikipedia.org/wiki/AMD_Am2900) bit slicers <a id="cite-note-6" href="#cite-ref-6">[6]</a> .

While the hardware did no longer improve significantly since the mid 80s, the software and [opening book](Opening_Book "Opening Book") did. Bebe approached [parallelism](Programming#Parallelism "Programming") in generating [attack and defend maps](Attack_and_Defend_Maps "Attack and Defend Maps"), [move generation](Move_Generation "Move Generation"), [move ordering](Move_Ordering "Move Ordering"), and [evaluation](Evaluation "Evaluation"), but otherwise had a serial [search](Search "Search"). Its implementation of [Iterative deepening](Iterative_Deepening "Iterative Deepening") was quite unique. To avoid the [odd-even effect](Odd-Even_Effect "Odd-Even Effect"), Bebe searched only odd [depths](Depth "Depth") with an increment of two [plies](Ply "Ply") at the [root](Root "Root") <a id="cite-note-7" href="#cite-ref-7">[7]</a> . It further introduced a [learning approach](Learning "Learning") utilizing a [persistent hash table](Persistent_Hash_Table "Persistent Hash Table"), explained in [award winning](Bebe#Award "Bebe") paper <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

After Tony Scherzer's early death in January 1995 <a id="cite-note-9" href="#cite-ref-9">[9]</a> , the work on Bebe discontinued, while *SYS-10, Inc.* continued, and is now a company providing custom software applications located in [South Elgin, Illinois](https://en.wikipedia.org/wiki/South_Elgin,_Illinois) <a id="cite-note-10" href="#cite-ref-10">[10]</a> , owned by Linda Scherzer since 1978 <a id="cite-note-11" href="#cite-ref-11">[11]</a> .

## Photos & Games

[](File:ACM1984BebeNovag.JPG)
[Linda](Linda_Scherzer "Linda Scherzer") and [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), Bob Henry and [David Kittinger](David_Kittinger "David Kittinger") at [ACM 1984](ACM_1984 "ACM 1984"), Bebe vs. [Novag X](Novag_X "Novag X") <a id="cite-note-12" href="#cite-ref-12">[12]</a>

```

[Event "ACM 1984"]
[Site "San Francisco USA"]
[Date "1984.10.09"]
[Round "4"]
[White "Bebe"]
[Black "Novag"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3 d6 7.Ng5 d5 8.exd5 Nd4
9.d6 Nxb3 10.dxc7 Qxc7 11.axb3 h6 12.Nf3 e4 13.Re1 Be7 14.Nc3 exf3 15.Nxb5 Qc5
16.Qxf3 Qxb5 17.Qxa8 Qb7 18.Qxb7 Bxb7 19.d4 Kd7 20.c4 Bb4 21.Re2 Rd8 22.d5 Nxd5
23.cxd5 Bxd5 24.Rxa6 Bxb3 25.Re4 Bc5 26.Be3 Kc7 27.Ra1 Bd5 28.Bf4+ Kc6 29.Rea4
Be6 30.Be5 Rd2 31.Bxg7 Bxf2+ 32.Kh1 Bd5 33.Bc3 Rc2 34.Ra6+ Kc7 35.R6a5 Kc6
36.Ra6+ Kc7 37.R6a5 Kc6 38.Ra8 Bb6 39.Rg8 f5 40.Rg6+ Kb5 41.Rd1 Be4 42.Bd2 Rxb2
43.Bxh6 f4 44.Rg5+ Kc6 45.Rc1+ Kd6 46.Bg7 Rf2 47.Rd1+ Kc6 48.Be5 Be3 49.Rg4 Bc2
50.Ra1 Kd5 51.Bb8 f3 52.gxf3 Rxf3 53.Ra5+ Ke6 54.h4 Bf5 55.Rga4 Kf7 56.Kg2 Rf2+
57.Kg3 Rf1 58.Bf4 Bf2+ 59.Kg2 Bd3 60.Rd5 Be2 61.Rd7+ Kg6 62.h5+ Kxh5 63.Rd2 Bb6
64.Rxe2 Rg1+ 65.Kh2 Rb1 66.Rg2 Rb5 67.Ra6 Rf5 68.Kg3 Rf6 1-0

```

## Achievements

Bebe was one of the strongest chess entities in the 80s. At its first appearance, the [WCCC 1980](WCCC_1980 "WCCC 1980") in [Linz](https://en.wikipedia.org/wiki/Linz), it finished best placed "Micro" <a id="cite-note-13" href="#cite-ref-13">[13]</a> . Four draws in four rounds, playing programs like [Chess 4.9](</Chess_(Program)> "Chess (Program)") and [Nuchess](Nuchess "Nuchess"). The following three [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship") were even more successful. Bebe was first runner up at the [WCCC 1983](WCCC_1983 "WCCC 1983") in [New York](https://en.wikipedia.org/wiki/New_York_City), tied for first place at the [WCCC 1986](WCCC_1986 "WCCC 1986") in [Cologne](https://en.wikipedia.org/wiki/Cologne), and finally was runner up again in [Edmonton](https://en.wikipedia.org/wiki/Edmonton) at the [WCCC 1989](WCCC_1989 "WCCC 1989"). As mentioned by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), Bebe "helped" [Cray Blitz](Cray_Blitz "Cray Blitz") to win both the [WCCC 1983](WCCC_1983 "WCCC 1983") and the [WCCC 1986](WCCC_1986 "WCCC 1986") <a id="cite-note-14" href="#cite-ref-14">[14]</a> .

Bebe further played 13 consecutive [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), including the already mentioned WCCC in New York, from [1980](ACM_1980 "ACM 1980") until [1993](ACM_1993 "ACM 1993"), again runner up in [1981](ACM_1981 "ACM 1981") (tied), [1984](ACM_1984 "ACM 1984") and [1985](ACM_1985 "ACM 1985").

## Selective Deepening

At [ACM 1986](ACM_1986 "ACM 1986"), after winning [ChipTest](ChipTest "ChipTest"), [Merlin](Merlin "Merlin") and [Recom](Rebel "Rebel"), Bebe lost to [Belle](Belle "Belle"), the eventual winner. In the battle for the second place, Bebe was defeated by [Lachex](Lachex "Lachex"). Both programs went in a sequence of forced moves where both sides had only one single good choice along the way. Neither program had any idea about who would come up ahead in the end, until suddenly after playing along the forced line, both programs realized that Bebe was lost. In a discussion with [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") and others, Tony Scherzer made the statement that the old idea of selective [pruning](Pruning "Pruning") was dead, replaced by the new idea of selective [extensions](Extensions "Extensions") . According to Hsu, that was how the idea of [Singular Extensions](Singular_Extensions "Singular Extensions") began <a id="cite-note-15" href="#cite-ref-15">[15]</a> .

```

[Event "ACM 1986"]
[Site "Dallas USA"]
[Date "1986.11.05"]
[Round "5"]
[White "Lachex"]
[Black "Bebe"]
[Result "1-0"]

1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 e6 5.Nf3 Nc6 6.Na3 Bd7 7.Bc4 Qe4+ 8.Qe2 Qxe2+
9.Bxe2 cxd4 10.Nb5 O-O-O 11.cxd4 Bb4+ 12.Nc3 Be8 13.Be3 Nge7 14.O-O Ng6
15.Rad1 Kb8 16.a3 Bd6 17.d5 exd5 18.Rxd5 Nf4 19.Rxd6 Nxe2+ 20.Nxe2 Rxd6
21.Bf4 Kc8 22.Bxd6 Bd7 23.Rc1 Bg4 24.Ned4 Bxf3 25.gxf3 Kd7 26.Nxc6 bxc6
27.Rd1 Kc8 28.Bf4 Rd8 29.Rxd8+ Kxd8 30.b4 a6 31.Kf1 Ke7 32.Ke2 Ke6 33.Kd3 Kd5
34.Be3 g6 35.a4 h5 36.h4 f6 37.f4 f5 38.Bb6 Ke6 39.Kc4 Kd6 40.f3 1-0

```

## Descriptions

## 1980

from the [ACM 1980](ACM_1980 "ACM 1980") booklet <a id="cite-note-16" href="#cite-ref-16">[16]</a> :
Tony Scherzer, *SYS-10, Inc.*, [Hoffman Estates, Illinois](https://en.wikipedia.org/wiki/Hoffman_Estates,_Illinois), Bebe Chess Machine on site (32K bytes, 16 bits, 6,250,000 [inst/sec](https://en.wikipedia.org/wiki/Instructions_per_second))

```C++
A relatively new program and machine, Bebe has recently acquired a provisional [UCSF rating](https://en.wikipedia.org/wiki/US_Chess_Federation#Ratings) of 1810 based on play in one tournament. Bebe defeated an Expert in that tournament. Tony Scherzer's brainchild examines 10,000 [nodes/sec](Nodes_per_Second "Nodes per Second") or about 2,000,000 in a three minute move. The program is small, requiring only 10k 16 bit words. The program has no book. It uses [iterative deepening](Iterative_Deepening "Iterative Deepening") and is written in [assembly language](Assembly "Assembly"). 

```

## 1981-1986

- [ACM 1981](ACM_1981 "ACM 1981") <a id="cite-note-17" href="#cite-ref-17">[17]</a> : Tony Scherzer, Hoffman Estates, Illinois, Bebe 25.000 Nodes/Sec
- [WCCC 1983](WCCC_1983 "WCCC 1983") <a id="cite-note-18" href="#cite-ref-18">[18]</a> : Tony Scherzer, *SYS-10 Inc.*, Hoffman Estates, Illinois, Bebe Chess Engine, 7 [mips](https://en.wikipedia.org/wiki/Million_instructions_per_second#Million_instructions_per_second), 20K Nodes/Sec
- [ACM 1984](ACM_1984 "ACM 1984") <a id="cite-note-19" href="#cite-ref-19">[19]</a> : Tony Scherzer, *SYS-20 Inc.*, Hoffman Estates, Illinois, Bebe Chess Engine 20K Nodes/Sec
- [ACM 1986](ACM_1986 "ACM 1986") <a id="cite-note-20" href="#cite-ref-20">[20]</a> : Tony Scherzer and Linda Scherzer, SYS-10 Inc., Hoffman Estates, Illinois, Bebe Chess Engine 40K Nodes/Sec

## 1989

from the [WCCC 1989](WCCC_1989 "WCCC 1989") booklet <a id="cite-note-21" href="#cite-ref-21">[21]</a> :

```C++
Tony Scherzer and Linda Scherzer, SYS-10 Inc., Hoffman Estates, Illinois, Bebe Chess Engine, 40K Nodes/Sec

```

```C++
In early 1980 SYS-10 tried new hardware techniques needed for their mini/mainframe processor in co-processors for Bebe's CPU. Each co-processor takes over a specific function from the main CPU.

```

```C++
The first co-processor does the complete task of [move list generation](Move_Generation "Move Generation"). The actual unit is divided into two processors which function in parallel: one that finds pieces and one that calculate and stores moves. This parallelism provides results more than 25 times faster than software.

```

```C++
A second co-processor performs the [position scoring](Evaluation "Evaluation") function. The scorer "looks at" the output of the move generator and uses the moves to calculate values for piece position [mobility](Mobility "Mobility") and co-operation. The scorer functions in parallel with the move generator.

```

```C++
Bebe operates at four distinct levels:

```

- `Software does I/O, [timekeeping](Time_Management "Time Management"), [book lookup](Opening_Book "Opening Book"), [search depth](Depth "Depth") control, and overall system control.`
- `Special CPU instructions do [move list sorting](Move_Ordering "Move Ordering"), [internal board](Board_Representation "Board Representation") [update](Incremental_Updates "Incremental Updates") for [making](Make_Move "Make Move") and [unmaking moves](Unmake_Move "Unmake Move"), the [alpha-beta](Alpha-Beta "Alpha-Beta") minimax control, keeping track of [killer moves](Killer_Move "Killer Move"), building [bit maps](Bitboards "Bitboards") of piece locations, and some board scoring functions.`
- `The co-processors perform move list generation, and some of the board scoring functions.`
- `The self-activated parallel processor determines of either [king is in check](Check "Check") and determines the [attack-defender count](Attack_and_Defend_Maps "Attack and Defend Maps") for any [square](Squares "Squares"). Because it self starts, the answers for both kings are ready before the software can ask the question.`

## Mephisto Best-Publication Award

The fourth [Mephisto Best-Publication Award](Hegener_%26_Glaser#MephistoAward "Hegener & Glaser") for publications between April 01, 1990 and March 31, 1991 is awarded to [Tony](Tony_Scherzer "Tony Scherzer") and [Linda Scherzer](Linda_Scherzer "Linda Scherzer") and [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") for their article *Learning in Bebe* published in [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition") <a id="cite-note-22" href="#cite-ref-22">[22]</a>, explaining the implementation of a [persistent hash table](Persistent_Hash_Table#LearninginBebe "Persistent Hash Table") inside Bebe. The jury consisted of [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [David Levy](David_Levy "David Levy"), [Tony Marsland](Tony_Marsland "Tony Marsland"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") and [Ken Thompson](Ken_Thompson "Ken Thompson"). The image by Jaap van den Herik from the Award giving ceremony during [ACM 1991](ACM_1991 "ACM 1991"), November 20, 1991, [Albuquerque](https://en.wikipedia.org/wiki/Albuquerque%2C_New_Mexico), [New Mexico](https://en.wikipedia.org/wiki/New_Mexico), published in [ICCA Journal, Vol. 14, No. 4](ICGA_Journal#14_4 "ICGA Journal") <a id="cite-note-23" href="#cite-ref-23">[23]</a>, the same issue also containes a condensed version of the paper <a id="cite-note-24" href="#cite-ref-24">[24]</a> .

[](File:LearningInBeBe.jpg)
[Linda Scherzer](Linda_Scherzer "Linda Scherzer") with the Award <a id="cite-note-25" href="#cite-ref-25">[25]</a>, [ICCA](ICCA "ICCA") representant [Tony Marsland](Tony_Marsland "Tony Marsland"), and [Tony Scherzer](Tony_Scherzer "Tony Scherzer") .

## See also

- [Odd-Even Effect](Odd-Even_Effect "Odd-Even Effect")
- [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")

## Publications

- Editor (**1979**). *Scuffle in a Corner*. [Personal Computing, Vol. 3, No. 8](Personal_Computing#3_8 "Personal Computing"), pp. 76 » [ACM 1978](ACM_1978 "ACM 1978"), [Sargon](Sargon "Sargon")
- [Tony Scherzer](Tony_Scherzer "Tony Scherzer") (**1979**). *Background on BB-1*. [Personal Computing, Vol. 3, No. 11](Personal_Computing#3_11 "Personal Computing"), pp. 80
- [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") (**1990**). *Learning in Bebe.* [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")  » [Mephisto Best-Publication Award](Bebe#Award "Bebe")
- [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") (**1991**). *Learning in Bebe.* [ICCA Journal, Vol. 14, No. 4](ICGA_Journal#14_4 "ICGA Journal")
- [Linda Scherzer](Linda_Scherzer "Linda Scherzer") (**2020**). *BEBE, SYS-10, Inc., and computer chess*. [ICGA Journal, Vol. 42, Nos. 2-3](ICGA_Journal#42_23 "ICGA Journal")

## Forum Posts

- [Machine Learning Experience](https://groups.google.com/d/msg/rec.games.chess/wkTUUFfEvIE/RyFnJTjyQq4J) by [Mike Valvo](Michael_Valvo "Michael Valvo"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), January 22, 1990
- [Bebe and Belle](https://www.stmintz.com/ccc/index.php?id=71765) by Joshua Lee, [CCC](CCC "CCC"), October 04, 1999 » [Belle](Belle "Belle")

## External Links

## Chess Program

- [Bebe's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=350)

## Misc

- [bebe - Wiktionary](http://en.wiktionary.org/wiki/bebe)
- [bebé - Wiktionary](http://en.wiktionary.org/wiki/beb%C3%A9)
- [Bebe from Wikipedia](https://en.wikipedia.org/wiki/Bebe) (Disambiguation page)
- [Astrud Gilberto](Category:Astrud_Gilberto "Category:Astrud Gilberto") - [Água de Beber](https://en.wikipedia.org/wiki/%C3%81gua_de_Beber), 1965, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Cartoon](Cartoons "Cartoons") by Jeff Ragsdale from the [ICCA Journal](ICGA_Journal "ICGA Journal") 1987, 1988 and 1989, reprinted in [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings") from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> Linda Scherzer (1984): *"We justify this as our research and development department. We try out the firmware in Bebe, then design it for commercial products".*
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> Editor (**1979**). *Scuffle in a Corner*. [Personal Computing, Vol. 3, No. 8](Personal_Computing#3_8 "Personal Computing"), pp. 76 » [ACM 1978](ACM_1978 "ACM 1978"), BB-1, [Sargon](Sargon "Sargon")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a>  [Tony Scherzer](Tony_Scherzer "Tony Scherzer") (**1979**). *Background on BB-1*. [Personal Computing, Vol. 3, No. 11](Personal_Computing#3_11 "Personal Computing"), pp. 80
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> *SYS-10*, not to be confused with the decimal [Singer System-10](http://members.iinet.net.au/~daveb/S10/Sys-10.html)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Peggy Watt](http://www.linkedin.com/in/pwatt) (**1984**). *Mainframes checkmate Micros*. [InfoWorld](https://en.wikipedia.org/wiki/InfoWorld), November 5, 1984, pp. 18, [google books](https://books.google.de/books?id=oC4EAAAAMBAJ&lpg=PA49&dq=InfoWorld%2C%20November%205%2C%201984&client=firefox-a&hl=de&pg=PA18#v=onepage&q=InfoWorld,%20November%205,%201984&f=false)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Odd ply versus even ply searches](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/fb40c7c141dc062a) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 28, 1996
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") (**1990**). *Learning in Bebe.* [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [IGI Individual Record - Anthony Scherzer](http://www.familysearch.org/Eng/Search/IGI/individual_record.asp?recid=100000058897&lds=1&region=11&regionfriendly=North+America&frompage=99)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Welcome to SYS-10, Inc.](http://www.sys-10.com/)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Linda Scherzer (Shinouskis) - LinkedIn](http://www.linkedin.com/in/lindascherzer)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Peggy Watt](http://www.linkedin.com/in/pwatt) (**1984**). *Mainframes checkmate Micros*. [InfoWorld](https://en.wikipedia.org/wiki/InfoWorld), November 5, 1984, pp. 18, [google books](http://books.google.com/books?id=oC4EAAAAMBAJ&pg=PA49&dq=InfoWorld,+November+5,+1984&client=firefox-a&cd=4#v=onepage&q=InfoWorld%2C%20November%205%2C%201984&f=false)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Mikros noch ohne Großmeister-Format](https://www.computerwoche.de/a/mikros-noch-ohne-grossmeister-format,1191318) November 28, 1980, [Computerwoche](Computerworld#Woche "Computerworld") 48/1980 (German)
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Re: Who is the better chess program author? (more)](https://www.stmintz.com/ccc/index.php?id=201764) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), December 13, 2001
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**2002**). *[Behind Deep Blue](http://press.princeton.edu/titles/7342.html): Building the Computer that Defeated the World Chess Champion*, Princeton University Press, ISBN 0-691-09065-3, pp. 54-55
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [The Eleventh ACM's North American Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cdeeb), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.1980_11th_ACM_NACCC/The_Eleventh_ACMs_North_American_Computer_Chess_Championship.1980.062303015.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [The Twelfth ACM's North American Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6ce737), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.1981_ACM_NACCC/1981_ACM_NACCC.sm.062303017.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [The Fourth World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c8af8) (labeled 22nd ACM), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1983_WCCC/1983-%20WCCC.062303061.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_36_C.pdf) by [Danny Kopec](Danny_Kopec "Danny Kopec")
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [The Fifteenth ACM Computer Chess Championship, San Francisco California, October 7-9, 1984](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c9575), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1984_15th_NACCC/1984%20NACCC.062303012.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [The ACM's Seventeenth North American Computer Chess Championship and The Sixth World Microcomputer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6ca4a7) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1986_17th_NACCC/1986%20NACCC.062303062.sm.pdf)
1. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)
1. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") (**1990**). *Learning in Bebe.* [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")
1. <a id="cite-ref-23" href="#cite-note-23">↑</a> The Board of ICCA (**1991**). *The Mephisto Best-Publication Award*. [ICCA Journal, Vol. 14, No. 4](ICGA_Journal#14_4 "ICGA Journal"), pp. 211
1. <a id="cite-ref-24" href="#cite-note-24">↑</a> [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") (**1991**). *Learning in Bebe.* [ICCA Journal, Vol. 14, No. 4](ICGA_Journal#14_4 "ICGA Journal")
1. <a id="cite-ref-25" href="#cite-note-25">↑</a> [Linda Scherzer](Linda_Scherzer "Linda Scherzer") with the Award (a [Mephisto Vancouver](Mephisto_Vancouver "Mephisto Vancouver") ?)

**[Up one level](Engines "Engines")**

