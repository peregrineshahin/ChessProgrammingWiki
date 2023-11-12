---
title: Check
---
**[Home](Home "Home") * [Chess](Chess "Chess") * Check**

[](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb9) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Lighthouse <a id="cite-note-1" href="#cite-ref-1">[1]</a>
Inside a [game of chess](Chess_Game "Chess Game"), a **check** occurs if a [king](King "King") is under immediate [attack](Attacks "Attacks") by one (or two) opponent [pieces](Pieces "Pieces"). If the king has no way to remove it from attack on the next move, the check is even [checkmate](Checkmate "Checkmate"). Since check is crucial concerning the outcome of game and the [horizon effect](Horizon_Effect "Horizon Effect"), [check extensions](Check_Extensions "Check Extensions") might be applied to evade the check.

## Kind of Checks

## Single Check

The king is attacked by one opponent piece, either by the piece which just moved directly attacking the king, or alternatively a [discovered check](Discovered_Check "Discovered Check") where a distant sliding piece attacks the king by opening the [ray](Rays "Rays") in opponent king [direction](Direction "Direction") with another piece.

## Double Check

A [double check](Double_Check "Double Check") occurs if the moving piece directly attacks the king but also discovers a distant sliding attacker.

## In Check Detection

Whether the side to move is in check is essential to know inside the [search](Search "Search") for various reasons. It might be [checkmate](Checkmate "Checkmate"), and most [pseudo-legal moves](Pseudo-Legal_Move "Pseudo-Legal Move") [generated](Move_Generation "Move Generation") may be illegal, leaving the king attacked. [Null move](Null_Move "Null Move") would yield in an illegal position as well, at or below the [horizon](Horizon_Node "Horizon Node") we don't want to [stand pat](Quiescence_Search#StandPat "Quiescence Search") if [material balance](Material "Material") or static [evaluation](Evaluation "Evaluation") is far greater than [beta](Beta "Beta").

## By last Move

The cheapest and most straightforward way to detect checks is to consider the previous move just made by the opponent. It might be a direct check or discovered check, so one has to test whether piece on [target square](Target_Square "Target Square") attacks the king, or whether piece on [origin square](Origin_Square "Origin Square") is attacked by an own sliding piece on an otherwise open [ray](Rays "Rays") in opponent king direction <a id="cite-note-2" href="#cite-ref-2">[2]</a>. If the last move was an [en passant](En_passant "En passant") capture, one has to consider a few more complicated cases of possible discovered checks, since the captured pawn is not on the target square, and two pawns disappear from the 4th (5th) rank.

## Attack Tables

Based on the design and data structure of a chess program, an [incremental updated](Incremental_Updates "Incremental Updates") [attack and defend map](Attack_and_Defend_Maps "Attack and Defend Maps") may immedeatly answer whether the king is under attack of one or even two opponent pieces.

## On the Fly

With [bitboards](Bitboards "Bitboards") one may determine a [square attacked](Square_Attacked_By#AnyAttackBySide "Square Attacked By") as mentioned in [checks and pinned pieces](</Checks_and_Pinned_Pieces_(Bitboards)> "Checks and Pinned Pieces (Bitboards)").

## Getting out of check

While in check, it is recommended to perform a specialized [Move Generation](Move_Generation "Move Generation") for check evasion of either a reasonable subset of all [pseudo-legal moves](Pseudo-Legal_Move "Pseudo-Legal Move") or even a strict [legal move](Legal_Move "Legal Move") generation:

## Double Check

- Only king moves to non attacked squares, sliding check x-rays the king

## Single Check

- Capture of checking piece. The capturing piece is not [absolutely pinned](Pin#AbsolutePin "Pin")
- King moves to non attacked squares, sliding check x-rays the king
- Interposing moves in case of distant sliding check. The moving piece is not absolutely pinned.

## Perpetual Check

A perpetual check occurs if one player forces an "endless" series of checks with repeated [reversible moves](Reversible_Moves "Reversible Moves"), finally resulting in a draw by [threefold repetitions](Repetitions "Repetitions").

## See also

- [Check Extensions](Check_Extensions "Check Extensions")
- [Checkmate](Checkmate "Checkmate")
- [Checks and Pinned Pieces (Bitboards)](</Checks_and_Pinned_Pieces_(Bitboards)> "Checks and Pinned Pieces (Bitboards)")
- [Checks](Quiescence_Search#Checks "Quiescence Search") in [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Desperado](Stalemate#Desperado "Stalemate")
- [DirGolem](DirGolem "DirGolem")
- [Horizon Effect](Horizon_Effect "Horizon Effect")
- [Stalemate](Stalemate "Stalemate")

## Publications

- [Richard L. Smith](index.php?title=Richard_L._Smith&action=edit&redlink=1 "Richard L. Smith (page does not exist)"), [Fernand Gobet](Fernand_Gobet "Fernand Gobet"), [Peter Lane](index.php?title=Peter_Lane&action=edit&redlink=1 "Peter Lane (page does not exist)") (**2009**). *[Checking chess checks with chunks: A model of simple check detection](http://bura.brunel.ac.uk/handle/2438/3503)*. [ICCM 2009](http://sideshow.psyc.bbk.ac.uk/rcooper/iccm2009/proceedings/) » [CHREST](CHREST "CHREST"), [Chunking](Chunking "Chunking")

## Forum Posts

## 1997 ...

- [quiescence search](https://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ca0300b50438a388) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 16, 1997 » [Quiescence Search](Quiescence_Search "Quiescence Search"), [Crafty](Crafty "Crafty")

## 2000 ...

- [Checks in the Qsearch](https://www.stmintz.com/ccc/index.php?id=237893) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), June 28, 2002 » [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Idea for check function](https://www.stmintz.com/ccc/index.php?id=265069) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), November 14, 2002
- [Fast check detection in bitboard engine](https://www.stmintz.com/ccc/index.php?id=334869) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang"), [CCC](CCC "CCC"), December 10, 2003
- [Rebel's long checks concept in QS](https://www.stmintz.com/ccc/index.php?id=344282) by [milix](Anastasios_Milikas "Anastasios Milikas"), [CCC](CCC "CCC"), January 23, 2004 » [Rebel](Rebel "Rebel"), [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Qsearch Checks](https://www.stmintz.com/ccc/index.php?id=385027) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), August 29, 2004 » [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Checks in QSearch](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=702&p=2642) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), November 23, 2004 » [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")

## 2005 ...

- [in check test](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3034) by Anonymous , [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 07, 2005
- [How to Best Limit Checks in the Quiescence ?](http://www.talkchess.com/forum/viewtopic.php?p=139285) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), August 20, 2007 » [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")
- [discovered check definition](http://www.talkchess.com/forum/viewtopic.php?t=16414) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), September 12, 2007 » [Discovered Check](Discovered_Check "Discovered Check")
- [checks in q-search](http://www.talkchess.com/forum/viewtopic.php?t=23447) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 02, 2008

## 2010 ...

- [Standpat and check](http://www.talkchess.com/forum/viewtopic.php?t=32424) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), February 06, 2010 » [Standing Pat](Quiescence_Search#StandPat "Quiescence Search")
- [Detecting Checks](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51343&sid=2384b91c58dc091e82cef3abd2a4f3f4) by beneficii, [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), November 27, 2010
- [out of check move ordering](http://www.talkchess.com/forum/viewtopic.php?t=38387) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), March 12, 2011 » [Move Ordering](Move_Ordering "Move Ordering")
- [checks in quies](http://www.talkchess.com/forum/viewtopic.php?t=42971) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), March 22, 2012 » [Quiescence Search](Quiescence_Search "Quiescence Search")
- [What is (in your opinion) the best check validation method?](http://www.open-chess.org/viewtopic.php?f=5&t=2599) by goodgame0111, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 24, 2014
- [Spite checks](http://www.talkchess.com/forum/viewtopic.php?t=52309) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 13, 2014

## 2015 ...

- [Check-extension in QS](http://www.talkchess.com/forum/viewtopic.php?t=55874) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 03, 2015 » [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")
- [Ostrich tactics and pointless checks](http://www.talkchess.com/forum/viewtopic.php?t=56517) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), May 29, 2015 » [Horizon Effect](Horizon_Effect "Horizon Effect")
- [Checks in qsearch - must-have or optional?](http://www.talkchess.com/forum/viewtopic.php?t=59529) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), March 15, 2016 » [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")
- [perpetual check position](http://www.talkchess.com/forum/viewtopic.php?t=61140) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), August 16, 2016
- [Spite checks, again](http://www.talkchess.com/forum/viewtopic.php?t=61803) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 23, 2016
- [check evasions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=65479) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), October 18, 2017

## 2020 ...

- [Efficiently Detect Whether a Move Gives Check](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79128) by ori yonay, [CCC](CCC "CCC"), January 16, 2022

## External Links

- [Check (chess) from Wikipedia](https://en.wikipedia.org/wiki/Check_%28chess%29)
- [Double check from Wikipedia](https://en.wikipedia.org/wiki/Double_check)
- [Perpetual check from Wikipedia](https://en.wikipedia.org/wiki/Perpetual_check) » [Repetitions](Repetitions "Repetitions")
- [Cross-check from Wikipedia](https://en.wikipedia.org/wiki/Cross-check)
- [Check (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Check)
- [Checkbox from Wikipedia](https://en.wikipedia.org/wiki/Checkbox) » [GUI](GUI "GUI")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb9), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Idea for check function](https://www.stmintz.com/ccc/index.php?id=265069) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), November 14, 2002

**[Up one Level](Chess "Chess")**

