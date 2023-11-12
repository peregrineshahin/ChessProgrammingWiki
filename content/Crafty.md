---
title: Crafty
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Crafty**

[](http://twogirlsbeingcrafty.blogspot.de/2011/04/owl-pin-cushion.html) Crafty Owl [[1]](#cite_note-1)
**Crafty**, [[2]](#cite_note-2)

a portable [open source engine](Category:Open_Source "Category:Open Source") supporting the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") written by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") in [ANSI C](C "C") starting in the early 90s, loosely derived from [Cray Blitz](Cray_Blitz "Cray Blitz"), winner of the [1983](WCCC_1983 "WCCC 1983") and [1986](WCCC_1986 "WCCC 1986") World Computer Chess Championships [[3]](#cite_note-3). Crafty pioneered in using [Rotated bitboards](Rotated_Bitboards "Rotated Bitboards") , [parallel search](Parallel_Search "Parallel Search") and probing [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases"). It performs a [principal variation search](Principal_Variation_Search "Principal Variation Search"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), [LMR](Late_Move_Reductions "Late Move Reductions") as well as a [SEE swap algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm") for [move ordering](Move_Ordering "Move Ordering") and to [prune](Pruning "Pruning") "bad" [captures](Captures "Captures") in [quiescence search](Quiescence_Search "Quiescence Search"). In 2006/2007, Crafty switched from rotated to [Magic bitboards](Magic_Bitboards "Magic Bitboards") [[4]](#cite_note-4), according to Robert Hyatt because it was not faster but simpler [[5]](#cite_note-5). Crafty **25.1**, released in October 2016, not only includes an increase in playing strength [[6]](#cite_note-6) but support for [Syzygy bases](Syzygy_Bases "Syzygy Bases") by [Ronald de Man](Ronald_de_Man "Ronald de Man") aided by the coding [contributions](Syzygy_Bases#Fathom "Syzygy Bases") of [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli") [[7]](#cite_note-7). Crafty **25.3** features [playing strength](Playing_Strength "Playing Strength") adjustment between 800 and 2600 Elo [[8]](#cite_note-8).

## Team Members

as mentioned at [WCRCC 2010](WCRCC_2010 "WCRCC 2010") [[9]](#cite_note-9) and [CCT15](CCT15 "CCT15"), 2013 [[10]](#cite_note-10)

- [Peter Berger](Peter_Berger "Peter Berger"), Crafty's [book author](Category:Opening_Book_Author "Category:Opening Book Author") at [WCCC 2004](WCCC_2004 "WCCC 2004"), [WCCC 2005](WCCC_2005 "WCCC 2005") and [WCCC 2006](WCCC_2006 "WCCC 2006")
- [Michael Byrne](Michael_Byrne "Michael Byrne")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
- [Tracy Riegle](index.php?title=Tracy_Riegle&action=edit&redlink=1 "Tracy Riegle (page does not exist)")
- [Peter Skinner](Peter_Skinner "Peter Skinner")

## Tournaments

Crafty participated at four [World Microcomputer Chess Championships](World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship"), the [WMCCC 1996](WMCCC_1996 "WMCCC 1996"), [WMCCC 1997](WMCCC_1997 "WMCCC 1997"), [WMCCC 2000](WMCCC_2000 "WMCCC 2000"), and [WMCCC 2001](WMCCC_2001 "WMCCC 2001"), three [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship"), the [WCCC 2004](WCCC_2004 "WCCC 2004"), [WCCC 2005](WCCC_2005 "WCCC 2005") and [WCCC 2006](WCCC_2006 "WCCC 2006"), the [ACCA Americas' Computer Chess Championships](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship"), the [ACCA World Computer Rapid Chess Championships](ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship"), [CCT](CCT_Tournaments "CCT Tournaments") and various other [tournaments](index.php?title=Tournaments&action=edit&redlink=1 "Tournaments (page does not exist)"). Crafty won the [CCT1](CCT1 "CCT1") in 2000, [CCT5](CCT5 "CCT5") in 2003 and [CCT6](CCT6 "CCT6") in 2004. At the [Fifth Annual ACCA Americas' Computer Chess Championships](ACCA_2010 "ACCA 2010") in 2010 Crafty was runner-up behind [Thinker](Thinker "Thinker") [[11]](#cite_note-11) .

## Descriptions

## 1997

from the [ICGA](ICGA "ICGA") page [[12]](#cite_note-12) :

```C++
Crafty is a "bitmapper" using 64 bit words to represent the chess board, along the lines of the famous [Chess 4.x](Chess_(Program) "Chess (Program)") program from [Northwestern University](Northwestern_University "Northwestern University"). It uses a traditional [alpha/beta search](Alpha-Beta "Alpha-Beta") with the [PVS](Principal_Variation_Search "Principal Variation Search") ([null-window](Null_Window "Null Window")) enhancement, along with [null-moves](Null_Move_Pruning "Null Move Pruning") ([R](Depth_Reduction_R "Depth Reduction R")=2) and lots of search [extensions](Extensions "Extensions") including "[fractional ply extensions](Extensions#FractionalExtensions "Extensions")" to drive the search deeper along interesting lines. It has a very simple [quiescence search](Quiescence_Search "Quiescence Search") that only considers [capture moves](Captures "Captures") and is fairly selective about which captures are included. It does a full endpoint [evaluation](Evaluation "Evaluation"), with no root [pre-processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables") nor [incrementally updated](Incremental_Updates "Incremental Updates") scoring terms. It is currently about 37,000 lines of ANSI C with about 3,000 lines of that being evaluation.

```

```C++
Since Crafty uses [bitmaps](Bitboards "Bitboards"), much of the [evaluation](Evaluation "Evaluation") is significantly shorter than it would be in a more traditional (array-based) [board representation](Board_Representation "Board Representation"), so that this 3,000 lines of code is somewhat misleading (for example, to ask "can this pawn run and promote before the opposing king can get there?" only takes one line of code in Crafty. It is still very fast, searching around 100,000 moves per second. At 60 seconds per move, it solves 297/300 of the [Win At Chess](index.php?title=Win_At_Chess&action=edit&redlink=1 "Win At Chess (page does not exist)") tactical positions. It has a large [opening database](Opening_Book "Opening Book") composed from 250,000 GM games, and uses 3-4-5 piece [endgame databases](Endgame_Tablebases "Endgame Tablebases") during the search (not just at the [root](Root "Root") of the [tree](Search_Tree "Search Tree").) It has played over 100,000 games during the past two years, playing on various [chess servers](Chess_Server "Chess Server") around the world, and has maintained ratings on these servers that are always near the very top. 

```

## 2008

from a [CCC](CCC "CCC") post [[13]](#cite_note-13) :

```C++
Crafty's basic search is pretty simple. Just [PVS](Principal_Variation_Search "Principal Variation Search") + [null-move](Null_Move_Pruning "Null Move Pruning") + [LMR](Late_Move_Reductions "Late Move Reductions") + [check extension](Check_Extensions "Check Extensions") (all others have been removed after testing showed they hurt performance rather than helped), + simple q-search checks (I am playing with this as I write this however and it might change) + simple q-search. I've used [killers](Killer_Heuristic "Killer Heuristic") and [hashing](Transposition_Table "Transposition Table") since middle 70's so those are not new. [Bitboards](Bitboards "Bitboards") were around in the middle 70's so that's not new. I don't think there is anything remarkable in my evaluation, certainly nothing we were not doing 15 years ago or longer, other than tuning adjustments.

```

```C++
As far as tuning goes on LMR and null-move, I have not gone very far afield there. I use [R](Depth_Reduction_R "Depth Reduction R")=3 everywhere. LMR is a 1-ply reduction although I have plans to try a variable reduction so that for moves that look really ugly I reduce them even further (white playing Na1 for example, with king on the other side of the board, no passed pawns, etc...)

```

```C++
I have even run without the check extension, the only one that is left. Many think the purpose of this extension is to find deep mates. That's wrong. The purpose is to try to expose [horizon-effect](Horizon_Effect "Horizon Effect") moves and avoid them when possible. I also want to test a restricted check extension, where it is only applied in the last N plies where the horizon effect is most notable, where right now I apply them everywhere with no limit, always +1 ply added to depth. 

```

## Generation II

Crafty **25.0**, Generation II, December 2015 [[14]](#cite_note-14)

- This version contains a major rewrite of the [parallel search](Parallel_Search "Parallel Search") code, now referred to as **Generation II**. It has a more lightweight split algorithm, that costs the parent MUCH less effort to split the search. The key is that now the individual "helper" [threads](Thread "Thread") do all the work, allocating a split block, copying the data from the parent, etc., rather than the parent doing it all. Gen II based on the [DTS](Dynamic_Tree_Splitting "Dynamic Tree Splitting") "late-join" idea so that a thread will try to join existing split points before it goes to the idle wait loop waiting for some other thread to split with it. In fact, this is now the basis for the new split method where the parent simply creates a split point by allocating a split block for itself, and then continuing the search, after the parent split block is marked as "joinable". Now any idle threads just "jump in" without the parent doing anything else, which means that currently idle threads will "join" this split block if they are in the "wait-for-work" spin loop, and threads that become idle also join in exactly the same way. This is MUCH more efficient, and also significantly reduces the number of split blocks needed during the search. We also now pre-split the search when we are reasonably close to the root of the tree, which is called a "gratuitous split. This leaves joinable split points laying around so that whenever a thread becomes idle, it can join in at these pre-existing split points immediately. We now use a much more conservative approach when dealing with [fail highs](Fail-High "Fail-High") at the [root](Root "Root"). Since [LMR](Late_Move_Reductions "Late Move Reductions") and such have introduced greater levels of [search instability](Search_Instability "Search Instability"), we no longer trust a fail-high at the root if it fails low on the research. We maintain the last [score](Score "Score") returned for every root move, along with the [PV](index.php?title=Principal_variation&action=edit&redlink=1 "Principal variation (page does not exist)") . Either an [exact score](Exact_Score "Exact Score") or the [bound](Bound "Bound") score that was returned. At the end of the iteration, we sort the root move list using the backed-up score as the sort key, and we play the move with the best score. This solves a particularly ugly issue where we get a score for the first move, then another move fails high, but then fails low and the re-search produces a score that is actually WORSE than the original [best move](Best_Move "Best Move"). We still see that, but we always play the best move now. One other efficiency trick is that when the above happens, the search would tend to be less efficient since the best score for that fail-high/fail-low move is actually worse than the best move/score found so far. If this happens, the score is restored to the original best move score (in Search()) so that we continue searching with a good [lower bound](Lower_Bound "Lower Bound") , not having to deal with moves that would fail high with this worse value, but not with the original best move's value.
- We also added a new method to automatically tune the new SMP parameters. The command is autotune and "help autotune" will explain how to run it.
- In addition , we did a complete re-factor of pawn evaluation code. There were too many overlapping terms that made tuning difficult. Now a pawn is classified as one specific class, there is no overlap between classes, which simplifies the code significantly. The code is now easier to understand and modify. In addition, the [passed pawn](Passed_Pawn "Passed Pawn") evaluation was rewritten and consolidates all the passed pawn evaluation in one place. The evaluation used to add a bonus for [rooks behind passed pawns](Tarrasch_Rule "Tarrasch Rule") in rook scoring, blockading somewhere else, etc. All of this was moved to the passed pawn code to make it easier to understand and modify.
- Added a limited version of [late move pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (LMP) for the last two plies. Once a set number of moves have been searched with no fail high, non-interesting moves are simply skipped in a way similar to [futility pruning](Futility_Pruning "Futility Pruning").
- We had a minor change to [history counters](History_Heuristic "History Heuristic") that now rely on a "saturating counter" idea. I wanted to avoid the aging idea, and it seemed to not be so clear that preferring history moves by the depth at which they were good was the way to go. I returned to a history counter idea I tested around 2005 but discarded, namely using a saturating counter. The idea is that a center value (at present 1024) represents a zero score. Decrementing it makes it worse, incrementing it makes it better. But to make it saturate at either end, I only reduce the counter by a fraction of its distance from the saturation point so that once it gets to either extreme value, it will not be modified further avoiding wrap-around. This [basic idea](Relative_History_Heuristic "Relative History Heuristic") was originally reported by [Mark Winands](Mark_Winands "Mark Winands") in 2005. It seems to provide better results (slightly) on very deep searches. One impetus for this was an intent to fold this into a move so that I could sort the moves rather than doing the selection approach I currently use. However, this had a bad effect on testing, since history information is dynamic and is constantly changing, between two moves at the same ply in fact. The sort fixed the history counters to the value at the start of that ply. This was discarded after testing, but the history counter based on the saturating counter idea seemed to be OK and was left in even though it produced minimal Elo gain during testing.
- We change to the way moves are counted, to add a little more consistency to LMR. Now Next\*() returns an order number that starts with 1 and monotonically increases, this order number is used for LMR and such decisions that vary things based on how far down the move list something occurs. Root move counting was particularly problematic with parallel searching, now things are at least "more consistent". The only negative impact is that now the move counter gets incremented even for illegal moves, but testing showed this was a no-change change with one thread, and the consistency with multiple threads made it useful.
- Added the ["counter-move" heuristic](Countermove_Heuristic "Countermove Heuristic") for move ordering ([Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [IJICCA](ICGA_Journal#15_1 "ICGA Journal")) which simply remembers a fail high move and the move at the previous ply. If the hash, captures or killer moves don't result in a fail high, this move is tried next. No significant cost, seems to reduce tree size noticeably. Added a follow-up idea based on the same idea, except we pair a move that fails high with the move two plies back, introducing a sort of "connection" between them. This is a sort of "plan" idea where the first move of the pair enables the second move to fail high. The benefit is that this introduces yet another pair of good moves that get ordered before history moves, and is therefore not subject to reduction. I have been unable to come up with a reference for this idea, but I believe I first saw it somewhere around the time [Fruit](Fruit "Fruit") showed up, I am thinking perhaps in the [JICCA/JICGA](ICGA_Journal "ICGA Journal"). Any reference would be appreciated.
- A minor change to the way the PV and fail-hi/fail-low moves are displayed when [pondering](Pondering "Pondering") .
- Crafty now adds the ponder move to the front of the PV enclosed in parentheses so that it is always visible in console mode. The depths are reaching such extreme numbers the ponder move scrolls off the top of the screen when running in console mode or when "tail -f" is used to watch the log file while a game is in progress. This is a bit trickier than you might think since Crafty displays the game move numbers in the PV.
- The penalty for pawns on same color as bishop now only applies when there is one bishop.

## Leading or Trailing Zeros

Crafty had always mapped square-index 0 to square 'a1', 7 to 'h1', and 63 to 'h8' respectively, but recently (crafty-20.6) reversed the bit-index versus square-index mapping from [leading](BitScan#LeadingZeroCount "BitScan") to [trailing zero count](BitScan#TrailingZeroCount "BitScan") based [little-endian rank-file](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations") (LERF), using [bitscan forward](BitScan#Bitscanforward "BitScan") ([LSB](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations")) to retrieve squares in **a1-h8** order, as most often used in [CPW](index.php?title=MappingHint&action=edit&redlink=1 "MappingHint (page does not exist)") bitboard samples.

### LSB

[Trailing zero count](BitScan#TrailingZeroCount "BitScan") aka bitscan forward for non empty sets as used in [bitboard serialization](Bitboard_Serialization "Bitboard Serialization") for [move generation](Move_Generation "Move Generation") and [evaluation](Evaluation "Evaluation") purposes, is implemented with [x86-64](X86-64 "X86-64") [bsf instruction](BitScan#bsfbsr "BitScan") via intrinsic or [inline assembly](Assembly#InlineAssembly "Assembly") if available (there are also 32-bit [x86](X86 "X86") bsf versions), and a conditional 16-bit [byte](Byte "Byte") lookup approach otherwise - [Windows 64](Windows "Windows"), [Linux 64](Linux "Linux") and lookup versions with preprocessor instructions for conditional compiles omitted [[15]](#cite_note-15):

```C++

int LSB(BITBOARD arg1) {
  unsigned long index;
  if (_BitScanForward64(&index, arg1))
    return index;
  else
    return 64;
}

int static __inline__ LSB(long word)
{
  long dummy, dummy2;

asm("          bsfq    %1, %0     " "\n\t"
    "          jnz     1f         " "\n\t"
    "          movq    $64, %0    " "\n\t"
    "1:                           " "\n\t"
:   "=&r"(dummy), "=&r" (dummy2)
:   "1"((long) (word))
:   "cc");
  return (dummy);
}

unsigned char lsb[65536];

int LSB(BITBOARD arg1) {
  if ( arg1        & 65535) return (lsb[ arg1        & 65535]);
  if ((arg1 >> 16) & 65535) return (lsb[(arg1 >> 16) & 65535] + 16);
  if ((arg1 >> 32) & 65535) return (lsb[(arg1 >> 32) & 65535] + 32);
  return (lsb[arg1 >> 48] + 48);
}

```

### Last One

Earlier Crafty versions prior to 20.6 had a [leading zero count](BitScan#LeadingZeroCount "BitScan") compliant, [big-endian](Big-endian "Big-endian") rank-file mapping. Left-bottom square (from White's point of view) 'a1' with square-index 0 was mapped to the leftmost, arithmetical most significant bit of an unsigned 64-bit integer with bit-index 63, while square 'h8' with square-index 63, was mapped to the rightmost, arithmetical least significant bit with bit-index 0. Bitscan forward and found index [reversal](Flipping_Mirroring_and_Rotating#Rotationby180degrees "Flipping Mirroring and Rotating") was used in LastOne, to retrieve squares in **h8-a1** order [[16]](#cite_note-16):

```C++

int LastOne(BITBOARD arg1)
{
  unsigned long index;
  if (_BitScanForward64(&index, arg1))
    return 63 - index;
  else
    return 64;
}

```

This one was found in 15.17 with [Mac OS](Mac_OS "Mac OS") support [[17]](#cite_note-17)

```C++

int LastOne(register BITBOARD a)
{
  register unsigned long i;
  if (i = a & 0xffffffff)
    return(__cntlzw(i ^ (i - 1)) + 32);
  if (i = a >> 32)
    return(__cntlzw(i ^ (i - 1)));
  return(64);
}

```

## Selected Games

## WCCC 2004

[WCCC 2004](WCCC_2004 "WCCC 2004"), round 9, [Falcon](Falcon "Falcon") - Crafty [[18]](#cite_note-18)

```

[Event "WCCC 2004"]
[Site "Ramat Gan, Israel"]
[Date "2004.07.11"]
[Round "9"]
[White "Falcon"]
[Black "Crafty"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.Nc3 Bd6 5.O-O O-O 6.d3 h6 7.Be3 a6 8.Ba4 b5 
9.Bb3 Na5 10.d4 exd4 11.Bxd4 Be7 12.e5 Ne8 13.Nd5 Nxb3 14.axb3 c5 15.Be3 
Bb7 16.b4 Bxd5 17.Qxd5 Nc7 18.Qb7 Rb8 19.Qe4 cxb4 20.Rfd1 Qc8 21.Nd4 Re8 
22.Nf5 Bf8 23.Qg4 Kh7 24.Bxh6 gxh6 25.Qh5 Kg8 26.Rd3 Re6 27.Rg3+ Rg6 28.Rxg6+ 
fxg6 29.Qxg6+ Kh8 30.Nxh6 Bxh6 31.Qxh6+ Kg8 32.Qg6+ Kf8 33.Rd1 Ne6 34.Rd3 
Ke7 35.Qf6+ Ke8 36.Rg3 Qc5 37.Rg8+ Nf8 38.Rg7 Rb6 39.Qf7+ Kd8  40.Rg8 Kc7 
41.Qxf8 Qxf8 42.Rxf8 a5 43.Ra8 a4 44.g3 Rb8 45.Ra7+ Rb7 46.Ra5 Kb6 47.Ra8 
Ra7 48.Rb8+ Kc6 49.Rc8+ Kd5 50.e6 dxe6 51.Rd8+ Kc5 52.Rc8+ Kb6 53.Re8 a3 
54.Rxe6+ Kc5 55.bxa3 0-1

```

## WCCC 2006

[WCCC 2006](WCCC_2006 "WCCC 2006"), round 8, [Diep](Diep "Diep") - Crafty [[19]](#cite_note-19)

```

[Event "WCCC 2006"]
[Site "Turin, Italy"]
[Date "2006.05.30"]
[Round "8"]
[White "Diep"]
[Black "Crafty"]
[Result "0-1"]

1.e4 e5 2.Nf3 d6 3.d4 exd4 4.Nxd4 Nf6 5.Nc3 Be7 6.Bf4 O-O 7.Qd2 c6 8.O-O-O b5 
9.f3 b4 10.Nce2 c5 11.Nb3 Nc6 12.Bxd6 c4 13.Nc5 Qa5 14.Bxe7 Nxe7 15.Qd6 Nf5 
16.exf5 Qxa2 17.g4 a5 18.Rd4 Re8 19.Kd1 Qxb2 20.Nc1 b3 21.cxb3 cxb3 22.Bd3 a4 
23.Re1 Rxe1+ 24.Kxe1 Qxc1+ 25.Ke2 Bb7 26.Qd8+ Ne8 27.Qe7 Bc6 28.Bc4 Nf6 29.Bxf7+ 
Kh8 30.Nd3 b2 31.Rd8+ Rxd8 32.Qxd8+ Be8 33.Bxe8 Qc2+ 34.Ke3 Nd5+ 35.Kd4 Qc3+ 
36.Ke4 Qc7 37.Qxc7 Nxc7 38.Nxb2 a3 39.Bf7 axb2 40.Ba2 Nb5 41.Kd3 Na3 42.g5 b1=B+ 
43.Bxb1 Nxb1 44.h4 Kg8 45.h5 Kf8 46.f4 Ke7 47.Kd4 Nd2 48.Ke3 Nc4+ 49.Kd4 Nd6 
50.Ke5 Nf7+ 51.Kd5 h6 52.f6+ gxf6 53.g6 Nd8 54.f5 Nb7 55.Kc6 Na5+ 0-1

```

## Copyright

Many programmers did not grasp Crafty's [Copyright](https://en.wikipedia.org/wiki/Copyright) statement, but apparently took remarks by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") like in his reply to [Ren Wu](Ren_Wu "Ren Wu"), January 26, 1999, concerning [code reuse](https://en.wikipedia.org/wiki/Code_reuse) and not [reinventing the wheel](https://en.wikipedia.org/wiki/Reinventing_the_wheel) as alibi for their chess programming [[20]](#cite_note-20) :

```C++
This is a basic tenet of software engineering called 'code reuse'. Why should I pay you to write something from scratch and take a year, if you can take something that exists and modify it to do the same thing in a month? And then I don't have as much trouble debugging and testing, since it is mostly already done...

```

```C++
that's not a bad side to this... Of course occasionally starting over is a good thing. But not starting from 'scratch'. IE if you don't know what has already been tried, you will re-invent the same bad wheels over and over and probably follow the same footsteps many before you did... software engineering wants to avoid that 'reinvention' problem... 

```

[Robert Hyatt](Robert_Hyatt "Robert Hyatt") further on the copyright problem [[21]](#cite_note-21) :

```C++
My primary requirement is that if something is done to crafty to make it 'better', then that 'something' must be as public as the original code was. Because many have contributed bits and pieces... Eugene, George, Steffen, Mark, SJE, and many others that are to numerous to mention. Seems unfair that they modify what I did, then they make their stuff public, and then someone else takes _all_ of this and purports it to be 'original'.

```

```C++
I suppose it has to do with 'national morals' or whatever, ie the software piracy problem in China, to name but one. 

```

## Crafty Clones

- [Bionic Impakt](Bionic_Impakt "Bionic Impakt")
- [Brause](Brause "Brause")
- [Chinito](Chinito "Chinito")
- [Fafis](Fafis "Fafis")
- [Gunda-1](Gunda-1 "Gunda-1")
- [Kaissa (BY)](</Kaissa_(BY)> "Kaissa (BY)")
- [LaGrande](LaGrande "LaGrande")
- [LaPetite](LaPetite "LaPetite")
- [Patriot](Patriot "Patriot")
- [Vafra](index.php?title=Vafra&action=edit&redlink=1 "Vafra (page does not exist)")
- [Voyager](Voyager "Voyager")

## See also

- [Cray Blitz](Cray_Blitz "Cray Blitz")
- [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")
- [Open Source Engines](Category:Open_Source "Category:Open Source")

## Publications

## 1997 ...

- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1997**). *CRAFTY Goes Deep*. [ICCA Journal, Vol. 20, No. 2](ICGA_Journal#20_2 "ICGA Journal")

## 2000 ...

- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Modeling the “Go Deep” Behaviour of CRAFTY and DARK THOUGHT.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9") » [Depth](Depth "Depth"), [DarkThought](DarkThought "DarkThought")
- [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_11)*. [CG 2002](CG_2002 "CG 2002"), [pdf](http://www.pradu.us/old/Nov27_2008/Buzz/research/parallel/movemap_heuristic.pdf) » [Neural MoveMap Heuristic](Neural_MoveMap_Heuristic "Neural MoveMap Heuristic")
- [Albert Xin Jiang](Albert_Xin_Jiang "Albert Xin Jiang") (**2003**). *Implementation of Multi-ProbCut in Chess*. CPSC 449 Thesis, [pdf](http://www.cs.ubc.ca/%7Ejiang/papers/thesis.pdf)
- [Jan Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen") (**2005**). *New Results in Deep-Search Behaviour*. [ICGA Journal, Vol. 28, No. 4](ICGA_Journal#28_4 "ICGA Journal"), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.104.9527)
- [Yew Jin Lim](Yew_Jin_Lim "Yew Jin Lim"), [Wee Sun Lee](Wee_Sun_Lee "Wee Sun Lee") (**2006**). *RankCut - A Domain Independent Forward Pruning Method for Games*. [AAAI 2006](Conferences#AAAI-2006 "Conferences"), [pdf](http://www.yewjin.com/storage/papers/rankcut.pdf)  » [RankCut](RankCut "RankCut")
- [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2006**). *Computer Analysis of World Chess Champions*. [ICGA Journal, Vol. 29, No. 2](ICGA_Journal#29_2 "ICGA Journal"), [pdf](https://ailab.si/matej/doc/Computer_Analysis_of_World_Chess_Champions.pdf) [[22]](#cite_note-22) [[23]](#cite_note-23)
- [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2006**). *[Computer Analysis of Chess Champions](https://link.springer.com/chapter/10.1007/978-3-540-75538-8_1)*. [CG 2006](CG_2006 "CG 2006")
- [Yew Jin Lim](Yew_Jin_Lim "Yew Jin Lim") (**2007**). *On Forward Pruning in Game-Tree Search*. Ph.D. thesis, [National University of Singapore](https://en.wikipedia.org/wiki/National_University_of_Singapore), [pdf](http://www.yewjin.com/storage/papers/PhDThesisLimYewJin.pdf)
- [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2007**). *Factors affecting diminishing returns for searching deeper*. [CGW 2007](CGW_2007 "CGW 2007") » Crafty, [Rybka](Rybka "Rybka"), [Shredder](Shredder "Shredder"), [Diminishing Returns](Depth#DiminishingReturns "Depth")
- [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2007**). *Factors affecting diminishing returns for searching deeper*. [ICGA Journal, Vol. 30, No. 2](ICGA_Journal#30_2 "ICGA Journal"), [pdf](http://www.ailab.si/matej/doc/Factors_Affecting_Diminishing_Returns.pdf)
- [Matej Guid](Matej_Guid "Matej Guid"), [Aritz Pérez](Aritz_P%C3%A9rez "Aritz Pérez"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2007**). *How trustworthy is Crafty's analysis of world chess champions*? [CGW 2007](CGW_2007 "CGW 2007")
- [Matej Guid](Matej_Guid "Matej Guid"), [Aritz Pérez](Aritz_P%C3%A9rez "Aritz Pérez"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2008**). *How trustworthy is Crafty's analysis of world chess champions*? [ICGA Journal, Vol. 31, No. 3](ICGA_Journal#31_3 "ICGA Journal"), [pdf](http://www.ailab.si/matej/doc/How_Trustworthy_is_Craftys_Analysis.pdf)

## 2010 ...

- [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [David J. King](index.php?title=David_J._King&action=edit&redlink=1 "David J. King (page does not exist)") (**2010**). *[A new enhancement to MTD(f)](https://rke.abertay.ac.uk/en/publications/a-new-enhancement-to-mtdf)*. Games and Arts, [Abertay University](https://en.wikipedia.org/wiki/Abertay_University), [ResearchGate](https://www.researchgate.net/publication/304307495_A_New_Enhancement_to_MTDf) » [MTD(f)](</MTD(f)> "MTD(f)") [[24]](#cite_note-24)
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2014**). *A Solution to Short PVs Caused by Exact Hash Matches*. [ICGA Journal, Vol. 37, No. 3](ICGA_Journal#37_3 "ICGA Journal") » [Transposition Table](Transposition_Table "Transposition Table"), [Separate TT for the PV](Principal_Variation#SeparateTT "Principal Variation")
- [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2014**). *Computer Chess Endgame Play with Pawns: Then and Now*. [ICGA Journal, Vol. 37, No. 4](ICGA_Journal#37_4 "ICGA Journal") » [Peasant](Peasant "Peasant"), [Pawn Endgame](Pawn_Endgame "Pawn Endgame")
- [Guy Haworth](Guy_Haworth "Guy Haworth") (**2015**). *Chess Endgame News*. [ICGA Journal, Vol. 38, No. 1](ICGA_Journal#38_1 "ICGA Journal") » [FinalGen](FinalGen "FinalGen")

## 2020 ...

- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2020**). *The history of BLITZ/CRAY-BLITZ/CRAFTY*. [ICGA Journal, Vol. 42, Nos. 2-3](ICGA_Journal#42_23 "ICGA Journal")

## Forum Posts

## 1995 ...

- [Re: Crafty version 8.7](http://groups.google.com/group/rec.games.chess.computer/msg/a1c2d43fab3601ab) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 05, 1995
- [Crafty V9.22](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/f2c922d3c296bbbe) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 05, 1996
- [Crafty V9.26](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1c03a81c896c048b) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 08, 1996
- [Crafty's opening book - technical details](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/784986ccb84e473b) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 04, 1996
- [Crafty V11.3](https://groups.google.com/d/msg/rec.games.chess.computer/tcjwWnFhXt4/ifkLE7GwfSEJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 22, 1996 » [Fractional Extensions](Extensions#FractionalExtensions "Extensions")
- [Crafty 11.15](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/f2ff4847ad3bb180) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 30, 1997
- [Repetitions in Crafty](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/6e999936bc7e5200) by [Martin Borriss](Martin_Borriss "Martin Borriss"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 30, 1997 » [Repetitions](Repetitions "Repetitions")
- [quiescence search](https://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ca0300b50438a388) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 16, 1997 » [Quiescence Search](Quiescence_Search "Quiescence Search"), [Check](Check "Check")
- [Crafty and fastest Cray: question to Bob](https://www.stmintz.com/ccc/index.php?id=12532) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), December 01, 1997
- [Parallel Crafty](https://www.stmintz.com/ccc/index.php?id=15912) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 19, 1998
- [Current Crafty strength on SMP?](https://groups.google.com/d/msg/rec.games.chess.computer/C6z6Nnh2Nbs/G3LOexi_PMUJ) by Charlton Harrison, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 29, 1998
- [crafty copyright problem](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/cc8520f40dc69198) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 17, 1999 » [Voyager](Voyager "Voyager")
- [Crafty Modifications MUST be made available to Robert Hyatt](https://www.stmintz.com/ccc/index.php?id=43533) by [KarinsDad](index.php?title=KarinsDad&action=edit&redlink=1 "KarinsDad (page does not exist)"), [CCC](CCC "CCC"), February 17, 1999
- [Crafty implications ...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ed89415506592e02) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 4, 1999
- [Do have the Crafty the Assembler written core?](https://www.stmintz.com/ccc/index.php?id=75923) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), November 01, 1999

## 2000 ...

- [Crafty internal iterative deepening](https://www.stmintz.com/ccc/index.php?id=92088) by [Tijs van Dam](index.php?title=Tijs_van_Dam&action=edit&redlink=1 "Tijs van Dam (page does not exist)"), [CCC](CCC "CCC"), January 26, 2000 » [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Crafty 17.13 - re-importing FEN files?](https://www.stmintz.com/ccc/index.php?id=136233) by [Wieland Belka](Wieland_Belka "Wieland Belka"), [CCC](CCC "CCC"), November 02, 2000
- [Crafty 17.13 - using game archives by engines?](https://www.stmintz.com/ccc/index.php?id=136234) by [Wieland Belka](Wieland_Belka "Wieland Belka"), [CCC](CCC "CCC"), November 02, 2000
- [razoring in crafty version 16.9, mid 1999](https://www.stmintz.com/ccc/index.php?id=246598) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), August 21, 2002
- [Crafty SMP questions](https://www.stmintz.com/ccc/index.php?id=310051) by Matthew Hull, [CCC](CCC "CCC"), August 05, 2003 » [SMP](SMP "SMP")
- [Crafty 19.08 SE 2004 released ...](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45863) by [Michael Byrne](Michael_Byrne "Michael Byrne"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 01, 2004 » [Wb2UCI](Wb2UCI "Wb2UCI")
- [Re: Crafty 1910 SE vs Ruffian2 I hate this , but](https://www.stmintz.com/ccc/index.php?id=347219) by [Peter Skinner](Peter_Skinner "Peter Skinner"), [CCC](CCC "CCC"), February 04, 2004 » [Ruffian](Ruffian "Ruffian")
- [is this a sign of broken smp](https://www.stmintz.com/ccc/index.php?id=353751) by [Michael Byrne](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), March 09, 2004 » [SMP](SMP "SMP")
- [Question about Crafty and Bishop Pair](https://www.stmintz.com/ccc/index.php?id=376529) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), July 13, 2004 » [Bishop Pair](Bishop_Pair "Bishop Pair")

## 2005 ...

- [Re: need help in compiling Crafty](https://www.stmintz.com/ccc/index.php?id=412534) by [Joshua Haglund](index.php?title=Joshua_Haglund&action=edit&redlink=1 "Joshua Haglund (page does not exist)"), [CCC](CCC "CCC"), February 19, 2005
- [Crafty and assembly code](https://www.stmintz.com/ccc/index.php?id=424820) by [Alain Zanchetta](index.php?title=Alain_Zanchetta&action=edit&redlink=1 "Alain Zanchetta (page does not exist)"), [CCC](CCC "CCC"), May 08, 2005
- [Re: BitBoard Tests Magic v Non-Rotated 32 Bits v 64 Bits](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=140141&t=16002) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 25, 2007 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [crafty-22.0](http://www.talkchess.com/forum/viewtopic.php?t=19706) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), February 18, 2008
- [Crafty questions](http://www.talkchess.com/forum/viewtopic.php?t=21194) by [Pablo Vazquez](Pablo_Vazquez "Pablo Vazquez"), [CCC](CCC "CCC"), May 16, 2008
- [Re: Lemming Poll](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=220004&t=23894) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 22, 2008 » [Tapered Eval](Tapered_Eval "Tapered Eval"), [LearningLemming](LearningLemming "LearningLemming")
- [Crafty - no analysis output near mate?](http://www.talkchess.com/forum/viewtopic.php?t=25224) by [cyberfish](Matthew_Lai "Matthew Lai"), December 03, 2008
- [MTD(f) experiments with Crafty](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=31130) by [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [CCC](CCC "CCC"), December 18, 2009 » [MTD(f)](</MTD(f)> "MTD(f)") [[25]](#cite_note-25)

## 2010 ...

- [Crafty Transpostion Table Question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=34606) by [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [CCC](CCC "CCC"), May 30, 2010 » [Lockless Hashing](Shared_Hash_Table#Lockless "Shared Hash Table")
- [old crafty vs new crafty on new hardware](http://www.talkchess.com/forum/viewtopic.php?t=36040) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 11, 2010
- [Crafty tests show that Software has advanced more](http://www.talkchess.com/forum/viewtopic.php?t=36050) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 12, 2010
- [Final results - Crafty - hardware vs software](http://www.talkchess.com/forum/viewtopic.php?t=36059) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 13, 2010
- [hardware doubling number for Crafty](http://www.talkchess.com/forum/viewtopic.php?t=36088) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 15, 2010

**2011**

- [On Crafty...](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=407977&t=39149) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), May 22, 2011
- [Re: Robert - How did you came up with the name Crafty](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=410448&t=39381) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 16, 2011
- [Re: Still waiting on Ed](http://www.open-chess.org/viewtopic.php?f=3&t=1477&start=10#p13013) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 07, 2011 » on 22.1 vs. 23.4. differences
- [Re: Still waiting on Ed](http://www.open-chess.org/viewtopic.php?f=3&t=1477&start=20#p13017) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 07, 2011 » on 22.1 vs. 23.4. differences
- [ICGA rule #2 / opening books / Diep-Crafty, Turino 2006](http://www.talkchess.com/forum/viewtopic.php?t=40853) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), October 22, 2011 » [Opening Book](Opening_Book "Opening Book"), [WCCC 2006](WCCC_2006 "WCCC 2006")

**2012**

- [Crafty source](http://www.talkchess.com/forum/viewtopic.php?t=45338) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 26, 2012

**2013**

- [Crafty 23.6 released](http://www.talkchess.com/forum/viewtopic.php?t=48351) by [Peter Skinner](Peter_Skinner "Peter Skinner"), [CCC](CCC "CCC"), June 20, 2013
- [interesting SMP bug](http://www.talkchess.com/forum/viewtopic.php?t=49450) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 24, 2013 » [Parallel Search](Parallel_Search "Parallel Search")
- [Crafty 23.8](http://www.talkchess.com/forum/viewtopic.php?t=50030) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 11, 2013

**2014**

- [Crafty 24.0](http://www.talkchess.com/forum/viewtopic.php?t=52432) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), May 26, 2014
- [Crafty 24.1](http://www.talkchess.com/forum/viewtopic.php?t=53907) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), October 01, 2014
- [Threads test incl. Crafty 24.1](http://www.talkchess.com/forum/viewtopic.php?t=54059) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 15, 2014 » [Thread](Thread "Thread"), [Parallel Search](Parallel_Search "Parallel Search")
- [Android Version of Crafty](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=54795) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), December 30, 2014 » [Android](Android "Android")

## 2015 ...

- [Grafty vs Crafty](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=30107) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), April 21, 2015 » [Stockfish](Stockfish "Stockfish")
- [parallel speedup and assorted trivia](http://www.talkchess.com/forum/viewtopic.php?t=56595) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 05, 2015 » [Parallel Search](Parallel_Search "Parallel Search")
- [Crafty UCI version](http://www.talkchess.com/forum/viewtopic.php?t=56935) by [Marek Soszynski](index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), July 10, 2015 » [UCI](UCI "UCI")
- [An interesting parallel search non-bug](http://www.talkchess.com/forum/viewtopic.php?t=58160) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 05, 2015 » [Parallel Search](Parallel_Search "Parallel Search")
- [Crafty 25.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=58688) by Michael B, [CCC](CCC "CCC"), December 25, 2015
- [Crafty 25.0 announcement](http://www.talkchess.com/forum/viewtopic.php?t=58711) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), December 28, 2015

**2016**

- [crafty eval cache](http://www.talkchess.com/forum/viewtopic.php?t=58758) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), January 01, 2016 » [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [NUMA 101](http://www.talkchess.com/forum/viewtopic.php?t=58830) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 07, 2016 » [NUMA](NUMA "NUMA")
- [Crafty 25.0.1](http://www.talkchess.com/forum/viewtopic.php?t=58931) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 15, 2016
- [Crafty's four hash tables](http://www.talkchess.com/forum/viewtopic.php?t=58944) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), January 17, 2016 » [Hash Table](Hash_Table "Hash Table")
- [Crafty c questions](http://www.talkchess.com/forum/viewtopic.php?t=59464) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), March 10, 2016 » [C](C "C")
- [Crafty chess engine](http://www.talkchess.com/forum/viewtopic.php?t=59577) by Krzysztof Grzelak, [CCC](CCC "CCC"), March 20, 2016
- [Crafty SMP measurement](http://talkchess.com/forum/viewtopic.php?t=59745) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), April 04, 2016 » [Parallel Search](Parallel_Search "Parallel Search")
- [Around Crafty dev. ...](http://www.talkchess.com/forum/viewtopic.php?t=61289) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), August 31, 2016

[Re: Around Crafty dev. ...](http://www.talkchess.com/forum/viewtopic.php?t=61289&start=2) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 01, 2016

- [Crafty 25.1 Release](http://www.talkchess.com/forum/viewtopic.php?t=61594) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), October 04, 2016
- [Crafty v25.2 Release](http://www.talkchess.com/forum/viewtopic.php?t=61874) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), October 29, 2016

**2017 ...**

- [Crafty Play By Elo ( Crafty v25.3)](http://www.talkchess.com/forum/viewtopic.php?t=62907) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), January 23, 2017 » [Playing Strength](Playing_Strength "Playing Strength")
- [SYZYGY question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71512) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 11, 2019 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases"), [En passant](En_passant "En passant")
- [Crafty 25.3 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71585) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), August 17, 2019

## 2020 ...

- [Crafty 25.6](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72970) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), February 01, 2020
- [Crafty 25.6 search stability](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73738) by [jhaglund2](index.php?title=Joshua_Haglund&action=edit&redlink=1 "Joshua Haglund (page does not exist)"), [CCC](CCC "CCC"), April 23, 2020
- [Crafty NNUE Chess Engine?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77200) by supersharp77, [CCC](CCC "CCC"), April 29, 2021 » [NNUE](NNUE "NNUE"), [Vafra](index.php?title=Vafra&action=edit&redlink=1 "Vafra (page does not exist)") [[26]](#cite_note-26)

## External Links

## Chess Engine

- [GitHub - MichaelB7/Crafty](https://github.com/MichaelB7/Crafty)
- [Crafty Chess](http://www.craftychess.com/) managed by [Tracy Riegle](index.php?title=Tracy_Riegle&action=edit&redlink=1 "Tracy Riegle (page does not exist)")
- [Index of /downloads/source](http://www.craftychess.com/downloads/source/)
- [Crafty from Wikipedia](https://en.wikipedia.org/wiki/Crafty)
- [Crafty Documentation](http://www.craftychess.com/documentation/craftydoc.html)
- [Crafty's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=34)
- [The chess games of Crafty (Computer)](http://www.chessgames.com/perl/chessplayer?pid=5405) from [chessgames.com](http://www.chessgames.com/index.html)
- [Crafty](http://wbec-ridderkerk.nl/html/details1/Crafty.html) from [WBEC Ridderkerk](WBEC "WBEC")
- [How Far We've Come: 20 Years of Personal Computing](http://wondersmith.com/rants/howfar.htm) by [Blake Linton Wilfong](http://wondersmith.com/scifi/author.htm), November 05, 2000 » [ACM 1981](ACM_1981 "ACM 1981"), [Sargon](Sargon "Sargon"), [Cray Blitz](Cray_Blitz "Cray Blitz")
- [186.crafty: SPEC CPU2000 Benchmark Description](http://www.spec.org/cpu2000/CINT2000/186.crafty/docs/186.crafty.html)
- [Crafty Versions](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Crafty&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/40](CCRL "CCRL")

## Misc

- [crafty - Wiktionary](http://en.wiktionary.org/wiki/crafty)
- [Craft from Wikipedia](https://en.wikipedia.org/wiki/Craft)
- [American craft from Wikipedia](https://en.wikipedia.org/wiki/American_craft)
- [Arts and Crafts movement from Wikipedia](https://en.wikipedia.org/wiki/Arts_and_Crafts_movement)
- [American Craftsman from Wikipedia](https://en.wikipedia.org/wiki/American_Craftsman)
- [Guitar Craft from Wikipedia](https://en.wikipedia.org/wiki/Guitar_Craft)
- [Robert Fripp](Category:Robert_Fripp "Category:Robert Fripp") and the League of Crafty Guitarists, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. [↑](#cite_ref-1) [Two Girls Being Crafty: Owl Pin Cushion](http://twogirlsbeingcrafty.blogspot.de/2011/04/owl-pin-cushion.html)
1. [↑](#cite_ref-2) [Re: Robert - How did you came up with the name Crafty](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=410448&t=39381) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 16, 2011
1. [↑](#cite_ref-3) [Crafty from Wikipedia](https://en.wikipedia.org/wiki/Crafty)
1. [↑](#cite_ref-4) [Re: Fastest Magic Move Bitboard Generator ready to use](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5452&start=56) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 09, 2006
1. [↑](#cite_ref-5) [Re: BitBoard Tests Magic v Non-Rotated 32 Bits v 64 Bits](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=140141&t=16002) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 25, 2007
1. [↑](#cite_ref-6) [Crafty Chess](http://www.craftychess.com/) managed by [Tracy Riegle](index.php?title=Tracy_Riegle&action=edit&redlink=1 "Tracy Riegle (page does not exist)")
1. [↑](#cite_ref-7) [Crafty 25.1 Release](http://www.talkchess.com/forum/viewtopic.php?t=61594) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), October 04, 2016
1. [↑](#cite_ref-8)  [Crafty Play By Elo ( Crafty v25.3)](http://www.talkchess.com/forum/viewtopic.php?t=62907) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), January 23, 2017
1. [↑](#cite_ref-9) [2010 Fourth Annual ACCA World Computer Rapid Chess Championships - Participants](http://aigames.net/ACCA/ACCAWCRCC/2010ACCAWCRCC/WCRCCPart.html)
1. [↑](#cite_ref-10) [CCT 15 Participants | CCT Events](https://www.cctchess.com/previous-events/cct-15/participants/)
1. [↑](#cite_ref-11) [The 2010 Fifth Annual ACCA Americas' Computer Chess Championships - Results](http://compchess.org/ACCAChampionships/ACCA2010Championships/2010ACCCResults.html)
1. [↑](#cite_ref-12) [Crafty's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=34)
1. [↑](#cite_ref-13) [Re: Hardware vs Software - test result](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=235340&t=25215) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), December 03, 2008
1. [↑](#cite_ref-14) [Crafty 25.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=58688) by Michael B, [CCC](CCC "CCC"), December 25, 2015
1. [↑](#cite_ref-15) [Index of /downloads/source](http://www.craftychess.com/downloads/source/) crafty-23.5.zip, inline64.h, boolean.c
1. [↑](#cite_ref-16) [Index of /downloads/source](http://www.craftychess.com/downloads/source/), crafty-20.5.zip, boolean.c
1. [↑](#cite_ref-17) [Index of /downloads/source](http://www.craftychess.com/downloads/source/), crafty-15.17.zip, boolean.c
1. [↑](#cite_ref-18) [Ramat-Gan 2004 - Chess - Round 9 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=24&round=9&id=3)
1. [↑](#cite_ref-19) [Turin 2006 - Chess - Round 8 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=16&round=8&id=5)
1. [↑](#cite_ref-20) [Re: Bionic v Crafty - a possible solution](https://www.stmintz.com/ccc/index.php?id=40922) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 26, 1999
1. [↑](#cite_ref-21) [Re: crafty copyright problem](http://groups.google.com/group/rec.games.chess.computer/msg/db825bdc948464b6) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 17, 1999
1. [↑](#cite_ref-22) [Computers choose: who was the strongest player?](https://en.chessbase.com/post/computers-choose-who-was-the-strongest-player-), [ChessBase News](ChessBase "ChessBase"), October 30, 2006
1. [↑](#cite_ref-23) [Computer analysis of world champions](https://en.chessbase.com/post/computer-analysis-of-world-champions) by [Søren Riis](S%C3%B8ren_Riis "Søren Riis"), [ChessBase News](ChessBase "ChessBase"), November 02, 2006
1. [↑](#cite_ref-24) [MTD(f) experiments with Crafty](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=31130) by [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [CCC](CCC "CCC"), December 18, 2009 » [MTD(f)](</MTD(f)> "MTD(f)")
1. [↑](#cite_ref-25) [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [David J. King](index.php?title=David_J._King&action=edit&redlink=1 "David J. King (page does not exist)") (**2010**). *[A new enhancement to MTD(f)](https://rke.abertay.ac.uk/en/publications/a-new-enhancement-to-mtdf)*. Games and Arts, [Abertay University](https://en.wikipedia.org/wiki/Abertay_University)
1. [↑](#cite_ref-26) [Vafra](http://www.jurjevic.org.uk/chess/vafra/index.html) by [Robert Jurjević](index.php?title=Robert_Jurjevi%C4%87&action=edit&redlink=1 "Robert Jurjević (page does not exist)")

**[Up one level](Engines "Engines")**

