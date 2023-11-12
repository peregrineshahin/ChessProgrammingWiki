---
title: Mr. Turk
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Mr. Turk**



[ The Turk <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Mr. Turk**,  

an early chess program by primary authors [Gary Boos](Gary_Boos "Gary Boos") and [James Mundstock](James_Mundstock "James Mundstock") at [University of Minnesota](University_of_Minnesota "University of Minnesota"), written in [Fortran](Fortran "Fortran") to run on a [CDC 6600](CDC_6600 "CDC 6600"). Mr. Turk participated in the [ACM's Second North American Computer-Chess Championship](ACM_1971 "ACM 1971") 1971. It did not use [alpha-beta](Alpha-Beta "Alpha-Beta"), but a search based on a *Multipurpose, Theorem-Proving Heuristic Program* as described by [James R. Slagle](James_R._Slagle "James R. Slagle") and [Philip Bursky](Philip_Bursky "Philip Bursky") in 1968 <a id="cite-note-2" href="#cite-ref-2">[2]</a> . 



### Contents


* [1 Description](#description)
* [2 See also](#see-also)
* [3 External Links](#external-links)
* [4 References](#references)






by [Gary Boos](Gary_Boos "Gary Boos") from [Ben Mittman's](Ben_Mittman "Ben Mittman") 1971 Panel <a id="cite-note-3" href="#cite-ref-3">[3]</a> :




```C++
Since late 1967 [James Mundstock](James_Mundstock "James Mundstock"), myself, and others, have been working on our chess program, *Mr. Turk*. *Mr. Turk* was developed at the University of Minnesota on a CDC 6600. At almost all times everyone working on the program was both a chess player and a reasonably good FORTRAN programmer. Our main goal has been to produce a program that could win as many chess games as possible. The methods used in striving for this goal have varied from group to group.

```


```C++
Based upon our chess experience (Mundstock is a class B player, and I am an experienced, class A player), we knew that to obtain a winning position, one normally has to outplay the opponent in both the opening and the middle game. Consequently, we concentrated our initial efforts on writing good [evaluation](Evaluation "Evaluation") routines for the [opening](Opening "Opening") and [middlegame](Middlegame "Middlegame"), plus producing routines that supplied [legal moves](Legal_Move "Legal Move"), location of [pinned pieces](Pin "Pin"), which squares are attacked by which pieces, etc. The result was a program that would produce reasonable moves 80 to 90% of the time, with (in effect) a 1-ply level lookahead.

```


```C++
The next major task was to write a lookahead routine and incorporate it into the rest of the program. Existing lookahead routines were not impressive. They tended to have a vast number of limbs in their move tree, and very little evaluation was spent on the positions examined. An experienced human chess player selects variations with an efficiency at least 10 times greater than any pre-1970 program. Mundstock and I felt that any attempt to approach a master's thought process should help in shaping and improving the move tree. The most noticeable difference in previous lookahead routines and a master's analysis is that the master analyzes one and only one line at a time. He seems to try to insure that that line is the best for both sides, and he attempts to analyze it as deeply as his vision and time permit.

```


```C++
Mundstock noticed an article by [Slagle](James_R._Slagle "James R. Slagle") and [Bursky](Philip_Bursky "Philip Bursky") in the Journal of the ACM, that pointed toward an algorithm that seemed better than alpha-beta pruning. Based upon this article, and guided by Mundstock, I wrote a lookahead routine whose main theme is that the best line is analyzed until it is shown that it is no longer the best line.

```


```C++
This process eliminates many common problems that accompany a fixed depth search, one of which is the *[Ostrich Effect](Horizon_Effect "Horizon Effect")* which existed in even [Northwestern University's](Northwestern_University "Northwestern University")  [Chess 3.0](Chess_(Program) "Chess (Program)"). Tests showed that in a small set of positions, *Mr. Turk* could find the main variation on the first try. We believe that the basic theme of our lookahead routine is better than alpha-beta pruning.

```


```C++
Full scale tests of the program revealed serious shortcomings. *Mr. Turk* had only a [fixed width](Type_B_Strategy "Type B Strategy") (5 moves) move tree, and when all of the top 5 moves were bad (often twice a game), the program was forced to play the best of those 5. That is to say, we had no fall-back routine; no panic button to push.

```


```C++
Other weaknesses were: a) the inability to include sacrificial moves in the move tree, b) little endgame capability, and c) only a small opening book. Nevertheless, we challenged five other programs to postal matches. Only Northwestern University was capable of playing. The match was started in late 1970, and Chess 3.2 is presently winning the two game match. Our team has been working on the above weaknesses since September 1970, and also performing a major overhaul on the existing code. We hope to be able to include tactical moves in the move tree, provide a fall-back algorithm, enlarge and improve our [opening book](Opening_Book "Opening Book") and still keep the necessary storage at under 54k.

```


```C++
It is our opinion that existing chess programs have many weaknesses, and that their play is far too often superficial. Almost all programs find it very difficult to win an endgame if positional play is of the essence. Most programs have opening books, but I seriously doubt that any can handle [transpositions](Transposition "Transposition"). I have never seen a program sacrifice material unless either checkmate or a net win of material was within its view. Also (and this is probably the hardest task of all) no program has been able to develop a logical plan of play in a general position. With the aid of other chess players in Minnesota, we have developed a secret weapon for the [Second ACM tournament](ACM_1971 "ACM 1971"), and will attempt to exploit one of these weaknesses.

```


```C++
The Second ACM tournament will be far stronger than the [1970 championship](ACM_1970 "ACM 1970") (how much stronger will be indicated by where Chess 3.5 finishes). The tournament will provide very interesting games, and the panel discussions between chess programmers from across the nation will bring forth new ideas. We must learn all the lessons we can, for next year, the Russians are coming.

```

## See also


* [Iron Fish](Iron_Fish "Iron Fish")
* [Kempelen](Kempelen "Kempelen")
* [The Baron](The_Baron "The Baron")
* [The Turk](The_Turk "The Turk")


## External Links


* [The Turk from Wikipedia](https://en.wikipedia.org/wiki/The_Turk), the historic fake chess-playing machine
* [Ein Türke in Paderborn](https://de.chessbase.com/post/ein-trke-in-paderborn) from [ChessBase Nachrichten](ChessBase "ChessBase") (German)


## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Gaughan's](https://en.wikipedia.org/wiki/John_Gaughan) reconstructed Turk, [Source image](http://www.grg.org/images/TurkSColes.jpg) with [L. Stephen Coles](L._Stephen_Coles "L. Stephen Coles"): This is a derivative, released under the [GFDL](https://en.wikipedia.org/wiki/GNU_Free_Documentation_License) and [CC](https://en.wikipedia.org/wiki/Creative_Commons), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [James R. Slagle](James_R._Slagle "James R. Slagle"), [Philip Bursky](Philip_Bursky "Philip Bursky") (**1968**). *Experiments With a Multipurpose, Theorem-Proving Heuristic Program*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 15, No. 1
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Ben Mittman](Ben_Mittman "Ben Mittman") (**1971**). *[Computer Chess Programs (Panel)](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d1ee8)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-3.computer_chess_panel.mittman/3-1%20and%203-3.computer_chess_panel.mittman_etc.1971.ACM.062303021.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")

**[Up one level](Engines "Engines")**







 
