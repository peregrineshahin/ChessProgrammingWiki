---
title: Backtracking8QinBitboards
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Algorithms](Algorithms "Algorithms") * Backtracking**

\[
**Backtracking**,

a general search algorithm for finding solutions of certain [computational problems](https://en.wikipedia.org/wiki/Computational_problem). It incrementally builds candidates to a solution, and "backtracks" a partial candidate as soon as it determines it cannot become member of the solution. Therefor backtracking algorithms, most often implemented as [recursive](Recursion "Recursion") [depth-first](Depth-First "Depth-First") algorithm, are not considered [brute-force](Brute-Force "Brute-Force"), and have the advantage of potentially requiring a search tree with less nodes.

## History

[Bitner](Mathematician#JRBitner "Mathematician") and [Reingold](Mathematician#EMReingold "Mathematician") <a id="cite-note-2" href="#cite-ref-2">[2]</a> credit [Derrick H. Lehmer](Mathematician#DHLehmer "Mathematician") with first using the term 'backtrack' in the 1950s, but it has been discovered and rediscovered many times. [Robert J. Walker](Mathematician#RJWalker "Mathematician") <a id="cite-note-3" href="#cite-ref-3">[3]</a> was the first who called using a well-known depth-first procedure Backtracking in 1960.

## Applications

Classic examples of using backtracking algorithms are solving [Exact cover problems](https://en.wikipedia.org/wiki/Exact_cover) and [Tour puzzles](https://en.wikipedia.org/wiki/Tour_puzzle), like the [Eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle), the [Knight's tour puzzle](https://en.wikipedia.org/wiki/Knight%27s_tour) and other [Maze](https://en.wikipedia.org/wiki/Maze) or [Labyrinth](https://en.wikipedia.org/wiki/Labyrinth) puzzles. [Knuth's](Donald_Knuth "Donald Knuth") [Algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) along with [Dancing Links](https://en.wikipedia.org/wiki/Dancing_Links) finds all solutions to an exact cover problem. Backtracking is further applied to solving [Constraint satisfaction problems](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem), such as [Crossword puzzles](https://en.wikipedia.org/wiki/Crosswords), [Sudoku](https://en.wikipedia.org/wiki/Sudoku), [Pentomino](https://en.wikipedia.org/wiki/Pentomino) tiling, [boolean satisfiability problems](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) and other [NP-complete problems](https://en.wikipedia.org/wiki/NP-complete). [Logic programming languages](https://en.wikipedia.org/wiki/Logic_programming) such as [Prolog](index.php?title=Prolog&action=edit&redlink=1 "Prolog (page does not exist)") internally use backtracking to generate answers.

## De Bruijn Sequences

A further sample is to find [De Bruijn sequences](De_Bruijn_Sequence "De Bruijn Sequence"), as demonstrated by the recursive [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator"). Here early partial candidates may be discarded if the lock indicates a new six-bit number already occured before.

## Looking for Magics

Unfortunately, [looking for magics](Looking_for_Magics "Looking for Magics") to find factors for the application of [Magic Bitboards](Magic_Bitboards "Magic Bitboards"), seems not to fit into a class of these kind of problems. Here [trial and error](Trial_and_Error "Trial and Error") with spare populated, but otherwise randomly chosen numbers is used.

## 8Q in Bitboards

"Thinking" [Bitboards](Bitboards "Bitboards"), [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") made following [Eight queens](https://en.wikipedia.org/wiki/Eight_queens_puzzle) <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> proposal, to traverse [ranks](Ranks "Ranks") as disjoint candidate sets for one [queen](Queen "Queen") each, with premature elimination of redundant tests <a id="cite-note-6" href="#cite-ref-6">[6]</a> of [squares](Squares "Squares") already [attacked](Sliding_Piece_Attacks "Sliding Piece Attacks") by queens put on the board . Therefor, while [serializing](Bitboard_Serialization "Bitboard Serialization") the set of not attacked candidate squares from one rank to put a queen on it, it maintains a "taboo" [union set](General_Setwise_Operations#Union "General Setwise Operations") for consequent queens on upper ranks by "oring" [queen attacks](On_an_empty_Board "On an empty Board") in [north](On_an_empty_Board#PositiveRays "On an empty Board") [directions](Direction "Direction"). It performs some optimization to keep the processed rank always the first, to only use a lookup [array](Array "Array") of queen attacks of that first rank, and to [shift](General_Setwise_Operations#ShiftingBitboards "General Setwise Operations") the taboo-set consecutively [one rank down](General_Setwise_Operations#OneStepOnly "General Setwise Operations"). A little [space-time tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff") saves the [bitscan](BitScan "BitScan") at the cost of some more [memory](Memory "Memory") to index the eight attacks from an [sparse array](https://en.wikipedia.org/wiki/Sparse_array) of 129 bitboards with the [single isolated](General_Setwise_Operations#LS1BIsolation "General Setwise Operations") [bit](Bit "Bit") inside one [byte](Byte "Byte") (the first rank).

### Code

The sample [C](C "C") code demonstrates an [iterative solution](Iteration "Iteration") using [arrays](Array "Array") as explicit [stacks](Stack "Stack") on the stack:

```C++
typedef unsigned char U8;

/**
 * eightQueen Bitboard implementation
 * @author Gerd Isenberg
 * @date April 29, 2011
 */
void eightQueenBitboard(*U64 taboo */ ) {
   U64 t[8];             /* stack of taboo bitboards */
   U8  q[8], c[8];       /* stack of queens and candidate squares */
   unsigned int p = 0;   /* ply, queen index 0..7 as "stack pointer" */
   t[0] = 0;             /* no square attacked so far (taboo) */

C: c[p] = ~(U8)t[p];     /* 1. rank squares not attacked */
   while ( c[p] ) {      /* while candidate squares */
      q[p] = c[p]&-c[p]; /* LS1B -> 1,2,4,8,16,32,64,128 */
      if ( p == 7 ) {
         print8Q( q );   /* solution found */
      } else {           /* "or" attacks to taboo, shift it  */
         t[p+1] = (t[p] | nAtt[q[p]]) >> 8; /* one rank down */
         ++p; goto C;    /* make "recursive call" iterative  */
R:       p--;
      }
      c[p] ^= q[p];      /* reset candidate square */
   }
   if ( p ) goto R;      /* return from iterative "call" */
}

```

### Node Counts

The algorithm backtracks all [92 distinct Eight queen solutions](https://en.wikipedia.org/wiki/Eight_queens_puzzle#Constructing_a_solution). Using an **if do-while else** construct instead of **while** control structure allows counting "pruned" [nodes](Node "Node"), where the candidate set is initially empty in the else case, leaving following node statistics differentiated by ply (excluding the [root](Root "Root")):

|  Ply
|  Nodes
|  Pruned
|  Sum
|
| --- | --- | --- | --- |
|  0
|  8
|  0
|  8
|
|  1
|  42
|  0
|  42
|
|  2
|  140
|  0
|  140
|
|  3
|  344
|  0
|  344
|
|  4
|  568
|  18
|  586
|
|  5
|  550
|  150
|  700
|
|  6
|  312
|  256
|  568
|
|  7
| **92** |  220
|  312
|
|  Sum
|  2056
|  644
|  2700
|

### Data and Print

The declaration of the north attack array to save a byte-wise [bitscan](BitScan "BitScan"), and for convenience the print routine used:

```C++
/**
 * north | nw | ne attacks of a queen on the 1. rank
 *
 * indexed by a first rank - bitboard
 * with one bit set, representing the file
 * 1,2,4,8,16,32,64,128
 */
static const U64 nAtt[130] = {
   0,
   C64(0x8141211109050300), /*   1 */
   C64(0x02824222120A0700), /*   2 */
   0,
   C64(0x0404844424150E00), /*   4 */
   0,0,0,
   C64(0x08080888492A1C00), /*   8 */
   0,0,0,0,0,0,0,
   C64(0x1010101192543800), /*  16 */
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
   C64(0x2020212224A87000), /*  32 */
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
   C64(0x404142444850E000), /*  64 */
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
   C64(0x8182848890A0C000), /* 128 */
   0
};

/**
 * printing 8q boards
 */
void print8Q( unsigned char q8[] ) {
   static int count=1;
   int r, f, b;
   printf("NQ %d\n", count++ );
   for (r=7; r >= 0; --r) { /* 8th rank top */
      for ( f=0, b=1; f < 8; ++f, b <<= 1) {
         printf("%c ", (q8[r] & b) ? 'Q' : '.');
      }
      printf("\n");
   }
   printf("\n");
}

```

## N Queens

### By Marcel van Kervinck

A very short and therefor slightly obfuscated, but elegant and tricky general backtracker in enumerating N Queen solutions is given by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") in two lines of [C](C "C") code, Version 2, 1996 <a id="cite-note-7" href="#cite-ref-7">[7]</a>, [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling") as its best:

```C++
t(a,b,c){int d=0,e=a&~b&~c,f=1;if(a)for(f=0;e-=d,d=e&-e;f+=t(a-d,(b+d)*2,(
c+d)/2));return f;}main(q){scanf("%d",&q);printf("%d\n",t(~(~0<<q),0,0));}

```

### By Tony Lezard

As mentioned by Marcel van Kervinck, a similar 8 Queen program was introduced by Tony Lezard in 1991 <a id="cite-note-8" href="#cite-ref-8">[8]</a>:

```C++
static int count = 0;

void try(int row, int left, int right) {
   int poss, place;
   if (row == 0xFF) ++count;
   else {
      poss = ~(row|left|right) & 0xFF;
      while (poss != 0) {
         place = poss & -poss;
         try(row|place, (left|place)<<1, (right|place)>>1);
         poss &= ~place;
      }
   }
}

void main() {   
   try(0,0,0);
   printf("There are %d solutions.\n", count);
}

```

## See also

- [Brute-Force](Brute-Force "Brute-Force")
- [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator")
- [Depth-First](Depth-First "Depth-First")
- [Iterative Search](Iterative_Search "Iterative Search")
- [Looking for Magics](Looking_for_Magics "Looking for Magics")
- [Prolog](index.php?title=Prolog&action=edit&redlink=1 "Prolog (page does not exist)")
- [Recursion](Recursion "Recursion")
- [Search](Search "Search")
- [Trial and Error](Trial_and_Error "Trial and Error")

## Publications

## 1960 ...

- [Robert J. Walker](Mathematician#RJWalker "Mathematician") (**1960**). *An Enumerative Technique for a Class of Combinatorial Problems*. [Proceedings of Symposia in Applied Mathematics, Vol. X, Combinatorial Analysis](http://www.bibliopolis.com/main/books/caliban_0036592.html), [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") and [Marshall Hall, Jr.](Mathematician#MHallJr "Mathematician"), eds., [American Mathematical Society](https://en.wikipedia.org/wiki/American_Mathematical_Society), [Providence, Rhode Island](https://en.wikipedia.org/wiki/Providence,_RI), pp. 91-94
- [Solomon W. Golomb](Mathematician#SMGolomb "Mathematician"), [Leonard D. Baumert](Mathematician#LDBaumert "Mathematician") (**1965**). *[Backtrack Programming](http://portal.acm.org/citation.cfm?id=321300&dl=ACM&coll=DL)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 12, No. 4
- [Martin Gardner](Martin_Gardner "Martin Gardner") (**1969, 1991**). *The Unexpected Hanging and Other Mathematical Diversions*. [Simon & Schuster](https://en.wikipedia.org/wiki/Simon_%26_Schuster), [University Of Chicago Press](https://en.wikipedia.org/wiki/University_of_Chicago_Press).

## Chapter 16: *The Eight Queens and Other Chessboard Diversions*. 1970 ...

- [Mark B. Wells](Mathematician#MBWells "Mathematician") (**1971**). *Elements of Combinatorial Computing*. [Pergamon Press](https://en.wikipedia.org/wiki/Pergamon_Press), [amazon.com](http://www.amazon.com/Elements-combinatorial-computing-Mark-Wells/dp/B0000EG7JI)
- [James R. Bitner](Mathematician#JRBitner "Mathematician"), [Edward M. Reingold](Mathematician#EMReingold "Mathematician") (**1975**). *[Backtrack Programming Techniques](http://portal.acm.org/citation.cfm?id=361224&dl=ACM&coll=DL&CFID=18128359&CFTOKEN=31610180)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 18, No. 11 <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Donald Knuth](Donald_Knuth "Donald Knuth") (**1974**). *Estimating efficiency of backtrack programs*. STAN-CS-74-442, CS-Department, [Stanford University](Stanford_University "Stanford University") <a id="cite-note-10" href="#cite-ref-10">[10]</a>
- [Donald Knuth](Donald_Knuth "Donald Knuth") (**1975**). *[Estimating the Efficiency of Backtrack Programs](http://www.ams.org/journals/mcom/1975-29-129/S0025-5718-1975-0373371-6/home.html)*. [Mathemathics of Computation](http://www.ams.org/publications/journals/journalsframework/mcom), Vol. 29
- [Nissim Francez](http://www.cs.technion.ac.il/%7Efrancez/), [Boris Klebansky](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/k/Klebansky:Boris.html), [Amir Pnueli](https://en.wikipedia.org/wiki/Amir_Pnueli) (**1977**). *Backtracking in Recursive Computations*. [Acta Informatica Vol. 8, No. 2](http://ftp.math.utah.edu/pub//tex/bib/toc/actainfo.html#8%282%29:May:1977)
- [John Gaschnig](John_Gaschnig "John Gaschnig") (**1977**). *[A General Backtrack Algorithm That Eliminates Most Redundant Tests](https://dl.acm.org/citation.cfm?id=1624534)*. [IJCAI 1977](Conferences#IJCAI1977 "Conferences")
- [Hirosi Hitotumatua](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/h/Hitotumatu:Hirosi.html), [Kohei Noshita](index.php?title=Kohei_Noshita&action=edit&redlink=1 "Kohei Noshita (page does not exist)") (**1979**). *[A technique for implementing backtrack algorithms and its application](http://portal.acm.org/citation.cfm?id=1710829)*. [Information Processing Letters](https://en.wikipedia.org/wiki/Information_Processing_Letters) Vol. 8, No. 4
- [Gary Lindstrom](Gary_Lindstrom "Gary Lindstrom") (**1979**). *[Backtracking in a Generalized Control Setting](http://dl.acm.org/citation.cfm?id=357063)*. [ACM Transactions on Programming Languages and Systems](ACM#TOPLAS "ACM"), Vol. 1, No. 1

## 1980 ...

- [Paul W. Purdom](Paul_W._Purdom "Paul W. Purdom"), [Cynthia A. Brown](Mathematician#CABrown "Mathematician"), [Edward L. Robertson](https://www.cs.indiana.edu/%7Eedrbtsn/) (**1981**). *Backtracking with Multi-Level Dynamic Search Rearrangement*. [Acta Informatica Vol. 15, No. 2](http://ftp.math.utah.edu/pub//tex/bib/toc/actainfo.html#15%282%29:December:1981)
- [Robert A. Wagner](Robert_A._Wagner "Robert A. Wagner"), [Robert Geist](Mathematician#RGeist "Mathematician") (**1984**). *The Crippled Queen Placement Problem*. [Science of Computer Programming, Vol. 4](https://dblp.uni-trier.de/db/journals/scp/scp4.html), No. 3, [pdf](https://core.ac.uk/download/pdf/82594002.pdf)
- [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Ewald Speckenmeyer](Ewald_Speckenmeyer "Ewald Speckenmeyer") (**1986**). *Superlinear Speedup for Parallel Backtracking.* Technical Report 30, [Paderborn University](Paderborn_University "Paderborn University")
- [Andrew Appel](index.php?title=Andrew_Appel&action=edit&redlink=1 "Andrew Appel (page does not exist)"), [Guy Jacobson](index.php?title=Guy_Jacobson&action=edit&redlink=1 "Guy Jacobson (page does not exist)") (**1988**). *The World’s Fastest Scrabble Program*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 31, No. 5, [pdf](https://pdfs.semanticscholar.org/da31/cb24574f7c881a5dbf008e52aac7048c9d9c.pdf) » [Scrabble](index.php?title=Scrabble&action=edit&redlink=1 "Scrabble (page does not exist)")

## 1990 ...

- [Ilan Vardi](Ilan_Vardi "Ilan Vardi") (**1991**). *Computational Recreations in Mathematica*. Redwood City, CA: Addison-Wesley, ISBN 0201529890, [amazon.com](http://www.amazon.com/Computational-Recreations-Mathematica-Ilan-Vardi/dp/0201529890)
- [Matthew L. Ginsberg](Matthew_L._Ginsberg "Matthew L. Ginsberg") (**1993**). *[Dynamic Backtracking](http://www.jair.org/papers/paper1.html)*. [JAIR Vol. 1](http://www.jair.org/vol/vol1.html)
- [Patrick Prosser](https://en.wikipedia.org/wiki/Patrick_Prosser) (**1993**). *[Hybrid Algorithms for the Constraint Satisfaction Problem](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-8640.1993.tb00310.x)*. [Computational Intelligence](<https://en.wikipedia.org/wiki/Computational_Intelligence_(journal)>), Vol. 9, No. 3
- [Richard Karp](Richard_Karp "Richard Karp"), [Yanjun Zhang](Yanjun_Zhang "Yanjun Zhang") (**1993**). *[Randomized parallel algorithms for backtrack search and branch-and-bound computation](http://dl.acm.org/citation.cfm?id=174130.174145&coll=DL&dl=GUIDE&CFID=67253533&CFTOKEN=20355103)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 40, No. 3 <a id="cite-note-11" href="#cite-ref-11">[11]</a>
- [Matthew L. Ginsberg](Matthew_L._Ginsberg "Matthew L. Ginsberg"), [David McAllester](David_McAllester "David McAllester") (**1994**). *GSAT and Dynamic Backtracking*. [KR 1994](http://www.informatik.uni-trier.de/~ley/db/conf/kr/kr94.html#GinsbergM94) <a id="cite-note-12" href="#cite-ref-12">[12]</a>
- [Peter Sanders](Peter_Sanders "Peter Sanders") (**1995**). *Better Algorithms for Parallel Backtracking*. [IRREGULAR 1995](http://www.informatik.uni-trier.de/~ley/db/conf/irregular/irregular95.html#HoppS95)
- [Paul W. Purdom](Paul_W._Purdom "Paul W. Purdom"), [G. Neil Haven](https://dblp.uni-trier.de/pid/15/2493.html) (**1996**). *Backtracking and Probing*. [Satisfiability Problem: Theory and Applications 1996](https://dblp.uni-trier.de/db/conf/dimacs/dimacs35.html#PurdomH96), [pdf](https://www.academia.edu/22023319/Backtracking_and_probing)
- [Basil Vandegriend](https://github.com/basilv), [Joe Culberson](Joe_Culberson "Joe Culberson") (**1998**). *[The Gn, m Phase Transition is Not Hard for the Hamiltonian Cycle Problem](https://www.jair.org/index.php/jair/article/view/10213)*. [JAIR](https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_Research), Vol. 9, [arXiv:1105.5443](https://arxiv.org/abs/1105.5443) <a id="cite-note-13" href="#cite-ref-13">[13]</a>

## 2000 ...

- [Carla P. Gomes](http://www.cs.cornell.edu/gomes/), [Cèsar Fernández](http://dblp.uni-trier.de/pers/hd/f/Fern=aacute=ndez:C=egrave=sar), [Bart Selman](Bart_Selman "Bart Selman"), [Christian Bessière](http://dblp.uni-trier.de/pers/hd/b/Bessiere:Christian) (**2004**). *Statistical Regimes Across Constrainedness Regions*. [CP 2004](http://dblp.uni-trier.de/db/conf/cp/cp2004.html#GomesFSB04), [pdf](http://www.cs.cornell.edu/selman/papers/pdf/04.cp.stat-regimes.pdf)
- [Lukas Kroc](http://www.cs.cornell.edu/~kroc/), [Ashish Sabharwal](Ashish_Sabharwal "Ashish Sabharwal"), [Bart Selman](Bart_Selman "Bart Selman") (**2008, 2011**). *[Leveraging Belief Propagation, Backtrack Search, and Statistics for Model Counting](http://link.springer.com/article/10.1007%2Fs10479-009-0680-7)*. [CPAIOR 2008](http://dblp.uni-trier.de/db/conf/cpaior/cpaior2008.html#KrocSS08), [Annals of Operations Research, Vol. 184](http://dblp.uni-trier.de/db/journals/anor/anor184.html#KrocSS11)

## 2010 ...

- [Pablo San Segundo](Pablo_San_Segundo "Pablo San Segundo") (**2011**). *[New decision rules for exact search in N-Queens](http://www.springerlink.com/content/t18m6980g334nu84/)*. [Journal of Global Optimization, Vol. 51, No. 3](http://www.informatik.uni-trier.de/~ley/db/journals/jgo/jgo51.html#Segundo11)
- [Martin Gardner](Martin_Gardner "Martin Gardner") (**2014**). *[Knots and Borromean Rings, Rep-Tiles, and Eight Queens: Martin Gardner’s Unexpected Hanging](http://www.cambridge.org/gb/academic/subjects/mathematics/recreational-mathematics/knots-and-borromean-rings-rep-tiles-and-eight-queens-martin-gardners-unexpected-hanging)*. [The Mathematical Association of America](https://en.wikipedia.org/wiki/Mathematical_Association_of_America) / [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)

## Chapter 16: *The Eight Queens and Other Chessboard Diversions*. Forum Posts

- [N-Queens number for large boards](https://groups.google.com/g/rec.games.chess.computer/c/ty2-qKDlJUI/m/Wt292BRnL14J) by [Truman Collins](Truman_Collins "Truman Collins"), [rgcm](Computer_Chess_Forums "Computer Chess Forums"), January 30, 1997
- [N Queens Puzzle Algorithm](http://www.talkchess.com/forum/viewtopic.php?t=66016) by Aaron Alfer, [CCC](CCC "CCC"), December 15, 2017

## External Links

- [Backtracking from Wikipedia](https://en.wikipedia.org/wiki/Backtracking)
- [Backjumping from Wikipedia](https://en.wikipedia.org/wiki/Backjumping)
- [Backtrack Search using a Computer](http://www.cecm.sfu.ca/organics/papers/lam/paper/html/node4.html) from [The Search for a Finite Projective Plane of Order 10](http://www.cecm.sfu.ca/organics/papers/lam/paper/html/paper.html) by [Clement W. H. Lam](http://www.cecm.sfu.ca/organics/authors/lam/)
- [Constraint satisfaction problem from Wikipedia](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)
- [Boolean satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem)
- [NP-complete from Wikipedia](https://en.wikipedia.org/wiki/NP-complete)
- [Karp's 21 NP-complete problems from Wikipedia](https://en.wikipedia.org/wiki/Karp%27s_21_NP-complete_problems)
- [List of NP-complete problems from Wikipedia](https://en.wikipedia.org/wiki/List_of_NP-complete_problems)
- [Four color theorem from Wikipedia](https://en.wikipedia.org/wiki/Four_color_theorem)
- [Knight's tour from Wikipedia](https://en.wikipedia.org/wiki/Knight%27s_tour) and [a backtracking implementation in C++](http://www.compgeom.com/%7Epiyush/teach/3330/homeworks/knightour.cpp)
- [Eight queens puzzle from Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
- [N-queens problem](http://rosettacode.org/wiki/N-queens_problem) - [Rosetta Code](https://en.wikipedia.org/wiki/Rosetta_Code)
- [Knuth's Algorithm X from Wikipedia](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)
- [Dancing Links from Wikipedi](https://en.wikipedia.org/wiki/Dancing_Links)
- [Dancing Links : Solving Sodoku](http://cgi.cse.unsw.edu.au/%7Exche635/dlx_sodoku/) by [Xi Chen](http://youtu.be/FL2VahPZlk4)
- [Sudoku algorithms from Wikipedia](https://en.wikipedia.org/wiki/Sudoku_algorithms)
- [Exact Covering and DLX](http://www.dylanscott.org/blog/2010/03/exact-covering-and-dlx/) by [Dylan Scott](http://www.dylanscott.org/), March 6, 2010
- [Sudoku as an Exact Cover Problem](http://www.dylanscott.org/blog/2010/03/sudoku-as-an-exact-cover-problem/) by [Dylan Scott](http://www.dylanscott.org/), March 17, 2010
- [Trial and error from Wikipedia](https://en.wikipedia.org/wiki/Trial_and_error)
- [Backtracking](http://www.hostpublications.com/books/backtracking.html) poems by [Dave Oliphant](http://www.hostpublications.com/books/bookinfo/backtracking-author.html)
- [Flora Purim](Category:Flora_Purim "Category:Flora Purim") - Niura is Coming Back, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Visual Example of the Eight Queens backtrack Algorithm, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Eight queens puzzle from Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [James R. Bitner](Mathematician#JRBitner "Mathematician"), [Edward M. Reingold](Mathematician#EMReingold "Mathematician") (**1975**). *[Backtrack Programming Techniques](http://portal.acm.org/citation.cfm?id=361224&dl=ACM&coll=DL&CFID=18128359&CFTOKEN=31610180)*. [Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM), Vol. 18, No. 11
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Robert J. Walker](Mathematician#RJWalker "Mathematician") (**1960**). *An Enumerative Technique for a Class of Combinatorial Problems*. [Proceedings of Symposia in Applied Mathematics, Vol. X, Combinatorial Analysis](http://www.bibliopolis.com/main/books/caliban_0036592.html), [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") and [Marshall Hall, Jr.](Mathematician#MHallJr "Mathematician"), eds., [American Mathematical Society](https://en.wikipedia.org/wiki/American_Mathematical_Society), [Providence, Rhode Island](https://en.wikipedia.org/wiki/Providence,_RI), pp. 91-94
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Onur Demirörs](http://www.ii.metu.edu.tr/people/onur-demir%C3%B6rs), [N. Rafraf](http://www.ii.metu.edu.tr/biblio/author/749), [M.M. Tanik](http://www.ii.metu.edu.tr/biblio/author/750) (**1992**). *[Obtaining n-queens solutions from magic squares and constructing magic squares from n-queens solutions](http://www.ii.metu.edu.tr/publications/1992/obtaining-n-queens-solutions-magic-squares-and-constructing-magic-squares-n-queens)*. Journal of Recreational Mathematics, Vol. 24
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Magic square from Wikipedia](https://en.wikipedia.org/wiki/Magic_square)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [John Gaschnig](John_Gaschnig "John Gaschnig") (**1977**). *[A General Backtrack Algorithm That Eliminates Most Redundant Tests](https://dl.acm.org/citation.cfm?id=1624534)*. [IJCAI 1977](Conferences#IJCAI1977 "Conferences")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Queens ~ /etc/marcelk](http://marcelk.net/queens/)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [8 Queens (NO \*SPOILER\*)](http://groups.google.com/group/rec.puzzles/msg/4820204ffbaad284?hl=en&dmode=source) by Tony Lezard, [rec.puzzles](http://groups.google.com/group/rec.puzzles/topics?hl=en), November 18, 1991
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [The 70\*70 Square Puzzle](http://home.datacomm.ch/t_wolf/tw/misc/squares.html) by [Thomas Wolf](http://home.datacomm.ch/t_wolf/)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Re: Perft(15) estimate after averaging 800 MC samples](http://www.talkchess.com/forum/viewtopic.php?t=47740&start=36) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), November 21, 2013 » [Perft](Perft "Perft")
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Branch and bound - Wikipedia](https://en.wikipedia.org/wiki/Branch_and_bound)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [WalkSAT from WIkipedia](https://en.wikipedia.org/wiki/WalkSAT)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Hamiltonian path problem from Wikipedia](https://en.wikipedia.org/wiki/Hamiltonian_path_problem)

**[Up one Level](Algorithms "Algorithms")**

