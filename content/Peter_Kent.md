---
title: Peter Kent
---
**[Home](Home "Home") \* [People](People "People") \* Peter Kent**



 [](http://www.chilton-computing.org.uk/gallery/ral76/slide8.htm) Peter Kent <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Peter Kent**,  

a British computer scientist and programmer from [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory"), [Chilton, Oxfordshire](https://en.wikipedia.org/wiki/Chilton,_Oxfordshire). In 1969 Peter started to work on [Alex Bell's](Alex_Bell "Alex Bell") [Atlas](Atlas "Atlas") program, which was a reproduction of [Nils Barricelli's](Nils_Barricelli "Nils Barricelli") chess program in [Algol](Algol "Algol"). It was later rewritten to [PL/1](index.php?title=PL_1&action=edit&redlink=1 "PL 1 (page does not exist)") with the help of [John Birmingham](John_Birmingham "John Birmingham"), and in 1973 [Alex Bell](Alex_Bell "Alex Bell") joined the team to develop the chess playing program **M**inimax **a**lgorithm Te**ster**, short [Master](Master "Master"), which competed the first three [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, from 1975 with Kent <a id="cite-note-3" href="#cite-ref-3">[3]</a> and Birmingham as sole authors. Both authors further improved Master, and as scientists, talked about their secrets in tree searching techniques and [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance") during the first two [Advances in Computer Chess](Conferences "Conferences") conferences, [published](Peter_Kent#Publications "Peter Kent") as Proceedings by [Mike Clarke](Mike_Clarke "Mike Clarke"), and reprinted in [David Levy's](David_Levy "David Levy") [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"). 



### Contents


* [1 Quotes](#quotes)
* [2 Selected Publications](#selected-publications)
* [3 External Links](#external-links)
* [4 References](#references)






[Alex Bell](Alex_Bell "Alex Bell") about his collaboration with Peter Kent <a id="cite-note-4" href="#cite-ref-4">[4]</a><a id="cite-note-5" href="#cite-ref-5">[5]</a>:




```C++
The [first Computer Chess Conference](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1") took place at the Atlas Computer Laboratory in May 1973. Apart from inviting the speakers it was also obvious that the conference would have to demonstrate a chess program in some form and it is at this point in time that MASTER really got started.

```


```C++
One of the programmers at Atlas, Peter Kent, had taken over the program and modified it to maximise the number of squares controlled. This, combined with a few other improvements, had produced a much stronger program - as Peter later wrote:

```


```C++
"The program captured if you gave it the chance, moved a piece if threatened, but still generally displayed no imagination. The computer operators used to play the program at night and write sarcastic comments on the output after winning in 15 or so moves. I then decided to try building some sort of strategy into the program by giving the squares different values. Initially the ratios were 3 for the central four squares, 2 for the next ring of twelve and 1 for all the remainder. The next night the best player among the operators tried playing the program expecting to win with his usual ease. The program opened with the rather aggressive if unsound Blackmar gambit. It then developed all its pieces fairly rapidly, castled queen side, doubled its rooks on the open queen file and stormed down the board using both rooks and the queen, ending the game with a mate by its queen on the 8th rank and a rook on the 7th. The comment on the output the next morning was "well it seems to work now".

```


```C++
From then on the operators played more carefully and revealed that the program, because it still only had a shallow search, still suffered badly from horizon effect. Nevertheless it did win a few more games and it was decided to use it as the demonstration program at the conference.

```


```C++
Well it didn't win a game, hardly surprising since it was up against much stronger players. Nevertheless several people noticed that the program was usually achieving its main aim of controlling the centre squares; in other words, it was quite successful in doing what little it had been told to do but, from then on, it had no further direction other than a vague idea of advancing its own pawns and blocking its opponent's. Peter improved its sense of purpose by making the program, as the game progressed, put less emphasis on controlling the fixed centre squares and more and more emphasis on controlling the squares around the enemy king, wherever he may be. Because of mini-max this also caused the program to protect the squares around its own king far more effectively. 

```


```C++
This change from centre control to actively hunting the opponent's king was very noticeable. At this point a very energetic programmer from Harwell Atomic Energy Research Establishment, [John Birmingham](John_Birmingham "John Birmingham"), became interested. He translated the program, plus all the new improvements, into PL/l in about 6 weeks of his spare time and also extended the depth of the search. I would say at this point that England at last had a program comparable to MACHACK and we ambitiously christened it MASTER-Minimax Algorithm teSTER; if nothing else we had the patent on a good name.

```


```C++
Alex returned to the Chilton site (Rutherford Laboratory) in 1973 and joined forces with Peter Kent and John Birmingham from Harwell creating a chess program called MASTER. The first Computer Chess Conference took place at the Atlas Laboratory in May 1973. In 1974, MASTER competed in the first [IFIP](IFIP "IFIP") [World Computer Chess Championship](WCCC_1974 "WCCC 1974") in Stockholm in 1974 winning 2, losing 2 and coming about 5th out of 13 programs using 2 hours of time of the Rutherford's [360/195](IBM_360 "IBM 360").

```


```C++
On the last night, having won two easy games, MASTER again met a tough opponent, [RIBBIT](Ribbit "Ribbit") from Canada. At one point in this game Peter Kent, who was in Stockholm, told us that if MASTER won then there was a chance that it could play off for the championship but, unfortunately, [TECH 2](Tech "Tech") had been a costly game in sabbatical time and MASTER was set to play very quickly, missed its chances and gave away a piece. The position at move 54 was (Fig. 10) and Peter Kent asked me if MASTER was saying it wanted to resign.

```

 

|  |
| --- |
|                                                                                                                    ♗                ♔ ♘   ♙        ♚        |


 8/8/8/B7/8/1K1N3P/8/k7 w - - 1 54

```C++
During the tournament we had not been linked directly to Peter Kent in Stockholm but had been relaying our moves algebraically through London where another chess program was also competing in the tournament. This relay had caused us to use a voice code for the moves (ABLE, BAKER, CHARLIE, DOG, EASY, FOX, GEORGE, HOTEL) and, oddly enough, we never sent or received a bad move.

```





## Selected Publications


<a id="cite-note-6" href="#cite-ref-6">[6]</a>



* Peter Kent (**1973**). *A Simple Working Model*. in [Alex Bell](Alex_Bell "Alex Bell") (ed.) (**1973**). *Computer Chess*. Proceedings [May 1973 Meeting on chess playing by computer](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1"). Science Research Council, [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory"), pp. 15-27
* [John Birmingham](John_Birmingham "John Birmingham"), Peter Kent (**1977**). *Tree-searching and tree-pruning techniques*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1"), (Ed. [M.R.B. Clarke](Mike_Clarke "Mike Clarke")), pp. 89–107. Edinburgh University Press, Edinburgh. ISBN 0-852-24292-1. reprinted in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") by [D.N.L. Levy](David_Levy "David Levy") (ed.), pp. 123-128
* [John Birmingham](John_Birmingham "John Birmingham"), Peter Kent <a id="cite-note-7" href="#cite-ref-7">[7]</a> (**1980**). *Mate at a Glance.* [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2"), (Ed. [M.R.B. Clarke](Mike_Clarke "Mike Clarke")), pp. 122–130. Edinburgh University Press, Edinburgh. ISBN 0-85224-377-4. reprinted in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") by [D.N.L. Levy](David_Levy "David Levy") (ed.), pp. 258-265
* Peter Kent (**1980**). *The MASTER Chess Program*. [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2") (ed. [M.R.B. Clarke](Mike_Clarke "Mike Clarke")), pp. 131-142. Edinburgh University Press, Edinburgh. ISBN 0-85224-377-4.


## External Links


* [Peter Kent's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/person.php?id=439)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Image clipped from [Chilton home :: Gallery home :: Slide 8: 18.05.78 to 13.03.79](http://www.chilton-computing.org.uk/gallery/ral76/slide8.htm)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Master's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=46)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Peter Kent's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/person.php?id=439)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Alex Bell](Alex_Bell "Alex Bell") (**1978**). *[MASTER at IFIPS](http://www.chilton-computing.org.uk/acl/applications/cocoa/p008.htm)*. Excerpt from: The Machine Plays Chess? from [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory"), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Alex Bell](http://www.chilton-computing.org.uk/acl/associates/permanent/bell.htm) from [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory"), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [ICGA Reference Database](ICGA_Journal#RefDB "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> In the ICGA Database [John Birmingham](John_Birmingham "John Birmingham") is mentioned as sole author

**[Up one level](People "People")**







 
