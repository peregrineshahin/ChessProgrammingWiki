---
title: GopherCheck
---
**[Home](Home "Home") * [Engines](Engines "Engines") * GopherCheck**

\[ Pocket Gopher <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**GopherCheck**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Stephen Lovell](index.php?title=Stephen_Lovell&action=edit&redlink=1 "Stephen Lovell (page does not exist)"), written in the [Go programming language](</Go_(Programming_Language)> "Go (Programming Language)"), first released in June 2016 <a id="cite-note-2" href="#cite-ref-2">[2]</a> under the [MIT license](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology").
GopherCheck supports a [parallel search](Parallel_Search "Parallel Search"), defaulting to one search goroutine, a type of [light-weight process](https://en.wikipedia.org/wiki/Light-weight_process) <a id="cite-note-3" href="#cite-ref-3">[3]</a>
per logical core. GopherCheck is [bitboard](Bitboards "Bitboards") based and determines [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") with [magic bitboards](Magic_Bitboards "Magic Bitboards") with plain, homogenous arrays, which performed better than the common [fancy implementations](Magic_Bitboards#Fancy "Magic Bitboards") whith individual table sizes, thus less memory but variable shift while calculating the index <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Contents

- [1 Features](#features)
  - [1.1 Board Representation](#board-representation)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc)
- [5 References](#references)

## Features

<a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Plain Magic Bitboards](Magic_Bitboards#Plain "Magic Bitboards")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search") (PVS)
- [Parallel Search](Parallel_Search "Parallel Search")
  - [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
  - [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
- [Selectivity](Selectivity "Selectivity")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") with [Verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")
  - [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Prune](Pruning "Pruning") [Quiet Moves](Quiet_Moves "Quiet Moves") if [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") \< 0
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Singular Extensions](Singular_Extensions "Singular Extensions")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Promotion Extensions](Promotions "Promotions")

## [Evaluation](Evaluation "Evaluation")

- [Material Balance](Material "Material")
- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
- [King Safety](King_Safety "King Safety")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Passed Pawns](Passed_Pawn "Passed Pawn")
  - [Backward Pawns](Backward_Pawn "Backward Pawn")
  - [Isolated Pawns](Isolated_Pawn "Isolated Pawn")
  - [Doubled Pawns](Doubled_Pawn "Doubled Pawn")
  - [Pawn Chain](Pawn_Chain "Pawn Chain")
  - [Pawn Duo](</Duo_Trio_Quart_(Bitboards)> "Duo Trio Quart (Bitboards)")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")

## See also

- [Gerbil](Gerbil "Gerbil")
- [Rodent](Rodent "Rodent")

## Forum Posts

- [GopherCheck 0.1.0 released](http://www.talkchess.com/forum/viewtopic.php?t=60378) by [Stephen Lovell](index.php?title=Stephen_Lovell&action=edit&redlink=1 "Stephen Lovell (page does not exist)"), [CCC](CCC "CCC"), June 06, 2016
- [Chess Engine - Gopher Check](http://www.talkchess.com/forum/viewtopic.php?t=53903) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), October 01, 2014
- [GopherCheck 0.2.0 released](http://www.talkchess.com/forum/viewtopic.php?t=62998) by [Stephen Lovell](index.php?title=Stephen_Lovell&action=edit&redlink=1 "Stephen Lovell (page does not exist)"), [CCC](CCC "CCC"), January 31, 2017

## External Links

## Chess Engine

- [GitHub - stephenjlovell/gopher_check: Concurrent UCI Chess Engine written in Go](https://github.com/stephenjlovell/gopher_check)
- [GopherCheck](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=GopherCheck&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/40](CCRL "CCRL")

## Misc

- [Gopher from Wikipedia](https://en.wikipedia.org/wiki/Gopher)
- [Gopher (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Gopher_(disambiguation)>)
- [Gopher (protocol) from Wikipedia](<https://en.wikipedia.org/wiki/Gopher_(protocol)>)
- [gopher - Wiktionary](https://en.wiktionary.org/wiki/gopher)
- [Alex Gopher](https://en.wikipedia.org/wiki/Alex_Gopher) - [The Child](https://www.discogs.com/de/Alex-Gopher-The-Child/master/89389) (1999), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

Contains vocal samples of [God Bless the Child](<https://en.wikipedia.org/wiki/God_Bless_the_Child_(Billie_Holiday_song)>) by [Billie Holiday](Category:Billie_Holiday "Category:Billie Holiday")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Pocket gopher, [Yellowstone National Park](https://en.wikipedia.org/wiki/Yellowstone_National_Park), [Gillian Bowser](https://source.colostate.edu/research-scientist-gillian-bowser-lauded-commitment-diversity-science/), 1990, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [GopherCheck 0.1.0 released](http://www.talkchess.com/forum/viewtopic.php?t=60378) by [Stephen Lovell](index.php?title=Stephen_Lovell&action=edit&redlink=1 "Stephen Lovell (page does not exist)"), [CCC](CCC "CCC"), June 06, 2016
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Effective Go - The Go Programming Language - Concurrency](https://golang.org/doc/effective_go.html#concurrency)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [gopher_check/bitboard_magic.go at master · stephenjlovell/gopher_check · GitHub](https://github.com/stephenjlovell/gopher_check/blob/master/bitboard_magic.go)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [gopher_check/readme.md at master · stephenjlovell/gopher_check · GitHub](https://github.com/stephenjlovell/gopher_check/blob/master/readme.md)

**[Up one Level](Engines "Engines")**

