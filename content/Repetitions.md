---
title: Repetitions
---
**[Home](Home "Home") \* [Search](Search "Search") \* Repetitions**



 [](http://www.mcescher.com/Gallery/back-bmp/LW327.jpg) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Reptiles, 1943 [[1]](#cite_note-1) 
**Repetitions** of [positions](Chess_Position "Chess Position") may happen during [game play](Chess_Game "Chess Game") and inside the [search](Search "Search") of a chess program due to [reversible moves](Reversible_Moves "Reversible Moves") played from both sides, which might be nullified in one or multiple further reversible moves. The player to move **may** claim a [draw](Draw "Draw") if the same position occurs **three** times, or will occur after an intended move, in any order, with the same player to move. 


Two positions are considered same or equal, if all occupied squares and kind of [pieces](Pieces "Pieces") (not necessarily the same piece) they occupy are the same, the [castling rights](Castling_Rights "Castling Rights") for both sides did not change, and no [en passant capture](En_passant "En passant") was possible during the first occurrence, even if obviously not played. 



### Contents


* [1 Assigning Draw Score](#Assigning_Draw_Score)
* [2 Rules](#Rules)
	+ [2.1 Fide Rule](#Fide_Rule)
	+ [2.2 Since July 01, 2014](#Since_July_01.2C_2014)
	+ [2.3 Former Rule](#Former_Rule)
* [3 Repetition of Positions](#Repetition_of_Positions)
	+ [3.1 Transposition Table](#Transposition_Table)
	+ [3.2 List of Keys](#List_of_Keys)
	+ [3.3 Dedicated Hash Table](#Dedicated_Hash_Table)
* [4 Repetition of Moves](#Repetition_of_Moves)
* [5 See also](#See_also)
* [6 Publications](#Publications)
	+ [6.1 1929](#1929)
	+ [6.2 1980 ...](#1980_...)
	+ [6.3 1990 ...](#1990_...)
	+ [6.4 2000 ...](#2000_...)
	+ [6.5 2010 ...](#2010_...)
* [7 Forum Posts](#Forum_Posts)
	+ [7.1 1990 ...](#1990_..._2)
	+ [7.2 1995 ...](#1995_...)
	+ [7.3 2000 ...](#2000_..._2)
	+ [7.4 2005 ...](#2005_...)
	+ [7.5 2010 ...](#2010_..._2)
	+ [7.6 2015 ...](#2015_...)
	+ [7.7 2020 ...](#2020_...)
* [8 External Links](#External_Links)
* [9 References](#References)






Threefold repetition implies a position occurred thrice, that is repeated twice. When to score the position as a draw, however, is an entirely different matter. Most programs do this on the first repetition, no matter whether the first occurrence of the repeated position appears in the current search space, or not. Other programs consider that fact, they avoid [cycles](https://en.wikipedia.org/wiki/Cycle_%28graph_theory%29) inside the current [search tree](Search_Tree "Search Tree") to make it a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG), but allow a one-fold repetition, if the first occurrence appears in the game history before the current [root](Root "Root"). Anyway, to wait for the second repetition one has its pros and cons. The Repetition score is either zero or the [contempt factor](Contempt_Factor "Contempt Factor").



## Rules


The [rules of chess](Rules_of_Chess "Rules of Chess") state a [threefold repetition](https://en.wikipedia.org/wiki/Threefold_repetition) of a [position](Chess_Position "Chess Position") gives the [player to move](Side_to_move "Side to move") the option to claim a draw, no matter whether the threefold repetition already occurred yet, or is about to occur after declaring the intended move in conjunction with the draw claim. The latter case is a bit tricky for computers, and is/was likely not strictly implemented in most programs or their [user interfaces](User_Interface "User Interface"), since a draw message text or box appeared after the repetition occurs but no claim before. Since July 2014 a fivefold repetition is sufficient without any claim [[2]](#cite_note-2).



### Fide Rule


[[3]](#cite_note-3)




```
9.2 The game is drawn, upon a correct claim by the player having the move, when the same position, for at least the third time (not necessarily by a repetition of moves)
 a) is about to appear, if he first writes his move on his [scoresheet](Game_Notation "Game Notation") and declares
    to the arbiter his intention to make this move, or
 b) has just appeared, and the player claiming the draw has the move.
Positions as in (a) and (b) are considered the same, if the same player has the move, pieces of the same kind and color occupy the same squares, and the possible moves of all the pieces of both players are the same. Positions are not the same if a pawn that could have been captured en passant can no longer in this manner be captured or if the right to castle has been changed temporarily or permanently. 

```

### Since July 01, 2014



```
9.6  If one or both of the following occur(s) then the game is drawn: 
 a) the same position has appeared, as in 9.2b, for at least five consecutive alternate moves by each player.  
 b) any consecutive series of 75 moves have been completed by each player without the movement of any pawn 
    and without any capture. If the last move resulted in checkmate, that shall take precedence. 

```

### Former Rule


A former (German) rule, was believed to be sufficient to make the game of chess finite [[4]](#cite_note-4) :




```
A chess game ends with a draw if a sequence of moves - with all pieces in exactly the same positions - is played three times successively. 

```

was proved not sufficient by [Max Euwe](Max_Euwe "Max Euwe") in 1929 by applying the [Prouhet–Thue–Morse Sequence](Max_Euwe#ProuhetThueMorseSequence "Max Euwe") [[5]](#cite_note-5) , i. e. with following move indices [[6]](#cite_note-6) :





|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  0
 |  Nb1-c3
 |  Nb8-c6
 |  Nc3-b1
 |  Nc6-b8
 |
|  1
 |  Ng1-f3
 |  Ng8-f6
 |  Nf3-g1
 |  Nf6-g8
 |


Euwe's prove was the reason, two other rules in force each of which guarantees chess to be a finite game, [threefold repetition](https://en.wikipedia.org/wiki/Threefold_repetition) of positions and the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule").




## Repetition of Positions


By [position](Chess_Position "Chess Position") we mean the location of all the [pieces](Pieces "Pieces") on the [Chessboard](Chessboard "Chessboard") as well as [castling rights](Castling_Rights "Castling Rights") and [en passant](En_passant "En passant") status. Since the rule speaks about the piece position, and not their identity (i.e. artificially constructed repeated position where the rooks of one player changed places still would be a draw), repetition may be detected by using the [Zobrist-](Zobrist_Hashing "Zobrist Hashing") or [BCH signatures](BCH_Hashing "BCH Hashing") of the position.



### Transposition Table


One possible implementation was used by [Ken Thompson](Ken_Thompson "Ken Thompson") in [Belle](Belle "Belle"), who told [Bruce Moreland](Bruce_Moreland "Bruce Moreland") that he detected repetitions by using the [transposition hash table](Transposition_Table "Transposition Table"), as follows [[7]](#cite_note-7) :




```
The idea is to set an "open" flag in the position's transposition table element when the hash table is probed. This flag stays set until the position is no longer being searched, meaning when the search function returns a value for that position.

```


```
At any given time, the only nodes that are "open" are nodes that are in the game history, or are in the current line in the tree search, so if the hash table probe encounters an open node, it must be because the current position has occurred somewhere before

```


```
This has the advantage that it uses data structures that are already present in the typical chess program, but there are a few problems with this idea. The hash table element must be written when a node is entered, so an "always replace" scheme must be used. This isn't a problem for Thompson, since his scheme involves using an "always replace" table, but other implementations might not use this kind of replacement scheme. Another problem is that there can be hash table entry collisions, and they must be dealt with. I am not talking about hash key collisions which occur when two positions map to the same 64-bit key, I'm talking about when two particular positions want to share the same hash table element, which should be pretty common. If two open nodes that want to share the same hash element, it's not immediately obvious what to do, other than not detect repetitions on the second one. Perhaps this problem could be dealt with via a re-hashing scheme, but this seems like an annoying thing to add in order to support functionality that isn't central to what the transposition table should be doing. A final problem is that it is hard to figure out how to adapt this to a [multiprocessor search](Parallel_Search "Parallel Search") where there might be several search [threads](Thread "Thread") accessing the same hash table. When an open node is encountered, it might not indicate a repetition at all, since it could belong to a line being searched by another processor. This problem sounds complicated to solve. 

```





### List of Keys


Most programs use an [array](Array "Array") or list of Zobrist- or BCH-keys and compare the current signature with keys 4, 6, 8 and so on [plies](Ply "Ply") along the actual variation. This is usually quite cheap, since testing often does not require looking through the entire list, since [captures](Captures "Captures") and [pawn moves](Pawn_Push "Pawn Push"), that reset the [halfmove clock](Halfmove_Clock "Halfmove Clock") for the purpose of enforcing [fifty-move rule](Fifty-move_Rule "Fifty-move Rule") are known to make a repetition impossible. Since each thread or process may own its own copy of the game-record, this approach has also some merits in [parallel search](Parallel_Search "Parallel Search") implementations.


[John Stanback](John_Stanback "John Stanback") about his implementation in [Zarkov](Zarkov "Zarkov") [[8]](#cite_note-8):




```
In Zarkov I simply keep 32 bits of [hash](Zobrist_Hashing "Zobrist Hashing") for each move in the [game history](Chess_Game#GameRecord "Chess Game"), whether it has actually occurred on the board or during the current search. I also have a variable that contains the [ply](Ply "Ply") at which the last [irreversible move](Irreversible_Moves "Irreversible Moves") occurred.  At each [node](Node "Node") in the search, including [quiescence](Quiescence_Search "Quiescence Search"), if the current ply is at least 4 plies beyond the last irreversible move I test the current hash value against those for each position in the game history (for the current side to move only) back to the last irreversible move and count the number of matches (repetitions).  

```


```
If the count is 2, then this is the third repetition and a draw score is returned.  If the count is 1 and the current_ply > root_ply+2 then a draw score is also returned. This avoids problems that can occur if the program thinks that a move at the [root](Root "Root") leads to a draw (due to a single repetition) when the opponent may vary, but it also lets the program treat repeated positions in the search as draws which helps a lot. Since most positions in a search are less than 4 plies beyond the last irreversible move the repetition() function is rarely called and the performance hit for detecting repetitions is negligible. 

```





### Dedicated Hash Table


Some programs, like [Gerbil](Gerbil "Gerbil") or [Rookie](Rookie "Rookie") use a separate small [hash table](Hash_Table "Hash Table"), actually an implementation of a [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) revealed by [Ronald de Man](Ronald_de_Man "Ronald de Man") as mentioned by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") in his thesis *The design and implementation of the Rookie 2.0 Chess Playing Program* [[9]](#cite_note-9):




```
It is tempting to use the transposition table to help detecting repeated positions. However, overloaded transposition tables can lose entries. So we choose something else [[10]](#cite_note-10)[[11]](#cite_note-11) : a dedicated, small, repetition hash table. This tables has 2^14 one-byte entries that are initially zero (totaling 16KB). When entering a new position, the low 14 bits of the hash-key are used to index the table and bump up its value by one. The value is restored after unmaking the move. When entering a node and its value is found to be non-zero already, we know there could be a cycle, which we verify by tracing back the actual variation. The repetition table is large enough to sufficiently reduce the number of false hits and this vaporizes the costs of futile back-traces. 

```





## Repetition of Moves


An alternative, pragmatical approach based on repetitions of [moves](Moves "Moves") was proposed by [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") and [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović") in 2004, as implemented in [Axon](Axon "Axon") [[12]](#cite_note-12) and discussed in [CCC](CCC "CCC") [[13]](#cite_note-13) [[14]](#cite_note-14). 


The algorithm needs a [move list](Move_List "Move List") containing the [game record](Chess_Game#GameRecord "Chess Game") including the variation actually [searched](Search "Search"), 16-bit entries with [origin](Origin_Square "Origin Square") and [target square](Target_Square "Target Square"), and a flag whether a move is [irreversible](Irreversible_Moves "Irreversible Moves"), as only information required. Starting with the last move made, the list is scanned backwards as long there are [reversible moves](Reversible_Moves "Reversible Moves"). A local concatenating list of up to 24 entries (one entry for each piece able to make reversible moves) is used to determine cycles per piece, where consecutive moves on their target squares are merged to one "pseudo" move, using the earliest origin and the latest target square. If all distinct white and black moving pieces in the chain list contain equal from- and to coordinates, all cycles of moves are closed and a move repetition is detected. This is how the algorithm as given in the paper in [8086](8086 "8086") [assembly](Assembly "Assembly") looks in pseudo [C++](Cpp "Cpp"), square coordinates are offset from a 12\*12 [mailbox](Mailbox "Mailbox") approach, so that empty entries have no valid square index. 




```

bool repetition(SMove *pVariant) {
   SMove chainList[24], m;
   short c = 0, i;

   for (i=0; i < 24; ++i) {
      chainList[i].setEmpty();
   }

l: m = *pVariant--; /* fetch move and decrement move list pointer */
   if ( m.isReversible() ) { 
      /* lookup chain list for from-coordinate that match current to coordinate */
      for (i=0; i < 24; ++i) {
         if ( m.to == chainList[i].from ) {
            if ( m.from == chainList[i].to ) {
              if ( --c == 0 )
                  return true; /* repetition detected */
               chainList[i].setEmpty();
               goto l;
            } 
            chainList[i].from = m.from; /* concatenate moves */
            goto l;
         }
      }
      /* lookup for next empty slot, to add the current move in the chain list */
      for (i=0; i < 24; ++i) {
         if ( chainList[i].isEmpty() ) {
            chainList[i] = m;
            ++c;
            goto l;
         }
      }
   }
   return false;
}

```

## See also


* [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Desperado](Stalemate#Desperado "Stalemate")
* [Draw](Draw "Draw")
* [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
* [Graph History Interaction](Graph_History_Interaction "Graph History Interaction") (GHI)
* [Path-Dependency](Path-Dependency "Path-Dependency")
* [Perpetual Check](Check#Perpetual "Check")
* [Pursuit](index.php?title=Pursuit&action=edit&redlink=1 "Pursuit (page does not exist)")
* [Repetitions in Belzebub](Belzebub#Repetitions "Belzebub")
* [Repetitions in SCP](SCP#Repetitions "SCP")
* [Transposition](Transposition "Transposition")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Vice Video on Repetition](Vice#Repetitions "Vice")


## Publications


### 1929


* [Max Euwe](Max_Euwe "Max Euwe") (**1929**). *Mengentheoretische Betrachtungen über das Schachspiel*. Proc. Konin. Akad. Wetenschappen (Amsterdam)


### 1980 ...


* [Murray Campbell](Murray_Campbell "Murray Campbell") (**1985**). *[The graph-history interaction: on ignoring position history](http://portal.acm.org/citation.cfm?id=320516)*. Computer Science Department, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), Proceedings of the 1985 ACM annual conference, [pdf](http://wiki.cs.pdx.edu/wurzburg2009/nfp/campbell-ghi.pdf)
* [Harry Nelson](Harry_Nelson "Harry Nelson"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1988**). *The Draw Heuristic of Cray Blitz*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal") » [Cray Blitz](Cray_Blitz "Cray Blitz")


### 1990 ...


* [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Victor Allis](Victor_Allis "Victor Allis") (**1999**). *A Solution to the GHI Problem for Best-First Search*. [CG 1998](CG_1998 "CG 1998") » [Graph History Interaction](Graph_History_Interaction "Graph History Interaction"), [Best-First](Best-First "Best-First")


### 2000 ...


* [Thomas Lincke](Thomas_Lincke "Thomas Lincke") (**2002**). *Exploring the Computational Limits of Large Exhaustive Search Problems*. Ph.D thesis, [ETH Zurich](ETH_Zurich "ETH Zurich"), [pdf](http://e-collection.library.ethz.ch/eserv/eth:25905/eth-25905-02.pdf), [[15]](#cite_note-15) Chapter 4.3 Cycles
* [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković"), [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović") (**2004**). *A New Approach to Draw Detection by Move Repetition in Computer Chess Programming.* [CoRR arXiv:cs/0406038](http://arxiv.org/abs/cs/0406038) [[16]](#cite_note-16) [[17]](#cite_note-17)
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2004**). *A General Solution to the Graph History Interaction Problem*. [AAAI](AAAI "AAAI") National Conference, [pdf](http://webdocs.cs.ualberta.ca/~mmueller/ps/aaai-ghi.pdf)
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto") (**2005**). *Correct and Efficient Search Algorithms in the Presence of Repetitions*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), Received the 2005 [ChessBase](ChessBase "ChessBase") [Best-Publication Award](ICGA#BestPublicationAwards "ICGA"), [pdf](http://www.is.titech.ac.jp/%7Ekishi/pdf_file/kishi_phd_thesis.pdf) » [Proof-Number Search](Proof-Number_Search "Proof-Number Search")
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2005**). *A Solution to the GHI Problem for Depth-First Proof-Number Search*. 7th Joint Conference on Information Sciences (JCIS2003), pp. 489 - 492, [pdf](http://webdocs.cs.ualberta.ca/~mmueller/ps/kishimoto-mueller-infsci-ghi.pdf) » [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")
* [Daniel Andersson](index.php?title=Daniel_Andersson&action=edit&redlink=1 "Daniel Andersson (page does not exist)") (**2009**). *Perfect-Information Games with Cycles*. Ph.D. thesis, [Aarhus University](https://en.wikipedia.org/wiki/Aarhus_University), advisor [Peter Bro Miltersen](Mathematician#Miltersen "Mathematician"), [pdf](http://www.cs.au.dk/~koda/thesis.pdf)


### 2010 ...


* [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2013**). *A fast software-based method for upcoming cycle detection in search trees*. [pdf preview](http://marcelk.net/2013-04-06/paper/upcoming-rep-v2.pdf) [[18]](#cite_note-18)


## Forum Posts


### 1990 ...


* [Repetition detection w/hash tables](http://groups.google.com/group/rec.games.chess/browse_frm/thread/8cc6428ab611f70e) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), August 14, 1993


### 1995 ...


* [Draw by Repetition Code](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7edf36b54a47267d) by cmayer, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 31, 1996
* [Repetitions in Crafty](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/6e999936bc7e5200) by [Martin Borriss](Martin_Borriss "Martin Borriss"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 30, 1997 » [Crafty](Crafty "Crafty")
* [Perpetual check](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/e3bf1dac24b7b1ce) by [Ian Kennedy](Ian_Kennedy "Ian Kennedy"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 19, 1997
* [Handling of repetition (draw) in transposition table](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1d601e208c97c395) by Bjarke Dahl Ebert, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 9, 1997
* [Detected draw by repetition](https://groups.google.com/d/msg/rec.games.chess.computer/T9VBgvjL450/u6aUpiL1XzMJ) by [Tim Foden](Tim_Foden "Tim Foden"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 15, 1997
* [triple repetition](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/c431ac1739de871b) by Daniel Kang, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 26, 1997
* [draw by repetition and hash tables](https://www.stmintz.com/ccc/index.php?id=22816) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), July 24, 1998
* [Draw by 2nd repetition?](https://www.stmintz.com/ccc/index.php?id=47663) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), March 31, 1999
* [Problem with draws by rep and hash table](https://www.stmintz.com/ccc/index.php?id=72221) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), October 07, 1999


### 2000 ...


* [Does your program understand castling/en passant rights on 3x repetition](https://www.stmintz.com/ccc/index.php?id=99216) by Richard A. Fowell, [CCC](CCC "CCC"), February 27, 2000 » [Castling Rights](Castling_Rights "Castling Rights"), [En passant](En_passant "En passant")
* [Detecting three-fold repetition?](https://www.stmintz.com/ccc/index.php?id=119867) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), July 17, 2000


 [Re: Detecting three-fold repetition?](https://www.stmintz.com/ccc/index.php?id=119911) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), July 17, 2000 » [SCP Repetition detection](SCP#Repetitions "SCP")
**2001**



* [The Old way to detect 3fold repetition (help needed)](https://www.stmintz.com/ccc/index.php?id=160274) by [Gianluigi Masciulli](Gianluigi_Masciulli "Gianluigi Masciulli"), [CCC](CCC "CCC"), March 26, 2001
* ["Don't trust draw score" <=Is it true?](https://www.stmintz.com/ccc/index.php?id=182927) by [Teerapong Tovirat](Teerapong_Tovirat "Teerapong Tovirat"), [CCC](CCC "CCC"), August 08, 2001 » [Transposition Table](Transposition_Table "Transposition Table"), [Path-Dependency](Path-Dependency "Path-Dependency")


**2002**



* [Detecting Draws using a Small Hash Table?](https://www.stmintz.com/ccc/index.php?id=214562) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), February 20, 2002
* [3 fold repetiton (Seacher v Postmodernist)](https://www.stmintz.com/ccc/index.php?id=216120) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), March 02, 2002
* [A new(?) technique to recognize draws](https://www.stmintz.com/ccc/index.php?id=233270) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), June 01, 2002 » [Perpetual Check](Check#Perpetual "Check"), [Corresponding Squares](Corresponding_Squares "Corresponding Squares")
* [Repetitions: is this code correct?](https://www.stmintz.com/ccc/index.php?id=239987) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), July 12, 2002


**2003**



* [Draw claims](https://www.stmintz.com/ccc/index.php?id=301324) by [Thomas Mayer](Thomas_Mayer "Thomas Mayer"), [CCC](CCC "CCC"), June 17, 2003
* [In computer games 3-fold repetition should be AUTOMATICALLY draw!](https://www.stmintz.com/ccc/index.php?id=332089) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 30, 2003


**2004**



* [perpetual check recognition](https://www.stmintz.com/ccc/index.php?id=345832) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [CCC](CCC "CCC"), January 30, 2004
* [A New Approach to Draw Detection by Move Repetition](https://www.stmintz.com/ccc/index.php?id=379648) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), July 29, 2004
* [Draw Detection by Move Repetition Procedure - Comments](https://www.stmintz.com/ccc/index.php?id=380201) by [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [CCC](CCC "CCC"), August 01, 2004
* [How to handle the first repetition correctly? (long)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48537) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 10, 2004
* [Repetition Detection](https://www.stmintz.com/ccc/index.php?id=398421) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), December 01, 2004
* [Perpetual check](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=858) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 03, 2004


### 2005 ...


* [When to claim repetition and 50 move draws?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2093) by Peter Hughes, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 26, 2005
* [draw by repetition](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3863) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 21, 2005


**2007**



* [Handling 3-rep/50-move in hash tables](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6238) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 19, 2007
* [avoidrep-pruning](http://www.talkchess.com/forum/viewtopic.php?t=13791) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), May 15, 2007 » [Pruning](Pruning "Pruning")


**2008**



* [Problem with Transposition Table and Repitition-Draw](http://www.talkchess.com/forum/viewtopic.php?t=18854) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 11, 2008 » [Transposition Table](Transposition_Table "Transposition Table")
* [Again, rep-draws (and score aging)](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6422) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 28, 2008
* [Repetition detection question](http://www.talkchess.com/forum/viewtopic.php?t=19257) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 28, 2008
* [Repetition detection structure](http://www.talkchess.com/forum/viewtopic.php?t=19779) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), February 23, 2008
* [Semi-Path Dependent Hashing: a semi-useless idea](http://www.talkchess.com/forum/viewtopic.php?t=21343) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), May 24, 2008
* [Repetition Detection](http://www.talkchess.com/forum/viewtopic.php?t=22968) by Colin, [CCC](CCC "CCC"), August 13, 2008
* [When and how to return a draw evaluation?](http://www.talkchess.com/forum/viewtopic.php?t=23257) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), August 26, 2008 » [Draw](Draw "Draw")
* [Are everybody making this bad?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=25075) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), November 26, 2008
* [Draw by repetition when mate is possible](http://www.talkchess.com/forum/viewtopic.php?t=25705) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), December 30, 2008 » [Checkmate](Checkmate "Checkmate")


**2009**



* [wrong draw claim or right?](http://www.talkchess.com/forum/viewtopic.php?t=30925) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), December 03, 2009
* [Stupid Extension Problem/Question](http://www.talkchess.com/forum/viewtopic.php?t=31220) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), December 23, 2009 » [Extensions](Extensions "Extensions")


### 2010 ...


* [Repetition Detection Without Hashing](http://www.talkchess.com/forum/viewtopic.php?t=32597) by Levi Aho, [CCC](CCC "CCC"), February 13, 2010
* [nullmove and repetitive draw detection](http://www.talkchess.com/forum/viewtopic.php?t=35052) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), June 20, 2010 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [bizarre repetition detection issue](http://www.talkchess.com/forum/viewtopic.php?t=36599) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 04, 2010


**2011**



* [Repeating moves to add time](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=38608) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), March 31, 2011 » [Time Management](Time_Management "Time Management")
* [Repetitions/50 moves and TT](http://www.talkchess.com/forum/viewtopic.php?t=40388) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 13, 2011
* [repetition detection](http://www.talkchess.com/forum/viewtopic.php?t=40931) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), October 29, 2011


**2012**



* [Draw by 3-fold repetition?](http://www.talkchess.com/forum/viewtopic.php?t=41833) by [Andy Duplain](index.php?title=Andy_Duplain&action=edit&redlink=1 "Andy Duplain (page does not exist)"), [CCC](CCC "CCC"), January 06, 2012
* [Aquarium IDEA, repetitions, and minimax over cycles](http://www.open-chess.org/viewtopic.php?f=5&t=2093) by kevinfat, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), September 17, 2012 » [Aquarium](Aquarium "Aquarium")
* [Why is this game not a draw?](http://www.talkchess.com/forum/viewtopic.php?t=45774) by [Carlos Pagador](index.php?title=Carlos_Pagador&action=edit&redlink=1 "Carlos Pagador (page does not exist)"), [CCC](CCC "CCC"), October 29, 2012
* [Re: Move Tables - explain as if I'm five](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=490672&t=45846) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), November 05, 2012 » [Repetitions in Belzebub](Belzebub#Repetitions "Belzebub")
* [FIDE Rules](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52677&sid=5875e0b83aa323c58f9e9b3af0718049) by crystalclear, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 11, 2012


**2013**



* [Half Move Clock Confusion](http://www.open-chess.org/viewtopic.php?f=3&t=2209) by HumbleProgrammer, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 10, 2013 » [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule"), [Halfmove Clock](Halfmove_Clock "Halfmove Clock")
* [Repetition check](http://www.talkchess.com/forum/viewtopic.php?t=47637) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 29, 2013
* [Upcoming repetition detection](http://www.open-chess.org/viewtopic.php?f=5&t=2300) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 06, 2013
* [Stockfish bug](http://www.talkchess.com/forum/viewtopic.php?t=48149) by [Steven Atkinson](Steven_Atkinson "Steven Atkinson"), [CCC](CCC "CCC"), May 30, 2013 » [Stockfish](Stockfish "Stockfish")
* [Repetition check](http://www.talkchess.com/forum/viewtopic.php?t=48696) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 20, 2013
* [UCI protocol issue](http://www.talkchess.com/forum/viewtopic.php?t=48768) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 27, 2013 » [UCI](UCI "UCI")
* [ep and castle rights hashing](http://www.talkchess.com/forum/viewtopic.php?t=49362) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), September 15, 2013 » [Castling Rights](Castling_Rights "Castling Rights"), [En passant](En_passant "En passant"), [Transposition Table](Transposition_Table "Transposition Table")


**2014**



* [Two fold repetition rule](http://www.talkchess.com/forum/viewtopic.php?t=51000) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), January 22, 2014
* [FIDE's new rules for chess](http://www.talkchess.com/forum/viewtopic.php?t=53030) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), July 20, 2014


### 2015 ...


* [Using TT for detecting repetitions](http://www.open-chess.org/viewtopic.php?f=5&t=2863) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 18, 2015


**2016**



* [Simple triple repetition handler](http://www.talkchess.com/forum/viewtopic.php?t=59322) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), February 21, 2016
* [How to test 3rd repetition rule?](http://www.talkchess.com/forum/viewtopic.php?t=59841) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), April 12, 2016


 [This should be in the wiki](http://www.talkchess.com/forum/viewtopic.php?t=59841&start=14) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 13, 2016
* [3rd repetition, a case where not cause castle rights... but](http://www.talkchess.com/forum/viewtopic.php?t=59854) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), April 14, 2016 » [Castling Rights](Castling_Rights "Castling Rights")
* [Triple Repitition: Is this considered a repitition or not?](http://www.talkchess.com/forum/viewtopic.php?t=60075) by Jayakiran Akurathi, [CCC](CCC "CCC"), May 07, 2016 » [En passant](En_passant "En passant")
* [Repetitions in the Search Tree](http://www.talkchess.com/forum/viewtopic.php?t=60310) by Jayakiran Akurathi, [CCC](CCC "CCC"), May 29, 2016
* [Syzygy and draw by repetition](http://www.talkchess.com/forum/viewtopic.php?t=60906) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 22, 2016 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [perpetual check position](http://www.talkchess.com/forum/viewtopic.php?t=61140) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), August 16, 2016 » [Perpetual Check](Check#Perpetual "Check")
* [Hashed repetition table](http://www.talkchess.com/forum/viewtopic.php?t=61328) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), September 04, 2016 » [Repetition Hash Table](Repetitions#RepetitionHashTable "Repetitions")
* [transposition tables and three-fold repetition](http://www.talkchess.com/forum/viewtopic.php?t=61384) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), September 10, 2016 » [Transposition Table](Transposition_Table "Transposition Table")
* [The new chess rules (5-fold repetition and 75-move draw)](https://groups.google.com/d/msg/fishcooking/M2bkzC3MuFQ/N3pHK4DcAgAJ) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 29, 2016 » [Stockfish](Stockfish "Stockfish"), [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")


**2017**



* [Have engines updated for fide 2014 draw rules?](http://www.talkchess.com/forum/viewtopic.php?t=62956) by [Norm Pollock](index.php?title=Norm_Pollock&action=edit&redlink=1 "Norm Pollock (page does not exist)"), [CCC](CCC "CCC"), January 28, 2017
* [Reporting a draw in UCI](http://www.talkchess.com/forum/viewtopic.php?t=63906) by Vince Sempronio, [CCC](CCC "CCC"), May 05, 2017 » [Draw](Draw "Draw"), [UCI](UCI "UCI")


**2018**



* [3-fold repetition and cutechess-cli](http://www.talkchess.com/forum/viewtopic.php?t=66323) by Lars Mathiesen, [CCC](CCC "CCC"), January 14, 2018 » [En passant](En_passant "En passant")


### 2020 ...


* [FEN and 3rd repetition rule. No information?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73552) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), April 03, 2020 » [FEN](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
* [Make engine stop repeating moves in a clearly won position](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75573) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), October 27, 2020


**2021**



* [Alpha-beta search for drawing endgames](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77497) by Emanuel Torres, [CCC](CCC "CCC"), June 16, 2021 » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [Draw Evaluation](Draw_Evaluation "Draw Evaluation"), [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")


**2022**



* [Draw by repetition](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79286) by Philippe Chevalier, [CCC](CCC "CCC"), February 05, 2022
* [Elegant algorithm for detecting repetitions?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=80520) by A. Li, [CCC](CCC "CCC"), August 19, 2022


## External Links


* [Cycle detection (graph theory) from Wikipedia](https://en.wikipedia.org/wiki/Cycle_%28graph_theory%29#Cycle_detection)
* [Cycle detection from Wikipedia](https://en.wikipedia.org/wiki/Cycle_detection)
* [Repetition Detection](http://web.archive.org/web/20070710013535/www.brucemo.com/compchess/programming/repetition.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
* [Threefold repetition from Wikipedia](https://en.wikipedia.org/wiki/Threefold_repetition)
* [Perpetual check from Wikipedia](https://en.wikipedia.org/wiki/Perpetual_check)
* [Fide Handbook - E.I.01A. Laws of Chess](http://www.fide.com/component/handbook/?id=124&view=article)
* [A Chess Firewall at Zero?](https://rjlipton.wordpress.com/2016/01/21/a-chess-firewall-at-zero/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), January 21, 2016
* [Agnes Obel](Category:Agnes_Obel "Category:Agnes Obel") - [It's Happening Again](http://lyrics.wikia.com/wiki/Agnes_Obel:It%27s_Happening_Again) (2016), [BBC 6 Music Live Room](https://en.wikipedia.org/wiki/BBC_Radio_6_Music), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 featuring [Kristina Koropecki](https://www.couchsurfing.com/people/kriskar), [Charlotte Danhier](https://mobile.twitter.com/agnesobel_org/status/637306150413803524), [Catherine De Biasio](https://www.discogs.com/de/artist/1453695-Catherine-De-Biasio)
 
## References


1. [↑](#cite_ref-1) [Picture gallery "Back in Holland 1941 - 1954"](http://www.mcescher.com/Gallery/back-bmp/LW327.jpg) from [The Official M.C. Escher Website](http://www.mcescher.com/)
2. [↑](#cite_ref-2) [FIDE's new rules for chess](http://www.talkchess.com/forum/viewtopic.php?t=53030) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), July 20, 2014
3. [↑](#cite_ref-3) [Fide Handbook - E.I.01A. Laws of Chess](http://www.fide.com/component/handbook/?id=124&view=article)
4. [↑](#cite_ref-4) [Mathematical Problems - Max Euwe's sequence](http://www.fh-friedberg.de/users/boergens/english/problems/problem059engl.htm) by [Manfred Börgens](http://www.fh-friedberg.de/users/boergens/main.htm)
5. [↑](#cite_ref-5) [Max Euwe](Max_Euwe "Max Euwe") (**1929**). *Mengentheoretische Betrachtungen über das Schachspiel*, Proc. Konin. Akad. Wetenschappen (Amsterdam)
6. [↑](#cite_ref-6) [Mathematical Problems - Max Euwe's sequence - Solution](http://www.fh-friedberg.de/users/boergens/english/problems/problem059englloe.htm) by [Manfred Börgens](http://www.fh-friedberg.de/users/boergens/main.htm)
7. [↑](#cite_ref-7) [Repetition Detection](http://web.archive.org/web/20040427014858/brucemo.com/compchess/programming/repetition.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)
8. [↑](#cite_ref-8) [Draw by Repetition Code, post 4](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7edf36b54a47267d) by [John Stanback](John_Stanback "John Stanback"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 31, 1996
9. [↑](#cite_ref-9) [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *The design and implementation of the Rookie 2.0 Chess Playing Program*. Masters Thesis, [pdf](http://alexandria.tue.nl/extra2/afstversl/wsk-i/kervinck2002.pdf)
10. [↑](#cite_ref-10) Courtesy [Ronald de Man](Ronald_de_Man "Ronald de Man") for revealing this implementation trick
11. [↑](#cite_ref-11) [Re: triple repetition](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/c431ac1739de871b/d8f8d6ee1b252b86) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 27, 1997
12. [↑](#cite_ref-12) [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković"), [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović") (**2004**). *A New Approach to Draw Detection by Move Repetition in Computer Chess Programming.* [CoRR arXiv:cs/0406038](http://arxiv.org/abs/cs/0406038)
13. [↑](#cite_ref-13) [A New Approach to Draw Detection by Move Repetition](https://www.stmintz.com/ccc/index.php?id=379648) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), July 29, 2004
14. [↑](#cite_ref-14) [Draw Detection by Move Repetition Procedure - Comments](https://www.stmintz.com/ccc/index.php?id=380201) by [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [CCC](CCC "CCC"), August 01, 2004
15. [↑](#cite_ref-15) [Re: Aquarium IDEA, repetitions, and minimax over cycles](http://www.open-chess.org/viewtopic.php?f=5&t=2093#p17469) by [syzygy](Ronald_de_Man "Ronald de Man"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2012
16. [↑](#cite_ref-16) [A New Approach to Draw Detection by Move Repetition](https://www.stmintz.com/ccc/index.php?id=379648) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), July 29, 2004
17. [↑](#cite_ref-17) [Draw Detection by Move Repetition Procedure - Comments](https://www.stmintz.com/ccc/index.php?id=380201) by [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [CCC](CCC "CCC"), August 01, 2004
18. [↑](#cite_ref-18) [Upcoming repetition detection](http://www.open-chess.org/viewtopic.php?f=5&t=2300) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 06, 2013

**[Up one Level](Search "Search")**







 
