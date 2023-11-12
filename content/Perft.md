---
title: Perft
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Move Generation](Move_Generation "Move Generation") \* Perft**


**Perft**, (**perf**ormance **t**est, move path enumeration)  

a [debugging](Debugging "Debugging") function to walk the move generation tree of strictly [legal moves](Legal_Move "Legal Move") to count all the [leaf nodes](Leaf_Node "Leaf Node") of a certain [depth](Depth "Depth"), which can be compared to [predetermined values](Perft_Results "Perft Results") and used to isolate [bugs](Engine_Testing#bugs "Engine Testing"). In perft, nodes are only counted at the end after the last [makemove](Make_Move "Make Move"). Thus "higher" [terminal nodes](Terminal_Node "Terminal Node") (e.g. mate or stalemate) are not counted, instead the number of move paths of a certain depth. Perft ignores draws by [repetition](Repetitions "Repetitions"), by the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule") and by [insufficient material](Material#InsufficientMaterial "Material"). By recording the amount of time taken for each iteration, it's possible to compare the performance of different move generators or the same generator on different machines, though this must be done with caution since there are variations to perft.



## Speed up


### Bulk-counting


Assuming the above code used a legal move generator. The algorithm is simple, short but it makes moves for every node even they are the leave (ends of branches). It could improve speed significantly: instead of counting nodes at "depth 0", legal move generators can take advantage of the fact that the number of moves generated at "depth 1" represents the accurate Perft value for that branch. Therefore they can skip the last [makemove](Make_Move "Make Move")/[undomove](Unmake_Move "Unmake Move"), which gives much faster results and is a better indicator of the raw move generator speed (versus move generator + make/unmake). However, this can cause some confusion when comparing Perft values and may make the task of collecting some extra information such as the number of captures and checks be almost impossible. 




```C++

u64 Perft(int depth /* assuming >= 1 */)
{
  MOVE move_list[256];
  int n_moves, i;
  u64 nodes = 0;

  n_moves = GenerateLegalMoves(move_list);

  if (depth == 1) 
    return (u64) n_moves;

  for (i = 0; i < n_moves; i++) {
    MakeMove(move_list[i]);
    nodes += Perft(depth - 1);
    UndoMove(move_list[i]);
  }
  return nodes;
}

```

### Pseudo Legal Moves


To generate legal moves some programs have to make moves first, call a function to check if the position incheck and then undo those moves. That makes the above Perft function to make and undo moves twice for all moves. Below code can avoid that problem and run much faster:




```C++

u64 Perft(int depth)
{
  MOVE move_list[256];
  int n_moves, i;
  u64 nodes = 0;

  if (depth == 0) 
    return 1ULL;

  n_moves = GenerateMoves(move_list);
  for (i = 0; i < n_moves; i++) {
    MakeMove(move_list[i]);
    if (!IsIncheck())
      nodes += Perft(depth - 1);
    UndoMove(move_list[i]);
  }
  return nodes;
}

```

### Hashing


Perft can receive another speed boost by [hashing](Hash_Table "Hash Table") node counts, with a small chance for inaccurate results. Sometimes this is used as a sanity check to make sure the hash table and keys are working correctly.



## Divide


The Divide command is often implemented as a variation of Perft, listing all moves and for each move, the perft of the decremented depth. However, some programs already give "divided" output for Perft. Below is output of [Stockfish](Stockfish "Stockfish") when computing perft 5 for start position:




```C++

go perft 5
a2a3: 181046
b2b3: 215255
c2c3: 222861
d2d3: 328511
e2e3: 402988
f2f3: 178889
g2g3: 217210
h2h3: 181044
a2a4: 217832
b2b4: 216145
c2c4: 240082
d2d4: 361790
e2e4: 405385
f2f4: 198473
g2g4: 214048
h2h4: 218829
b1a3: 198572
b1c3: 234656
g1f3: 233491
g1h3: 198502

Nodes searched: 4865609

```

## Purposes


Perft is mostly for debugging purposes. It works mainly with functions: move generators, make move, unmake move. They all are very basic and vital for chess engines. By comparing Perft results developers can find out if those functions work correctly or not. If they are incorrect developers can narrow quickly by comparing branches, then call Perft for wrong branches with lower depth, repeat until finding direct positions which give the wrong result.


Other purposes:



* give a quick glance at how good/bad their generators/make/unmake functions are, compared with the speed of other engines
* calculate branch factors
* a factor to estimate how the complexity of chess variants, by comparing branch factors or Perft results at a given depth for their starting positions


## History


Supposably, perft was first implemented within the [Cobol](index.php?title=Cobol&action=edit&redlink=1 "Cobol (page does not exist)") program [RSCE-1](index.php?title=RSCE-1&action=edit&redlink=1 "RSCE-1 (page does not exist)") by [R.C. Smith](Rolf_C._Smith#RCSmith "Rolf C. Smith"), submitted to the [USCF](https://en.wikipedia.org/wiki/United_States_Chess_Federation) for evaluation, and subject of an [1978](Timeline#1978 "Timeline") [Computerworld](Computerworld "Computerworld") article [[1]](#cite_note-1) . RSCE-1's purpose was not to play chess games, but position analysis, to find forced [mates](Checkmate "Checkmate"), and to perform a move path enumeration of up to three [plies](Ply "Ply"), with the [perft(3) result](Perft_Results "Perft Results") of 8,902 from the [initial position](Initial_Position "Initial Position") already mentioned [[2]](#cite_note-2). [Ken Thompson](Ken_Thompson "Ken Thompson") may have calculated perft(3) and perft(4) earlier than this date with [Belle](Belle "Belle"). [Steven Edwards](Steven_Edwards "Steven Edwards") suggested the move path enumeration in 1995 as implemented in [Spector](Spector "Spector") [[3]](#cite_note-3) and has since been actively involved in Perft computations, while the term "Perft" was likely coined by a [Crafty](Crafty "Crafty") command, despite its initial implementation was not conform to the above definition [[4]](#cite_note-4).


In **December 2003**, [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson") started a distributed project [[5]](#cite_note-5) to calculate perft(11) of the [initial position](Initial_Position "Initial Position"), taking over a week to calculate [[6]](#cite_note-6) . Exact Perft numbers have been computed and verified up to a depth of 13 by Edwards and are now available in the [On-Line Encyclopedia of Integer Sequences](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences) [[7]](#cite_note-7) , and are given under [Initial Position Summary](Initial_Position_Summary "Initial Position Summary"). A so far unverified claim for perft(**14**) of 61,885,021,521,585,529,237 was given by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund") in **April 2013** [[8]](#cite_note-8), while [Daniel Shawul](Daniel_Shawul "Daniel Shawul") proposed Perft estimation applying [Monte carlo methods](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") [[9]](#cite_note-9) [[10]](#cite_note-10). 

In **August 2017**, [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), who already confirmed Peter Österlund's perft(**14**) in September 2016 [[11]](#cite_note-11), computed perft(**15**) of 2,015,099,950,053,364,471,960 with his [GPU](GPU "GPU") perft program [[12]](#cite_note-12), running it several days two times with different [zobrist keys](Zobrist_Hashing "Zobrist Hashing") on a cluster of [Nvidia DGX-1](https://en.wikipedia.org/wiki/Nvidia_DGX-1) server systems [[13]](#cite_note-13). His program starts exploring the tree in [depth first](Depth-First "Depth-First") manner on CPU. When a certain depth is reached a GPU function (kernel) is launched to compute perft of the subtree in [breadth first](Best-First "Best-First") manner [[14]](#cite_note-14). Ankan Banerjee dedicated his computations in honor to [Steven Edwards](Steven_Edwards "Steven Edwards") - whose tireless efforts for verifying perft(14) encouraged him to verify perft(14) and take up the challenge to compute perft(15) [[15]](#cite_note-15).



## Quotes


by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") in a forum post, June 12, 2020 [[16]](#cite_note-16) :




```C++
I believe I was the first to use this. Back in the 80's. We rewrote the move generator in Cray Blitz in assembly language. It was a pain to debug. I decided on the "perft" approach solely to test/debug the move generator. We'd run two versions, one FORTRAN, one assembly, and we tested and debugged until they matched.
I carried this over into Crafty as early versions went through several different approaches on move generation. Starting with the Slate/Atkin approach, then rotated bit boards (which took some time to debug), and the magic. It was really intended solely for that purpose. Then several started to use it as a benchmark for speed. I never followed that path since move generation is a very small part of the overall CPU time burned.
Speed here is not so important. I doubt anyone's move generator takes more than 10% of total search time, which means a 20% improvement in perft numbers is only a 2% overall speed gain. I would not worry about anything but matching the node counts exactly...

```

## Results


* [Perft Results](Perft_Results "Perft Results")
* [Chess960 Perft Results](Chess960_Perft_Results "Chess960 Perft Results")
* [Chinese Chess Perft Results](Chinese_Chess_Perft_Results "Chinese Chess Perft Results")


## Publications


* [Aart Bik](Aart_Bik "Aart Bik") (**2012**). *Computing Deep Perft and Divide Numbers for Checkers*. [ICGA Journal, Vol. 35, No. 4](ICGA_Journal#35_4 "ICGA Journal") » [Checkers](Checkers "Checkers")
* [Daniel S. Abdi](Daniel_Shawul "Daniel Shawul") (**2013**). *Monte carlo methods for estimating game tree size*. [[17]](#cite_note-17) » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")


## Forum Posts


### 1995 ...


* [Re: Speed of Move Generator](https://groups.google.com/d/msg/rec.games.chess.computer/M8V1AzkfOok/YV9lcfOlfgIJ) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 16, 1995 » [Spector](Spector "Spector")
* [Re: complete opening tree stats](https://groups.google.com/d/msg/rec.games.chess.computer/2nqtCdHC-r0/ENqomE2u51kJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 05, 1998 » [Crafty](Crafty "Crafty")


### 2000 ...


* [Testing speed of "position visiting"](https://www.stmintz.com/ccc/index.php?id=107258) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), April 23, 2000
* [Experiments with crafty perft command](https://groups.google.com/d/msg/rec.games.chess.computer/ek5fbFf4ajc/lrPxv2kDHgkJ) by Guy Macon, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 10, 2000
* [Who is the champion in calculating perft?](https://www.stmintz.com/ccc/index.php?id=198498) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), November 22, 2001
* [Perft 5,6 {Fastest program is List}](https://www.stmintz.com/ccc/index.php?id=234025) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 04, 2002 » [List](List_(Program) "List (Program)")
* [Perft revisited](https://www.stmintz.com/ccc/index.php?id=275133) by [Normand M. Blais](index.php?title=Normand_M._Blais&action=edit&redlink=1 "Normand M. Blais (page does not exist)"), [CCC](CCC "CCC"), January 05, 2003
* [perft question](https://www.stmintz.com/ccc/index.php?id=276596) by [Joel Veness](Joel_Veness "Joel Veness"), [CCC](CCC "CCC"), January 12, 2003
* [Perft](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41318) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 18, 2003
* [Highest perft for initial position?](https://www.stmintz.com/ccc/index.php?id=326134) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), November 07, 2003
* [Distributed perft project](https://www.stmintz.com/ccc/index.php?id=335026) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), December 09, 2003
* [Perft(10) verified](https://www.stmintz.com/ccc/index.php?id=334499) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), December 09, 2003
* [Distributed perft, current standings and trends](https://www.stmintz.com/ccc/index.php?id=335527) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), December 12, 2003
* [Hashing in distributed perft](https://www.stmintz.com/ccc/index.php?id=336985) by [Steffen Jakob](Steffen_A._Jakob "Steffen A. Jakob"), [CCC](CCC "CCC"), December 19, 2003
* [perft records](https://www.stmintz.com/ccc/index.php?id=386249) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), September 06, 2004
* [perft results (how accurate is accurate enough ?)](https://www.stmintz.com/ccc/index.php?id=388806) by [Roman Hartmann](Roman_Hartmann "Roman Hartmann"), [CCC](CCC "CCC"), September 23, 2004
* [FRC Perft](https://www.stmintz.com/ccc/index.php?id=394229) by Jürgen Suntinger, [CCC](CCC "CCC"), November 02, 2004


### 2005 ...


* [perft question](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=1377) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 19, 2005
* [Perft vs Search Re: Cache size does matter](https://www.stmintz.com/ccc/index.php?id=466491) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), December 03, 2005
* [Perft -- Test position and data](https://www.stmintz.com/ccc/index.php?id=488816) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), February 23, 2006
* [A perft faster than qperft?!](http://www.talkchess.com/forum/viewtopic.php?t=20834) by [Allard Siemelink](Allard_Siemelink "Allard Siemelink"), [CCC](CCC "CCC"), April 24, 2008
* [Perft problems...](http://www.talkchess.com/forum/viewtopic.php?t=23634) by [Chris Tatham](index.php?title=Chris_Tatham&action=edit&redlink=1 "Chris Tatham (page does not exist)"), [CCC](CCC "CCC"), September 10, 2008
* [What is perft(x) exactly meaning?](http://www.talkchess.com/forum/viewtopic.php?t=27334) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), April 06, 2009
* [Perft and mate](http://www.talkchess.com/forum/viewtopic.php?t=29425) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), August 16, 2009 » [Freccia](Freccia "Freccia")
* [Perft and insufficient material](http://www.talkchess.com/forum/viewtopic.php?t=30754) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), November 23, 2009


### 2010 ...


* [Does perft include underpromotion?](http://www.talkchess.com/forum/viewtopic.php?t=34025) by [Chan Rasjid](Rasjid_Chan "Rasjid Chan"), [CCC](CCC "CCC"), April 27, 2010


**2011**



* [Perft 12 in progress](http://www.talkchess.com/forum/viewtopic.php?t=38235) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), February 27, 2011
* [Perft(12) count confirmed](http://www.talkchess.com/forum/viewtopic.php?t=38862) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 25, 2011
* [Perft(13) betting pool](http://www.talkchess.com/forum/viewtopic.php?t=39678) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 10, 2011
* [Fastest perft](http://www.talkchess.com/forum/viewtopic.php?t=40108) by ethan ara, [CCC](CCC "CCC"), August 19, 2011
* [Perft(3) from 1978, with a twist!](http://www.talkchess.com/forum/viewtopic.php?t=41373) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 08, 2011 [[18]](#cite_note-18)


**2012**



* [estimating the number of possible stalemates in perft(n)](http://www.talkchess.com/forum/viewtopic.php?t=42512) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 18, 2012 » [Stalemate](Stalemate "Stalemate")
* [Shatranj perfts](http://www.talkchess.com/forum/viewtopic.php?t=42600) by [Paul Byrne](index.php?title=Paul_Byrne&action=edit&redlink=1 "Paul Byrne (page does not exist)"), [CCC](CCC "CCC"), February 24, 2012 » [Shatranj](Shatranj "Shatranj")
* [Perft and en\_passant](http://www.talkchess.com/forum/viewtopic.php?t=45099) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), September 11, 2012 » [En passant](En_passant "En passant")
* [about perft, what is the proper way of doing it?](http://www.talkchess.com/forum/viewtopic.php?t=46004) by Fred Piche, [CCC](CCC "CCC"), November 14, 2012


**2013**



* [A few positions to test movegen](http://www.talkchess.com/forum/viewtopic.php?t=47318) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 24, 2013
* [Perft(14) estimates thread](http://www.talkchess.com/forum/viewtopic.php?t=47335) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), February 26, 2013


 [Re: Perft(14) estimates thread](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=513308&t=47335) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), April 02, 2013 » 61,885,021,521,585,529,237
* [Perft(15) estimates thread](http://www.talkchess.com/forum/viewtopic.php?t=47740) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 10, 2013


 [MC methods](http://www.talkchess.com/forum/viewtopic.php?t=47740&start=2) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 11, 2013 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
 [Re: MC methods](http://www.talkchess.com/forum/viewtopic.php?t=47740&topic_view=flat&start=11) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 13, 2013
* [Is Perft Speed Important?](http://www.chessprogramming.net/computerchess/is-perft-speed-important/) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [Computer Chess Programming](http://www.chessprogramming.net/), April 19, 2013
* [Perft search speed bottleneck](http://www.talkchess.com/forum/viewtopic.php?t=48217) by Jim Jarvis, [CCC](CCC "CCC"), June 07, 2013
* [Fast perft on GPU (upto 20 Billion nps w/o hashing)](http://www.talkchess.com/forum/viewtopic.php?t=48387) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), June 22, 2013 » [GPU](GPU "GPU"), [Kogge-Stone Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") [[19]](#cite_note-19)
* [A perft() benchmark](http://www.talkchess.com/forum/viewtopic.php?t=48423) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), June 26, 2013
* [gperft](http://www.talkchess.com/forum/viewtopic.php?t=48491) by [Paul Byrne](index.php?title=Paul_Byrne&action=edit&redlink=1 "Paul Byrne (page does not exist)"), [CCC](CCC "CCC"), July 01, 2013
* [perft/divide bug in roce38 and Sharper? [SOLVED](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52965)] by thedrunkard, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 16, 2013 » [ROCE](ROCE "ROCE"), [Sharper](Sharper "Sharper")


**2014**



* [Perft and Captures](http://www.open-chess.org/viewtopic.php?f=5&t=2238) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 24, 2013 » [Captures](Captures "Captures")
* [Perft(14) revisited](http://www.talkchess.com/forum/viewtopic.php?t=53224) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 08, 2014
* [Perft(14) Weekly Status Report](http://www.talkchess.com/forum/viewtopic.php?t=53406) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 24, 2014
* [Non recursive perft()](http://www.talkchess.com/forum/viewtopic.php?t=53408) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 24, 2014 » [Iterative Search](Iterative_Search "Iterative Search")
* [OpenCL perft() Technical Issues](http://www.talkchess.com/forum/viewtopic.php?t=53439) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 26, 2014 » [OpenCL](OpenCL "OpenCL")
* [A method guaranteed to localize the toughest perft() bugs](http://www.talkchess.com/forum/viewtopic.php?t=53743) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), September 18, 2014
* [FRC / Chess960 Engine with "Divided" Command](http://www.talkchess.com/forum/viewtopic.php?t=54528) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 02, 2014 » [Chess960](Chess960 "Chess960")
* [Handling integer overflow for certain perft() calculations](http://www.talkchess.com/forum/viewtopic.php?t=54719) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 22, 2014
* [Perft(14) verification](http://www.talkchess.com/forum/viewtopic.php?t=54767) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 28, 2014


### 2015 ...


* [Perft(14) Weekly Status Reports for 2015](http://www.talkchess.com/forum/viewtopic.php?t=54853) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 04, 2015
* [Perft(15)](http://www.talkchess.com/forum/viewtopic.php?t=55195) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), February 09, 2015
* [Some Chess960/FRC positions to be confirmed](http://www.talkchess.com/forum/viewtopic.php?t=55274) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), February 09, 2015 » [Chess960](Chess960 "Chess960")
* [An MPI perft program](http://www.talkchess.com/forum/viewtopic.php?t=55896) by [Chao Ma](Chao_Ma "Chao Ma"), [CCC](CCC "CCC"), April 05, 2015 » [Parallel Search](Parallel_Search "Parallel Search")
* [Deep split perft()](http://www.talkchess.com/forum/viewtopic.php?t=56523) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 29, 2015 » [Thread](Thread "Thread")
* [Please comment on my Perft speeds](http://www.open-chess.org/viewtopic.php?f=5&t=2855) by ppyvabw, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 10, 2015
* [100 easy perft(7) test positions](http://www.talkchess.com/forum/viewtopic.php?t=56998) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 17, 2015
* [Perft using nullmove](http://www.talkchess.com/forum/viewtopic.php?t=57417) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), August 29, 2015
* [Perft and hash with legal move generator](http://www.open-chess.org/viewtopic.php?f=5&t=2913) by [Peterpan](index.php?title=Izak_Pretorius&action=edit&redlink=1 "Izak Pretorius (page does not exist)"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 12, 2015 » [Transposition Table](Transposition_Table "Transposition Table")
* [Auriga - distributed and collaborative Perft](http://www.talkchess.com/forum/viewtopic.php?t=58406) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella"), [CCC](CCC "CCC"), November 28, 2015 [[20]](#cite_note-20)
* [Perft(14) Weekly Status Reports for 2016](http://www.talkchess.com/forum/viewtopic.php?t=58726) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 29, 2015


**2016**



* [Best way to debug perft?](http://www.talkchess.com/forum/viewtopic.php?t=59046) by Meni Rosenfeld, [CCC](CCC "CCC"), January 25, 2016 » [Debugging](Debugging "Debugging")
* [Perft, leaf nodes?](http://www.talkchess.com/forum/viewtopic.php?t=59567) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), March 19, 2016
* [reverse perft](http://www.talkchess.com/forum/viewtopic.php?t=60108) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), May 09, 2016
* [Perft for Xiangqi & Shogi](http://www.talkchess.com/forum/viewtopic.php?t=60445) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), June 12, 2016 » [Xiangqi](Chinese_Chess "Chinese Chess"), [Shogi](Shogi "Shogi")
* [yet another attempt on Perft(14)](http://www.talkchess.com/forum/viewtopic.php?t=61119) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 13, 2016


 [Re: yet another attempt on Perft(14)](http://www.talkchess.com/forum/viewtopic.php?t=61119&start=30) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), September 09, 2016 
**2017 ...**



* [Perft results?](http://www.open-chess.org/viewtopic.php?f=5&t=3063) by notachessplayer, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 01, 2017
* [perft(15)](http://www.talkchess.com/forum/viewtopic.php?t=64983) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 25, 2017 » [Perft(15)](Perft#15 "Perft")


 [Re: perft(15)](http://www.talkchess.com/forum/viewtopic.php?t=64983&start=4) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 25, 2017 
 [Re: Perft(15): comparison of estimates with Ankan's result](http://www.talkchess.com/forum/viewtopic.php?t=64983&start=9) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 26, 2017 
* [No standard specification for Perft](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70530) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), April 19, 2019
* [You gotta love Perft... just not too much!](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71379) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), July 27, 2019
* [Shogi Perft numbers](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71550) by [Toni Helminen](Toni_Helminen "Toni Helminen"), [CCC](CCC "CCC"), August 14, 2019 » [Shogi](Shogi "Shogi")
* [LastEmperor - Chess960 perft tool](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72669) by [JohnWoe](Toni_Helminen "Toni Helminen"), [CCC](CCC "CCC"), December 28, 2019 » [Chess960 Perft Results](Chess960_Perft_Results "Chess960 Perft Results")


### 2020 ...


* [Where to enter/read position into hash table in perft?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73493) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 28, 2020 » [Transposition Table](Transposition_Table "Transposition Table")
* [Count the number of nodes of perft(14) and beyond](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73558) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), April 04, 2020
* [magic bitboard perft](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73625) by [Richard Delorme](Richard_Delorme "Richard Delorme"), [CCC](CCC "CCC"), April 11, 2020 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [Perft speed optimization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73577) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), April 06, 2020
* [Request for InDoubleCheck PERFTS EPDs](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73812) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), May 02, 2020 » [Double Check](Double_Check "Double Check")
* [Perft speed and depth questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74153) by [Mark Buisseret](index.php?title=Mark_Buisseret&action=edit&redlink=1 "Mark Buisseret (page does not exist)"), [CCC](CCC "CCC"), June 12, 2020
* [Place to find correct perft result from a fen position](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75877) by [Elias Nilsson](index.php?title=Elias_Nilsson&action=edit&redlink=1 "Elias Nilsson (page does not exist)"), [CCC](CCC "CCC"), November 20, 2020 » [Perft Results](Perft_Results "Perft Results")


**2021**



* [Chinese chess Xiangqi perft results](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76430) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 27, 2021 » [Chinese Chess Perft Results](Chinese_Chess_Perft_Results "Chinese Chess Perft Results")
* [PERFT transposition table funny?!](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77054) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), April 10, 2021 » [Transposition Table](Transposition_Table "Transposition Table"), [Memory](Memory "Memory")
* [Perft 7 -> 1.6 trillion moves](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77069) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), April 12, 2021
* [Being silly with perft and legal move generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77350) by [Jakob Progsch](index.php?title=Jakob_Progsch&action=edit&redlink=1 "Jakob Progsch (page does not exist)"), [CCC](CCC "CCC"), May 19, 2021 » [Legal Move Generation](Move_Generation#Legal "Move Generation"), [En passant](En_passant "En passant")
* [Perft position to debug check-evasions via en passant capture](http://talkchess.com/forum3/viewtopic.php?f=7&t=78119) by [Roland Tomasi](index.php?title=Roland_Tomasi&action=edit&redlink=1 "Roland Tomasi (page does not exist)"), [CCC](CCC "CCC"), September 06, 2021
* [Perft test](http://talkchess.com/forum3/viewtopic.php?f=7&t=78241) by [Pierluigi Meloni](index.php?title=Pierluigi_Meloni&action=edit&redlink=1 "Pierluigi Meloni (page does not exist)"), [CCC](CCC "CCC"), September 24, 2021
* [Gigantua: 1.5 Giganodes per Second per Core move generator](http://talkchess.com/forum3/viewtopic.php?f=7&t=78230) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), September 22, 2021
* [Gigantua: 2 Gigamoves per Second per Core move generator - Sourcecode Release](http://talkchess.com/forum3/viewtopic.php?f=7&t=78352) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), October 07, 2021
* [My Perft Results](http://talkchess.com/forum3/viewtopic.php?f=7&t=80952) by [JoAnn Peeler](index.php?title=JoAnn_Peeler&action=edit&redlink=1 "JoAnn Peeler (page does not exist)"), [CCC](CCC "CCC"), November 04, 2022


## External Links


* [A048987](http://oeis.org/A048987) from [On-Line Encyclopedia of Integer Sequences](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences) (OEIS)
* [Statistics on chess games](https://wismuth.com/chess/statistics-games.html) by [François Labelle](Mathematician#FLabelle "Mathematician")
* [Performance testing from Wikipedia](https://en.wikipedia.org/wiki/Performance_testing)
* [Distributed Perft Project](https://web.archive.org/web/20061014115710/http://www.albert.nu/programs/dperft/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))


### Perft in other Games


* [Perft for other forms of Chess](http://tonyjh.com/chess/technical/) by [Tony Hecker](index.php?title=Tony_Hecker&action=edit&redlink=1 "Tony Hecker (page does not exist)")
* [Perft for Checkers](http://checker-board.blogspot.com/2009/02/perft-for-checkers.html) by [Martin Fierz](Martin_Fierz "Martin Fierz")
* [Perft for Checkers and Reversi/Othello](http://www.aartbik.com/strategy.php) by [Aart Bik](Aart_Bik "Aart Bik")


### Implementations


* [µ-Max Dowload Page - qperft](https://home.hccnet.nl/h.g.muller/dwnldpage.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") » [Micro-Max](Micro-Max "Micro-Max")
* [ankan-ban/perft\_gpu · GitHub](https://github.com/ankan-ban/perft_gpu) [[21]](#cite_note-21)
* [Auriga](http://cinnamonchess.altervista.org/auriga) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella") [[22]](#cite_note-22)
* [BBPerft: A fast, bitboard based chess perft result generator](https://github.com/Mk-Chan/BBPerft) by [Manik Charan](Manik_Charan "Manik Charan") derived from [WyldChess](WyldChess "WyldChess")
* [Chess Engine OliThink - New Move Generator OliPerft (Pre OliThink 5)](http://brausch.org/home/chess/index.html) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch") » [OliThink](OliThink "OliThink")
* [Crafty Command Documentation](http://www.craftychess.com/documentation/craftydoc.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), see perft » [Crafty](Crafty "Crafty")
* [hqperft: Chess move generation based on (H)yperbola (Q)uintessence & range attacks](https://github.com/abulmo/hqperft) by [Richard Delorme](Richard_Delorme "Richard Delorme") » [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence")
* [GitHub - jniemann66/juddperft: Chess move generation engine](https://github.com/jniemann66/juddperft) by [Judd Niemann](Judd_Niemann "Judd Niemann")
* [perft, divide, debugging a move generator](http://www.rocechess.ch/perft.html) from [ROCE](ROCE "ROCE") by [Roman Hartmann](Roman_Hartmann "Roman Hartmann")
* [perft-random.epd](http://marcelk.net/rookie/nostalgia/v3/perft-random.epd) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") » [Rookie](Rookie "Rookie")


### Video Tutorial


* A quick overview of the perft process by [Jonathan Warkentin](Jonathan_Warkentin "Jonathan Warkentin"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos


 
* An example of debugging a perft error by [Jonathan Warkentin](Jonathan_Warkentin "Jonathan Warkentin"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos


 
* Improving the perft speed & debugging tips by [Jonathan Warkentin](Jonathan_Warkentin "Jonathan Warkentin"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos


 
## References


1. [↑](#cite_ref-1) [Written in Cobol - Program Written as Chess Buff's Research Aid](http://news.google.com/newspapers?nid=849&dat=19780417&id=h8lOAAAAIBAJ&sjid=DEoDAAAAIBAJ&pg=6180,1080528) by Brad Schultz, [Computerworld](Computerworld "Computerworld"), April 17, 1978, Page 37
2. [↑](#cite_ref-2) [Perft(3) from 1978, with a twist!](http://www.talkchess.com/forum/viewtopic.php?t=41373) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 08, 2011
3. [↑](#cite_ref-3) [Re: Speed of Move Generator](https://groups.google.com/d/msg/rec.games.chess.computer/M8V1AzkfOok/YV9lcfOlfgIJ) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 16, 1995
4. [↑](#cite_ref-4) [Re: complete opening tree stats](https://groups.google.com/d/msg/rec.games.chess.computer/2nqtCdHC-r0/ENqomE2u51kJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 05, 1998
5. [↑](#cite_ref-5) [Distributed perft project](https://www.stmintz.com/ccc/index.php?id=335026) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), December 09, 2003
6. [↑](#cite_ref-6) [Distributed Perft Project](https://web.archive.org/web/20061014115710/http://www.albert.nu/programs/dperft/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
7. [↑](#cite_ref-7) [A048987](http://oeis.org/A048987) from [On-Line Encyclopedia of Integer Sequences](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences) (OEIS)
8. [↑](#cite_ref-8) [Re: Perft(14) estimates thread](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=513308&t=47335) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), April 02, 2013
9. [↑](#cite_ref-9) [MC methods](http://www.talkchess.com/forum/viewtopic.php?t=47740&start=2) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 11, 2013
10. [↑](#cite_ref-10) [Daniel S. Abdi](Daniel_Shawul "Daniel Shawul") (**2013**). *Monte carlo methods for estimating game tree size*. [pdf](https://dl.dropboxusercontent.com/u/55295461/perft/perft.pdf)
11. [↑](#cite_ref-11) [Re: yet another attempt on Perft(14)](http://www.talkchess.com/forum/viewtopic.php?t=61119&start=30) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), September 09, 2016
12. [↑](#cite_ref-12) [ankan-ban/perft\_gpu · GitHub](https://github.com/ankan-ban/perft_gpu)
13. [↑](#cite_ref-13) [DGX-1 for AI Research | NVIDIA](https://www.nvidia.com/en-us/data-center/dgx-1/)
14. [↑](#cite_ref-14) [Re: Perft(15): comparison of estimates with Ankan's result](http://www.talkchess.com/forum/viewtopic.php?t=64983&start=9) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 26, 2017
15. [↑](#cite_ref-15) [Re: perft(15)](http://www.talkchess.com/forum/viewtopic.php?t=64983&start=4) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 25, 2017
16. [↑](#cite_ref-16) [Re: Perft speed and depth questions](http://talkchess.com/forum3/viewtopic.php?f=7&t=74153) by [Mark Buisseret](index.php?title=Mark_Buisseret&action=edit&redlink=1 "Mark Buisseret (page does not exist)"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), June 12, 2020
17. [↑](#cite_ref-17) [Re: MC methods](http://www.talkchess.com/forum/viewtopic.php?t=47740&topic_view=flat&start=11) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 13, 2013
18. [↑](#cite_ref-18) [Written in Cobol - Program Written as Chess Buff's Research Aid](http://news.google.com/newspapers?nid=849&dat=19780417&id=h8lOAAAAIBAJ&sjid=DEoDAAAAIBAJ&pg=6180,1080528) by Brad Schultz, [Computerworld](Computerworld "Computerworld"), April 17, 1978, Page 37
19. [↑](#cite_ref-19) [ankan-ban/perft\_gpu · GitHub](https://github.com/ankan-ban/perft_gpu)
20. [↑](#cite_ref-20) [Auriga](http://cinnamonchess.altervista.org/auriga) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella")
21. [↑](#cite_ref-21) [Fast perft on GPU (upto 20 Billion nps w/o hashing)](http://www.talkchess.com/forum/viewtopic.php?t=48387) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), June 22, 2013
22. [↑](#cite_ref-22) [Auriga - distributed and collaborative Perft](http://www.talkchess.com/forum/viewtopic.php?t=58406) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella"), [CCC](CCC "CCC"), November 28, 2015

**[Up one level](Move_Generation "Move Generation")**







 
