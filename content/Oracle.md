---
title: Oracle
---
**[Home](Home "Home") \* [Knowledge](Knowledge "Knowledge") \* Oracle**



[ [John William Waterhouse](Category:John_William_Waterhouse "Category:John William Waterhouse") - *Consulting the Oracle* [[1]](#cite_note-1)
**Oracle**,  

an instance with the fame of perfect knowledge, that is [evaluation](Evaluation "Evaluation") without [noise](https://en.wikipedia.org/wiki/Statistical_noise) or errors, a form of [divination](https://en.wikipedia.org/wiki/Divination), and a perfect supervisor in [learning](Learning "Learning"). For instance [endgame tablebases](Endgame_Tablebases "Endgame Tablebases") act like an oracle, providing the optimal moves. 



### Contents


* [1 Pre-processing](#Pre-processing)
* [2 Quotes](#Quotes)
	+ [2.1 Bruce Wright](#Bruce_Wright)
	+ [2.2 David Kittinger](#David_Kittinger)
	+ [2.3 Peter Gillgasch](#Peter_Gillgasch)
	+ [2.4 Chrilly Donninger](#Chrilly_Donninger)
	+ [2.5 Don Dailey](#Don_Dailey)
	+ [2.6 Ulrich Türke](#Ulrich_T.C3.BCrke)
	+ [2.7 Amir Ban](#Amir_Ban)
	+ [2.8 Don Dailey](#Don_Dailey_2)
	+ [2.9 Vincent Diepeveen](#Vincent_Diepeveen)
* [3 See also](#See_also)
* [4 Publications](#Publications)
* [5 Forum Posts](#Forum_Posts)
* [6 External Links](#External_Links)
* [7 References](#References)






A so called oracle approach is a knowledge instance applied at the [root](Root "Root") or the [interior](Interior_Node "Interior Node") of the [tree](Search_Tree "Search Tree") with some [depth](Depth "Depth") left to the [horizon](Horizon_Node "Horizon Node"), which guides [search](Search "Search") and [leaf evaluation](Evaluation "Evaluation") for specific features or [pattern](index.php?title=Pattern&action=edit&redlink=1 "Pattern (page does not exist)"), relevant in particular chess positions, and not in others. This applies to first order evaluation terms by initializing [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables"), also dubbed **Pre Scan Heuristics** [[2]](#cite_note-2) as propagated by [David Kittinger](David_Kittinger "David Kittinger"), as well as second order terms if related pattern match as described by [Hans Berliner](Hans_Berliner "Hans Berliner") in *Some Innovations Introduced by [HiTech](HiTech "HiTech")* [[3]](#cite_note-3). 


While [Pre-processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables") seems somewhat outdated with todays [search depths](Depth "Depth") in conjunction with [transposition table](Transposition_Table "Transposition Table") anomalies and resulting [search instabilities](Search_Instability "Search Instability"), Oracle approaches may be used to control [time management](Time_Management "Time Management"), to [order moves](Move_Ordering "Move Ordering"), or, as proposed by [Ronald de Man](Ronald_de_Man "Ronald de Man") in [scoring root moves](Ronald_de_Man#ScoringRootMoves "Ronald de Man") by slightly shifting the [alpha-beta windows](Window "Window") [[4]](#cite_note-4).



## Quotes


### Bruce Wright


[Bruce Wright](Bruce_Wright "Bruce Wright") on [pre-processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables") in [Duchess](Duchess "Duchess") [[5]](#cite_note-5)




```C++
One thing that we used to do with our chess program, [Duchess](Duchess "Duchess"), was to have a special routine that ran before the [main search](Search "Search") that identified strong and weak points in each side's respective position - weak squares, [passed pawns](Passed_Pawn "Passed Pawn"), weak [king protection](King_Safety "King Safety"), etc, and tried to grow trees of moves to protect our own weak squares or attack the opponent's weak squares. These would be just sequences of moves by our own or our opponent's  pieces and pawns to reach the targeted squares. A table was build for the value of reaching each of these goals for each type of piece and for reaching the middle points along the paths (the value diminishing the further they were from the goal). Then during the search the program would get bonus points for reaching some of the intermediate points in the plan.

```


```C++
This seemed most useful in the [endgame](Endgame "Endgame") when actually reaching the culmination of a play might be beyond the [search depth](Depth "Depth"), and where [tactics](Tactics "Tactics") did not dominate as much as they do in the [middle game](Middlegame "Middlegame"); for example, Duchess was quite capable of finding long King maneuvers that might take the King far away from simpleminded heuristics such as "[centralize the King in the endgame](King_Centralization "King Centralization")" and that were too deep to be found by a direct search. It wasn't perfect; it could not take into account the changes in strategy that might be dictated by a radically different structure encountered deep in the search, but it seemed to be better than nothing. 

```

### David Kittinger


[David Kittinger](David_Kittinger "David Kittinger") and [Scott McDonald](Scott_McDonald "Scott McDonald") in 1984 on [Pre Scan Heuristics](Piece-Square_Tables#Preprocessing "Piece-Square Tables") of the [Super Constellation](Super_Constellation "Super Constellation") [[6]](#cite_note-6)




```C++
A second departure from other commercial programs has been the simplification of the [evaluation function](Evaluation_Function "Evaluation Function") as applied to the [end nodes](Leaf_Node "Leaf Node") of the tree [search](Search "Search"). The programs instead rely heavily on specific chess [knowledge](Knowledge "Knowledge") which is concentrated into a special [preprocessor](Piece-Square_Tables#Preprocessing "Piece-Square Tables") which interfaces to the tree search primarily through the [scores](Score "Score") associated with specific ply-one [moves](Moves "Moves"). This ides of a ply-one move preprocessor was originally implemented in the program [Tech](Tech "Tech") by [James Gillogly](James_Gillogly "James Gillogly") in the late 1960s. Although Tech only achieved a high 1400 rating running on a large computer, the strategy has certain appeal. First, chess tree searching has become very efficient, and second, the interaction problems associated with putting ever increasing amounts of chess knowledge in the tree become formidable. It has become apparent to that this rather simple approach might contain the structure of a master level microcomputer program. 

```

### Peter Gillgasch


[Peter Gillgasch](Peter_Gillgasch "Peter Gillgasch") on [DarkThought's](DarkThought "DarkThought") Oracle, February 1996 [[7]](#cite_note-7)




```C++
After toying with horrible slow code that did endpoint evaluations for the pieces I got the idea (as many did before, but I swear I didn't know that and hence I was quite proud of it) to analyze the root position and to modify the [piece/square table](Piece-Square_Tables "Piece-Square Tables") relative to [pawn structure](Pawn_Structure "Pawn Structure") and king locations. The piece/square table scores were also used for [move ordering](Move_Ordering "Move Ordering") to cut down the tree size (this helped a lot since it is basically using the evaluation to order the moves at close to no cost).

```


```C++
Of course the program played **much** better than before but it had serious trouble when the pawn structure was highly flexible and if there was a way to lock its bishops with own pawns it was guaranteed to like exactly this line ;)

```


```C++
Later the three of us modified the oracle code (to use Berliner's term) and we where quite successful with it - DarkThought started to beat commercial PC programs. But it was quite hard to make further progress, so a lot of knowledge was moved to the endpoint evaluation up to the point that there was basically no oracle code left. This improved [playing strength](Playing_Strength "Playing Strength") but it was always my impression that we suffered in the "[tactical](Tactics "Tactics")" aspect a bit since the search was no longer fast as hell and I was never convinced that going this way was the best decision. 

```





### Chrilly Donninger


Quote by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") from *CHE: A Graphical Language for Expressing Chess Knowledge*, 1996 [[8]](#cite_note-8)




```C++
The main design criterion for successor [Nimzo-3](Nimzo "Nimzo") was combining the positional play of Nimzo-2 with the [tactical](Tactics "Tactics") strength of a program like [Fritz](Fritz "Fritz"). Nimzo-2 was developed on an [486/50 MHz](X86 "X86") [PC](IBM_PC "IBM PC"), which calculated about 3,000 [nodes per second](Nodes_per_Second "Nodes per Second"). Thereof 60 to 70 percent was spent/wasted in the [leaf evaluation](Evaluation "Evaluation") routines. Hence, a major improvement in speed and thus in tactical strength could only be obtained by performing most of the evaluation either in the root or the interior of the [search tree](Search_Tree "Search Tree"). So, Nimzo-3 became a [Genius](Chess_Genius "Chess Genius")/[Fritz](Fritz "Fritz")-like program with a complex root evaluation, called Oracle, similar to [Berliner's](Hans_Berliner "Hans Berliner") Oracle, and with a very simple, mainly first order evaluation at the [leaves](Leaf_Node "Leaf Node") [[9]](#cite_note-9). Nimzo-3 spends about 10 to 20% on leaf evaluation, its node rate has increased by 400% up to 12,000 nodes/second on the same hardware. 

```

### Don Dailey


[Don Dailey](Don_Dailey "Don Dailey") on [Pre-processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables"), May 1998 [[10]](#cite_note-10) :





|  |
| --- |
|  The term pre-processing is normally used in the context of an evaluation function. It's a process where you make most of your evaluation decisions BEFORE the [search](Search "Search") begins. Typically you determine where each piece should go and essentially build a 64 square table for each piece type of each color on the chess board. You might decide that the c file is [open](Open_File "Open File") and so you give rooks a big bonus if they can get to the c file. Once you make this decision it doesn't change during the search. So if the c file suddenly gets blocked during the search, the rooks won't know this and still try to get on the c file.
Pre-processing has many advantages and disadvantages. Here is a list of them:
**Pro's**
* Very fast, evaluation almost free.
* Trivial to implement.
* Can put huge amounts of knowledge in chess program with essentially no slowdown. This is because all the real work is done in a fraction of a second before the search begins.
* Especially good with [pawn patterns](Pawn_Pattern_and_Properties "Pawn Pattern and Properties"). (but not [pawn structure](Pawn_Structure "Pawn Structure"))

**Con's**
* The evaluation is very dependent on the [starting position](Root "Root"). Deeper searches suffer more than shallow one. Ironically, you can do deeper searches if you do lots of pre-processing.
* Very difficult to put in dynamic endings where relationships change quickly.
* Concepts like [mobility](Mobility "Mobility") are covered very inexactly. Pawn structure terms cannot be calculated with any reliability.
* Makes it problematic whether to use [hash table](Transposition_Table "Transposition Table") aging because it affects the hash tables in strange ways. The problem is that 2 identical positions can have different scores if they are descendants of different starting positions.

There are probably other pro's and con's I didn't think of. Many really good programs use this method, but almost always there is a mixture of pre-processing with more dynamic stuff like pawn structure which might be hashed, or calculated quickly with incremental updating schemes. There is quite a bit of diversity and opinion on this subject. Some swear by it and others shun it completely. I don't use it any more but my older programs did. My feeling is that with ever increasing depth, it becomes more and more troublesome. Imagine a program doing 60 ply searches. The end nodes of the tree will not bear very much resemblance to the initial position where the decisions were made. But since we don't usually look 60 ply deep pre-processing is still a workable method.
But I believe you can still write very strong programs that do a substantial amount of pre-processing. [Fritz](Fritz "Fritz") is one example. [Genius](Chess_Genius "Chess Genius") also does substantial pre-processing. I think probably more programs use this than not. My old program [RexChess](RexChess "RexChess") was almost all pre-process with a little dynamic pawn structure mixed in! Pre-processing does not necessarily have to be pure piece/sq tables. You can make other evaluation decisions in advance too and prepare them for fast execution during the search. 
 |


### Ulrich Türke


Reply by [Ulrich Türke](Ulrich_T%C3%BCrke "Ulrich Türke") [[11]](#cite_note-11) :




```C++
I too think that pre-processing is still done in most of the current chess programs, more or less. I am considering the possibility of a moderated pre-processing, i. e. apply the time-consuming pre-processing evaluation parts not at the root but to nodes at [depth](Depth "Depth") - say - the half of the aimed search depth. Thus, one would still have the main advantage, saving a lot of calculation time, because the number of pre-processed nodes would still be a microscopic fraction of the [leaf nodes](Leaf_Node "Leaf Node"). But on the other hand, the pre-processed knowledge would be applied to nodes being far closer to the leaf nodes (in your examples "only" 30 ply instead of 60). Opinions? 

```

### Amir Ban


Note by [Amir Ban](Amir_Ban "Amir Ban") [[12]](#cite_note-12) :




```C++
It's a fair but simplistic description of [Junior](Junior "Junior"). 

```

### Don Dailey


[Don Dailey](Don_Dailey "Don Dailey") again [[13]](#cite_note-13) :




```C++
I've been considering this type of approach for a long time. I think it definitely has merit. It would suffer from [hash table](Transposition_Table "Transposition Table") anomalies but there are ways to deal with this, the primary one to simply ignore them.

```


```C++
There are a few issues to be dealt with but my feeling is that you might do well with this scheme. Scoring might be a little fuzzy at times but that might be ok. Probably the scheme would be to pre-process at every level up to MAX_DEPTH-n, where n might be at least 3 or 4 ply. Keep in mind that pre-processing is incredibly expensive even compared to fully dynamic processing, so I suspect you cannot get very close to the leaf nodes. Of course 3 or 4 ply away might be considered pretty close if you were doing 14 ply searches.

```


```C++
The way I got this idea (which I'm not taking credit for) actually began when I was programming the ending [Bishop and Knight vs King](KBNK_Endgame "KBNK Endgame") with a pre-processor program of mine a few years ago. This is a very good exercise for someone wanting to understand some of the difficulties of pre-processing. I tested with a 3 ply search, and tuned the thing up to do quite well. But it turned out to not work so well at other levels! It turns out that no matter what table you use, they will tend to be optimum for a specific depth only. It was almost funny because I kept figuring out which positions in the search were messing it up and changed the tables accordingly. These anticipations were wrong though at different levels! Finally though, I extracted the most general principles possible and created a table that was almost static (not based as much on the placing of the pieces) and it did ok, but not as good as the depth specific ones. Some pre-processors will suggest a move and for this ending that would work well. The idea is to give a bonus to the whole search tree under some root move. For example I might give a small bonus for playing any move that's a pin. This makes the program slightly in favor of playing a pin. I call these "ply 1 incentives" but there is probably better terminology in use. This is also another example of pre-processing. See note at end of my post.

```


```C++
But your idea would solve this and a host of other problems. You could make very good guesses about configurations if you knew the possible changes to a position were limited. This would enable you to be more aggressive about the knowledge you included.

```


```C++
Here is another idea I had which is more dynamic in nature. It occurred to me that you could do a fairly decent evaluation based on pawn position only, the idea being a separate set of tables for each pawn structure. These could be built by the pawn structure hash table mechanism most programs have. Most pieces can be judged well by the pawn structure around them.

```


```C++
I did not pursue this idea because I fear it may still be too slow. If my hash table hit rate was say 95 percent, then 1/20 of the positions would require a pre-processing step. While this does not seem like much, you have to consider how expensive building the table is. It's pretty expensive, especially if you want sophistication. But on top of that you must recompute the positional score each time the pawn structure changes, EVEN if the table itself is ready to go. This should be fairly fast but not trivial in terms of execution speed. You have already killed some of the speed you were hoping to gain. Is the idea workable? Maybe, but I'm skeptical. Also, the pawn structure is not the only relevant factor so other evaluation would not doubt be needed. For instance you cannot look at the pawn structure and know for sure that you are in an endgame. You could make assumptions though based on the exact position you had when you built the tables.

```


```C++
Anyway the idea is interesting and I sometimes toy with the idea of trying it out, but it seems like a lot of work for an experiment that may not pay off. It could well be that someone dedicated to making it work might find imaginative solutions to some of the problems. But your idea may be more sound. It may very well be that some are using it. I've never heard of a specific example of it though. 

```


```C++
I think an old program called [Tech](Tech "Tech") used the method of "ply 1 move incentives." There was no evaluation at all (the way I remember it) except for [material](Material "Material") value and a list of moves was prepared in order of goodness from a pre-processor at the root. The program simply played the first move it came to in the move list that was at least as good tactical as any other. I'll bet [Bob Hyatt](Robert_Hyatt "Robert Hyatt") knows about this one. I had a nice discussion once with [the programmer](James_Gillogly "James Gillogly") when he was giving a talk on [hash table collisions](Transposition_Table#bits "Transposition Table") in chess programs. 

```

### Vincent Diepeveen


[Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen") on [Pre-processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables"), October 2000 [[14]](#cite_note-14)





|  |
| --- |
|  It's pretending you know in advance what is the best move and just let the program figure out the tactics. It's fast and of course my first line is a rude outline of what it is, but it's definitely no compare to a leaf evaluation.
So the 2 things against each other:
* Prescan heuristics/ piece square tables:

 fill a table BEFORE you search and apply there the knowledge, so for example for each piece at each square and in your [makemove](Make_Move "Make Move") only add the score from the tables and do nothing in your leafs (don't see why one would need a [qsearch](Quiescence_Search "Quiescence Search") in fact for such programs a 'guess' function should be plenty enough). No evaluation needed. Even [passers](Passed_Pawn "Passed Pawn") you can easily do [incremental](Incremental_Updates "Incremental Updates"), no problem.* Leaf eval: you can sure use the makemove to build up data structures, but the evaluation is NOT dependent upon the moves made, but only upon the position and you go scan the board position in each leaf for chess knowledge.

So the big difference is for example when exchanging queen: [Chess Tiger](Chess_Tiger "Chess Tiger") used (don't know whether it's still a pre-processor) to be happy before queen exchange, then after queen exchange it's suddenly very unhappy. Old [Fritz](Fritz "Fritz") versions except the latest 6a, 6b etcetera were also pre-processors.
Of course many programmers figured out that using a pre-processor only is very hard to play chess, so usually a few big scores they do in eval like passed pawns. Many old programs simply had no king safety at all.
[Nimzo](Nimzo "Nimzo") is a classical case of pre-processing too. if you checkout its book you'll see it hardly plays openings with very tough pawn structures without having all tough lines in book, as otherwise the pre-processor makes big mistakes as it doesn't see the position change in the root of course.
Now where is the big advantage of pre-processors apart that you can do it faster, why have they been so pretty successful in the past? I think very important reason is that it's also very easy to debug a pre-processor when comparing that with a leaf evaluation. 
 |


## See also


* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [Incremental Updates](Incremental_Updates "Incremental Updates")
* [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
* [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
* [Piece-Square Tables | Pre-processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables")
* [Ronald de Man | Scoring Root Moves](Ronald_de_Man#ScoringRootMoves "Ronald de Man")


## Publications


* [James Gillogly](James_Gillogly "James Gillogly") (**1972**). *The Technology Chess Program*. Artificial Intelligence, Vol. 3, pp. 145-163. ISSN 0004-3702. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**1986**). *Fuzzy Production Rules in Chess*. [ICCA Journal, Vol. 9, No. 4](ICGA_Journal#9_4 "ICGA Journal")
* [Hans Berliner](Hans_Berliner "Hans Berliner") (**1987**). *Some Innovations Introduced by Hitech*. [ICCA Journal, Vol. 10, No. 3](ICGA_Journal#10_3 "ICGA Journal")
* [Hans Berliner](Hans_Berliner "Hans Berliner") (**1989**). *Some Innovations Introduced by Hitech*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")
* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1996**). *CHE: A Graphical Language for Expressing Chess Knowledge*. [ICCA Journal, Vol. 19, No. 4](ICGA_Journal#19_4 "ICGA Journal")


## Forum Posts


* [computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/99eec6923b0481db) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 1, 1997


 [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/0df39371422a600c) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 3, 1997
 [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/ccc2546e26d92f88) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997
* [What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18179) by Howard Exner, [CCC](CCC "CCC"), May 07, 1998


 [Re: What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18181) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 07, 1998
* [Preprocessing vs leaf evaluating - any preprocessors left?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ce25565232355c61) by [Tom King](Tom_King "Tom King"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 05, 1998
* [Ply 1 scoring factors](https://www.stmintz.com/ccc/index.php?id=35000) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), December 07, 1998
* [Re: What is Prescan Heuristics ??](https://www.stmintz.com/ccc/index.php?id=132894) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), October 13, 2000


## External Links


* [Oracle from Wikipedia](https://en.wikipedia.org/wiki/Oracle)
* [Oracle (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Oracle_%28disambiguation%29)
* [Oracle (software testing) from Wikipedia](https://en.wikipedia.org/wiki/Oracle_%28software_testing%29)


 [ORACLE (computer) from Wikipedia](https://en.wikipedia.org/wiki/ORACLE_%28computer%29)
* [Oracle machine from Wikipedia](https://en.wikipedia.org/wiki/Oracle_machine)
* [Matroid oracle from Wikipedia](https://en.wikipedia.org/wiki/Matroid_oracle)
* [Prophecy from Wikipedia](https://en.wikipedia.org/wiki/Prophecy)
* [Oracle Corporation from Wikipedia](https://en.wikipedia.org/wiki/Oracle_Corporation)
* [Oracle Database from Wikipedia](https://en.wikipedia.org/wiki/Oracle_Database)
* [Michael Hedges](Category:Michael_Hedges "Category:Michael Hedges") - [Oracle](https://en.wikipedia.org/wiki/Oracle_%28Michael_Hedges_album%29) / Fusion of the Five Elements, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) Consulting the Oracle by [John William Waterhouse](Category:John_William_Waterhouse "Category:John William Waterhouse"), 1884, showing eight priestesses in a temple of prophecy, [Oracle from Wikipedia](https://en.wikipedia.org/wiki/Oracle)
2. [↑](#cite_ref-2) [PSH](http://www.schach-computer.info/wiki/index.php/PSH) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
3. [↑](#cite_ref-3) [Hans Berliner](Hans_Berliner "Hans Berliner") (**1987**). *Some Innovations Introduced by Hitech*. [ICCA Journal, Vol. 10, No. 3](ICGA_Journal#10_3 "ICGA Journal")
4. [↑](#cite_ref-4) [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/ccc2546e26d92f88) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997
5. [↑](#cite_ref-5) [Bruce C. Wright](Bruce_Wright "Bruce Wright") (**1996**). *Routines prior to Main Search*. [Computer Chess Reports](Computer_Chess_Reports "Computer Chess Reports"), Vol. 5, Nos. 3+4, p. 102
6. [↑](#cite_ref-6) [David Kittinger](David_Kittinger "David Kittinger") and [Scott McDonald](Scott_McDonald "Scott McDonald") (**1984**). *Report from the U.S. Open*. [Computer Chess Digest Annual 1984](Computer_Chess_Reports "Computer Chess Reports") pp. 15-33
7. [↑](#cite_ref-7) [Drawn games (Was Re: Transposition table)](http://groups.google.com/group/rec.games.chess.computer/msg/b8bdef757df5d5c9) by [Peter Gillgasch](Peter_Gillgasch "Peter Gillgasch"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 06, 1996
8. [↑](#cite_ref-8) [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1996**). *CHE: A Graphical Language for Expressing Chess Knowledge*. [ICCA Journal, Vol. 19, No. 4](ICGA_Journal#19_4 "ICGA Journal")
9. [↑](#cite_ref-9) This approach seems to have been invented by [Kaare Danielsen](Kaare_Danielsen "Kaare Danielsen") for his program [CXG Advanced Star Chess](CXG_Star_Chess#Advanced "CXG Star Chess"), Quote from [Donninger's](Chrilly_Donninger "Chrilly Donninger") CHE paper
10. [↑](#cite_ref-10) [Re: What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18181) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 07, 1998
11. [↑](#cite_ref-11) [Re: What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18203) by [Ulrich Türke](Ulrich_T%C3%BCrke "Ulrich Türke"), [CCC](CCC "CCC"), May 08, 1998
12. [↑](#cite_ref-12) [Re: What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18213) by [Amir Ban](Amir_Ban "Amir Ban"), [CCC](CCC "CCC"), May 08, 1998
13. [↑](#cite_ref-13) [Re: What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18209) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 08, 1998
14. [↑](#cite_ref-14) [Re: What is Prescan Heuristics ??](https://www.stmintz.com/ccc/index.php?id=132894) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), October 13, 2000

**[Up one Level](Knowledge "Knowledge")**







 
