---
title: BCH Hashing
---
**[Home](Home "Home") * [Search](Search "Search") * [Transposition Table](Transposition_Table "Transposition Table") * BCH Hashing**

[](http://en.wikipedia.org/wiki/Metamorphosis_of_Narcissus) [Salvador Dalí](Category:Salvador_Dal%C3%AD "Category:Salvador Dalí") - [Metamorphosis of Narcissus](https://en.wikipedia.org/wiki/Metamorphosis_of_Narcissus), 1937 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**BCH Hashing**,

a fast [incremental](Incremental_Updates "Incremental Updates") [Hash function](https://en.wikipedia.org/wiki/Hash_function) to transform a board [position](Chess_Position "Chess Position") into a number of a set length, quite similar to [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing"). It was proposed by [Tony Warnock](Tony_Warnock "Tony Warnock") and [Burton Wendroff](Burton_Wendroff "Burton Wendroff") in 1988 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, relying on [BCH codes](https://en.wikipedia.org/wiki/BCH_code) invented by [Alexis Hocquenghem](Mathematician#Hocquenghem "Mathematician") in 1959 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and independently by [Raj Chandra Bose](Mathematician#RCBose "Mathematician") and [Dwijendra Kumar Ray-Chaudhuri](Mathematician#RayChaudhuri "Mathematician") in 1960 <a id="cite-note-4" href="#cite-ref-4">[4]</a>. They used a BCH signature length of 81 (or more) bits to protect 16 bits from the full position string of 749 (64\*12 - 2\*2\*8 + 4 + 8 + 1) bits, which is sufficient to avoid [collisions](Transposition_Table#KeyCollisions "Transposition Table") within an 8 ply search. They stored 63 bits of the BCH signature as "lock" inside the table, and used 18 (or more) lower bits as index. [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") elaborates on BCH codes inside his thesis as well <a id="cite-note-5" href="#cite-ref-5">[5]</a>, and refers [Elwyn Berlekamp's](Elwyn_Berlekamp "Elwyn Berlekamp") *Algebraic Coding Theory* <a id="cite-note-6" href="#cite-ref-6">[6]</a> .

## Contents

- [1 Quotes](#quotes)
  - [1.1 Tony Warnock](#tony-warnock)
  - [1.2 Kathe and Dan Spracklen](#kathe-and-dan-spracklen)
- [2 See also](#see-also)
- [3 Publications](#publications)
- [4 Postings](#postings)
- [5 External Links](#external-links)
- [6 References](#references)

## Quotes

## [Tony Warnock](Tony_Warnock "Tony Warnock")

on *Search Tables in Computer Chess* <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>:

```C++
The following paper describes a method of generating the numbers for a hash table. By using [error correcting codes](https://en.wikipedia.org/wiki/Error_detection_and_correction), we ensure that positions that are close on the board are not close in the hash space. Some experiments showed that we got an improvement in collision rate compared to using a [random set of numbers](Pseudorandom_Number_Generator "Pseudorandom Number Generator").

```

```C++
[MacWilliams](Mathematician#JMacWilliam "Mathematician") and [Sloane's](Mathematician#NSloane "Mathematician") book on error correcting codes <a id="cite-note-9" href="#cite-ref-9">[9]</a> has the glory details about the theory and programming. 

```

## [Kathe](Kathe_Spracklen "Kathe Spracklen") and [Dan Spracklen](Dan_Spracklen "Dan Spracklen")

excerpt from their *Oral History* <a id="cite-note-10" href="#cite-ref-10">[10]</a> :

```C++
Well, first explain what a hash table is... You want to spread your positions out over a large data area so you need random numbers that will distribute a Chess position over, you know, a lot of different, you know, memory maps or memory locations.

```

```C++
So BCH random numbers were something that some people had developed at the [University of New Mexico](https://en.wikipedia.org/wiki/University_of_New_Mexico). Those people had [a Chess program](Lachex "Lachex"). They wrote an article on it and ... I think it's three different people that developed it. Anyway, it's a coding scheme that gives the maximal distance between... Bit adjacent numbers so that you spread your positions over - more uniformly over the hash table area. They don't tend to bunch up as much that way. 

```

```C++
So, anyway, they wrote an article on how to do that and I had - in fact, I even got the book that they recommended and read it and figured it out how to do it because they didn't really tell you how to do it. They just said that they were using them and they were... So I tried it and, sure enough, they worked a lot better than the old method of getting random numbers. 

```

## See also

- [Hash Table](Hash_Table "Hash Table")
- [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")

## Publications

- [Alexis Hocquenghem](Mathematician#Hocquenghem "Mathematician") (**1959**). *Codes correcteurs d'erreurs*. Chiffres, Paris 2, pp. 147–156 (French)
- [Raj Chandra Bose](Mathematician#RCBose "Mathematician"), [Dwijendra Kumar Ray-Chaudhuri](Mathematician#RayChaudhuri "Mathematician") (**1960**). *On A Class of Error Correcting Binary Group Codes*. [Information and Control](https://en.wikipedia.org/wiki/Information_and_Computation) Vol. 3, No. 1, pp. 68–79, ISSN 0890-5401, [pdf](http://kom.aau.dk/~heb/kurser/NOTER/KOFA03.PDF)
- [Elwyn Berlekamp](Elwyn_Berlekamp "Elwyn Berlekamp") (**1968**). *Algebraic Coding Theory*. New York: McGraw-Hill. Revised ed., Aegean Park Press, (**1984**), ISBN 0894120638. [amazon](http://www.amazon.com/Algebraic-Coding-Theory-Revised-M-6/dp/0894120638) <a id="cite-note-11" href="#cite-ref-11">[11]</a>
- [Jessie MacWilliams](Mathematician#JMacWilliam "Mathematician"), [Neil Sloane](Mathematician#NSloane "Mathematician") (**1981**). *[The Theory of Error-Correcting Codes](http://www.sciencedirect.com/science/bookseries/09246509/16)*. North-Holland Mathematical Library, [amazon](http://www.amazon.com/Theory-Error-Correcting-North-Holland-Mathematical-Library/dp/0444851933)
- [Tony Warnock](Tony_Warnock "Tony Warnock"), [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1988**). *Search Tables in Computer Chess*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
- [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems*. Ph.D. Thesis
- [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1995**). *Programmes d'Échecs de Championnat: Architecture Logicielle Synthèse de Fonctions d'Évaluations, Parallélisme de Recherche*. Ph.D. Thesis. [Université Paris 8](University_of_Paris#8 "University of Paris"), Saint-Denis, [zipped ps](http://www.recherche.enac.fr/%7Eweill/publications/phdJCW.ps.gz) (French) <a id="cite-note-12" href="#cite-ref-12">[12]</a>
- [J. P. Grossman](index.php?title=J._P._Grossman&action=edit&redlink=1 "J. P. Grossman (page does not exist)"), [Levente Jakab](http://www.linkedin.com/in/ljakab) (**2004**). *[Using the BCH construction to generate robust linear hash functions](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1405309)*. [Information Theory Workshop, 2004. IEEE](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=9641)

## Postings

- [Re: Hash tables----Clash!!!-What happens next?](https://groups.google.com/group/rec.games.chess/msg/2a4183cb654443dc?hl=en) by [Tony Warnock](Tony_Warnock "Tony Warnock"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 17, 1994
- [Re: Hash functions for use with a transition table](https://groups.google.com/d/msg/rec.games.chess.computer/0sIKY_dfLUs/aMlLOXkDJJsJ) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 7, 1997
- [How gracefully do BCH codes degrade](http://www.science-bbs.com/121-math/3da76fc0fd4785b9.htm#.UdMt06wXl8E) by Eb Oesch, [Science Forum, math](http://www.science-bbs.com/viewforum/121-math/1796.htm), May 20, 2008
- [Re: Overlapped Zobrist keys array](http://www.talkchess.com/forum/viewtopic.php?t=30008&start=11) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), October 06, 2009

## External Links

- [BCH codes from Wikipedia](https://en.wikipedia.org/wiki/BCH_code)
- [Berlekamp–Massey algorithm from Wikipedia](https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm)
- [Berlekamp–Welch algorithm from Wikipedia](https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Welch_algorithm)
- [Coding theory from Wikipedia](https://en.wikipedia.org/wiki/Coding_theory)
- [Coding Theory](http://www.youtube.com/course?list=EC5002EB7306694E7D) by [Andrew Thangaraj](http://www.ee.iitm.ac.in/~andrew/), Department of Electronics & Communication Engineering, [Indian Institute of Technology Madras](https://en.wikipedia.org/wiki/Indian_Institute_of_Technology_Madras), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos
- [Cyclic code from Wikipedia](https://en.wikipedia.org/wiki/Cyclic_code)
- [Error detection and correction from Wikipedia](https://en.wikipedia.org/wiki/Error_detection_and_correction)
- [Finite field from Wikipedia](https://en.wikipedia.org/wiki/Finite_field)

[GF(2) from Wikipedia](https://en.wikipedia.org/wiki/GF%282%29)

- [Forward error correction from Wikipedia](https://en.wikipedia.org/wiki/Forward_error_correction)
- [MinT - Cyclic Codes (BCH-Bound)](http://mint.sbg.ac.at/desc_CCyclic-BCHBound.html)
- [Root of unity modulo n from Wikipedia](https://en.wikipedia.org/wiki/Root_of_unity_modulo_n)
- [Hux Flux](Category:Hux_Flux "Category:Hux Flux") - Calculus, [Cryptic Crunch](https://en.wikipedia.org/wiki/Hux_Flux#Albums), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Metamorphosis of Narcissus from Wikipedia](https://en.wikipedia.org/wiki/Metamorphosis_of_Narcissus)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Tony Warnock](Tony_Warnock "Tony Warnock"), [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1988**). *Search Tables in Computer Chess*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Alexis Hocquenghem](Mathematician#Hocquenghem "Mathematician") (**1959**). *Codes correcteurs d'erreurs*. Chiffres, Paris 2, pp. 147–156 (French)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Raj Chandra Bose](Mathematician#RCBose "Mathematician"), [Dwijendra Kumar Ray-Chaudhuri](Mathematician#RayChaudhuri "Mathematician") (**1960**). *On A Class of Error Correcting Binary Group Codes*. [Information and Control](https://en.wikipedia.org/wiki/Information_and_Computation) Vol. 3, No. 1, pp. 68–79, ISSN 0890-5401, [pdf](http://kom.aau.dk/~heb/kurser/NOTER/KOFA03.PDF)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems*. Ph.D. Thesis, [BCH Codes](https://en.wikipedia.org/wiki/BCH_Code) at page 22 and page 145 (Appendix A)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Elwyn Berlekamp](Elwyn_Berlekamp "Elwyn Berlekamp") (**1968**). *Algebraic Coding Theory*. New York: McGraw-Hill. Revised ed., Aegean Park Press, (**1984**), ISBN 0894120638. [amazon](http://www.amazon.com/Algebraic-Coding-Theory-Revised-M-6/dp/0894120638)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Hash tables----Clash!!!-What happens next?](https://groups.google.com/group/rec.games.chess/msg/2a4183cb654443dc?hl=en) by [Tony Warnock](Tony_Warnock "Tony Warnock"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 17, 1994
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Tony Warnock](Tony_Warnock "Tony Warnock"), [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1988**). *Search Tables in Computer Chess*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Jessie MacWilliams](Mathematician#JMacWilliam "Mathematician"), [Neil Sloane](Mathematician#NSloane "Mathematician") (**1981**). *[The Theory of Error-Correcting Codes](http://www.sciencedirect.com/science/bookseries/09246509/16)*. North-Holland Mathematical Library, [amazon](http://www.amazon.com/Theory-Error-Correcting-North-Holland-Mathematical-Library/dp/0444851933)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Gardner Hendrie](http://www.computerhistory.org/trustee/gardner-hendrie) (**2005**). *Oral History of Kathe and Dan Spracklen*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/oral-history/spacklen.oral_history.2005.102630821/spracklen.oral_history_transcript.2005.102630821.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [CSE 545, Error Correcting Codes: Combinatorics, Algorithms and Applications](http://www.cse.buffalo.edu/~atri/courses/coding-theory/) by [Atri Rudra](http://www.cse.buffalo.edu/~atri/)
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Re: Overlapped Zobrist keys array](http://www.talkchess.com/forum/viewtopic.php?t=30008&start=11) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), October 06, 2009

**[Up one Level](Transposition_Table "Transposition Table")**

