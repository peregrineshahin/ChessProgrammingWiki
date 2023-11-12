---
title: The Bernstein Chess Program
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* The Bernstein Chess Program**



 [](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f6482e6) [Alex Bernstein](Alex_Bernstein "Alex Bernstein"), [IBM 704](IBM_704 "IBM 704") console <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**The Bernstein Chess Program**,  

was the first complete chess program, developed around [1957](Timeline#1957 "Timeline") at [Service Bureau Corporation](https://en.wikipedia.org/wiki/Service_Bureau_Corporation), [Madison](https://en.wikipedia.org/wiki/Madison_Avenue) & [59th Street](https://en.wikipedia.org/wiki/59th_Street_%28Manhattan%29), [Manhattan](https://en.wikipedia.org/wiki/Manhattan), [New York City](https://en.wikipedia.org/wiki/New_York_City) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, by chess player and programmer at [IBM](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)"), [Alex Bernstein](Alex_Bernstein "Alex Bernstein") with his colleagues [Michael de V. Roberts](Michael_de_V._Roberts "Michael de V. Roberts"), [Timothy Arbuckle](Timothy_Arbuckle "Timothy Arbuckle") and [Martin Belsky](Martin_Belsky "Martin Belsky"), supported by chess advisor [Arthur Bisguier](https://en.wikipedia.org/wiki/Arthur_Bisguier) <a id="cite-note-3" href="#cite-ref-3">[3]</a>, who became IBM employee at that time and in 1957 [international chess grandmaster](https://en.wikipedia.org/wiki/International_Grandmaster), and supervised by [Nathaniel Rochester](Nathaniel_Rochester "Nathaniel Rochester") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck), who was married to [Joseph F. Traub](Mathematician#JFTraub "Mathematician"), interviewed Alex Bernstein as published with several details given on the development of the program in her seminal book *[Machines Who Think](Artificial_Intelligence#MachinesWhoThink "Artificial Intelligence")* <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



### McCorduck


Quotes by [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck) from *[Machines Who Think](Artificial_Intelligence#MachinesWhoThink "Artificial Intelligence")* <a id="cite-note-6" href="#cite-ref-6">[6]</a>




```C++
Bernstein drew upon not only his own experience with chess, but began to study [Modern Chess Openings](https://en.wikipedia.org/wiki/Modern_Chess_Openings), which came out then every two years, and spent six months going through some five hundred chess openings. He assigned scores to various positions, scores that depended not only on the pieces retained, but also on [area control](Square_Control "Square Control") of the board and [mobility](Mobility "Mobility"). He also developed a fourth measure, what he called a “[greens area](King_Pattern "King Pattern")” around the king, meaning that the more squares outward from the king controlled by his own side the better. But after six months of this he gave it up. He couldn’t make any sense out of it.

```


```C++
At this time, Bernstein was unaware of [Shannon’s seminal papers](Claude_Shannon "Claude Shannon"), and did not know that chess had caught the interests of a group at [Los Alamos](Los_Alamos_National_Laboratory "Los Alamos National Laboratory"), including [J. Kister](James_Kister "James Kister"), [P. Stein](Paul_Stein "Paul Stein"), [S. Ulam](Stanislaw_Ulam "Stanislaw Ulam"), [W. Walden](William_Walden "William Walden"), and [M. Wells](Mark_Wells "Mark Wells"), who were working on a limited [6x6 board](MANIAC_I "MANIAC I"), rather than the regulation 8x8. Nor did he know that [Allen Newell](Allen_Newell "Allen Newell"), [J. C. Shaw](Cliff_Shaw "Cliff Shaw"), and [Herbert Simon](Herbert_Simon "Herbert Simon") together, and [John McCarthy](John_McCarthy "John McCarthy") independently, were also pondering chess-playing machines. Alex Bernstein only knew that the problem was hot ... 

```


```C++
It was now that Bernstein became aware of [Turing’s](Alan_Turing "Alan Turing") work and read at least one of Shannon’s papers. When he finally began to see how he might codify some of the principles he felt were essential, he telephoned [Claude Shannon](Claude_Shannon "Claude Shannon") at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"). “I went up to MIT and spent a day or two with him, telling him what I was planning to do, and he said he thought it was intelligent, and a good way of proceeding. Essentially I felt I’d received his blessings, which was pleasant.”

```


```C++
Bernstein also mentioned that he was working on the problem to [Dr. Edward Lasker](https://en.wikipedia.org/wiki/Edward_Lasker), a well-known chess writer, who introduced him to [Stanislaw Ulam](Stanislaw_Ulam "Stanislaw Ulam") of the Los Alamos group. Bernstein had the advantage that the Los Alamos group didn’t have, of a machine with a large amount of memory, although the four thousand words of memory the [IBM 704](IBM_704 "IBM 704") had to begin with were insufficient for Bernstein’s program in the end. The 704’s memory was to have doubled by the time Bernstein finished his program, and he still came within two hundred words of overflowing memory.

```


```C++
So Bernstein’s chess program selected what seemed to be the likeliest fruitful moves, and these it examined in considerable depth, comparing one to another among a number of dimensions. The program contained a large data base, which allowed it to examine any particular piece or square at any time. In descending order of importance, the program asked such questions as, Is the [king](King "King") in [check](Check "Check")? If the king is in check, there is nothing else to do. Is the king in [double check](Check#DoubleCheck "Check")? If he is, merely to capture one piece that threatens the king will be insufficient; the king must be moved. The next question had to do with [material](Material "Material"): is there any to be gained, or any in danger of [capture](Captures "Captures")? And clearly it is more important to rescue or capture a rook than to rescue or capture a pawn, and this was factored into the program. 

```

### McCarthy


As mentioned by [John McCarthy](John_McCarthy "John McCarthy") <a id="cite-note-7" href="#cite-ref-7">[7]</a>, the Bernstein Chess Program under construction was presented at the [1956 Dartmouth workshop](https://en.wikipedia.org/wiki/Dartmouth_workshop):




```C++
Alex Bernstein of IBM presented his chess program under construction. My reaction was to invent and recommend to him [alpha-beta](Alpha-Beta "Alpha-Beta") pruning. He was unconvinced. 

```

## Shannon Type B


The Bernstein Chess Program was the prototype of a selective forward pruning, [Shannon Type B](Type_B_Strategy "Type B Strategy") program. On an [IBM 704](IBM_704 "IBM 704"), one of the last vacuum tube computers, it searched four [plies](Ply "Ply") [minimax](Minimax "Minimax") in around 8 minutes, considering seven most plausible moves from each position and [evaluated](Evaluation "Evaluation") [material](Material "Material"), [mobility](Mobility "Mobility"), [area control](Square_Control "Square Control") and [king defense](King_Safety "King Safety") <a id="cite-note-8" href="#cite-ref-8">[8]</a>. 



## Publications


<a id="cite-note-9" href="#cite-ref-9">[9]</a>



* [Alex Bernstein](Alex_Bernstein "Alex Bernstein"), [Michael de V. Roberts](Michael_de_V._Roberts "Michael de V. Roberts") (**1958**). *[Computer vs. Chess-Player](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f690f16)*. [Scientific American](Scientific_American "Scientific American"), Vol. 198, reprinted **1988** in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Alex Bernstein](Alex_Bernstein "Alex Bernstein")  (**1958**). *[A Chess Playing Program for the IBM 704](http://www.computerhistory.org/chess/full_record.php?iid=doc-4316153963418)*. [Chess Review](https://en.wikipedia.org/wiki/Chess_Review), July 1958
* [Alex Bernstein](Alex_Bernstein "Alex Bernstein"), [Michael de V. Roberts](Michael_de_V._Roberts "Michael de V. Roberts"), [Timothy Arbuckle](Timothy_Arbuckle "Timothy Arbuckle"), [Martin Belsky](Martin_Belsky "Martin Belsky") (**1958**). *[A chess playing program for the IBM 704](https://www.computerhistory.org/chess/doc-431e18a41d415/)*. Proceedings of the 1958 Western Joint Computer Conference
* [Fritz Leiber](https://en.wikipedia.org/wiki/Fritz_Leiber) (**1962**). *[The 64-Square Madhouse](https://en.wikipedia.org/wiki/Fritz_Leiber_bibliography#Short_stories)*. [Worlds of If](http://www.unz.org/Pub/WorldsIfSF-1962may-00064) <a id="cite-note-10" href="#cite-ref-10">[10]</a>
* [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck) (**1979**). *Machines Who Think*. [W. H. Freeman](https://en.wikipedia.org/wiki/W._H._Freeman_and_Company)
* [David Levy](David_Levy "David Levy"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1982**). *[All About Chess and Computers](http://link.springer.com/book/10.1007/978-3-642-85538-2)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck) (**2004**). *[Machines Who Think: A Personal Inquiry into the History and Prospects of Artificial Intelligence](Artificial_Intelligence#MachinesWhoThink "Artificial Intelligence")*. [A. K. Peters](https://en.wikipedia.org/wiki/A_K_Peters) (25th anniversary edition)


## External Links


* [Alex Bernstein](https://www.computerhistory.org/chess/search/?q=Alex+Bernstein) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
 * [Photos](https://www.gettyimages.de/fotos/ibm-704?editorialproducts=timelife&family=editorial&phrase=IBM%20704&page=1&recency=anydate&suppressfamilycorrection=true) with [Edward Lasker](https://en.wikipedia.org/wiki/Edward_Lasker) by [Andreas Feininger](https://en.wikipedia.org/wiki/Andreas_Feininger), [Getty Images](https://en.wikipedia.org/wiki/Getty_Images) » [Quote from Machines Who Think](IBM_704#QuoteMachinesWhoThink "IBM 704") 
* [The History of Computer Chess - Part 3 - Alex Bernstein](https://www.chess.com/blog/Ginger_GM/the-history-of-computer-chess-part-3-alex-bernstein) by [Simon Williams](https://en.wikipedia.org/wiki/Simon_Williams_(chess_player)), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), August 31, 2019
* [The History of Computer Chess - Part 4 - Alex Bernstein continued...](https://www.chess.com/blog/Ginger_GM/the-history-of-computer-chess-part-4-alex-bernstein-continued) by [Simon Williams](https://en.wikipedia.org/wiki/Simon_Williams_(chess_player)), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), September 28, 2019
* [Runner-Up - The New Yorker - November 29, 1958](https://www.newyorker.com/magazine/1958/11/29/runner-up-4)
* Alex Bernstein: *juega al ajedrez con un* IBM 704 (Thinking Machines), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [IBM programmer Alex Bernstein](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f6482e6) 1958 Courtesy of [IBM](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)") Archives from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Runner-Up - The New Yorker - November 29, 1958](http://www.newyorker.com/magazine/1958/11/29/runner-up-4)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Arthur Bisguier from Wikipedia.de](http://de.wikipedia.org/wiki/Arthur_Bisguier) (German)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Nathaniel Rochester (computer scientist) from Wikipedia](https://en.wikipedia.org/wiki/Nathaniel_Rochester_%28computer_scientist%29)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: The mystery of Alex Bernstein](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70939&start=17) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), June 09, 2019
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck) (**2004**). *[Machines Who Think: A Personal Inquiry into the History and Prospects of Artificial Intelligence](Artificial_Intelligence#MachinesWhoThink "Artificial Intelligence")*. [A. K. Peters](https://en.wikipedia.org/wiki/A_K_Peters) (25th anniversary edition), pp. 182-185
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [The Dartmouth Workshop--as planned and as it happened](http://www-formal.stanford.edu/jmc/slides/dartmouth/dartmouth/node1.html)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Alex Bernstein](Alex_Bernstein "Alex Bernstein"), [Michael de V. Roberts](Michael_de_V._Roberts "Michael de V. Roberts") (**1958**). *[Computer vs. Chess-Player](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f690f16)*. [Scientific American](Scientific_American "Scientific American"), Vol. 198, reprinted **1988** in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> hosted by [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Fritz Leiber's "The 64-Square Madhouse"](http://www.talkchess.com/forum/viewtopic.php?t=49858) by [Ian Osgood](Ian_Osgood "Ian Osgood"), [CCC](CCC "CCC"), October 28, 2013

**[Up one Level](Engines "Engines")**







 
