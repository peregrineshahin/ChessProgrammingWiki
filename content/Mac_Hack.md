---
title: Mac Hack
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Mac Hack VI**



 [](File:Machackdisplay02.jpg) Mac Hack [display](Lawrence_J._Krakauer#DEC340 "Lawrence J. Krakauer") <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> 
 [](File:TV-Ocm.png) Mac Hack on bitmapped display 
**Mac Hack VI**, also called **Mac Hack**, **MacHack VI** and the **Greenblatt Chess Program**, 
was a chess program, developed in 1966 and [1967](Timeline#1967 "Timeline") at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") by [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") assisted by [Donald Eastlake](Donald_Eastlake "Donald Eastlake") for a DEC [PDP-6](PDP-6 "PDP-6"). It was developed entirely in [MIDAS](Assembly#MIDAS "Assembly"), the PDP-6 macro assembler. The Greenblatt Chess Program was the first computer program to play chess in human tournament competitions and be granted a chess rating <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



## Hash Table


Mac Hack VI was the first chess program which uses a [transposition table](Transposition_Table "Transposition Table"), but not yet [iterative deepening](Iterative_Deepening "Iterative Deepening"). It regular searched five plies plus [quiescence search](Quiescence_Search "Quiescence Search") and a conditional intermediate layer if own pieces were [en prise](En_prise "En prise").


In his 1970 paper *A New Hashing Method with Application for Game Playing* <a id="cite-note-6" href="#cite-ref-6">[6]</a>, where he introduced [Zobrist hashing](Zobrist_Hashing "Zobrist Hashing"), [Albert Zobrist](Albert_Zobrist "Albert Zobrist") mentions a possible hashing method to obtain an integer which describes the board configuration, and then to [divide](https://en.wikipedia.org/wiki/Division_algorithm) the integer by the hash table size and use the [remainder](https://en.wikipedia.org/wiki/Remainder) as hash address and the [quotient](https://en.wikipedia.org/wiki/Quotient) as key. However, the integer which describes the board may occupy many computer words, and the divide will be complicated and slow. Further the quotient may occupy several words as well, thus most of the transposition table would be occupied by these keys if [type 1 errors](Transposition_Table#KeyCollisions "Transposition Table") were to be avoided. While Zobrist mentions Mac Hack VI used a 32K hash table, he does not made it explicit that Mac Hack used this divide technique. 


More recently, [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), who had a chance to talk with Greenblatt several times, mentioned Mac Hack's hash function used a series of xor operations on occupied squares <a id="cite-note-7" href="#cite-ref-7">[7]</a>. 



## Type B


Inspired by the [Kotok-McCarthy-Program](Kotok-McCarthy-Program "Kotok-McCarthy-Program"), Greenblatt thought he could do better and he succeeded to do so. Mac Hack VI was [Shannon Type B](Type_B_Strategy "Type B Strategy"), but was less narrow than [Kotok-McCarthy's](Kotok-McCarthy-Program#TypeB "Kotok-McCarthy-Program") {4, 3, 2, 2, 1, 1, 1, 1, 0, 0} and used a width of {15, 15, 9, 9, 7, ...} in tournament play. [Quote](Template:Quote_Greenblatt_on_Kotok-McCarthy "Template:Quote Greenblatt on Kotok-McCarthy") by [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") concerning Mac Hack VI from his *Oral History* <a id="cite-note-8" href="#cite-ref-8">[8]</a>:


Most of this printout was analysis from the [Kotok program](Kotok-McCarthy-Program "Kotok-McCarthy-Program"). And I also saw some kind of a textual thing, which I don’t believe was [Kotok’s](Alan_Kotok "Alan Kotok") thesis, but which had some of the same information as Kotok’s thesis. It was probably some kind of a technical report, or something, that was anticipatory to Kotok’s thesis <a id="cite-note-9" href="#cite-ref-9">[9]</a>. Anyway, one of the things I remembered, and which I just talked with Kotok, as a matter of fact, a few days ago, was the detail that they had is [Alpha Beta](Alpha-Beta "Alpha-Beta"), and so forth, and they had these whips, and the whips were set at 4, 4, 3, 3, 2, 2, 1, 1. In other words, that was how many. It would first look at the top ply. It would look at the four best moves. The next plys, it would look at the three best. Next ply, two best, next ply, one best. Well, I just recognized immediately that that was incredibly wrong.


You see, basically looking at only one wide, you just have no signals or noise function. In other words, you look at one move, which you think is the best, but there’s a tremendous amount of noise. Well, you look at some more moves, and if you find that one of those are better, you’ve effectively rejected some noise. Well, essentially the thing that I knew that they did, they were very weak chess players, both [McCarthy](John_McCarthy "John McCarthy") and Kotok. And basically they had a very romanticized view of chess. And so I knew, however, that chess is a very, very precise game. And you really- the name of the game is take the other guy’s pieces, and you don’t just go along. In any kind of a strong game, you don’t just lose pieces, win pieces, lose pieces, win pieces. I mean, if you lose even a single pawn without compensation, then you may have drawing chances, if you’re lucky. Otherwise, the game is lost. Losing more than one pawn almost invariably results in loss of the game, period.



## Opening book


Mac Hack VI incorporated a table of opening positions with selected replies. The [opening book](Opening_Book "Opening Book") was compiled by two MIT students, [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), a chess master and top rated U. S. Junior player, and [Alan Baisley](Alan_Baisley "Alan Baisley") a chess expert. It is noteworthy that Larry Kaufman started his computer chess career over 50 years ago as team member of Mac Hack!
Quote from *Oral History of Richard Greenblatt*:


And it was compacted pretty efficiently. And you know, there was a – by later standards it wasn't so big, but at the time it was pretty good sized. I don't know I think it was probably 8,000 or 10,000 moves in there.
He – Kaufman spent quite a while doing it. Of course, a number of the moves, you know, would – the game would just play it. There was very little chance of it actually staying in the book. You know, the – but I think Kaufman did a good job and he did – we did perceive some of the – well of course, one of the basic things about computer programs, really to the present day, is that they're very tactical. It's much easier for them to see that the tactics than the strategy. So what's called a closed position is hard for a computer. That's where all the pieces are blocking each other and it's very long maneuvering. Whereas, an open position which is sort of tactical combinations is much more to the computer's liking. So therefore, when designing the opening book, you want to kind of play offbeat and kind of unbalanced type openings that tend to lead to these closed position – open positions, which are then good for the computer. And so we realized that and you know, I think Kaufman did a fairly good job of ...



## Matches


### Robert Q


First tournament game by a computer, Carl Wagner (2190) - Mac Hack VI aka "[Robert Q](Template:Robert_Q "Template:Robert Q")", January 21, 1967 <a id="cite-note-10" href="#cite-ref-10">[10]</a>.
"Robert Q", a computer programmed to play chess, was beaten in its first competition with a human, Carl Wagner. The [computer](PDP-6 "PDP-6"), at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") in [Cambridge, Mass.](https://en.wikipedia.org/wiki/Cambridge,_Massachusetts), was operated by Allen Moulton, and [R. William Gosper](Bill_Gosper "Bill Gosper"), while Wagner made his moves several miles away in the YMCU in [Boston](https://en.wikipedia.org/wiki/Boston). The moves were relayed into the computer by teletype operated by [Alan Baisley](Alan_Baisley "Alan Baisley"). "Robert Q" was entered as an experiment, in the monthly [Boylston Chess Club](http://www.boylstonchessclub.org/) Tournament at the [Young Mens Christian Union](https://en.wikipedia.org/wiki/Boston_Young_Men%27s_Christian_Union).



 [](File:RobertQ1967.JPG) 
Allen Moulton and [R. William Gosper](Bill_Gosper "Bill Gosper") operating "[Robert Q](Mac_Hack#RobertQ "Mac Hack")" on a [PDP-6](PDP-6 "PDP-6") <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a>



 [](File:RobertQAlanBaisley1967.JPG) 
Carl Wagner and [Alan Baisley](Alan_Baisley "Alan Baisley") (right) <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a>




```
[Event "Boylston Chess Club Tournament"]
[Site "YMCU, Boston"]
[Date "1967.01.21"]
[Round "1"]
[White "Carl Wagner"]
[Black "Robert Q"]
[Result "1-0"]

1.g3 e5 2.Nf3 e4 3.Nd4 Bc5 4.Nb3 Bb6 5.Bg2 Nf6 6.c4 d6 7.Nc3 Be6 8.d3 exd3
9.Bxb7 Nbd7 10.exd3 Rb8 11.Bg2 O-O 12.O-O Bg4 13.Qc2 Re8 14.d4 c5 15.Be3 cxd4
16.Nxd4 Ne5 17.h3 Bd7 18.b3 Bc5 19.Rad1 Qc8 20.Kh2 Ng6 21.Bg5 Re5 22.Bxf6 gxf6
23.Ne4 f5 24.Nf6+ Kg7 25.Nxd7 Qxd7 26.Nc6 Rbe8 27.Nxe5 Rxe5 28.Qc3 f6 29.Rd3 Re2
30.Rd2 Rxd2 31.Qxd2 Ne5 32.Rd1 Qc7 33.Bd5 Kg6 34.b4 Bb6 35.Qc2 Nc6 36.Be6 Nd4
37.Rxd4 Bxd4 38.Qxf5+ Kg7 39.Qg4+ Kh6 40.Qxd4 Qe7 41.Qh4+ Kg6 42.Bf5+ Kf7 43.Qxh7+
Kf8 44.Qh8+ Kf7 45.Qa8 Qc7 46.Qd5+ Kg7 47.Kg2 Qe7 48.h4 Kh6 49.g4 Kg7 50.h5 Qe2
51.h6+ Kf8 52.h7 Qxf2+ 53.Kxf2 Ke7 54.h8=Q a6 55.Qe6# 1-0

```

### The Dreyfus Match


In 1967 [AI](Artificial_Intelligence "Artificial Intelligence") critic [Hubert Dreyfus](Mathematician#HDreyfus "Mathematician") <a id="cite-note-15" href="#cite-ref-15">[15]</a> <a id="cite-note-16" href="#cite-ref-16">[16]</a> at MIT was challenged by Greenblatt to play a game against his program.
Quote from *Oral History of Richard Greenblatt*:


And so then as word got around- Well, there was a guy a MIT in those days named Hubert Dreyfus, who was a prominent critic of artificial intelligent, and made some statements of the form, you know, computers will never be any good for chess, and so forth. And, of course, he was, again, very romanticized. He was not a strong chess player. However, he thought he was, or I guess he knew was wasn’t world class, but he thought he was a lot better than he was. So anyway, I had this chess program and basically [Jerry Sussman](Mathematician#Sussman "Mathematician"), who’s a professor at MIT now, and who was also a member of our group, had played. It was around and it was available on the machine. People played it, and so forth. And basically Sussman brought over Dreyfus and said, well, how would you like to have a friendly game or something. Dreyfus said, oh, sure. And sure enough, Dreyfus sat down and got beat. So this immediately got quite a bit of publicity.


[Herbert Simon](Herbert_Simon "Herbert Simon"), an AI pioneer, watched the match. He said <a id="cite-note-17" href="#cite-ref-17">[17]</a> :
It was a wonderful game - a real cliffhanger between two woodpushers with bursts of insights and fiendish plans ... great moments of drama and disaster that go in such games.




```
[Event "The Dreyfus Match"]
[Site "MIT"]
[Date "1967.??.??"]
[Round "1"]
[White "Hubert Dreyfus"]
[Black "Mac Hack VI"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Nc3 Bc5 5.d3 O-O 6.Ng5 Na5 7.Bd5 c6 8.Bb3 Nxb3
9.cxb3 h6 10.Nh3 d5 11.exd5 Bg4 12.f3 Bxh3 13.gxh3 Nxd5 14.Nxd5 Qxd5 15.Bd2 Qxd3 16.b4
Be7 17.Rg1 e4 18.fxe4 Bh4+ 19.Rg3 Bxg3+ 20.hxg3 Qxg3+ 21.Ke2 Qxh3 22.Qg1 h5 23.Bc3
g6 24.Qf2 h4 25.Qf6 Qg4+ 26.Kd2 Rad8+ 27.Kc2 Qxe4+ 28.Kb3 Qe6+ 29.Qxe6 fxe6 30.Rh1
Rf4 31.Be1 Rf3+ 32.Ka4 h3 33.b5 Rd4+ 34.b4 cxb5+ 35.Kxb5 Ra3 36.Kc5 Rd5+ 37.Kc4 b5# 0-1

```

### IFIP Match


In August 1968, at the 4th [IFIP](IFIP "IFIP") [conference](Conferences#IFIP "Conferences") held in [Edinburgh](https://en.wikipedia.org/wiki/Edinburgh), Mac Hack running on a [PDP-10](PDP-10 "PDP-10") won an [exhibition match](Lancaster#MacHack "Lancaster") versus [a program](Lancaster "Lancaster") written by [John J. Scott](John_J._Scott "John J. Scott"), running on a [ICL 1909/5](index.php?title=ICL_1900&action=edit&redlink=1 "ICL 1900 (page does not exist)"). The game was analyzed by [Jack Good](Jack_Good "Jack Good"), as published in [Donald Michie's](Donald_Michie "Donald Michie") *Machine Intelligence 4* <a id="cite-note-18" href="#cite-ref-18">[18]</a>.



### ETH-MIT Match


In 1968, [Gerald Tripard](Gerald_Tripard "Gerald Tripard"), postdoc at [ETH Zurich](ETH_Zurich "ETH Zurich") and co-author of the chess program [Charly](Charly "Charly"), asked [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") for a match versus Mac Hack VI. [Three games](Charly#ETHMIT "Charly") were played in October and November 1968 via [ham radio](https://en.wikipedia.org/wiki/Amateur_radio) <a id="cite-note-19" href="#cite-ref-19">[19]</a>, all three won by Mac Hack VI <a id="cite-note-20" href="#cite-ref-20">[20]</a> <a id="cite-note-21" href="#cite-ref-21">[21]</a> <a id="cite-note-22" href="#cite-ref-22">[22]</a>.



### The 70s


Mac Hack was ported to a [PDP-10](PDP-10 "PDP-10") and was the first computer chess program to be widely distributed. It didn't play any [ACM](ACM "ACM") or [ICCA](ICCA "ICCA") tournaments, though. In 1977, Mac Hack played three exhibition games against [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer) <a id="cite-note-23" href="#cite-ref-23">[23]</a>. In 1978, Mac Hack (dubbed Machack) played a match versus the readers of the [Computerwoche](Computerworld#Woche "Computerworld"), a German weekly computer magazine affiliated with the [International Data Group](https://en.wikipedia.org/wiki/IDG), one move per week <a id="cite-note-24" href="#cite-ref-24">[24]</a> <a id="cite-note-25" href="#cite-ref-25">[25]</a> <a id="cite-note-26" href="#cite-ref-26">[26]</a> :




```
[Event "Schach dem Computer"]
[Site "Computerwoche"]
[Date "1978"]
[Round "?"]
[White "CW-Leser"]
[Black "Machack"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Be7 7.h3 O-O 8.O-O Nc6
9.Nc3 Nxc3 10.bxc3 Be6 11.Bf4 Re8 12.Re1 Qd7 13.Rb1 Rab8 14.Ng5 Bf5 15.Qh5 Bxg5
16.Qxg5 Rxe1+ 17.Rxe1 Be6 18.Qg3 Rc8 19.Bh6 g6 20.Qh4 f5 21.Qf6 Nxd4 22.cxd4 c6 1-0

```

## CHEOPS


*see main article [CHEOPS](CHEOPS "CHEOPS")*


In the end of the 70s a [brute force](Brute-Force "Brute-Force") version of Mac Hack was ported to the Chess-orientated Processing System [CHEOPS](CHEOPS "CHEOPS") <a id="cite-note-27" href="#cite-ref-27">[27]</a> , one of the first dedicated hardware approaches in computer chess, which original conception and hardware design was instrumented by [Edward Fredkin](Edward_Fredkin "Edward Fredkin"). Unfortunately it never competed against other programs of that time.



## See also


* [CHEOPS](CHEOPS "CHEOPS")
* [Kotok-McCarthy-Program](Kotok-McCarthy-Program "Kotok-McCarthy-Program")


## Publications


* [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *[The Greenblatt Chess Program](https://www.computerhistory.org/chess/doc-431614f6c7a98/)*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), [pdf](https://d1yx3ys82bpsa0.cloudfront.net/chess/the-greenblatt-chess-program.greenblatt-eastlake-crocker.1967.fall-joint-computer-conference.062303060.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") or as [pdf or ps](http://dspace.mit.edu/handle/1721.1/6176) from [DSpace](http://libraries.mit.edu/dspace-mit/) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
* [L. Stephen Coles](L._Stephen_Coles "L. Stephen Coles") (**1967**). *Memorandum - Chess at Carnegie Tech*. [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=41937) <a id="cite-note-28" href="#cite-ref-28">[28]</a> <a id="cite-note-29" href="#cite-ref-29">[29]</a>
* [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") et al. (**197?**). *Greenblatt Program Info*. (draft) [pdf](https://github.com/larsbrinkhoff/its-archives/blob/master/ailab/Greenblatt.pdf) hosted by [Lars Brinkhoff](User:Larsbrinkhoff "User:Larsbrinkhoff")
* [Paul Rushton](Paul_Rushton "Paul Rushton"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1973**). *Current Chess Programs: A Summary of their Potential and Limitations*. INFOR Journal of the Canadian Information Processing Society Vol. 11, No. 1, [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Rushton-Marsland-Feb73.pdf)
* [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1975**). *Computer Chess*. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press), New York, N.Y.


 Chapter IV. The Greenblatt Chess Program
* [John Moussouris](John_Moussouris "John Moussouris"), [Jack Holloway](Jack_Holloway "Jack Holloway"), [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") (**1979**). *[CHEOPS: A Chess-orientated Processing System](http://portal.acm.org/citation.cfm?id=61701.67028)*. [Machine Intelligence 9](http://www.doc.ic.ac.uk/~shm/MI/mi9.html) ([Jean Hayes Michie](Jean_Hayes_Michie "Jean Hayes Michie"), [Donald Michie](Donald_Michie "Donald Michie") and L.I. Mikulich editors) Ellis Horwood, Chichester, 1979, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")


## Forum Posts


* [Another reason for Fischer's reappearance?](https://groups.google.com/d/msg/rec.games.chess/Lt5J3167kNE/K2qJR_yH5mQJ) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 10, 1992
* [Re: Berliner vs. Botvinnik Some interesting points](https://groups.google.com/d/msg/rec.games.chess.computer/JZ-_0rObjuQ/Mfwy9qBLxoAJ) by [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 06, 1996 » [Transposition Table](Transposition_Table "Transposition Table") in Mac Hack
* [Re: backward thinking & checking your work](https://groups.google.com/d/msg/rec.games.chess.computer/ngtMXXkWA6w/yp2Dei00Dj8J) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 13, 1998
* [Fischer vs. MIT's Greenblatt program, 1978](https://groups.google.com/d/msg/rec.games.chess.computer/W5CUj2B77MY/J8mplRhRNbMJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 27, 1999
* [More Fischer v Greenblatt](https://groups.google.com/d/msg/rec.games.chess.computer/q8r3kvLk3QU/rAoZJCtVOiYJ) by scorsi, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 28, 1999
* [Re: What Chess programs existed in the '60s?](https://www.stmintz.com/ccc/index.php?id=105974) by [David Blackman](David_Blackman "David Blackman"), [CCC](CCC "CCC"), April 13, 2000
* [MacHack VI](https://www.stmintz.com/ccc/index.php?id=445924) by kaqs, [CCC](CCC "CCC"), August 28, 2005
* [MacHack under PDP-10 emulation](http://www.talkchess.com/forum/viewtopic.php?t=37938) by [Ian Osgood](Ian_Osgood "Ian Osgood"), [CCC](CCC "CCC"), February 03, 2011


## External Links


* [Mac Hack from Wikipedia](https://en.wikipedia.org/wiki/MacHack_%28chess%29)
* [Opening Moves: Origins of Computer Chess, Getting Going](http://www.computerhistory.org/chess/main.php?sec=thm-42b86c2029762&sel=thm-42b86c7bdbaf1) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [CHESS HOW Printout - 1979 · Maynard Historical Society Archives](http://collection.maynardhistory.org/items/show/5459)
* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-30" href="#cite-ref-30">[30]</a>
* [Mac Hack Attack](http://www.chess.com/article/view/machack-attack) by [Bill Wall](index.php?title=Bill_Wall&action=edit&redlink=1 "Bill Wall (page does not exist)"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), May 13, 2008
* [Mac Hack VI competes](http://ljkrakauer.com/LJK/60s/machack.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
* [Chess stories](http://ljkrakauer.com/LJK/60s/chess1.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
* [I resign](http://ljkrakauer.com/LJK/60s/resign.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
* [Computer chess via ham radio](http://ljkrakauer.com/LJK/60s/hamchess.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
* [Boylston Chess Club Weblog: Bill Buckner & Ben Landy...All is Forgiven](http://boylston-chess-club.blogspot.com/2008/08/bill-buckner-ben-landy-all-is-forgiven.html)
* [Chess and Canada](http://web.archive.org/web/20091026180259/http://geocities.com/rookknightrook/ChessArticlesDavidCohen.htm#A0507%7CComputer) by [David Cohen](http://web.archive.org/web/20091026180259/http://geocities.com/rookknightrook/ChessArticlesDavidCohen.htm), 2005 - covers Phil Haley - Dataline PDP-10 (MacHack 7)
* [63-chess.mp4](http://projects.csail.mit.edu/video/history/aifilms/63-chess.mp4) hosted by [MIT CSAIL](https://www.csail.mit.edu/)
* [PDP-10/its · GitHub](https://github.com/PDP-10/its/tree/master/src/chprog) (OCM 470 and accompanying files is a 1980 version of Mac Hack) maintained by [Lars Brinkhoff](User:Larsbrinkhoff "User:Larsbrinkhoff") and [Eric Swenson](https://github.com/eswenson1)
* [The Adventure of Chess Programming (Part 2)](https://en.chessbase.com/post/the-adventure-of-chess-programming-part-2) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), February 12, 2019


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [I resign](http://ljkrakauer.com/LJK/60s/resign.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chess stories](http://ljkrakauer.com/LJK/60s/chess1.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> see also [63-chess.mp4](http://projects.csail.mit.edu/video/history/aifilms/63-chess.mp4) hosted by [MIT CSAIL](https://www.csail.mit.edu/)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *The Greenblatt Chess Program*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-4.Greenblatt_Chess_Program/The_Greenblatt_Chess_Program.Greenblatt_Eastlake_Crocker.1967.Fall_Joint_Computer_Conference.062303060.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") or as [or ps](http://dspace.mit.edu/handle/1721.1/6176%7Cpdf)] from [[1]](http://libraries.mit.edu/dspace-mit/%7CDSpace)] at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Mac Hack from Wikipedia](https://en.wikipedia.org/wiki/MacHack_%28chess%29)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Albert Zobrist](Albert_Zobrist "Albert Zobrist") (**1970**). *A New Hashing Method with Application for Game Playing*. Technical Report #88, Computer Science Department, [The University of Wisconsin, Madison](https://de.wikipedia.org/wiki/University_of_Wisconsin%E2%80%93Madison), reprinted (**1990**) in [ICCA Journal, Vol. 13, No. 2](ICGA_Journal#13_2 "ICGA Journal"), [pdf](http://www.cs.wisc.edu/techreports/1970/TR88.pdf)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a>  [Re: What are you allowed to learn from a GPL engine (eg. Stockfish) ?](http://www.talkchess.com/forum3/viewtopic.php?f=10&t=73644&start=50) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 02, 2020 (Engine Origins requires registration)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Oral History of Richard Greenblatt](http://archive.computerhistory.org/resources/text/Oral_History/Greenblatt_Richard/greenblatt.oral_history_transcript.2005.102657935.pdf) (pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Alan Kotok](Alan_Kotok "Alan Kotok") (**1962**). *[Artificial Intelligence Project - MIT Computation Center: Memo 41 - A Chess Playing Program](http://www.kotok.org/AI_Memo_41.html)*. [pdf](ftp://publications.ai.mit.edu/ai-publications/pdf/AIM-041.pdf)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> *[MIT Computer Loses to Human in Chess](http://news.google.com/newspapers?nid=1928&dat=19670123&id=O2ggAAAAIBAJ&sjid=1GYFAAAAIBAJ&pg=2308,2313204)*. [Sun Journal (Lewiston)](https://en.wikipedia.org/wiki/Sun_Journal_%28Lewiston%29), January 23, 1967, [Google News](https://en.wikipedia.org/wiki/Google_News)
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> *[MIT Computer Loses to Human in Chess](https://news.google.com/newspapers?nid=1928&dat=19670123&id=O2ggAAAAIBAJ&sjid=1GYFAAAAIBAJ&pg=2308,2313204&hl=en)*. [Sun Journal (Lewiston)](https://en.wikipedia.org/wiki/Sun_Journal_%28Lewiston%29), January 23, 1967, [Google News](https://en.wikipedia.org/wiki/Google_News)
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> See also [50 years ago “Robert Q”, a computer programmed to play chess, was beaten in its first competition with a human in the monthly Boylston Chess Club Tournament in Boston](https://www.reddit.com/r/chess/comments/5tcwhw/50_years_ago_robert_q_a_computer_programmed_to/). [Reddit](https://en.wikipedia.org/wiki/Reddit)
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *The Greenblatt Chess Program*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31, pp. 808
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> 
[Carl Wagner vs Robert Q from lichess.org](https://lichess.org/kyBnGoLK)
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Hubert L. Dreyfus](Mathematician#HDreyfus "Mathematician") (**1965**). *[Alchemy and Artificial Intelligence](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f691d6d)*. [Rand](https://en.wikipedia.org/wiki/RAND) Paper
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Hubert L. Dreyfus](Mathematician#HDreyfus "Mathematician") (**1972, 1979, 1991**). *[What Computers Can't Do](https://en.wikipedia.org/wiki/What_Computers_Can%27t_Do)*.
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Mac Hack Attack](http://www.chess.com/article/view/machack-attack) by [Bill Wall](index.php?title=Bill_Wall&action=edit&redlink=1 "Bill Wall (page does not exist)"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), May 13, 2008
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Jack Good](Jack_Good "Jack Good") (**1969**). *Analysis of the machine chess game, J. Scott (White), ICL-1900 versus R.D. Greenblatt, PDP-10*. [Machine Intelligence Vol. 4](http://www.doc.ic.ac.uk/~shm/MI/mi4.html)
19. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Computer chess via ham radio](http://ljkrakauer.com/LJK/60s/hamchess.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
20. <a id="cite-ref-20" href="#cite-note-20">↑</a> [The first inter-computer chess game via ham radio](http://ljkrakauer.com/LJK/60s/game1list.htm)
21. <a id="cite-ref-21" href="#cite-note-21">↑</a> [October 30, 1968 letter from Richard Greenblatt to G. Tripard](http://ljkrakauer.com/LJK/60s/greenblattltr.htm)
22. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Games 2 and 3](http://ljkrakauer.com/LJK/60s/games23list.htm)
23. <a id="cite-ref-23" href="#cite-note-23">↑</a> [Greenblatt Chess Program versus Bobby Fischer](http://www.chessgames.com/perl/ezsearch.pl?search=Greenblatt+%28Computer%29) three games played 1977 from [chessgames.com](http://www.chessgames.com/index.html)
24. <a id="cite-ref-24" href="#cite-note-24">↑</a> [Wer setzt Machack matt?](https://www.computerwoche.de/a/wer-setzt-machack-matt,1194734)], January 05, 1978, [Computerwoche](Computerworld#Woche "Computerworld") 1/1978
25. <a id="cite-ref-25" href="#cite-note-25">↑</a> [Schach dem Computer: Ivan Kühnmund (32) wird die Partie "CW-Leser gegen Machack" kommentieren](https://www.computerwoche.de/a/ivan-kuehnmund-32-wird-die-partie-cw-leser-gegen-machack-kommentieren,1194877), January 20, 1978, [Computerwoche](Computerworld#Woche "Computerworld") 4/1978
26. <a id="cite-ref-26" href="#cite-note-26">↑</a> [Schach dem Computer](https://www.computerwoche.de/a/schach-dem-computer,1197292), November 10, 1978, [Computerwoche](Computerworld#Woche "Computerworld") 46/1978
27. <a id="cite-ref-27" href="#cite-note-27">↑</a> [John Moussouris](John_Moussouris "John Moussouris"), [Jack Holloway](Jack_Holloway "Jack Holloway"), [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") (**1979**). *[CHEOPS: A Chess-orientated Processing System](http://portal.acm.org/citation.cfm?id=61701.67028)*. [Machine Intelligence 9](http://www.doc.ic.ac.uk/~shm/MI/mi9.html) ([Jean Hayes Michie](Jean_Hayes_Michie "Jean Hayes Michie"), [Donald Michie](Donald_Michie "Donald Michie") and L.I. Mikulich editors) Ellis Horwood, Chichester, 1979, pp. 351-360, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
28. <a id="cite-ref-28" href="#cite-note-28">↑</a> Letter from [L. Stephen Coles](L._Stephen_Coles "L. Stephen Coles") to [Allen Newell](Allen_Newell "Allen Newell") and [Herbert Simon](Herbert_Simon "Herbert Simon") at [Carnegie Tech](Carnegie_Mellon_University "Carnegie Mellon University") , April 23, 1967 after losing from Mac Hack VI
29. <a id="cite-ref-29" href="#cite-note-29">↑</a> [Bendix G-20 G-21 - Wikipedida](https://en.wikipedia.org/wiki/Bendix_G-20)
30. <a id="cite-ref-30" href="#cite-note-30">↑</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one Level](Engines "Engines")**







 
