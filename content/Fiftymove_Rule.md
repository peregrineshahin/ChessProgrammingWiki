---
title: Fiftymove Rule
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Draw](Draw "Draw") * Fifty-move Rule**

The **Fifty-move rule** states that a [game of chess](Chess_Game "Chess Game") is considered [drawn](Draw "Draw") after **fifty** consecutive [full moves](Moves "Moves") without a [capture](Captures "Captures") or a [pawn move](Pawn_Push "Pawn Push"). If the last move of such series delivers a [checkmate](Checkmate "Checkmate"), this takes precedence over the 50 move rule. Inside a chess program, the [halfmove clock](Halfmove_Clock "Halfmove Clock") takes care of enforcing fifty-move rule. If the halfmove clock becomes greater or equal than 100, and the [side to move](Side_to_move "Side to move") has at least one [legal move](Legal_Move "Legal Move"), a [draw score](Score#DrawScore "Score") should be assigned to that [node](Node "Node"), with appropriate [protocol](Protocols "Protocols") handling and [game state](Chess_Game#endofgame "Chess Game") transitions, if the node is already the [root](Root "Root") and there is no mate in one.

## Contents

- [1 Fide Rule](#fide-rule)
  - [1.1 Since July 01, 2014](#since-july-01.2c-2014)
  - [1.2 Temporary Exceptions](#temporary-exceptions)
- [2 See also](#see-also)
- [3 Publications](#publications)
- [4 Forum Posts](#forum-posts)
  - [4.1 1998 ...](#1998-...)
  - [4.2 2000 ...](#2000-...)
  - [4.3 2010 ...](#2010-...)
  - [4.4 2015 ...](#2015-...)
  - [4.5 2020 ...](#2020-...)
- [5 External Links](#external-links)
- [6 References](#references)

## Fide Rule

```
9.3 The game is drawn, upon a correct claim by the player having the move, if <a id="cite-note-1" href="#cite-ref-1">[1]</a>

a) he writes his move on his [scoresheet](Game_Notation "Game Notation"), and declares to the arbiter his intention to make this move which shall result in the last 50 moves having been made by each player without the movement of any pawn and without any capture, or

b) the last 50 consecutive moves have been made by each player without the movement of any pawn and without any capture. 

```

## Since July 01, 2014

Since July 01, 2014 75 moves without capture and pawn move end the game even without a claim <a id="cite-note-2" href="#cite-ref-2">[2]</a>

```
9.6  If one or both of the following occur(s) then the game is drawn: 

a) the same position has appeared, as in  [9.2b](Repetitions#92b "Repetitions"), for at least five consecutive alternate moves by each player.  

b) any consecutive series of 75 moves have been completed by each player without the movement of any pawn and without any capture. If the last move resulted in checkmate, that shall take precedence. 

```

## Temporary Exceptions

At the beginning of the nineties, when it has been proven that some [endgames](Endgame "Endgame") can be won only in a larger number of moves, there has been an attempt to complicate the rule with a series of exceptions, all of which has been scraped later on.

## See also

- [Draw](Draw "Draw")
- [Endgame Tablebases | DTZ50 - Depth to Zeroing in the context of the Fifty-move Rule](Endgame_Tablebases#DTZ50 "Endgame Tablebases")
- [Graph History Interaction](Graph_History_Interaction "Graph History Interaction") (GHI)
- [Halfmove Clock](Halfmove_Clock "Halfmove Clock")
- [Path-Dependency](Path-Dependency "Path-Dependency")
- [Repetitions](Repetitions "Repetitions")
- [Transposition](Transposition "Transposition")
- [Transposition Table](Transposition_Table "Transposition Table")

## Publications

- [John Roycroft](John_Roycroft "John Roycroft") (**1984**). *A Proposed Revision of the ‘50-Move Rule’*. [ICCA Journal, Vol. 7, No. 3](ICGA_Journal#7_3 "ICGA Journal")
- [Bob Herschberg](Bob_Herschberg "Bob Herschberg"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1993**). *Back to fifty*. [ICCA Journal, Vol. 16, No. 1](ICGA_Journal#16_1 "ICGA Journal")
- [Galen Huntington](index.php?title=Galen_Huntington&action=edit&redlink=1 "Galen Huntington (page does not exist)"), [Guy Haworth](Guy_Haworth "Guy Haworth") (**2015**). *Depth to Mate and the 50-Move Rule*. [ICGA Journal, Vol. 38, No. 2](ICGA_Journal#38_2 "ICGA Journal") » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases") <a id="cite-note-3" href="#cite-ref-3">[3]</a>

## Forum Posts

## 1998 ...

- [Horrible move!](https://www.stmintz.com/ccc/index.php?id=18139) by [Tony Hedlund](Tony_Hedlund "Tony Hedlund"), [CCC](CCC "CCC"), May 07, 1998 » [HIARCS](HIARCS "HIARCS")
- [50 move rule question](https://www.stmintz.com/ccc/index.php?id=49261) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), April 20, 1999

## 2000 ...

- [Question about 50 move rule and e.p./castle flags](https://www.stmintz.com/ccc/index.php?id=280707) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), January 31, 2003

## 2010 ...

- [Repetitions/50 moves and TT](http://www.talkchess.com/forum/viewtopic.php?t=40388) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 13, 2011
- [Texel recipe to fix TT draws scores](http://www.talkchess.com/forum/viewtopic.php?t=44167) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), June 23, 2012 » [Texel](Texel "Texel")
- [Draw by 50 move rule or mate](http://www.talkchess.com/forum/viewtopic.php?t=45556) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), October 13, 2012
- [Half Move Clock Confusion](http://www.open-chess.org/viewtopic.php?f=3&t=2209) by HumbleProgrammer, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 10, 2013 » [Halfmove Clock](Halfmove_Clock "Halfmove Clock"), [Repetitions](Repetitions "Repetitions")
- [FIDE's new rules for chess](http://www.talkchess.com/forum/viewtopic.php?t=53030) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), July 20, 2014

## 2015 ...

- [The 75 move rule](http://www.talkchess.com/forum/viewtopic.php?t=55633) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 11, 2015
- [Hashtable and 50 move rule draws](http://www.talkchess.com/forum/viewtopic.php?t=60264) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), May 24, 2016 » [Transposition Table](Transposition_Table "Transposition Table")
- [The new chess rules (5-fold repetition and 75-move draw)](https://groups.google.com/d/msg/fishcooking/M2bkzC3MuFQ/N3pHK4DcAgAJ) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 29, 2016 » [Stockfish](Stockfish "Stockfish"), [Repetitions](Repetitions "Repetitions")
- [Have engines updated for fide 2014 draw rules?](http://www.talkchess.com/forum/viewtopic.php?t=62956) by [Norm Pollock](index.php?title=Norm_Pollock&action=edit&redlink=1 "Norm Pollock (page does not exist)"), [CCC](CCC "CCC"), January 28, 2017
- [Losing by draw](http://www.open-chess.org/viewtopic.php?f=5&t=3093) by Hamfer, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 17, 2017
- [Fifty move counter and Null move](http://www.talkchess.com/forum/viewtopic.php?t=64853) by Tamás Kuzmics, [CCC](CCC "CCC"), August 09, 2017 » [Halfmove Clock](Halfmove_Clock "Halfmove Clock"), [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
- [75 moves FIDE-rule in section 9.6b](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66023) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), December 16, 2017
- [changing the 50 move rule to 5 move rule](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69750) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 28, 2019
- [50 move counter in FEN and GUIs](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72308) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 12, 2019
- [Graph History Interaction 2 questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72578) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), December 15, 2019 » [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")

## 2020 ...

- [Turning off 50-move draw rule in Stockfish & other engines](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73374) by jp, [CCC](CCC "CCC"), March 15, 2020

## External Links

- [Fifty-move rule from Wikipedia](https://en.wikipedia.org/wiki/Fifty-move_rule)
- [Fide Handbook - E.I.01A. Laws of Chess](http://www.fide.com/component/handbook/?id=124&view=article)
- [Endgame tablebases with the fifty-move rule](http://galen.metapath.org/egtb50/) by [Galen Huntington](index.php?title=Galen_Huntington&action=edit&redlink=1 "Galen Huntington (page does not exist)")
- [Computerschach - Eine Wette, die ich gerne verloren habe](http://www.horst-wandersleben.de/Wette.htm) by [Horst Wandersleben](index.php?title=Horst_Wandersleben&action=edit&redlink=1 "Horst Wandersleben (page does not exist)") (German) <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Fide Handbook - E.I.01A. Laws of Chess](http://www.fide.com/component/handbook/?id=124&view=article)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [FIDE's new rules for chess](http://www.talkchess.com/forum/viewtopic.php?t=53030) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), July 20, 2014
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Endgame tablebases with the fifty-move rule](http://galen.metapath.org/egtb50/) by [Galen Huntington](index.php?title=Galen_Huntington&action=edit&redlink=1 "Galen Huntington (page does not exist)")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner") found a game finished in a fifty-move rule draw, where [castling](Castling "Castling") occurred during the last fifty moves

**[Up one Level](Draw "Draw")**

