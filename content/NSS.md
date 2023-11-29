---
title: NSS
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* NSS Chess Program**



[
**NSS Chess Program**, (Newell, Shaw, and Simon, also mentioned as Newell CP <a id="cite-note-2" href="#cite-ref-2">[2]</a>)  

an early chess program developed in the the late 1950s by [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University") researchers [Allen Newell](Allen_Newell "Allen Newell") and [Herbert Simon](Herbert_Simon "Herbert Simon"), and [Cliff Shaw](Cliff_Shaw "Cliff Shaw") at [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation). NSS ran on the [JOHNNIAC](https://en.wikipedia.org/wiki/JOHNNIAC) (short for **Joh**n v. **N**eumann **N**umerical **I**ntegrator and **A**utomatic **C**omputer), and was written in a high-level language developed by Shaw, known as [Information Processing Language](https://en.wikipedia.org/wiki/Information_Processing_Language) (IPL). It already used branch-and-bounds as an approximation to the [alpha-beta algorithm](Alpha-Beta "Alpha-Beta"). 



## Description


given by [Paul Rushton](Paul_Rushton "Paul Rushton") and [Tony Marsland](Tony_Marsland "Tony Marsland") in 1973 <a id="cite-note-4" href="#cite-ref-4">[4]</a> :




```C++A goal directed approach to the game was adopted by Newell, Shaw, and Simon. Features of the game were associated with goals, each of which required a [move generator](Move_Generation "Move Generation"), a [static evaluator](Evaluation "Evaluation"), and an analysis procedure. For ease of modification, each goal consisted of a separate procedure. In order to select which goals were relevant to a position, a preliminary analysis routine was invoked and the corresponding goals chosen were ordered by their suspected importance. This static set of goals controls the move generation process, including selection of variations, evaluation, and final choice.

```


```C++Move generators for goals were responsible for proposing moves relevant to a particular goal and finding positive reasons for making these. The generators did not suggest continuations. A proposed move had then to be valued by an analysis procedure which was concerned with acceptability of that move. Before a position can be assigned a value it must be dead with respect to all goals. If a position is not dead for a particular goal, moves are suggested by the corresponding move generator and the resultant positions are checked to see if they are quiescent for all goals. If not, the above procedure is repeated, constituting an analysis of variations, until a position is reached which can be evaluated. The final choice depends on an acceptance value and if a move receives a value greater than this threshold it is played, otherwise the best move found by the [alpha-beta](Alpha-Beta "Alpha-Beta") backing up procedure will be made. This program did not realize the state of development and use that the more recent programs have; however, hand simulation gave an indication, in the openings at least, that the program would make moves for reasons similar to those of chess players. 

```

## Quotes


[Bill Wall](index.php?title=Bill_Wall&action=edit&redlink=1 "Bill Wall (page does not exist)") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```C++In 1958, a chess program (NSS) beat a human player for the first time. The human player was a secretary who was taught how to play chess one hour before her game with the computer. The computer program was played on an IBM 704. The computer displayed a level of chess-playing expertise greater than an adult human could gain from one hour of chess instruction. 

```

## See also


* [Mater](Mater "Mater")


## Publications


* [Allen Newell](Allen_Newell "Allen Newell"), [Cliff Shaw](Cliff_Shaw "Cliff Shaw"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1958**). *Chess Playing Programs and the Problem of Complexity*. IBM Journal of Research and Development, Vol. 4, No. 2, pp. 320-335. Reprinted (1963) in [Computers and Thought](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=6685) (eds. [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") and [Julian Feldman](Mathematician#JulianFeldman "Mathematician")), pp. 39-70. McGraw-Hill, New York, N.Y. [pdf](http://aitopics.org/sites/default/files/classic/Feigenbaum_Feldman/C&T-Newll-Shaw-Simon.pdf)
* [Allen Newell](Allen_Newell "Allen Newell"), [Cliff Shaw](Cliff_Shaw "Cliff Shaw"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1959**). *Report on a general problem-solving program*. Proceedings of the International Conference on Information Processing, pp. 256-264 <a id="cite-note-6" href="#cite-ref-6">[6]</a>
* [Walter R. Reitman](Walter_R._Reitman "Walter R. Reitman") (**1967**). *[Modeling the formation and use of concepts, percepts, and rules](http://projecteuclid.org/DPubS?service=UI&version=1.0&verb=Display&handle=euclid.bsmsp/1200513787)*. [Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Volume 4: Biology and Problems of Health](http://projecteuclid.org/DPubS?service=UI&version=1.0&verb=Display&handle=euclid.bsmsp/1200513779), [pdf](http://projecteuclid.org/DPubS/Repository/1.0/Disseminate?view=body&id=pdf_1&handle=euclid.bsmsp/1200513787) from [Project Euclid - mathematics and statistics resources online](http://projecteuclid.org/DPubS?Service=UI&version=1.0&verb=Display&handle=euclid)
* [Paul Rushton](Paul_Rushton "Paul Rushton"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1973**). *Current Chess Programs: A Summary of their Potential and Limitations*. INFOR Journal of the Canadian Information Processing Society Vol. 11, No. 1, [pdf](http://webdocs.cs.ualberta.ca/%7Etony/OldPapers/Rushton-Marsland-Feb73.pdf)


## External Links


* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-7" href="#cite-ref-7">[7]</a>
* [JOHNNIAC from Wikipedia](https://en.wikipedia.org/wiki/JOHNNIAC)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Johnniac computer, [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), California, by Andrew Lih, [JOHNNIAC from Wikipedia](https://en.wikipedia.org/wiki/JOHNNIAC)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Aritificial Intelligence pioneers Allen Newell (right) and Herbert Simon 1958](http://www.computerhistory.org/chess/full_record.php?iid=stl-431e1a07cf7a1) Courtesy of [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Paul Rushton](Paul_Rushton "Paul Rushton"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1973**). *Current Chess Programs: A Summary of their Potential and Limitations*. INFOR Journal of the Canadian Information Processing Society Vol. 11, No. 1, [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Rushton-Marsland-Feb73.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Computer Chess History](http://www.oocities.org/siliconvalley/lab/7378/comphis.htm) by [Bill Wall](index.php?title=Bill_Wall&action=edit&redlink=1 "Bill Wall (page does not exist)")
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [General Problem Solver from Wikipedia](https://en.wikipedia.org/wiki/General_Problem_Solver)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one Level](Engines "Engines")**







 
