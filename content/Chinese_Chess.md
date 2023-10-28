---
title: Chinese Chess
---
**[Home](Home "Home") * [Games](Games "Games") * Chinese Chess**

\[ Xiangqi board, with pieces in their starting positions [[1]](#cite_note-1)
**Chinese Chess**, or **Xiangqi** 象棋 [[2]](#cite_note-2),\
is a chess variant which is very popular in East Asia, especially in China and Vietnam. The Chinese Chess set includes a board and 32 pieces for two players. The board has ten horizontal lines called [ranks](Ranks "Ranks") and nine vertical lines called [files](Files "Files"). Pieces are located not in the cells but intersectional points of ranks and files which are 90 in total. In the middle of the board the central seven files are interrupted by a horizontal space called the “River”, which splits the board into two parts. Each side of the board has a “Palace” a 3x3 area in the central base. The two sides are usually distinguished by colors, traditional names are red or black [[3]](#cite_note-3) but now they can be called white and black as chess. Sometimes the Xiangqi board could be considered as the presentation of the war between two countries when the standard chess presents for a battle only.

## Contents

- [1 Pieces](#Pieces)
- [2 Rules](#Rules)
  - [2.1 Basic](#Basic)
  - [2.2 3-Folk Rules](#3-Folk_Rules)
- [3 Notations](#Notations)
- [4 Programming](#Programming)
- [5 Sub variants](#Sub_variants)
- [6 Engines](#Engines)
- [7 Computer Olympiads](#Computer_Olympiads)
- [8 Photos](#Photos)
- [9 Publications](#Publications)
  - [9.1 1981 ...](#1981_...)
  - [9.2 1990 ...](#1990_...)
  - [9.3 2000 ...](#2000_...)
  - [9.4 2005 ...](#2005_...)
  - [9.5 2010 ...](#2010_...)
  - [9.6 2015 ...](#2015_...)
  - [9.7 2020 ...](#2020_...)
- [10 Forum Posts](#Forum_Posts)
  - [10.1 1994](#1994)
  - [10.2 2000 ...](#2000_..._2)
  - [10.3 2010 ...](#2010_..._2)
  - [10.4 2015 ...](#2015_..._2)
  - [10.5 2020 ...](#2020_..._2)
- [11 External Links](#External_Links)
  - [11.1 Chinese Chess](#Chinese_Chess)
  - [11.2 Computer Chinese Chess](#Computer_Chinese_Chess)
  - [11.3 Source Code](#Source_Code)
  - [11.4 Xiangqi Cloud Database](#Xiangqi_Cloud_Database)
- [12 References](#References)

## Pieces

There are 7 types: King, Advisor, Elephant, Rook, Cannon, Horse, and Pawn. Typically those pieces are made from small, simple wood pieces which some symbols (new way) or Chinese characters (traditional way) written on them. As the Chinese characters, pieces on the white side may use different characters than their counterparts on the black side. They are the same pieces, but names on the White side are subtly more noble than those on the Black side [[4]](#cite_note-4).

Cannon is the most interesting piece in Chinese chess.

|  Images
|  Name
|  Notation [[5]](#cite_note-5) |  Value [[6]](#cite_note-6) |  Movement
|  Restriction
|
| --- | --- | --- | --- | --- | --- |
| [Xiangqi General (Trad).svg](</File:Xiangqi_General_(Trad).svg>) |  帥、將
| King(General)
|  K
|  |  moves and capturesone orthogonal step
|  may not leave the palaceThe two kings may not faceeach other along the same filewith no intervening piece
|
| [Xiangqi Advisor (Trad).svg](</File:Xiangqi_Advisor_(Trad).svg>) |  仕, 士
| Advisor
(Guard)
|  A
|  2
|  moves and capturesone diagonal step
|  may not leave the palace
|
| [Xiangqi Elephant (Trad).svg](</File:Xiangqi_Elephant_(Trad).svg>) |  相、象
| Elephant
|  E
|  2
|  moves and capturestwo diagonal points
|  may not jump over interveningpieces,may not cross the river
|
| [Xiangqi Horse (Trad).svg](</File:Xiangqi_Horse_(Trad).svg>) |  傌, 馬
| Horse
|  H
|  4
|  moves and capturesone orthogonal stepplus one diagonal step
|  blocked by orthogonal adjacentpieces
|
| [Xiangqi Chariot (Trad).svg](</File:Xiangqi_Chariot_(Trad).svg>) |  俥, 車
| Rook(ChaRiot)
|  R
|  9
|  moves and capturesany distance orthogonally
|  may not jump over interveningpieces
|
| [Xiangqi Cannon (Trad).svg](</File:Xiangqi_Cannon_(Trad).svg>) |  炮, 炮
| Cannon
|  C
|  4½
|  moves any distance orthogonally - captures by jumping asingle piece, friend or foe, in-between the orthogonal pathof attack towards the captured piece
|
| [Xiangqi Soldier (Trad).svg](</File:Xiangqi_Soldier_(Trad).svg>) |  兵、卒
| Pawn(Soldier)
|  P(S)
|  12
|  moves and captures one step forward -once crossed the river, also one point sideways
|

## Rules

## Basic

Basic rules are similar to chess with some modifications. Pieces can move and capture according to their individual ability and restriction along the lines including the “Riverbanks”. Xiangqi doesn’t have rules such as castles, en-passants, promotions. Instead it has some limitations such as King, Advisors must move inside their own Palaces, Horses and Elephants can be blocked (from moving), two King cannot “face” each other (stands in the same column without any piece between). The object of the game is to [checkmate](Checkmate "Checkmate") or [stalemate](Stalemate "Stalemate") (is a win as well) the opponent King aka General.

## 3-Folk Rules

When a position repeated 3 time (3 folks) the game will be terminated too. However, partly due to the freedom and power of the Rook over other pieces, and the limited freedom of the King, it is forbidden to [repeat](Repetitions "Repetitions") perpetually a direct thread (i.e. a perpetual check 長將, perpetual thread of capture 長捉, a check and then a threat of mate 一將一殺, or a combination of these). If no side violates the forbidden, game will be ruled as a draw.

Ruling the game when 3 forks happen is the hardest thing for fully understanding, installing for both players and software.

## Notations

- [FEN](FEN "FEN"): Chinese Chess can use [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") to save down positions, ignored some fields such as Castling and En passant target square. Here is FEN of the starting position: rheakaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAKAEHR w - - 0 1

- [Traditional Chinese Chess Notation](index.php?title=Traditional_Chinese_Chess_Notation&action=edit&redlink=1 "Traditional Chinese Chess Notation (page does not exist)")

- [SAN](index.php?title=SAN&action=edit&redlink=1 "SAN (page does not exist)")

- [WXF](index.php?title=WXF&action=edit&redlink=1 "WXF (page does not exist)")

## Programming

Chinese chess is quite similar to chess in multi-aspects thus its software can be developed and tested in similar ways. It can use almost all chess techniques, from traditional methods using [Board Representation](Board_Representation "Board Representation"), [Alpha-Beta](Alpha-Beta "Alpha-Beta") [search](Search "Search"), [Evaluation](Evaluation "Evaluation"), [Opening Book](Opening_Book "Opening Book"), [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")... to new ones using [NNUE](NNUE "NNUE"), [AlphaZero](AlphaZero "AlphaZero") methods...

However its programming is a bit harder to gain high levels due to some reasons:

a) The board is significantly larger (90 vs 64, 40% larger)

b) Even there’s no diagonal slide moves (such as Bishops), its pieces have more limitations, been blockable, Cannons have a special way to capture... The board size (90) can't fit 64-bit integer either, the number of columns 9 can't help quick devices... All may make move generators be more complex and slower

c) The search trees are usually larger. For example, when comparing Perft results at deep 7, Xiangqi number is 72 times as large

d) Evaluation of positions may require more knowledge, especially endgame positions

e) Rules 3-fork repetitions are hard to implement and maybe so slow

- [Chinese Chess Board Representation](Chinese_Chess_Board_Representation "Chinese Chess Board Representation")
- [Chinese Chess Perft Results](Chinese_Chess_Perft_Results "Chinese Chess Perft Results")

## Sub variants

- [Banqi](index.php?title=Banqi&action=edit&redlink=1 "Banqi (page does not exist)")
- [Jeiqi](Jeiqi "Jeiqi")

## Engines

- [Xiangqi Engines](Category:Xiangqi "Category:Xiangqi")

## [Computer Olympiads](Computer_Olympiad "Computer Olympiad")

- [1st Computer Olympiad, London 1989](1st_Computer_Olympiad#ChineseChess "1st Computer Olympiad")
- [2nd Computer Olympiad, London 1990](2nd_Computer_Olympiad#ChineseChess "2nd Computer Olympiad")
- [3rd Computer Olympiad, Maastricht 1991](3rd_Computer_Olympiad#ChineseChess "3rd Computer Olympiad")
- [4th Computer Olympiad, London 1992](4th_Computer_Olympiad#ChineseChess "4th Computer Olympiad")
- [6th Computer Olympiad, Maastricht 2001](6th_Computer_Olympiad#ChineseChess "6th Computer Olympiad")
- [7th Computer Olympiad, Maastricht 2002](7th_Computer_Olympiad#ChineseChess "7th Computer Olympiad")
- [8th Computer Olympiad, Graz 2003](8th_Computer_Olympiad#ChineseChess "8th Computer Olympiad")
- [9th Computer Olympiad, Ramat Gan 2004](9th_Computer_Olympiad#ChineseChess "9th Computer Olympiad")
- [10th Computer Olympiad, Taipei 2005](10th_Computer_Olympiad#ChineseChess "10th Computer Olympiad")
- [11th Computer Olympiad, Turin 2006](11th_Computer_Olympiad#ChineseChess "11th Computer Olympiad")
- [12th Computer Olympiad, Amsterdam 2007](12th_Computer_Olympiad#ChineseChess "12th Computer Olympiad")
- [13th Computer Olympiad, Beijing 2008](13th_Computer_Olympiad#ChineseChess "13th Computer Olympiad")
- [14th Computer Olympiad, Pamplona 2009](14th_Computer_Olympiad#ChineseChess "14th Computer Olympiad")
- [15th Computer Olympiad, Kanazawa 2010](15th_Computer_Olympiad#ChineseChess "15th Computer Olympiad")
- [16th Computer Olympiad, Tilburg 2011](16th_Computer_Olympiad#ChineseChess "16th Computer Olympiad")
- [17th Computer Olympiad, Yokohama 2013](17th_Computer_Olympiad#ChineseChess "17th Computer Olympiad")
- [18th Computer Olympiad, Leiden 2015](18th_Computer_Olympiad#ChineseChess "18th Computer Olympiad")
- [19th Computer Olympiad, Leiden 2016](19th_Computer_Olympiad#ChineseChess "19th Computer Olympiad")
- [20th Computer Olympiad, Leiden 2017](20th_Computer_Olympiad#ChineseChess "20th Computer Olympiad")

## Photos

[](http://www.yss-aya.com/photo/graz2003/1126/Htmls/PICT1282.html)
Xiangqi winners in [Graz 2003](8th_Computer_Olympiad#ChineseChess "8th Computer Olympiad"), [Pascal Tang](Pascal_Tang "Pascal Tang"), [Zhi-Jian Tu](index.php?title=Zhi-Jian_Tu&action=edit&redlink=1 "Zhi-Jian Tu (page does not exist)") and [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") [[7]](#cite_note-7)

[](http://icga.leidenuniv.nl/icga/news/Olympiad/Olympiad2005/fotos/IMG_0232.JPG)
Xiangqi winners [Taipei 2005](10th_Computer_Olympiad#ChineseChess "10th Computer Olympiad") with TD [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") and representative of the sponsor [Acer Inc.](https://en.wikipedia.org/wiki/Acer_Inc.),\
[Mingyang Zhao](index.php?title=Mingyang_Zhao&action=edit&redlink=1 "Mingyang Zhao (page does not exist)") (Gold), [Ming-Cheng Cheng](index.php?title=Ming-Cheng_Cheng&action=edit&redlink=1 "Ming-Cheng Cheng (page does not exist)") (Silver) and [Jiao Wang](Jiao_Wang "Jiao Wang") (Bronze) [[8]](#cite_note-8)

[](http://icga.org//?page_id=800&wppa-album=3&wppa-cover=0&wppa-occur=1&wppa-photo=45)
[Yokohama 2013](17th_Computer_Olympiad "17th Computer Olympiad"), [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") and [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") [[9]](#cite_note-9)

## Publications

## 1981 ...

- Y.T. Zhang (**1981**). *Application of Artificial Intelligence in Computer Chinese Chess*. M.Sc. thesis, Department of Electrical Engineering, [National Taiwan University](National_Taiwan_University "National Taiwan University") (Chinese)
- [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), D.H. Huang (**1985**). *Design and Implementation of a Chinese Chess Knowledge Base.* Proceedings of NCS, pp. 505-509. (Chinese)
- Robert Nisonoff, M. Stephanie Ricks (**1988**). *To Catch a King: East Meets West in the Game of Chess*. [PC Magazine](PC_Magazine "PC Magazine"), October 31, 1988, pp. 506 » [EGA Chess](EGA_Chess "EGA Chess"), [Xian](index.php?title=Xian&action=edit&redlink=1 "Xian (page does not exist)")
- [Nick Jacobs](index.php?title=Nick_Jacobs&action=edit&redlink=1 "Nick Jacobs (page does not exist)") (**1989**). *Xian, a Chinese Chess Program*. [Heuristic Programming in AI 1](1st_Computer_Olympiad#Workshop "1st Computer Olympiad")

## 1990 ...

- [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**1990**). *Introduction to Computer Chess and Computer Chinese Chess.* Journal of Computer, Vol. 2, No. 2, pp. 1-8. (in Chinese)
- [Kuo-Ming Tsao](index.php?title=Kuo-Ming_Tsao&action=edit&redlink=1 "Kuo-Ming Tsao (page does not exist)"), [Jen-Hsuan Li](index.php?title=Jen-Hsuan_Li&action=edit&redlink=1 "Jen-Hsuan Li (page does not exist)"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**1991**). *Design and Implementation of a Chinese Chess Program*. [Heuristic Programming in AI 2](2nd_Computer_Olympiad#Workshop "2nd Computer Olympiad")
- [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Kuo-Ming Tsao](index.php?title=Kuo-Ming_Tsao&action=edit&redlink=1 "Kuo-Ming Tsao (page does not exist)") (**1991**). *Design and Implementation of an Opening Game Knowledge-Base System for Computer Chinese Chess.* Bulletin of the College of Engineering, N.T.U., No. 53, pp. 75-86. (in Chinese)
- [Chun Ye](Chun_Ye "Chun Ye") (**1992**). *Experiments in Selective Search Extensions*. MSc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1)
- [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Experiments in Forward Pruning with Limited Extensions.* [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/RecentPapers/Experiments-FP-YeMars-1992.pdf)
- [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Selective Extensions in Game-Tree Search.* [Heuristic Programming in AI 3](3rd_Computer_Olympiad#Workshop "3rd Computer Olympiad"), [pdf](https://webdocs.cs.ualberta.ca/~tony/RecentPapers/SelectiveExten-YeMars.pdf)
- [Yi-Fan Ke](Yi-Fan_Ke "Yi-Fan Ke"), [Tai-Ming Parng](Tai-Ming_Parng "Tai-Ming Parng") (**1993**). *The Guard Heuristic: Legal Move Ordering with Forward Game-Tree Pruning*. [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal")
- [Mei-En Chen](index.php?title=Mei-En_Chen&action=edit&redlink=1 "Mei-En Chen (page does not exist)"), [Yo-Ping Huang](index.php?title=Yo-Ping_Huang&action=edit&redlink=1 "Yo-Ping Huang (page does not exist)") (**1995**). *[Guard heuristic by dynamic fuzzy reasoning model for Chinese chess](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=527751)*. Proceedings of ISUMA-NAFIPS '95

## 2000 ...

- [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2001**). *ELP wins Chinese Chess tournament*. [ICGA Journal, Vol. 24, No. 3](ICGA_Journal#24_3 "ICGA Journal") » [6th Computer Olympiad#ChineseChess](6th_Computer_Olympiad#ChineseChess "6th Computer Olympiad")
- [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2001**). *Construction of Chinese Chess Endgame Databases by Retrograde Analysis*. [CG 2000](CG_2000 "CG 2000")

**2002**

- [Ren Wu](Ren_Wu "Ren Wu"), [Don Beal](Don_Beal "Don Beal") (**2002**). *A memory efficient retrograde algorithm and its application to solve Chinese Chess endgames.* [More Games of No Chance](http://library.msri.org/books/Book42/) edited by [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski")
- [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2002**). *ELP wins Chinese Chess tournament*. [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal") » [7th Computer Olympiad#ChineseChess](7th_Computer_Olympiad#ChineseChess "7th Computer Olympiad")
- [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2002**). *[Indefinite Sequence of Moves in Chinese Chess Endgames](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_18)*. [CG 2002](CG_2002 "CG 2002")

**2003**

- [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2003**). *ZMBL wins Chinese Chess tournament*. [ICGA Journal, Vol. 26, No. 4](ICGA_Journal#26_4 "ICGA Journal") » [8th Computer Olympiad#ChineseChess](8th_Computer_Olympiad#ChineseChess "8th Computer Olympiad")

**2004**

- [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2004**). *Checking Indefinitely in Chinese-Chess Endgames*. [ICGA Journal, Vol. 27, No. 1](ICGA_Journal#27_1 "ICGA Journal")
- [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Tai-Ning Yang](index.php?title=Tai-Ning_Yang&action=edit&redlink=1 "Tai-Ning Yang (page does not exist)"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2004**). *[Computer Chinese Chess](https://www.researchgate.net/publication/220174553_Computer_Chinese_Chess)*. [ICGA Journal, Vol. 27, No. 1](ICGA_Journal#27_1 "ICGA Journal"), [pdf](https://pdfs.semanticscholar.org/223d/ef59c884503f18610bba314034157f55aacd.pdf)
- [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang") (**2004**). *[Rule-Tolerant Verification Algorithms for Completeness of Chinese-Chess Endgame Databases](http://link.springer.com/chapter/10.1007/11674399_9)*. [CG 2004](CG_2004 "CG 2004")
- [Kuang-Che Wu](index.php?title=Kuang-Che_Wu&action=edit&redlink=1 "Kuang-Che Wu (page does not exist)"), [Tsan-Sheng Hsu](index.php?title=Tsan-Sheng_Hsu&action=edit&redlink=1 "Tsan-Sheng Hsu (page does not exist)"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2004**). *Contemplation wins Chinese Chess tournament*. [ICGA Journal, Vol. 27, No. 3](ICGA_Journal#27_3 "ICGA Journal") » [9th Computer Olympiad#ChineseChess](9th_Computer_Olympiad#ChineseChess "9th Computer Olympiad")

## 2005 ...

- [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang") (**2005**). *The Nature of Retrograde Analysis for Chinese Chess, Part I*. [ICGA Journal, Vol. 28, No. 2](ICGA_Journal#28_2 "ICGA Journal")
- [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang") (**2005**). *Nature of Retrograde Analysis for Chinese Chess, Part II*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal")
- [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2005**). *XQMaster wins Chinese Chess tournament*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal") » [10th Computer Olympiad#ChineseChess](10th_Computer_Olympiad#ChineseChess "10th Computer Olympiad")

**2006**

- [Kuang-Che Wu](index.php?title=Kuang-Che_Wu&action=edit&redlink=1 "Kuang-Che Wu (page does not exist)"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2006**). *The Graph-History Interaction Problem in Chinese Chess.* [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11")
- [Xinhe Xu](Xinhe_Xu "Xinhe Xu") (**2006**). *Principle and Methodology of Computer Games of Chinese Chess*. [ISDA 2006](http://www.informatik.uni-trier.de/~ley/db/conf/isda/isda2006-1.html#Xu06)
- [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Pangfeng Liu](Pangfeng_Liu "Pangfeng Liu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2008**). *Abstracting Knowledge from Annotated Chinese-Chess Game Records*. [CG 2006](CG_2006 "CG 2006")
- [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2006**). *NEUChess wins Chinese Chess tournament*. [ICGA Journal, Vol. 29, No. 2](ICGA_Journal#29_2 "ICGA Journal") » [11th Computer Olympiad#ChineseChess](11th_Computer_Olympiad#ChineseChess "11th Computer Olympiad")
- [Chun-Bin Hsu](Chun-Bin_Hsu "Chun-Bin Hsu") (**2006**). *Pattern Recognition in Chinese Chess*. Master thesis, [National Chiao Tung University](National_Chiao_Tung_University "National Chiao Tung University"), [pdf](https://ir.nctu.edu.tw/bitstream/11536/78749/1/753801.pdf) (Chinese)

**2007**

- [Changming Xu](index.php?title=Changming_Xu&action=edit&redlink=1 "Changming Xu (page does not exist)") (**2007**). *NEUChess wins Chinese Chess tournament*. [ICGA Journal, Vol. 30, No. 2](ICGA_Journal#30_2 "ICGA Journal") » [12th Computer Olympiad#ChineseChess](12th_Computer_Olympiad#ChineseChess "12th Computer Olympiad")
- [Chin Soon Ong](index.php?title=Chin_Soon_Ong&action=edit&redlink=1 "Chin Soon Ong (page does not exist)"), [Hanyang Quek](index.php?title=Hanyang_Quek&action=edit&redlink=1 "Hanyang Quek (page does not exist)"), [Kay Chen Tan](index.php?title=Kay_Chen_Tan&action=edit&redlink=1 "Kay Chen Tan (page does not exist)"), [Arthur Tay](index.php?title=Arthur_Tay&action=edit&redlink=1 "Arthur Tay (page does not exist)") (**2007**). *[Discovering Chinese Chess Strategies through Coevolutionary Approaches](https://www.semanticscholar.org/paper/Discovering-Chinese-Chess-Strategies-through-Coevo-Ong-Quek/489e4f258766855943c941cd65ca2989ad64ed14)*. [IEEE Symposium on Computational Intelligence and Games](IEEE#CIG "IEEE"), [pdf](http://wxf.ca/xq/book/2011.pdf)

**2008**

- [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Pangfeng Liu](Pangfeng_Liu "Pangfeng Liu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2008**). *[Knowledge Inferencing on Chinese Chess Endgames](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_17)*. [CG 2008](CG_2008 "CG 2008")
- [Jiao Wang](Jiao_Wang "Jiao Wang"), [Xinhe Xu](Xinhe_Xu "Xinhe Xu") (**2008**). *Intella wins Chinese Chess tournament*. [ICGA Journal, Vol. 31, No. 3](ICGA_Journal#31_3 "ICGA Journal") » [13th Computer Olympiad#ChineseChess](13th_Computer_Olympiad#ChineseChess "13th Computer Olympiad")

**2009**

- [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Pangfeng Liu](Pangfeng_Liu "Pangfeng Liu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2009**). *Conflict Resolution of Chinese Chess Endgame Knowledge Base*. [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [pdf](http://ticc.uvt.nl/icga/acg12/proceedings/Contribution108.pdf)
- [Guofeng Tong](index.php?title=Guofeng_Tong&action=edit&redlink=1 "Guofeng Tong (page does not exist)"), [Ying Qu](http://www.informatik.uni-trier.de/~ley/pers/hd/q/Qu:Ying.html), [Tong Cheng](http://www.informatik.uni-trier.de/~ley/pers/hd/c/Cheng:Tong.html) (**2009**). *[Human-computer interactive gaming system - a chinese chess robot](http://dl.acm.org/citation.cfm?id=1733531)*. [IROS 2009](http://www.informatik.uni-trier.de/~ley/db/conf/iros/iros2009.html#TongQC09), pp. 984-987 » [Robots](Robots "Robots")
- [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2009**). *TMSK wins the Chinese-Chess tournament*. [ICGA Journal, Vol. 32, No. 2](ICGA_Journal#32_2 "ICGA Journal") » [14th Computer Olympiad#ChineseChess](14th_Computer_Olympiad#ChineseChess "14th Computer Olympiad")
- [Wei-Lun Kao](Wei-Lun_Kao "Wei-Lun Kao") (**2009**). *The Automatically Tuning System of Evaluation Function for Computer Chinese Chess*. Master thesis, [National Chiao Tung University](National_Chiao_Tung_University "National Chiao Tung University"), [pdf](https://ir.nctu.edu.tw/bitstream/11536/43333/1/553001.pdf) (Chinese)

## 2010 ...

- [Jiao Wang](Jiao_Wang "Jiao Wang"), [Si-Zhong Li](index.php?title=Si-Zhong_Li&action=edit&redlink=1 "Si-Zhong Li (page does not exist)"), [Xin-He Xu](Xinhe_Xu "Xinhe Xu") (**2010**). *A Minors Hash Table in Chinese-Chess Programs*. [ICGA Journal, Vol. 33, No. 1](ICGA_Journal#33_1 "ICGA Journal")
- [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Bing-Jie Shen](Bing-Jie_Shen "Bing-Jie Shen"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2010**). *Chinese Dark Chess*. [ICGA Journal, Vol. 33, No. 2](ICGA_Journal#33_2 "ICGA Journal")
- [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Pangfeng Liu](Pangfeng_Liu "Pangfeng Liu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2010**). *[Knowledge Abstraction in Chinese Chess Endgame Databases](http://www.springerlink.com/content/6374711454584j73/)*. [CG 2010](CG_2010 "CG 2010")

**2011**

- [Jr-Hung Guo](http://www.informatik.uni-trier.de/~ley/pers/hd/g/Guo:Jr=Hung.html), [Kuo-Lan Su](http://www.informatik.uni-trier.de/~ley/pers/hd/s/Su:Kuo=Lan.html), [Sheng-Ven Shiau](http://arnetminer.org/person/sheng-ven-shiau-1028081.html) (**2011**). *Path Searching Algorithms of Multiple Robot System Applying in Chinese Chess Game*. [Recent Advances in Mobile Robotics](http://www.intechopen.com/books/recent-advances-in-mobile-robotics), [Dr. Andon Topalov](http://www.intechopen.com/profiles/557/Andon-Topalov) (Ed.), ISBN: 978-953-307-909-7, [pdf](http://cdn.intechopen.com/pdfs/24923/InTech-Path_searching_algorithms_of_multiple_robot_system_applying_in_chinese_chess_game.pdf) » [Robots](Robots "Robots")

**2013**

- [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ching-Hua Kuo](Ching-Hua_Kuo "Ching-Hua Kuo"), [Bo-Han Lin](index.php?title=Bo-Han_Lin&action=edit&redlink=1 "Bo-Han Lin (page does not exist)") (**2013**). *[A Supervised Learning Method for Chinese Chess Programs](https://kaigi.org/jsai/webprogram/2013/paper-138.html)*. [JSAI2013](http://2013.conf.ai-gakkai.or.jp/english-info), [pdf](https://kaigi.org/jsai/webprogram/2013/pdf/138.pdf)
- [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Tsan-Cheng Su](index.php?title=Tsan-Cheng_Su&action=edit&redlink=1 "Tsan-Cheng Su (page does not exist)") (**2013**). *SHIGA Wins Chinese Chess Tournament*. [ICGA Journal, Vol. 36, No. 3](ICGA_Journal#36_3 "ICGA Journal") » [17th Computer Olympiad#ChineseChess](17th_Computer_Olympiad#ChineseChess "17th Computer Olympiad")
- [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Hung-Jui Chang](Hung-Jui_Chang "Hung-Jui Chang"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2013**). *Multilevel Inference in Chinese Chess Endgame Knowledge Bases*. [ICGA Journal, Vol. 36, No. 4](ICGA_Journal#36_4 "ICGA Journal") » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")

**2014**

- [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Hung-Jui Chang](Hung-Jui_Chang "Hung-Jui Chang"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2014**). *Advanced Meta-knowledge for Chinese Chess Endgame Knowledge Bases*. [ICGA Journal, Vol 37, No. 1](ICGA_Journal#37_1 "ICGA Journal")

## 2015 ...

- [Qiang Gao](Qiang_Gao "Qiang Gao"), [Xinhe Xu](Xinhe_Xu "Xinhe Xu") (**2015**). *Research on the Computational Complexity of n x n Chinese Chess*. [ICGA Journal, Vol. 38, No. 1](ICGA_Journal#38_1 "ICGA Journal")
- [Pascal Tang](Pascal_Tang "Pascal Tang") (**2015**). *SHIGA wins Chinese Chess Tournament*. [ICGA Journal, Vol. 38, No. 4](ICGA_Journal#38_4 "ICGA Journal") » [18th Computer Olympiad#ChineseChess](18th_Computer_Olympiad#ChineseChess "18th Computer Olympiad")
- [Nguyen Hong Pham](Pham_Hong_Nguyen "Pham Hong Nguyen") (**2018**). *A completed implementation for Xiangqi rules*. [ICGA Journal, Vol. 40, No. 3](ICGA_Journal#40_3 "ICGA Journal")
- [Ting-Yu Lin](index.php?title=Ting-Yu_Lin&action=edit&redlink=1 "Ting-Yu Lin (page does not exist)"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2018**). *The number of effective moves for Chinese chess*. [CG 2018](CG_2018 "CG 2018"), [ICGA Journal, Vol. 40, No. 4](ICGA_Journal#40_4 "ICGA Journal")
- [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Tinghan Wei](index.php?title=Tinghan_Wei&action=edit&redlink=1 "Tinghan Wei (page does not exist)") (**2018**). *Comparison Training for Computer Chinese Chess*. [arXiv:1801.07411](https://arxiv.org/abs/1801.07411)

## 2020 ...

- [Maximilian Langer](Maximilian_Langer "Maximilian Langer") (**2021**). *Evaluation of Monte-Carlo Tree Search for Xiangqi*. B.Sc. thesis, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](https://ml-research.github.io/papers/langer2021xiangqi.pdf)

## Forum Posts

## 1994

- [rec.games.chinese-chess FAQ](https://groups.google.com/d/msg/rec.games.chinese-chess/4lorUoAbEME/FAmEa1DpSakJ) by Stephen Leary, [rec.games.chinese-chess](Computer_Chess_Forums "Computer Chess Forums"), January 04, 1994, also from [chessvariants](http://www.chessvariants.com/chinfaq.html)
- [Xiang Qi Is Not The Elephant Game](https://groups.google.com/d/msg/rec.games.chinese-chess/gcreEzzU3yQ/HvWOlP7yaYkJ) by Stephen Leary, [rec.games.chinese-chess](Computer_Chess_Forums "Computer Chess Forums"), November 18, 1994
- [Machine vs. IGM in Chinese Chess](https://www.stmintz.com/ccc/index.php?id=60304) by [Ren Wu](Ren_Wu "Ren Wu"), [CCC](CCC "CCC"), July 13, 1999

## 2000 ...

- [Tony Marsland and Chinese Chess in Maastricht (slightly O.T.)](https://www.stmintz.com/ccc/index.php?id=243199) by [Omid David](Eli_David "Eli David"), [CCC](CCC "CCC"), July 30, 2002 » [7th Computer Olympiad, Maastricht 2002](7th_Computer_Olympiad#ChineseChess "7th Computer Olympiad")

[Re: Tony Marsland and Chinese Chess in Maastricht (slightly O.T.)](https://www.stmintz.com/ccc/index.php?id=243231) by [Pham Hong Nguyen](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), July 30, 2002

- [Bitboard techniques in Xiangqi](http://www.talkchess.com/forum/viewtopic.php?t=26527) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 12, 2009 » [Bitboards](Bitboards "Bitboards")
- [Computer Olympiad (XQ)](http://www.talkchess.com/forum/viewtopic.php?t=27903) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 14, 2009 » [14th Computer Olympiad, Pamplona 2009](14th_Computer_Olympiad#ChineseChess "14th Computer Olympiad")
- [Kindergarten bitboards and Xiangqi move genaration?](http://www.talkchess.com/forum/viewtopic.php?t=31348) by Han Chengye, [CCC](CCC "CCC"), December 30, 2009 » [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")

## 2010 ...

- [Xiangqi evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=35356) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), July 09, 2010 » [Evaluation](Evaluation "Evaluation")
- [Xiangqi chase algorithm](http://www.talkchess.com/forum/viewtopic.php?t=41110) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), November 16, 2011 » [Sjaak](</Sjaak_(Glebbeek)> "Sjaak (Glebbeek)")
- [Interesting (Chinese) Chess variant](http://www.talkchess.com/forum/viewtopic.php?t=51019) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 23, 2014
- [UCCI2WB](http://www.talkchess.com/forum/viewtopic.php?t=54162) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 27, 2014 » [Protocols](Protocols "Protocols")
- [UCI protocol for chess variants](http://www.talkchess.com/forum/viewtopic.php?t=54167) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 28, 2014 » [UCI](UCI "UCI")
- [Xiangqi chase - again](http://www.talkchess.com/forum/viewtopic.php?t=54258) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), November 06, 2014 » [Sjaak](</Sjaak_(Glebbeek)> "Sjaak (Glebbeek)")

## 2015 ...

- [Evaluation in Xiangqi](http://www.talkchess.com/forum/viewtopic.php?t=56885) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 06, 2015
- [11-men tablebases (XQ)](http://www.talkchess.com/forum/viewtopic.php?t=60255) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 23, 2016 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [Xiangqi piece value model](http://www.talkchess.com/forum/viewtopic.php?t=60303) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), May 29, 2016 » [Point Value](Point_Value "Point Value")
- [Perft for Xiangqi & Shogi](http://www.talkchess.com/forum/viewtopic.php?t=60445) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), June 12, 2016 » [Shogi](Shogi "Shogi"), [Perft](Perft "Perft")
- [Cumulative building of a shared search tree](http://www.talkchess.com/forum/viewtopic.php?t=62639) by [Bojun Guo](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), December 28, 2016 » [Opening Book](Opening_Book "Opening Book"), [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
- [Probe EGT in quiescence?](http://www.talkchess.com/forum/viewtopic.php?t=64030) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), May 20, 2017 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases"), [Quiescence Search](Quiescence_Search "Quiescence Search")
- [A new design for Xianqgi (Chinese chess) Endgame Tablebase](http://www.talkchess.com/forum/viewtopic.php?t=66337) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), January 16, 2018 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [Chinese Chess](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67534) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 22, 2018
- [Xiangqi evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67877) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 01, 2018
- [A proposal for Jeiqi notation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69386) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), December 26, 2018

## 2020 ...

- [Xiangqi chess engine in javascript - YouTube tutorial series](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76400) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 24, 2021
- [Did anyone write a xiangqi chess engine?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76391) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 27, 2021
- [Chinese chess Xiangqi perft results](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76430) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 27, 2021 » [Chinese Chess Perft Results](Chinese_Chess_Perft_Results "Chinese Chess Perft Results")
- [Wukong Xiangqi - Chinese chess engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76464) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 31, 2021
- [SEE test suite for Xiangqi (Chinese chess)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=80642) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), September 08, 2022

## External Links

## Chinese Chess

- [World Xiangqi Federation](http://www.wxf.org/xq/in.htm)
- [Xiangqi from Wikipedia](https://en.wikipedia.org/wiki/Xiangqi)
- [Xiangqi: Chinese Chess](http://www.chessvariants.com/xiangqi.html) from [The Chess Variant Pages](http://www.chessvariants.com/)
- [How to Play Xiangqi - Chinese Chess](http://ancientchess.com/page/play-xiangqi.htm)
- [Chinese Chess or Xiangqi](http://www.chinasage.info/chess.htm) from [Chinasage](http://www.chinasage.info/index.htm)
- [How XiangQi can improve your chess](https://en.chessbase.com/post/why-you-need-to-learn-xiangqi-for-playing-better-chess) by [Davide Nastasio](https://en.chessbase.com/author/davide-nastasio), [ChessBase](ChessBase "ChessBase"), December 06, 2017
- [rec.games.chinese-chess](https://groups.google.com/forum/#!forum/rec.games.chinese-chess)

## Computer Chinese Chess

- [ICGA: Chinese Chess](http://icga.leidenuniv.nl/icga/games/chinesechess/)
- [Chinese Chess](https://www.game-ai-forum.org/icga-tournaments/game.php?id=13) at the [Computer Olympiad](Computer_Olympiad "Computer Olympiad")
- [Computer Chinese Chess](http://www.iis.sinica.edu.tw/~tshsu/projects/che.html) by [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu")
- [XiangQi (Chinese Chess)](http://home.hccnet.nl/h.g.muller/XQ.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")

[WinBoard and XiangQi](http://home.hccnet.nl/h.g.muller/XQwinboard.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")

- [Chinese Chess Endgame Databases Query System](http://lpforth.forthfreak.net/endgame-en.html) by [Jih Tung Pai](index.php?title=Jih_Tung_Pai&action=edit&redlink=1 "Jih Tung Pai (page does not exist)")
- [中国象棋电脑应用规范(五)：中国象棋通用引擎协议](http://www.xqbase.com/protocol/cchess_ucci.htm) Universal Chinese Chess Protocol (UCCI)
- [电脑象棋联赛 - 象棋百科全书 - Computer Chess League - Chess Encyclopedia](http://www.xqbase.com/league.htm)
- [Discovering Chinese chess Xiangqi to create game engine for it](https://www.youtube.com/watch?v=r3g2wxFLTVY&list=PLmN0neTso3Jw59oLgLUwSTZ_AO_u-pwWt) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), January 22, 2021, [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos

## Source Code

- [GitHub - NeymarL/ChineseChess-AlphaZero: Implement AlphaZero/AlphaGo Zero methods on Chinese chess](https://github.com/NeymarL/ChineseChess-AlphaZero) » [AlphaZero](AlphaZero "AlphaZero")
- [GitHub - maksimKorzh/wukong-xiangqi: Didactic Chinese chess Xiangqi engine](https://github.com/maksimKorzh/wukong-xiangqi) by [Code Monkey King](Maksim_Korzh "Maksim Korzh")

## Xiangqi Cloud Database

- [Xiangqi Cloud Database Query Interface](https://www.chessdb.cn/query_en/) by [noobpwnftw](Bojun_Guo "Bojun Guo")

## References

1. [↑](#cite_ref-1) [Xiangqi from Wikipedia](https://en.wikipedia.org/wiki/Xiangqi)
1. [↑](#cite_ref-2) [Xiang Qi Is Not The Elephant Game](https://groups.google.com/d/msg/rec.games.chinese-chess/gcreEzzU3yQ/HvWOlP7yaYkJ) by Stephen Leary, [rec.games.chinese-chess](Computer_Chess_Forums "Computer Chess Forums"), November 18, 1994
1. [↑](#cite_ref-3) [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Tai-Ning Yang](index.php?title=Tai-Ning_Yang&action=edit&redlink=1 "Tai-Ning Yang (page does not exist)"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2004**) *[Computer Chinese Chess](https://www.researchgate.net/publication/220174553_Computer_Chinese_Chess)*. [ICGA Journal, Vol. 27, No. 1](ICGA_Journal#27_1 "ICGA Journal"), [pdf](https://pdfs.semanticscholar.org/223d/ef59c884503f18610bba314034157f55aacd.pdf)
1. [↑](#cite_ref-4) [How to Play Xiangqi - Chinese Chess](http://ancientchess.com/page/play-xiangqi.htm)
1. [↑](#cite_ref-5) [WXF Notation](http://wxf.ca/xq/computer/wxf_notation.html)
1. [↑](#cite_ref-6) [Xiangqi - Approximate relative values of the pieces - Wikipedia](https://en.wikipedia.org/wiki/Xiangqi#Approximate_relative_values_of_the_pieces)
1. [↑](#cite_ref-7) [Computer Olympiad 2003 in Graz, Austria, November 26](http://www.yss-aya.com/photo/graz2003/1126/index01.html) by [Hiroshi Yamashita](Hiroshi_Yamashita "Hiroshi Yamashita")
1. [↑](#cite_ref-8) Clipped from [Image](http://icga.leidenuniv.nl/icga/news/Olympiad/Olympiad2005/fotos/IMG_0232.JPG) by [Joke Hellemons](Johanna_Hellemons "Johanna Hellemons")
1. [↑](#cite_ref-9) [Photos 2013 Events: day 3](http://icga.org//?page_id=800), [ICGA](ICGA "ICGA")

**[Up one Level](Games "Games")**

