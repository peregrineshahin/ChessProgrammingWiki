---
title: Paul Wiereyn
---
**[Home](Home "Home") \* [People](People "People") \* Paul Wiereyn**


**Paul H. Wiereyn**,  

a Dutch [chess problem composer](Category:Chess_Composer "Category:Chess Composer") and [chess solving engine](Category:Problem "Category:Problem") and [GUI](GUI "GUI") programmer. 
He is author of a free [Sudoku](https://en.wikipedia.org/wiki/Sudoku) program and the [Windows](Windows "Windows") [GUI](GUI "GUI") [APwin](APwin "APwin") for the chess problem solving programs [Alybadix](Alybadix "Alybadix") and [Popeye](Popeye "Popeye").



### Contents


* [1 0x88](#0x88)
* [2 Selected Publications](#selected-publications)
* [3 External Links](#external-links)
* [4 References](#references)






In his 1985 paper *Inventive Problem Solving* <a id="cite-note-1" href="#cite-ref-1">[1]</a>, Paul Wiereyn described [0x88](0x88 "0x88") coordinates with [nibbles](Nibble "Nibble") for [ranks](Ranks "Ranks") and [files](Files "Files") inside a [byte](Byte "Byte"), and used such [square differences](Vector_Attacks "Vector Attacks") (mod 256) as table-index to determine [pinned pieces](Pin "Pin") and [discovered checks](Discovered_Check "Discovered Check") in his problem solving program:




```
It is obvious to chess-players that a piece when pinned should not be allowed to move out of the direction in which it is pinned. Hence, as a preliminary, we calculate, in one byte, the difference between the coordinates of the piece about to be moved and one's own King, e.g.,

```


```
Rd5 - Kf5 <=> 45 - 65 = E0, hexadecimals and reduction modulo 256 

```


```
being implied throughout.

```


```
The difference, E0 say, serves to enter a table T. The tabular value T[E0] so found, when zero, indicates non-collinearity (the pieces are not on the same rank, file or (co-)diagonal). If not zero, the value codes the direction of collinearity, i.e., the pinning direction. In our example the value T[E0] = F0, stands for due West. 

```

## Selected Publications


<a id="cite-note-2" href="#cite-ref-2">[2]</a>



* Paul Wiereyn (**1985**). *Problem-Solving Ability Tested II*. [ICCA Journal, Vol. 8, No. 3](ICGA_Journal#8_3 "ICGA Journal")
* Paul Wiereyn (**1985**). *Inventive Problem Solving*. [ICCA Journal, Vol. 8, No. 4](ICGA_Journal#8_4 "ICGA Journal")
* Paul Wiereyn (**1997**). *Genius-3 Cooked Endgame Studies*. [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal") » [Chess Genius](Chess_Genius "Chess Genius")


## External Links


* [apwin](https://alybadix.000webhostapp.com/apwin.htm)
* [Chess Composers: March 31st - Paul H. Wiereyn (31-03-1936) Dutch composer](http://chesscomposers.blogspot.com/2012/03/march-31st.html)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Paul Wiereyn (**1985**). *Inventive Problem Solving*. [ICCA Journal, Vol. 8, No. 4](ICGA_Journal#8_4 "ICGA Journal")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [ICGA Reference Database](ICGA_Journal#RefDB "ICGA Journal")

**[Up one level](People "People")**







 
