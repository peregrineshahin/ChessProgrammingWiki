---
title: Cyrus
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Cyrus**

[](http://www.worldofspectrum.org/infoseekid.cgi?id=0001214) Cyrus IS-Chess <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cyrus**,

[Richard Lang's](Richard_Lang "Richard Lang") first chess program, written in [Assembly](Assembly "Assembly") for a [Z80](Z80 "Z80") CPU. Starting programming in January 1981, his tournament debut at the [2nd European Microcomputer Chess Championship](European_MCC_1981 "European MCC 1981") at the [PCW](Personal_Computer_World "Personal Computer World") Show 1981 in London was already a breakthrough. Cyrus was the clear winner with 5 out of 5 in a field of 12 Micros. Cyrus ran on a [Nascom](https://en.wikipedia.org/wiki/Nascom) microcomputer using a 4 MHz Z80 CPU, and Lang immediately was offered two contracts by [David Levy](David_Levy "David Levy") and [Kevin O’Connell](Kevin_O%E2%80%99Connell "Kevin O’Connell"), one for Cyrus, and one to work as programmer for [Intelligent Software](Intelligent_Software "Intelligent Software"). Lang accepted, and *Cyrus IS-Chess* for the [Sinclair ZX Spectrum](ZX_Spectrum "ZX Spectrum") was his first commercial entry, followed by programs for various [dedicated chess computers](Dedicated_Chess_Computers "Dedicated Chess Computers") merchandised by *Intelligent Software*, as well a further improved version of Cyrus, Cyrus II. In an 2003 interview, Richard Lang stated that there is still much of Cyrus in current versions of [Chess Genius](Chess_Genius "Chess Genius"). For example, he had never used [quiescence searches](Quiescence_Search "Quiescence Search") and relied instead on a [static swap off routine](Static_Exchange_Evaluation "Static Exchange Evaluation") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## ACM 1981 Blitz

An improved version of Cyrus appeared at the [ACM Speed Chess Tournament 1981](ACM_1981 "ACM 1981"), running on an [Osborne](https://en.wikipedia.org/wiki/Osborne_Computer_Corporation) Z80 microcomputer and matched against mainframe programs, beating [Cray Blitz](Cray_Blitz "Cray Blitz") and [Chess 4.5](</Chess_(Program)> "Chess (Program)"), and only losing to [Belle](Belle "Belle") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

```

[Event "ACM 1981 Speed Tournament"]
[Site "Los Angeles"]
[Date " 1981.11.10"]
[Round "?"]
[White "Cyrus"]
[Black "Cray Blitz"]
[Result "1-0"]

1.e4 d6 2.d4 g6 3.Nc3 Nf6 4.Bb5 Nbd7 5.Nf3 c6 6.Be2 Bg7 7.0-0 0-0 8.Qd3 e5 
9.Bg5 h6 10.Bxf6 Qxf6 11.Rfd1 Rd8 12.a4 a5 13.Ra3 Qf4 14.g3 Qf6 15.Rb3 Ra7 
16.Qc4 Ra6 17.dxe5 dxe5 18.Rd2 b6 19.Qd3 Bb7 20.Qd6 Qxd6 21.Rxd6 Raa8 
22.Rd2 Ba6 23.Bxa6 Rxa6 24.Ne2 c5 25.Rbd3 Ra7 26.Nc3 Rb7 27.b3 Kh8 28.Nb5 
Kg8 29.Nd6 Rc7 30.Nb5 Rb7 31.Rd5 f6 32.Nd6 Rc7 33.Nb5 Rb7 34.c4 Bf8 35.Nc3 
g5 36.Ne1 Bg7 37.Nc2 Kh8 38.Ne3 Kg8 39.Nf5 Bf8 40.Ne3 Bg7 41.R5d3 Kh8 
42.Nf5 Ra7 43.Nb5 Ra6 44.Nc7 Ra7 45.Ne6 Re8 46.Nexg7 1-0

```

## Intelligent Software

Following programs and [dedicated chess computers](Dedicated_Chess_Computers "Dedicated Chess Computers") with programs based on Cyrus were released during Lang's period working for [Intelligent Software](Intelligent_Software "Intelligent Software") <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

- Cyrus for [Sinclair ZX Spectrum](ZX_Spectrum "ZX Spectrum"), [Z80](Z80 "Z80") [assembly](Assembly "Assembly") language, 1981
- [Chess 2001](Chess_2001 "Chess 2001"), Z80 assembly language, 1982 <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [Intelligent Chess Software](Intelligent_Chess_Software "Intelligent Chess Software"), Z80 assembly language
- [L'Empereur](L%27Empereur "L'Empereur"), Z80 assembly language <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [La Regence](La_Regence "La Regence"), Z80 assembly language <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>
- [Dragon Chess](index.php?title=Dragon_Chess&action=edit&redlink=1 "Dragon Chess (page does not exist)"), [6809](https://en.wikipedia.org/wiki/Motorola_6809) assembly language, for [Dragon Data](https://en.wikipedia.org/wiki/Dragon_Data) [Home computers](https://en.wikipedia.org/wiki/Home_computer) <a id="cite-note-9" href="#cite-ref-9">[9]</a>

## Cyrus II

[](http://www.worldofspectrum.org/infoseekid.cgi?id=0001213) Cyrus II [3D screen](3D_Graphics_Board "3D Graphics Board") <a id="cite-note-10" href="#cite-ref-10">[10]</a>
Working for [Intelligent Software](Intelligent_Software "Intelligent Software"), Richard Lang continued the Cyrus development including a [6502](6502 "6502") port to cover the growing market of [Apple II](Apple_II "Apple II") and [Commodore 64](Commodore_64 "Commodore 64") [home computers](https://en.wikipedia.org/wiki/Home_computer).

At the [3rd European Microcomputer Chess Championship](European_MCC_1982 "European MCC 1982"), September 1982, [La Regence](La_Regence "La Regence") became strong runner up behind [Advance 2.4](Advance "Advance"), while Cyrus II itself didn't quite come up to its expectations. Lang: 'It was written in such a hurry and the tournament came in the middle of its development period rather than at the end'. There were quite a few new ideas in the program, and he didn't have much time to test them before the tournament. The new ideas were a combination of running faster and implementing new [chess knowledge](Knowledge "Knowledge"), by getting it to recognize [isolated](Isolated_Pawn "Isolated Pawn") and [doubled pawns](Doubled_Pawn "Doubled Pawn") and the like <a id="cite-note-11" href="#cite-ref-11">[11]</a>. Various programs derivate from Cyrus competed at the [4th European Microcomputer Chess Championship](European_MCC_1983 "European MCC 1983"), September 1983. Cyrus 2.5 finished best (4th) of the home computer programs tied with [White Knight 11](White_Knight "White Knight") by [Martin Bryant](Martin_Bryant "Martin Bryant"), behind [Advance 3.0](Advance "Advance") and [Chess 2001](Chess_2001 "Chess 2001").

## Cyrus 68K

*see main article [Cyrus 68K](Cyrus_68K "Cyrus 68K")*

In about 1983 Richard Lang started to write his new program [Psion](Psion "Psion") for [68000](68000 "68000") family of processors, and was about to abandon the work for [Intelligent Software](Intelligent_Software "Intelligent Software"), who continued their own work by owning the Cyrus brand by primary programmer [Mark Taylor](Mark_Taylor "Mark Taylor"), yielding in [Cyrus 68K](Cyrus_68K "Cyrus 68K"). Its predecessor, competing under the name *65 Cyrus X* at the [WMCCC 1983](WMCCC_1983 "WMCCC 1983") in [Budapest](https://en.wikipedia.org/wiki/Budapest) is assigned to *Intelligent Software* with the authors [David Levy](David_Levy "David Levy"), [Mark Taylor](Mark_Taylor "Mark Taylor") and [Kevin O’Connell](Kevin_O%E2%80%99Connell "Kevin O’Connell") at the [ICGA](ICGA "ICGA") tournament page <a id="cite-note-12" href="#cite-ref-12">[12]</a>.

## See also

- [Cyrus 68K](Cyrus_68K "Cyrus 68K")

## External Links

## Chess Program

- [Chess Computers - The UK Story](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")
- [Cyrus IS Chess - World of Spectrum](http://www.worldofspectrum.org/infoseekid.cgi?id=0001214)
- [Cyrus II - World of Spectrum](http://www.worldofspectrum.org/infoseekid.cgi?id=0001213)
- [Cyrus download @ Game Downloads](http://free-game-downloads.mosw.com/abandonware/pc/board_games_h/cyrus.html)
- [Cyrus Is Chess by Sinclair from Retrogames](http://www.retrogames.co.uk/more/on/details/015072)
- [Cyrus II Chess for CPC - GameSpot](http://www.gamespot.com/cpc/puzzle/cyrusiichess/index.html)
- [Cyrus for DOS (1985)](http://www.mobygames.com/game/cyrus) from [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
- [Chess and Computers](http://members.chello.at/theodor.lauppert/games/chess.htm)

## Misc

- [Cyrus (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Cyrus_(disambiguation)>)
- [Cyrus I from Wikipedia](https://en.wikipedia.org/wiki/Cyrus_I), King of [Anshan](https://en.wikipedia.org/wiki/Anshan_%28Persia%29)
- [Cyrus the Great from Wikipedia](https://en.wikipedia.org/wiki/Cyrus_the_Great), grandson of [Cyrus I](https://en.wikipedia.org/wiki/Cyrus_I) and the founder of the [Achaemenid Empire](https://en.wikipedia.org/wiki/Achaemenid_Empire)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Cyrus IS Chess - World of Spectrum](http://www.worldofspectrum.org/infoseekid.cgi?id=0001214)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Richard Lang - Question & Answer Interview given to a German magazine in 2003](http://www.chesscomputeruk.com/Richard_Lang_Q_A.pdf), pdf hosted by [Mike Watters](Mike_Watters "Mike Watters"), [Chess Computer UK](http://www.chesscomputeruk.com/index.html)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Tony Harrington](Tony_Harrington "Tony Harrington") (**1983**). *Winner Takes All*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), [September 83](http://www.chesscomputeruk.com/html/publication_archive_1983.html), [pdf](http://www.chesscomputeruk.com/Richard_Lang0001.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters"), [Chess Computer UK](http://www.chesscomputeruk.com/index.html)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Richard Lang - Question & Answer Interview given to a German magazine in 2003](http://www.chesscomputeruk.com/Richard_Lang_Q_A.pdf), pdf hosted by [Mike Watters](Mike_Watters "Mike Watters"), [Chess Computer UK](http://www.chesscomputeruk.com/index.html)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [CXG Chess 2001](http://www.schach-computer.info/wiki/index.php/CXG_Chess_2001) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [SciSys and Novag : The Early Years](http://www.chesscomputeruk.com/html/scisys_and_novag___the_early_y.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Chafitz TSB 4 La Regence](http://www.schach-computer.info/wiki/index.php/Sandy_TSB_4_La_Regence) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Gilbert Obermair](http://de.wikipedia.org/wiki/Gilbert_Obermair) (**1983**). [Schach-Computer Report ’84](http://www.schach-computer.info/wiki/index.php/Schachcomputer_Report_%2784), S. 62-63, [Applied Concepts](Applied_Concepts "Applied Concepts") - La Regence TSB IV, [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/10-1982%20%5BH-0601%5D%20Applied%20Concepts%20-%20La%20Regence%20TSB%20IV.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis") (German)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Computing History - DragonChess](http://www.computinghistory.org.uk/det/4186/DragonChess/)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Cyrus II - World of Spectrum](http://www.worldofspectrum.org/infoseekid.cgi?id=0001213)
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Tony Harrington](Tony_Harrington "Tony Harrington") (**1983**). *Winner Takes All*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), [September 83](http://www.chesscomputeruk.com/html/publication_archive_1983.html), [pdf](http://www.chesscomputeruk.com/Richard_Lang0001.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Cyrus' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=405)

**[Up one level](Engines "Engines")**

