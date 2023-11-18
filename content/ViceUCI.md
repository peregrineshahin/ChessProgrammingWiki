---
title: ViceUCI
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Vice**



[ Tree of Vices <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Vice**, (Video Instructional Chess Engine)  

a didactic [open source chess engine](Category:Open_Source "Category:Open Source") by [BlueFeverSoft](BlueFeverSoft "BlueFeverSoft"), written in [C](C "C"), and introduced in a series of 87 + 8 [YouTube](https://en.wikipedia.org/wiki/YouTube) videos from May 2013 until January 2014 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.


Vice [represents the board](Board_Representation "Board Representation") with a [120 square array](10x12_Board "10x12 Board") and additionally has some [bitboards](Bitboards "Bitboards") for [pawn](Pawn "Pawn") stuff. It applies an [alpha-beta](Alpha-Beta "Alpha-Beta") search with [transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning") and [quiescence](Quiescence_Search "Quiescence Search") inside an [iterative deepening framework](Iterative_Deepening "Iterative Deepening"). It is compatible with the [UCI](UCI "UCI") and the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), and since version 1.1, supports the [PolyGlot](PolyGlot "PolyGlot") [opening book](Opening_Book "Opening Book") format <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## External Links


### Chess Engine


* [Vice ReadMe File and Download](http://bluefever.net/Downloads/ViceReadMe.html)
* [Vice 1.0 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Vice%201.0%2064-bit) in [CCRL Blitz](CCRL "CCRL") <a id="cite-note-4" href="#cite-ref-4">[4]</a>


### Videos


* [Programming A Chess Engine in C](https://www.youtube.com/watch?v=bGAfaepBco4&feature=share&list=PLZ1QII7yudbc-Ky058TEaOstZHVbT-2hg), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos by [BlueFeverSoft](BlueFeverSoft "BlueFeverSoft")


1. [Resources and Community](https://www.youtube.com/watch?v=bGAfaepBco4)
2. [Board Representation](https://www.youtube.com/watch?v=VuJL4qhpp-8) » [Board Representation](Board_Representation "Board Representation")
3. [First Definitions](https://www.youtube.com/watch?v=x9sPmLt-EBM)
4. [Board Structure](https://www.youtube.com/watch?v=3uBCUF_qHcg)
5. [Undo-Move Structure](https://www.youtube.com/watch?v=1q0NlSdGOjI) » [Unmake Move](Unmake_Move "Unmake Move")
6. [Array[120] to Array[64] Indexing for Pawns](https://www.youtube.com/watch?v=pqYFUnUn0qw) » [10x12 Board](10x12_Board "10x12 Board"), [8x8 Board](8x8_Board "8x8 Board")
7. [Piece Lists and ASSERT!](https://www.youtube.com/watch?v=Bi61lMwhksw) » [Piece-Lists](Piece-Lists "Piece-Lists")
8. [Bitboards](https://www.youtube.com/watch?v=JsjSChsu2L0) » [Bitboards](Bitboards "Bitboards")
9. [Bitboards Pop and Count](https://www.youtube.com/watch?v=ITVB7JSaI3w) » [BitScan](BitScan "BitScan"), [Population Count](Population_Count "Population Count")
10. [Set and Clear bits](https://www.youtube.com/watch?v=pa0W1mz_wa4) » [General Setwise Operations](General_Setwise_Operations "General Setwise Operations")
11. [Position Key (Hashkey) #1](https://www.youtube.com/watch?v=uw9jsInf4jA) » [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
12. [Position Key (Hashkey) #2](https://www.youtube.com/watch?v=WqVwQBXLwE0)
13. [Position Setup - Reset Board](https://www.youtube.com/watch?v=vF_Td1nABYw)
14. [Position Setup - FEN Notation](https://www.youtube.com/watch?v=4vCiIf73FQM)  » [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
15. [Parsing An FEN (1)](https://www.youtube.com/watch?v=usUJFkGyqM4)
16. [Parsing An FEN (2)](https://www.youtube.com/watch?v=GmCxU4elNcA)
17. [Printing the board to screen](https://www.youtube.com/watch?v=-wrSMzYGlGs)
18. [Piece Lists](https://www.youtube.com/watch?v=clLaVOnvUvA) » [Piece-Lists](Piece-Lists "Piece-Lists")
19. [Rank and File Arrays](https://www.youtube.com/watch?v=CRaIcMGbkpE)
20. [Checkboard](https://www.youtube.com/watch?v=O5YtKzh4siE)
21. [Next steps](https://www.youtube.com/watch?v=PGPdT9zz-xg)
22. [Square Attacked (1)](https://www.youtube.com/watch?v=8mHFATWbeik)
23. [Square Attacked (2)](https://www.youtube.com/watch?v=VdH0ObqK3CA)
24. [Move Format & Bits (1)](https://www.youtube.com/watch?v=KQcArvyrbIo) » [Encoding Moves](Encoding_Moves "Encoding Moves")
25. [Move Format & Bits (2)](https://www.youtube.com/watch?v=N6yImiyzWpo)
26. [Move Format & Bits (3)](https://www.youtube.com/watch?v=n2ZgdkW7uls)
27. [Printmove and Printsquare](https://www.youtube.com/watch?v=siLoAPTOaWE)
28. [Move Generation #1](https://www.youtube.com/watch?v=uBwwC5uWJKo) » [Move Generation](Move_Generation "Move Generation")
29. [Move Generation #2 - Validations](https://www.youtube.com/watch?v=wD9CNtvLCrI)
30. [Move Generation #3 - White Pawns](https://www.youtube.com/watch?v=1TCKuEoHvcs)
31. [Move Generation #4 - Black Pawns](https://www.youtube.com/watch?v=8LUkqaodUFA)
32. [Move Generation #5 - Piece Index Setup](https://www.youtube.com/watch?v=MFMk5SiXvHQ)
33. [Move Generation #6 - Non Slider Pieces](https://www.youtube.com/watch?v=6WovWHeRKFA)
34. [Move Generation #7 - Slider Pieces](https://www.youtube.com/watch?v=dkHlnSP3u3w)
35. [Move Generation #8 - Castling](https://www.youtube.com/watch?v=srAcgIKONO4) » [Castling](Castling "Castling")
36. [Move Generation #9 - Final Movelist!](https://www.youtube.com/watch?v=kVXi615rFxE) » [Move List](Move_List "Move List")
37. [Writing MakeMove - Introduction](https://www.youtube.com/watch?v=ZWcjcn4KVTk) » [Make Move](Make_Move "Make Move")
38. [Writing MakeMove #1](https://www.youtube.com/watch?v=9Rfx1WHkJ3o)
39. [Writing MakeMove #2 - ClearPiece()](https://www.youtube.com/watch?v=F_L2AhqB4V4)
40. [Writing MakeMove #3 - Add/MovePiece()](https://www.youtube.com/watch?v=ai_193NC3zU)
41. [Writing MakeMove #4 - MakeMove()](https://www.youtube.com/watch?v=qnHQJAsJFvk)
42. [Writing MakeMove #5 - TakeMove()](https://www.youtube.com/watch?v=aKaU0WHVrJI)
43. [Introduction to Perft testing](https://www.youtube.com/watch?v=ioaPTMKU3zg) » [Perft](Perft "Perft")
44. [Perft Testing (Move Make / Unmake debug)](https://www.youtube.com/watch?v=6Y_FaQhqX2c) » [Unmake Move](Unmake_Move "Unmake Move")
45. [Quick Look At MinMax and NegaMax](https://www.youtube.com/watch?v=6ib1Kf44KR0) » [Minimax](Minimax "Minimax"), [Negamax](Negamax "Negamax")
46. [Quick Look At Alpha Beta](https://www.youtube.com/watch?v=j_ZHeE87udo) » [Alpha-Beta](Alpha-Beta "Alpha-Beta")
47. [Overview of search implementation](https://www.youtube.com/watch?v=eox81XUaXYI) » [Search](Search "Search")
48. [Parsing a move from user / GUI](https://www.youtube.com/watch?v=XPOcvp4h7VU) » [GUI](GUI "GUI")
49. [Repetition Detection](https://www.youtube.com/watch?v=1Vq-Ic9t4FE) » [Repetitions](Repetitions "Repetitions")
50. [Getting the time in milliseconds](https://www.youtube.com/watch?v=l_OrrycM7Fw)
51. [Principal Variation Table #1 Definitions](https://www.youtube.com/watch?v=AlwyJFG466M) » [Principal Variation](Principal_Variation "Principal Variation")
52. [Principal Variation Table #2 Store / Probe](https://www.youtube.com/watch?v=BpR76VBo7DQ)
53. [Principal Variation Table #3 Retrieval](https://www.youtube.com/watch?v=9LKX9jgqx84)
54. [Preparation for search](https://www.youtube.com/watch?v=_063cuTPOe8)
55. [Search Function Definitions](https://www.youtube.com/watch?v=F74y0ErjWTI)
56. [Basic Evaluation (very basic)](https://www.youtube.com/watch?v=zSJF6jZ61w0) » [Evaluation](Evaluation "Evaluation")
57. [Clear To Search](https://www.youtube.com/watch?v=6WobF80RgaY)
58. [Writing the Iterative Deepening Function](https://www.youtube.com/watch?v=31guiVzPJuU) » [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
59. [Writing the Alpha Beta Function](https://www.youtube.com/watch?v=-WyXnVpJVSQ) » [Alpha-Beta](Alpha-Beta "Alpha-Beta")
60. [Vice solves a Mate in 3 !](https://www.youtube.com/watch?v=r4pNoANs8_0) » [Checkmate](Checkmate "Checkmate")
61. [Move Ordering - Setting Up MVV LVA](https://www.youtube.com/watch?v=hDHa4-fijMc) » [Move Ordering](Move_Ordering "Move Ordering"), [MVV-LVA](MVV-LVA "MVV-LVA")
62. [Move Ordering - Picking a Move](https://www.youtube.com/watch?v=8LYMXwH1xsg)
63. [BUG ALERT - Change to Move Generation!](https://www.youtube.com/watch?v=RkZ7mUQnviA)
64. [Move Ordering - Killer, History Heuristics, PV Move](http://www.youtube.com/watch?v=jIc2YOP1W7U) » [Killer Heuristic](Killer_Heuristic "Killer Heuristic"), [History Heuristic](History_Heuristic "History Heuristic"), [PV-Move](PV-Move "PV-Move")
65. [Quiescence - Getting rid of the horizon effect](https://www.youtube.com/watch?v=ouWcWzyCOCY) » [Quiescence Search](Quiescence_Search "Quiescence Search")
66. [UCI Protocol #1 - Intoduction](https://www.youtube.com/watch?v=NBl92Vs0fos) » [UCI](UCI "UCI")
67. [UCI Protocol #2 - UCI Loop](https://www.youtube.com/watch?v=gcBYSby9f88)
68. [UCI Protocol #3 - Parse Position](https://www.youtube.com/watch?v=EzkmJEkAmoY)
69. [UCI Protocol #4 - Parse Go](https://www.youtube.com/watch?v=Lo54mNqOMAs)
70. [UCI Protocol #5 - Interrupt Thinking & Working Program](https://www.youtube.com/watch?v=gVGadWuBqEA)
71. [Vice vs Nero 6.1 - The first ever game!!](https://www.youtube.com/watch?v=_1S_vDHWJp8) » [Nero](Nero "Nero")
72. [XBoard / Winboard Protocol #1](https://www.youtube.com/watch?v=DZwW-st4Jl8) » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
73. [XBoard / Winboard Protocol #2](https://www.youtube.com/watch?v=ubSDzI3ecwc)
74. [XBoard / Winboard Protocol #3 And Console Mode](https://www.youtube.com/watch?v=pClToEJ-g-A)
75. [BUG ALERT #2](https://www.youtube.com/watch?v=KuQCsEcCO0g)
76. [In Check Extension](https://www.youtube.com/watch?v=1SiR7A1NQ0g) » [Check Extensions](Check_Extensions "Check Extensions")
77. [Improving Evaluation - Bitmasks](https://www.youtube.com/watch?v=XkbK_yOvcUw) » [Evaluation](Evaluation "Evaluation")
78. [Improving Evaluation - Pawn Bitmasks](https://www.youtube.com/watch?v=oB2l2KADPYc)
79. [Improving Evaluation - Mirror Board Function](https://www.youtube.com/watch?v=tfzG-o77RD8) » [Color Flipping](Color_Flipping "Color Flipping")
80. [Improving Evaluation - Isolani and passer](https://www.youtube.com/watch?v=uoHEwVSEy5s) » [Isolated Pawn](Isolated_Pawn "Isolated Pawn"), [Passed Pawn](Passed_Pawn "Passed Pawn")
81. [Improving Evaluation - Open Files](https://www.youtube.com/watch?v=XXdzSQ49aM0) » [Open File](Open_File "Open File")
82. [Improving Evaluation - King Position and Material Draws](https://www.youtube.com/watch?v=4ozHuSRDyfE) » [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
83. [Null Move Pruning #1](https://www.youtube.com/watch?v=wgYuNhzCYe0) » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
84. [Null Move Pruning #2](https://www.youtube.com/watch?v=5rqXb_QMLA4)
85. [Transpositon Table](https://www.youtube.com/watch?v=MMoOsCHSdj4) » [Transposition Table](Transposition_Table "Transposition Table")
86. [Test Results, Debug Test Run](https://www.youtube.com/watch?v=jmLNzigTceM) » [Debugging](Debugging "Debugging")
87. [Vice 1.0 release, end of series](https://www.youtube.com/watch?v=-G_tQKNfVuM)
88. [Adding An opening Book Using Polyglot](https://www.youtube.com/watch?v=HjZtevzCa5Y) » [Opening Book](Opening_Book "Opening Book"), [PolyGlot](PolyGlot "PolyGlot")
89. [Polyglot Opening Book #1](https://www.youtube.com/watch?v=hGy5kR_mOdM)
90. [Polyglot Book #2 Hashkey Generation](https://www.youtube.com/watch?v=jEurXv03JIs)
91. [Polyglot Book #3 Read In Data](https://www.youtube.com/watch?v=_VZfnlhk2SU)
92. [Polyglot Book #4 Read Book Moves](https://www.youtube.com/watch?v=wT7H4ogSDak)
93. [Polyglot Book #5 Internal Format Book Moves](https://www.youtube.com/watch?v=u5WEOplKjdc)
94. [Polyglot Book #6 Book Option](https://www.youtube.com/watch?v=30GFA_d98SQ)
95. [Vice 1.1 Polyglot Books](https://www.youtube.com/watch?v=eGGL_9_qduI)


### Misc


* [vice - Wiktionary](https://en.wiktionary.org/wiki/vice)
* [Vice (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Vice_%28disambiguation%29)
* [Vice from Wikipedia](https://en.wikipedia.org/wiki/Vice)
* [Vice (character) from Wikipedia](https://en.wikipedia.org/wiki/Vice_%28character%29)
* [Tree of virtues and tree of vices from Wikipedia](https://en.wikipedia.org/wiki/Tree_of_virtues_and_tree_of_vices)
* [Seven deadly sins from Wikipedia](https://en.wikipedia.org/wiki/Seven_deadly_sins)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> "Tree of Vices" from [Speculum Virginum](https://en.wikipedia.org/wiki/Speculum_Virginum), [Walters Art Museum](https://en.wikipedia.org/wiki/Walters_Art_Museum), [Ms. W.72, fol. 25v](http://www.thedigitalwalters.org/Data/WaltersManuscripts/html/W72/description.html), Early [13th century](https://en.wikipedia.org/wiki/13th_century) manuscript from the [Cistercian](https://en.wikipedia.org/wiki/Cistercians) [abbey of Himmerode](https://en.wikipedia.org/wiki/Himmerod_Abbey), [Tree of virtues and tree of vices from Wikipedia](https://en.wikipedia.org/wiki/Tree_of_virtues_and_tree_of_vices)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a>  [Programming A Chess Engine in C](http://www.youtube.com/watch?v=bGAfaepBco4&feature=share&list=PLZ1QII7yudbc-Ky058TEaOstZHVbT-2hg), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos by [BlueFeverSoft](BlueFeverSoft "BlueFeverSoft")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Vice ReadMe File and Download](http://bluefever.net/Downloads/ViceReadMe.html)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Vice CCRL rating](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77205) by [Amanj Sherwany](Amanj_Sherwany "Amanj Sherwany"), [CCC](CCC "CCC"), April 29, 2021 » [CCRL](CCRL "CCRL")

**[Up one Level](Engines "Engines")**







 
