---
title: Draw
---
**[Home](Home "Home") * [Chess](Chess "Chess") * Draw**

[](http://www.elke-rehder.de/Chess_Woodcuts.htm) [Elke Rehder](Category:Elke_Rehder "Category:Elke Rehder") - Remis (1990) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Draw**,

the outcome of a [chess game](Chess_Game "Chess Game") when it appears that neither side will win. Draws are codified by various rules of chess including [stalemate](Stalemate "Stalemate"), threefold [repetition](Repetitions "Repetitions"), and the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule"). A draw also occurs when neither player has [sufficient material](Material#InsufficientMaterial "Material") to [checkmate](Checkmate "Checkmate") the opponent or when no sequence of legal moves can lead to checkmate.

Players may further [agree to a draw](https://en.wikipedia.org/wiki/Draw_by_agreement), the side to move may not only claim, but offer a draw, the other side may accept or decline - in computer chess, conform to a protocol and considering [game stage](Game_Phases "Game Phases"), late [endgame](Endgame "Endgame") [material](Material "Material") configuration, [score](Score "Score") history and forecast. In official over the board [computer chess tournaments](Tournaments_and_Matches "Tournaments and Matches") such as the [World Computer Chess Championship](World_Computer_Chess_Championship "World Computer Chess Championship"), operator draw agreements require confirmation by the tournament director or arbiter.

## Recognizing Draws

The primary purpose to recognize draws is to direct the chess program to produce drawing moves if alternatives are likely losing, or to avoid draws if ahead and alternative moves most likely win as reflected by the [score](Score "Score") of the [minimax search](Minimax "Minimax").

## Draw Score

Usually, assuming symmetric [evaluation](Evaluation "Evaluation") and [negamaxed](Negamax "Negamax") values, positive scores indicate the [side to move](Side_to_move "Side to move") is ahead, and negative if behind, which defines the value of zero as a natural [draw score](Score#DrawScore "Score"). However, a score of zero does not necessarily reflect a draw score, but a score of a equal or balanced position. Same is true, if programs apply a [contempt factor](Contempt_Factor "Contempt Factor") considering the relative strength of the opponent.

## Cray Blitz

[Cray Blitz](Cray_Blitz "Cray Blitz") applied a special draw heuristic, not uniformly using zero as draw score, but rather zero plus the [ply](Ply "Ply") distance to the [root](Root "Root") to prefer later draws rather than a draw now. Additionally, the draw score range is disjoint from [evaluation](Evaluation "Evaluation") scores, which then exclude values around zero by adding or subtracting appropriate offsets if either greater or equal, or less than zero <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Draw Topics

- [Blockage Detection](Blockage_Detection "Blockage Detection")
- [Contempt Factor](Contempt_Factor "Contempt Factor")
- [Corresponding Squares](Corresponding_Squares "Corresponding Squares")
- [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
- [Draw Score](Score#DrawScore "Score")
- [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
- [Insufficient Material](Material#InsufficientMaterial "Material")
- [Perpetual Check](Check#Perpetual "Check")
- [Repetitions](Repetitions "Repetitions")
- [Stalemate](Stalemate "Stalemate")
- [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn")

## See also

- [Checkmate](Checkmate "Checkmate")
- [Chess Game](Chess_Game "Chess Game")
- [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [Graph History Interaction](Graph_History_Interaction "Graph History Interaction") (GHI)
- [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
- [KPK](KPK "KPK")
- [Match Statistics](Match_Statistics "Match Statistics")
- [Path-Dependency](Path-Dependency "Path-Dependency")
- [Pursuit](index.php?title=Pursuit&action=edit&redlink=1 "Pursuit (page does not exist)")
- [Rules of Chess](Rules_of_Chess "Rules of Chess")
- [Score](Score "Score")
- [Transposition](Transposition "Transposition")
- [Transposition Table](Transposition_Table "Transposition Table")

## Publications

- [David Slate](David_Slate "David Slate") (**1984**). *Interior-node Score Bounds in a Brute-force Chess Program.* [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal")
- [Harry Nelson](Harry_Nelson "Harry Nelson"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1988**). *The Draw Heuristic of Cray Blitz*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1998**) *[Efficient Interior-Node Recognition](http://people.csail.mit.edu/heinz/dt/node33.html)*. [ICCA Journal, Vol. 21, No. 3](ICGA_Journal#21_3 "ICGA Journal")
- [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković"), [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović") (**2004**). *A New Approach to Draw Detection by Move Repetition in Computer Chess Programming.* [arXiv:cs/0406038](https://arxiv.org/abs/cs/0406038) <a id="cite-note-3" href="#cite-ref-3">[3]</a>
- [Guy Haworth](Guy_Haworth "Guy Haworth") (**2021**). *Chess without draws*. [ICGA Journal, Vol. 43, No. 2](ICGA_Journal#43_2 "ICGA Journal")

## Forum Posts

## 1995 ...

- [50 move rule question](https://www.stmintz.com/ccc/index.php?id=49261) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), April 20, 1999

## 2000 ...

- [Shortest Stalemate by Samuel Loyd](https://www.stmintz.com/ccc/index.php?id=156762) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), March 02, 2001
- ["Don't trust draw score" \<=Is it true?](https://www.stmintz.com/ccc/index.php?id=182927) by [Teerapong Tovirat](Teerapong_Tovirat "Teerapong Tovirat"), [CCC](CCC "CCC"), August 08, 2001
- [A new(?) technique to recognize draws](https://www.stmintz.com/ccc/index.php?id=233270) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), June 01, 2002 » [Perpetual Check](Check#Perpetual "Check"), [Corresponding Squares](Corresponding_Squares "Corresponding Squares")

## 2005 ...

- [Quark 2.35 draw claim bug](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2112) by [Igor Korshunov](Igor_Korshunov "Igor Korshunov"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 28, 2005 » [Quark](Quark "Quark")
- [Draw scores](http://www.talkchess.com/forum/viewtopic.php?t=16942) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), October 05, 2007 » [Draw Score](Score#DrawScore "Score")
- [When and how to return a draw evaluation?](http://www.talkchess.com/forum/viewtopic.php?t=23257) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), August 26, 2008 » [Repetitions](Repetitions "Repetitions")

## 2010 ...

- [Re: question on draw evaluation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=354023&t=34673) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), June 07, 2010
- [Wrong draw claim by Naum 4.2 ?](http://www.talkchess.com/forum/viewtopic.php?t=37592) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), January 12, 2011 » [Naum](Naum "Naum"), [Insufficient Material](Material#InsufficientMaterial "Material")
- [Playing better moves in drawish positions (anti-0.00)](http://www.talkchess.com/forum/viewtopic.php?t=38410) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Onno](Onno "Onno")
- [final drawscore testing results](http://www.talkchess.com/forum/viewtopic.php?t=40386) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September, 13, 2011
- [Repetitions/50 moves and TT](http://www.talkchess.com/forum/viewtopic.php?t=40388) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 13, 2011 » [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
- [Texel recipe to fix TT draws scores](http://www.talkchess.com/forum/viewtopic.php?t=44167) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), June 23, 2012 » [Texel](Texel "Texel")
- [Draw value](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=44702) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), August 06, 2012
- [Draw aversion](http://www.open-chess.org/viewtopic.php?f=5&t=2172) by [Don Dailey](Don_Dailey "Don Dailey"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 16, 2012
- [Value draw](http://www.talkchess.com/forum/viewtopic.php?t=50321) by [Marek Kwiatkowski](index.php?title=Marek_Kwiatkowski&action=edit&redlink=1 "Marek Kwiatkowski (page does not exist)"), [CCC](CCC "CCC"), December 04, 2013

## 2015 ...

- [Final Report on Draw Problem in Correspondence Chess](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?pid=552902) by [Ciron](Arno_Nickel "Arno Nickel"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 26, 2015 <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [The future of chess and elo ratings](http://www.talkchess.com/forum/viewtopic.php?t=57696) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), September 20, 2015 » [Match Statistics](Match_Statistics "Match Statistics"), [Opening Book](Opening_Book "Opening Book")
- [Test positions for draw detection](http://www.talkchess.com/forum/viewtopic.php?t=57772) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), September 27, 2015 » [Test-Positions](Test_Positions "Test-Positions")
- [Syzygy and draw by repetition](http://www.talkchess.com/forum/viewtopic.php?t=60906) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 22, 2016  » [Repetitions](Repetitions "Repetitions"), [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
- [Some thoughts about draws](http://www.talkchess.com/forum/viewtopic.php?t=61023) by [Pio Korinth](index.php?title=Pio_Korinth&action=edit&redlink=1 "Pio Korinth (page does not exist)"), [CCC](CCC "CCC"), August 03, 2016
- [The new chess rules (5-fold repetition and 75-move draw)](https://groups.google.com/d/msg/fishcooking/M2bkzC3MuFQ/N3pHK4DcAgAJ) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 29, 2016 » [Stockfish](Stockfish "Stockfish"), [Repetitions](Repetitions "Repetitions")
- [Have engines updated for fide 2014 draw rules?](http://www.talkchess.com/forum/viewtopic.php?t=62956) by [Norm Pollock](index.php?title=Norm_Pollock&action=edit&redlink=1 "Norm Pollock (page does not exist)"), [CCC](CCC "CCC"), January 28, 2017
- [Managing draws in the tree search](http://www.talkchess.com/forum/viewtopic.php?t=63562) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), March 26, 2017
- [Reporting a draw in UCI](http://www.talkchess.com/forum/viewtopic.php?t=63906) by Vince Sempronio, [CCC](CCC "CCC"), May 05, 2017 » [UCI](UCI "UCI")
- [Ways to avoid "Draw Death" in Computer Chess](http://www.talkchess.com/forum/viewtopic.php?t=64719) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 25, 2017 » [Match Statistics](Match_Statistics "Match Statistics"), [Playing Strength](Playing_Strength "Playing Strength")
- [Draw rate](https://groups.google.com/d/msg/fishcooking/WgN3KD0ThA4/iIk2j0RhBAAJ) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), March 07, 2018 » [Stockfish](Stockfish "Stockfish")
- [Draw scores in TT](http://www.talkchess.com/forum/viewtopic.php?t=67102) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), April 14, 2018 » [Draw Score](Score#DrawScore "Score"), [Transposition Table](Transposition_Table "Transposition Table")
- [Rebel Book Draw?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68558) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), October 03, 2018 » [Opening Book](Opening_Book "Opening Book")
- [Are draws hard to predict?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69069) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), November 27, 2018 » [Neural Networks](Neural_Networks "Neural Networks")
- [Why does stockfish randomise draw evaluations?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71707) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), September 01, 2019 » [Stockfish](Stockfish "Stockfish"), [Draw Evaluation](Draw_Evaluation "Draw Evaluation"), [Draw Score](Score#DrawScore "Score"), [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")

## 2020 ...

- [what is the rating of engines when you do not count draws?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77544) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), June 23, 2021 » [Match Statistics](Match_Statistics "Match Statistics"), [Playing Strength](Playing_Strength "Playing Strength")

## External Links

- [Fide Handbook - E.I.01A. Laws of Chess](http://www.fide.com/component/handbook/?id=124&view=article) - Article 9: The drawn game
- [Draw (chess) from Wikipedia](https://en.wikipedia.org/wiki/Draw_%28chess%29)
- [Draw by agreement from Wikipedia](https://en.wikipedia.org/wiki/Draw_by_agreement)

[Grandmaster draw from Wikipedia](https://en.wikipedia.org/wiki/Draw_by_agreement#Grandmaster_draw)

- [D (Dead Draw, Draw, Drawing line, Drawish, Draw odds, Drawing weapon) - Glossary of chess from Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_chess#D)
- [Book draw - Glossary of chess from Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_chess#Book_draw)
- [Draw (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Draw)
- [draw - Wiktionary](https://en.wiktionary.org/wiki/draw)
- [Tie (draw) from Wikipedia](https://en.wikipedia.org/wiki/Tie_%28draw%29)
- [How many points should you get for a draw?](https://en.chessbase.com/post/how-many-points-should-you-get-for-a-draw) by [Arno Nickel](Arno_Nickel "Arno Nickel"), [ChessBase News](ChessBase "ChessBase"), August 20, 2015 <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Elke Rehder](Category:Elke_Rehder "Category:Elke Rehder") - Remis (1990) (two kings in a draw), [Holzschnitte zum Schach](http://www.elke-rehder.de/Chess_Woodcuts.htm)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Harry Nelson](Harry_Nelson "Harry Nelson"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1988**). *The Draw Heuristic of Cray Blitz*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Draw Detection by Move Repetition Procedure -- Comments](https://www.stmintz.com/ccc/index.php?id=380201) by [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [CCC](CCC "CCC"), August 01, 2004
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [How many points should you get for a draw?](http://en.chessbase.com/post/how-many-points-should-you-get-for-a-draw) by [Arno Nickel](Arno_Nickel "Arno Nickel"), [ChessBase News](ChessBase "ChessBase"), August 20, 2015
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Final Report on Draw Problem in Correspondence Chess](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?pid=552902) by [Ciron](Arno_Nickel "Arno Nickel"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 26, 2015

**[Up one Level](Chess "Chess")**

