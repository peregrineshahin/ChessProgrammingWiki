---
title: SSS and Dual
---
**[Home](Home "Home") \* [Search](Search "Search") \* SSS\* and Dual**\*



 [](http://www.mcescher.com/Gallery/back-bmp/LW359.jpg) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Stars, 1948 <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**SSS**\*,  

a [best-first](Best-First "Best-First") [state space search](https://en.wikipedia.org/wiki/State_space_search) developed in 1977 by [George C. Stockman](George_Stockman "George Stockman") for the [linguistic](https://en.wikipedia.org/wiki/Linguistics) analysis of waveforms <a id="cite-note-2" href="#cite-ref-2">[2]</a> . In a later paper, Stockman ([1979](Timeline#1979 "Timeline")) <a id="cite-note-3" href="#cite-ref-3">[3]</a> showed how to use this algorithm to determine the minimax value of game trees. **SSS**\* and it counterpart **Dual**\* are non-directional algorithms for searching AND/OR graphs in a best-first manner similar to [A\*](index.php?title=A*&action=edit&redlink=1 "A* (page does not exist)"). They expand multiple paths of the search graph and retain global information about the search space, and search fewer nodes than [Alpha-Beta](Alpha-Beta "Alpha-Beta") in fixed-depth minimax tree search.


The algorithm was examined and improved by various researchers: [Igor Roizen](Igor_Roizen "Igor Roizen") and [Judea Pearl](Judea_Pearl "Judea Pearl") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, [Toshihide Ibaraki](Toshihide_Ibaraki "Toshihide Ibaraki") <a id="cite-note-5" href="#cite-ref-5">[5]</a> , [Tony Marsland](Tony_Marsland "Tony Marsland") *et al.*, [Subir Bhattacharya](Subir_Bhattacharya "Subir Bhattacharya") and [Amitava Bagchi](Amitava_Bagchi "Amitava Bagchi"), [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls") and [Arie de Bruin](Arie_de_Bruin "Arie de Bruin"). In 1988 [Burkhard Monien](Burkhard_Monien "Burkhard Monien") and [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") compared parallel [Alpha-Beta](Alpha-Beta "Alpha-Beta") with parallel SSS\* <a id="cite-note-6" href="#cite-ref-6">[6]</a> and in 1990, [Hans-Joachim Kraas](Hans-Joachim_Kraas "Hans-Joachim Kraas") wrote his Ph.D thesis about how to parallelize **SSS**\* <a id="cite-note-7" href="#cite-ref-7">[7]</a> .


However, it turned out the algorithmic overhead was too big to pay off the saved nodes. [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls") and [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") pointed out, that **SSS**\* can be reformulated as a sequence of [alpha-beta](Alpha-Beta "Alpha-Beta") [null window](Null_Window "Null Window") calls with a [Transposition Table](Transposition_Table "Transposition Table"). 



### Pseudo C-Code



```C++

int SSS* (node n; int bound)
{
   push (n, LIVE, bound);
   while ( true ) {
      pop (node);
      switch ( node.status ) {
      case LIVE:
          if (node == LEAF)
             insert (node, SOLVED, min(eval(node),h));
          if (node == MIN_NODE)
             push (node.1, LIVE, h);
          if (node == MAX_NODE)
             for (j=w; j; j--)
                push (node.j, LIVE, h);
          break;
      case SOLVED:
          if (node == ROOT_NODE)
             return (h);
          if (node == MIN_NODE) {
              purge (parent(node));
              push (parent(node), SOLVED, h);
          }
          if (node == MAX_NODE) {
             if (node has an unexamined brother)
                push (brother(node), LIVE, h);
             else
                push (parent(node), SOLVED, h);
          }
          break;
      }
   }
}

```


```C++
SSS* is too complex and too slow!

```

* `In each step, the node with the maximum h-value is removed from OPEN.`
* `Whenever an interior MAX-node gets SOLVED, all direct and indirect descendants must be purged from OPEN`


`These two steps alone take 90% of the CPU time!`


[Aske Plaat](Aske_Plaat "Aske Plaat") et al. continue:




```C++
SSS*, as formulated by Stockman, has several problems. First, it takes considerable effort to understand how the algorithm works, and still more to understand its relation to Alpha-Beta. Second, SSS* maintains a data structure known as the OPEN list, similar to that found in single-agent search algorithms like A*. The size of this list grows exponentially with the depth of the search tree. This has led many authors to conclude that SSS* is effectively disqualified from being useful for real applications like game-playing programs. Third, the OPEN list must be kept in sorted order. Insert and (in particular) delete/purge operations on the OPEN list can dominate the execution time of any program using SSS*. Despite the promise of expanding fewer nodes, the disadvantages of SSS* have proven a significant deterrent in practice.

```

Quote by [Judea Pearl](Judea_Pearl "Judea Pearl") 1984 <a id="cite-note-9" href="#cite-ref-9">[9]</a> :




```C++
The meager improvement in the pruning power of SSS* is more than offset by the increased storage space and bookkeeping (e.g. sorting OPEN) that it requires. One can safely speculate therefore that [alphabeta](Alpha-Beta "Alpha-Beta") will continue to monopolize the practice of computerized game playing.

```

## Dual\*


**Dual**\* is the dual counterpart of **SSS**\* by [Tony Marsland](Tony_Marsland "Tony Marsland") *et al* <a id="cite-note-10" href="#cite-ref-10">[10]</a> . The dual version of **SSS**\* can be created by inverting **SSS\*’s** operations: use an ascendingly sorted list instead of descending, swap max and min operations, and start at -oo instead of +oo.






## RecSSS\* and RecDual\*


The development of [recursive](Recursion "Recursion") variants was driven by the need for a better understanding of **SSS**\*'s node expansion process and by the demand for more efficient implementations. Two recursive variants were proposed 1990: **RecSSS**\* <a id="cite-note-11" href="#cite-ref-11">[11]</a> by [Subir Bhattacharya](Subir_Bhattacharya "Subir Bhattacharya") and [Amitava Bagchi](Amitava_Bagchi "Amitava Bagchi") and **SSS-2** <a id="cite-note-12" href="#cite-ref-12">[12]</a> by [Wim Pijls](Wim_Pijls "Wim Pijls") and [Arie de Bruin](Arie_de_Bruin "Arie de Bruin"). In 1993 [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") improved **RecSSS**\*, making it both faster and more space efficient, using an OPEN-[array](Array "Array") rather than dynamic list structures <a id="cite-note-13" href="#cite-ref-13">[13]</a> .



### Pseudo C-Code


based on [Alexander Reinefeld's](Alexander_Reinefeld "Alexander Reinefeld") [Pascal](Pascal "Pascal") pseudo code:




```C++

int RecSS*(nodeType n)
{
   if (n is leaf) {
      s(n) = SOLVED;
      return min (evaluate(n), h(n));                                            /* evaluate leaf */
   }
   if ( s(n) == UNEXPANDED ) {                                                  /* first descend? */
      s(n) = LIVE;                                                                    /* expand n */
      for (i = 1 to width)
         if ( n.i is leaf )
            insert (n.i, UNEXPANDED, h(n));                    /* insert sons (= MIN leaves) of n */
         else
            insert (n.i.1, UNEXPANDED, h(n));                       /* insert left grandsons of n */
   }
   g = highest h-valued grandson (or son) of n in OPEN;
   while ( h(g) == h(n) && status(g) != SOLVED ) {
      h(g) = RecSS*(g);                                                    /* get new upper bound */
      if ( s(g) == SOLVED && g has a right brother )
          replace g by (brother(g), UNDEXPANDED, h(g));                      /* next brother of g */
      g = highest h-valued grandson (or son) of n in OPEN; /*resolve ties in lexicographical order*/
   }
   if ( s(g) == SOLVED )
      s(n) = SOLVED;
   return h(g);
}

```


```C++

int main()
{
   insert (root, UNEXPANDED, oo);
   do
      h = RecSSS*(root);
   while ( s(n) != SOLVED );
}

```





## SSS\* and Dual\* as MT


[Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls") and [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") proved with their Memory Test framework, that both **SSS**\* and **Dual**\* can be reformulated as a sequence of [alpha-beta](Alpha-Beta "Alpha-Beta") [null window](Null_Window "Null Window") calls with a [Transposition Table](Transposition_Table "Transposition Table") <a id="cite-note-14" href="#cite-ref-14">[14]</a> :



### Pseudo C-Code



```C++

int MT-SSS*( n )
{
   g := +oo;
   do {
      G := g;
      g := Alpha-Beta(n, G-1, G );
   } while (g != G);
   return g;
}

```


```C++

int MT-DUAL*(n)
{
   g := -oo;
   do {
      G := g;
      g := Alpha-Beta(n, G, G+1 );
   } while (g != G);
   return g;
}

```

At the [8th Advances in Computer Chess](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8") conference 1996, **SSS**\* was finally declared "dead" by [Wim Pijls](Wim_Pijls "Wim Pijls") and [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") <a id="cite-note-15" href="#cite-ref-15">[15]</a> <a id="cite-note-16" href="#cite-ref-16">[16]</a> .



## See also


* [MTD(f)](MTD(f) "MTD(f)")
* [NegaC\*](NegaC* "NegaC*")
* [NegaScout](NegaScout "NegaScout")
* [Scout](Scout "Scout")


## Publications


### 1979


* [George Stockman](George_Stockman "George Stockman") (**1979**). *A Minimax Algorithm Better than Alpha-Beta?* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 12, No. 2.


### 1980 ...


* [Igor Roizen](Igor_Roizen "Igor Roizen"), [Judea Pearl](Judea_Pearl "Judea Pearl") (**1983**). *A Minimax Algorithm Better than Alpha-Beta? Yes and No*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 21
* [Murray Campbell](Murray_Campbell "Murray Campbell"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1983**). *A Comparison of Minimax Tree Search Algorithms*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 20, No. 4, pp. 347-367. ISSN 0004-3702, [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/TR82-3.pdf)
* [Nanda Srimani](index.php?title=Nanda_Srimani&action=edit&redlink=1 "Nanda Srimani (page does not exist)") (**1985**). *A New Algorithm (PS\*) for Searching Game Trees*. Master's thesis, [University of Alberta](University_of_Alberta "University of Alberta")
* [Daniel B. Leifker](http://www.informatik.uni-trier.de/~ley/pers/hd/l/Leifker:Daniel_B=.html), [Laveen N. Kanal](Laveen_Kanal "Laveen Kanal") (**1985**). *[A Hybrid SSS\*/Alpha-Beta Algorithm for Parallel Search of Game Trees](http://dl.acm.org/citation.cfm?id=1623687)*. [IJCAI'85](http://www.informatik.uni-trier.de/~ley/db/conf/ijcai/ijcai85.html#LeifkerK85)
* [Toshihide Ibaraki](Toshihide_Ibaraki "Toshihide Ibaraki") (**1986**). *[Generalization of Alpha-Beta and SSS\* Search Procedures](https://www.sciencedirect.com/science/article/abs/pii/0004370286900925)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 29
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Nanda Srimani](index.php?title=Nanda_Srimani&action=edit&redlink=1 "Nanda Srimani (page does not exist)") (**1986**). *Phased State Search*. [Fall Joint Computer Conference](http://www.informatik.uni-trier.de/~ley/db/conf/fjcc/fjcc86.html#MarslandS86), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/fjcc.1986.pdf)
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1987**). Low Overhead Alternatives to SSS\*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 31, No. 2, pp. 185-199. ISSN 0004-3702.
* [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1988**). *Parallel Alpha-Beta versus Parallel SSS\**. Proc. of the IFIP WG 10.3 Working Conference on Distributed Processing, North Holland
* [Yoshiroh Katoh](https://dblp.uni-trier.de/pers/hd/k/Katoh:Yoshiroh), [Toshihide Ibaraki](Toshihide_Ibaraki "Toshihide Ibaraki") (**1988**). *[Game Solving Procedure SSS\* is Unsurpassed](https://onlinelibrary.wiley.com/doi/pdf/10.1002/scj.4690190710)*. [Systems and Computers in Japan](https://onlinelibrary.wiley.com/journal/1520684x), Vol. 19, No. 7


### 1990 ...


* [Subir Bhattacharya](Subir_Bhattacharya "Subir Bhattacharya"), [Amitava Bagchi](Amitava_Bagchi "Amitava Bagchi") (**1990**). *Unified Recursive Schemes for Search in Game Trees.* Technical Report WPS-144, [Indian Institute of Management, Calcutta](https://en.wikipedia.org/wiki/Indian_Institute_of_Management_Calcutta)
* [Hans-Joachim Kraas](Hans-Joachim_Kraas "Hans-Joachim Kraas") (**1990**).*Zur Parallelisierung des SSS\*-Algorithmus*. Ph.D thesis, [TU Braunschweig](https://en.wikipedia.org/wiki/Technical_University_of_Braunschweig) (German)
* [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1990**). *Another View on the SSS\* Algorithm.* International Symposium SIGAL '90
* [Claude G. Diderich](Claude_G._Diderich "Claude G. Diderich") (**1992**). *Evaluation des performance de l'algorithme SSS\* avec phases de synchronisation sur une machine parallèle à mémoires distribées*. Technical report LITH-99, [Swiss Federal Institute of Technology](https://en.wikipedia.org/wiki/%C3%89cole_Polytechnique_F%C3%A9d%C3%A9rale_de_Lausanne), Computer Science Theory Laboratory, Lausanne, Switzerland (French)
* [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1993**). *SSS\*-like Algorithms in Constrained Memory.* [ICCA Journal, Vol. 16, No. 1](ICGA_Journal#16_1 "ICGA Journal")
* [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**1994**). *A Minimax Algorithm Faster than Alpha-Beta*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1994, 2014**). *SSS\* = Alpha-Beta + TT*. TR-CS-94-17, [University of Alberta](University_of_Alberta "University of Alberta"), [arXiv:1404.1517](https://arxiv.org/abs/1404.1517)
* [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld"), [Peter Ridinger](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/r/Ridinger:Peter.html) (**1994**). *[Time-Efficient State Space Search](http://www.sciencedirect.com/science/article/pii/0004370294900493)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 71, No. 2, [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.42.1934)
* [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1996**). *An Algorithm Faster than NegaScout and SSS\* in Practice*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.77.9111&rep=rep1&type=pdf) from [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX) » [MTD(f)](MTD(f) "MTD(f)")
* [Arie de Bruin](Arie_de_Bruin "Arie de Bruin"), [Wim Pijls](Wim_Pijls "Wim Pijls") (**1997**). *SSS†.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")


### 2000 ...


* [Arie de Bruin](Arie_de_Bruin "Arie de Bruin"), [Wim Pijls](Wim_Pijls "Wim Pijls") (**2003**). *[Trends in game tree search](https://repub.eur.nl/pub/459)*. [Erasmus University, Rotterdam](https://en.wikipedia.org/wiki/Erasmus_University_Rotterdam)


### 2010 ...


* [Bojun Huang](Bojun_Huang "Bojun Huang") (**2015**). *[Pruning Game Tree by Rollouts](https://www.semanticscholar.org/paper/Pruning-Game-Tree-by-Rollouts-Huang/a38b358745067f71a9c780db117ae2471e693d63)*. [AAAI](AAAI "AAAI") » [MT-SSS\*](SSS*_and_Dual*#SSStarandDualStarAsMT "SSS* and Dual*"), [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") <a id="cite-note-17" href="#cite-ref-17">[17]</a>


## External Links


* [SSS\* from Wikipedia](https://en.wikipedia.org/wiki/SSS*)
* [State space search from Wikipedia](https://en.wikipedia.org/wiki/State_space_search)
* [Aziza Mustafa Zadeh](Category:Aziza_Mustafa_Zadeh "Category:Aziza Mustafa Zadeh") - Stars Dance, [Leverkusener Jazztage](https://en.wikipedia.org/wiki/Leverkusener_Jazztage), November 7, 2006, [3sat](https://en.wikipedia.org/wiki/3sat), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Stars, 1948, [Picture gallery "Back in Holland 1941 - 1954"](http://www.mcescher.com/Gallery/gallery-back.htm) from [The Official M.C. Escher Website](http://www.mcescher.com/)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [George Stockman](George_Stockman "George Stockman"), [Laveen Kanal](Laveen_Kanal "Laveen Kanal") (**1983**). *[Problem Reduction Representation for the Linguistic Analysis of Waveforms](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?isnumber=4767384&arnumber=4767391&count=16&index=6)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 5, No 3
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [George Stockman](George_Stockman "George Stockman") (**1979**). *A Minimax Algorithm Better than Alpha-Beta?* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 12, No. 2
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Igor Roizen](Igor_Roizen "Igor Roizen"), [Judea Pearl](Judea_Pearl "Judea Pearl") (**1983**). *A Minimax Algorithm Better than Alpha-Beta? Yes and No*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 21
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Toshihide Ibaraki](Toshihide_Ibaraki "Toshihide Ibaraki") (**1986**). *[Generalization of Alpha-Beta and SSS\* Search Procedures](https://www.sciencedirect.com/science/article/abs/pii/0004370286900925)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 29
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1988**). *Parallel Alpha-Beta versus Parallel SSS\**. Proc. of the IFIP WG 10.3 Working Conference on Distributed Processing, North Holland
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Hans-Joachim Kraas](Hans-Joachim_Kraas "Hans-Joachim Kraas") (**1990**). *Zur Parallelisierung des SSS\*-Algorithmus*. Ph.D thesis, [TU Braunschweig](https://en.wikipedia.org/wiki/Technical_University_of_Braunschweig) (German)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**2005**). *Die Entwicklung der Spielprogrammierung: Von John von Neumann bis zu den hochparallelen Schachmaschinen*. [slides as pdf](http://www.informatik.hu-berlin.de/studium/ringvorlesung/ss05/slides/05-06-02.pdf), Themen der Informatik im historischen Kontext Ringvorlesung an der [HU Berlin](https://en.wikipedia.org/wiki/Humboldt_University_of_Berlin), 02.06.2005 (English paper, German title)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Judea Pearl](Judea_Pearl "Judea Pearl") (**1984**). Heuristics: Intelligent Search Strategies for Computer Problem Solving. Addison-Wesley Publishers Co., Reading, MA. ISBN 0-201-05594-5.
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Tony Marsland](Tony_Marsland "Tony Marsland"), [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1987**). Low Overhead Alternatives to SSS\*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 31, No. 2, pp. 185-199. ISSN 0004-3702.
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Subir Bhattacharya](Subir_Bhattacharya "Subir Bhattacharya"), [Amitava Bagchi](Amitava_Bagchi "Amitava Bagchi") (**1990**). *Unified Recursive Schemes for Search in Game Trees.* Technical Report WPS-144, [Indian Institute of Management, Calcutta](https://en.wikipedia.org/wiki/Indian_Institute_of_Management_Calcutta)
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1990**). *Another View on the SSS\* Algorithm*. International Symposium SIGAL '90
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**1994**). *A Minimax Algorithm Faster than Alpha-Beta*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1994, 2014**). *SSS\* = Alpha-Beta + TT*. TR-CS-94-17, [University of Alberta](University_of_Alberta "University of Alberta"), [arXiv:1404.1517](https://arxiv.org/abs/1404.1517)
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Arie de Bruin](Arie_de_Bruin "Arie de Bruin"), [Wim Pijls](Wim_Pijls "Wim Pijls") (**1997**). *SSS†.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin")(**1996**). *Best-First Fixed-Depth Minimax Algorithms.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 87
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Re: Announcing lczero](http://www.talkchess.com/forum/viewtopic.php?t=66280&start=67) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 21, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")

**[Up one level](Search "Search")**







 
