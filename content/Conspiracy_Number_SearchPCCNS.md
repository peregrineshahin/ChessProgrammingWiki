---
title: Conspiracy Number SearchPCCNS
---
**[Home](Home "Home") * [Search](Search "Search") * Conspiracy Number Search**

\[ [Eye of Providence](https://en.wikipedia.org/wiki/Eye_of_Providence) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Conspiracy Number Search**, (CNS, cns)

a [best-first search](Best-First "Best-First") algorithm first described by [David McAllester](David_McAllester "David McAllester") based on [Conspiracy Numbers](Conspiracy_Numbers "Conspiracy Numbers") of the [root](Root "Root") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
[Trees](Search_Tree "Search Tree") are grown in [memory](Memory "Memory") - in an often deep and narrow way - that maximizes the conspiracy required to change the root value.
The phases of the best-first search procedure are **Selection** of a [leaf node](Leaf_Node "Leaf Node"), **Expansion** and **Evaluation** of that leaf, and to **Back-up** the result of that evaluation back to the root.

## Contents

- [1 CNS](#cns)
- [2 CCNS](#ccns)
- [3 PCCNS](#pccns)
- [4 See also](#see-also)
- [5 Chess Programs](#chess-programs)
- [6 Publications](#publications)
  - [6.1 1985 ...](#1985-...)
  - [6.2 1990 ...](#1990-...)
  - [6.3 1995 ...](#1995-...)
  - [6.4 2000 ...](#2000-...)
  - [6.5 2010 ...](#2010-...)
- [7 External Links](#external-links)
- [8 References](#references)

## CNS

CNS maintains a range of possible values and keeps expanding the tree until a certain degree of confidence is reached. The confidence is measured by the width of a possible values’ range **W** and a minimum value for conspiracy numbers **T**. The purpose of the search is to raise the conspiracy numbers of unlikely values to greater than **T** in order to reduce the range of possible values to below **W**. At each turn, CNS tries to disprove either the highest or lowest possible value, which has the highest conspiracy numbers, by expanding one of its conspirators. Then, it recalculates conspiracy numbers and repeats the process until the desired confidence is obtained <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Since **W** depends on the number of possible evaluation values, fine grained evaluation, considered necessary for good positional play, yields into additional computation and thus inefficient search. Further, a final [alpha-beta](Alpha-Beta "Alpha-Beta") [quiescence search](Quiescence_Search "Quiescence Search") in early CNS implementations was quite expensive due to the lack of [bounds](Bound "Bound").

## CCNS

[Ulf Lorenz'](Ulf_Lorenz "Ulf Lorenz") and [Valentin Rottmann's](Valentin_Rottmann "Valentin Rottmann") et al. proposed improvements dubbed **Controlled Conspiracy Number Search** (CCNS) <a id="cite-note-4" href="#cite-ref-4">[4]</a> address the drawbacks of CNS by introducing general **CN Targets** and **Extended Conspiracy Numbers**. CN targets (security demands) are splitted over the successors in order to inform each node about the goal of its examination.
Extended Conspiracy Numbers of the root are defined as the least number of leaf nodes that must change their value in order to change the decision at the root to another move.

## PCCNS

**Parallel Controlled Conspiracy Number Search** (PCCNS) aims at a dynamic distribution of the game tree, initiating a worker/employer relationship along with a sophisticated splitting heuristic of CN targets. The [stack](Stack "Stack"), used to keep the nodes of the best-first search, could be manipulated from outside in order to share work and integrate results from other processors <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## See also

- [Category:CNS](Category:CNS "Category:CNS")
- [Alpha-Beta Conspiracy Search](index.php?title=Alpha-Beta_Conspiracy_Search&action=edit&redlink=1 "Alpha-Beta Conspiracy Search (page does not exist)")
- [Conspiracy Numbers](Conspiracy_Numbers "Conspiracy Numbers")
- [Proof-Number Search](Proof-Number_Search "Proof-Number Search")

## Chess Programs

performing CNS or its improvements:

- [Arachne](Arachne "Arachne") (CNS)
- [P.ConNerS](P.ConNerS "P.ConNerS") (PCCNS)
- [Ulysses](Ulysses "Ulysses") (CCNS)

## Publications

## 1985 ...

- [David McAllester](David_McAllester "David McAllester") (**1985**). *A New Procedure for Growing Minimax Trees*. Technical Report, Artificial Intelligence Laboratory, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- [David McAllester](David_McAllester "David McAllester") (**1988**). *Conspiracy Numbers for Min-Max Search*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 35, No. 1
- [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1988**). *Root Evaluation Errors: How they Arise and Propagate*. [ICCA Journal, Vol. 11, Nos. 2/3](ICGA_Journal#11_23 "ICGA Journal")
- [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1988**). *Parallel Conspiracy-Number Search*. M.Sc. thesis, Faculty of Mathematics and Computer Science, [Vrije Universteit, Amsterdam](https://en.wikipedia.org/wiki/Vrije_Universiteit)
- [Norbert Klingbeil](Norbert_Klingbeil "Norbert Klingbeil") (**1988**). *Search Strategies for Conspiracy Numbers*. M.Sc. thesis
- [Norbert Klingbeil](Norbert_Klingbeil "Norbert Klingbeil"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1988**). *Search Strategies for Conspiracy Numbers.* Canadian Artificial Intelligence Conference, pp. 133-139
- [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *Conspiracy Numbers.* [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5") » [also published in AI](Conspiracy_Numbers#AI "Conspiracy Numbers")
- [Charles Elkan](Charles_Elkan "Charles Elkan") (**1989**). *Conspiracy Numbers and Caching for Searching And/Or Trees and Theorem-Proving*. [IJCAI 1989](Conferences#IJCAI "Conferences"), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-89-VOL1/PDF/054.pdf)

## 1990 ...

- [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1990**). *Conspiracy-Number Search*. [ICCA Journal, Vol. 13, No. 1](ICGA_Journal#13_1 "ICGA Journal")
- [Norbert Klingbeil](Norbert_Klingbeil "Norbert Klingbeil"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1990**). *[Empirical Results with Conspiracy Numbers](https://www.semanticscholar.org/paper/Empirical-results-with-conspiracy-numbers-Klingbeil-Schaeffer/5fc0f8a0901c5e85c04ec813b6e11a7acf32143f).* [Computational Intelligence](<https://en.wikipedia.org/wiki/Computational_Intelligence_(journal)>), Vol. 6
- [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1990**). *Conspiracy Numbers*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 43, No. 1
- [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen"), [Victor Allis](Victor_Allis "Victor Allis"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1990**). *A Comment on `Conspiracy-Number Search`*. [ICCA Journal, Vol. 13, No. 2](ICGA_Journal#13_2 "ICGA Journal")
- [Victor Allis](Victor_Allis "Victor Allis"), [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1991**). *Conspiracy-Number Search.* [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
- [David McAllester](David_McAllester "David McAllester"), [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1993**). *Alpha-Beta Conspiracy Search*. [ps (draft)](http://ttic.uchicago.edu/%7Edmcallester/abc.ps)
- [Lisa Lister](index.php?title=Lisa_Lister&action=edit&redlink=1 "Lisa Lister (page does not exist)"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1994**). *An Analysis of the Conspiracy Numbers Algorithm*. [Computers & Mathematics with Applications](https://en.wikipedia.org/wiki/Computers_and_Mathematics_with_Applications) Vol. 27, No. 1, [Elsevier](https://en.wikipedia.org/wiki/Elsevier), [pdf](http://webdocs.cs.ualberta.ca/%7Ejonathan/publications/ai_publications/icn.pdf)
- [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1994**). *[The Principle of Pressure in Chess](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=EJurXJ4AAAAJ&cstart=40&citation_for_view=EJurXJ4AAAAJ:TQgYirikUcIC)*. TAINN 1994

## 1995 ...

- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann"), [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1995**). *Controlled Conspiracy-Number Search.* [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal")
- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1996**). *Parallel Controlled Conspiracy-Number Search.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**1999**). *Controlled Conspiracy-2 Search*. Technical Report, [Paderborn University](Paderborn_University "Paderborn University")
- [Robin Upton](index.php?title=Robin_Upton&action=edit&redlink=1 "Robin Upton (page does not exist)") (**1999**). *[Dynamic Stochastic Control - A New Approach to Game Tree Searching](http://www.robinupton.com/research/phd/)*. Ph.D. thesis, [University of Warwick](https://en.wikipedia.org/wiki/University_of_Warwick)

## 2000 ...

- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2000**). *[Controlled Conspiracy Number Search](http://digital.ub.uni-paderborn.de/hsmig/content/titleinfo/2460)*. [Paderborn University](Paderborn_University "Paderborn University"), Dissertation, advisor [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (German)
- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2000**). *Controlled Conspiracy-2 Search*. Proceedings of the 17th Annual Symposium on Theoretical Aspects of Computer Science (STACS)
- [David McAllester](David_McAllester "David McAllester"), [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**2002**). *[Alpha-Beta Conspiracy Search](https://www.semanticscholar.org/paper/Alpha-Beta-Conspiracy-Search-McAllester-Yuret/7538bf85b5110207c2925ee8781c69826ad2a425)*. [ICGA Journal, Vol. 25, No. 1](ICGA_Journal#25_1 "ICGA Journal")
- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2002**). *[Parallel Controlled Conspiracy Number Search](https://link.springer.com/chapter/10.1007/3-540-45706-2_57)*. [Euro-Par 2002](https://dblp1.uni-trier.de/db/conf/europar/europar2002.html), [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 2400, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

## 2010 ...

- [Mohd Nor Akmal Khalid](index.php?title=Mohd_Nor_Akmal_Khalid&action=edit&redlink=1 "Mohd Nor Akmal Khalid (page does not exist)"), [Umi Kalsom Yusof](index.php?title=Umi_Kalsom_Yusof&action=edit&redlink=1 "Umi Kalsom Yusof (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)") (**2015**). *[Critical Position Identification in Games and Its Application to Speculative Play](https://www.researchgate.net/publication/281152992_Critical_Position_Identification_in_Games_and_Its_Application_to_Speculative_Play)*. [ICAART 2015](http://www.scitepress.org/DigitalLibrary/ProceedingsDetails.aspx?ID=+mGlly8Sp00=&t=1)
- [Mohd Nor Akmal Khalid](index.php?title=Mohd_Nor_Akmal_Khalid&action=edit&redlink=1 "Mohd Nor Akmal Khalid (page does not exist)"), [E. Mei Ang](index.php?title=E._Mei_Ang&action=edit&redlink=1 "E. Mei Ang (page does not exist)"), [Umi Kalsom Yusof](index.php?title=Umi_Kalsom_Yusof&action=edit&redlink=1 "Umi Kalsom Yusof (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)") (**2015**). *[Identifying Critical Positions Based on Conspiracy Numbers](http://link.springer.com/chapter/10.1007%2F978-3-319-27947-3_6)*. [Agents and Artificial Intelligence](http://link.springer.com/book/10.1007/978-3-319-27947-3), [ICAART 2015 - Revised Selected Papers](http://dblp.uni-trier.de/db/conf/icaart/icaart2015s.html#KhalidAYII15)
- [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2015**). *[Sibling Conspiracy Number Search](https://www.aaai.org/ocs/index.php/SOCS/SOCS15/paper/view/11040)*. [SoCS 2015](https://en.wikipedia.org/wiki/Symposium_on_Combinatorial_Search)
- [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2016**). *[Conspiracy number search with relative sibling scores](https://www.sciencedirect.com/science/article/pii/S0304397516302729)*. [Theoretical Computer Science](<https://en.wikipedia.org/wiki/Theoretical_Computer_Science_(journal)>), Vol. 644
- [Quang Vu](index.php?title=Quang_Vu&action=edit&redlink=1 "Quang Vu (page does not exist)"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)"), [Jean-Christophe Terrillon](index.php?title=Jean-Christophe_Terrillon&action=edit&redlink=1 "Jean-Christophe Terrillon (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2016**). *Using Conspiracy Numbers for Improving Move Selection in Minimax Game-Tree Search*. [ICAART 2016](http://www.icaart.org/?y=2016), [pdf](https://pdfs.semanticscholar.org/1bcf/bd2047bc1d74affda11bf2007cac442dd6f4.pdf)
- [Zhang Song](index.php?title=Zhang_Song&action=edit&redlink=1 "Zhang Song (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2018**). *Using single conspiracy number for long term position evaluation*. [CG 2018](CG_2018 "CG 2018"), [ICGA Journal, Vol. 40, No. 3](ICGA_Journal#40_3 "ICGA Journal")

## External Links

- [Conspiracy from Wikipedia](https://en.wikipedia.org/wiki/Conspiracy)
- [Conspiracy (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Conspiracy_(disambiguation)>)
- [Conspiracy (board game) from Wikipedia](<https://en.wikipedia.org/wiki/Conspiracy_(board_game)>)
- [Jeanne Lee](Category:Jeanne_Lee "Category:Jeanne Lee") - Sundance, [Conspiracy](https://www.discogs.com/de/Jeanne-Lee-Conspiracy/release/687632) (1975), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

feat.: [Jack Gregg](https://fr.wikipedia.org/wiki/Jack_Gregg), [Mark Whitecage](https://en.wikipedia.org/wiki/Mark_Whitecage), [Steve McCall](<https://en.wikipedia.org/wiki/Steve_McCall_(drummer)>), [Gunter Hampel](Category:Gunter_Hampel "Category:Gunter Hampel"), [Sam Rivers](https://en.wikipedia.org/wiki/Sam_Rivers), [Marty Cook](https://en.wikipedia.org/wiki/Marty_Cook)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The [Eye of Providence](https://en.wikipedia.org/wiki/Eye_of_Providence) can be seen on the reverse of the [Great Seal of the United States](https://en.wikipedia.org/wiki/Great_Seal_of_the_United_States), seen here on the [US $1 bill](https://en.wikipedia.org/wiki/United_States_one-dollar_bill). Popular among [conspiracy theorists](https://en.wikipedia.org/wiki/Conspiracy_theory) is the claim that the Eye of Providence shown atop an unfinished pyramid on the Great Seal of the United States indicates the influence of [Freemasonry](https://en.wikipedia.org/wiki/Freemasonry) in the [founding of the United States](https://en.wikipedia.org/wiki/Founding_Fathers_of_the_United_States), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [David McAllester](David_McAllester "David McAllester") (**1985**). *A New Procedure for Growing Minimax Trees*. Technical Report, Artificial Intelligence Laboratory, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Quang Vu](index.php?title=Quang_Vu&action=edit&redlink=1 "Quang Vu (page does not exist)"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)"), [Jean-Christophe Terrillon](index.php?title=Jean-Christophe_Terrillon&action=edit&redlink=1 "Jean-Christophe Terrillon (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2016**). *Using Conspiracy Numbers for Improving Move Selection in Minimax Game-Tree Search*. [ICAART 2016](http://www.icaart.org/?y=2016), [pdf](https://pdfs.semanticscholar.org/1bcf/bd2047bc1d74affda11bf2007cac442dd6f4.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann"), [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1995**). *Controlled Conspiracy-Number Search.* [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1996**). *Parallel Controlled Conspiracy-Number Search.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")

**[Up one level](Search "Search")**

