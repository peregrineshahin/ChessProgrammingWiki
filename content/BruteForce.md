---
title: BruteForce
---
**[Home](Home "Home") * [Search](Search "Search") * Brute-Force**

[](https://en.wikipedia.org/wiki/Brute_Force_%281947_film%29) Brute Force, 1947 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Brute-Force** performs an exhaustive search, which enumerates all possible candidates for the solution to prove whether it satisfies the [problem statement](https://en.wikipedia.org/wiki/Problem_statement). Brute-force algorithms are conceptually simple, but usually suffer from exponential growing [search space](Search_Space "Search Space").

## Contents

- [1 Search Algorithms](#search-algorithms)
- [2 Backtracking](#backtracking)
- [3 See also](#see-also)
- [4 Publications](#publications)
  - [4.1 1949](#1949)
  - [4.2 1970 ...](#1970-...)
  - [4.3 1980 ...](#1980-...)
  - [4.4 1990 ...](#1990-...)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
- [7 References](#references)

## Search Algorithms

In 1949, [Claude Shannon](Claude_Shannon "Claude Shannon") categorized brute-force [minimax search](Minimax "Minimax") as [Type A strategy](Type_A_Strategy "Type A Strategy"), which enumerates and minimaxes all leaf positions of a [tree](Search_Tree "Search Tree") with an uniform [depth](Depth "Depth"), and concluded a machine operating according to the type A strategy would be both slow and a weak player <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Considering the [branching factor](Branching_Factor "Branching Factor") potentiated by depth, Shannon favored the [Type B strategy](Type_B_Strategy "Type B Strategy"), a selective approach only searching "important" branches as the most promising.

However, with the advent of brute-force [alpha-beta](Alpha-Beta "Alpha-Beta"), and programs like [Daly CP](Daly_CP "Daly CP"), [Tech](Tech "Tech"), [Kaissa](Kaissa "Kaissa") and [Chess 4.5](</Chess_(Program)> "Chess (Program)") in the early 70s, the era of the former dominating Type B programs drew to a close. Today most programs are closer to Type A, but have some characteristics of a Type B due to [selectivity](Selectivity "Selectivity").

## Backtracking

[Backtracking](Backtracking "Backtracking") discards large sets of incrementally build candidates to a solution, and "backtracks" a partial candidate as soon as it determines it cannot become member of the solution, for instance as demonstrated by the [recursive](Recursion "Recursion") [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator"). Backtracking algorithms are not considered brute-force.

## See also

- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Backtracking](Backtracking "Backtracking")
- [Brute Force (Program)](</Brute_Force_(Program)> "Brute Force (Program)")
- [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator")
- [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [Looking for Magics](Looking_for_Magics "Looking for Magics")
- [Minimax](Minimax "Minimax")
- [Saitek Brute Force](Saitek_Brute_Force "Saitek Brute Force")
- [Selective Search versus Brute Force - Conference at WCCC 1986](WCCC_1986#Workshop "WCCC 1986")
- [Selectivity](Selectivity "Selectivity")
- [Shannon's Type A Strategy](Type_A_Strategy "Type A Strategy")
- [Shannon's Type B Strategy](Type_B_Strategy "Type B Strategy")
- [Trial and Error](Trial_and_Error "Trial and Error")

## Publications

## 1949

- [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf)

## 1970 ...

- [James Gillogly](James_Gillogly "James Gillogly") (**1972**). *[The Technology Chess Program](http://www.sciencedirect.com/science/article/pii/0004370272900458)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 3, pp. 145-163, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
- [David Slate](David_Slate "David Slate") and [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")

## 1980 ...

- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1981**). *An Examination of Brute Force Intelligence.* [IJCAI 81](Conferences#IJCAI1981 "Conferences")
- [Richard Korf](Richard_Korf "Richard Korf") (**1984**). *The Complexity of Brute Force Search*. Technical Report, Department of Computer Science, [Columbia University](Columbia_University "Columbia University") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [David Slate](David_Slate "David Slate") (**1984**). *Interior-node Score Bounds in a Brute-force Chess Program.* [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal")
- [David Levy](David_Levy "David Levy") (**1986**). *When will Brute Force Programs beat Kasparov?* [ICCA Journal, Vol. 9, No. 2](ICGA_Journal#9_2 "ICGA Journal")
- [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek"), [Marcus Wagner](Marcus_Wagner "Marcus Wagner") (**1986**). *Selective Search versus Brute Force.* [ICCA Journal, Vol. 9, No. 3](ICGA_Journal#9_3 "ICGA Journal")
- [Richard Wheen](index.php?title=Richard_Wheen&action=edit&redlink=1 "Richard Wheen (page does not exist)") (**1989**). *Brute Force Programming for Solving Double Dummy Bridge Problems*. [Heuristic Programming in AI 1](1st_Computer_Olympiad#Workshop "1st Computer Olympiad")
- [Donald Michie](Donald_Michie "Donald Michie") (**1989**). *Brute Force in Chess and Science*. [ICCA Journal, Vol. 12, No. 3](ICGA_Journal#12_3 "ICGA Journal")

## 1990 ...

- [Donald Michie](Donald_Michie "Donald Michie") (**1990**). *Brute Force in Chess and Science*. [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")
- [Alan Frank](index.php?title=Alan_Frank&action=edit&redlink=1 "Alan Frank (page does not exist)") (**1991**). *Brute Force Search in Games of Imperfect Information*. [Heuristic Programming in AI 2](2nd_Computer_Olympiad#Workshop "2nd Computer Olympiad")
- [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Paul Lu](Paul_Lu "Paul Lu"), [Duane Szafron](Duane_Szafron "Duane Szafron"), [Rob Lake](index.php?title=Rob_Lake&action=edit&redlink=1 "Rob Lake (page does not exist)") (**1993**). *A Re-examination of Brute-force Search*. Intelligent Games: Planning and Learning. (AAAI 1993 Report FS9302, Proccedings of the AAAI Fall Symposiuem, eds. S. Epstein and R. Levinson), pp. 51-58, AAAI Press, Menol Park, CA. ISBN 0-929-28051-2. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.34.4488&rep=rep1&type=pdf)
- [Miikka Maki-Uuro](index.php?title=Miikka_Maki-Uuro&action=edit&redlink=1 "Miikka Maki-Uuro (page does not exist)") (**1999**). *Limits to the brute force intelligence in computer chess*. Proc. 1999 HeCSE Winter School, (ed. [Tapio Elomaa](http://www.cs.tut.fi/~elomaa/)), Report No. C-1999-1, Department of Computer Science, [University of Helsinki](University_of_Helsinki "University of Helsinki") <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## Forum Posts

- [alpha-beta pruning != brute force](https://groups.google.com/d/msg/rec.games.chess/XQWb-ZjSsy0/MiYEhpjTT08J) by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 22, 1993 » [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Brute Force vs. Selective Search Re: Fernando & Jim](https://www.stmintz.com/ccc/index.php?id=40680) by Melvin S. Schwartz, [CCC](CCC "CCC"), January 24, 1999
- [Brute force base of good game. True or not true?](https://www.stmintz.com/ccc/index.php?id=67695) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), September 07, 1999
- [How make Fritz execute brute force search?](https://www.stmintz.com/ccc/index.php?id=121789) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), July 26, 2000 » [Fritz](Fritz "Fritz")

## External Links

- [Subject: brute-force vs. intuition in math & chess](http://www.mathematik.uni-bielefeld.de/%7Esillke/NEWS/brute-force) by [Bill Dubuque](https://en.wikipedia.org/wiki/Macsyma), August 1996
- [Middle Game: Computer Chess Comes of Age - Brute Force vs Knowledge](http://www.computerhistory.org/chess/main.php?sec=thm-42eeabf470432&sel=thm-42f15c52333a3) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Brute-force search from Wikipedia](https://en.wikipedia.org/wiki/Brute-force_search)
- [brute force - Wiktionary](http://en.wiktionary.org/wiki/brute_force)
- [Brute force attack from Wikipedia](https://en.wikipedia.org/wiki/Brute_force_attack)
- [Brute Force (1947 film) from Wikipedia](https://en.wikipedia.org/wiki/Brute_Force_%281947_film%29) <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Backtracking from Wikipedia](https://en.wikipedia.org/wiki/Backtracking)
- [Proof by exhaustion from Wikipedia](https://en.wikipedia.org/wiki/Proof_by_exhaustion)
- [Trial and error from Wikipedia](https://en.wikipedia.org/wiki/Trial_and_error)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Brute Force (1947 film) from Wikipedia](https://en.wikipedia.org/wiki/Brute_Force_%281947_film%29)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Paper is mentioned by [Richard Korf](Richard_Korf#JudeaPearl "Richard Korf") at [Judea Pearl Symposium](Judea_Pearl#Symposium "Judea Pearl"), 2010
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Quoted by [Hans Berliner](Hans_Berliner "Hans Berliner"), [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch") (**1985**). *A Study of Search Methods : The Effect of Constraint Satisfaction and Adventurousness*, [pdf](http://dli.iiit.ac.in/ijcai/IJCAI-85-VOL2/PDF/083.pdf), [pdf](http://dli.iiit.ac.in/ijcai/IJCAI-85-VOL2/PDF/083.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [University of Helsinki - Department of Computer Science - Annual Report 1999](http://www.cs.helsinki.fi/research/hallinto/TOIMINTARAPORTIT/1999/CS_Annual_Report_1999.pdf) (pdf)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Chess In The Cinema - Chess scenes from the movie Brute Force (Burt Lancaster)](http://www.chess-in-the-cinema.de/showfilm.php?filmfile=4708.txt&pfad=4049)

**[Up one Level](Search "Search")**

