---
title: Type A Strategy
---
**[Home](Home "Home") \* [Search](Search "Search") \* Type A Strategy**


The **Type A Strategy** was coined in 1949 by [Claude Shannon](Claude_Shannon "Claude Shannon") in his groundbreaking publication *Programming a Computer for Playing Chess* <a id="cite-note-1" href="#cite-ref-1">[1]</a> as a [brute-force](Brute-Force "Brute-Force") strategy, which Shannon concluded would be both slow and a weak player, due to the [average branching factor](Branching_Factor "Branching Factor") and the huge exponential explosion. He therefor favored to search only a small subset of plausible moves within a [Type B strategy](Type_B_Strategy "Type B Strategy"). However, with the advent of [alpha-beta](Alpha-Beta "Alpha-Beta") and all its enhancement, brute-force got very successful from the 70s until present, since the task of classifying and excluding "not plausible" moves, turned out to be quite difficult and error-prone.



### Contents


* [1 Quotes](#quotes)
* [2 See also](#see-also)
* [3 External Links](#external-links)
* [4 References](#references)






from Shannon's *Programming a Computer for Playing Chess*:




```C++
A two-move strategy (based on considering all variations out to 2 moves) is given by

```


```C++

  Max  Min   Max    Min    f(M_ijkl M_ijk M_ij M_i P)
  M_i  M_ij  M_ijk  M_ijkl                                 . . . . (1)

```


```C++
A strategy of this sort, in which all variations are considered out to a definite number of moves and the move then determined form a formula such as will be called type A strategy. The type A strategy has certain basic weaknesses, which we will discuss later, but is conceptually simple, and we will first show how a computer can be programmed for such a strategy.

```


```C++
Unfortunately a machine operating according to the type A strategy would be both slow and a weak player. It would be slow since even if each position were evaluated in one microsecond (very optimistic) there are about 10^9 evaluations to be made after three moves (for each side). Thus, more than 16 minutes would be required for a move, or 10 hours for its half of a 40-move game.

```

## See also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Brute-Force](Brute-Force "Brute-Force")
* [Minimax](Minimax "Minimax")
* [Shannon's Type B Strategy](Type_B_Strategy "Type B Strategy")


## External Links


* [Subject: brute-force vs. intuition in math & chess](http://www.mathematik.uni-bielefeld.de/%7Esillke/NEWS/brute-force) by [Bill Dubuque](https://en.wikipedia.org/wiki/Macsyma), August 1996
* [Brute-force search from Wikipedia](https://en.wikipedia.org/wiki/Brute-force_search)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf)

**[Up one Level](Search "Search")**







 
