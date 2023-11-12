---
title: BootChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * BootChess**

**BootChess**,

one of the smallests computer implementations of a none [FIDE](FIDE "FIDE") compliant chess variant written by [Olivier Poudade](Olivier_Poudade "Olivier Poudade") in [x86](X86 "X86") [Assembly](Assembly "Assembly"), released in January 2015.
Its size of 487 (468) <a id="cite-note-1" href="#cite-ref-1">[1]</a> bytes fits into a 512 byte [boot sector](https://en.wikipedia.org/wiki/Boot_sector) for [Windows](Windows "Windows"), [Linux](Linux "Linux"), [OS X](Mac_OS "Mac OS"), [DOS](MS-DOS "MS-DOS") and [BSD](Unix "Unix") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. [Castling](Castling "Castling"), [minor promotions](Promotions#MinorPromotion "Promotions") and [en passant](En_passant "En passant") are not implemented.
BootChess otherwise performs a so called "TaxiMax" heuristic, maximizing [captures](Captures "Captures") and trying to minimize the [Manhattan distance](Manhattan-Distance "Manhattan-Distance") to the opponent's king rank.
This kind of half-ply search cannot prevent moving it's own [king](King "King") in [check](Check "Check"), opposed to the old [1K ZX Chess](1K_ZX_Chess "1K ZX Chess") by [David Horne](David_Horne "David Horne") and the recent [Toledo Atomchess](Toledo "Toledo") by [Óscar Toledo Gutiérrez](%C3%93scar_Toledo_Guti%C3%A9rrez "Óscar Toledo Gutiérrez"),
who took the BootChess challenge with 481 bytes and a 3-ply search <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## See also

- [1K ZX Chess](1K_ZX_Chess "1K ZX Chess")
- [ChessLin](ChessLin "ChessLin")
- [Toledo Atomchess](Toledo "Toledo")

## Forum Posts

- [BootChess (minimal chess engine)](http://www.talkchess.com/forum/viewtopic.php?t=55125) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), January 28, 2015

## [Smallest engine in the world...](http://www.talkchess.com/forum/viewtopic.php?t=55149) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), January 29, 2015 External Links

- [BootChess by Red Sector Inc. :: pouët.net](http://www.pouet.net/prod.php?which=64962)
- [BootChess Listing](http://olivier.poudade.free.fr/src/BootChess.asm)
- [Coder creates smallest chess game for computer](https://www.bbc.com/news/technology-31028787) by [Leo Kelion](http://journalisted.com/leo-kelion), [BBC News](https://en.wikipedia.org/wiki/BBC_News), January 28, 2015
- [Hyper Minimal Graphics Create The Smallest Chess Game In History](https://www.fastcompany.com/3041601/hyper-minimal-graphics-create-the-smallest-chess-game-in-history) by [Mark Wilson](http://www.fastcodesign.com/user/mark-wilson), [Co.Design | business + design](http://www.fastcodesign.com/), January 29, 2015
- [ZX81 BEATEN at last as dev claims smallest Chess code crown](https://www.theregister.co.uk/2015/01/29/zx81_record_falls_as_dev_claims_smallest_chess_code_crown/) by [Simon Sharwood](http://www.theregister.co.uk/Author/2488), [The Register](https://en.wikipedia.org/wiki/The_Register), January 29, 2015
- [Does size matter? It does if you’re French, and a chess-loving hacker!](https://nakedsecurity.sophos.com/2015/01/30/does-size-matter-it-does-if-youre-french/?utm_source=Naked%2520Security%2520-%2520Feed&utm_medium=feed&utm_content=rss2&utm_campaign=Feed) by [Paul Ducklin](https://nakedsecurity.sophos.com/author/pducklin/), [Naked Security](https://en.wikipedia.org/wiki/Sophos), January 30, 2015
- [The world's smallest chess engines](https://en.chessbase.com/post/the-world-s-smallest-chess-engines) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), September 23, 2015 » [1K ZX Chess](1K_ZX_Chess "1K ZX Chess"), BootChess, [Toledo Nanochess](Toledo "Toledo"), [Micro-Max](Micro-Max "Micro-Max")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> 468 bytes without rank/file indicators of the board display
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [BootChess by Red Sector Inc. :: pouët.net](http://www.pouet.net/prod.php?which=64962)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: BootChess (minimal chess engine)](http://www.talkchess.com/forum/viewtopic.php?t=55125&start=9) by [Óscar Toledo Gutiérrez](%C3%93scar_Toledo_Guti%C3%A9rrez "Óscar Toledo Gutiérrez"), [CCC](CCC "CCC"), January 31, 2015

**[Up one Level](Engines "Engines")**

