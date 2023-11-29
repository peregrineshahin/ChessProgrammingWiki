---
title: Mephisto HMM1
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Mephisto I-III**



 [](http://www.schachcomputer.at/mep1.htm) Mephisto I <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Mephisto**,  

a family of [dedicated chess computers](Dedicated_Chess_Computers "Dedicated Chess Computers"), produced and traded by [Hegener & Glaser](Hegener_%26_Glaser "Hegener & Glaser") since 1979 with programs of [Elmar Henne](Elmar_Henne "Elmar Henne") and [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche"). Short after winning the World Microcomputer Chess Champion title at [WMCCC 1984](WMCCC_1984 "WMCCC 1984") in Glasgow (shared), [Hegener & Glaser](Hegener_%26_Glaser "Hegener & Glaser") abandoned the collaboration with Henne and Nitsche <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and started to work with [Richard Lang](Richard_Lang "Richard Lang") in continuing the [Mephisto](Mephisto "Mephisto") brand name, later also with programs of other professional chess programmers like [Frans Morsch](Frans_Morsch "Frans Morsch"), [Ulf Rathsman](Ulf_Rathsman "Ulf Rathsman"), [Ed Schröder](Ed_Schroder "Ed Schroder") and [Johan de Koning](Johan_de_Koning "Johan de Koning"). 



## Mephisto I, II


The mighty Mephisto I and II chess computers with their unique [Briquette](https://en.wikipedia.org/wiki/Briquette) design ran on the [RCA 1802](https://en.wikipedia.org/wiki/RCA_1802) 8-bit [CMOS](https://en.wikipedia.org/wiki/CMOS) processor with 6 KiB of a 8KiB [ROM](Memory#ROM "Memory") and one KiB of [RAM](Memory#RAM "Memory"), the Mephisto II, released in 1981, doubled the memory sizes. The [opening book](Opening_Book "Opening Book") was supplied by [Ossi Weiner](Ossi_Weiner "Ossi Weiner") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. The programs were based on Nitsche's former program [Orwell](Orwell "Orwell") - a mixture of [Shannon Type A](Type_A_Strategy "Type A Strategy") and [Type B strategy](Type_B_Strategy "Type B Strategy"). The first plies of a [brute-force](Brute-Force "Brute-Force") [alpha-beta search](Alpha-Beta "Alpha-Beta") were extended by a [selective](Selectivity "Selectivity") layer of plausible moves <a id="cite-note-4" href="#cite-ref-4">[4]</a>, no [quiescence search](Quiescence_Search "Quiescence Search"), but [SOMA](SOMA#SOMAALGO "SOMA") like [exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.




## Mephisto III


### CDL


The new **Mephisto III** program was written in [Compiler Description Language](https://en.wikipedia.org/wiki/Compiler_Description_Language) [CDL2](http://everything2.com/title/CDL2) for high abstraction with chess pattern terms, but only 1.5-2.0 times slower than [assembly](Assembly "Assembly"). It was further possible to compile the program for different target processors. While the default Mephisto III Briquette model as well the first [modular](Mephisto_Module_Systems "Mephisto Module Systems") **Mephisto MM I**, first released in 1983, still had an 8-bit RCA CMOS processor, now with 32 KiB ROM and 4 KiB RAM, the **Mephisto III-S** and Mephisto **Excalibur** were shipped with [Motorola's](index.php?title=Motorola&action=edit&redlink=1 "Motorola (page does not exist)") [68000](68000 "68000") 16-bit processor. Mephisto III-S won the the World Microcomputer Chess Champion title at [WMCCC 1984](WMCCC_1984 "WMCCC 1984") in Glasgow (shared with three other computers) <a id="cite-note-6" href="#cite-ref-6">[6]</a>.



### The Mephisto 3-Projekt


The programs of Henne and Nitsche were famous for their very small and selective "humanlike" [search trees](Search_Tree "Search Tree") <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a> . Translated quote from *Das Mephisto 3-Projekt* <a id="cite-note-9" href="#cite-ref-9">[9]</a> :




```C++
MEPHISTO 3 divides the decision tree into 3 sections

```

* `Utopian moves (good, if the opponent does not do anything): A position occurs in a depth of approximately 1-3. The beginning of a combination. Nearly every move promising somehow is selected, even if the probability of success is quite small. Humans call some of these moves sacrifices.`
* `Optimistic moves (good, if the opponent has only the second-best answer): The combination reached a depth of 4-8. Only moves with a probability hit rate larger than 30% are selected. ON BEHALF are this moves, which attack heavy pieces, threaten check, etc. these moves are however no sacrifices.`
* `Realistic moves (good, if the opponent selects the best countermove): The position occurs in depths greater than 8. Only clear completions are examined. I.e. the program does not attack no more on suspicion, but pursues moves with high hit rate. To bring i.e. an attacked piece into security, so that the piece is really safe and not bound or overloaded.`


## See also


* [Demonology](Category:Demonology "Category:Demonology")
* [Hegener & Glaser](Hegener_%26_Glaser "Hegener & Glaser")
* [Mephisto](Mephisto "Mephisto")
* [Mephisto Module Systems](Mephisto_Module_Systems "Mephisto Module Systems")


## Publications


* [Ab Dezember neuer Mikroschachcomputer für 350 Mark:: Mephisto unterm Weihnachtsbaum](http://www.computerwoche.de/heftarchiv/1979/36/1194002/), October 7, 1979, [Computerwoche](Computerworld#Woche "Computerworld") 36/1979 (German)
 * [Schachcomputer: Tricks und Trug](http://www.spiegel.de/spiegel/print/d-14334137.html), [Der Spiegel](https://en.wikipedia.org/wiki/Der_Spiegel) 50/1980, December 08, 1980, (German) [pdf](http://wissen.spiegel.de/wissen/image/show.html?did=14334137&aref=image036/2006/06/16/cq-sp198005000620071.pdf) 
* [Mychess, Sargon und Boris auf den Plätzen zwei bis vier: Münchner Mephisto siegt in Stockholm](http://www.computerwoche.de/heftarchiv/1981/9/1185335/), February 27, 1981, [Computerwoche](Computerworld#Woche "Computerworld") 9/1981 (German) » [Stockholm MCCT 1980](Stockholm_MCCT_1980 "Stockholm MCCT 1980")
* [Gern gefällig](http://www.spiegel.de/spiegel/print/d-14018815.html), [Der Spiegel](https://en.wikipedia.org/wiki/Der_Spiegel) 1/1983, January 03, 1983 (German) <a id="cite-note-10" href="#cite-ref-10">[10]</a>
* [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") (**1983**). *The Mephisto Concept, A "Humanlike" Thinking Chess Program.* [Computer Chess Digest Annual 1983](Computer_Chess_Reports "Computer Chess Reports")
* [Tony Harrington](Tony_Harrington "Tony Harrington") (**1983**). *A Match for Brute Force*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), [May 1983](http://www.chesscomputeruk.com/html/publication_archive_1983.html)
* [Tony Harrington](Tony_Harrington "Tony Harrington") (**1984**). *Mephisto III*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), [April 1984](http://www.chesscomputeruk.com/html/publication_archive_1984.html)
* [Tony Harrington](Tony_Harrington "Tony Harrington") (**1984**). *Mephisto's dual edge*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), [May 1984](http://www.chesscomputeruk.com/html/publication_archive_1984.html)
* [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") (**1984**). [Das Mephisto 3-Projekt](http://www.schach-computer.info/wiki/index.php/Das_Mephisto_3-Projekt), [Schach-Echo](http://de.wikipedia.org/wiki/Schach-Echo) 7/1984 (German)


## External Links


### Chess Computers


* [Mephisto (chess computer) from Wikipedia](https://en.wikipedia.org/wiki/Mephisto_%28chess_computer%29)
* [Mephisto's (H) ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=498)
* [About the company Hegener & Glaser (Mephisto)](https://www.schach-computer.info/wiki/index.php?title=Hegener_%26_Glaser_En) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
* [Hegener & Glaser (Mephisto)](http://www.ismenio.com/mephisto.html) from [ChessComputers.org](http://www.ismenio.com/chess_computers.html)
* [Mephisto I](http://www.schach-computer.info/wiki/index.php/Mephisto_I) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
* [Mephisto II](http://www.schach-computer.info/wiki/index.php/Mephisto_II) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
* [Mephisto III](http://www.schach-computer.info/wiki/index.php/Mephisto_III) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
* [Mephisto III-S Glasgow](http://www.schach-computer.info/wiki/index.php/Mephisto_III-S_Glasgow) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
* [Mephisto MM I](http://www.schach-computer.info/wiki/index.php/Mephisto_MM_I) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
* [Das Mephisto 3-Projekt](http://www.schach-computer.info/wiki/index.php/Das_Mephisto_3-Projekt) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
* [Mephisto Excalibur](http://www.schach-computer.info/wiki/index.php/Mephisto_Excalibur) by [Alwin Gruber](index.php?title=Alwin_Gruber&action=edit&redlink=1 "Alwin Gruber (page does not exist)"), [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
* [Mephisto | Photo collection](http://www.flickr.com/photos/10261668@N05/sets/72157600922171154/) by [Chewbanta](Steve_Blincoe "Steve Blincoe")
* [Mephisto Electronic Chess Computers](http://www.spacious-mind.com/html/mephisto.html) from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
* [The Long History of Mephisto - Part 1](http://adamsccpages.blogspot.de/2012/07/the-long-history-of-mephisto-part-1.html) from [Adam's](Adam_Hair "Adam Hair") [Computer Chess Pages](http://adamsccpages.blogspot.de/), June 18, 2012


### Misc


* [Mephisto (automaton) from Wikipedia](https://en.wikipedia.org/wiki/Mephisto_%28automaton%29)
* [Mephistopheles from Wikipedia](https://en.wikipedia.org/wiki/Mephistopheles)
* [Faust from Wikipedia](https://en.wikipedia.org/wiki/Faust)
* [Mephisto (novel) from Wikipedia](https://en.wikipedia.org/wiki/Mephisto_%28novel%29)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Mephisto I](http://www.schachcomputer.at/mep1.htm) from [Kurt´s Schachcomputer Homepage](http://www.schachcomputer.at/index.htm) by [Kurt Kispert](Kurt_Kispert "Kurt Kispert") (German)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Interview mit Manfred Hegener](http://www.schaakcomputers.nl/hein_veldhuis/database/files/10-1985,%20Interview%20mit%20Manfred%20Hegener,%20Neue%20Programme%20von%20neuen%20Programmierern.pdf) (pdf), Erwerbsquelle: 10-1985, Zeitschrift Schachcomputer (Herausgeber Florian Piel), Edition 20, S. 6-8, [Gerhard Piel](index.php?title=Gerhard_Piel&action=edit&redlink=1 "Gerhard Piel (page does not exist)"): Neue Programme von neuen Programmierern.(German) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Mephisto I](http://www.schaakcomputers.nl/hein_veldhuis/database/files/09-1980%20%5BA-5746%5D%20Mephisto%20-%20Mephisto%20%28I%29.pdf) (pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis") (Dutch, German)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a>  [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") (**1983**). *The Mephisto Concept, A "Humanlike" Thinking Chess Program.* [Computer Chess Digest Annual 1983](Computer_Chess_Reports "Computer Chess Reports")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a>  [Ab Dezember neuer Mikroschachcomputer für 350 Mark:: Mephisto unterm Weihnachtsbaum](http://www.computerwoche.de/heftarchiv/1979/36/1194002/), October 7, 1979, [Computerwoche](Computerworld#Woche "Computerworld") 36/1979 (German)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [4th World Microcomputer Chess Championship](https://www.game-ai-forum.org/icga-tournaments/tournament.php?id=64) from the [ICGA Tournament Site](https://www.game-ai-forum.org/icga-tournaments/)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") (**1983**). *The Mephisto Concept, A "Humanlike" Thinking Chess Program.* [Computer Chess Digest Annual 1983](Computer_Chess_Reports "Computer Chess Reports")
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Menschliche Spielweise und der erste Blick](http://www.schach-computer.info/wiki/index.php/Das_Mephisto_3-Projekt#Menschliche_Spielweise_und_der_erste_Blick) from [Das Mephisto 3-Projekt](http://www.schach-computer.info/wiki/index.php/Das_Mephisto_3-Projekt), [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") (**1984**). [Das Mephisto 3-Projekt](http://www.schach-computer.info/wiki/index.php/Das_Mephisto_3-Projekt), [Schach-Echo](http://de.wikipedia.org/wiki/Schach-Echo) 7/1984 (German)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Chess TV-World Cup](http://www.youtube.com/watch?v=yYNZtRDgH0c) - German free of ads regional [ARD broadcaster](https://en.wikipedia.org/wiki/ARD_%28broadcaster%29), [Drittes](http://de.wikipedia.org/wiki/Drittes_Fernsehprogramm) with [Mephisto](Mephisto "Mephisto") advertisement

**[Up one level](Engines "Engines")**







 
