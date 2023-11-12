---
title: Papa
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Papa**



[ [Papa and Rangi](https://en.wikipedia.org/wiki/Rangi_and_Papa) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Papa**,  

an early computer chess program written by [George Rajna](George_Rajna "George Rajna") and [B. Almasi](index.php?title=B._Almasi&action=edit&redlink=1 "B. Almasi (page does not exist)"), in the 70s affiliated with the [Hungarian Academy of Sciences](https://en.wikipedia.org/wiki/Hungarian_Academy_of_Sciences). Papa applies the concept of [entropy](Papa#Entropy "Papa") based on own and opponent [mobility](Mobility#Papa "Mobility"). It participated at the [First World Computer Chess Championship](WCCC_1974 "WCCC 1974"), 1974 in [Stockholm](https://en.wikipedia.org/wiki/Stockholm), unfortunately loosing all its three games due to tactical blunders. Based on preliminary results or expectations, Papa was seeded third, ahead of later winner [Kaissa](Kaissa "Kaissa") seeded fifth. 






### Contents


* [1 Entropy](#entropy)
	+ [1.1 Rajna](#rajna)
	+ [1.2 Marsland](#marsland)
	+ [1.3 The Merit](#the-merit)
* [2 Binary Logarithm](#binary-logarithm)
* [3 Selected Games](#selected-games)
* [4 See also](#see-also)
* [5 External Links](#external-links)
	+ [5.1 Chess Program](#chess-program)
	+ [5.2 Papa](#papa)
	+ [5.3 Entropy](#entropy-2)
* [6 References](#references)






### Rajna


In 2012, [George Rajna](George_Rajna "George Rajna") has re-published a short paper on [entropy](https://en.wikipedia.org/wiki/Entropy) in chess <a id="cite-note-2" href="#cite-ref-2">[2]</a>, which already appeared in *[The World Computer-Chess Championship](WCCC_1974 "WCCC 1974")* by [Hayes](Jean_Hayes_Michie "Jean Hayes Michie") and [Levy](David_Levy "David Levy") <a id="cite-note-3" href="#cite-ref-3">[3]</a>:




```C++
The basic theory on which one chess program can be constructed is that there exists a general characteristic of the game of chess, namely the concept of entropy. This concept has been employed in physics for a long time. In the case of a [gas](https://en.wikipedia.org/wiki/Gas), it is the [logarithm](https://en.wikipedia.org/wiki/Logarithm) of the number of those [microscopic states](https://en.wikipedia.org/wiki/Microstate_%28statistical_mechanics%29) compatible with the [macroscopic](https://en.wikipedia.org/wiki/Macroscopic_scale) parameters of the gas.

```


```C++
What does this mean in terms of chess? A common characteristic of every [piece](Pieces "Pieces") is that it could move to certain [squares](Squares "Squares"), including by [capture](Captures "Captures"). In any given [position](Chess_Position "Chess Position"), therefore, the pieces by the rules of the game possess certain states, only one of which will be realized on the next move. The difference of the logarithm of the numbers of such states for Black and White respectively is the "entropy of the position". The task of the computer is then to increase this value for its own benefit. 

```

...




```C++
 Entropy is a principle of [statistical physics](https://en.wikipedia.org/wiki/Statistical_physics) and therefore is only applicable in statistical contexts. The number of microstates of a confined gas is very large and therefore the statistical approach is valid. In chess, however, the number of pieces, a macroscopic parameter, is very small and therefore in this context the "value" of a position cannot be an exact function of entropy. For example, it is possible to [checkmate](Checkmate "Checkmate") with a total force of a single pawn despite the fact that the opponent has many pieces and various positions available. 

```

  




### Marsland


[Tony Marsland](Tony_Marsland "Tony Marsland") mentioned Papa and other programs participating the [WCCC 1974](WCCC_1974 "WCCC 1974") in his handwritten notes on the Hayes and Levy book <a id="cite-note-4" href="#cite-ref-4">[4]</a> :




```C++
 [Freedom](Freedom "Freedom") and Papa both use [mobility](Mobility "Mobility") as their primary term in their [evaluation functions](Evaluation_Function "Evaluation Function"). As with [Wita](Awit "Awit"), both use the ratio of computer's moves / opponent moves. Papa and Wita also multiply by the ratio of the [squares controlled](Square_Control "Square Control") and Papa goes one step further and takes the logarithm of this product to form the "entropy" of the position. The true merit of this entropy over the product ratio was not made clear, but it does ensure that in extreme situations the evaluation remains more closely bounded. 

```

### The Merit


The merit of this entropy over the product ratio probably is that it makes a product a sum and a quotient a difference, resulting in [Negamax](Negamax "Negamax") compatible symmetric values around zero in relation to [side to move](Side_to_move "Side to move") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



 [](File:PapaNegaLog.jpg) 
## Binary Logarithm


The definition of the amount of [self-information](https://en.wikipedia.org/wiki/Self-information) and [information entropy](https://en.wikipedia.org/wiki/Entropy_%28information_theory%29) involves the [binary logarithm](https://en.wikipedia.org/wiki/Binary_logarithm). On [x86](X86 "X86") or [x86-64](X86-64 "X86-64"), Log2 (lb) may be applied using [MMX](MMX "MMX") or [SSE2](SSE2 "SSE2") instructions <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>, with vectors of two or four [floats](Float "Float").



 [](File:PapaLog2.jpg) 
[ [8]")




## Selected Games


[WCCC 1974](WCCC_1974 "WCCC 1974"), round 3, Papa - [Ribbit](Ribbit "Ribbit") <a id="cite-note-9" href="#cite-ref-9">[9]</a> :




```

[Event "WCCC 1974"]
[Site "Stockholm, Sweden"]
[Date "1974.08.07"]
[Round "3"]
[White "Papa"]
[Black "Ribbit"]
[Result "0-1"]

1.Nf3 d5 2.d4 Nc6 3.Ne5 Nxe5 4.dxe5 e6 5.e4 dxe4 6.Bb5+ Bd7 7.Bxd7+ Qxd7
8.Qxd7+ Kxd7 9.O-O f5 10.Rd1+ Kc6 11.Be3 Bc5 12.Bxc5 Kxc5 13.Rd7 Nh6
14.Rxc7+ Kb6 15.Rxg7 Ng4 16.f4 exf3 17.gxf3 Nxe5 18.Nd2 Rag8 19.Nc4+ Nxc4
20.Rg6 hxg6 21.Rd1 Rgd8 22.Rxd8 Rxd8 23.a3 Nxb2 24.a4 Nxa4 25.c3 Nxc3
26.f4 Nd5 27.Kf2 Nxf4 28.Kf3 e5 29.h4 Rd4 30.Kg3 Nh5+ 31.Kf2 Rxh4 0-1

```

## See also


* [Eden](Eden "Eden")
* [Gaia](Gaia "Gaia")
* [Genesis](Genesis_AR "Genesis AR") by [Claudio Bollini](Claudio_Bollini "Claudio Bollini")
* [Genesis](Genesis_IL "Genesis IL") by [Eli David](Eli_David "Eli David")
* [Genesis](Genesis_NL "Genesis NL") by [Eric van Riet Paap](Eric_van_Riet_Paap "Eric van Riet Paap")
* [Paradise](Paradise "Paradise")
* [Terra](Terra "Terra")


## External Links


### Chess Program


* [Papa's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=52)
* [The chess games of Papa (Computer)](http://www.chessgames.com/perl/chessplayer?pid=48723) from [chessgames.com](http://www.chessgames.com/index.html)


### Papa


* [Papa (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Papa)
* [Rangi and Papa from Wikipedia](https://en.wikipedia.org/wiki/Rangi_and_Papa)
* [Earth Mother from Wikipedia](https://en.wikipedia.org/wiki/Earth_Mother)
* [Creation myth from Wikipedia](https://en.wikipedia.org/wiki/Creation_myth)
* [Johnny Winter](Category:Johnny_Winter "Category:Johnny Winter") - [Sweet Papa John](https://en.wikipedia.org/wiki/Captured_Live!), September 14, 1975, at [Swing Auditorium](https://en.wikipedia.org/wiki/Swing_Auditorium), [San Bernardino, California](https://en.wikipedia.org/wiki/San_Bernardino,_California), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
### Entropy


* [Entropy from Wikipedia](https://en.wikipedia.org/wiki/Entropy)
* [Entropy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Entropy_%28disambiguation%29)
* [Entropy (statistical thermodynamics) from Wikipedia](https://en.wikipedia.org/wiki/Entropy_%28statistical_thermodynamics%29)
* [Entropy (information theory) from Wikipedia](https://en.wikipedia.org/wiki/Entropy_%28information_theory%29)
* [Entropy in thermodynamics and information theory from Wikipedia](https://en.wikipedia.org/wiki/Entropy_in_thermodynamics_and_information_theory)
* [Principle of maximum entropy from Wikipedia](https://en.wikipedia.org/wiki/Principle_of_maximum_entropy)
* [Maximum entropy probability distribution from Wikipedia](https://en.wikipedia.org/wiki/Maximum_entropy_probability_distribution)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Maori](https://en.wikipedia.org/wiki/M%C4%81ori_culture) carving depicting a woman and a man embracing. From the pataka (food storehouse) belonging to [Te Pokiha Taranui](https://en.wikipedia.org/wiki/Te_Pokiha_Taranui) of [Ngati Pikiao](https://en.wikipedia.org/wiki/Ng%C4%81ti_Pikiao), [Te Arawa](https://en.wikipedia.org/wiki/Te_Arawa). The storehouse was completed in the 1870s, and stood at [Maketu](https://en.wikipedia.org/wiki/Maketu), [Bay of Plenty](https://en.wikipedia.org/wiki/Bay_of_Plenty), [New Zealand](https://en.wikipedia.org/wiki/New_Zealand). It is now at [Auckland Museum](https://en.wikipedia.org/wiki/Auckland_War_Memorial_Museum), [Rangi and Papa from Wikipedia](https://en.wikipedia.org/wiki/Rangi_and_Papa)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [George Rajna](George_Rajna "George Rajna") (**1976, 2012**). *Information – Entropy theory of Artificial Intelligence*. [pdf](http://vixra.org/pdf/1201.0063v1.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Jean E. Hayes](Jean_Hayes_Michie "Jean Hayes Michie"), [David Levy](David_Levy "David Levy") (**1976**). *[The world computer chess championship, Stockholm 1974](http://www.getcited.org/pub/101724802)*. University Press (Edinburgh) ISBN 0852242859
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [wita-awit#19-box2.pdf](http://webdocs.cs.ualberta.ca/~tony/Public/Awit-Wita-ComputerChess/Wita-base/WitaNotes/wita-awit%2319-box2.pdf) from [Wita Notes](http://webdocs.cs.ualberta.ca/~tony/Public/Awit-Wita-ComputerChess/Wita-base/WitaNotes/) by [Tony Marsland](Tony_Marsland "Tony Marsland")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [log(w/b) instead of w-b?](http://www.talkchess.com/forum/viewtopic.php?t=43545) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), May 02, 2012
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Simple SSE and SSE2 optimized sin, cos, log and exp](http://gruntthepeon.free.fr/ssemath/)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Approximate Math Library - Devmaster](http://devmaster.net/forums/topic/6679-approximate-math-library/page__p__39242#entry39242), January 25, 2007
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> Plot of Log2 from [Binary logarithm from Wikipedia](https://en.wikipedia.org/wiki/Binary_logarithm)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Stockholm 1974 - Chess - Round 3 - Game 2 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=7&round=3&id=2)

**[Up one Level](Engines "Engines")**







 
