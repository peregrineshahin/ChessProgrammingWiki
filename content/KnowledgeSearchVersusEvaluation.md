---
title: KnowledgeSearchVersusEvaluation
---
**[Home](Home "Home") \* Knowledge**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bc6) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Knowledgeable <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Knowledge** is the possession of information, its acquisition involves complex [cognitive](Cognition "Cognition") processes: [perception](https://en.wikipedia.org/wiki/Perception), [learning](Learning "Learning"), [communication](https://en.wikipedia.org/wiki/Communication), [association](https://en.wikipedia.org/wiki/Association) and [reasoning](https://en.wikipedia.org/wiki/Reasoning).


Inside a chess program, knowledge is manifested either as [procedural](https://en.wikipedia.org/wiki/Procedural_knowledge) or as [declarative knowledge](https://en.wikipedia.org/wiki/Declarative_knowledge). The declarative [a priori](https://en.wikipedia.org/wiki/A_priori_and_a_posteriori) knowledge about the [rules of chess](Rules_of_Chess "Rules of Chess") is immanent inside the [move generator](Move_Generation "Move Generation") in conjunction with [check](Check "Check") detection. Further declarative knowledge is coded as [rules of thumb](https://en.wikipedia.org/wiki/Rule_of_thumb) of the [evaluation](Evaluation "Evaluation") function, as well as persistent perfect knowledge from [retrograde analysis](Retrograde_Analysis "Retrograde Analysis"), or as [empirical](https://en.wikipedia.org/wiki/Empirical) knowledge mostly from human [experience](https://en.wikipedia.org/wiki/Experience), to retrieve [moves](Moves "Moves") from an hand crafted [opening book](Opening_Book "Opening Book"). Procedural knowledge is applied by [Learning](Learning "Learning"), as well to backup declarative knowledge by [Search](Search "Search"). However, the Search versus Knowledge trade-off in computer chess and games refers heuristic or perfect knowledge. 




### In Practice


[Andreas Junghanns](Andreas_Junghanns "Andreas Junghanns") and [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") in *Search versus knowledge in game-playing programs revisited* <a id="cite-note-3" href="#cite-ref-3">[3]</a>:




```C++The difficulty lies in quantifying the knowledge axis. Perfect knowledge assumes an [oracle](Oracle "Oracle"), which for most games we do not have. However, we can approximate an oracle by using a high-quality, game playing program that performs deep searches. Although not perfect, it is the best approximation available. Using this, how can we measure the quality of knowledge in the program?

```


```C++A heuristic evaluation function, as judged by an oracle, can be viewed as a combination of two things: oracle knowledge and noise. The oracle knowledge is beneficial and improves the program' s play. The noise, on the other hand, represents the inaccuracies in the program' s knowledge. It can be introduced by several things, including knowledge that is missing, over- or under-valued, and/or irrelevant. As the noise level increase, the beneficial contribution of the knowledge is overshadowed.

```


```C++By definition, an oracle has no noise. We can measure the quality of the heuristic evaluation in a program by the amount of noise that is added into it. To measure this, we add a [random number](Pseudorandom_Number_Generator "Pseudorandom Number Generator") to each [leaf node evaluation](Search_with_Random_Leaf_Values "Search with Random Leaf Values") ... 

```

### HiTech versus LoTech


At the [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5") conference 1987, [Hans Berliner](Hans_Berliner "Hans Berliner") et al. introduced an interesting experiment. [HiTech](HiTech "HiTech") with a sophisticated evaluation competed versus LoTech, almost the same program but a rudimentary evaluation, at different [search depths](Depth "Depth") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. According to [Peter Kouwenhoven](Peter_Kouwenhoven "Peter Kouwenhoven") <a id="cite-note-5" href="#cite-ref-5">[5]</a>, Berliner's conclusion was that more was to be won by increasing HiTech's knowledge at constant speed rather than further increasing its speed while keeping knowledge constant. The abstract from the extended 1990 paper <a id="cite-note-6" href="#cite-ref-6">[6]</a>:




```C++Chess programs can differ in depth of search or in the evaluation function applied to leaf nodes or both. Over the past 10 years, the notion that the principal way to [strengthen](Playing_Strength "Playing Strength") a chess program is to improve its depth of search has held sway. Improving depth of search undoubtedly does improve a program's strength. However, projections of potential gain have time and again been found to overestimate the actual gain.

```


```C++We examine the notion that it is possible to project the playing strength of chess programs by having different versions of the same program (differing only in depth of search) play each other. Our data indicates that once a depth of “tactical sufficiency” is reached, a knowledgeable program can beat a significantly less knowledgeable one almost all of the time when both are searching to the same depth. This suggests that once a certain knowledge gap has been opened up, it cannot be overcome by small increments in searching depth. The conclusion from this work is that extending the depth of search without increasing the present level of knowledge will not in any foreseeable time lead to World Championship level chess. The approach of increasing knowledge has been taken in the HiTech chess machine. 

```

### Ed Schröder's Conclusion


[Ed Schröder](Ed_Schroder "Ed Schroder") concluded HiTech's extra knowledge was just worth one [ply](Ply "Ply") in the computer-computer area <a id="cite-note-7" href="#cite-ref-7">[7]</a><a id="cite-note-8" href="#cite-ref-8">[8]</a>, and further elaborated on [tactical](Tactics "Tactics") evaluation knowledge helpful in early [Rebel](Rebel "Rebel") searching 5-7 plies versus Rebel searching 13-15 plies on 2001 hardware <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a>:




```C++Some specific chess knowledge through the years become out-dated due to the speed of nowadays computers. An example: In the early days of computer chess, say the period 1985-1989 I as hardware had a [6502](6502 "6502") running at 5 Mhz. [Rebel](Rebel "Rebel") at that time could only search 5-7 plies on tournament time control. Such a low depth guarantees you one thing: [horizon effects](Horizon_Effect "Horizon Effect") all over, thus losing the game.

```


```C++To escape from the horizon effect all kind of tricks were invented, chess knowledge about dangerous [pins](Pin "Pin"), [knight forks](Knight_Pattern#KnightForks "Knight Pattern"), [double attacks](Double_Attack "Double Attack"), [overloading of pieces](Overloading "Overloading") and reward those aspects in [eval](Evaluation "Evaluation"). Complicated and processor time consuming software it was (15-20% less performance) but it did the trick escaping from the horizon effect in a reasonable way.

```


```C++Today we run chess program on 1500 Mhz machines and instead of the 5-7 plies Rebel now gets 13-15 plies in the middle game and the horizon effect which was a major problem at 5 Mhz slowly was fading away.

```


```C++So I wondered, what if I throw that complicated "anti-horizon" code out of Rebel, is it still needed? So I tried and found out that Rebel played as good with the "anti-horizon" code as without the code. In other words, the net gain was a "free" speed gain of 15-20%, thus an improvement.

```


```C++One aspect of chess programming is that your program is in a constant state of change due to the state of art of nowadays available hardware. I am sure a Rebel at 10 Ghz several parts of Rebel need a face-lift to get the maximum out of the new speed monster. 

```





### Search versus Evaluation


[Mark Uniacke](Mark_Uniacke "Mark Uniacke") in a reply to [Ed Schröder](Ed_Schroder "Ed Schroder"), on [Search](Search "Search") or [Evaluation](Evaluation "Evaluation"), mentioning the [1st Computer Olympiad](1st_Computer_Olympiad#Chess "1st Computer Olympiad"), [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [HIARCS](HIARCS "HIARCS"), [Woodpusher](Woodpusher "Woodpusher"), [E6P](E6P "E6P"), [Rebel](Rebel "Rebel"), [Fritz](Fritz "Fritz") ... <a id="cite-note-11" href="#cite-ref-11">[11]</a>:




```C++I am not saying search is the only reason but that search is more significant in the Elo jump than other factors. Thanks for the interesting history which in general I agree with but I should add for clarification...

```


```C++In 1989 I was exposed to the  [null move](Null_Move "Null Move") in [HIARCS'](HIARCS "HIARCS") first official computer tournament at the [Olympiad](1st_Computer_Olympiad "1st Computer Olympiad") in London. [John Hamlen](John_Hamlen "John Hamlen") had written his program [Woodpusher](Woodpusher "Woodpusher") as part of his M.Sc project investigating the null move exclamation and although Woodpusher did not do well in that tournament I had the good fortune to discuss null move with John and reading his project which interested me very much. John and I had many discussions on computer chess over the following months.
That Olympiad probably had an impact on you too and not only because [Rebel](Rebel "Rebel") won Gold above [Mephisto X](Mephisto_Portorose "Mephisto Portorose") and [Fidelity X](Fidelity "Fidelity") for the first time but because there was a program there running quite fast (at that time in history) called [E6P](E6P "E6P") (so named because it could reach 6 ply full width!) running on an Acorn [ARM](ARM2 "ARM2") [based machine](Acorn_Archimedes "Acorn Archimedes"). [Jan](Jan_Louwman "Jan Louwman") was operating Rebel at the tournament as you know and I noticed Jan take a keen interest in this new machine. 

```


```C++[Frans](Frans_Morsch "Frans Morsch") was using null move in [Fritz 2](Fritz "Fritz") in [Madrid 1992](WCCC_1992 "WCCC 1992") (I am not sure about Fritz 1). I am sure you remember that tournament fondly. I remember at Madrid having a discussion with a few programmers including [Richard](Richard_Lang "Richard Lang") about what on earth was Fritz 2 doing to reach the [depths](Depth "Depth") it was attaining, this seed of interest made me investigate search enhancements carefully after Madrid and it was then that I began re-investigating the null move. It was not long before HIARCS began using null moves too and by Christmas 1992 I had a working implementation which gave a big jump over Hiarcs 1 which had only been released shortly before. I had much fun playing my Hiarcs 1.n against [Mephisto Risc 1](Mephisto_RISC "Mephisto RISC") in late 1992, early 1993 and that sort of closes the circle on the E6P story. Even so, the null move idea still evolved and my implementation today is much better than it was initially and so it can be for other ideas. We can all profit from these techniques but some gain more than others if they find new ways to exploit it.

Rebel 7/8/9 and Hiarcs 5/6/7 battled hard in those years and my big jump to the top of the rating lists happened partly because of a search change to Hiarcs 5/6 which led at one stage to a 71 Elo lead on the SSDF. I recall Rebel and Hiarcs exchanging the lead on the [SSDF](SSDF "SSDF") list a number of times in those years. So we agree the impact search has made on computer chess progress is clear. Now we diverge on what might be the reason for new progress in the field.
Clearly we have good search enhancements on [cut nodes](Node_Types#cut-nodes "Node Types") and [all nodes](Node_Types#all-nodes "Node Types"), but that does not mean they cannot be improved and enhanced or in fact that another technique might prove to be superior or complementary. Meanwhile there can be no doubt that progress is made positionally irrespective of search but I do not believe it can be the reason for a breakthrough jump in chess strength but rather a steady climb.

But wait!
Maybe there is a middle way, a third avenue of improvement which sort of falls between the two pillars of search and evaluation and that is search intelligence. Something both of us have practiced in our programs for years but maybe not properly exploited. The ability of the eval to have a more significant impact on the search than traditionally has been the case. I think this area has been relatively unexplored and offers interesting potential. 

```

## Knowing


* [Chunking](Chunking "Chunking")
* [Cognition](Cognition "Cognition")
* [Learning](Learning "Learning")
* [Pattern Recognition](Pattern_Recognition "Pattern Recognition")
* [Planning](Planning "Planning")






## Declarative Knowledge


### A Priori


* [Rules of Chess](Rules_of_Chess "Rules of Chess")
* [Move Generation](Move_Generation "Move Generation")
* [In Check](Check "Check")


### Heuristic Knowledge


* [Evaluation](Evaluation "Evaluation")
* [Move Ordering](Move_Ordering "Move Ordering")
* [Selectivity](Selectivity "Selectivity")


### Empirical Knowledge


* [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Opening Book](Opening_Book "Opening Book")






### Perfect Knowledge


Perfect Knowledge usually incorporates [analysis](Retrograde_Analysis "Retrograde Analysis") or stored results from exhaustive search, which requires no further search at [interior nodes](Interior_Node "Interior Node") except the [root](Root "Root"). An [oracle](Oracle "Oracle") might be considered as "perfect" [evaluation](Evaluation "Evaluation").



* [Oracle](Oracle "Oracle")
* [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis")






### Interior Node Recognizer


* [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")


### Endgame Databases


as probed inside a Recognizer framework, if a certain material constellation is detected.



* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [Endgame Bitbases](Endgame_Bitbases "Endgame Bitbases")


## Procedural Knowledge


* [Search](Search "Search")
* [Checkmate](Checkmate "Checkmate")
* [Stalemate](Stalemate "Stalemate")
* [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
* [Repetitions](Repetitions "Repetitions")


## See also


* [Artificial Intelligence](Artificial_Intelligence "Artificial Intelligence")
* [Diminishing Returns](Depth#DiminishingReturns "Depth")
* [Memory](Memory "Memory")
* [Opponent Model Search](Opponent_Model_Search "Opponent Model Search")
* [Psychology](index.php?title=Psychology&action=edit&redlink=1 "Psychology (page does not exist)")
* [Strategy](Strategy "Strategy")
* [Tactics](Tactics "Tactics")


## Publications


### 1970 ...


* [Marvin Minsky](Marvin_Minsky "Marvin Minsky") (**1974**). *[Framework for Representing Knowledge 1974](http://web.media.mit.edu/~minsky/papers/Frames/frames.html)*. [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")-AI Laboratory Memo 306
* [Coen Zuidema](index.php?title=Coen_Zuidema&action=edit&redlink=1 "Coen Zuidema (page does not exist)") (**1974**). *Chess: How to Program the Exceptions?* Technical Report IW21/74, [Mathematical Center Amdsterdam](https://en.wikipedia.org/wiki/Centrum_Wiskunde_%26_Informatica). [pdf](http://oai.cwi.nl/oai/asset/9480/9480A.pdf)


### 1975 ...


* [Donald Michie](Donald_Michie "Donald Michie") (**1976**). *An Advice-Taking System for Computer Chess.* Computer Bulletin, Ser. 2, Vol. 10, pp. 12-14. ISSN 0010-4531.
* [Jack Good](Jack_Good "Jack Good") (**1977**). *Dynamic Probability, Computer Chess, and the Measurement of Knowledge.* Machine Intelligence, Vol. 8 (eds. E. Elcock and [Donald Michie](Donald_Michie "Donald Michie")), pp. 139-150. Ellis Horwood, Chichester.
* [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Danny Kopec](Danny_Kopec "Danny Kopec"), [Donald Michie](Donald_Michie "Donald Michie") (**1978**). *Pattern-Based Representation of Chess Endgame Knowledge*. [The Computer Journal, Vol. 21, No. 2](http://comjnl.oxfordjournals.org/content/21/2.toc), pp. 149-153. [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_44_C.pdf)
* [Donald Michie](Donald_Michie "Donald Michie"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**1978**). *Advice Table Representations of Chess End-Game Knowledge*. Proceedings 3rd AISB/GI Conference, pp. 194-200.
* [David Wilkins](David_Wilkins "David Wilkins") (**1979**). *Using Patterns and Plans to Solve Problems and Control Search*. Ph.D. thesis, Computer Science Dept, [Stanford University](Stanford_University "Stanford University"), AI Lab Memo AIM-329
* [Max Bramer](Max_Bramer "Max Bramer"), [Mike Clarke](Mike_Clarke "Mike Clarke") (**1979**). *[A Model for the Representation of Pattern-Knowledge for the Endgame in Chess](http://www.sciencedirect.com/science/article/pii/S0020737379800139)*. [International Journal of Man-Machine Studies, Vol. 11, No.5](http://www.interaction-design.org/references/periodicals/international_journal_of_man-machine_studies_volume_11.html)


### 1980 ...


* [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Donald Michie](Donald_Michie "Donald Michie") (**1980**). *A Representation of Pattern-Knowledge in Chess Endgames*. [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")
* [David Wilkins](David_Wilkins "David Wilkins") (**1980**). *Using patterns and plans in chess*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), vol. 14, pp. 165-203. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [David Wilkins](David_Wilkins "David Wilkins") (**1982**). *Using Knowledge to Control Tree Searching*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), vol. 18, pp. 1-51.
* [Alen Shapiro](Alen_Shapiro "Alen Shapiro"), [Tim Niblett](Tim_Niblett "Tim Niblett") (**1982**). *Automatic Induction of Classification Rules for Chess End game.* [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
* [Hans Berliner](Hans_Berliner "Hans Berliner") (**1982**). *Search vs. knowledge: an analysis from the domain of games*. Technical Report Department of Computer Science, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
* [Allen Newell](Allen_Newell "Allen Newell") (**1982**). *The Knowledge Level*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 18, No. 1
* [Raymond Smullyan](Raymond_Smullyan "Raymond Smullyan") (**1982**). *[An Epistemological Nightmare](http://www.mit.edu/people/dpolicar/writing/prose/text/epistemologicalNightmare.html)*. [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
* [David Wilkins](David_Wilkins "David Wilkins") (**1983**). *Using chess knowledge to reduce search*. In [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine") ([Peter W. Frey](Peter_W._Frey "Peter W. Frey"), ed.), Ch. 10, 2nd Edition, Springer-Verlag.
* [Danny Kopec](Danny_Kopec "Danny Kopec") (**1983**). *Human and Machine Representations of Knowledge*. Ph.D. thesis, [University of Edinburgh](University_of_Edinburgh "University of Edinburgh"), supervisor: [Donald Michie](Donald_Michie "Donald Michie")
* [Alen Shapiro](Alen_Shapiro "Alen Shapiro") (**1983**). *The Role of Structured Induction in Expert Systems*. [University of Edinburgh](University_of_Edinburgh "University of Edinburgh"), Machine Intelligence Research Unit (Ph.D. thesis) <a id="cite-note-12" href="#cite-ref-12">[12]</a>
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1984**). *The Relative Importance of Knowledge*. [ICCA Journal, Vol. 7, No. 3](ICGA_Journal#7_3 "ICGA Journal")
* [Albrecht Heeffer](Albrecht_Heeffer "Albrecht Heeffer") (**1984**). *Automated Acquisition on Concepts for the Description of Middle-game Positions in Chess*. [Turing Institute](https://en.wikipedia.org/wiki/Turing_Institute), [Glasgow](https://en.wikipedia.org/wiki/Glasgow), [Scotland](https://en.wikipedia.org/wiki/Scotland), TIRM-84-005


### 1985 ...


* [Albrecht Heeffer](Albrecht_Heeffer "Albrecht Heeffer") (**1985**). *Validating Concepts from Automated Acquisition Systems*. [IJCAI 85](Conferences#IJCAI "Conferences"), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-85-VOL1/PDF/118.pdf)
* [Reiner Seidel](Reiner_Seidel "Reiner Seidel") (**1985**). *Grammatical Description of Chess Positions, Data-Base versus Human Knowledge*. [ICCA Journal, Vol. 8, No. 3](ICGA_Journal#8_3 "ICGA Journal")
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1985**). *The Utility of Expert Knowledge*. Proceedings [IJCAI 85](http://www.informatik.uni-trier.de/%7Eley/db/conf/ijcai/ijcai85.html), pp. 585-587. Los Angeles.
* [Alen Shapiro](Alen_Shapiro "Alen Shapiro"), [Donald Michie](Donald_Michie "Donald Michie") (**1986**). *A Self-commenting Facility for Inductively Synthesised Endgame Expertise*. [Advances in Computer Chess 4](Advances_in_Computer_Chess_4 "Advances in Computer Chess 4")
* [Bernd Owsnicki](Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe"), [Kai von Luck](Kai_von_Luck "Kai von Luck") (**1986**). *N.N.: A Case Study in Chess Knowledge Representation*. [Advances in Computer Chess 4](Advances_in_Computer_Chess_4 "Advances in Computer Chess 4")
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1986**). *Experiments in Search and Knowledge*. Ph.D. Thesis, [University of Waterloo](University_of_Waterloo "University of Waterloo"). Reprinted as Technical Report TR 86-12, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), Edmonton, Alberta.
* [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**1986**). *Fuzzy Production Rules in Chess*. [ICCA Journal, Vol. 9, No. 4](ICGA_Journal#9_4 "ICGA Journal")
* [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**1986**). *[A Bit-Mapped Classifier](https://archive.org/stream/byte-magazine-1986-11/1986_11_BYTE_11-12_Knowledge_Representation#page/n175/mode/2up)*. [BYTE, Vol. 11, No. 12](Byte_Magazine#BYTE1112 "Byte Magazine"), pp. 161-172.
* [Subhash Kak](https://en.wikipedia.org/wiki/Subhash_Kak) (**1987**). *Patanjali and Cognitive Science*. [Vitasta Publishing](http://www.vitastapublishing.com/) <a id="cite-note-13" href="#cite-ref-13">[13]</a>
* [Alen Shapiro](Alen_Shapiro "Alen Shapiro") (**1987**). *Structured Induction in Expert Systems*. Turing Institute Press in association with Addison-Wesley Publishing Company, Workingham, UK. ISBN 0-201-178133. [amazon](http://www.amazon.com/exec/obidos/ASIN/0201178133/acmorg-20)<a id="cite-note-14" href="#cite-ref-14">[14]</a>
* [Stephen Muggleton](Stephen_Muggleton "Stephen Muggleton") (**1988**). *Inductive Acquisition of Chess Strategies*. [Machine Intelligence 11](http://www.doc.ic.ac.uk/%7Eshm/MI/mi11.html) (eds. [Jean Hayes Michie](Jean_Hayes_Michie "Jean Hayes Michie"), [Donald Michie](Donald_Michie "Donald Michie"), and J. Richards), pp. 375-389. Clarendon Press, Oxford, U.K. ISBN 0-19-853718-2.
* [Reiner Seidel](Reiner_Seidel "Reiner Seidel")(**1989**). *A Model of Chess Knowledge - Planning Structures and Constituent Analysis*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")
* [Hans Berliner](Hans_Berliner "Hans Berliner"), [Carl Ebeling](Carl_Ebeling "Carl Ebeling") (**1989**). *Pattern Knowledge and Search: The SUPREM Architecture.* Artificial Intelligence, Vol. 38, No. 2, pp. 161-198. ISSN 0004-3702.


 Revised as [Hans Berliner](Hans_Berliner "Hans Berliner"), [Carl Ebeling](Carl_Ebeling "Carl Ebeling") (**1990**). *Hitech*. [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")
* [Hans Berliner](Hans_Berliner "Hans Berliner"), [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Carl Ebeling](Carl_Ebeling "Carl Ebeling") (**1989**). *Measuring the Performance Potential of Chess Programs,* [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")
* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1989**). *Towards a Theory of Knowledge*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")


### 1990 ...


* [Hans Berliner](Hans_Berliner "Hans Berliner"), [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Carl Ebeling](Carl_Ebeling "Carl Ebeling") (**1990**). *[Measuring the Performance Potential of Chess Programs](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6TYF-47WTT8W-3J&_user=10&_coverDate=04%2F30%2F1990&_rdoc=1&_fmt=high&_orig=search&_origin=search&_sort=d&_docanchor=&view=c&_searchStrId=1541914346&_rerunOrigin=google&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=a43185e00b7d7d4550af0add28ff36b8&searchtype=a).* Artificial Intelligence, Vol. 43, No. 1
* [Kiyoshi Shirayanagi](index.php?title=Kiyoshi_Shirayanagi&action=edit&redlink=1 "Kiyoshi Shirayanagi (page does not exist)") (**1990**). *Knowledge Representation and its Refinement in Go Programs*. [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [Tony Marsland](Tony_Marsland "Tony Marsland"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [David Wilkins](David_Wilkins "David Wilkins") (**1991**). *The Role of Chess in Artificial Intelligence Research*. [IJCAI 1991](http://dli.iiit.ac.in/ijcai/IJCAI-91-VOL1/CONTENT/content.htm), [pdf](http://dli.iiit.ac.in/ijcai/IJCAI-91-VOL1/PDF/084.pdf), also in [ICCA Journal, Vol. 14, No. 3](ICGA_Journal#14_3 "ICGA Journal"), [pdf](http://www.ai.sri.com/%7Ewilkins/papers/chess-panel.pdf)
* [Christian Posthoff](Christian_Posthoff "Christian Posthoff"), [Michael Schlosser](Michael_Schlosser "Michael Schlosser"), [Jens Zeidler](Jens_Zeidler "Jens Zeidler") (**1993**). *Search vs. Knowledge? - Search and Knowledge!* In: Proc. 3rd KADS Meeting, Munich, March 8-9 1993, Siemens AG, Corporate Research and Development, 305-326, 1993.
* [Steven Walczak](index.php?title=Steven_Walczak&action=edit&redlink=1 "Steven Walczak (page does not exist)"), [Douglas D. Dankel II](http://www.cise.ufl.edu/~ddd/) (**1993**). *Acquiring Tactical and Strategic Knowledge with a Generalized Method for Chunking of Game Pieces*. International Journal of Intelligent Systems 8 (2), 249-270.
* [Christian Posthoff](Christian_Posthoff "Christian Posthoff"), [Michael Schlosser](Michael_Schlosser "Michael Schlosser"), [Rainer Staudte](Rainer_Staudte "Rainer Staudte"), [Jens Zeidler](Jens_Zeidler "Jens Zeidler") (**1994**). *Transformations of Knowledge*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Gil Fuchs](index.php?title=Gil_Fuchs&action=edit&redlink=1 "Gil Fuchs (page does not exist)") (**1994**). *A Pattern-Weight Formulation of Search Knowledge*. UCSC-CRL-94-10, [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.35.1027)


### 1995 ...


* [Richard Fikes](Richard_Fikes "Richard Fikes") (**1996**). *Ontologies: What Are They, and Where's The Research?* [KR 1996](http://www.informatik.uni-trier.de/~ley/db/conf/kr/kr96.html#Fikes96)
* [Andreas Junghanns](Andreas_Junghanns "Andreas Junghanns"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *Search versus knowledge in game-playing programs revisited*. [IJCAI-97](Conferences#IJCAI1997 "Conferences"), Vol 1, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.32.168&rep=rep1&type=pdf)
* [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**1997**). *Knowledge Discovery in Chess Databases: A Research Proposal.* Technical Report OEFAI-TR-97-33, Austrian Research Institute for Artificial Intelligence, [zipped ps](http://www.ke.informatik.tu-darmstadt.de/%7Ejuffi/publications/chess-ws.ps.gz), [pdf](http://www.top-5000.nl/ps/Knowledge%20discovery%20in%20chess%20databases%20-%20a%20research%20proposal.pdf) <a id="cite-note-15" href="#cite-ref-15">[15]</a>
* [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec"), [Roman Slowinski](http://www.informatik.uni-trier.de/~ley/pers/hd/s/Slowinski:Roman.html), [Irmina Szczesniak](http://www.informatik.uni-trier.de/~ley/pers/hd/s/Szczesniak:Irmina.html) (**1998**). *[Pedagogical Method for Extraction of Symbolic Knowledge from Neural Networks](http://link.springer.com/chapter/10.1007%2F3-540-69115-4_60)*. [Rough Sets and Current Trends in Computing 1998](http://link.springer.com/book/10.1007%2F3-540-69115-4)
* [Edward J. Quigley](Edward_John_Quigley "Edward John Quigley"), [Anthony Debons](http://www.ischool.pitt.edu/people/debons.php) (**1999**). *Interrogative Theory of Information and Knowledge*. [SIGCPR '99](http://www.informatik.uni-trier.de/~ley/db/conf/sigcpr/sigcpr1999.html#QuigleyD99), [pdf](http://www.thirdwave-websites.com/datainfoknow.pdf)


### 2000 ...


* [Michael Thielscher](Michael_Thielscher "Michael Thielscher") (**2000**). *Representing the Knowledge of a Robot*. [KR 2000](http://www.informatik.uni-trier.de/~ley/db/conf/kr/kr2000.html#Thielscher00), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.35.477)
* [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2002**). *[Genetic Programming-based Construction of Features for Machine Learning and Knowledge Discovery Tasks](http://link.springer.com/article/10.1023/A:1020984725014)*. [Genetic Programming and Evolvable Machines, Vol. 3](http://www.informatik.uni-trier.de/~ley/db/journals/gpem/gpem3.html#Krawiec02), No. 4
* [Stuart Russell](Stuart_Russell "Stuart Russell"), [Peter Norvig](Peter_Norvig "Peter Norvig") (**2003**). *[Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu/)*, 2nd edition, [3rd edition 2009](http://books.google.com/books?id=8jZBksh-bUMC&dq=isbn:0137903952&hl=en)
* [Stuart Russell](Stuart_Russell "Stuart Russell") (**2003**). *Rationality and Intelligence.* In Renee Elio (Ed.), Common sense, reasoning, and rationality, Oxford University Press, [pdf](http://www.cs.berkeley.edu/%7Erussell/papers/aij-cnt.pdf)
* [Aleksander Sadikov](Aleksander_Sadikov "Aleksander Sadikov"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Igor Kononenko](Igor_Kononenko "Igor Kononenko") (**2003**). *Search versus Knowledge: An Empirical Study of Minimax on KRK*. [Advances in Computer Games 10](Advances_in_Computer_Games_10 "Advances in Computer Games 10"), [pdf](http://www.ailab.si/sasha/acg2003.pdf)
* [Tristan Caulfield](index.php?title=Tristan_Caulfield&action=edit&redlink=1 "Tristan Caulfield (page does not exist)") (**2004**). *Acquiring and Using Knowledge in Computer Chess*. BSc Computer Science, [University of Bath](https://en.wikipedia.org/wiki/University_of_Bath), [pdf](http://opus.bath.ac.uk/16854/1/CSBU)
* [Elias M. Awad](http://people.virginia.edu/~ema3z/), [Hassan M. Ghaziri](http://www.goodreads.com/author/show/4245178.Hassan_Ghaziri) (**2004,2010**). *Knowledge Management Systems*. [Pearson Education India](http://www.pearsoned.co.in/web/books/9788131714034_Knowledge-Management_Hassan-M-Ghaziri.aspx), [Knowledge Management Systems - Lecture Notes](http://turing.une.edu.au/~comp292/Lectures/HEADER_KM_2004_LEC_NOTES/HEADER_KM_2004_LEC_NOTES.html), [LaTeX2HTML](http://www.latex2html.org/) by [Nikos Drakos](http://www.astro.ku.dk/software/latex2html/manual/manual.html), [Ross Moore](http://maths.mq.edu.au/~ross/)
* [Nick Pelling](Nick_Pelling "Nick Pelling") (**2004**). *[The Network Is The Knowledge: Ideology & Strategy in Mintzberg's Ten Schools](http://www.nickpelling.com/dissertation/)*. [MBA](https://en.wikipedia.org/wiki/Master_of_Business_Administration) dissertation, [Kingston University](https://en.wikipedia.org/wiki/Kingston_University) [Business School](https://en.wikipedia.org/wiki/Kingston_Business_School), [Surrey](https://en.wikipedia.org/wiki/Surrey), UK


### 2005 ...


* [Christian Posthoff](Christian_Posthoff "Christian Posthoff"), [Michael Schlosser](Michael_Schlosser "Michael Schlosser") (**2005**). *[Optimal strategies — Learning from examples — Boolean equations](http://link.springer.com/chapter/10.1007%2F3-540-60217-8_17)*. in [Klaus P. Jantke](https://www.researchgate.net/profile/Klaus_Jantke), [Steffen Lange](https://www.fbi.h-da.de/organisation/personen/lange-steffen.html) (eds.) (**2005**). [Algorithmic Learning for Knowledge-Based Systems](http://link.springer.com/book/10.1007/3-540-60217-8), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 961, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Aleksander Sadikov](Aleksander_Sadikov "Aleksander Sadikov"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2006**). *[Search Versus Knowledge Revisited Again](http://link.springer.com/chapter/10.1007/978-3-540-75538-8_15)*. [CG 2006](CG_2006 "CG 2006")
* [David J. Stracuzzi](index.php?title=David_J._Stracuzzi&action=edit&redlink=1 "David J. Stracuzzi (page does not exist)") (**2006**). *[Scalable Knowledge Acquisition through Cumulative Learning and Memory Organization](http://scholarworks.umass.edu/dissertations/AAI3242366/)*. Ph.D. thesis, [University of Massachusetts Amherst](https://en.wikipedia.org/wiki/University_of_Massachusetts_Amherst), advisor [Paul E. Utgoff](Paul_E._Utgoff "Paul E. Utgoff"), [pdf](http://stracuzzi.info/david/manuscripts/dissertation06.pdf)
* [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Louis Chatriot](index.php?title=Louis_Chatriot&action=edit&redlink=1 "Louis Chatriot (page does not exist)"), [Christophe Fiter](index.php?title=Christophe_Fiter&action=edit&redlink=1 "Christophe Fiter (page does not exist)"), [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Jean-Baptiste Hoock](Jean-Baptiste_Hoock "Jean-Baptiste Hoock"), [Julien Pérez](index.php?title=Julien_P%C3%A9rez&action=edit&redlink=1 "Julien Pérez (page does not exist)"), [Arpad Rimmel](index.php?title=Arpad_Rimmel&action=edit&redlink=1 "Arpad Rimmel (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2008**). *Combining expert, offline, transient and online knowledge in Monte-Carlo exploration*. [pdf](http://www.lri.fr/~teytaud/eg.pdf)
* [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Christophe Fiter](index.php?title=Christophe_Fiter&action=edit&redlink=1 "Christophe Fiter (page does not exist)"), [Jean-Baptiste Hoock](Jean-Baptiste_Hoock "Jean-Baptiste Hoock"), [Arpad Rimmel](index.php?title=Arpad_Rimmel&action=edit&redlink=1 "Arpad Rimmel (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2009**). *Adding Expert Knowledge and Exploration in Monte-Carlo Tree Search*. [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [pdf](http://www.personeel.unimaas.nl/g-chaslot/papers/acg09.pdf), [pdf](http://www.lri.fr/~rimmel/publi/EK_explo.pdf)


### 2010 ...


* [Matej Guid](Matej_Guid "Matej Guid") (**2010**). *Search and Knowledge for Human and Machine Problem Solving*, Ph.D. thesis, [University of Ljubljana](University_of_Ljubljana "University of Ljubljana"), [pdf](http://eprints.fri.uni-lj.si/1113/1/Matej__Guid.disertacija.pdf) <a id="cite-note-16" href="#cite-ref-16">[16]</a>
* [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang"), [Kuo-Yuan Kao](Kuo-Yuan_Kao "Kuo-Yuan Kao"), [Tai-Ning Yang](index.php?title=Tai-Ning_Yang&action=edit&redlink=1 "Tai-Ning Yang (page does not exist)") (**2012**). *[Bitboard Knowledge Base System and Elegant Search Architectures for Connect6](http://www.sciencedirect.com/science/article/pii/S0950705112001293)*. [Knowledge-Based Systems](https://www.journals.elsevier.com/knowledge-based-systems/), Vol. 34
* [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Hung-Jui Chang](Hung-Jui_Chang "Hung-Jui Chang"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2013**). *Multilevel Inference in Chinese Chess Endgame Knowledge Bases*. [ICGA Journal, Vol. 36, No. 4](ICGA_Journal#36_4 "ICGA Journal") » [Chinese Chess](Chinese_Chess "Chinese Chess"), [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Hung-Jui Chang](Hung-Jui_Chang "Hung-Jui Chang"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2014**). *Advanced Meta-knowledge for Chinese Chess Endgame Knowledge Bases*. [ICGA Journal, Vol 37, No. 1](ICGA_Journal#37_1 "ICGA Journal")
* [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2015**). *Quantifying Depth and Complexity of Thinking and Knowledge*. [ICAART 2015](http://www.icaart.org/EuropeanProjectSpace.aspx?y=2015), [pdf](http://www.cse.buffalo.edu/~regan/papers/pdf/BiReICAART15CR.pdf)


### 2020 ...


* [Thomas McGrath](index.php?title=Thomas_McGrath&action=edit&redlink=1 "Thomas McGrath (page does not exist)"), [Andrei Kapishnikov](index.php?title=Andrei_Kapishnikov&action=edit&redlink=1 "Andrei Kapishnikov (page does not exist)"), [Nenad Tomašev](index.php?title=Nenad_Toma%C5%A1ev&action=edit&redlink=1 "Nenad Tomašev (page does not exist)"), [Adam Pearce](index.php?title=Adam_Pearce&action=edit&redlink=1 "Adam Pearce (page does not exist)"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Been Kim](index.php?title=Been_Kim&action=edit&redlink=1 "Been Kim (page does not exist)"), [Ulrich Paquet](index.php?title=Ulrich_Paquet&action=edit&redlink=1 "Ulrich Paquet (page does not exist)"), [Vladimir Kramnik](index.php?title=Vladimir_Kramnik&action=edit&redlink=1 "Vladimir Kramnik (page does not exist)") (**2021**). *Acquisition of Chess Knowledge in AlphaZero*. [arXiv:2111.09259](https://arxiv.org/abs/2111.09259) » [AlphaZero](AlphaZero "AlphaZero") <a id="cite-note-17" href="#cite-ref-17">[17]</a>


## Forum Posts


### 1996 ...


* [Incoporating chess knowledge in chess programs](https://groups.google.com/d/msg/rec.games.chess.computer/47bgYzU2kyQ/BKAn9pqUtogJ) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 26, 1996
* [computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/99eec6923b0481db) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 1, 1997 » [Oracle](Oracle "Oracle")
* [Knowledge is not elegant](https://www.stmintz.com/ccc/index.php?id=20531) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), June 14, 1998
* [The end of computer chess progress?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/e917da2d88146756) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 06, 1999
* [The Limits of Positional Knowledge](https://www.stmintz.com/ccc/index.php?id=77234) by Michael Neish from [CCC](CCC "CCC"), November 11, 1999


### 2000 ...


* [suggestions for (a new generation of) chess knowledge using engines](https://www.stmintz.com/ccc/index.php?id=261167) by [Ingo Lindam](index.php?title=Ingo_Lindam&action=edit&redlink=1 "Ingo Lindam (page does not exist)"), [CCC](CCC "CCC"), October 23, 2002
* [likelihood instead of pawnunits? + chess knowledge](https://www.stmintz.com/ccc/index.php?id=261636) by [Ingo Lindam](index.php?title=Ingo_Lindam&action=edit&redlink=1 "Ingo Lindam (page does not exist)"), [CCC](CCC "CCC"), October 25, 2002
* [Knowledge](https://www.stmintz.com/ccc/index.php?id=389133) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 26, 2004


### 2005 ...


* [The superior Rybka chess knowledge](https://www.stmintz.com/ccc/index.php?id=480599) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), January 18, 2006 » [Rybka](Rybka "Rybka")
* [knowledge and blitz; search and long games](https://www.stmintz.com/ccc/index.php?id=486851) by Joseph Ciarrochi, [CCC](CCC "CCC"), February 15, 2006
* [Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?t=402) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 05, 2007 » [Search](Search "Search"), [Evaluation](Evaluation "Evaluation")


 [Re: Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?p=2944) by [Mark Uniacke](Mark_Uniacke "Mark Uniacke"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 14, 2007
### 2010 ...


* [hardware advances - a different perspective](http://www.talkchess.com/forum/viewtopic.php?t=36031) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 09, 2010
* [old crafty vs new crafty on new hardware](http://www.talkchess.com/forum/viewtopic.php?t=36040) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 11, 2010 » [Crafty](Crafty "Crafty")
* [Crafty tests show that Software has advanced more](http://www.talkchess.com/forum/viewtopic.php?t=36050) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 12, 2010
* [Final results - Crafty - hardware vs software](http://www.talkchess.com/forum/viewtopic.php?t=36059) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 13, 2010 » [Crafty](Crafty "Crafty")
* [Deep Blue vs Rybka](http://www.talkchess.com/forum/viewtopic.php?t=36058) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 13, 2010 » [Deep Blue](Deep_Blue "Deep Blue"), [Rybka](Rybka "Rybka")
* [hardware doubling number for Crafty](http://www.talkchess.com/forum/viewtopic.php?t=36088) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 15, 2010 » [Crafty](Crafty "Crafty")
* [Ahhh... the holy grail of computer chess](http://www.talkchess.com/forum/viewtopic.php?t=40166) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), August 23, 2011
* [Is search irrelevant when computing ahead of very big trees?](http://www.talkchess.com/forum/viewtopic.php?t=48743) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), July 24, 2013 » [Search](Search "Search")
* [Improve the search or the evaluation?](http://www.talkchess.com/forum/viewtopic.php?t=49190) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), August 31, 2013 » [Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge")
* [Slow Searchers?](http://www.talkchess.com/forum/viewtopic.php?t=49906) by Michael Neish, [CCC](CCC "CCC"), November 02, 2013
* [Chessprogams with the most chessknowing](http://www.talkchess.com/forum/viewtopic.php?t=54697) by Joe Boden, [CCC](CCC "CCC"), December 19, 2014


### 2015 ...


* [An attempt to measure the knowledge of engines](http://www.talkchess.com/forum/viewtopic.php?t=55752) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 23, 2015
* [Re: Chessprogams with the most chessknowing](http://www.talkchess.com/forum/viewtopic.php?t=54697&start=44) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), February 18, 2017


 [Re: Chessprogams with the most chessknowing](http://www.talkchess.com/forum/viewtopic.php?t=54697&start=46) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), February 18, 2017
 [Re: Chessprogams with the most chessknowing](http://www.talkchess.com/forum/viewtopic.php?t=54697&start=47) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), February 18, 2017 » [Komodo](Komodo "Komodo")
 [Re: Chessprogams with the most chessknowing](http://www.talkchess.com/forum/viewtopic.php?t=54697&start=50) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), February 19, 2017 » [Stockfish](Stockfish "Stockfish")
## External Links


### Knowledge


* [Knowledge from Wikipedia](https://en.wikipedia.org/wiki/Knowledge)
* [Knowledge acquisition from Wikipedia](https://en.wikipedia.org/wiki/Knowledge_acquisition)
* [Knowledge discovery from Wikipedia](https://en.wikipedia.org/wiki/Knowledge_discovery)
* [Knowledge engineering from Wikipedia](https://en.wikipedia.org/wiki/Knowledge_engineering)
* [Knowledge Engineering Environment from Wikipedia](https://en.wikipedia.org/wiki/Knowledge_Engineering_Environment)
* [Knowledge extraction from Wikipedia](https://en.wikipedia.org/wiki/Knowledge_extraction)
* [Knowledge management from Wikipedia](https://en.wikipedia.org/wiki/Knowledge_management)
* [Knowledge representation and reasoning from Wikipedia](https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning)
* [Knowledge transfer from Wikipedia](https://en.wikipedia.org/wiki/Knowledge_transfer)


### Related Topics


* [Awareness from Wikipedia](https://en.wikipedia.org/wiki/Awareness)
* [Belief from Wikipedia](https://en.wikipedia.org/wiki/Belief)
* [Cognition from Wikipedia](https://en.wikipedia.org/wiki/Cognition)
* [Consciousness from Wikipedia](https://en.wikipedia.org/wiki/Consciousness)
* [Data mining from Wikipedia](https://en.wikipedia.org/wiki/Data_mining)
* [Epistemology from Wikipedia](https://en.wikipedia.org/wiki/Epistemology)
* [Experience from Wikipedia](https://en.wikipedia.org/wiki/Experience)
* [Expert from Wikipedia](https://en.wikipedia.org/wiki/Expert)
* [Expert system from Wikipedia](https://en.wikipedia.org/wiki/Expert_system)
* [Imagination from Wikipedia](https://en.wikipedia.org/wiki/Imagination)
* [Instinct from Wikipedia](https://en.wikipedia.org/wiki/Instinct)
* [Intelligence from Wikipedia](https://en.wikipedia.org/wiki/Intelligence)
* [Intuition (philosophy) from Wikipedia](https://en.wikipedia.org/wiki/Intuition_%28philosophy%29)
* [Intuition (psychology) from Wikipedia](https://en.wikipedia.org/wiki/Intuition_%28psychology%29)
* [Learning from Wikipedia](https://en.wikipedia.org/wiki/Learning)
* [Mind from Wikipedia](https://en.wikipedia.org/wiki/Mind)
* [Ontology (information science) from Wikipedia](https://en.wikipedia.org/wiki/Ontology_%28information_science%29)
* [Paradigm from Wikipedia](https://en.wikipedia.org/wiki/Paradigm)
* [Philosophy from Wikipedia](https://en.wikipedia.org/wiki/Philosophy)
* [Philosophy of mind from Wikipedia](https://en.wikipedia.org/wiki/Philosophy_of_mind)
* [Psychology from Wikipedia](https://en.wikipedia.org/wiki/Psychology)
* [Science from Wikipedia](https://en.wikipedia.org/wiki/Science)
* [Scientia potentia est - knowledge is power - Wikipedia](https://en.wikipedia.org/wiki/Scientia_potentia_est)
* [Skill from Wikipedia](https://en.wikipedia.org/wiki/Skill)
* [Thought from Wikipedia](https://en.wikipedia.org/wiki/Thought)
* [Understanding from Wikipedia](https://en.wikipedia.org/wiki/Understanding)


### Types of Knowledge


* [A priori and a posteriori from Wikipedia](https://en.wikipedia.org/wiki/A_priori_and_a_posteriori)
* [Common knowledge from Wikipedia](https://en.wikipedia.org/wiki/Common_knowledge)
* [Common knowledge (logic) from Wikipedia](https://en.wikipedia.org/wiki/Common_knowledge_%28logic%29)
* [Declarative Knowledge](http://decisionautomation.com/glossary/14.php) from [Decision Automation Resources](http://decisionautomation.com/)
* [Descriptive knowledge from Wikipedia](https://en.wikipedia.org/wiki/Descriptive_knowledge)
* [Dispersed knowledge from Wikipedia](https://en.wikipedia.org/wiki/Dispersed_knowledge)
* [Distributed knowledge from Wikipedia](https://en.wikipedia.org/wiki/Distributed_knowledge)
* [Metaknowledge from Wikipedia](https://en.wikipedia.org/wiki/Metaknowledge)
* [Mutual knowledge (logic) from Wikipedia](https://en.wikipedia.org/wiki/Mutual_knowledge_%28logic%29)
* [Procedural knowledge from Wikipedia](https://en.wikipedia.org/wiki/Procedural_knowledge)
* [Teaching Declarative Knowledge](http://www.ehhs.cmich.edu/%7Ermscott/643declarative.html) by [Renay M. Scott](http://www.ehhs.cmich.edu/%7Ermscott/index.html)


### Musicvideos


* [Mahavishnu Orchestra](Category:Mahavishnu_Orchestra "Category:Mahavishnu Orchestra") - [You Know You Know](https://en.wikipedia.org/wiki/The_Inner_Mounting_Flame), August 17, 1972, more recent [3Sat](https://en.wikipedia.org/wiki/3sat) broadcast <a id="cite-note-18" href="#cite-ref-18">[18]</a>, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [John McLaughlin](Category:John_McLaughlin "Category:John McLaughlin"), [Billy Cobham](Category:Billy_Cobham "Category:Billy Cobham"), [Rick Laird](Category:Rick_Laird "Category:Rick Laird"), [Jan Hammer](Category:Jan_Hammer "Category:Jan Hammer"), [Jerry Goodman](https://en.wikipedia.org/wiki/Jerry_Goodman)
 
* [Biréli Lagrène](Category:Bir%C3%A9li_Lagr%C3%A8ne "Category:Biréli Lagrène") - Si Tu Savais, [Biréli Lagrène & Friends Live Jazz A Vienne 2002](http://www.djangostation.com/Live-Jazz-a-Vienne,060.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bc6), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). [One Jump Ahead](http://www.cs.ualberta.ca/%7Ejonathan/OJA/oja.html) *Challenging Human Supremacy in Checkers*, Springer, ISBN 0-387-94930-5, Prelude to Disaster, pp. 255-256 or pp. 249-250 in the [Second Edition, 2009](http://www.springer.com/computer/artificial/book/978-0-387-76575-4)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Andreas Junghanns](Andreas_Junghanns "Andreas Junghanns"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *Search versus knowledge in game-playing programs revisited*. [IJCAI-97](Conferences#IJCAI1997 "Conferences"), Vol 1, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.32.168&rep=rep1&type=pdf), 3 Search Versus Knowledge: Practise
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Hans Berliner](Hans_Berliner "Hans Berliner"), [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Carl Ebeling](Carl_Ebeling "Carl Ebeling") (**1989**). *Measuring the Performance Potential of Chess Programs*, [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Peter Kouwenhoven](Peter_Kouwenhoven "Peter Kouwenhoven") (**1987**). *Advances in Computer Chess, The 5th Triennial Conference*. [ICCA Journal, Vol. 10, No. 2](ICGA_Journal#10_2 "ICGA Journal") (report)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Hans Berliner](Hans_Berliner "Hans Berliner"), [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Carl Ebeling](Carl_Ebeling "Carl Ebeling") (**1990**). *[Measuring the Performance Potential of Chess Programs](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6TYF-47WTT8W-3J&_user=10&_coverDate=04%2F30%2F1990&_rdoc=1&_fmt=high&_orig=search&_origin=search&_sort=d&_docanchor=&view=c&_searchStrId=1541914346&_rerunOrigin=google&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=a43185e00b7d7d4550af0add28ff36b8&searchtype=a).* Artificial Intelligence, Vol. 43, No. 1
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Chess in 2010](http://www.rebel.nl/ches2010.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder"), The Berliner Experiment
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [The end of computer chess progress?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/e917da2d88146756) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 06, 1999
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Re: Intelligent software, please](https://www.stmintz.com/ccc/index.php?id=198940) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), November 26, 2001
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Schröder, Ed](http://www.schach-computer.info/wiki/index.php/Schr%C3%B6der,_Ed) (German) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) also refers the post by [Ed Schröder](Ed_Schroder "Ed Schroder")
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Re: Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?p=2944) by [Mark Uniacke](Mark_Uniacke "Mark Uniacke"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 14, 2007
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [UCI Machine Learning Repository: Chess (King-Rook vs. King-Pawn) Data Set](http://archive.ics.uci.edu/ml/datasets/Chess+%28King-Rook+vs.+King-Pawn%29)
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Patanjali from Wikipedia](https://en.wikipedia.org/wiki/Patanjali)
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1988**). [Alen D. Shapiro](Alen_Shapiro "Alen Shapiro"): *Structured Induction in Expert Systems*. [ICCA Journal, Vol. 11, No. 4](ICGA_Journal#11_4 "ICGA Journal")
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Knowledge discovery from Wikipedia](https://en.wikipedia.org/wiki/Knowledge_discovery)
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**2010**). *How can Humans learn from Computers?* Review on [Matej Guid's](Matej_Guid "Matej Guid") Ph.D. thesis, [ICGA Journal, Vol. 33, No. 4](ICGA_Journal#33_4 "ICGA Journal")
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Acquisition of Chess Knowledge in AlphaZero](https://en.chessbase.com/post/acquisition-of-chess-knowledge-in-alphazero), [ChessBase News](ChessBase "ChessBase"), November 18, 2021
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> Original [ZDF](https://en.wikipedia.org/wiki/ZDF) broadcast "[Sonntagskonzert](https://de.wikipedia.org/wiki/ZDF_Sonntagskonzert)", September 17, 1972, recorded at [Kongresshalle](http://www.abendzeitung-muenchen.de/inhalt.deutsches-museum-kongresshalle-wird-zur-event-location-gaudi-und-tralala.0fbdbcaa-3122-4466-a8b3-69a7de1bde68.html) [Deutschen Museum](https://en.wikipedia.org/wiki/Deutsches_Museum), [Munich](https://en.wikipedia.org/wiki/Munich), "Jazz Now", August 17, 1972, curator [Joachim-Ernst Berendt](http://alchetron.com/Joachim-Ernst-Berendt-780489-W), see [The Mahavishnu Orchestra On Film](http://www.bathedinlightning.com/bonus%20material/the_mahavishnu_orchestra_on_film.html), [MUENCHEN-72\_KPL.pdf](http://www.embryo.de/MUENCHEN-72_KPL.pdf), [Diese Woche im Fernsehen](http://www.spiegel.de/spiegel/print/d-42891878.html), [Der Spiegel](https://en.wikipedia.org/wiki/Der_Spiegel) 38/1972 (German), [1972 Summer Olympics](https://en.wikipedia.org/wiki/1972_Summer_Olympics)

**[Up one Level](Home "Home")**







 
