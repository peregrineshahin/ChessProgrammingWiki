---
title: ProofNumber SearchPDS
---
**[Home](Home "Home") \* [Search](Search "Search") \* Proof-Number Search**



[_-_Phillips_Collection_-_DSC04897.JPG) [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Tree Nursery <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Proof-Number Search**, (Pn-Search, PnS, PNS)  

a [best-first](Best-First "Best-First") [and-or tree](https://en.wikipedia.org/wiki/And%E2%80%93or_tree) search algorithm designed by [Victor Allis](Victor_Allis "Victor Allis") for finding the game-theoretical value in game trees <a id="cite-note-2" href="#cite-ref-2">[2]</a> . PNS is based on ideas derived from [conspiracy number search](Conspiracy_Number_Search "Conspiracy Number Search"). While in cn search the purpose is to continue searching until it is unlikely that the [minimax](Minimax "Minimax") value of the [root](Root "Root") will change, PNS aims at **proving** the true value of the root <a id="cite-note-3" href="#cite-ref-3">[3]</a>. In the fall 2012 issue of the [ICGA Journal](ICGA_Journal#35_3 "ICGA Journal"), about 20 years after its invention, [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Mark Winands](Mark_Winands "Mark Winands"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") and [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito") wrote a résumé about PNS and its variants and enhancements, considered a tribute to Victor Allis by editor [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> . 



### Conspiracy Numbers


PNS specializes [conspiracy numbers](Conspiracy_Numbers "Conspiracy Numbers") to [and-or tree](https://en.wikipedia.org/wiki/And%E2%80%93or_tree) search with binary outcome, with significant reduced [memory](Memory "Memory") requirements compared to CnS <a id="cite-note-6" href="#cite-ref-6">[6]</a> . MAX-nodes are represented as OR-nodes, MIN-nodes as AND-nodes. A solved tree with value *true* is called proved, while a solved tree with value *false* is called disproved. Evaluation of leaves yields in the values of *false*, *true* or *unknown*, the latter can be expanded to become a [frontier node](Frontier_Nodes "Frontier Nodes"). For backpropagation, after expansion, AND-nodes become *false* if at least one child is *false*, else *unknown* if at least one child is *unknown*, otherwise *true*. At OR-nodes, *false* and *true* are interchanged analogously.



### Proof and Disproof Numbers


The algorithm requires the whole tree in memory to select the next evaluated but yet unknown node to be expanded using two criteria: the potential range of subtree values and the number of nodes which must conspire to **prove** or **disprove** that range of potential values. These two criteria enable PNS to treat game trees with a non-uniform [branching factor](Branching_Factor "Branching Factor") and deep and narrow lines efficiently.


PNS continuously tries to solve the tree by focusing on the potentially shortest solution, i.e., consisting of the least number of nodes. At each step of the search, a node which is part of the potentially shortest solution available is selected and expanded or developed. After expansion, its conspiracy numbers, the proof- and disproof number, are established anew, to update the proof- and disproof numbers of its ancestors. This process of selection, expansion and ancestor update is repeated until either the tree is solved or has run out of time- or memory resources.



### Tree Sample


Following sample, taken from Allis' Ph.D. thesis <a id="cite-note-7" href="#cite-ref-7">[7]</a> , illustrates how proof and disproof numbers are assigned and updated to solve the tree.


All frontier nodes (E, F, I, L, M, N and P) have proof number or conspiracy of 1. A terminal node with value *true* (node K) has proof number 0, with value *false* (node O), proof number ∞. Internal AND-nodes (B, D, G, H and J) have proof numbers equal to the sum of the proof numbers of their children, internal OR-nodes (A and C) have proof numbers equal to the minimum of the proof numbers of their children. Disproof numbers behave analogously to proof numbers, interchanging the roles of AND-nodes and OR-nodes, and the cardinalities 0 and ∞. Each pair consisting of a smallest proof set and a smallest disproof set has a non-empty intersection.





|  |  |
| --- | --- |
| [ProofNTree.jpg](File:ProofNTree.jpg) | [DisproofNTree.jpg](File:DisproofNTree.jpg) |
|  And-or tree with proof numbers
 |  and disproof numbers
 |


## Pseudo Code


The PNS C-like pseudo code is based on the code given in *Game-Tree Search using Proof Numbers: The First Twenty Years* by [Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto") et al. <a id="cite-note-8" href="#cite-ref-8">[8]</a> . The domain dependent procedure evaluate assigns one of the values *proven*, *disproven* and *unknown* to node.value.




```C++

void PNS ( Node root ) {
  evaluate( root );
  setProofAndDisproofNumbers( root );
  Node current = root;
  while ( root.proof != 0 && root.disproof != 0 && resourcesAvailable() ) {
    Node mostProving = selectMostProvingNode( current );
    expandNode( mostProving );
    current = updateAncestors( mostProving, root );
  }
}

```

### Set Numbers



```C++

void setProofAndDisproofNumbers( Node n ) {
  if ( n.expanded ) { /* interior node */
    if ( n.type == AND ) {
      n.proof = 0;  n.disproof = ∞;
      for (each child c of n) {
         n.proof += c.proof;
         n.disproof = min(n.disproof, c.disproof);
      }
    } else { /* OR node */
      n.proof = ∞;  n.disproof = 0;
      for (each child c of n) {
         n.disproof += c.disproof;
         n.proof = min(n.proof, c.proof);
      }
    }
  } else { /* terminal node or none terminal leaf */
    switch( n.value ) {
      case disproven: n.proof = ∞; n.disproof = 0; break;
      case proven:    n.proof = 0; n.disproof = ∞; break;
      case unknown:   n.proof = 1; n.disproof = 1; break;
    }
  }
}

```

### Select



```C++

Node selectMostProvingNode( Node n ) {
  while ( n.expanded ) {
    int value = ∞;
    Node best;
    if ( n.type == AND ) {
      for (each child c of n) {
        if ( value > c.disproof ) {
           best = c;
           value = c.disproof;
        }
      }
    } else { /* OR node */
      for (each child c of n) {
        if ( value > c.proof ) {
           best = c;
           value = c.proof;
        }
      }
    }
    n = best;
  }
  return n;
}

```

### Expand



```C++

void expandNode( Node n ) {
  generateChildren( n );
  for (each child c of n) {
    evaluate( c );
    setProofAndDisproofNumbers( c );
    if ( n.type == AND ) {
      if ( c.disproof == 0 ) break;
    } else {  /* OR node */
      if ( c.proof == 0 ) break;
    }
  }
  n.expanded = true;
}

```

### Update Ancestors



```C++

Node updateAncestors( Node n, Node root ) {
  while( n != root ) {
    int oldProof = n.proof;
    int oldDisproof = n.disproof;
    setProofAndDisproofNumbers( n );
    if ( n.proof == oldProof && n.disproof == oldDisproof )
      return n;
    n = n.parent;
  }
  setProofAndDisproofNumbers( root );
  return root;
}

```

## Enhancements


Proof-number search as illustrated above is suited for pure trees, but has issues with games consisting of [directed acyclic graphs](https://en.wikipedia.org/wiki/Directed_acyclic_graph) ([transpositions](Transposition "Transposition")) and even more, [directed cyclic graphs](https://en.wikipedia.org/wiki/Directed_graph) ([repetitions](Repetitions "Repetitions")), already addressed by [Martin Schijf](index.php?title=Martin_Schijf&action=edit&redlink=1 "Martin Schijf (page does not exist)") in 1993 <a id="cite-note-9" href="#cite-ref-9">[9]</a> .



### Pn²


The **Pn²** search algorithm safes resources by using a second PNS instead of calling *evaluate*, which child-nodes can be discarded afterwards <a id="cite-note-10" href="#cite-ref-10">[10]</a> .




### Depth First


**C**\* and **PN**\*, introduced by [Masahiro Seo](index.php?title=Masahiro_Seo&action=edit&redlink=1 "Masahiro Seo (page does not exist)") <a id="cite-note-11" href="#cite-ref-11">[11]</a> and Seo et al <a id="cite-note-12" href="#cite-ref-12">[12]</a> , transforms a best-first PNS into an [iterative deepening](Iterative_Deepening "Iterative Deepening") [depth-first](Depth-First "Depth-First") approach **df-pn**. Moreover, PN\* also incorporates ideas from [Korf's](Richard_Korf "Richard Korf") *Linear-Space Best-First Search* (RBFS) <a id="cite-note-13" href="#cite-ref-13">[13]</a>, and is enhanced by methods such as [recursive iterative deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), dynamic evaluation, efficient [successor ordering](Move_Ordering "Move Ordering"), and pruning by dependency relations. 




### PDS


[Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai") proposed a depth-first variation of PNS dubbed **PDS** for Proof-number and Disproof-number Search <a id="cite-note-14" href="#cite-ref-14">[14]</a> .



### PDS-PN


**PDS-PN** is a two-level search, which performs a depth-first Proof-number and Disproof-number Search (PDS) at the first level, followed by second level best-first PNS <a id="cite-note-15" href="#cite-ref-15">[15]</a> .



### Parallel PNS


[Parallel search](Parallel_Search "Parallel Search") implementations of PNS were introduced by [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto") and [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") in 1999 <a id="cite-note-16" href="#cite-ref-16">[16]</a> , and by [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") in 2010 <a id="cite-note-17" href="#cite-ref-17">[17]</a> .



## Applications


In conjunction with [retrograde analysis](Retrograde_Analysis "Retrograde Analysis") and [alpha-beta](Alpha-Beta "Alpha-Beta"), PNS approaches were used to solve various games completely or partial, and to support game playing programs in finding game theoretic solutions. As pointed out by [Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto") et al. <a id="cite-note-18" href="#cite-ref-18">[18]</a> , [Victor Allis](Victor_Allis "Victor Allis") first used the notion of proof and disproof numbers while analyzing and solving [Connect Four](Connect_Four "Connect Four"), still called [conspiracy numbers](Conspiracy_Numbers "Conspiracy Numbers") <a id="cite-note-19" href="#cite-ref-19">[19]</a> . [Charles Elkan](Charles_Elkan "Charles Elkan") applied proof numbers to [theorem proving](https://en.wikipedia.org/wiki/Automated_theorem_proving) <a id="cite-note-20" href="#cite-ref-20">[20]</a> . In [Go](Go "Go"), PNS could be applied in [Life and death](https://en.wikipedia.org/wiki/Life_and_death) situations <a id="cite-note-21" href="#cite-ref-21">[21]</a> , and PNS played an important role in solving [Checkers](Checkers "Checkers") by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") et al. in 2007 <a id="cite-note-22" href="#cite-ref-22">[22]</a> <a id="cite-note-23" href="#cite-ref-23">[23]</a> .


In [Shogi](Shogi "Shogi") as well in Chess, PNS solves deep [tsume-shogi](https://en.wikipedia.org/wiki/Tsumeshogi) or [mate](Checkmate "Checkmate") problems. [Prover](Duck#Prover "Duck") was a PNS implementation for chess, using chess-specific routines of [Duck](Duck "Duck"). Provers only goal was [searching for mate](Mate_Search "Mate Search") <a id="cite-note-24" href="#cite-ref-24">[24]</a> . [Sjeng](Sjeng "Sjeng") by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto") uses Proof-number search in it's [suicide and loser's](https://en.wikipedia.org/wiki/Antichess) mode <a id="cite-note-25" href="#cite-ref-25">[25]</a> .



## See also


* [Conspiracy Numbers](Conspiracy_Numbers "Conspiracy Numbers")
* [Conspiracy Number Search](Conspiracy_Number_Search "Conspiracy Number Search")
* [Lambda-Search](index.php?title=Lambda-Search&action=edit&redlink=1 "Lambda-Search (page does not exist)")
* [Mate Search](Mate_Search "Mate Search")
* [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis")
* [Theorem-Proving](James_R._Slagle#TheoremProving "James R. Slagle") by [James R. Slagle](James_R._Slagle "James R. Slagle")
* [Theorem-Proving from Five-Year Plan](Jack_Good#TheoremProving "Jack Good") by [Jack Good](Jack_Good "Jack Good")


## Publications


### 1988 ...


* [Victor Allis](Victor_Allis "Victor Allis") (**1988**). *A Knowledge-Based Approach of Connect Four: The Game is Over, White to Move Wins*. M.Sc. thesis, Report No. IR-163, Faculty of Mathematics and Computer Science, [Vrije Universteit, Amsterdam](https://en.wikipedia.org/wiki/Vrije_Universiteit)
* [Charles Elkan](Charles_Elkan "Charles Elkan") (**1989**). *Conspiracy Numbers and Caching for Searching And/Or Trees and Theorem-Proving*. [IJCAI 1989](Conferences#IJCAI "Conferences"), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-89-VOL1/PDF/054.pdf)


### 1990 ...


* [Victor Allis](Victor_Allis "Victor Allis"), [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1991**). *Proof-Number Search.* Technical Reports in Computer Science, CS 91-01. Department of Computer Science, [University of Limburg](Maastricht_University "Maastricht University"). ISSN 0922-8721.
* [Victor Allis](Victor_Allis "Victor Allis"), [Patrick Schoo](index.php?title=Patrick_Schoo&action=edit&redlink=1 "Patrick Schoo (page does not exist)") (**1992**). *Qubic Solved Again*. Heuristic Programming in Artificial Intelligence 3: [The Third Computer Olympiad](3rd_Computer_Olympiad "3rd Computer Olympiad")
* [Martin Schijf](index.php?title=Martin_Schijf&action=edit&redlink=1 "Martin Schijf (page does not exist)") (**1993**). *Proof-number Search and Transpositions*. M.Sc. thesis, [Leiden University](Leiden_University "Leiden University")
* [Victor Allis](Victor_Allis "Victor Allis") (**1994**). *Searching for Solutions in Games and Artificial Intelligence*. Ph.D. thesis, [University of Limburg](Maastricht_University "Maastricht University"), [pdf](http://fragrieu.free.fr/SearchingForSolutions.pdf)
* [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Victor Allis](Victor_Allis "Victor Allis"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1994**). *How to Mate: Applying Proof-Number Search*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), reprint as [Mate in 38: Applying Proof-Number Search](http://www.top-5000.nl/ps/Mate%20in%2038-%20applying%20proof%20number%20search%20to%20chess.pdf) from [Ed Schroder's](Ed_Schroder "Ed Schroder") [Programmer's Stuff site](http://www.top-5000.nl/prostuff.htm)
* [Victor Allis](Victor_Allis "Victor Allis"), [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1994**). *[Proof-Number Search](http://www.sciencedirect.com/science/article/pii/0004370294900043)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 66, No. 1
* [Martin Schijf](index.php?title=Martin_Schijf&action=edit&redlink=1 "Martin Schijf (page does not exist)"), [Victor Allis](Victor_Allis "Victor Allis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1994**). *Proof-Number Search and Transpositions*. [ICCA Journal, Vol. 17, No. 2](ICGA_Journal#17_2 "ICGA Journal")


### 1995 ...


* [Masahiro Seo](index.php?title=Masahiro_Seo&action=edit&redlink=1 "Masahiro Seo (page does not exist)") (**1995**). *The C\* Algorithm for AND/OR Tree Search and Its Application to a Tsume-Shogi Program*. M.Sc. thesis, [University of Tokyo](https://en.wikipedia.org/wiki/University_of_Tokyo), [ps](http://www-imai.is.s.u-tokyo.ac.jp/PAPERS/Seo95.ps)
* [Dennis Breuker](Dennis_Breuker "Dennis Breuker") (**1998**). *[Memory versus Search in Games](http://www.dennisbreuker.nl/thesis/index.html)*. Ph.D. thesis, [Maastricht University](Maastricht_University "Maastricht University"), Chapter 3: The proof-number search algorithm, Chapter 4: The pn2-search algorithm
* [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai") (**1998**). *A new AND/OR Tree Search Algorithm Using Proof Number and Disproof Number*. Complex Games Lab Workshop, Tsukuba
* [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai") (**1999**). *A New Depth-First-Search Algorithm for AND/OR Trees*. M.Sc. thesis, [University of Tokyo](https://en.wikipedia.org/wiki/University_of_Tokyo)
* [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai"), [Hiroshi Imai](Hiroshi_Imai "Hiroshi Imai") (**1999**). *Proof for the Equivalence Between Some Best-First Algorithms and Depth-First Algorithms for AND/OR Trees*. Proceedings of the Korea-Japan Joint Workshop on Algorithms and Computation
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**1999**). *Parallel AND/OR tree search based on proof and disproof numbers*. [5th Game Programming Workshop](Conferences#GPW "Conferences")
* [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai"), [Hiroshi Imai](Hiroshi_Imai "Hiroshi Imai") (**1999**). *Application of df-pn+ to Othello endgames*. [5th Game Programming Workshop](Conferences#GPW "Conferences") » [Othello](Othello "Othello")


### 2000 ...


* [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2000**). *[Abstract Proof Search](http://link.springer.com/chapter/10.1007/3-540-45579-5_3)*. [CG 2000](CG_2000 "CG 2000"), [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/APS-final.pdf)
* [Masahiro Seo](index.php?title=Masahiro_Seo&action=edit&redlink=1 "Masahiro Seo (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2001**). *The PN\*-Search Algorithm: Applications to Tsume-Shogi.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 129, Nos. 1-2
* [Makoto Sakuta](Makoto_Sakuta "Makoto Sakuta"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2001**). *The Performance of PN\*, PDS, and PN Search on 6x6 Othello and Tsume-Shogi*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
* [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *The PN2-Search Algorithm*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
* [Mark Winands](Mark_Winands "Mark Winands"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2001**). *PN, PN2 and PN\* in Lines of Action*. [6th Computer Olympiad Workshop](6th_Computer_Olympiad#Workshop "6th Computer Olympiad"), [pdf](https://dke.maastrichtuniversity.nl/m.winands/documents/PN_PN2_AND_PNstar_%20IN_LOA.pdf) » [Lines of Action](Lines_of_Action "Lines of Action")
* [Makoto Sakuta](Makoto_Sakuta "Makoto Sakuta"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2001**). *[AND/OR-tree Search Algorithms in Shogi Mating Search](http://ilk.uvt.nl/icga/journal/contents/content24-4.htm#AND/OR-TREE)*. [ICGA Journal, Vol. 24, No. 4](ICGA_Journal#24_4 "ICGA Journal")
* [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2001**). *Proof-Set Search*. Technical Report TR 01-09, [University of Alberta](University_of_Alberta "University of Alberta") [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.20.9972) <a id="cite-note-26" href="#cite-ref-26">[26]</a>
* [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2002**). *[Proof-Set Search](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_7)*. [CG 2002](CG_2002 "CG 2002")
* [Mark Winands](Mark_Winands "Mark Winands"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[PDS-PN: A New Proof-Number Search Algorithm: Application to Lines of Action](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_5)*. [CG 2002](CG_2002 "CG 2002") » [Lines of Action](Lines_of_Action "Lines of Action")
* [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai") (**2002**). *Df-pn Algorithm for Searching AND/OR Trees and Its Applications*. Ph.D. thesis, [University of Tokyo](https://en.wikipedia.org/wiki/University_of_Tokyo)
* [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai"), [Hiroshi Imai](Hiroshi_Imai "Hiroshi Imai") (**2002**). *[Proof for the Equivalence Between Some Best-First Algorithms and Depth-First Algorithms for AND/OR Trees](http://ci.nii.ac.jp/naid/110006376599)*. [IEICE transactions on information and systems](http://ci.nii.ac.jp/vol_issue/nels/AA10826272/ISS0000408668_en.html)
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2003**). *Df-pn in Go: An Application to the One-Eye Problem*. [Advances in Computer Games 10](Advances_in_Computer_Games_10 "Advances in Computer Games 10"), [pdf](http://www.fun.ac.jp/%7Ekishi/pdf_file/acg_kishimoto_mueller.pdf) » [Go](Go "Go") <a id="cite-note-27" href="#cite-ref-27">[27]</a>
* [Mark Winands](Mark_Winands "Mark Winands"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2004**). *An Effective Two-Level Proof-Number Search Algorithm*. [Theoretical Computer Science](http://www.sciencedirect.com/science/journal/03043975). Vol. 313, No.3, pp. 511-525. [ps](http://www.personeel.unimaas.nl/m-winands/documents/An%20Effective%20Two-Level%20Proof-Number%20Search%20Algorithm.ps)
* [Mark Winands](Mark_Winands "Mark Winands") (**2004**). *Informed Search in Complex Games*. Ph.D. thesis, [Universiteit Maastricht](Maastricht_University "Maastricht University"), Received the 2004 [ChessBase](ChessBase "ChessBase") [Best-Publication Award](ICGA#BestPublicationAwards "ICGA"), [pdf](http://www.personeel.unimaas.nl/m-winands/documents/informed_search.pdf), Chapter 4 - Proof-Number Search Algorithm, Chapter 5 - An Effective Two-Level Proof-Number Search Algorithm


### 2005 ...


* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto") (**2005**). *Correct and Efficient Search Algorithms in the Presence of Repetitions*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), Received the 2005 [ChessBase](ChessBase "ChessBase") [Best-Publication Award](ICGA#BestPublicationAwards "ICGA"), [pdf](http://www.is.titech.ac.jp/%7Ekishi/pdf_file/kishi_phd_thesis.pdf)
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2005**). *A Solution to the GHI Problem for Depth-First Proof-Number Search*. 7th Joint Conference on Information Sciences (JCIS2003), pp. 489 - 492, [pdf](http://webdocs.cs.ualberta.ca/~mmueller/ps/kishimoto-mueller-infsci-ghi.pdf) » [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Neil Burch](index.php?title=Neil_Burch&action=edit&redlink=1 "Neil Burch (page does not exist)"), [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Rob Lake](index.php?title=Rob_Lake&action=edit&redlink=1 "Rob Lake (page does not exist)"), [Paul Lu](Paul_Lu "Paul Lu"), [Steve Sutphen](index.php?title=Steve_Sutphen&action=edit&redlink=1 "Steve Sutphen (page does not exist)") (**2005**). *Solving Checkers*. [IJCAI 2005](Conferences#IJCAI2005 "Conferences"), [pdf](http://www.ru.is/faculty/yngvi/pdf/SchaefferBBKMLLS05.pdf)
* [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Sander Bakkes](index.php?title=Sander_Bakkes&action=edit&redlink=1 "Sander Bakkes (page does not exist)"), [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito") (**2006**). *Intelligent Search Techniques Proof-Number Search*. MICC/IKAT [Universiteit Maastricht](Maastricht_University "Maastricht University")
* [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito"), [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2006**). *[Monte-Carlo Proof-Number Search for Computer Go](http://link.springer.com/chapter/10.1007/978-3-540-75538-8_5)*. [CG 2006](CG_2006 "CG 2006")
* [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Łukasz Lew](index.php?title=%C5%81ukasz_Lew&action=edit&redlink=1 "Łukasz Lew (page does not exist)") (**2006**). *[Improving Depth-first PN-Search: 1 + ε Trick](http://link.springer.com/chapter/10.1007%2F978-3-540-75538-8_14)*. [CG 2006](CG_2006 "CG 2006"), [pdf](http://www.mimuw.edu.pl/~pan/papers/lm-pns.pdf)
* [Kazuki Yoshizoe](index.php?title=Kazuki_Yoshizoe&action=edit&redlink=1 "Kazuki Yoshizoe (page does not exist)"), [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"). (**2007**). *Lambda Depth-First Proof-Number Search and Its Application to Go*. [IJCAI 2007](Conferences#IJCAI2007 "Conferences"), [pdf](http://www.fun.ac.jp/%7Ekishi/pdf_file/yoshizoe-ijcai07.pdf)
* [Kazuki Yoshizoe](index.php?title=Kazuki_Yoshizoe&action=edit&redlink=1 "Kazuki Yoshizoe (page does not exist)") (**2008**). *[A New Proof-Number Calculation Technique for Proof-Number Search](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_13)*. [CG 2008](CG_2008 "CG 2008")
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2008**). *[About the Completeness of Depth-First Proof-Number Search](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_14)*. [CG 2008](CG_2008 "CG 2008")
* [Toru Ueda](index.php?title=Toru_Ueda&action=edit&redlink=1 "Toru Ueda (page does not exist)"), [Tsuyoshi Hashimoto](Tsuyoshi_Hashimoto "Tsuyoshi Hashimoto"), [Junichi Hashimoto](Junichi_Hashimoto "Junichi Hashimoto"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2008**). *[Weak Proof-Number Search](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_15)*. [CG 2008](CG_2008 "CG 2008")
* [Kazuki Yoshizoe](index.php?title=Kazuki_Yoshizoe&action=edit&redlink=1 "Kazuki Yoshizoe (page does not exist)") (**2009**). *AND-OR Tree Search Algorithms for Domains with Uniform Branching Factors*. Ph.D. thesis, [University of Tokyo](https://en.wikipedia.org/wiki/University_of_Tokyo)
* [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito"), [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2009**). *Randomized Parallel Proof-Number Search*. [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [pdf](http://wwwis.win.tue.nl/bnaic2009/papers/bnaic2009_paper_23.pdf)
* [Changming Xu](index.php?title=Changming_Xu&action=edit&redlink=1 "Changming Xu (page does not exist)"), [Zongmin Ma](index.php?title=Zongmin_Ma&action=edit&redlink=1 "Zongmin Ma (page does not exist)"), [Junjie Tao](index.php?title=Junjie_Tao&action=edit&redlink=1 "Junjie Tao (page does not exist)"), [Xinhe Xu](Xinhe_Xu "Xinhe Xu") (**2009**). *Enhancements of Proof Number Search in Connect6*. [IEEE](IEEE "IEEE") Control and Decision Conference


### 2010 ...


* [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2010**). *Relevance-Zone-Oriented Proof Search for Connect6*. Ph.D. thesis
* [Mark Winands](Mark_Winands "Mark Winands"), [Maarten Schadd](index.php?title=Maarten_Schadd&action=edit&redlink=1 "Maarten Schadd (page does not exist)") (**2010**). *[Evaluation-Function Based Proof-Number Search](http://link.springer.com/chapter/10.1007%2F978-3-642-17928-0_3)*. [CG 2010](CG_2010 "CG 2010"), [pdf](https://dke.maastrichtuniversity.nl/m.winands/documents/CG2010pneval.pdf)
* [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Hung-Hsuan Lin](Hung-Hsuan_Lin "Hung-Hsuan Lin"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin"), [Der-Johng Sun](Der-Johng_Sun "Der-Johng Sun"), [Yi-Chih Chan](Yi-Chih_Chan "Yi-Chih Chan"), [Bo-Ting Chen](index.php?title=Bo-Ting_Chen&action=edit&redlink=1 "Bo-Ting Chen (page does not exist)") (**2010**). *[Job-Level Proof-Number Search for Connect6](http://link.springer.com/chapter/10.1007/978-3-642-17928-0_2)*. [CG 2010](CG_2010 "CG 2010")
* [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2010**). *Relevance-Zone-Oriented Proof Search for Connect6*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 2, No. 3 » [Connect6](Connect6 "Connect6")
* [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang") (**2010**). *[Searching for Stage Proof Number in Connect6](https://www.semanticscholar.org/paper/Searching-for-Stage-Proof-Number-in-Connect6-Yen-Yang/2de70372893e8773b12391f75d2b964ea7fb6df2)*. [TAAI 2010](index.php?title=TAAI_2010&action=edit&redlink=1 "TAAI 2010 (page does not exist)")
* [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2010**). *Parallel Depth First Proof Number Search*. [AAAI 2010](http://www.informatik.uni-trier.de/~ley/db/conf/aaai/aaai2010.html#Kaneko10)
* [Abdallah Saffidine](Abdallah_Saffidine "Abdallah Saffidine"), [Nicolas Jouandeau](index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2011**). *Solving Breakthrough with Race Patterns and Job-Level Proof Number Search*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13") » [Breakthrough (Game)](Breakthrough_(Game) "Breakthrough (Game)")
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Mark Winands](Mark_Winands "Mark Winands"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito") (**2012**). *Game-Tree Search using Proof Numbers: The First Twenty Years*. [ICGA Journal, Vol. 35, No. 3](ICGA_Journal#35_3 "ICGA Journal")
* [Abdallah Saffidine](Abdallah_Saffidine "Abdallah Saffidine") (**2012**). *Minimal Proof Search for Modal Logic K Model Checking*. [CoRR, July 2012](http://www.informatik.uni-trier.de/~ley/db/journals/corr/corr1207.html#abs-1207-1832) <a id="cite-note-28" href="#cite-ref-28">[28]</a>
* [Abdallah Saffidine](Abdallah_Saffidine "Abdallah Saffidine"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2012**). *Multiple-Outcome Proof Number Search*. [ECAI 2012](http://www.informatik.uni-trier.de/~ley/db/conf/ecai/ecai2012.html#SaffidineC12)
* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito") (**2013**). *Parallel Dovetailing and its Application to Depth-First Proof-Number Search*. [ICGA Journal, Vol. 36, No. 1](ICGA_Journal#36_1 "ICGA Journal") <a id="cite-note-29" href="#cite-ref-29">[29]</a>
* [Abdallah Saffidine](Abdallah_Saffidine "Abdallah Saffidine") (**2013**). *Solving Games and All That*. Ph.D. thesis, 2.4 Proof Number Search
* [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Hung-Hsuan Lin](Hung-Hsuan_Lin "Hung-Hsuan Lin"), [Der-Johng Sun](Der-Johng_Sun "Der-Johng Sun"), [Kuo-Yuan Kao](Kuo-Yuan_Kao "Kuo-Yuan Kao"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin"), [Yi-Chih Chan](Yi-Chih_Chan "Yi-Chih Chan"), [Bo-Ting Chen](index.php?title=Bo-Ting_Chen&action=edit&redlink=1 "Bo-Ting Chen (page does not exist)") (**2013**). *Job-Level Proof Number Search*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 5, No. 1
* [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2013**). *Scalable Parallel DFPN Search*. [CG 2013](CG_2013 "CG 2013"), [pdf](https://webdocs.cs.ualberta.ca/~hayward/papers/pawlhayw.pdf)
* [Mark Watkins](Mark_Watkins "Mark Watkins") (**2014**). *Solved Openings in Losing Chess*. [ICGA Journal, Vol. 37, No. 2](ICGA_Journal#37_2 "ICGA Journal") » [Losing Chess](Losing_Chess "Losing Chess")


### 2015 ...


* [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2015**). *Reducing the Seesaw Effect with Deep Proof Number Search*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14")
* [Jiaxing Song](index.php?title=Jiaxing_Song&action=edit&redlink=1 "Jiaxing Song (page does not exist)") (**2017**). *Deep df-pn and its Efficient Implementations*. [Advances in Computer Games 15](Advances_in_Computer_Games_15 "Advances in Computer Games 15")
* [Chao Gao](index.php?title=Chao_Gao&action=edit&redlink=1 "Chao Gao (page does not exist)"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2017**). *Focused Depth-first Proof Number Search using Convolutional Neural Networks for the Game of Hex*. [IJCAI 2017](Conferences#IJCAI2017 "Conferences")


## Forum Posts


* [Re: One mate to solve...(proof number search results)](https://www.stmintz.com/ccc/index.php?id=169978) by Angrim, [CCC](CCC "CCC"), May 16, 2001
* [Re: A new(?) technique to recognize draws](https://www.stmintz.com/ccc/index.php?id=233322) by [Dan Andersson](index.php?title=Dan_Andersson&action=edit&redlink=1 "Dan Andersson (page does not exist)"), [CCC](CCC "CCC"), June 01, 2002
* [Proof number & conspiracy search](https://www.stmintz.com/ccc/index.php?id=248605) by Eli Liang, [CCC](CCC "CCC"), August 29, 2002
* [Mixing alpha-beta with PN search](https://www.stmintz.com/ccc/index.php?id=343084) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), January 18, 2004 » [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Upper bound on proof tree size](http://www.talkchess.com/forum/viewtopic.php?t=52936) by Forrest Hoch, [CCC](CCC "CCC"), July 11, 2014
* [Proof-number search](http://www.talkchess.com/forum/viewtopic.php?t=61774) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 20, 2016 » [Crazyhouse](Crazyhouse "Crazyhouse")


## External Links


* [Proof-number search from Wikipedia](https://en.wikipedia.org/wiki/Proof-number_search)


### Proof


* [Proof from Wikipedia](https://en.wikipedia.org/wiki/Proof)
* [Formal proof from Wikipedia](https://en.wikipedia.org/wiki/Formal_proof)
* [Mathematical proof from Wikipedia](https://en.wikipedia.org/wiki/Mathematical_proof)


 [List of mathematical proofs from Wikipedia](https://en.wikipedia.org/wiki/List_of_mathematical_proofs)
* [Automated theorem proving from Wikipedia](https://en.wikipedia.org/wiki/Automated_theorem_proving)
* [Combinatorial proof from Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_proof)


 [Bijective proof from Wikipedia](https://en.wikipedia.org/wiki/Bijective_proof)
* [Mathematical induction from Wikipedia](https://en.wikipedia.org/wiki/Mathematical_induction)
* [Proof by exhaustion from Wikipedia](https://en.wikipedia.org/wiki/Proof_by_exhaustion)
* [Proof theory from Wikipedia](https://en.wikipedia.org/wiki/Proof_theory)
* [Proof calculus from Wikipedia](https://en.wikipedia.org/wiki/Proof_calculus)
* [Method of analytic tableaux from Wikipedia](https://en.wikipedia.org/wiki/Method_of_analytic_tableaux)


### Misc


* [Marcus Miller](Category:Marcus_Miller "Category:Marcus Miller") & [Herbie Hancock's](Category:Herbie_Hancock "Category:Herbie Hancock") [Headhunters'05](Category:The_Headhunters "Category:The Headhunters") - [Actual Proof](https://en.wikipedia.org/wiki/Thrust_%28album%29), Live at [Tokyo Jazz 2005](http://tokyo-jazz.com/2005/english/index.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Terri Lyne Carrington](Category:Terri_Lyne_Carrington "Category:Terri Lyne Carrington"), [Roy Hargrove](Category:Roy_Hargrove "Category:Roy Hargrove"), [Munyungo Jackson](http://www.discogs.com/artist/256492-Munyungo-Jackson), [Lionel Loucke](https://en.wikipedia.org/wiki/Lionel_Loueke), [Wah Wah Watson](https://en.wikipedia.org/wiki/%27Wah_Wah%27_Watson) 
 
* [Herbie Hancock](Category:Herbie_Hancock "Category:Herbie Hancock"): [The Imagine Project](https://en.wikipedia.org/wiki/The_Imagine_Project) - [Actual Proof](https://en.wikipedia.org/wiki/Thrust_%28album%29), [Montreux Jazz Festival](https://en.wikipedia.org/wiki/Montreux_Jazz_Festival), July 16, 2010, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Tal Wilkenfeld](Category:Tal_Wilkenfeld "Category:Tal Wilkenfeld"), [Greg Phillinganes](Category:Greg_Phillinganes "Category:Greg Phillinganes"), [Vinnie Colaiuta](Category:Vinnie_Colaiuta "Category:Vinnie Colaiuta"), [Lionel Loueke](https://en.wikipedia.org/wiki/Lionel_Loueke)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Tree Nursery, [The Phillips Collection](https://en.wikipedia.org/wiki/The_Phillips_Collection), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Victor Allis](Victor_Allis "Victor Allis") (**1994**). *Searching for Solutions in Games and Artificial Intelligence*. Ph.D. thesis, [University of Limburg](Maastricht_University "Maastricht University"), [pdf](http://fragrieu.free.fr/SearchingForSolutions.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Victor Allis](Victor_Allis "Victor Allis"), [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1994**). *[Proof-Number Search](http://www.sciencedirect.com/science/article/pii/0004370294900043)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 66, No. 1
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Mark Winands](Mark_Winands "Mark Winands"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito") (**2012**). *Game-Tree Search using Proof Numbers: The First Twenty Years*. [ICGA Journal, Vol. 35, No. 3](ICGA_Journal#35_3 "ICGA Journal")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2012**). *All is Proof Numbers*. [ICGA Journal, Vol. 35, No. 3](ICGA_Journal#35_3 "ICGA Journal") (editorial)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Mark Winands](Mark_Winands "Mark Winands"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito") (**2012**). *Game-Tree Search using Proof Numbers: The First Twenty Years*. [ICGA Journal, Vol. 35, No. 3](ICGA_Journal#35_3 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Victor Allis](Victor_Allis "Victor Allis") (**1994**). *Searching for Solutions in Games and Artificial Intelligence*. Ph.D. thesis, [University of Limburg](Maastricht_University "Maastricht University")
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Mark Winands](Mark_Winands "Mark Winands"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito") (**2012**). *Game-Tree Search using Proof Numbers: The First Twenty Years*. [ICGA Journal, Vol. 35, No. 3](ICGA_Journal#35_3 "ICGA Journal")
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Martin Schijf](index.php?title=Martin_Schijf&action=edit&redlink=1 "Martin Schijf (page does not exist)") (**1993**). *Proof-number Search and Transpositions*. M.Sc. thesis, [Leiden University](Leiden_University "Leiden University")
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Dennis Breuker](Dennis_Breuker "Dennis Breuker") (**1998**). *[Memory versus Search in Games](http://www.dennisbreuker.nl/thesis/index.html)*. Ph.D. thesis, [Maastricht University](Maastricht_University "Maastricht University"), Chapter 4: The pn2-search algorithm
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Masahiro Seo](index.php?title=Masahiro_Seo&action=edit&redlink=1 "Masahiro Seo (page does not exist)") (**1995**). *The C\* Algorithm for AND/OR Tree Search and Its Application to a Tsume-Shogi Program*. M.Sc. thesis, [University of Tokyo](https://en.wikipedia.org/wiki/University_of_Tokyo), [ps](http://www-imai.is.s.u-tokyo.ac.jp/PAPERS/Seo95.ps)
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Masahiro Seo](index.php?title=Masahiro_Seo&action=edit&redlink=1 "Masahiro Seo (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2001**). *The PN\*-Search Algorithm: Applications to Tsume-Shogi.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 129, Nos. 1-2
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Richard Korf](Richard_Korf "Richard Korf") (**1993**). *Linear-Space Best-First Search.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 62, No. 1, [pdf](http://www.aaai.org/Papers/AAAI/1992/AAAI92-082.pdf)
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai") (**2002**). *Df-pn Algorithm for Searching AND/OR Trees and Its Applications*. Ph.D. thesis, [University of Tokyo](https://en.wikipedia.org/wiki/University_of_Tokyo)
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Mark Winands](Mark_Winands "Mark Winands"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *PDS-PN: A new proofnumber search algorithm: Application to Lines of Action*. [CG 2002](CG_2002 "CG 2002"), [pdf](http://www.personeel.unimaas.nl/m-winands/documents/PDSPNCG2002.pdf)
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**1999**). *Parallel AND/OR tree search based on proof and disproof numbers*. [5th Game Programming Workshop](Conferences#GPW "Conferences")
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2010**). *Parallel Depth First Proof Number Search*. [AAAI 2010](http://www.informatik.uni-trier.de/~ley/db/conf/aaai/aaai2010.html#Kaneko10)
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Mark Winands](Mark_Winands "Mark Winands"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito") (**2012**). *Game-Tree Search using Proof Numbers: The First Twenty Years*. [ICGA Journal, Vol. 35, No. 3](ICGA_Journal#35_3 "ICGA Journal")
19. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Victor Allis](Victor_Allis "Victor Allis") (**1988**). *A Knowledge-Based Approach of Connect Four: The Game is Over, White to Move Wins*. M.Sc. thesis, Report No. IR-163, Faculty of Mathematics and Computer Science, [Vrije Universteit, Amsterdam](https://en.wikipedia.org/wiki/Vrije_Universiteit)
20. <a id="cite-ref-20" href="#cite-note-20">↑</a> [Charles Elkan](Charles_Elkan "Charles Elkan") (**1989**). *Conspiracy Numbers and Caching for Searching And/Or Trees and Theorem-Proving*. [IJCAI 1989](Conferences#IJCAI "Conferences"), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-89-VOL1/PDF/054.pdf)
21. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2003**). *Df-pn in Go: An Application to the One-Eye Problem*. [Advances in Computer Games 10](Advances_in_Computer_Games_10 "Advances in Computer Games 10"), [pdf](http://www.fun.ac.jp/%7Ekishi/pdf_file/acg_kishimoto_mueller.pdf)
22. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Neil Burch](index.php?title=Neil_Burch&action=edit&redlink=1 "Neil Burch (page does not exist)"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Rob Lake](index.php?title=Rob_Lake&action=edit&redlink=1 "Rob Lake (page does not exist)"), [Paul Lu](Paul_Lu "Paul Lu"), [Steve Sutphen](index.php?title=Steve_Sutphen&action=edit&redlink=1 "Steve Sutphen (page does not exist)") (**2007**). *[Checkers is Solved](http://www.sciencemag.org/content/317/5844/1518.abstract)*. [Science](https://en.wikipedia.org/wiki/Science_%28journal%29), Vol. 317, no. 5844
23. <a id="cite-ref-23" href="#cite-note-23">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Neil Burch](index.php?title=Neil_Burch&action=edit&redlink=1 "Neil Burch (page does not exist)"), [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Rob Lake](index.php?title=Rob_Lake&action=edit&redlink=1 "Rob Lake (page does not exist)"), [Paul Lu](Paul_Lu "Paul Lu"), [Steve Sutphen](index.php?title=Steve_Sutphen&action=edit&redlink=1 "Steve Sutphen (page does not exist)") (**2005**). *Solving Checkers*. [IJCAI 2005](Conferences#IJCAI2005 "Conferences")
24. <a id="cite-ref-24" href="#cite-note-24">↑</a> [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Victor Allis](Victor_Allis "Victor Allis"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1994**). *How to Mate: Applying Proof-Number Search*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), reprint as [Mate in 38: Applying Proof-Number Search](http://www.top-5000.nl/ps/Mate%20in%2038-%20applying%20proof%20number%20search%20to%20chess.pdf) from [Ed Schroder's](Ed_Schroder "Ed Schroder") [Programmer's Stuff site](http://www.top-5000.nl/prostuff.htm)
25. <a id="cite-ref-25" href="#cite-note-25">↑</a> [Sjeng : Download / proof.c](http://sjeng.org/download.html)
26. <a id="cite-ref-26" href="#cite-note-26">↑</a> [Re: A new(?) technique to recognize draws](https://www.stmintz.com/ccc/index.php?id=233322) by [Dan Andersson](index.php?title=Dan_Andersson&action=edit&redlink=1 "Dan Andersson (page does not exist)"), [CCC](CCC "CCC"), June 01, 2002
27. <a id="cite-ref-27" href="#cite-note-27">↑</a> [Tsumego at Sensei's Library](http://senseis.xmp.net/?Tsumego)
28. <a id="cite-ref-28" href="#cite-note-28">↑</a> [Modal logic from Wikipedia](https://en.wikipedia.org/wiki/Modal_logic)
29. <a id="cite-ref-29" href="#cite-note-29">↑</a> [Dovetailing (computer science) from Wikipedia](https://en.wikipedia.org/wiki/Dovetailing_%28computer_science%29)

**[Up one level](Search "Search")**







 
