---
title: Type B Strategy
---
**[Home](Home "Home") \* [Search](Search "Search") \* Type B Strategy**


The **Type B Strategy**, proposed in 1949 by [Claude Shannon](Claude_Shannon "Claude Shannon") in his groundbreaking publication *Programming a Computer for Playing Chess* <a id="cite-note-1" href="#cite-ref-1">[1]</a>, is a [selective](Selectivity "Selectivity") approach to search [minimax](Minimax "Minimax") [trees](Search_Tree "Search Tree") considering only a subset of plausible moves in contrast to the [brute-force](Brute-Force "Brute-Force") [Type A strategy](Type_A_Strategy "Type A Strategy").



### Contents


* [1 Quotes](#quotes)
* [2 Type B programs](#type-b-programs)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
* [6 References](#references)






from Shannon's *Programming a Computer for Playing Chess*:




```
From these remarks it appears that to improve the speed and strength of play the machine must:

```

1. `Examine forceful variations out as far as possible and evaluate only at reasonable positions, where some quasi-stability has been established.`
2. `Select the variations to be explored by some process so that the machine does not waste its time in totally pointless variations.`



```
A strategy with these two improvements will be called a type B strategy. It is not difficult to construct programs incorporating these features. For the first we define a function g(P) of a position which determines whether approximate stability exists (no pieces en prise, etc.). A crude definition might be:

```


```

                | 1 if any piece is attacked by a piece of lower value,
     g(P) =    /    or by more pieces then defences of if any check exists
               \    on a square controlled by opponent.
                | 0 otherwise.

```


```
Using this function, variations could be explored until g(P)=0, always, however, going at least two moves and never more say, 10.

```

## Type B programs


Most early chess programs were Type B and used a selective **width** for a maximum amount of plausible moves to be tried. [Bernstein](Alex_Bernstein "Alex Bernstein") used {7, 7, 7, 7}, later programs chose width dependent from [depth](Depth "Depth"), [Kotok-McCarthy](Kotok-McCarthy-Program "Kotok-McCarthy-Program") had {4, 3, 2, 2, 1, 1, 1, 1, 0, 0}, while [Greenblatt's](Richard_Greenblatt "Richard Greenblatt") [Mac Hack](Mac_Hack "Mac Hack") used {15, 15, 9, 9, 7, ...}, and [CHAOS](CHAOS "CHAOS") carried out a selective search with iterative widening. With the advent of brute-force [alpha-beta](Alpha-Beta "Alpha-Beta"), and programs like [Tech](Tech "Tech"), [Kaissa](Kaissa "Kaissa") and [Chess 4.5](Chess_(Program) "Chess (Program)") in the early 70s, the era of the former dominating Type B programs drew to a close. Today most programs are closer to Type A, but have some characteristics of a Type B due to [selectivity](Selectivity "Selectivity").


  




* [Awit](Awit "Awit")
* [Black Knight](Black_Knight "Black Knight")
* [Blitz](Blitz "Blitz")
* [CHAOS](CHAOS "CHAOS")
* [Chess Simulator](Chess_Simulator "Chess Simulator")
* [Coko](Coko "Coko")
* [Genie](Genie "Genie")
* [Kotok-McCarthy-Program](Kotok-McCarthy-Program "Kotok-McCarthy-Program")
* [Mac Hack](Mac_Hack "Mac Hack")
* [MAX (Gillogly)](MAX_(Gillogly) "MAX (Gillogly)")
* [NSS](NSS "NSS")
* [Schach (US)](Schach_(US) "Schach (US)")
* [The Bernstein Chess Program](The_Bernstein_Chess_Program "The Bernstein Chess Program")


and



* [Chess < 4.0](Chess_(Program) "Chess (Program)")


## See also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Brute-Force](Brute-Force "Brute-Force")
* [Minimax](Minimax "Minimax")
* [Selectivity](Selectivity "Selectivity")
* [Shannon's Type A Strategy](Type_A_Strategy "Type A Strategy")


## Forum Posts


* [B strategy is the future](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68823) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [CCC](CCC "CCC"), November 04, 2018
* [Which of the many chess engines in this forum use b strategy ?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75287) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [CCC](CCC "CCC"), October 03, 2020


 [Re: Which of the many chess engines in this forum use b strategy ?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75287&start=48) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), October 08, 2020
## External Links


* [Subject: brute-force vs. intuition in math & chess](http://www.mathematik.uni-bielefeld.de/%7Esillke/NEWS/brute-force) by [Bill Dubuque](https://en.wikipedia.org/wiki/Macsyma), August 1996
* [Brute-force search from Wikipedia](https://en.wikipedia.org/wiki/Brute-force_search)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf)

**[Up one Level](Search "Search")**







 
