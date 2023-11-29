---
title: Conspiracy Numbers
---
**[Home](Home "Home") * [Search](Search "Search") * Conspiracy Numbers**

[](File:ACC5Schaeffer.jpg) [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") on *Conspiracy Numbers.* <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Conspiracy Numbers** of the [root](Root "Root") or [interior nodes](Interior_Node "Interior Node") of a [search tree](Search_Tree "Search Tree") for some value **V** are defined as the least number of conspirators, that are [leaves](Leaf_Node "Leaf Node") that must change their evaluation value to **V** in order to change the minimax value of the interior node or root <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Conspiracy Numbers and their possible application for [Minimax](Minimax "Minimax") search within a [best-first search](Best-First "Best-First") algorithm was first described by [David McAllester](David_McAllester "David McAllester") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Sample

## Minimax Tree

A sample minimax tree T with some arbitrary values of the leaves <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```C++
root                    ┌───────┐
max node                │  A=3  │
                        └───────┘
           ┌───────┐                 ┌───────┐
min nodes  │  B=2  │                 │  C=3  │
           └───────┘                 └───────┘
  ┌───────┐       ┌───────┐   ┌───────┐       ┌───────┐
  │  D=5  │       │  E=2  │   │  F=3  │       │  G=4  │
  └───────┘       └───────┘   └───────┘       └───────┘

```

## Conspiracy Numbers

|  Conspiracy numbers for all possible values of the root A
|
| --- |
|  v
|  cn(A, v)
|  conspirators
|
|  \<= 1
|  2
|  (D or E) and (F or G)
|
|  2
|  1
|  (F or G)
|
|  3
|  0
|  none
|
|  4
|  1
|  (E or F)
|
|  5
|  1
|  E
|
|  >= 6
|  2
|  (D and E) or (F and G)
|
|  Conspiracy numbers for all possible values of node B
|
|  v
|  cn(B, v)
|  conspirators
|
|  \<= 1
|  1
|  (D or E)
|
|  2
|  0
|  none
|
|  3,4,5
|  1
|  E
|
|  >= 6
|  2
|  (D and E)
|
|  Conspiracy numbers for all possible values of node C
|
|  v
|  cn(C, v)
|  conspirators
|
|  \<= 2
|  1
|  (F or G)
|
|  3
|  0
|  none
|
|  4
|  1
|  F
|
|  >= 5
|  2
|  (F and G)
|

## Recursive Definition

Following [recursive](Recursion "Recursion") definition in pseudo [C](C "C") is based on [Van der Meulen's](Maarten_van_der_Meulen "Maarten van der Meulen") code <a id="cite-note-5" href="#cite-ref-5">[5]</a>. **V(J)** represents the minimaxed value of node J. Opposed to McAllester's original definition which deals with pure game theoretic values, Van der Meulen's distinguished non terminal leaves with cn = 1 for values different of **v** from game theoretic terminal nodes to assign +oo, since it is impossible to change their value, independently been arrived at by [Norbert Klingbeil](Norbert_Klingbeil "Norbert Klingbeil") and [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

```C++
int cn(CNode J, int v) {
   int c;
   if ( V(J) == v ) {
      c = 0;
   } else if ( isTerminal(J) ) { 
      c = +oo; /* checkmate, stalemate, tablebase score, etc. */
   } else if ( isLeaf(J) ) {
      c = 1; 
   } else if (isMaxNode(J) && v < V(J) ) {
      c = 0;
      for (all childs J.j)
         if (v < V(J.j) ) c += cn(J.j, v); /* sum */
   } else if (isMinNode(J) && v > V(J) ) {
      c = 0;
      for (all childs J.j)
         if (v > V(J.j) ) c += cn(J.j, v); /* sum */
   } else {
      c = +oo;
      for (all childs J.j)
         c = min( cn(J.j, v), c);
   }
   return c;
}

```

## Conspiracy Theory

Let δ be a number called the singular margin <a id="cite-note-7" href="#cite-ref-7">[7]</a>. **Conspiracy theory** can be formulated using the following definition <a id="cite-note-8" href="#cite-ref-8">[8]</a>:

```C++**Definition**: Let **T** be a search tree with min-max value **V[T]**. The [lower boand](Lower_Bound "Lower Bound") conspiracy number of **T**, denoted **C<[T]**, is the number of leaf static values that must be changed to bring the root min-max value down to **V[T]-δ**. The [upper boand](Upper_Bound "Upper Bound") conspiracy number of **T**, denoted **C>[T]**, is the number of leaves that must be changed to bring the root value up to **V[T]+δ**. 

```

**C\<\[T\]** expresses the confidence that the lower bound [α](Alpha "Alpha") will hold by further expansion of the search tree.

## Search Algorithms

[McAllester's](David_McAllester "David McAllester") aim was related to some drawbacks of [alpha-beta](Alpha-Beta "Alpha-Beta"), at the worst, the decision at the root is based on a single evaluation of one leaf. If that leaf has assigned an erroneous value, the decision may be disastrous <a id="cite-note-9" href="#cite-ref-9">[9]</a>. The idea of [Conspiracy Number Search](Conspiracy_Number_Search "Conspiracy Number Search") (cn-search) and its variants is to continue until it is unlikely that the minimax value at the root will change.

- [Alpha-Beta Conspiracy Search](index.php?title=Alpha-Beta_Conspiracy_Search&action=edit&redlink=1 "Alpha-Beta Conspiracy Search (page does not exist)")
- [Conspiracy Number Search](Conspiracy_Number_Search "Conspiracy Number Search")
- [Proof-Number Search](Proof-Number_Search "Proof-Number Search")

## Publications

<a id="cite-note-10" href="#cite-ref-10">[10]</a>

## 1985 ...

- [David McAllester](David_McAllester "David McAllester") (**1985**). *A New Procedure for Growing Minimax Trees*. Technical Report, Artificial Intelligence Laboratory, MIT
- [David McAllester](David_McAllester "David McAllester") (**1988**). *Conspiracy Numbers for Min-Max Search*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 35, No. 1
- [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1988**). *Root Evaluation Errors: How they Arise and Propagate*. [ICCA Journal, Vol. 11, Nos. 2/3](ICGA_Journal#11_23 "ICGA Journal")
- [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1988**). *Parallel Conspiracy-Number Search*. M.Sc. thesis, Faculty of Mathematics and Computer Science, [Vrije Universteit, Amsterdam](https://en.wikipedia.org/wiki/Vrije_Universiteit)
- [Norbert Klingbeil](Norbert_Klingbeil "Norbert Klingbeil") (**1988**). *Search Strategies for Conspiracy Numbers*. M.Sc. thesis
- [Norbert Klingbeil](Norbert_Klingbeil "Norbert Klingbeil"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1988**). *Search Strategies for Conspiracy Numbers.* Canadian Artificial Intelligence Conference, pp. 133-139
- [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *Conspiracy Numbers.* [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5"). » [also published](Conspiracy_Numbers#AI "Conspiracy Numbers")
- [Charles Elkan](Charles_Elkan "Charles Elkan") (**1989**). *Conspiracy Numbers and Caching for Searching And/Or Trees and Theorem-Proving*. [IJCAI 1989](Conferences#IJCAI "Conferences"), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-89-VOL1/PDF/054.pdf)

## 1990 ...

- [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1990**). *Conspiracy-Number Search*. [ICCA Journal, Vol. 13, No. 1](ICGA_Journal#13_1 "ICGA Journal")
- [Norbert Klingbeil](Norbert_Klingbeil "Norbert Klingbeil"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1990**). *Empirical Results with Conspiracy Numbers.* Computational Intelligence, Vol. 6, pp. 1-11, [ps](http://webdocs.cs.ualberta.ca/%7Ejonathan/Papers/Papers/compi.ps)
- [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1990**). *Conspiracy Numbers*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 43, No. 1, pp. 67-84
- [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen"), [Victor Allis](Victor_Allis "Victor Allis"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1990**). *A Comment on \`Conspiracy-Number Search*. [ICCA Journal, Vol. 13, No. 2](ICGA_Journal#13_2 "ICGA Journal")
- [Victor Allis](Victor_Allis "Victor Allis"), [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1991**). *Conspiracy-Number Search.* [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
- [David McAllester](David_McAllester "David McAllester"), [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1993**). *Alpha-Beta Conspiracy Search*. [ps (draft)](http://ttic.uchicago.edu/%7Edmcallester/abc.ps)
- [Lisa Lister](index.php?title=Lisa_Lister&action=edit&redlink=1 "Lisa Lister (page does not exist)"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1994**). *An Analysis of the Conspiracy Numbers Algorithm*. [Computers & Mathematics with Applications](https://en.wikipedia.org/wiki/Computers_and_Mathematics_with_Applications) Vol. 27, No. 1, [Elsevier](https://en.wikipedia.org/wiki/Elsevier), [pdf](http://webdocs.cs.ualberta.ca/%7Ejonathan/publications/ai_publications/icn.pdf)
- [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1994**). *[The Principle of Pressure in Chess](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=EJurXJ4AAAAJ&cstart=40&citation_for_view=EJurXJ4AAAAJ:TQgYirikUcIC)*. TAINN 1994

## 1995 ...

- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann"), [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1995**). *Controlled Conspiracy-Number Search.* [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal")
- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1996**). *Parallel Controlled Conspiracy-Number Search.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**1999**). *Controlled Conspiracy-2 Search*. Technical Report, [Paderborn University](Paderborn_University "Paderborn University"), [ps](http://www2.cs.upb.de/cs/ag-monien/PUBLICATIONS/POSTSCRIPTS/Falgo.ps)
- [Robin Upton](index.php?title=Robin_Upton&action=edit&redlink=1 "Robin Upton (page does not exist)") (**1999**). *[Dynamic Stochastic Control - A New Approach to Game Tree Searching](http://www.robinupton.com/research/phd/)*. Ph.D. thesis, [University of Warwick](https://en.wikipedia.org/wiki/University_of_Warwick)

## 2000 ...

- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2000**). *Controlled Conspiracy-2 Search*. Proceedings of the 17th Annual Symposium on Theoretical Aspects of Computer Science (STACS)
- [David McAllester](David_McAllester "David McAllester"), [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**2002**). *Alpha-Beta Conspiracy Search*. [ICGA Journal, Vol. 25, No. 1](ICGA_Journal#25_1 "ICGA Journal")
- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2002**). *[Parallel Controlled Conspiracy Number Search](https://link.springer.com/chapter/10.1007/3-540-45706-2_57)*. [Euro-Par 2002](https://dblp1.uni-trier.de/db/conf/europar/europar2002.html), [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 2400, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

## 2010 ...

- [Mohd Nor Akmal Khalid](index.php?title=Mohd_Nor_Akmal_Khalid&action=edit&redlink=1 "Mohd Nor Akmal Khalid (page does not exist)"), [Umi Kalsom Yusof](index.php?title=Umi_Kalsom_Yusof&action=edit&redlink=1 "Umi Kalsom Yusof (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)") (**2015**). *[Critical Position Identification in Games and Its Application to Speculative Play](https://www.researchgate.net/publication/281152992_Critical_Position_Identification_in_Games_and_Its_Application_to_Speculative_Play)*. [ICAART 2015](http://www.scitepress.org/DigitalLibrary/ProceedingsDetails.aspx?ID=+mGlly8Sp00=&t=1)
- [Mohd Nor Akmal Khalid](index.php?title=Mohd_Nor_Akmal_Khalid&action=edit&redlink=1 "Mohd Nor Akmal Khalid (page does not exist)"), [E. Mei Ang](index.php?title=E._Mei_Ang&action=edit&redlink=1 "E. Mei Ang (page does not exist)"), [Umi Kalsom Yusof](index.php?title=Umi_Kalsom_Yusof&action=edit&redlink=1 "Umi Kalsom Yusof (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)") (**2015**). *[Identifying Critical Positions Based on Conspiracy Numbers](http://link.springer.com/chapter/10.1007%2F978-3-319-27947-3_6)*. [Agents and Artificial Intelligence](http://link.springer.com/book/10.1007/978-3-319-27947-3), [ICAART 2015 - Revised Selected Papers](http://dblp.uni-trier.de/db/conf/icaart/icaart2015s.html#KhalidAYII15)
- [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2015**). *[Sibling Conspiracy Number Search](https://www.aaai.org/ocs/index.php/SOCS/SOCS15/paper/view/11040)*. [SoCS 2015](https://en.wikipedia.org/wiki/Symposium_on_Combinatorial_Search)
- [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2016**). *[Conspiracy number search with relative sibling scores](https://www.sciencedirect.com/science/article/pii/S0304397516302729)*. [Theoretical Computer Science](<https://en.wikipedia.org/wiki/Theoretical_Computer_Science_(journal)>), Vol. 644
- [Quang Vu](index.php?title=Quang_Vu&action=edit&redlink=1 "Quang Vu (page does not exist)"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)"), [Jean-Christophe Terrillon](index.php?title=Jean-Christophe_Terrillon&action=edit&redlink=1 "Jean-Christophe Terrillon (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2016**). *Using Conspiracy Numbers for Improving Move Selection in Minimax Game-Tree Search*. [ICAART 2016](http://www.icaart.org/?y=2016), [pdf](https://pdfs.semanticscholar.org/1bcf/bd2047bc1d74affda11bf2007cac442dd6f4.pdf)
- [Zhang Song](index.php?title=Zhang_Song&action=edit&redlink=1 "Zhang Song (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2018**). *Using single conspiracy number for long term position evaluation*. [CG 2018](CG_2018 "CG 2018"), [ICGA Journal, Vol. 40, No. 3](ICGA_Journal#40_3 "ICGA Journal")

## External Links

## Conspiracy Numbers

- [Conspiracy Numbers, Conspiracy Probailities & PCN\* Search](http://www.robinupton.com/research/phd/cp_intro.html) by [Robin Upton](index.php?title=Robin_Upton&action=edit&redlink=1 "Robin Upton (page does not exist)")
- [Reading: McAllister paper on "Consipracy Theory"?](http://www.cs.duke.edu/brd/Teaching/Previous/AI/Lectures/conspiracy.txt) by [Bruce Donald](http://www.cs.duke.edu/brd/)

## Conspiracy

- [Conspiracy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Conspiracy)
- [Conspiracy theory from Wikipedia](https://en.wikipedia.org/wiki/Conspiracy_theory)
- [List of conspiracy theories from Wikipedia](https://en.wikipedia.org/wiki/List_of_conspiracy_theories)
- [Conspiracy theory (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Conspiracy_theory_%28disambiguation%29)
- [Squire](Category:Chris_Squire "Category:Chris Squire") & [Sherwood](https://en.wikipedia.org/wiki/Billy_Sherwood), [Conspiracy](https://en.wikipedia.org/wiki/Conspiracy_%28band%29) - [Conspiracy](<https://en.wikipedia.org/wiki/Conspiracy_(band)#Conspiracy>), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Photo from [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5") by [László Lindner](L%C3%A1szl%C3%B3_Lindner "László Lindner"), [ICCA Journal, Vol. 10, No. 3](ICGA_Journal#10_3 "ICGA Journal"), pp. 138
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> Definition, Sample, and Pseudo code taken from [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1990**). *Conspiracy-Number Search*. [ICCA Journal, Vol. 13, No. 1](ICGA_Journal#13_1 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [David McAllester](David_McAllester "David McAllester") (**1988**). *Conspiracy Numbers for Min-Max Search*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 35, No. 1, pp. 287-310. ISSN 0004-3702
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> due to [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *Conspiracy Numbers.* [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1990**). *Conspiracy-Number Search*. [ICCA Journal, Vol. 13, No. 1](ICGA_Journal#13_1 "ICGA Journal")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Norbert Klingbeil](Norbert_Klingbeil "Norbert Klingbeil"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1988**). *Search Strategies for Conspiracy Numbers.* Canadian Artificial Intelligence Conference, pp. 133-139
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> The term *singular margin* comes from the [singular extension](Singular_Extensions "Singular Extensions") algorithm ([Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") et al. 1990)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [David McAllester](David_McAllester "David McAllester"), [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1993**). *Alpha-Beta Conspiracy Search*. [ps (draft)](http://ttic.uchicago.edu/%7Edmcallester/abc.ps)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1996**). *Parallel Controlled Conspiracy-Number Search.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [ICGA Reference Database](ICGA_Journal#RefDB "ICGA Journal")

**[Up one Level](Search "Search")**

