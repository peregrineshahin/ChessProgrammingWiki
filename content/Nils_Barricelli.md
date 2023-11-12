---
title: Nils Barricelli
---
**[Home](Home "Home") \* [People](People "People") \* Nils Barricelli**



 [](http://makezine.com/08/dyson/) Nils Aall Barricelli <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Nils Aall Barricelli**, (January 24, 1912 – January 27, 1993)  

was a Norwegian-Italian [psychologist](Category:Psychologist "Category:Psychologist") and mathematician. He did early computer-assisted experiments in [symbiogenesis](https://en.wikipedia.org/wiki/Symbiogenesis) and [evolutionary algorithms](Genetic_Programming#EvolutionaryAlgorithms "Genetic Programming"), considered pioneering in [artificial life](https://en.wikipedia.org/wiki/Artificial_life) research. In the 50s he thought about to write a chess program to test evolutionary theories, and implemented a program in collaboration with [Alex Bell](Alex_Bell "Alex Bell"), who wrote a fast legal move generator, in the early 60s. In 1974, while he researched at the [University of Oslo](https://en.wikipedia.org/wiki/University_of_Oslo), he participated at the [First World Computer Chess Championship](WCCC_1974 "WCCC 1974") in Stockholm with his own chess program [Freedom](Freedom "Freedom") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



## Barricellian Symbioorganisms


[Alex Bell](Alex_Bell "Alex Bell") explains Barricelli's Symbioorganisms <a id="cite-note-4" href="#cite-ref-4">[4]</a>:
Barricelli devised the following extremely simple rules for sexual (symbiogenetic) reproduction. There are two integer [arrays](Array "Array"), this generation and next generation. The array this generation initially contains a random pattern of positive and negative integers. The following algorithm (expressed in Algol) is now executed: 




```C++

integer array this generation, next generation [1 :512];
begin
 loop: for i : = 1 step 1 until 512 do 
       begin 
       n := j := this generation[i];
reproduce: if j = 0 then goto next i;
       k := modulo 512 of (i) plus: (j);
       if next generation[k] > 0 then 
       goto mutation else 
       next generation[k] := n;
       j := this generation[k];
       goto reproduce;
  mutation:
  next i: end;

  copy next generation into this generation;

  print this generation;

  goto loop;
end;

```

## See also


* [Freedom](Freedom "Freedom")
* [Genetic Programming](Genetic_Programming "Genetic Programming")
* [WCCC 1974](WCCC_1974 "WCCC 1974")


## Selected Publications


* Nils Barricelli (**1954**). *Esempi numerici di processi di evoluzione*, Methodos, pp. 45-68, 1954
* Nils Barricelli (**1957**). *Symbiogenetic evolution processes realized by artificial methods*. Methodos: 143–182.
* Nils Barricelli (**1961**). *[Numerical testing of evolution theories. Part I Theoretical introduction and basic tests](http://www.springerlink.com/content/y502315688024453/)*. Department of Biology, Division of Molecular Biology, [Vanderbilt University](https://en.wikipedia.org/wiki/Vanderbilt_University), Nashville, Tennessee, [Acta Biotheoretica](http://www.springer.com/philosophy/philosophy+of+sciences/journal/10441), Springer Netherlands, ISSN: 0001-5342
* Nils Barricelli (**1963**). *[Numerical testing of evolution theories. Part II preliminary tests of performance. symbiogenesis and terrestrial life](http://www.springerlink.com/content/h85817217u25w6q7/)*. Department of Biology, Division of Molecular Biology, [Vanderbilt University](https://en.wikipedia.org/wiki/Vanderbilt_University), Nashville, Tennessee, [Acta Biotheoretica](http://www.springer.com/philosophy/philosophy+of+sciences/journal/10441), Springer Netherlands, ISSN: 0001-5342
* [George Dyson](https://en.wikipedia.org/wiki/George_Dyson_%28science_historian%29) (**1997, 2012**). *Darwin Among The Machines: The Evolution Of Global Intelligence*. [Basic Books](https://en.wikipedia.org/wiki/Basic_Books), Second Edition 2012, [from amazon](http://www.amazon.com/Darwin-Among-The-Machines-Intelligence/dp/0465031625) <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [David B. Fogel](David_B._Fogel "David B. Fogel") (**2006**). *[Nils Barricelli - artificial life, coevolution, self-adaptation](http://ieeexplore.ieee.org/Xplore/login.jsp?url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F10207%2F33585%2F01597062.pdf%3Farnumber%3D1597062&authDecision=-203)* . [IEEE Computational Intelligence Magazine](IEEE#CIM "IEEE"), Vol. 1, No. 1
* [Alexander R. Galloway](https://en.wikipedia.org/wiki/Alexander_R._Galloway) (**2008**). *Creative Evolution*. [Cabinet](https://en.wikipedia.org/wiki/Cabinet_%28magazine%29), No. 42 Forgetting, [pdf](http://cultureandcommunication.org/galloway/pdf/Galloway-Creative_Evolution-Cabinet_Magazine.pdf)
* [Alexander R. Galloway](https://en.wikipedia.org/wiki/Alexander_R._Galloway) (**2012**). *[The Computational Image of Organization: Nils Aall Barricelli](http://www.mitpressjournals.org/doi/abs/10.1162/GREY_a_00059#.VNn-8i6H-49)*. [Grey Room](https://en.wikipedia.org/wiki/Grey_Room), No. 46 <a id="cite-note-6" href="#cite-ref-6">[6]</a>


## External Links


* [Nils Aall Barricelli from Wikipedia](https://en.wikipedia.org/wiki/Nils_Aall_Barricelli)
* [Nils Barricelli's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/person.php?id=493)
* [Luz e Sangue - Nils Aall Barricelli (1912–1993) with Image](http://luzesangue.tumblr.com/)
* [Darwin Among The Machines; or, the Origins of [Artificial](http://www.edge.org/documents/archive/edge21.html) Life]. a presentation by [George Dyson](https://en.wikipedia.org/wiki/George_Dyson_%28science_historian%29), [Edge 21](https://en.wikipedia.org/wiki/Edge_Foundation,_Inc.), July 8, 1997
* [A Universe of Self-Replicating Code](http://edge.org/conversation/a-universe-of-self-replicating-code) by [George Dyson](https://en.wikipedia.org/wiki/George_Dyson_%28science_historian%29), [Edge.org](https://en.wikipedia.org/wiki/Edge_Foundation,_Inc.), March 26, 2012
* [Nils Barricelli’s 5 Kilobyte Symbiogenesis simulations and ‘molecule shaped numbers’ – A precursor to DNA Computing](http://www.dataisnature.com/?p=1448), [Dataisnature](http://www.dataisnature.com/), June 06, 2012
* [Meet the Father of Digital Life](http://nautil.us/issue/14/mutation/meet-the-father-of-digital-life) by [Robert Hackett](http://fortune.com/author/robert-hackett/), [Nautilus](http://nautil.us/), June 12, 2014
* [George Dyson](https://en.wikipedia.org/wiki/George_Dyson_%28science_historian%29) - The Birth of the Computer, <a id="cite-note-7" href="#cite-ref-7">[7]</a> [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [George Dyson](https://en.wikipedia.org/wiki/George_Dyson_%28science_historian%29) *Early experiments in digital evolution*. From the column [Retrospect](http://makezine.com/dyson/) by [George Dyson](https://en.wikipedia.org/wiki/George_Dyson_%28science_historian%29)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Nils Barricelli's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/person.php?id=493)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Alex Bell](Alex_Bell "Alex Bell") (**1978**). *[MASTER at IFIPS](http://www.chilton-computing.org.uk/acl/applications/cocoa/p008.htm)*. Excerpt from: The Machine Plays Chess? from [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory"), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Barricellian symbioorganisms](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p004.htm#index78) in [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227, hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Darwin among the Machines - Wikipedia](https://en.wikipedia.org/wiki/Darwin_among_the_Machines)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Barricelli: Built with Processing](http://cultureandcommunication.org/galloway/Barricelli/) by [Alexander R. Galloway](https://en.wikipedia.org/wiki/Alexander_R._Galloway)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Leviathan](https://en.wikipedia.org/wiki/Leviathan_%28book%29) by [Thomas Hobbes](https://en.wikipedia.org/wiki/Thomas_Hobbes)

**[Up one level](People "People")**







 
