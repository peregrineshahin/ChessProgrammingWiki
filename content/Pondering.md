---
title: Pondering
---
**[Home](Home "Home") \* [Search](Search "Search") \* Pondering**



[ [Vincent van Gogh](Category:Vincent_van_Gogh "Category:Vincent van Gogh") - [At Eternity's Gate](https://en.wikipedia.org/wiki/At_Eternity%27s_Gate), 1890
**Pondering** is simply using the opponent's move time to consider likely opponent moves and thus gain a pre-processing advantage when it is our turn to move, also referred as [Permanent brain](https://en.wikipedia.org/wiki/Permanent_brain).


One can generally use pondering time to seed the [transposition tables](Transposition_Table "Transposition Table"), using [iterative deepening](Iterative_Deepening "Iterative Deepening"), with positions, scores and suggested best start moves. Once it is your turn, you might either find an entry of sufficient depth to move immediately, or you may have enhanced your alpha-beta cutoff efficiency by having pre-computed moves in the transposition hash table, so that your move ordering is close to ideal. 



### Considering all Moves


Search the new root position from opponent's side to move, and therefor considering all opponent moves.



### Considering predicted Move


Search with the predicted opponent move from the [Principal Variation](Principal_Variation "Principal Variation") is actually made. If the expected move is really played by the opponent, a so called **Ponder Hit** occurred and one may either continue searching with the saved time, or dependent on score and time left, move immediately. Otherwise, if the the opponent doesn't agree and comes with another move, one needs to unmake the expected move and to restart search. According to [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), in about 50% the prediction is right <a id="cite-note-1" href="#cite-ref-1">[1]</a> .



### Hybrid Approaches


With the advent of Cluster architectures, hybrid Pondering approaches seem to advance <a id="cite-note-2" href="#cite-ref-2">[2]</a> .



## Protocol Considerations


Common [Protocols](Protocols "Protocols") for automated [game playing](Chess_Game "Chess Game") have various issues to conduct the game state inside a chess program and therefor with pondering <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



* [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
* [UCI](UCI "UCI")


## See also


* [Chess Game](Chess_Game "Chess Game")
* [Time Management](Time_Management "Time Management")


## Publications


* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1984**). *Using Time Wisely*. [ICCA Journal, Vol. 7, No. 1](ICGA_Journal#7_1 "ICGA Journal")
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1994**). *On Timing, Permanent Brain and Human Intervention*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [Masayuki Fujii](index.php?title=Masayuki_Fujii&action=edit&redlink=1 "Masayuki Fujii (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**1995**). *Prediction of an opponent's move using opponent's time effectively*. [2nd Game Programming Workshop](Conferences#GPW "Conferences")
* [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2005**). *An Optimistic Pondering Approach for Asynchronous Distributed Games*. [ICGA Journal, Vol. 28, No. 2](ICGA_Journal#28_2 "ICGA Journal")
* [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2012**). *[Optimistische verteilte Spielbaumsuche am Beispiel des Computerschachs](http://www.shaker.de/de/content/catalogue/index.asp?ID=8&ISBN=978-3-8440-0803-6)*. Dissertation (German) <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2012**). *GridChess: Combining Optimistic Pondering with the Young Brothers Wait Concept*. [ICGA Journal, Vol. 35, No. 2](ICGA_Journal#35_2 "ICGA Journal") » [GridChess](GridChess "GridChess"), [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")


## Forum Posts


### 1995 ...


* [Pondering and XBoard, WinBoard](https://www.stmintz.com/ccc/index.php?id=21841) by [Alessandro Damiani](Alessandro_Damiani "Alessandro Damiani"), [CCC](CCC "CCC"), July 07, 1998 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
* [WinBoard and pondering under W98](https://www.stmintz.com/ccc/index.php?id=62577) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), July 28, 1999 » [WinBoard](WinBoard "WinBoard")
* [PB-ON vs PB-OFF (results experiment-1)](https://www.stmintz.com/ccc/index.php?id=72537) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), October 10, 1999
* [PB-ON vs PB-OFF (final results)](https://www.stmintz.com/ccc/index.php?id=73408) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), October 15, 1999


### 2000 ...


* [Is pondering unfair in engine matches on a PC?](https://www.stmintz.com/ccc/index.php?id=155085) by [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [CCC](CCC "CCC"), February 19, 2001
* [PONDER=ON and TableBases on 1 PC](https://www.stmintz.com/ccc/index.php?id=181281) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), July 27, 2001 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [A pondering idea...](https://www.stmintz.com/ccc/index.php?id=190547) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), September 26, 2001
* [Pondering ("think on opponent's time")](https://www.stmintz.com/ccc/index.php?id=264237) by Jim Bumgardner, [CCC](CCC "CCC"), November 10, 2002
* [Question about pondering](https://www.stmintz.com/ccc/index.php?id=349367) by Michael Drexel, [CCC](CCC "CCC"), February 15, 2004
* [Ruffian's most peculiar way of pondering](https://www.stmintz.com/ccc/index.php?id=356976) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), March 27, 2004 » [Ruffian](Ruffian "Ruffian")
* [Pondering methods](https://www.stmintz.com/ccc/index.php?id=357181) by Zheng Zhixian, [CCC](CCC "CCC"), March 29, 2004
* [Elephant and pondering](https://www.stmintz.com/ccc/index.php?id=359543) by [Olivier Deville](Olivier_Deville "Olivier Deville"), [CCC](CCC "CCC"), April 11, 2004 » [Elephant](Elephant "Elephant")


### 2005 ...


* [obvious/easy move](http://www.talkchess.com/forum/viewtopic.php?t=20125) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), March 12, 2008
* [quick move after pondering](http://www.talkchess.com/forum/viewtopic.php?t=27105) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 21, 2009
* [Time managment on ponder hit](http://www.talkchess.com/forum/viewtopic.php?t=28438) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), June 16, 2009 » [Time Management](Time_Management "Time Management")
* [Pondering? Yes. Ponder move? Maybe not](http://www.talkchess.com/forum/viewtopic.php?t=29166) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 30, 2009
* [Pondering in WB](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50392) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), September 06, 2009 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")


### 2010 ...


* [Ponder console input move problem](http://www.talkchess.com/forum/viewtopic.php?t=34051) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), April 28, 2010 » [Command Line Interface](index.php?title=Command_Line_Interface&action=edit&redlink=1 "Command Line Interface (page does not exist)")
* [As though they were pondering](http://www.talkchess.com/forum/viewtopic.php?t=35554) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), July 23, 2010 » [Time Management](Time_Management "Time Management")
* [Move on Hash Hit](http://www.open-chess.org/viewtopic.php?f=5&t=588) by [kingliveson](Franklin_Titus "Franklin Titus"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 18, 2010 » [Time Management](Time_Management "Time Management")
* [Playing with ponder hits](http://www.talkchess.com/forum/viewtopic.php?t=44037) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 12, 2012
* [Ponder and UCI](http://www.open-chess.org/viewtopic.php?f=5&t=2146) by geko, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 19, 2012 » [UCI](UCI "UCI")
* [How to ponder](http://www.talkchess.com/forum/viewtopic.php?t=47554) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), March 20, 2013
* [How much elo is pondering worth?](http://www.talkchess.com/forum/viewtopic.php?t=48864) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), August 07, 2013
* [uci ponder protocol](http://www.talkchess.com/forum/viewtopic.php?t=48996) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), August 17, 2013 » [UCI](UCI "UCI")
* [SMP and pondering](http://www.talkchess.com/forum/viewtopic.php?t=51198) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), February 08, 2014 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [Myrddin](Myrddin "Myrddin")
* [Thinking During Adversary Time](http://www.talkchess.com/forum/viewtopic.php?t=52882) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), July 06, 2014


### 2015 ...


* [Speculative deep pondering](http://www.talkchess.com/forum/viewtopic.php?t=56697) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 17, 2015
* [ponder engine-gui interaction](http://www.talkchess.com/forum/viewtopic.php?t=56776) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), June 25, 2015 » [UCI](UCI "UCI")
* [stateless UCI](http://www.talkchess.com/forum/viewtopic.php?t=59235) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), February 13, 2016 » [UCI](UCI "UCI")


 [Re: stateless UCI](http://www.talkchess.com/forum/viewtopic.php?t=59235&start=11) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), February 14, 2016
* [Higher than expected by me efficiency of Ponder ON](http://www.talkchess.com/forum/viewtopic.php?t=63355) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 06, 2017 » [Match Statistics](Match_Statistics "Match Statistics")
* [Regarding UCI Pondering](http://www.talkchess.com/forum/viewtopic.php?t=65324) by [Manik Charan](Manik_Charan "Manik Charan"), [CCC](CCC "CCC"), September 28, 2017 » [UCI](UCI "UCI")
* [UCI pondering or infinite search](http://www.talkchess.com/forum/viewtopic.php?t=65679) by Lucas Braesch, [CCC](CCC "CCC"), November 10, 2017 » [UCI](UCI "UCI")
* [Regarding options ponder flag](http://www.talkchess.com/forum/viewtopic.php?t=65913) by [Jürgen Précour](index.php?title=J%C3%BCrgen_Pr%C3%A9cour&action=edit&redlink=1 "Jürgen Précour (page does not exist)"), [CCC](CCC "CCC"), December 06, 2017 » [UCI](UCI "UCI")
* [UCI Pondering workaround](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67971) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), July 13, 2018 » [UCI](UCI "UCI")
* [UCI pondering done right](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69279) by lucasart, [CCC](CCC "CCC"), December 16, 2018 » [UCI](UCI "UCI")
* [Tragic comedy in pondering](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70385) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), April 02, 2019 » [Stalemate](Stalemate "Stalemate")
* [UCI pondering and time management](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72686) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), December 30, 2019 » [UCI](UCI "UCI"), [Time Management](Time_Management "Time Management")


### 2020 ...


* [Missing input in ponder](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77088) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), April 15, 2021 » [UCI](UCI "UCI"), [Thread](Thread "Thread")


## External Links


* [Permanent brain from Wikipedia](https://en.wikipedia.org/wiki/Permanent_brain)
* [Pondering](http://web.archive.org/web/20071027053527/www.brucemo.com/compchess/programming/pondering.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
* [King Crimson](Category:King_Crimson "Category:King Crimson") - [Waiting Man](https://en.wikipedia.org/wiki/Beat_(King_Crimson_album)), [Rock from the Alabama](https://en.wikipedia.org/wiki/Alabama-Halle), [Munich](https://en.wikipedia.org/wiki/Munich), 1982, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Tony Levin](https://en.wikipedia.org/wiki/Tony_Levin), [Adrian Belew](Category:Adrian_Belew "Category:Adrian Belew"), [Bill Bruford](Category:Bill_Bruford "Category:Bill Bruford"), [Robert Fripp](Category:Robert_Fripp "Category:Robert Fripp")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: Pondering? Yes. Ponder move? Maybe not](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=283576&t=29166) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 30, 2009
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Himstedt, K.](Kai_Himstedt "Kai Himstedt") (**2005**). *An Optimistic Pondering Approach for Asynchronous Distributed Games*. [ICGA Journal, Vol. 28, No. 2](ICGA_Journal#28_2 "ICGA Journal")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Pondering in WB](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50392) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), September 06, 2009
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**2013**). *Optimistically Parallelizing Parallel Search Processes*. [ICGA Journal, Vol. 36, No. 2](ICGA_Journal#36_2 "ICGA Journal"), Review

**[Up one Level](Search "Search")**







 
