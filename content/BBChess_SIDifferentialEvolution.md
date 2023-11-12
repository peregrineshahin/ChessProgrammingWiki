---
title: BBChess SIDifferentialEvolution
---
**[Home](Home "Home") * [Engines](Engines "Engines") * BBChess (SI)**

**BBChess**,

a free [open source engine](Category:Open_Source "Category:Open Source") licensed under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), written in [ANSI C](C "C") by [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković") starting in 2005. BBChess is [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible and can be compiled for [Linux](Linux "Linux") and [Windows](Windows "Windows").
It performs a [parallel search](Parallel_Search "Parallel Search") using [threads](Thread "Thread"), [PVS](Principal_Variation_Search "Principal Variation Search"), and determines [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") with [magic bitboards](Magic_Bitboards "Magic Bitboards").

## Contents

- [1 Differential Evolution](#differential-evolution)
- [2 Namesake](#namesake)
- [3 See also](#see-also)
- [4 Publications](#publications)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
  - [6.1 Chess Engine](#chess-engine)
  - [6.2 Misc](#misc)
- [7 References](#references)

## Differential Evolution

BBChess' was further object of research in [genetic programming](Genetic_Programming "Genetic Programming") at *Computer Architecture and Languages Laboratory* <a id="cite-note-1" href="#cite-ref-1">[1]</a>, Institute of Computer Science at [University of Maribor](University_of_Maribor "University of Maribor"), its [evaluation](Evaluation "Evaluation") was [tuned](Automated_Tuning "Automated Tuning") by [differential evolution](https://en.wikipedia.org/wiki/Differential_evolution) (**DE**), which was also topic of Bošković's Ph.D. thesis <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```C++
The DE algorithm employs [mutation](https://en.wikipedia.org/wiki/Mutation) and [cross-over operations](https://en.wikipedia.org/wiki/Crossover_%28genetic_algorithm%29) to generate new individuals and [selection operation](https://en.wikipedia.org/wiki/Selection_%28genetic_algorithm%29) to select individuals that will survive into next generation. Before selection operation is employed, individuals have to be evaluated. In our case individuals are evaluated according to the games they have played. Therefore individuals play a specific number of games in each generation and individuals with greater efficiency survive into the next generation... 

```

```C++
With the proposed tuning approach, we tuned the chess evaluation function of BBChess chess program. Tuning was done with and without expert knowledge. When we tuned the parameters without expert knowledge, because the search space was huge, we tuned only a few parameters. After 500 generations of the evolutionary process, the value of parameters convergence to the values that relationship were approximately equal as known from the chess theory. When we tuned the parameter values with expert knowledge, the tuning intervals of parameter values were set around the approximate values and the number of tuned parameters was 190. The obtained results show that, our approach was successful. 

```

## Namesake

- [BBchess](BBchess "BBchess") by [Bernard Brioit](Bernard_Brioit "Bernard Brioit")

## See also

- [MinkoChess](MinkoChess "MinkoChess")

## Publications

- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2005**). *[The representation of chess game](https://ieeexplore.ieee.org/document/1491153)*. 27th International Conference on Information Technology Interfaces
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2006**). *[A Differential Evolution for the Tuning of a Chess Evaluation Function](https://ieeexplore.ieee.org/document/1688532)*. [IEEE Congress on Evolutionary Computation](IEEE "IEEE")
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2007**). *Uglaševanje šahovskega programa BBChess z uporabo algoritma diferencialne evolucije*. Zbornik šestnajste mednarodne Elektrotehniške in računalniške konference ERK (Slovenian)
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Aleš Zamuda](Ale%C5%A1_Zamuda "Aleš Zamuda"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2008**). *[An Adaptive Differential Evolution Algorithm with Opposition-Based Mechanisms, Applied to the Tuning of a Chess Program](https://link.springer.com/chapter/10.1007%2F978-3-540-68830-3_12)*. [Advances in Differential Evolution](https://link.springer.com/book/10.1007/978-3-540-68830-3), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković") (**2010**). *[Differential Evolution for the Tuning of a Chess Evaluation Function](http://labraj.uni-mb.si/en/PhD_Thesis_Defence_%28Borko_Bo%C5%A1kovi%C4%87%29)*. Ph.D. thesis, [University of Maribor](University_of_Maribor "University of Maribor")
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Janez Brest](Janez_Brest "Janez Brest") (**2011**). *[Tuning Chess Evaluation Function Parameters using Differential Evolution](http://www.informatica.si/index.php/informatica/article/view/353)*. Informatica, Vol. 35, No. 2
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Janez Brest](Janez_Brest "Janez Brest"), [Aleš Zamuda](Ale%C5%A1_Zamuda "Aleš Zamuda"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2011**). *[History mechanism supported differential evolution for chess evaluation function tuning](https://dl.acm.org/citation.cfm?id=1966601)*. [Soft Computing](http://www.springer.com/engineering/computational+intelligence+and+complexity/journal/500), Vol. 15, No. 4

## Forum Posts

- [BBChess 1.2 : 2296](http://www.talkchess.com/forum/viewtopic.php?t=16600) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), September 21, 2007
- [BBChess 1.2a : 2287](http://www.talkchess.com/forum/viewtopic.php?t=17057) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), October 10, 2007
- [BBChess 1.3a : 2309](http://www.talkchess.com/forum/viewtopic.php?t=19959) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), March 02, 2008
- [BBChess 1.3b : 2384](http://www.talkchess.com/forum/viewtopic.php?t=26078) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), Januray 17, 2009

## External Links

## Chess Engine

- [Chess program BBChess - Computer Architecture and Languages Laboratory](http://labraj.uni-mb.si/en/Chess_program_BBChess), [University of Maribor](University_of_Maribor "University of Maribor")
- [BBChess](http://computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=BBChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")
- [BBChess 1.3b 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=BBChess%201.3b%2064-bit#BBChess_1_3b_64-bit) in [CCRL 40/4](CCRL "CCRL")

## Misc

- [Black Stone Raiders](Category:Black_Stone_Raiders "Category:Black Stone Raiders") - live at [Festival Lent](https://en.wikipedia.org/wiki/Lent_Festival), [Maribor](https://en.wikipedia.org/wiki/Maribor), June 26, 2011, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Jean-Paul Bourelly](https://en.wikipedia.org/wiki/Jean-Paul_Bourelly), [Darryl Jones](Category:Darryl_Jones "Category:Darryl Jones"), [Will Calhoun](https://en.wikipedia.org/wiki/Will_Calhoun)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Computer Architecture and Languages Laboratory](http://labraj.uni-mb.si/en/General_Information)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković") (**2010**). *[Differential Evolution for the Tuning of a Chess Evaluation Function](http://labraj.uni-mb.si/en/PhD_Thesis_Defence_%28Borko_Bo%C5%A1kovi%C4%87%29)*. Ph.D. thesis, [University of Maribor](University_of_Maribor "University of Maribor")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Janez Brest](Janez_Brest "Janez Brest") (**2011**). *[Tuning Chess Evaluation Function Parameters using Differential Evolution](http://www.informatica.si/index.php/informatica/article/view/353)*. Informatica, Vol. 35, No. 2

**[Up one Level](Engines "Engines")**

