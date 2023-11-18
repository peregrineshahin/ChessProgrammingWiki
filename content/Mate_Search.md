---
title: Mate Search
---
**[Home](Home "Home") \* [Search](Search "Search") \* Mate Search**


A **Mate Search** is used in some engines to find a forced [checkmate](Checkmate "Checkmate") in a certain number of moves. After finding a forced line to a mate, a mate search is used to check for any other forced mates in a lesser number of moves, which might have been cut off by some of the commonly used [pruning](Pruning "Pruning") methods in [minimax search](Minimax "Minimax"). Some programs are built exclusively to find mates, such as [Chest](Chest "Chest"). While these programs are similar to normal engines, they are not typically considered engines because they cannot play a full game of chess <a id="cite-note-1" href="#cite-ref-1">[1]</a> .
The mate finding procedure usually works like an ordinary [depth first search](Depth-First "Depth-First"). The main difference lies in the absence of the evaluation function. Mate finders only look for forced mates, but not for any material/positional advances. So any other evaluations than a mate-inspection are useless.



### Backward Pruning


[Pruning](Pruning "Pruning") techniques that only discard nodes which wouldn't have influenced the final result anyway. Similar to standard chess engines mate searchers also use mate-distance-pruning. In its basic form all moves are pruned once a depth is reached, if another forced line has been found that has given mate at the same depth. Extending on this [Heiner Marxen](Heiner_Marxen "Heiner Marxen") coined the term Fatal-Anti-Check. If in a line the side to move must be mated in the next move, prune if it can check the attacker and so that there is no way to avoid the check and mate the defender at the same time. This idea is comparable to some sound variation of [futility pruning](Futility_Pruning "Futility Pruning").



### Forward Pruning


Mate searchers don't rely on probability based forward pruning techniques known from standard chess engines. As mate searchers are often used to solve chess problems that contain sacrifices, moves where these pruning techniques fail. [Chest](Chest "Chest") offers the user to search checking-moves only, prune if the defender has more than n moves, prune if the defending king has more than n moves or prune if more than n opponent pieces were able to move. Very stringent parameters can lead to solutions very quickly and can be extended gradually.



## Interior Nodes Recognizers


Additionally to pruning technics, [interior node recognizers](Interior_Node_Recognizer "Interior Node Recognizer") are often used to speed up search. Particularly useful for chess problems are:



* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance")
* [Blockage Detection](Blockage_Detection "Blockage Detection")
* [Perpetual Check Detection](Check#Perpetual "Check")


## See also


* [Checkmate](Checkmate "Checkmate")
* [Chest](Chest "Chest")
* [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance")
* [Mate-in-two](Mate-in-two "Mate-in-two")
* [Mater](Mater "Mater")
* [Popeye](Popeye "Popeye")
* [Proof-Number Search](Proof-Number_Search "Proof-Number Search")


## Publications


* [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") (**1952**). *Robot Chess*. Research, Vol. 6, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") » [Mate-in-two](Mate-in-two "Mate-in-two")
* [Gerd Veenker](Gerd_Veenker "Gerd Veenker") (**1965**). *[Ein Programm zur Lösung von Schachaufgaben](http://www.degruyter.com/view/j/itit.1965.7.issue-1-6/itit.1965.7.16.25/itit.1965.7.16.25.xml)*. [Elektronische Rechenanlagen, Vol. 7](http://dblp.uni-trier.de/db/journals/it/it7.html), No. 1 (German)
* [George W. Baylor](George_Baylor "George Baylor") (**1965**). *[Report on a Mating Combinations Program](http://www.dtic.mil/docs/citations/AD0619018)*. SDC Paper, No. SP-2150, System Development Corporation, Santa Monica, Calif. » [Mater](Mater "Mater")
* [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. [AFIPS](https://en.wikipedia.org/wiki/American_Federation_of_Information_Processing_Societies) [Joint Computer Conferences](https://en.wikipedia.org/wiki/Joint_Computer_Conference), reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [George W. Baylor](George_Baylor "George Baylor") (**1966**). *A Computer Model of Checkmating Behaviour in Chess*. in [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot"), [Walter R. Reitman](Walter_R._Reitman "Walter R. Reitman") (eds.) (**1966**). *Heuristic Processes in Thinking*. International Congress of Psychology, [Nauka](https://en.wikipedia.org/wiki/Nauka_%28publisher%29), [Moscow](https://en.wikipedia.org/wiki/Moscow)
* [Max Bramer](Max_Bramer "Max Bramer") (**1982**). *Finding Checkmates*. [Computer & Video Games](https://en.wikipedia.org/wiki/Computer_and_Video_Games), [Spring 1982](http://www.chesscomputeruk.com/html/publication_archive_1982.html), [pdf](http://www.chesscomputeruk.com/Computer___Video_Games_Spring_1982.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters") » [Mater](Mater "Mater")
* [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Victor Allis](Victor_Allis "Victor Allis"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1994**). *How to Mate: Applying Proof-Number Search*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), reprint as [Mate in 38: Applying Proof-Number Search](http://www.top-5000.nl/ps/Mate%20in%2038-%20applying%20proof%20number%20search%20to%20chess.pdf) from [Ed Schroder's](Ed_Schroder "Ed Schroder") [Programmer's Stuff site](http://www.top-5000.nl/prostuff.htm)
* [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2004**). *Realization of the Chess Mate Solver Application*. [Yugoslav Journal of Operations Research, Volume 14, Number 2](http://www.doiserbia.nb.rs/issue.aspx?issueid=138), [pdf](http://www.doiserbia.nbs.bg.ac.yu/img/doi/0354-0243/2004/0354-02430402273V.pdf)
* [Ami Hauptman](index.php?title=Ami_Hauptman&action=edit&redlink=1 "Ami Hauptman (page does not exist)"), [Moshe Sipper](index.php?title=Moshe_Sipper&action=edit&redlink=1 "Moshe Sipper (page does not exist)") (**2007**). *Evolution of an Efficient Search Algorithm for the Mate-In-N Problem in Chess*. [EuroGP 2007](http://www.informatik.uni-trier.de/~%20LEY/db/conf/eurogp/eurogp2007.html), [pdf](http://www.cs.bgu.ac.il/~sipper/papabs/gpsearch.pdf)


## Forum Posts


* [Questions about Mate Searching](https://www.stmintz.com/ccc/index.php?id=130376) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), September 23, 2000
* [Dedicated mate finders](http://www.talkchess.com/forum/viewtopic.php?t=57076) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 25, 2015
* [Why do engines lack mate solving?](http://www.talkchess.com/forum/viewtopic.php?t=61731) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), October 15, 2016


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. [AFIPS](https://en.wikipedia.org/wiki/American_Federation_of_Information_Processing_Societies) [Joint Computer Conferences](https://en.wikipedia.org/wiki/Joint_Computer_Conference), reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")

**[Up one level](Search "Search")**







 
