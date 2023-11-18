---
title: Beowulf
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Beowulf**

\[ Beowulf fighting the [dragon](Category:Dragon "Category:Dragon") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Beowulf**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible [open source engine](Category:Open_Source "Category:Open Source"), the game-playing brains behind the [ChessBrain](ChessBrain "ChessBrain") project, a distributed computing project similar to [SETI@home](https://en.wikipedia.org/wiki/SETI@home), that aims to harness the collective calculating power of individual computers over the internet to play a game of chess <a id="cite-note-2" href="#cite-ref-2">[2]</a> . [Colin Frayn](Colin_Frayn "Colin Frayn") is head of the project and primary Beowulf author, supported by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Ron Murawski](Ron_Murawski "Ron Murawski"), [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano") et al.. The version history ends with version 2.3, February 13, 2004, version 2.4 from August 21, 2010 is the latest released version with several bug fixes <a id="cite-note-3" href="#cite-ref-3">[3]</a> . Beowulf is published under [GNU General Public Licence V2](Free_Software_Foundation#GPL "Free Software Foundation").

## Features

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

- [Rotated Bitboard](Rotated_Bitboards "Rotated Bitboards") [Move Generator](Move_Generation "Move Generation")
- Advanced Static Analysis Function
- [Static Exchange Evaluator](Static_Exchange_Evaluation "Static Exchange Evaluation") for [Quiescence](Quiescence_Search "Quiescence Search") [Pruning](Pruning "Pruning")
- [Quiescence Search](Quiescence_Search "Quiescence Search") [Delta Cuts](Delta_Pruning "Delta Pruning")
- [Adaptive Depth Null move](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") with [Verification Search](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")
- [Adaptive Razoring](Razoring "Razoring") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [Innovative Design of Hashtables](Hash_Table "Hash Table")
- [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Aspiration Window Search](Aspiration_Windows "Aspiration Windows")
- [History](History_Heuristic "History Heuristic") and [Killer Move Heuristics](Killer_Heuristic "Killer Heuristic")
- [Numerous Search Extensions](Extensions "Extensions")
- [XBoard](XBoard "XBoard")/[WinBoard](WinBoard "WinBoard") Support
- [Opening Book Support](Opening_Book "Opening Book")
- [Endgame Tablebase Support](Endgame_Tablebases "Endgame Tablebases") ([Nalimov](Nalimov_Tablebases "Nalimov Tablebases"))
- [Matt Taylor's](Matt_Taylor "Matt Taylor") [Folded BitScan](BitScan#MattTaylorsFoldingtrick "BitScan") (board.c)
- [Variable Skill Levels](Playing_Strength "Playing Strength")
- [Test Suite Support](Test-Positions#TestSuites "Test-Positions")
- [ISAAC64 Pseudorandom Number Generator](Pseudorandom_Number_Generator "Pseudorandom Number Generator") by [Bob Jenkins](Bob_Jenkins "Bob Jenkins"), 1996, <a id="cite-note-6" href="#cite-ref-6">[6]</a> modifications by [Ron Murawski](Ron_Murawski "Ron Murawski"), 2001

## Forum Posts

## 2000 ...

- [On Beowulf - long post](https://www.stmintz.com/ccc/index.php?id=173418) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), April 04, 2001
- [Beowulf v1.5 Has Been Released](https://www.stmintz.com/ccc/index.php?id=176264) by [Colin Frayn](Colin_Frayn "Colin Frayn"), [CCC](CCC "CCC"), June 21, 2001
- [Beowulf 1.6d](https://www.stmintz.com/ccc/index.php?id=186505) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), August 30, 2001
- [Beowulf v1.7 Released](https://www.stmintz.com/ccc/index.php?id=192793) by [Colin Frayn](Colin_Frayn "Colin Frayn"), [CCC](CCC "CCC"), October 11, 2001
- [Beowulf v1.8 Released](https://www.stmintz.com/ccc/index.php?id=201043) by [Colin Frayn](Colin_Frayn "Colin Frayn"), [CCC](CCC "CCC"), December 08, 2001
- [Beowulf v1.9 Released](https://www.stmintz.com/ccc/index.php?id=212142) by [Colin Frayn](Colin_Frayn "Colin Frayn"), [CCC](CCC "CCC"), February 06, 2002
- [Beowulf v2.0 Release!](https://www.stmintz.com/ccc/index.php?id=221417) by [Colin Frayn](Colin_Frayn "Colin Frayn"), [CCC](CCC "CCC"), October 06, 2002
- [Beowulf hot spots shown pictorially](https://www.stmintz.com/ccc/index.php?id=236641) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 20, 2002
- [Beowulf v2.1](https://www.stmintz.com/ccc/index.php?id=256688) by [Colin Frayn](Colin_Frayn "Colin Frayn"), [CCC](CCC "CCC"), October 06, 2002
- [New Beowulf Finally \*officially) Released](https://www.stmintz.com/ccc/index.php?id=270921) by [Colin Frayn](Colin_Frayn "Colin Frayn"), [CCC](CCC "CCC"), December 16, 2002
- [Beowulf curve calibration results for depth = 5 plies](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=47806) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 07, 2004

## 2005 ...

- [Beowulf has Moved!](https://www.stmintz.com/ccc/index.php?id=434394) by [Colin Frayn](Colin_Frayn "Colin Frayn"), [CCC](CCC "CCC"), June 30, 2005
- [Beowulf Fixed (I hope)](https://www.stmintz.com/ccc/index.php?id=448350) by [Colin Frayn](Colin_Frayn "Colin Frayn"), [CCC](CCC "CCC"), September 07, 2005
- [Beowulf 2.4 Windows 64-bit build available](http://www.talkchess.com/forum/viewtopic.php?t=18395) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), December 15, 2007
- [Beowulf 2.4 Windows-executable version](http://www.talkchess.com/forum/viewtopic.php?t=23203) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 23, 2008

## 2010 ...

- [Beowulf v2.4a chess engine](http://www.talkchess.com/forum/viewtopic.php?t=35859) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 22, 2010
- \[TrappyBeowulf - A Beowulf mod to use [Trappy Minimax](http://www.talkchess.com/forum/viewtopic.php?t=47057)\] by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), January 30, 2013 <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## External Links

## Chess Engine

- [Beowulf Computer Chess Engine](http://www.frayn.net/beowulf/)
- [Beowulf version history](http://www.frayn.net/beowulf/version.html)
- [Computer Chess Programming Theory](http://www.frayn.net/beowulf/theory.html)
- [Beowulf 2.4a 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Beowulf%202.4a%2064-bit#Beowulf_2_4a_64-bit) in [CCRL 40/40](CCRL "CCRL")
- [probabilityZero/TrappyBeowulf · GitHub](https://github.com/probabilityZero/TrappyBeowulf) by [Mike Vollmer](index.php?title=Mike_Vollmer&action=edit&redlink=1 "Mike Vollmer (page does not exist)")

## Misc

- [Beowulf (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Beowulf_%28disambiguation%29)
- [Beowulf from Wikipedia](https://en.wikipedia.org/wiki/Beowulf)
- [Beowulf (hero) from Wikipedia](https://en.wikipedia.org/wiki/Beowulf_%28hero%29)
- [Beowulf cluster from Wikipedia](https://en.wikipedia.org/wiki/Beowulf_cluster)
- [List of Beowulf characters from Wikipedia](https://en.wikipedia.org/wiki/List_of_Beowulf_characters)
- [The Dragon (Beowulf) from Wikipedia](<https://en.wikipedia.org/wiki/The_dragon_(Beowulf)>)
- [Beowulf: The Legend from Wikipedia](https://en.wikipedia.org/wiki/Beowulf:_The_Legend)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> A 1908 depiction of Beowulf fighting the dragon by [J. R. Skelton](http://commons.wikimedia.org/wiki/Category:J._R._Skelton), Illustration in the children's book *[Stories of Beowulf](http://www.mainlesson.com/display.php?author=marshall&book=beowulf&story=_contents)* ([H. E. Marshall](https://en.wikipedia.org/wiki/Henrietta_Elizabeth_Marshall)), published in [New York](https://en.wikipedia.org/wiki/New_York_City) in 1908 by [E. P. Dutton & Company](https://en.wikipedia.org/wiki/E._P._Dutton), [Beowulf from Wikipedia](https://en.wikipedia.org/wiki/Beowulf), [The Dragon (Beowulf) from Wikipedia](https://en.wikipedia.org/wiki/The_Dragon_%28Beowulf%29)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [ChessBrain](http://www.chessbrain.net/)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Beowulf v2.4a chess engine](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=367856&t=35859) by [Tony Mokonen](index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](CCC "CCC"), August 25, 2010
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Beowulf version history](http://www.frayn.net/beowulf/version.html)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Beowulf 2.4 Windows 64-bit build available](http://www.talkchess.com/forum/viewtopic.php?t=18395) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), December 15, 2007
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [ISAAC, a fast cryptographic random number generator](http://burtleburtle.net/bob/rand/isaacafa.html)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [probabilityZero/TrappyBeowulf · GitHub](https://github.com/probabilityZero/TrappyBeowulf) by [Mike Vollmer](index.php?title=Mike_Vollmer&action=edit&redlink=1 "Mike Vollmer (page does not exist)")

**[Up one Level](Engines "Engines")**

