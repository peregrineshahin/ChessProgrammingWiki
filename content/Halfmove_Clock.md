---
title: Halfmove Clock
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Position](Chess_Position "Chess Position") * Halfmove Clock**

The **Halfmove Clock** inside an chess position object takes care of enforcing the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule"). This counter is **reset** after [captures](Captures "Captures") or [pawn moves](Pawn_Push "Pawn Push"), and incremented otherwise. Also moves which lose the [castling rights](Castling_Rights "Castling Rights"), that is [rook](Rook "Rook")- and [king](King "King") moves from their initial [squares](Squares "Squares"), including [castling](Castling "Castling") itself, **increment** the Halfmove Clock. However, those moves are [irreversible](Irreversible_Moves "Irreversible Moves") in the sense to reverse the same rights - since once a castling right is lost, it is lost forever, as considered in detecting [repetitions](Repetitions "Repetitions").

## See also

- [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
- [Halfmove Clock](Forsyth-Edwards_Notation#HalfmoveClock "Forsyth-Edwards Notation") in the [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
- [Ply](Ply "Ply")
- [Repetitions](Repetitions "Repetitions")

## Forum Posts

- [Half Move Clock Confusion](http://www.open-chess.org/viewtopic.php?f=3&t=2209) by HumbleProgrammer, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 10, 2013 » [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule"), [Repetitions](Repetitions "Repetitions")
- [Fifty move counter and Null move](http://www.talkchess.com/forum/viewtopic.php?t=64853) by Tamás Kuzmics, [CCC](CCC "CCC"), August 09, 2017 » [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule"), [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")

## External Links

- [plycount - Wiktionary](http://en.wiktionary.org/wiki/plycount)
- [Counter from Wikipedia](https://en.wikipedia.org/wiki/Counter)
- [Clock (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Clock_%28disambiguation%29)
- [Clock from Wikipedia](https://en.wikipedia.org/wiki/Clock)
- [Game clock from Wikipedia](https://en.wikipedia.org/wiki/Game_clock)

**[Up one Level](Chess_Position "Chess Position")**

