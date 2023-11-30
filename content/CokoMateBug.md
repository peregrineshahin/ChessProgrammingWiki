---
title: CokoMateBug
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Coko**

**Coko**, (COKO III)

a chess program by [Dennis Cooper](Dennis_Cooper "Dennis Cooper") and [Ed Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki") which competed the first four [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), [ACM 1970](ACM_1970 "ACM 1970"), [ACM 1971](ACM_1971 "ACM 1971"), [ACM 1972](ACM_1972 "ACM 1972") (**Coko III**) and [ACM 1972](ACM_1972 "ACM 1972") (**Coko IV**). Coko, the Cooper-Kozdrowicki chess program was written in [Fortran](Fortran "Fortran") as a highly selective tree searcher in the spirit of a [Shannon Type B](Type_B_Strategy "Type B Strategy") program using a tree pruning system (TPS) consists of a set of commands designed for programming heuristic tree searches <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## Descriptions

## Abstract

COKO III: The Cooper-Koz Chess Program, [Communications of the ACM](ACM#Communications "ACM"), Vol. 16, 7 <a id="cite-note-2" href="#cite-ref-2">[2]</a>

```C++
COKO III is a chess player written entirely in Fortran. On the [IBM 360-65](IBM_360 "IBM 360"), COKO III plays a minimal chess game at the rate of .2 sec cpu time per move, with a level close to lower chess club play. A selective tree searching procedure controlled by tactical chess logistics allows a deployment of multiple minimal game calculations to achieve some optimal move selection. The tree searching algorithms are the heart of COKO's effectiveness, yet they are conceptually simple. In addition, an interesting phenomenon called a tree searching catastrophe has plagued COKO's entire development just as it troubles a human player. Standard exponential growth is curbed to a large extent by the definition and trimming of the Fisher set. A clear distinction between tree pruning and selective tree searching is also made. Representation of the chess environment is described along with a strategical preanalysis procedure that maps the Lasker regions. Specific chess algorithms are described which could be used as a command structure by anyone desiring to do some chess program experimentation. A comparison is made of some mysterious actions of human players and COKO III.  

```

## Board Representation

Figure 2 from *COKO III: The Cooper-Koz Chess Program* explains COKO's [10x12 Board](10x12_Board "10x12 Board") Chess environment <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

[](https://www.semanticscholar.org/paper/COKO-III%3A-The-Cooper-Koz-Chess-Program-Kozdrowicki-Cooper/8ca0c0f08ba564883b96f6126e2c0c3745fe31e7/figure/1)
[Chess environment representation](Board_Representation "Board Representation"): minimal game board. (a) The chessboard represented by a [linear array](Array "Array").

(b) Representation of [pieces](Pieces "Pieces"), empty [squares](Squares "Squares") and border squares. (c) Move [directions](Direction "Direction") for [King](King "King") and [Queen](Queen "Queen").

(d) The [Knight](Knight "Knight") dictates that two rows of border squares surround the [8 X 8 game board](8x8_Board "8x8 Board").

Columns 10 and 1 are considered adjacent.

## Search

As described by Cooper in the 1971 Panel <a id="cite-note-4" href="#cite-ref-4">[4]</a>, Coko III does not use [Alpha-Beta](Alpha-Beta "Alpha-Beta"):

```C++
Although the alpha-beta procedure is a great time saving method, it is unclear at this stage of program development what the full significance of applying such a method to a tactical-strategical game tree would be. Coko III does save the chess tree with periodic pruning to allow for the addition of more branches. 

```

## Man-Machine Studies

International Journal of Man-Machine Studies <a id="cite-note-5" href="#cite-ref-5">[5]</a>

```C++
The performance capabilities of the best computer chess programs are compared with their human counterparts with emphasis being placed on machine behavior limits. A grandmaster usually spends a lifetime collecting knowledge or information about the game. Some of this knowledge is given to COKO in the form of a 12 000-line FORTRAN program. Using this knowledge COKO plays very poorly but at the super rate of approximately one move/see. The use of a brute-force selective tree-searching procedure yields an order of magnitude improvement in performance at the standard rate of 3 min/move. Perhaps three orders of magnitude additional improvement is needed to defeat the world champion, a gap which must be bridged, if ever, by programming more chess knowledge into the machine. This paper discusses the “tree-searching catastrophe” as a natural phenomenon that plagues selective tree searching for both man and machine. In addition so-called “interminimal-game communication” is considered as a natural, powerful procedure frequently used by humans to guide their selective search and as a point of emphasis for future development. It is concluded that COKO's development is just beginning, with no immediate barriers to progress, and no lack of ideas for improvement. At present COKO combines brilliant solutions to individual board position puzzles with unimaginable blunders. 

```

## Mate in one?

During the [ACM 1971](ACM_1971 "ACM 1971"), Coko III offered a pawn versus [Genie](Genie "Genie") which, if accepted, would permit a mating sequence 17 plies deep. The pawn was taken, mate was announced, and the predicted line was followed, until ... <a id="cite-note-6" href="#cite-ref-6">[6]</a>

<img src="https://lichess1.org/export/fen.gif?fen=8/pp6/2p2p2/6p1/1P6/2Q1P3/k1K2PPP/5B1R w - - 0 38" style="
    width: 300px;
">

```
8/pp6/2p2p2/6p1/1P6/2Q1P3/k1K2PPP/5B1R w - - 0 38 

```

Apparently due to a [bug](Engine_Testing#bugs "Engine Testing"), Coko III found other moves better than mate in one and threw the win ...

```
[Event "ACM 1971"]
[Site "Chicago"]
[Date "1972.08.03"]
[Round "2"]
[White "Coko III"]
[Black "Genie"]
[Result "0-1"]

1.d4 d5 2.Nf3 Nf6 3.Bg5 Bg4 4.Nc3 Ne4 5.Ne5 Be6 6.Nxe4 dxe4 7.c4 Nd7 8.Nxd7 Bxd7 9.e3 f6 
10.Bf4 Be6 11.Qh5+ Kd7 12.d5 Bg8 13.Qf5+ e6 14.dxe6+ Bxe6 15.Qxe4 c6 16.Rd1+ Ke8 17.Rxd8+ 
Kxd8 18.Qxe6 Bb4+ 19.Ke2 Re8 20.Qg4 g6 21.Qh4 g5 22.Qxh7 Be7 23.Qd3+ Kc8 24.Bd6 Kd7 25.Bxe7+ 
Kxe7 26.Qh7+ Ke6 27.Qe4+ Kd6 28.c5+ Kxc5 29.Qd4+ Kb5 30.Kd1+ Ka5 31.b4+ Ka4 32.Qc3 Rad8+ 
33.Kc2 Rd2+ 34.Kxd2 Rd8+ 35.Kc2 Rd2+ 36.Qxd2 Ka3 37.Qc3+ Kxa2 38.Kc1 f5 39.Kc2 f4 40.Kc1 g4 
41.Kc2 f3 42.Kc1 fxg2 43.Kc2 gxh1=Q 44.Kc1 Qxf1+ 45.Kd2 Qxf2+ 46.Kc1 Qg1+ 47.Kc2 Qxh2+ 48.Kc1 
Qh1+ 49.Kc2 Qb1+ 50.Kd2 g3 51.Qc4+ Qb3 52.Qxb3+ Kxb3 53.e4 Kxb4 54.e5 g2 0-1

```

## Mater

According to [Monroe Newborn](Monroe_Newborn "Monroe Newborn") in 1975, the chess [mating](Checkmate "Checkmate") [combinations](Combination "Combination") program [Mater](Mater "Mater") by [George Baylor](George_Baylor "George Baylor") and [Herbert Simon](Herbert_Simon "Herbert Simon"), initially written in [IPL V](http://en.wikipedia.org/wiki/Information_Processing_Language), was ported to [Fortran](Fortran "Fortran") and incorporated into Coko <a id="cite-note-7" href="#cite-ref-7">[7]</a> :

```C++
MATER is written by George Baylor and Simon in FORTRAN. It is able to search to great depths for checkmates. MATER is presently part of the Cooper-Kozdrowicki program. While MATER is an interesting program in its own right, the opportunity to checkmate one's opponent plays a relatively small computational part of the game of chess, and its inclusion in the Cooper-Kozdrowicki program does not seem to add measurably to the program's strength. 

```

## Publications

- [Edward W. Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki"), [John S. Licwinko](http://www.linkedin.com/pub/john-licwinko/15/b07/962), [Dennis W. Cooper](Dennis_Cooper "Dennis Cooper") (**1971**). *[Algorithms for a minimal chess player: A blitz player](http://www.sciencedirect.com/science/article/pii/S0020737371800123)*. [International Journal of Man-Machine Studies, Vol 3, 2](http://www.sciencedirect.com/science?_ob=PublicationURL&_tockey=%23TOC%236830%231971%23999969997%23695565%23FLP%23&_cdi=6830&_pubType=J&view=c&_auth=y&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=d904df3cf14dfeea642d77044a3a9d48)
- [Edward W. Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki"), [Dennis W. Cooper](Dennis_Cooper "Dennis Cooper") (**1973**). *[COKO III: The Cooper-Koz Chess Program](https://www.semanticscholar.org/paper/COKO-III%3A-The-Cooper-Koz-Chess-Program-Kozdrowicki-Cooper/8ca0c0f08ba564883b96f6126e2c0c3745fe31e7)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 16, 7
- [Edward W. Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki"), [Dennis W. Cooper](Dennis_Cooper "Dennis Cooper") (**1973**). *[COKO III and the future of inter-snap judgment communication](http://portal.acm.org/citation.cfm?id=805706)*. Proceedings of the ACM annual conference
- [Paul Rushton](Paul_Rushton "Paul Rushton"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1973**). *Current Chess Programs: A Summary of their Potential and Limitations*. INFOR Journal of the Canadian Information Processing Society Vol. 11, No. 1, [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Rushton-Marsland-Feb73.pdf)
- [Edward W. Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki"), [Dennis W. Cooper](Dennis_Cooper "Dennis Cooper") (**1974**). *[COKO III: The Cooper-Kozdrowicki chess program](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6WGS-4T73MH1-1&_user=10&_coverDate=11%2F30%2F1974&_rdoc=1&_fmt=high&_orig=browse&_srch=doc-info%28%23toc%236830%231974%23999939993%23696079%23FLP%23display%23Volume%29&_cdi=6830&_sort=d&_docanchor=&view=c&_ct=8&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=328130c5073ebaec9fde85ad1660329c).* [International Journal of Man-Machine Studies Vol. 6, 6](http://www.sciencedirect.com/science?_ob=PublicationURL&_tockey=%23TOC%236830%231974%23999939993%23696079%23FLP%23&_cdi=6830&_pubType=J&view=c&_auth=y&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=0e502b85e9d01337a96f6677d4ac3ad4)

## External Links

- [ACM COMPUTER CHESS](http://ed-thelen.org/comp-hist/ACM-ComputerChessWall.html) by [Bill Wall](index.php?title=Bill_Wall&action=edit&redlink=1 "Bill Wall (page does not exist)")
- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-8" href="#cite-ref-8">[8]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Edward W. Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki") (**1968**). *[An adaptive tree pruning system: A language for programming heuristic tree searches](http://portal.acm.org/citation.cfm?id=810637&dl=GUIDE&coll=GUIDE&CFID=85270894&CFTOKEN=84258946)*. Proceedings of the 1968 23rd ACM national conference
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Edward W. Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki"), [Dennis W. Cooper](Dennis_Cooper "Dennis Cooper") (**1973**). *[COKO III: The Cooper-Koz Chess Program](https://www.semanticscholar.org/paper/COKO-III%3A-The-Cooper-Koz-Chess-Program-Kozdrowicki-Cooper/8ca0c0f08ba564883b96f6126e2c0c3745fe31e7)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 16, 7
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Edward W. Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki"), [Dennis W. Cooper](Dennis_Cooper "Dennis Cooper") (**1973**). *[COKO III: The Cooper-Koz Chess Program](https://www.semanticscholar.org/paper/COKO-III%3A-The-Cooper-Koz-Chess-Program-Kozdrowicki-Cooper/8ca0c0f08ba564883b96f6126e2c0c3745fe31e7)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 16, 7, Fig. 2
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Ben Mittman](Ben_Mittman "Ben Mittman") (**1971**). *[Computer Chess Programs (Panel)](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d1ee8)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-3.computer_chess_panel.mittman/3-1%20and%203-3.computer_chess_panel.mittman_etc.1971.ACM.062303021.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Edward W. Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki"), [Dennis W. Cooper](Dennis_Cooper "Dennis Cooper") (**1974**). *[COKO III: The Cooper-Kozdrowicki chess program](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6WGS-4T73MH1-1&_user=10&_coverDate=11%2F30%2F1974&_rdoc=1&_fmt=high&_orig=browse&_srch=doc-info%28%23toc%236830%231974%23999939993%23696079%23FLP%23display%23Volume%29&_cdi=6830&_sort=d&_docanchor=&view=c&_ct=8&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=328130c5073ebaec9fde85ad1660329c).* [International Journal of Man-Machine Studies Vol. 6, 6](http://www.sciencedirect.com/science?_ob=PublicationURL&_tockey=%23TOC%236830%231974%23999939993%23696079%23FLP%23&_cdi=6830&_pubType=J&view=c&_auth=y&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=0e502b85e9d01337a96f6677d4ac3ad4)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [George Atkinson](index.php?title=George_Atkinson&action=edit&redlink=1 "George Atkinson (page does not exist)") (**1998**). *[Chess and Machine Intuition](http://books.google.com/books?id=ZuTvVo4zo6oC&printsec=frontcover&dq=Chess+and+machine+intuition#v=onepage&q&f=false)*. (Intellect Ltd.) pp 63
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1975**). *Computer Chess*. Academic Press, New York, N.Y. p. 26
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one level](Engines "Engines")**

