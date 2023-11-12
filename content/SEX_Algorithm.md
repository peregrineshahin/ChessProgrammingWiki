---
title: SEX Algorithm
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* SEX Algorithm**



[ Life cycle of sexually reproducing organisms <a id="cite-note-1" href="#cite-ref-1">[1]</a>
The **SEX Algorithm** was a proposal by [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton") and [Mark Taylor](Mark_Taylor "Mark Taylor") to apply [fractional extensions](Extensions#FractionalExtensions "Extensions") and [reductions](Reductions "Reductions"). It was introduced in 1989 in the [ICGA Journal](ICGA_Journal "ICGA Journal") paper *The SEX Algorithm in Computer Chess* (**S**earch **EX**tension), applied in programs and [dedicated computers](Dedicated_Chess_Computers "Dedicated Chess Computers") developed by [Intelligent Software](Intelligent_Software "Intelligent Software") in the 80s. Since "uninteresting moves" were decremented by up to 21 (forward moves) or 24 (backward moves), and the depth increment of the [ID framework](Iterative_Deepening "Iterative Deepening") was 7 or 8, SEX implemented fractional [reductions](Reductions "Reductions") and even a kind of [LMR](Late_Move_Reductions "Late Move Reductions") in [Cyrus 68K](Cyrus_68K "Cyrus 68K"), considering early [non-tactical moves](Quiet_Moves "Quiet Moves") from a evaluated sorted [move list](Move_List "Move List") by a moderate SX decrement, and to determine the SXDEC values for its non-tactical siblings on the basis of their score differences. Forced [tactical moves](Tactical_Moves "Tactical Moves") such as [checks](Check "Check") and [captures](Captures "Captures") were decremented by 3 to 7, and therefor extended by fractions of a ply, while late non-tactical moves were reduced by up to two and some fractional plies. 


Beside static move properties and [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), various other considerations were tried over the years from 1981 until 1988 to improve the algorithm and to distinguish between interesting and uninteresting moves, including [game phase](Game_Phases "Game Phases") (eight phases 0..7), [depth](Depth "Depth"), [Killer heuristic](Killer_Heuristic "Killer Heuristic"), [Parity Pruning](Parity_Pruning "Parity Pruning"), two separate SEX-values for both sides, [Mate threats](Checkmate "Checkmate") and [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance"). 



### Contents


* [1 Excerpts](#excerpts)
	+ [1.1 The Foundation of the Search Algorithm](#the-foundation-of-the-search-algorithm)
	+ [1.2 The Measurement of "Interestingness"](#the-measurement-of-.22interestingness.22)
	+ [1.3 Refinements](#refinements)
	+ [1.4 The Second Generation of the SEX Algorithm](#the-second-generation-of-the-sex-algorithm)
	+ [1.5 The SEX Horizon Effect](#the-sex-horizon-effect)
	+ [1.6 Chipography](#chipography)
* [2 See also](#see-also)
* [3 Publications](#publications)
	+ [3.1 Algorithm](#algorithm)
	+ [3.2 Sex](#sex)
* [4 External Links](#external-links)
* [5 References](#references)






from *The SEX Algorithm in Computer Chess* 1989 <a id="cite-note-2" href="#cite-ref-2">[2]</a> :



### The Foundation of the Search Algorithm


If a path in the [search tree](Search_Tree "Search Tree") consists of the [moves](Moves "Moves") Mi, Mij, Mijk, with the resulting [position](Chess_Position "Chess Position") being a [terminal node](Terminal_Node "Terminal Node"), then




```C++
P(Mi) * P(Mij) * P(Mijk)

```

is the probability that a terminal node in that path is the terminal node in the principal continuation. Therefor




```C++
log[P(Mi)] + log[P(Mij)] + log[P(Mijk)]

```

is an appropriate additive measure for the "interestingness" of the terminal node on this path.



### The Measurement of "Interestingness"


Our first attempts to formalize this idea were in 1981 when one of us ([David Broughton](David_Broughton "David Broughton")) replaced the usual integer depth (which simply controlled the maximum ply depth) with an integer SX. The SX parameter started out at the root node with some positive value, in a similar way to maximum depth, but instead of being decremented by one at each ply it would be decremented by a number determined by the type (or category) of move just made in the tree. When SX was decremented below zero this signaled the end of the search, except for the usual terminal node evaluations.
...
Later we designed a [68000](68000 "68000") program called [Cyrus 68K](Cyrus_68K "Cyrus 68K"), written by one of us ([Mark Taylor](Mark_Taylor "Mark Taylor")), which evaluated and sorted all the moves from a node being expanded: we used these evaluations to determine the SXDEC for moves that were non-tactical. An obvious way to accomplish this is to assign the "best" (i.e., highest-scoring) non-tactical move a low SXDEC and to determine the SXDEC values for its non-tactical siblings on the basis of the difference in score among them.
...



### Refinements


An important development of the idea was to add further categories of a move that depended on the non-swap-off <a id="cite-note-3" href="#cite-ref-3">[3]</a> value of a move in relation to the alpha-beta window. The basic idea was that moves which produced non-swap-off scores that were above the window were considered to be interesting, and it was left to deeper analysis to determine whether of not the move was easily refuted. Although some improvements could be made here, the idea led to control and decision problems at the root, for it violated one of the major principles of the [alpha-beta pruning method](Alpha-Beta "Alpha-Beta"), namely that the value of a move is independent of the window used for its analysis.
...
The early work on SX was designed for a [Z80](Z80 "Z80") based system that was later translated into [6502](6502 "6502") assembler and used in the [Chess Champion MK V](Chess_Champion_Mark_V "Chess Champion Mark V"), a dedicated chess-computer which won the Commercial World Championship for microcomputers at [Travemünde, West Germany, in 1981](WMCCC_1981 "WMCCC 1981"). Most of the refinements discussed above were first "published" with the launch, by [Parker Brothers](https://en.wikipedia.org/wiki/Parker_Brothers), of a program for the [IBM PC](IBM_PC "IBM PC"). <a id="cite-note-4" href="#cite-ref-4">[4]</a> 
...



### The Second Generation of the SEX Algorithm


A second generation of the search extension algorithm was developed during the period 1985-1988. Many of the original ideas were used but we tried to eliminate certain obvious deficiencies and to make the intelligence in the program more sophisticated. We came up with a number of new ideas and tested them in a [68000](68000 "68000")-based program called [Cyrus 68K](Cyrus_68K "Cyrus 68K"). In general the results were rather encouraging, and we now feel that there is no longer a need to be shy about our work, hence the revised acronym for the algorithm and the renaming of the key variables to SEX and SEXDEC.
...



### The SEX Horizon Effect


When looking for a deep combination the program would sometimes terminate the true [principal variation](Principal_Variation "Principal Variation") prematurely as a result of examining uninteresting moves for the defending side. These uninteresting moves would cause big values of SXDEC which would often wipe out all the remaining SX needed by the program to prove the soundness of the combination.


We overcome this problem in the SEX algorithm by using two separate values of SEX, one for each side. If the value of SEX for either side (or for both sides) remains positive then the search continues. This means that a combination will be found even of the defending side makes uninteresting moves, because the attacking side will score a series of low values for SEXDEC. This change produced a clear improvement in the performance of the program.



### Chipography


Since the authors are claiming some originality in the ideas represented in this paper, the following "chipography" is provided. This makes reference to various commercially available chess programs. Anyone doubting our claims as to the date of origination of these ideas should feel free to disassemble the object code in the products and confirm the authors' claims by examining the resulting source code. <a id="cite-note-5" href="#cite-ref-5">[5]</a>



* [Chess Champion Mark V](Chess_Champion_Mark_V "Chess Champion Mark V") - (1981): Dedicated, commercially available chess computer. Manufactured by [Scisys-W Ltd.](Saitek "Saitek"), Hong Kong. [Z80](Z80 "Z80") [development version](Philidor "Philidor") programmed by [Broughton, D.C.](David_Broughton "David Broughton") Program translated to [6502](6502 "6502") [Assembly](Assembly "Assembly") for production version by [Taylor M.](Mark_Taylor "Mark Taylor")
* [Cyrus 68K](Cyrus_68K "Cyrus 68K") - (1986): [68000](68000 "68000") based chess program. Briefly available commercially as the [Sphinx](CXG_Sphinx "CXG Sphinx") manufactured by [Newcrest Technology Ltd.](Newcrest_Technology "Newcrest Technology"), Hong Kong. Programmed in 68000 assembler by [Taylor M.](Mark_Taylor "Mark Taylor")
* [Parker Chess](Parker_Chess "Parker Chess") - (1983): Commercially available chess program on disk for [IBM PC](IBM_PC "IBM PC"). Manufactured by [Parker Brothers Inc., USA](https://en.wikipedia.org/wiki/Parker_Brothers). Programmed in [8086](8086 "8086") assembler by [Broughton, D.C.](David_Broughton "David Broughton")


## See also


* [Fractional Extensions](Extensions#FractionalExtensions "Extensions")
* [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")


## Publications


### Algorithm


* [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")
* [Yoshimasa Tsuruoka](Yoshimasa_Tsuruoka "Yoshimasa Tsuruoka"), [Daisaku Yokoyama](Daisaku_Yokoyama "Daisaku Yokoyama"), [Takashi Chikayama](Takashi_Chikayama "Takashi Chikayama") (**2002**). *[Game-Tree Search Algorithm based on Realization Probability](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.2.9258)*. [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal")
* [David Levy](David_Levy "David Levy") (**2002**). *[SOME COMMENTS ON REALIZATION PROBABILITIES AND THE SEX ALGORITHM](http://ilk.uvt.nl/icga/journal/contents/content25-3.htm#SOME%20COMMENTS%20ON%20REALIZATION%20PROBABILITIES)*. [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal")


### Sex


* [David Levy](David_Levy "David Levy") (**2007**). *[Love and Sex With Robots](https://en.wikipedia.org/wiki/Love_and_Sex_with_Robots): The Evolution of Human-Robot Relationships*. [HarperCollins](https://en.wikipedia.org/wiki/HarperCollins)


## External Links


* [Sex from Wikipedia](https://en.wikipedia.org/wiki/Sex)
* [Sexual reproduction from Wikipedia](https://en.wikipedia.org/wiki/Sexual_reproduction)
* [Evolution of sexual reproduction from Wikipedia](https://en.wikipedia.org/wiki/Evolution_of_sexual_reproduction)
* [Fertilisation from Wikipedia](https://en.wikipedia.org/wiki/Fertilisation)
* [Meiosis from Wikipedia](https://en.wikipedia.org/wiki/Meiosis)
* [Ploidy from Wikipedia](https://en.wikipedia.org/wiki/Ploidy)
* [Sex (book) from Wikipedia](https://en.wikipedia.org/wiki/Sex_%28book%29)
* [Everything You Always Wanted to Know About Sex\* (\*But Were Afraid to Ask) - Wikipedia](https://en.wikipedia.org/wiki/Everything_You_Always_Wanted_to_Know_About_Sex*_%28*But_Were_Afraid_to_Ask%29)
* [James Brown](https://en.wikipedia.org/wiki/James_Brown) - [Sex Machine](https://en.wikipedia.org/wiki/Get_Up_%28I_Feel_Like_Being_a%29_Sex_Machine), 1971, [Rai Storia](https://en.wikipedia.org/wiki/Rai_Storia), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The sexual cycle](https://commons.wikimedia.org/wiki/File:Sexual_cycle.svg), image by [Stannered](http://commons.wikimedia.org/wiki/User:Stannered), March 30, 2007, [Sex from Wikipedia](https://en.wikipedia.org/wiki/Sex) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> The **swap-off value** of a [move](Moves "Moves") is defined by its [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") value.
The **non-swap-off value** of a move is the value of the position arising after that move with no exchanging sequences evaluated
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Parker Chess](Parker_Chess "Parker Chess") developed by [David Broughton](David_Broughton "David Broughton")
 5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [ICCA1989 12 1 part.jpg](http://www.schach-computer.info/wiki/images/5/56/ICCA1989_12_1_part.jpg) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) 

**[Up one level](Selectivity "Selectivity")**







 
