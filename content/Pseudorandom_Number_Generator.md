---
title: Pseudorandom Number Generator
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Algorithms](Algorithms "Algorithms") \* Pseudorandom Number Generator**



[ Dice players [[1]](#cite_note-1)
**Pseudorandom Number Generator** (PRNG),  

an algorithmic [gambling](https://en.wikipedia.org/wiki/Gambling) device for generating [pseudorandom](https://en.wikipedia.org/wiki/Pseudorandomness) [numbers](https://en.wikipedia.org/wiki/Pseudorandom_number_generator), a [deterministic](https://en.wikipedia.org/wiki/Deterministic_system) sequence of numbers which appear to be [random](https://en.wikipedia.org/wiki/Randomness) with the property of reproducibility. They are useful in [simulation](https://en.wikipedia.org/wiki/Simulation), [sampling](https://en.wikipedia.org/wiki/Sampling), [computer programming](https://en.wikipedia.org/wiki/Computer_programming), [decision making](https://en.wikipedia.org/wiki/Decision-making), [cryptography](https://en.wikipedia.org/wiki/Cryptography), [aesthetics](https://en.wikipedia.org/wiki/Aesthetics) and [recreation](https://en.wikipedia.org/wiki/Recreation) [[2]](#cite_note-2) - in computer chess, beside randomization of game playing, primarily used to generate keys for [Zobrist hashing](Zobrist_Hashing "Zobrist Hashing"). 


Games of chance, such as [Backgammon](Backgammon "Backgammon") and [EinStein würfelt nicht!](EinStein_w%C3%BCrfelt_nicht! "EinStein würfelt nicht!") require PRNGs for rolling a [dice](https://en.wikipedia.org/wiki/Dice). Chess and game playing programs use PRNGs to randomly choose one of several possible moves of a position from an [opening book](Opening_Book "Opening Book"), or use random fluctuations in [learning](Learning "Learning") and [automated tuning](Automated_Tuning "Automated Tuning") tasks. Game playing programs performing a [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), use random playouts in their simulation phase. [Don Beal](Don_Beal "Don Beal") and [Martin C. Smith](Martin_C._Smith "Martin C. Smith") demonstrated that deeper [search with random leaf values](Search_with_Random_Leaf_Values "Search with Random Leaf Values") in chess yields to better play, with some interesting insights in [minimax search](Minimax "Minimax") and implications for designing and testing [evaluation](Evaluation "Evaluation") terms [[3]](#cite_note-3). 



### Contents


* [1 Methods](#Methods)
	+ [1.1 LCG](#LCG)
	+ [1.2 RKISS](#RKISS)
	+ [1.3 RANROT B3](#RANROT_B3)
	+ [1.4 MT](#MT)
	+ [1.5 ChaCha](#ChaCha)
* [2 Applications](#Applications)
* [3 See also](#See_also)
* [4 Selected Publications](#Selected_Publications)
	+ [4.1 1950 ...](#1950_...)
	+ [4.2 1960 ...](#1960_...)
	+ [4.3 1970 ...](#1970_...)
	+ [4.4 1980 ...](#1980_...)
	+ [4.5 1990 ...](#1990_...)
	+ [4.6 2000 ...](#2000_...)
	+ [4.7 2010 ...](#2010_...)
* [5 Forum Posts](#Forum_Posts)
	+ [5.1 1982 ...](#1982_...)
	+ [5.2 1990 ...](#1990_..._2)
	+ [5.3 1995 ...](#1995_...)
	+ [5.4 2000 ...](#2000_..._2)
	+ [5.5 2005 ...](#2005_...)
	+ [5.6 2010 ...](#2010_..._2)
	+ [5.7 2015 ...](#2015_...)
	+ [5.8 2020 ...](#2020_...)
* [6 External Links](#External_Links)
	+ [6.1 Randomness](#Randomness)
	+ [6.2 Methods](#Methods_2)
	+ [6.3 Language Support](#Language_Support)
		- [6.3.1 Basic](#Basic)
		- [6.3.2 C](#C)
		- [6.3.3 C++](#C.2B.2B)
		- [6.3.4 C#](#C.23)
		- [6.3.5 D](#D)
		- [6.3.6 Fortran](#Fortran)
		- [6.3.7 Go](#Go)
		- [6.3.8 Java](#Java)
		- [6.3.9 Lisp](#Lisp)
		- [6.3.10 Pascal](#Pascal)
		- [6.3.11 Python](#Python)
	+ [6.4 Tests](#Tests)
	+ [6.5 Misc](#Misc)
* [7 References](#References)






PRNGs maintain a state variable, a bitwise superset of the random number, initialized by a [random seed](https://en.wikipedia.org/wiki/Random_seed) - a constant for the same sequence each time, i.e. for Zobrist keys, otherwise, something like [system time](https://en.wikipedia.org/wiki/System_time) to produce varying pseudo randoms. Each call of the PRNG routine performs certain operations or [bit-twiddling](Bit-Twiddling "Bit-Twiddling") on that state, leaving the next pseudo random number. For various applications more or less important features are [randomness](https://en.wikipedia.org/wiki/Randomness), resolution, ([uniform](https://en.wikipedia.org/wiki/Equidistributed_sequence)) [distribution](https://en.wikipedia.org/wiki/Probability_distribution), and [periodicity](https://en.wikipedia.org/wiki/Periodicity) - topic of various [randomness tests](https://en.wikipedia.org/wiki/Randomness_tests) - and further performance, and [portability](https://en.wikipedia.org/wiki/Software_portability). 


[Zobrist hashing](Zobrist_Hashing "Zobrist Hashing") with about 12\*64 keys has less issues with randomness and period, but with distribution, and requires [linear independence](https://en.wikipedia.org/wiki/Linear_independence) so that a small subset of all keys doesn't xor to zero. Despite selected hard-coded random constants used at compile time, many programs use an own PRNG based on [recurrence relation](https://en.wikipedia.org/wiki/Recurrence_relation) in [GF(2)](https://en.wikipedia.org/wiki/GF%282%29) such as [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_twister) or [Xorshift](https://en.wikipedia.org/wiki/Xorshift). 



### LCG


A common method used in many library functions, such as [C](C "C")/[C++](Cpp "Cpp") rand() is the [linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator) (LCG) based on multiply, add, [modulo](https://en.wikipedia.org/wiki/Modulo_operation) with integers, where some past implementations had serious shortcomings in the randomness, distribution and period of the sequence [[4]](#cite_note-4). Due to such issues in rand() implementations, where lower bits are less random than higher bits, it is recommended not to use [modulo](https://en.wikipedia.org/wiki/Modulo_operation) X to reduce the integer range from RAND\_MAX to X, but division by (RAND\_MAX div X) [[5]](#cite_note-5) - or to use C++11's random number generation facilities to replace rand [[6]](#cite_note-6).



### RKISS


[Stockfish](Stockfish "Stockfish") (since 2.0) uses an implementation by [Heinz van Saanen](index.php?title=Heinz_van_Saanen&action=edit&redlink=1 "Heinz van Saanen (page does not exist)") based on [Bob Jenkins'](Bob_Jenkins "Bob Jenkins") [RKISS](Bob_Jenkins#RKISS "Bob Jenkins"), a member of [George Marsaglia's](Mathematician#GMarsaglia "Mathematician") Xorshift familly. 



### RANROT B3


[Amy](Amy "Amy") by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner") [[7]](#cite_note-7) uses an implementation of Agner Fog's RANROT B3 [[8]](#cite_note-8), also recommended by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") as used in [Shredder](Shredder "Shredder") [[9]](#cite_note-9). 



MT
--


[Arasan](Arasan "Arasan") 20.x switched to C++11 random number support using [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_twister) std::mt19937\_64 [[10]](#cite_note-10) [[11]](#cite_note-11).



### ChaCha


The [Rust](Rust "Rust") engine [Asymptote](Asymptote "Asymptote") uses the [ChaCha](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant) [stream cipher](https://en.wikipedia.org/wiki/Stream_cipher) developed by [Daniel J. Bernstein](Mathematician#DJBernstein "Mathematician"), built on a [pseudorandom function](https://en.wikipedia.org/wiki/Pseudorandom_function_family) based on [add-rotate-xor (ARX)](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant) operations [[12]](#cite_note-12).



## Applications


* [Looking for Magics](Looking_for_Magics#FeedinginRandoms "Looking for Magics")
* [Genetic Programming](Genetic_Programming "Genetic Programming")
* [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [Opening Book](Opening_Book "Opening Book")
* [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
* [Simulated Annealing](Simulated_Annealing "Simulated Annealing")
* [SPSA](SPSA "SPSA")
* [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")


## See also


* [CPW-Engine\_book](CPW-Engine_book "CPW-Engine book")
* [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator")
* [RKISS](Bob_Jenkins#RKISS "Bob Jenkins") by [Bob Jenkins](Bob_Jenkins "Bob Jenkins")
* [Sequential Logic](Sequential_Logic "Sequential Logic")
* [Trial and Error](Trial_and_Error "Trial and Error")


## Selected Publications


### 1950 ...


* [Derrick H. Lehmer](Mathematician#DHLehmer "Mathematician") (**1951**). *[Mathematical methods in large-scale computing units](http://www.ams.org/mathscinet-getitem?mr=0044899)*. [Proceedings of a 2nd Symposium on Large Scale Digital Computing Machinery](https://archive.org/details/proceedings_of_a_second_symposium_on_large-scale_), 1949, [Harvard University Press](https://en.wikipedia.org/wiki/Harvard_University_Press), pp. 141–146
* [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation) (**1955**). *[A Million Random Digits with 100,000 Normal Deviates](https://en.wikipedia.org/wiki/A_Million_Random_Digits_with_100,000_Normal_Deviates)*. [pdf](https://www.rand.org/content/dam/rand/pubs/monograph_reports/MR1418/MR1418.deviates.pdf), [online](https://www.rand.org/pubs/monograph_reports/MR1418/index2.html)


### 1960 ...


* [John von Neumann](John_von_Neumann "John von Neumann") (**1963**). *Various techniques used in connection with random digits*. von Neumann's Collected Works, Vol. 5, [Pergamon Press](https://en.wikipedia.org/wiki/Pergamon_Press), [pdf](https://dornsifecms.usc.edu/assets/sites/520/docs/VonNeumann-ams12p36-38.pdf)
* [M. Donald MacLaren](Mathematician#MDMacLaren "Mathematician"), [George Marsaglia](Mathematician#GMarsaglia "Mathematician") (**1965**). *[Uniform Random Number Generators](http://dl.acm.org/citation.cfm?id=321257)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 12, No. 1
* [Donald Knuth](Donald_Knuth "Donald Knuth") (**1969**). *[The Art of Computer Programming (TAOCP)](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming) - [Volume 2 - Seminumerical Algorithms](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming#Volumes)*. Chapter 3 – Random numbers, 1st edition


### 1970 ...


* [Joachim H. Ahrens](Mathematician#JHAhrens "Mathematician"), [Ulrich Dieter](Mathematician#UDieter "Mathematician"), [Andreas Grube](Mathematician#AGrube "Mathematician") (**1970**). *[Pseudo-random numbers](http://link.springer.com/article/10.1007%2FBF02241740?LI=true)*. [Computing](https://en.wikipedia.org/wiki/Computing_(journal)), Vol. 6, No. 1
* [George Marsaglia](Mathematician#GMarsaglia "Mathematician") (**1972**). *The Structure of Linear Congruential Sequences*. in S. K. Zaremba (ed.) *[Applications of Number Theory to Numerical Analysis](http://www.sciencedirect.com/science/book/9780127759500)*. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press)
* [Ulrich Dieter](Mathematician#UDieter "Mathematician"), [Joachim H. Ahrens](Mathematician#JHAhrens "Mathematician") (**1973**). *[A combinatorial method for the generation of normally distributed random numbers](http://link.springer.com/article/10.1007/BF02252903)*. [Computing](https://en.wikipedia.org/wiki/Computing_(journal)), Vol. 11, No. 2


### 1980 ...


* [Scott Kirkpatrick](Mathematician#SKirkpatrick "Mathematician"), [Erich P. Stoll](http://estoll.ch.marissa.hostorama.ch/) (**1981**). *[A Very Fast Shift-Register Sequence Random Number Generator](https://www.researchgate.net/publication/200104855_A_Very_Fast_Shift-Register_Sequence_Random_Number_Generator)*. [Journal of Computational Physics](https://en.wikipedia.org/wiki/Journal_of_Computational_Physics), Vol. 40, No. 2
* [George Marsaglia](Mathematician#GMarsaglia "Mathematician") (**1985**). *A Current View of Random Number Generators*. Proceedings, Computer Science and Statistics: 16th Symposium on the Interface, [Elsevier](https://en.wikipedia.org/wiki/Elsevier)
* [Pierre L'Ecuyer](Mathematician#PLEcuyer "Mathematician") (**1988**). *[Efficient and Portable combined random number generators](http://dl.acm.org/citation.cfm?id=62969)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 31, No. 6


### 1990 ...


* [Pierre L'Ecuyer](Mathematician#PLEcuyer "Mathematician") (**1990**). *[Random numbers for simulation](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=gDxovowAAAAJ&cstart=280&sortby=pubdate&citation_for_view=gDxovowAAAAJ:2osOgNQ5qMEC)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 33, No. 10
* [William H. Press](Mathematician#WHPress "Mathematician"), [Saul A. Teukolsky](Mathematician#SATeukolsky "Mathematician"), [William T. Vetterling](https://de.wikipedia.org/wiki/William_T._Vetterling), [Brian P. Flannery](https://en.wikipedia.org/wiki/Brian_P._Flannery) (**1992**). *[Numerical Recipes in C: The Art of Scientific Computing, 2nd edition](http://www.nrbook.com/a/bookcpdf.php)*. Chapter 7. Random Numbers
* [F. Warren Burton](index.php?title=F._Warren_Burton&action=edit&redlink=1 "F. Warren Burton (page does not exist)"), [Rex L. Page](http://www.cs.ou.edu/~rlpage/) (**1992**). *Distributed Random Number Generation*. [Journal of Functional Programming](https://en.wikipedia.org/wiki/Journal_of_Functional_Programming), Vol. 2, No. 2, [pdf](http://www.cs.ou.edu/~rlpage/burtonpagerngjfp.pdf)
* [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker"), [Jeffrey I. Schiller](https://jis.qyv.name/) (**1994**). *Randomness Recommendations for Security*. [RFC 1750](https://www.ietf.org/rfc/rfc1750.txt)
* [Donald Knuth](Donald_Knuth "Donald Knuth") (**1997**). *[The Art of Computer Programming (TAOCP)](http://www-cs-faculty.stanford.edu/~knuth/taocp.html) - [Volume 2 - Seminumerical Algorithms](http://www.informit.com/store/art-of-computer-programming-volume-2-seminumerical-9780201896848)*. [Chapter 3 – Random numbers](http://www.informit.com/articles/article.aspx?p=2221790), 3rd edition
* [Andrew Shapira](Andrew_Shapira "Andrew Shapira") (**1997**). *Cycle parity random number generators, and a general random number library*. Ph.D. thesis, [Rensselaer Polytechnic Institute](https://en.wikipedia.org/wiki/Rensselaer_Polytechnic_Institute), advisor [Mukkai S. Krishnamoorthy](Mathematician#Krishnamoorthy "Mathematician").
* [Makoto Matsumoto](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/eindex.html), [Takuji Nishimura](http://dblp.uni-trier.de/pers/hd/n/Nishimura:Takuji) (**1998**). *Mersenne twister: A 623-dimensionally equidistributed uniform pseudo-random number generator*. [ACM Transactions on Modeling and Computer Simulation](ACM#TOMACS "ACM"), Vol. 8, No. 1, [pdf preprint](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/ARTICLES/mt.pdf)
* Anna Górecka, [Maciej Szmit](Maciej_Szmit "Maciej Szmit") (**1998**). *[Programowe generatory liczb pseudolosowych. Znacie - to posłuchajcie](http://maciej.szmit.info/documents/prgr/index.htm).* Software 11/1998 (Polish)


### 2000 ...


* [Karl Entacher](Mathematician#KEntacher "Mathematician") (**2000**). *[A collection of classical pseudorandom number generators with linear structures - advanced version](http://random.mat.sbg.ac.at/results/karl/server/server.html)*.
* [Agner Fog](http://www.agner.org/) (**2001**). *Chaotic Random Number Generators with Random Cycle Lengths*. [pdf](http://www.agner.org/random/theory/chaosran.pdf)
* [Julio César Hernández-Castro](Julio_C%C3%A9sar_Hern%C3%A1ndez-Castro "Julio César Hernández-Castro"), [Arturo Ribagorda](https://scholar.google.es/citations?user=0q4BhD8AAAAJ&hl=en), [Pedro Isasi](https://scholar.google.com/citations?user=BHf4l7wAAAAJ&hl=en), [José M. Sierra](https://dblp.org/pid/56/6864.html) (**2001**). *[Genetic Algorithms Can be Used to Obtain Good Linear Congruential Generators](https://www.tandfonline.com/doi/abs/10.1080/0161-110191889897)*. [Cryptologia](https://en.wikipedia.org/wiki/Cryptologia), Vol. 25, No. 3
* [George Marsaglia](Mathematician#GMarsaglia "Mathematician") (**2002**). *[Random number generators](http://digitalcommons.wayne.edu/jmasm/vol2/iss1/2/)*. [Journal of Modern Applied Statistical Methods](https://en.wikipedia.org/wiki/Journal_of_Modern_Applied_Statistical_Methods), Vol. 2, No. 2.
* [George Marsaglia](Mathematician#GMarsaglia "Mathematician") (**2003**). *[Xorshift RNGs](https://www.jstatsoft.org/article/view/v008i14)*. [Journal of Statistical Software](https://en.wikipedia.org/wiki/Journal_of_Statistical_Software), Vol. 8, No. 14
* [Pierre L'Ecuyer](Mathematician#PLEcuyer "Mathematician") (**2004**). *Random Number Generation*. [pdf](http://www.iro.umontreal.ca/~lecuyer/myftp/papers/handstat.pdf)
* [Julio César Hernández-Castro](Julio_C%C3%A9sar_Hern%C3%A1ndez-Castro "Julio César Hernández-Castro"), [André Seznec](https://en.wikipedia.org/wiki/Andr%C3%A9_Seznec), [Pedro Isasi](https://scholar.google.com/citations?user=BHf4l7wAAAAJ&hl=en) (**2004**). *On the design of state-of-the-art pseudorandom number generators by means of genetic programming*. [CEC 2004](https://dblp.org/db/conf/cec/cec2004.html#HernandezSI04), [pdf](https://core.ac.uk/download/pdf/29399623.pdf)
* [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker"), [Jeffrey I. Schiller](https://jis.qyv.name/) (**2005**). *Randomness Requirements for Security*. [RFC 4086](https://tools.ietf.org/html/rfc4086)
* [William H. Press](Mathematician#WHPress "Mathematician"), [Saul A. Teukolsky](Mathematician#SATeukolsky "Mathematician"), [William T. Vetterling](https://de.wikipedia.org/wiki/William_T._Vetterling), [Brian P. Flannery](https://en.wikipedia.org/wiki/Brian_P._Flannery) (**2007**). *[Numerical Recipes. The Art of Scientific Computing](https://en.wikipedia.org/wiki/Numerical_Recipes), 3rd edition*. (C++ code)
* [Daniel J. Bernstein](Mathematician#DJBernstein "Mathematician") (**2007**). *The Salsa20 family of stream ciphers*. [University of Illinois at Chicago](https://en.wikipedia.org/wiki/University_of_Illinois_at_Chicago), [pdf](https://cr.yp.to/snuffle/salsafamily-20071225.pdf) [[13]](#cite_note-13)
* [Daniel J. Bernstein](Mathematician#DJBernstein "Mathematician") (**2008**). *ChaCha, a variant of Salsa20*. [University of Illinois at Chicago](https://en.wikipedia.org/wiki/University_of_Illinois_at_Chicago), [pdf](http://cr.yp.to/chacha/chacha-20080128.pdf)


### 2010 ...


* [Maciej Szmit](Maciej_Szmit "Maciej Szmit"), [Anna Szmit](https://dblp.uni-trier.de/pers/hd/s/Szmit:Anna) (**2011**). *[DNS Pseudo-Random Number Generators Weakness](https://link.springer.com/chapter/10.1007/978-3-642-21771-5_32)*. [CN 2011](https://dblp.uni-trier.de/db/conf/cn/cn2011.html), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2015**). *[When Completely Random is Just not Random Enough](http://www.aifactory.co.uk/newsletter/2014_02_completely_random.htm)*. [AI Factory](AI_Factory "AI Factory"), February 2015


## Forum Posts


### 1982 ...


* [compact representation of chess positions](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.07_duke.1593_net.chess.txt) by [Tom Truscott](Tom_Truscott "Tom Truscott"), net.chess, January 7, 1982


### 1990 ...


* [Re: Weakest Chess Program needed](https://groups.google.com/d/msg/rec.games.chess/Qe_5lhAWTsc/79h9BQslCWIJ) by Kenneth S A Oksanen, [rgc](Computer_Chess_Forums "Computer Chess Forums"), November 12, 1991
* [Hash tables - Clash!!! What happens next?](https://groups.google.com/d/msg/rec.games.chess/h9Q2wik_kTg/Jq7rYE0vqtoJ) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), March 15, 1994


 [Re: Hash tables - Clash!!! What happens next?](https://groups.google.com/d/msg/rec.games.chess/h9Q2wik_kTg/9zrP0flwuzAJ) by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), March 17, 1994
* [Re: Human VS computer](https://groups.google.com/d/msg/rec.games.chess/xIvJfi92jMc/BQP231Z0V84J) by [Don Beal](Don_Beal "Don Beal"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), July 11, 1994


### 1995 ...


* [Primitive Chess Program](https://groups.google.com/d/msg/rec.games.chess/NXEDz2iTbRc/k6uH2zBMmxMJ) by David Ewart, [rgc](Computer_Chess_Forums "Computer Chess Forums"), June 09, 1995
* [random play](https://groups.google.com/d/msg/rec.games.chess.computer/AI3xadkLEIk/lqWaLrHtl7AJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 25, 1996
* [Randomness in move selection](https://groups.google.com/d/msg/rec.games.chess.computer/ul-HWewM5FQ/sXcqhGL06UQJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 01, 1996
* [Re: Interesting random chess question - What is probability to win?](https://www.stmintz.com/ccc/index.php?id=28699) by [Jari Huikari](index.php?title=Jari_Huikari&action=edit&redlink=1 "Jari Huikari (page does not exist)"), [CCC](CCC "CCC"), October 03, 1998 » [Nero](Nero "Nero")
* [Random chess statistics, part two](https://www.stmintz.com/ccc/index.php?id=29571) by [Jari Huikari](index.php?title=Jari_Huikari&action=edit&redlink=1 "Jari Huikari (page does not exist)"), [CCC](CCC "CCC"), October 14, 1998
* [How to create a set of random integers for hashing?](https://www.stmintz.com/ccc/index.php?id=29817) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), October 18, 1998
* [Random numbers for C: End, at last?](https://groups.google.com/d/msg/sci.math.num-analysis/6dlqhMI2Dvs/t5uVomP0VbUJ) by [George Marsaglia](Mathematician#GMarsaglia "Mathematician"), [sci.math.num-analysis](https://groups.google.com/forum/?hl=en#!forum/sci.math.num-analysis), January 21, 1999


### 2000 ...


* [random book moves/ random generator](https://www.stmintz.com/ccc/index.php?id=88292) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), January 13, 2000


 [Re: random book moves/ random generator](https://www.stmintz.com/ccc/index.php?id=88293) by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), [CCC](CCC "CCC"), January 13, 2000
* [Simple Learning Technique and Random Play](https://www.stmintz.com/ccc/index.php?id=150687) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), January 18, 2001 » [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
* [Why Random Number Needed In HashFunction[piece](https://groups.google.com/d/msg/rec.games.chess.computer/WH0DlnlGH7g/Izx2q-xoHTcJ)[position]] by Cheok Yan Cheng, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 12, 2001
* [Random factor in static evaluation!](https://www.stmintz.com/ccc/index.php?id=175314) by Tiago Ribeiro, [CCC](CCC "CCC"), June 15, 2001
* [Simulating the result of a single game by random numbers](https://www.stmintz.com/ccc/index.php?id=178041) by Christoph Fieberg, [CCC](CCC "CCC"), July 03, 2001
* [Simulating the result of a single game by random numbers - Update!](https://www.stmintz.com/ccc/index.php?id=179091) by Christoph Fieberg, [CCC](CCC "CCC"), July 10, 2001
* [Simulating the result of a single game by random numbers - Update!](https://www.stmintz.com/ccc/index.php?id=178939) by Christoph Fieberg, [CCC](CCC "CCC"), August 02, 2001
* [About random numbers and hashing](https://www.stmintz.com/ccc/index.php?id=200366) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 04, 2001


 [Re: About random numbers and hashing](https://www.stmintz.com/ccc/index.php?id=200622) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), December 05, 2001
* [Random keys and hamming distance](https://www.stmintz.com/ccc/index.php?id=245775) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), August 16, 2002
* [Random play](https://www.stmintz.com/ccc/index.php?id=292517) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), April 08, 2003
* [64-Bit random numbers](https://www.stmintz.com/ccc/index.php?id=324223) by [Martin Schreiber](index.php?title=Martin_Schreiber&action=edit&redlink=1 "Martin Schreiber (page does not exist)"), [CCC](CCC "CCC"), October 28, 2003
* [A question about random numbers](https://www.stmintz.com/ccc/index.php?id=378514) by Antonio Senatore, [CCC](CCC "CCC"), July 22, 2004


### 2005 ...


* [randomness of random number generators? somewhat OT](https://www.stmintz.com/ccc/index.php?id=452889) by David Dahlem, [CCC](CCC "CCC"), October 01, 2005
* [Random number mobility scores](https://groups.google.com/d/msg/rec.games.chess.computer/Ab9uA1-8Hlw/UjT_JXTiHuIJ) by Guest, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 20, 2008
* [Zobrist key random numbers](http://www.talkchess.com/forum/viewtopic.php?t=26152) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 21, 2009
* [64-bit KISS RNGs](http://compgroups.net/comp.lang.fortran/64-bit-kiss-rngs/601519) by [George Marsaglia](Mathematician#GMarsaglia "Mathematician"), [comp.lang.fortran](http://compgroups.net/comp.lang.fortran/), February 28, 2009


### 2010 ...


* [Transposition table random numbers](http://www.talkchess.com/forum/viewtopic.php?t=35415) by Justin Madru, [CCC](CCC "CCC"), July 13, 2010
* [RKISS](http://www.talkchess.com/forum/viewtopic.php?t=37406) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), January 01, 2011
* [RKISS copyright?](http://www.talkchess.com/forum/viewtopic.php?t=38313) by Giorgio Medeot, [CCC](CCC "CCC"), March 07, 2011
* [Stockfish random generator (rkiss.h)](http://www.talkchess.com/forum/viewtopic.php?t=38760) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), April 15, 2011 » [Stockfish](Stockfish "Stockfish"), [Bob Jenkins](Bob_Jenkins "Bob Jenkins")
* [MT or KISS ?](http://www.talkchess.com/forum/viewtopic.php?t=43910) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), June 02, 2012 [[14]](#cite_note-14)
* [rkiss and other dependencies in syzygy](http://www.talkchess.com/forum/viewtopic.php?t=49807) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), October 23, 2013


### 2015 ...


* [A simple PRNG using /dev/urandom](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=56225) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 04, 2015
* [Revised source for the random game generator](http://www.talkchess.com/forum/viewtopic.php?t=56328) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 12, 2015
* [Random playout vs evaluation](http://www.talkchess.com/forum/viewtopic.php?t=56364) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), May 15, 2015
* ["random mover" chess programs](http://www.talkchess.com/forum/viewtopic.php?t=60582) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 24, 2016
* [Adding a random small number to the evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=61315) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), September 03, 2016
* [random evaluation perturbation factor](http://www.talkchess.com/forum/viewtopic.php?t=63803) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), April 24, 2017
* [xiphos 64 bit random number](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70050) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), February 28, 2019 » [Xiphos](Xiphos "Xiphos")


### 2020 ...


* [Rolling dice](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74028) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 27, 2020 » [CECP](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), [EinStein würfelt nicht!](EinStein_w%C3%BCrfelt_nicht! "EinStein würfelt nicht!")


## External Links


* [Pseudorandom number generator from Wikipedia](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
* [Pseudo-random number sampling from Wikipedia](https://en.wikipedia.org/wiki/Pseudo-random_number_sampling)
* [Pseudorandomness from Wikipedia](https://en.wikipedia.org/wiki/Pseudorandomness)
* [Statistical randomness from Wikipedia](https://en.wikipedia.org/wiki/Statistical_randomness)
* [Pseudo-random number sampling from Wikipedia](https://en.wikipedia.org/wiki/Pseudo-random_number_sampling)
* [Random seed from Wikipedia](https://en.wikipedia.org/wiki/Random_seed)
* [Cryptographically secure pseudorandom number generator from Wikipedia](https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator)


### Randomness


* [Randomness from Wikipedia](https://en.wikipedia.org/wiki/Randomness)
* [History of randomness from Wikipedia](https://en.wikipedia.org/wiki/History_of_randomness)
* [Random number generation from Wikipedia](https://en.wikipedia.org/wiki/Random_number_generation)
* [Hardware random number generator](https://en.wikipedia.org/wiki/Hardware_random_number_generator)
* [RANDOM.ORG - True Random Number Service](https://www.random.org/)
* [RANDOM.ORG - Integer Generator](https://www.random.org/integers/)


### Methods


* [Generating Uniform Random Numbers on [0,1](http://clomont.com/generating-uniform-random-numbers-on-01/) ] by [Chris Lomont](http://clomont.com/), March 2017
* [Linear congruential generator from Wikipedia](https://en.wikipedia.org/wiki/Linear_congruential_generator)


 [Lehmer random number generator from Wikipedia](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
 [Park-Miller-Carta Pseudo-Random Number Generators](http://www.firstpr.com.au/dsp/rand31/)
 [RANDU from Wikipedia](https://en.wikipedia.org/wiki/RANDU)
* [Mersenne Twister from Wikipedia](https://en.wikipedia.org/wiki/Mersenne_twister)


 [Mersenne Twister - Home Page](http://www.math.sci.hiroshima-u.ac.jp/%7Em-mat/MT/emt.html)
* [Linear-feedback shift register from Wikipedia](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)
* [Xorshift from Wikipedia](https://en.wikipedia.org/wiki/Xorshift)
* [A small noncryptographic pseudorandom number generator](http://www.burtleburtle.net/bob/rand/smallprng.html) by [Bob Jenkins](Bob_Jenkins "Bob Jenkins")
* [ISAAC, a fast cryptographic random number generator](http://www.burtleburtle.net/bob/rand/isaacafa.html) by [Bob Jenkins](Bob_Jenkins "Bob Jenkins")
* [Pseudo random number generators](http://www.agner.org/random/) by [Agner Fog](http://www.agner.org/)
* [Random Number Generators - the pLab project](http://random.mat.sbg.ac.at/generators/) by [Peter Hellekalek](Mathematician#PJHellekalek "Mathematician")
* [Random Number Generation](http://www.stat.tugraz.at/stadl/random.html) by [Ernst Stadlober](Mathematician#EStadlober "Mathematician")
* [Random Number Generators](http://www.paulm.org/random.html)
* [Salsa20 from Wikipedia](https://en.wikipedia.org/wiki/Salsa20)


### Language Support


### [Basic](Basic "Basic")


* [BASIC Programming/Random Number Generation - Wikibooks](https://en.wikibooks.org/wiki/BASIC_Programming/Random_Number_Generation)
* [Rnd Function (Visual Basic)](https://msdn.microsoft.com/en-us/library/f7s023d2(v=vs.90).aspx)
* [The Beginner's Page: The Random Function](http://www.atarimagazines.com/compute/issue90/The_Beginners_Page.php) » [Atari 8-bit](Atari_8-bit "Atari 8-bit")
* [RND - C64-Wiki](https://www.c64-wiki.com/wiki/RND) » [Commodore 64](Commodore_64 "Commodore 64")


### [C](C "C")


* [rand - MSDN](https://msdn.microsoft.com/en-us/library/398ax69y.aspx)
* [rand(3) - Linux manual page](http://man7.org/linux/man-pages/man3/rand.3.html)
* [GNU Scientific Library – Reference Manual: Random Number Generation](https://www.gnu.org/software/gsl/manual/html_node/Random-Number-Generation.html)


### [C++](Cpp "Cpp")


* [std::rand - cppreference.com](http://en.cppreference.com/w/cpp/numeric/random/rand)
* [Boost Random - Reference - 1.64.0](http://www.boost.org/doc/libs/1_64_0/doc/html/boost_random/reference.html)
* [Pseudo-random number generation - cppreference.com](http://en.cppreference.com/w/cpp/numeric/random)
* [mt19937\_64 - C++ Reference](http://www.cplusplus.com/reference/random/mt19937_64/)
* [Random number generation using](https://www.johndcook.com/blog/cpp_TR1_random/) [C++ Technical Report 1](https://en.wikipedia.org/wiki/C%2B%2B_Technical_Report_1) by [John D. Cook](https://www.johndcook.com/blog/) (2008)


### [C#](C_sharp "C sharp")


* [Random Class (System) - MSDN](https://msdn.microsoft.com/en-us/library/system.random(v=vs.110).aspx)
* [C# in Depth: Random numbers](http://csharpindepth.com/Articles/Chapter12/Random.aspx)
* [Simple Random Number Generation - CodeProject](https://www.codeproject.com/Articles/25172/Simple-Random-Number-Generation) by [John D. Cook](https://www.johndcook.com/blog/) (2008 - 2011)


### [D](D_(Programming_Language) "D (Programming Language)")


* [Module std.random - D Programming Language](https://dlang.org/library/std/random.html)
* [std.random - D Programming Language](https://dlang.org/phobos/std_random.html)


### [Fortran](Fortran "Fortran")


* [The GNU Fortran Compiler: RAND](https://gcc.gnu.org/onlinedocs/gfortran/RAND.html)
* [The GNU Fortran Compiler: RANDOM\_NUMBER](https://gcc.gnu.org/onlinedocs/gfortran/RANDOM_005fNUMBER.html)


### [Go](Go "Go")


* [rand - The Go Programming Language](https://golang.org/pkg/math/rand/)
* [Go by Example: Random Numbers](https://gobyexample.com/random-numbers)


### [Java](Java "Java")


* [Random (Java Platform SE 8 )](http://docs.oracle.com/javase/8/docs/api/java/util/Random.html)
* [ThreadLocalRandom (Java Platform SE 8 )](http://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadLocalRandom.html)


### [Lisp](index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)")


* [Common Lisp - 12.9. Random Numbers](https://www.cs.cmu.edu/Groups/AI/html/cltl/clm/node133.html)
* [Exploring pseudo-random numbers in Lisp](https://jorgetavares.com/2009/09/02/exploring-pseudo-random-numbers-in-lisp/) – [Jorge Tavares Notes](https://jorgetavares.com/)


### [Pascal](Pascal "Pascal")


* [Free Pascal - Random](https://www.freepascal.org/docs-html/rtl/system/random.html)
* [Generating Random Numbers - Free Pascal wiki](http://wiki.freepascal.org/Generating_Random_Numbers)
* [Delphi compatible LCG Random - Free Pascal wiki](http://wiki.freepascal.org/Delphi_compatible_LCG_Random)
* [Marsaglia's pseudo random number generators - Free Pascal wiki](http://wiki.freepascal.org/Marsaglia%27s_pseudo_random_number_generators)


### [Python](Python "Python")


* [9.6. random — Generate pseudo-random numbers — Python 2.7.13 documentation](https://docs.python.org/2/library/random.html)
* [9.6. random — Generate pseudo-random numbers — Python 3.6.1 documentation](https://docs.python.org/3/library/random.html)


### Tests


* [Randomness tests from Wikipedia](https://en.wikipedia.org/wiki/Randomness_tests)
* [Diehard tests from Wikipedia](https://en.wikipedia.org/wiki/Diehard_tests)
* [Spectral test from Wikipedia](https://en.wikipedia.org/wiki/Spectral_test)
* [TestU01 from Wikipedia](https://en.wikipedia.org/wiki/TestU01)


### Misc


* [Van der Graaf Generator](Category:Van_der_Graaf_Generator "Category:Van der Graaf Generator") - Theme One (1972), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) [Dice players](https://commons.wikimedia.org/wiki/File:Pompeii_-_Osteria_della_Via_di_Mercurio_-_Dice_Players.jpg) - [Roman](https://en.wikipedia.org/wiki/Ancient_Rome) [fresco](https://en.wikipedia.org/wiki/Fresco) from the [Osteria della Via di Mercurio](http://www.pompeiiinpictures.com/pompeiiinpictures/r6/6%2010%2001.htm) ([VI 10,1.19, room b](http://www.pompeiiinpictures.com/pompeiiinpictures/r6/6%2010%2001%20p2.htm)) in [Pompeii](https://en.wikipedia.org/wiki/Pompeii), Source: [Filippo Coarelli](https://en.wikipedia.org/wiki/Filippo_Coarelli) (ed.) (**2002**). *[Pompeji](https://www.zvab.com/buch-suchen/titel/pompeji/autor/coarelli/)*. [Hirmer Verlag](https://en.wikipedia.org/wiki/Hirmer_Verlag), [Munich](https://en.wikipedia.org/wiki/Munich), ISBN: 3-7774-9530-1, p. 146, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [History of randomness from Wikipedia](https://en.wikipedia.org/wiki/History_of_randomness)
2. [↑](#cite_ref-2) [Donald Knuth](Donald_Knuth "Donald Knuth") (**1997**). *[The Art of Computer Programming (TAOCP)](http://www-cs-faculty.stanford.edu/~knuth/taocp.html) - [Volume 2 - Seminumerical Algorithms](http://www.informit.com/store/art-of-computer-programming-volume-2-seminumerical-9780201896848)*. [Chapter 3 – Random numbers](http://www.informit.com/articles/article.aspx?p=2221790)
3. [↑](#cite_ref-3) [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1994**). *Random Evaluations in Chess*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
4. [↑](#cite_ref-4) "In the past, some implementations of rand() have had serious shortcomings in the randomness, distribution and period of the sequence produced (in one well-known example, the low-order bit simply alternated between 1 and 0 between calls) rand() is not recommended for serious random-number generation needs, like cryptography. It is recommended to use C++11's random number generation facilities to replace rand()." [rand - cppreference.com](http://en.cppreference.com/w/cpp/numeric/random/rand)
5. [↑](#cite_ref-5) [Re: random book moves/ random generator](https://www.stmintz.com/ccc/index.php?id=88293) by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), [CCC](CCC "CCC"), January 13, 2000
6. [↑](#cite_ref-6) [Pseudo-random number generation - cppreference.com](http://en.cppreference.com/w/cpp/numeric/random)
7. [↑](#cite_ref-7) amy-0.8.7.tar.gz /src/random.c
8. [↑](#cite_ref-8) [Agner Fog](http://www.agner.org/) (**2001**). *Chaotic Random Number Generators with Random Cycle Lengths*. [pdf](http://www.agner.org/random/theory/chaosran.pdf)
9. [↑](#cite_ref-9) [Re: random book moves/ random generator](https://www.stmintz.com/ccc/index.php?id=88309) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), January 13, 2000
10. [↑](#cite_ref-10) [arasan-chess/movegen.h at master · jdart1/arasan-chess · GitHub](https://github.com/jdart1/arasan-chess/blob/master/src/movegen.h)
11. [↑](#cite_ref-11) [mt19937\_64 - C++ Reference](http://www.cplusplus.com/reference/random/mt19937_64/)
12. [↑](#cite_ref-12) [rand::chacha::ChaChaRng - Rust](https://doc.rust-lang.org/1.0.0/rand/chacha/struct.ChaChaRng.html)
13. [↑](#cite_ref-13) [Salsa20 from Wikipedia](https://en.wikipedia.org/wiki/Salsa20)
14. [↑](#cite_ref-14) [Mersenne twister from Wikipedia](https://en.wikipedia.org/wiki/Mersenne_twister)

**[Up one Level](Algorithms "Algorithms")**







 
