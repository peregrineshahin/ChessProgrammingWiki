---
title: Chesley
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chesley**

\[.jpg) [Joe Biden](https://en.wikipedia.org/wiki/Joe_Biden) & [Chesley Sullenberger](https://en.wikipedia.org/wiki/Chesley_Sullenberger) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Chesley**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible [open source chess engine](Category:Open_Source "Category:Open Source") by [Matt Gingell](Matt_Gingell "Matt Gingell"), written in [C++](Cpp "Cpp"), licensed under the [GPL 2.0](Free_Software_Foundation#GPL "Free Software Foundation"),
targeting [Windows](Windows "Windows"), [Linux](Linux "Linux") and [Mac OS](Mac_OS "Mac OS"), first released to the public in May 2009 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
The chess engine takes its name from [Chesley B. “Sully” Sullenberger](https://en.wikipedia.org/wiki/Chesley_Sullenberger),
the pilot who [successfully landed an airplane](https://en.wikipedia.org/wiki/US_Airways_Flight_1549) on the [Hudson river](https://en.wikipedia.org/wiki/Hudson_River) around the time Matt was getting started <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Features

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
    - [Mate Killers](Mate_Killers "Mate Killers")
    - [Killer Moves](Killer_Move "Killer Move")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [History Heuristic](History_Heuristic "History Heuristic")
- [Selectivity](Selectivity "Selectivity")
  - [Extensions](Extensions "Extensions")
    - [Check Extensions](Check_Extensions "Check Extensions")
    - [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
    - [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
  - [Pruning](Pruning "Pruning")
    - [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
    - [Null Move Heuristic](Null_Move_Pruning "Null Move Pruning")
    - [Futility Pruning](Futility_Pruning "Futility Pruning")
    - [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
  - [Reductions](Reductions "Reductions")
    - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
    - [Razoring](Razoring "Razoring")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")

## [Evaluation](Evaluation "Evaluation")

- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
- [Evaluation of Pieces](Evaluation_of_Pieces "Evaluation of Pieces")
  - [Knight Outposts](Outposts "Outposts")
  - [Trapped Bishop](Trapped_Pieces "Trapped Pieces")
  - [Rook and Queen on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
  - [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Backward Pawns](</Backward_Pawns_(Bitboards)> "Backward Pawns (Bitboards)")
  - [Doubled Pawns](Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Passed Pawns](Passed_Pawn "Passed Pawn")
- [King](King "King")
  - [King-Square Tables](Piece-Square_Tables "Piece-Square Tables") for [Opening](Opening "Opening"), [Middlegame](Middlegame "Middlegame") and [Endgame](Endgame "Endgame")
  - [King Safety](King_Safety "King Safety")
    - [Castling Rights](Castling_Rights "Castling Rights")
    - [Pawn Shield](King_Safety#PawnShield "King Safety") in [Opening](Opening "Opening") and [Middlegame](Middlegame "Middlegame")

## Forum Posts

- [Chesley the Chess Engine!" released publicly](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=28195) by [Matt Gingell](Matt_Gingell "Matt Gingell"), [CCC](CCC "CCC"), May 31, 2009
- [Chesley r241 JA windows build available](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=29132) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), July 28, 2009
- [Re: undo move vs. Position Cloning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=29770&start=8) by [Matt Gingell](Matt_Gingell "Matt Gingell"), [CCC](CCC "CCC"), September 16, 2009 » [Copy-Make](Copy-Make "Copy-Make")
- [Chesley 1.1.2 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=29813) by [Matt Gingell](Matt_Gingell "Matt Gingell"), [CCC](CCC "CCC"), September 19, 2009
- [Chesley engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=36464) by Mark Loftus, [CCC](CCC "CCC"), October 23, 2010

## External Links

## Chess Engine

- [GitHub - matthewgingell/chesley: Chesley The Chess Engine!](https://github.com/matthewgingell/chesley)
- [Chesley the Chess Engine! download | SourceForge.net](https://sourceforge.net/projects/chesley/)
- [Index of /chess/engines/Jim Ablett/CHESLEY](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/CHESLEY/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Mac Chess Engines Repository](http://julien.marcel.free.fr/macchess/Chess_on_Mac/Engines.html) hosted by [Julien Marcel](Julien_Marcel "Julien Marcel")
- [Chesley](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Chesley&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [Chesley from Wikipedia](https://en.wikipedia.org/wiki/Chesley)
- [Chesley (name) from Wikipedia](<https://en.wikipedia.org/wiki/Chesley_(name)>)
- [Chesley Bonestell from Wikipedia](https://en.wikipedia.org/wiki/Chesley_Bonestell)
- [Chesley Awards from Wikipedia](https://en.wikipedia.org/wiki/Chesley_Awards)
- [Chesley B. “Sully” Sullenberger from Wikipedia](https://en.wikipedia.org/wiki/Chesley_Sullenberger)
- [12104 Chesley from Wikipedia](https://en.wikipedia.org/wiki/List_of_minor_planets:_12001%E2%80%9313000#104)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Former [Vice President](https://en.wikipedia.org/wiki/Vice_president) of the [United States](https://en.wikipedia.org/wiki/United_States) [Joe Biden](https://en.wikipedia.org/wiki/Joe_Biden) and [Chesley "Sully" Sullenberger](https://en.wikipedia.org/wiki/Chesley_Sullenberger) speaking with supporters at a community event at [Sun City MacDonald Ranch](https://scmronline.com/) in [Henderson, Nevada](https://en.wikipedia.org/wiki/Henderson,_Nevada), February 14, 2020, [Photo](<https://commons.wikimedia.org/wiki/File:Joe_Biden_%26_Chesley_Sullenberger_(49537249927).jpg>) by [Gage Skidmore](https://www.flickr.com/people/22007612@N05) from [Surprise, Arizona](https://en.wikipedia.org/wiki/Surprise,_Arizona), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Chesley the Chess Engine!" released publicly](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=28195) by [Matt Gingell](Matt_Gingell "Matt Gingell"), [CCC](CCC "CCC"), May 31, 2009
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [chesley/README.md at master · matthewgingell/chesley · GitHub](https://github.com/matthewgingell/chesley/blob/master/README.md)

**[Up one Level](Engines "Engines")**

