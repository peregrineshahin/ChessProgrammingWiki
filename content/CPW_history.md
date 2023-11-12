---
title: CPW history
---
**[Home](Home "Home") * [Engines](Engines "Engines") * [CPW-Engine](CPW-Engine "CPW-Engine") * History**

## December 2014, Version 1.1

- [LMR](Late_Move_Reductions "Late Move Reductions") added
- [eval pruning](Reverse_Futility_Pruning "Reverse Futility Pruning") added
- major cleanup of evaluation function
- new king attack function
- new [futility pruning](Futility_Pruning "Futility Pruning") restrictions

## September 2008

## 05.09.2008

- display of book alternatives
- FIX concerning illegal book moves
- NEW: book moves can be selected by their frequency

## 04.09.2008

- a couple of int functions whose returned value has not been used renamed to voids
- clearing of the search driver now done in search_run, not in time_xxx_go
- more comments

## 03.09.2008

- in search procedures renamed smove m[256] to smove movelist[256];

"m" should be reserved for a single move

- move_isPseudoLegal() replaced by move_isLegal() which tests for check

## 02.09.2008

- NEW: search_iterate() stops on one legal reply after searching to depth 4
- new names and location of functions move_isPseudoLegal() and move_countLegal()
- more comments in search.cpp
- separated book.h
- FIX: replies to moves excluded from the opening book ( again )

## August 2008

## 29.08.2008

- small internal book (in case that book file is missing)
- FIX: timing-bug

## 27.08.2008

- FIX: various bugs occuring in fast time controls
- only legal moves are checked at the root
- FIX: hash memory allocation change possible

total memory = hash + hash/4(pawn hash) + 4mb(opening book, etc)

- FIX: communication bug, stealing cpu of opponent
- FIX: en passant flag is not set when no pawn can execute en-passant capture

( which helps with opening book and increases the number of transposition table cutoffs )

- change in delta pruning
- a couple of range checks added
- numerous opening book code fixes
- simplification of move parsing routine
- because of ChessWar, reintroduced badCapture() pruning in quiescence search

## 26.08.2008

- NEW: program can use a TSCP-like book, exclude some moves out of it and handle transpositions
- changed time management + comments

## 26.08.2008

- NEW: program can use a TSCP book and handle transpositions

## 25.08.2008

- FIX: removed all compiler-warnings (more attention given to variable types)
- FIX: correct output of mate-values
- FIX: transposition-table crash fixed, when size set to 0
- FIX: ==/= bug in eval.cpp
- encapsulation of useKiller
- slight changes with futility-pruning
- created header file for transposition-table
- NEW: 4% speedup through prefetching the transpositiontable entry

## 22.08.2008

-FIX in pawn shield evaluation "=" replaced by "==" (aaargh!)

## 21.08.2008

- new pruning in QS (testing if a queen capture and/or promotion can improve alpha)

## 19.08.2008

- NEW: evaluation hashtable (currently disabled, since lazy eval performs much better,

but might become useful after a rewrite of evaluation function)

- finding good configuration of compiler switches

## 17.08.2008

- further restructuring of search routines
- NEW: aspiration search

## 16.08.2008

- separating setKillers() function

## 12.08.2008

- serious restructuring of root search functions (sepatating search_root and search_iterate)

## 10.08.2008

-FIX: hash moves from lower depths used for sorting

## 08.08.2008

- NEW: contempt() function instead of constant

## 07.08.2008

- NEW: adaptative null move pruning
- FIX: loop counter for killer moves initialized as 0, not as 1 (bad Pascal habits!)
- FIX: in info_currmove() first move number is 1, not 0 (bad C habits!)
- in search() variable move_to_make instead of a loop redetecting best move
- in movegen.ccp vectors represented as constants (NE etc) not as numbers
- in movegen.cpp unnecessary int functions changed to void
- getting rid of is_futility compiler switch

## 05.08.2008

- NEW: Pawn-hashtables
- NEW: fast_eval()
- because of that changes futility pruning gives some benefit, so it's enabled now
- added move_iscapt() and move_isprom() to improve readability

## 04.08.2008

- NEW: function slavMistake() that discourages blocking the center
- NEW: futility pruning (currently disabled, as node savings do not offset speed loss)

## July 2008

## 03.08.2008

- separating com_nothing() function
- more customizable evaluation parameters

## 30.07.2008

- NEW: CPW.ini stores evaluation constants
- Transposition table: The size is scaled down to the next lower power of 2
- thus replacing the slow mod operation by a quick 'and' operation when generating the tt-index
- reducing the tt-entry size from 24 to 16 bytes. (changing alignment)
- stop tt_save from overwriting an entry with the same position of a shallower depth
- com (uci-protocol): 'setoption name Hash value n' works now

## 28.07.2008

- TWEAK: reducing a score jump caused by castling
- TWEAK: bringing down mobility scores and second lazy evaluation limit
- TWEAK: penalty for the lack of pawns

## 26.07.2008

- TWEAK: raising piece/square scores
- TWEAK: modification of evalFianchetto()

## 22.07.2008

- NEW: [history heuristic](History_Heuristic "History Heuristic")
- TWEAK: doubled pawns do not count as a double king's shield
- TWEAK: expanded pawn center evaluation: support for e4 pawn also counts

## 21.07.2008

- NEW: basic fianchetto evaluation
- NEW: console interface will accept only pseudo-legal moves

## 20.07.2008

- NEW: killer heuristics (ugly code in need of redesign, but gains a couple of percent nodes)
- FIX: nodes per second calculation overflow problem fixed
- NEW: more human-friendly output in console mode

## 19.07.2008

- NEW: console mode reacts to "st" and "sd" commands

## 18.07.2008

- separating the eval.h file for function not used outside eval.cpp (better encapsulation)
- making use of 088_math.h and changing most of its functions into macros
- TWEAK: rooks on open files near the king increase tropism
- scaling of middlegame king evaluation affects also pcsq score
- creating a eval_vect struct collecting partial scores
- serious restructuring of eval.cpp
- creating printEval() function giving some insight into evaluation components
- FIX: fixed a bug with [delta pruning](index.php?title=Delta_pruning&action=edit&redlink=1 "Delta pruning (page does not exist)") (it does not prune promotions anymore)

## 11.07.2008

- better time management
- FIX: time check done once every 1024 nodes, not in each node - massive speedup
- optimization of doubled pawn eval (a table instead of multiple ifs)

## 10.07.2008

- NEW: [PVS](Principal_Variation_Search "Principal Variation Search") added
- FIX: a check extension also at the root (hash results from a move ago will be used more consistently)
- separated PIECE_VAL and SORT_VAL, simplifying the code and getting rid of problems with king value
- in fillSq() and clearSq() the count of pawns on a file is kept, so doubled pawns and open files are finally evaluated
- fillSq() and clearSq() don't update piece/square value for a king (this is done within eval.cpp)

## 01.07.2008

- FIX: check extension bug fixed

## June 2008

## 30.06.2008

- FIX: leaf node hashing bug fixed
- some move sorting experiments

## 29.06.2008

- repetition detection - from now on CPW becomes a chess engine (as opposite to almost-chess engine)
- FIX: solved the bug with the hash-values when time is over (tt_save only saves the hash, when time_over == false)
- FIX: solved the bug with the communication
- [null move](Null_Move_Pruning "Null Move Pruning") implemented

**[Up one Level](CPW-Engine "CPW-Engine")**

