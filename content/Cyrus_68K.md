---
title: Cyrus 68K
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Cyrus 68K**

\[ [Cyrus the Great](https://en.wikipedia.org/wiki/Cyrus_the_Great) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cyrus 68K**,

a chess program by [Mark Taylor](Mark_Taylor "Mark Taylor") and advisor [David Levy](David_Levy "David Levy") for the [68000](68000 "68000") (68K) based family of [microprocessors](https://en.wikipedia.org/wiki/Microprocessor). Cyrus 68K, not to confused with [Richard Lang's](Richard_Lang "Richard Lang") earlier program [Cyrus](Cyrus "Cyrus"), was written by Taylor from scratch in 1985. Richard Lang, like Mark Taylor affiliated with Levy's and [O’Connell's](Kevin_O%E2%80%99Connell "Kevin O’Connell") company [Intelligent Software](Intelligent_Software "Intelligent Software"), already focused on [Psion](Psion "Psion") at that time, had abandoned Intelligent Software, and was about to work for [Hegener & Glaser](Hegener_%26_Glaser "Hegener & Glaser") on [Mephisto](Mephisto "Mephisto").

## Photos & Games

[](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html)
[Mark Taylor](Mark_Taylor "Mark Taylor"), [Kevin O’Connell](Kevin_O%E2%80%99Connell "Kevin O’Connell") and [David Levy](David_Levy "David Levy") with Cyrus 68K vs. [Nona](Nona "Nona"), [WCCC 1986](WCCC_1986 "WCCC 1986") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>

```

[Event "5th World Computer Chess Championship"]
[Site "Cologne, Germany"]
[Date "1986.06.15"]
[Round "5"]
[White "Nona"]
[Black "Cyrus 68K"]
[Result "1-0"]

1.d4 e6 2.e4 d5 3.Nc3 Bb4 4.e5 Ne7 5.Bd2 Nf5 6.Nf3 Be7 7.Bd3 Nc6 8.Be3 Nxe3 
9.fxe3 Nb4 10.Be2 c5 11.O-O Nc6 12.Na4 c4 13.Nc3 Kf8 14.e4 Ke8 15.Rf2 h6 
16.exd5 exd5 17.Qd2 Bf5 18.Nd1 Nb4 19.Ne3 Be4 20.b3 cxb3 21.axb3 h5 22.Ng5 
Bxg5 23.Qxb4 Qe7 24.Bb5+ Kf8 25.Qxe7+ Kxe7 26.Re1 Ke6 27.c4 Raf8 28.cxd5+ 
Bxd5 29.Nxd5 Kxd5 30.e6 Be7 31.Rxf7 Rxf7 32.exf7 Bb4 33.Rd1 Rf8 34.Be2 h4 
35.Bc4+ Kd6 36.Rf1 Bc3 37.Rf4 Rh8 38.f8=Q+ 1-0

```

## SEX

Cyrus 68K was Intelligent Software's testbed for the [SEX Algorithm](SEX_Algorithm "SEX Algorithm"), to apply [fractional extensions](Extensions#FractionalExtensions "Extensions") and [reductions](Reductions "Reductions"), most notably already a kind of [LMR](Late_Move_Reductions "Late Move Reductions"), considering forced [tactical moves](Tactical_Moves "Tactical Moves") such as [checks](Check "Check"), [captures](Captures "Captures"), [mate threats](Checkmate "Checkmate") determined by [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance"), as well as [killer moves](Killer_Move "Killer Move") and early [non-tactical moves](Quiet_Moves "Quiet Moves") and from a evaluated and sorted [move list](Move_List "Move List") with a lower [depth](Depth "Depth") decrement than later non-tactical siblings.

Excerpts from *The [SEX Algorithm](SEX_Algorithm "SEX Algorithm") in Computer Chess* 1989 <a id="cite-note-4" href="#cite-ref-4">[4]</a> :

```C++
Later we designed a [68000](68000 "68000") program called **Cyrus 68K**, written by one of us ([Mark Taylor](Mark_Taylor "Mark Taylor")), which evaluated and sorted all the moves from a node being expanded: we used these evaluations to determine the SXDEC for moves that were non-tactical. An obvious way to accomplish this is to assign the "best" (i.e., highest-scoring) non-tactical move a low SXDEC and to determine the SXDEC values for its non-tactical siblings on the basis of the difference in score among them.
...
A second generation of the search extension algorithm was developed during the period 1985-1988. Many of the original ideas were used but we tried to eliminate certain obvious deficiencies and to make the intelligence in the program more sophisticated. We came up with a number of new ideas and tested them in a [68000](68000 "68000")-based program called **Cyrus 68K**. In general the results were rather encouraging, and we now feel that there is no longer a need to be shy about our work, hence the revised acronym for the algorithm and the renaming of the key variables to SEX and SEXDEC.

```

## The Sphinx

Cyrus 68K was commercially available as the [Sphinx](CXG_Sphinx "CXG Sphinx"), a [dedicated chess computer](Dedicated_Chess_Computers "Dedicated Chess Computers") under the brand name [CGX](Newcrest_Technology#CXG "Newcrest Technology"), and manufactured by [Eric White's](Eric_White "Eric White") [Newcrest Technology Ltd.](Newcrest_Technology "Newcrest Technology"), [Hong Kong](https://en.wikipedia.org/wiki/Hong_Kong) <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## See also

- [CXG Sphinx](CXG_Sphinx "CXG Sphinx")
- [Cyrus](Cyrus "Cyrus")

## Publications

- [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 12, No. 1, pp. 10-21

## External Links

## Chess Program

- [Cyrus 68K' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=405)
- [The chess games of Cyrus 68K (Computer)](http://www.chessgames.com/perl/chessplayer?pid=33964) from [chessgames.com](http://www.chessgames.com/index.html)
- [CXG Electronic Chess Computers](http://www.spacious-mind.com/html/cxg.html) from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
- [Chess Computers - The UK Story](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")

## Misc

- [Cyrus (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Cyrus_(disambiguation)>)
- [Cyrus I from Wikipedia](https://en.wikipedia.org/wiki/Cyrus_I)
- [Cyrus the Great from Wikipedia](https://en.wikipedia.org/wiki/Cyrus_the_Great)
- [Cyrus IMAP server from Wikipedia](https://en.wikipedia.org/wiki/Cyrus_IMAP_server)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Illustration from "[Illustrerad verldshistoria](http://sv.wikisource.org/wiki/Illustrerad_Verldshistoria) utgifven av [Ernst Wallis](http://sv.wikisource.org/wiki/F%C3%B6rfattare:Ernst_Wallis). Volume I": Relief of Cyrus, 1875. [Cyrus the Great from Wikipedia](https://en.wikipedia.org/wiki/Cyrus_the_Great), not to confused with his grandfather [Cyrus I](https://en.wikipedia.org/wiki/Cyrus_I)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chess Computers - The UK Story](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Cologne 1986 - Chess - Round 5 - Game 7 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=62&round=5&id=7)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 12, No. 1, pp. 10-21.
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [CXG Electronic Chess Computers](http://www.spacious-mind.com/html/cxg.html) from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [CXG](http://www.schach-computer.info/wiki/index.php/CXG) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)

**[Up one level](Engines "Engines")**

