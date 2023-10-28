---
title: Search Pathology
---
**[Home](Home "Home") \* [Search](Search "Search") \* Pathology**



[ Micrograph of membranous nephropathy <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Pathology** in game-trees is a counterintuitive phenomenon where a [deeper](Depth "Depth") [minimax](Minimax "Minimax") search results in worse play. It was discovered by [Don Beal](Don_Beal "Don Beal") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, who constructed a simple mathematical model to analyze the minimax algorithm. To his surprise, the analysis of the model showed that the backed-up values were actually somewhat less trustworthy than the heuristic values themselves. 



### Contents


* [1 Decision vs Evaluation](#decision-vs-evaluation)
* [2 Random Evaluations](#random-evaluations)
* [3 See also](#see-also)
* [4 Publications](#publications)
	+ [4.1 1979](#1979)
	+ [4.2 1980 ...](#1980-...)
	+ [4.3 1985 ...](#1985-...)
	+ [4.4 1990 ...](#1990-...)
	+ [4.5 1995 ...](#1995-...)
	+ [4.6 2000 ...](#2000-...)
	+ [4.7 2005 ...](#2005-...)
	+ [4.8 2010 ...](#2010-...)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
* [7 References](#references)






Independently, pathology in game trees was coined by [Dana S. Nau](Dana_S._Nau "Dana S. Nau"), who discovered pathology to exist in a large class of games <a id="cite-note-3" href="#cite-ref-3">[3]</a> under the assumption of independence of sibling values of trees with low branching factor (i.e. binary trees) with game theoretic leaf values of win and loss {1, -1}. In a simulation, Nau introduced strong dependencies between sibling nodes and discovered that this can cause search-depth pathology to disappear. While Nau was primarily concerned with decision accuracy, Beal <a id="cite-note-4" href="#cite-ref-4">[4]</a>, as well as [Bratko](Ivan_Bratko "Ivan Bratko") and [Gams](Matja%C5%BE_Gams "Matjaž Gams") <a id="cite-note-5" href="#cite-ref-5">[5]</a> were concerned with evaluation accuracy.




## Random Evaluations


Quite contrary to pathology in chess, Beal and others demonstrated <a id="cite-note-6" href="#cite-ref-6">[6]</a>, that deeper [search with random leaf values](Search_with_Random_Leaf_Values "Search with Random Leaf Values") yields to better play. As a quintessence, [Dana S. Nau](Dana_S._Nau "Dana S. Nau") et al. suggested an *Error minimizing minimax search* in their recent paper <a id="cite-note-7" href="#cite-ref-7">[7]</a> .



## See also


* [Conspiracy Numbers](Conspiracy_Numbers "Conspiracy Numbers")
* [Depth](Depth "Depth")
* [Diminishing Returns](Depth#DiminishingReturns "Depth")
* [Score Granularity](Score#Grain "Score")
* [Search Instability](Search_Instability "Search Instability")
* [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
* [Singularity and Pathology](Singular_Extensions#SingularityAndPathology "Singular Extensions")


## Publications


### 1979


* [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1979**). *Quality of Decision Versus Depth of Search on Game Trees.* Ph.D. dissertation, [Duke University](Duke_University "Duke University")
* [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1979**). *Preliminary results regarding quality of play versus depth of search in game playing.* First Internat. Symposium on Policy Analysis and Information Systems, [pdf](http://www.cs.umd.edu/%7Enau/papers/nau79preliminary.pdf)


### 1980 ...


* [Don Beal](Don_Beal "Don Beal") (**1980**). *An analysis of minimax*. [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")
* [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1980**). *Pathology on game trees: A summary of results.* In Proceedings of the National Conference on Artificial Intelligence (AAAI), pp. 102–104, [pdf](http://www.cs.umd.edu/%7Enau/papers/pathology-aaai80.pdf)
* [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1982**). *An Investigation of the Causes of Pathology in Games.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 19, 257–278, [University of Maryland, College Park](https://en.wikipedia.org/wiki/University_of_Maryland,_College_Park), Recommended by [Judea Pearl](Judea_Pearl "Judea Pearl"), [pdf](http://www.cs.umd.edu/%7Enau/papers/nau82investigation.pdf)
* [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams") (**1982**). *Error Analysis of the Minimax Principle*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
* [Don Beal](Don_Beal "Don Beal") (**1982**). *Benefits of minimax search*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
* [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1983**). *Decision quality as a function of search depth on game trees.* [Journal of the ACM](ACM#Journal "ACM"), Vol. 30, No. 4, [pdf](http://www.cs.umd.edu/%7Enau/papers/nau83decision.pdf)
* [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1983**). *Pathology on game trees revisited, and an alternative to minimaxing.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 21, No. 1-2, Reprinted in [Judea Pearl](Judea_Pearl "Judea Pearl") (ed.), Search and Heuristics, North-Holland Publishing Company, Amsterdam, [pdf](http://www.cs.umd.edu/%7Enau/papers/nau83pathology.pdf)
* [Judea Pearl](Judea_Pearl "Judea Pearl") (**1983**). *On the Nature of Pathology in Game Searching*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 20
* [Chun-Hung Tzeng](Chun-Hung_Tzeng "Chun-Hung Tzeng"), [Paul W. Purdom](Paul_W._Purdom "Paul W. Purdom") (**1983**). *[A Theory of Game Trees](https://www.aaai.org/Library/AAAI/1983/aaai83-080.php)*. [AAAI-83](Conferences#AAAI-83 "Conferences")


### 1985 ...


* [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1985**). *A Cure for Pathological Behavior in Games that Use Minimax.* [Uncertainty in Artificial Intelligence 1](Laveen_Kanal#Uncertainty_AI_1 "Laveen Kanal"), [arXiv:1304.3444](https://arxiv.org/abs/1304.3444)
* [Agata Muszycka](Agata_Muszycka-Jones "Agata Muszycka-Jones") (**1985**). *[Game Trees: Searching Techniques and Pathological Phenomenon](https://spectrum.library.concordia.ca/3343/)*. Masters thesis, Department of Computer Science, [Concordia University](https://en.wikipedia.org/wiki/Concordia_University), [Montreal](https://en.wikipedia.org/wiki/Montreal)
* [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1986**). *[An Explanation of and Cure for Minimax Pathology](https://www.sciencedirect.com/science/article/pii/B9780444700582500413)*. [Uncertainty in Artificial Intelligence 2](Laveen_Kanal#Uncertainty_AI_2 "Laveen Kanal")
* [Günther Schrüfer](G%C3%BCnther_Schr%C3%BCfer "Günther Schrüfer") (**1986**). *Presence and Absence of Pathology on Game Trees*. [Advances in Computer Chess 4](Advances_in_Computer_Chess_4 "Advances in Computer Chess 4")
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1988**). *Root Evaluation Errors: How they Arise and Propagate*. [ICCA Journal, Vol. 11, Nos. 2/3](ICGA_Journal#11_23 "ICGA Journal")
* [Liwu Li](Liwu_Li "Liwu Li") (**1989**). *[Probabilistic Analysis of Search](https://doi.org/10.7939/R3VX06F26)*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), advisor [Tony Marsland](Tony_Marsland "Tony Marsland")


### 1990 ...


* [Liwu Li](Liwu_Li "Liwu Li"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1990**). *On Minimax Game Tree Search Pathology and Node-value Dependence*. TR90-24, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR90-24.pdf)
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1991**). *On Pathology in Game Tree and other Recursion Tree Models*, Habilitation Thesis (June 1991), Faculty of Mathematics, [University of Bielefeld](https://en.wikipedia.org/wiki/University_of_Bielefeld)
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1994**). *Random Evaluations in Chess*. [ICCA Journal, Vol. 17, No. 1](ICGA_Journal#17_1 "ICGA Journal")
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1994**). *Random Evaluations in Chess*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")


### 1995 ...


* [Mark Levene](Mark_Levene "Mark Levene"), [Trevor Fenner](Trevor_Fenner "Trevor Fenner") (**1995**). *A Partial Analysis of Minimaxing Game Trees with Random Leaf Values*. [ICCA Journal, Vol. 18, No. 1](ICGA_Journal#18_1 "ICGA Journal")
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [Imre Leader](Mathematician#ImreLeader "Mathematician") (**1995**). *[Correlation of Boolean Functions and Pathology in Recursion Trees](http://epubs.siam.org/doi/abs/10.1137/S0895480192240470)*. [SIAM Journal on Discrete Mathematics](https://en.wikipedia.org/wiki/SIAM_Journal_on_Discrete_Mathematics), Vol. 8, No. 4
* [Don Beal](Don_Beal "Don Beal") (**1999**). *The Nature of MINIMAX Search*. Ph.D. thesis, IKAT, ISBN 90-62-16-6348


### 2000 ...


* [Mark Levene](Mark_Levene "Mark Levene"), [Trevor Fenner](Trevor_Fenner "Trevor Fenner") (**2001**). *The Effect of Mobility on Minimaxing of Game Trees with Random Leaf Values*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 130, No. 1, Review in [ICGA Journal, Vol. 24, No. 4](ICGA_Journal#18_1 "ICGA Journal")


### 2005 ...


* [Mitja Luštrek](Mitja_Lu%C5%A1trek "Mitja Luštrek"), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2005**). *Why Minimax Works: An Alternative Explanation*. [IJCAI 2005](Conferences#IJCAI2005 "Conferences"), [pdf](https://www.ijcai.org/Proceedings/05/Papers/1223.pdf)
* [Aleksander Sadikov](Aleksander_Sadikov "Aleksander Sadikov"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Igor Kononenko](Igor_Kononenko "Igor Kononenko") (**2005**). *[Bias and Pathology in Minimax Search](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6V1G-4HCN79X-1&_user=10&_coverDate=12%2F14%2F2005&_rdoc=1&_fmt=high&_orig=search&_sort=d&_docanchor=&view=c&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=79f966215bea9b7461b6877c9373b0bf)*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29),, Vol. 349, 2, [pdf](http://lkm.fri.uni-lj.si/xaigor/slo/clanki/Sadikov_final.pdf)
* [Mitja Luštrek](Mitja_Lu%C5%A1trek "Mitja Luštrek"), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2006**). *Is Real-Valued Minimax Pathological*? [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 170, [pdf](https://dis.ijs.si/MitjaL/documents/Is_Real-Valued_Minimax_Pathological-AIJ-06.pdf)
* [Brandon Wilson](index.php?title=Brandon_Wilson&action=edit&redlink=1 "Brandon Wilson (page does not exist)"), [Austin Parker](Austin_Parker "Austin Parker"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**2009**). *Error Minimizing Minimax: Avoiding Search Pathology in Game Trees*. [pdf](http://www.cs.umd.edu/~nau/papers/wilson2009error.pdf)


### 2010 ...


* [Dana S. Nau](Dana_S._Nau "Dana S. Nau"), [Mitja Luštrek](Mitja_Lu%C5%A1trek "Mitja Luštrek"), [Austin Parker](Austin_Parker "Austin Parker"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams") (**2010**). *[When is it better not to look ahead?](http://www.sciencedirect.com/science/article/pii/S0004370210001402)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 174, No. 16–17, [preprint as pdf](http://dis.ijs.si/mitjal/documents/Nau-When_is_it_better_not_to_look_ahead-AIJ-10.pdf)
* [Mitja Luštrek](Mitja_Lu%C5%A1trek "Mitja Luštrek"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams") (**2011**). *[Independent-valued minimax : Pathological or beneficial?](http://www.sciencedirect.com/science/article/pii/S0304397511009522)* [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol. 422, [pdf](http://dis.ijs.si/MitjaL/documents/Independent-valued_minimax-Pathological_or_beneficial-TCS-12.pdf)
* [Inon Zuckerman](index.php?title=Inon_Zuckerman&action=edit&redlink=1 "Inon Zuckerman (page does not exist)"), [Brandon Wilson](index.php?title=Brandon_Wilson&action=edit&redlink=1 "Brandon Wilson (page does not exist)"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**2018**). *[Avoiding game-tree pathology in 2-player adversarial search](https://onlinelibrary.wiley.com/doi/abs/10.1111/coin.12162)*. [Computational Intelligence](https://en.wikipedia.org/wiki/Computational_Intelligence_(journal)), Vol. 34, No. 2


## Forum Posts


* [Theory: Deeper Search creating worse performance due to PE](https://www.stmintz.com/ccc/index.php?id=476965) by [Charles Roberson](Charles_Roberson "Charles Roberson"), January 04, 2006
* [Pathology on Game trees](http://www.talkchess.com/forum/viewtopic.php?t=35538) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), July 22, 2010
* [Re: Null Move in Quiescent search](http://www.talkchess.com/forum/viewtopic.php?t=58527&start=10) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 10, 2015 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [Quiescence Search](Quiescence_Search "Quiescence Search")


 [Re: Null Move in Quiescent search](http://www.talkchess.com/forum/viewtopic.php?t=58527&start=11) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), December 10, 2015 » [PDS](Proof-Number_Search#PDS "Proof-Number Search")
 [Re: Null Move in Quiescent search](http://www.talkchess.com/forum/viewtopic.php?t=58527&start=16) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 12, 2015
* [random evaluation perturbation factor](http://www.talkchess.com/forum/viewtopic.php?t=63803) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), April 24, 2017


## External Links


* [Pathology (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Pathology_%28disambiguation%29)
* [Pathological (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Pathological_%28mathematics%29)
* [Pathology from Wikipedia](https://en.wikipedia.org/wiki/Pathology)
* [Pathological science from Wikipedia](https://en.wikipedia.org/wiki/Pathological_science)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Very high magnification [micrograph](https://en.wikipedia.org/wiki/Micrograph) of [membranous nephropathy](https://en.wikipedia.org/wiki/Membranous_nephropathy), abbreviated MN. MN may also be referred to as membranous glomerulonephritis, abbreviated MGN. [Kidney biopsy](https://en.wikipedia.org/wiki/Kidney_biopsy). [Jones stain](https://en.wikipedia.org/wiki/Jones_stain), [Pathology from Wikipedia](https://en.wikipedia.org/wiki/Pathology)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Don Beal](Don_Beal "Don Beal") (**1980**). *An analysis of minimax*. [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1982**). *An Investigation of the Causes of Pathology in Games.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 19, 257–278, [University of Maryland, College Park](https://en.wikipedia.org/wiki/University_of_Maryland,_College_Park), Recommended by [Judea Pearl](Judea_Pearl "Judea Pearl"), [pdf](http://www.cs.umd.edu/%7Enau/papers/nau82investigation.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Don Beal](Don_Beal "Don Beal") (**1982**). *Benefits of minimax search*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams") (**1982**). *Error Analysis of the Minimax Principle*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1994**). *Random Evaluations in Chess*. [ICCA Journal, Vol. 17, No. 1](ICGA_Journal#17_1 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Brandon Wilson](index.php?title=Brandon_Wilson&action=edit&redlink=1 "Brandon Wilson (page does not exist)"), [Austin Parker](Austin_Parker "Austin Parker"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**2009**). *Error Minimizing Minimax: Avoiding Search Pathology in Game Trees*. [pdf](http://www.cs.umd.edu/~nau/papers/wilson2009error.pdf)

**[Up one Level](Search "Search")**







 
