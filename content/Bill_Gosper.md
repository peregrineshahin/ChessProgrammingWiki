---
title: Bill Gosper
---
**[Home](Home "Home") * [People](People "People") * Bill Gosper**

\[ Bill Gosper 2006 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Ralph William (Bill) Gosper, Jr.**,

an American mathematician and computer scientist, along with [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") considered the co-founder of the [hacker](https://en.wikipedia.org/wiki/Hacker_culture) community <a id="cite-note-2" href="#cite-ref-2">[2]</a>. In the 60s, affiliated with [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), he worked for [Project MAC](https://en.wikipedia.org/wiki/Project_MAC%7CProject) (Machine-Aided Cognition), where his contributions to [computational mathematics](https://en.wikipedia.org/wiki/Computational_mathematics) and [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling") include [HAKMEM](#hakmem) and [Maclisp](index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)"). He helped Greenblatt with his chess program [Mac Hack VI](Mac_Hack "Mac Hack"), and operated the [PDP-6](PDP-6 "PDP-6") when [Robert Q](Mac_Hack#RobertQ "Mac Hack") played its first tournament game versus Carl Wagner.

In the 70s, Bill Gosper moved to [Stanford University](Stanford_University "Stanford University") for some years, where he lectured and helped [Donald Knuth](Donald_Knuth "Donald Knuth") to write volume II of [The Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming). He has worked at or consulted for [Xerox PARC](https://en.wikipedia.org/wiki/PARC_%28company%29), [Symbolics](https://en.wikipedia.org/wiki/Symbolics), [Wolfram Research](https://en.wikipedia.org/wiki/Wolfram_Research), the [Lawrence Livermore National Laboratory](Lawrence_Livermore_National_Laboratory "Lawrence Livermore National Laboratory"), and [Macsyma](https://en.wikipedia.org/wiki/Macsyma) <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Bill Gosper created numerous [packing problem](https://en.wikipedia.org/wiki/Packing_problem) puzzles such as the *Twubblesome Twelve* <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and was interested in the [Conway's](John_H._Conway "John H. Conway") [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), where he found the [Gun](https://en.wikipedia.org/wiki/Gun_%28cellular_automaton%29%7CGlider) and originated the [Hashlife](https://en.wikipedia.org/wiki/Hashlife) algorithm to speed up the computation of Life patterns.

## Robert Q

First tournament game by a computer, Carl Wagner (2190) - [Mac Hack VI](Mac_Hack "Mac Hack") aka "[Robert Q](Template:Robert_Q "Template:Robert Q")", January 21, 1967 <a id="cite-note-5" href="#cite-ref-5">[5]</a>.
"Robert Q", a computer programmed to play chess, was beaten in its first competition with a human, Carl Wagner. The [computer](PDP-6 "PDP-6"), at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") in [Cambridge, Mass.](https://en.wikipedia.org/wiki/Cambridge,_Massachusetts), was operated by Allen Moulton, and R. William Gosper, while Wagner made his moves several miles away in the YMCU in [Boston](https://en.wikipedia.org/wiki/Boston). The moves were relayed into the computer by teletype operated by [Alan Baisley](Alan_Baisley "Alan Baisley"). "Robert Q" was entered as an experiment, in the monthly [Boylston Chess Club](http://www.boylstonchessclub.org/) Tournament at the [Young Mens Christian Union](https://en.wikipedia.org/wiki/Boston_Young_Men%27s_Christian_Union).

[](File:RobertQ1967.JPG)
Allen Moulton and R. William Gosper (rear right) operating "[Robert Q](Mac_Hack#RobertQ "Mac Hack")" on a [PDP-6](PDP-6 "PDP-6") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

## HAKMEM

[HAKMEM](https://en.wikipedia.org/wiki/HAKMEM), alternatively known as [AI Memo](https://en.wikipedia.org/wiki/AI_Memo) 239, is a February 1972 "memo" (technical report) of the [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") [AI Lab](https://en.wikipedia.org/wiki/MIT_Computer_Science_and_Artificial_Intelligence_Laboratory) by Gosper et al. that describes a wide variety of [hacks](https://en.wikipedia.org/wiki/Kludge#In_computer_science), primarily useful and clever [algorithms](Algorithms "Algorithms") <a id="cite-note-7" href="#cite-ref-7">[7]</a>, and even a chess position <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>. A few samples, referred elsewhere:

## HAKMEM 70

HAKMEM 70, A neat chess problem, swiped from *Chess for Fun and Chess for Blood*, by [Edward Lasker](https://en.wikipedia.org/wiki/Edward_Lasker) <a id="cite-note-10" href="#cite-ref-10">[10]</a>. White mates in three moves <a id="cite-note-11" href="#cite-ref-11">[11]</a>:

<img src="https://lichess1.org/export/fen.gif?fen=5B2/6P1/1p6/8/1N6/kP6/2K5/8 w - -" style="
    width: 300px;
">

5B2/6P1/1p6/8/1N6/kP6/2K5/8 w - -

## HAKMEM 169

[HAKMEM 169](Population_Count#HAKMEM169 "Population Count"), to [count the ones](Population_Count "Population Count") in a [PDP-6](PDP-6 "PDP-6")/[PDP-10](PDP-10 "PDP-10") 36-bit word, written in [Assembly](Assembly#HAKMEM169 "Assembly") <a id="cite-note-12" href="#cite-ref-12">[12]</a>

```C++

   LDB   B,[014300,,A]     ;or MOVE B,A then LSH B,-1
   AND   B,[333333,,333333]
   SUB   A,B
   LSH   B,-1
   AND   B,[333333,,333333]
   SUBB  A,B               ;each octal digit is replaced by number of 1's in it
   LSH   B,-3
   ADD   A,B
   AND   A,[070707,,070707]
   IDIVI A,77              ;casting out 63.'s

```

## HAKMEM 175

[HAKMEM 175](Traversing_Subsets_of_a_Set#Snoob "Traversing Subsets of a Set") - next higher number with the same number of one bits (Snoob), by Bill Gosper, [PDP-6](PDP-6 "PDP-6") [Assembly](Assembly "Assembly"):

```C++

   MOVE  B,A
   MOVN  C,B
   AND   C,B
   ADD   A,C
   MOVE  D,A
   XOR   D,B
   LSH   D,-2
   IDIVM D,C
   IOR   A,C

```

## Gosper's Glider Gun

\[
Gosper's [Glider Gun](https://en.wikipedia.org/wiki/Gun_%28cellular_automaton%29) in action — a variation of [Conway's](John_H._Conway "John H. Conway") [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) <a id="cite-note-13" href="#cite-ref-13">[13]</a>

## See also

- [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling")
- [Mac Hack VI](Mac_Hack "Mac Hack")
- [PDP-6](PDP-6 "PDP-6")
- [Traversing Subsets of a Set](Traversing_Subsets_of_a_Set "Traversing Subsets of a Set")

## Selected Publications

- Michael Beeler, Bill Gosper, [Rich Schroeppel](https://en.wikipedia.org/wiki/Richard_Schroeppel) (**1972**). *[HAKMEM](https://dspace.mit.edu/handle/1721.1/6086)*, Memo 239, Artificial Intelligence Laboratory, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- Bill Gosper (**1974**). *[Acceleration of Series](https://dspace.mit.edu/handle/1721.1/6088), Memo 304*. [CSAIL](https://en.wikipedia.org/wiki/MIT_Computer_Science_and_Artificial_Intelligence_Laboratory), [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- Bill Gosper (**1976**). *[Continued Fraction Arithmetic](https://perl.plover.com/classes/cftalk/INFO/gosper.txt)*. <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a>
- Bill Gosper (**1977**). *Decision procedure for indefinite hypergeometric summation*. [PNAS USA](https://en.wikipedia.org/wiki/Proceedings_of_the_National_Academy_of_Sciences_of_the_United_States_of_America), Vol. 75, No. 1, [pdf](http://www.pnas.org/content/75/1/40.full.pdf) <a id="cite-note-16" href="#cite-ref-16">[16]</a>
- Corey Ziegler Hunts, Julian Ziegler Hunts, Bill Gosper, [Jack Holloway](Jack_Holloway "Jack Holloway") (**2010**). *[Minskys & Trinskys](http://www.blurb.com/b/2172660-minskys-trinskys-3rd-edition)*. 3rd edition, [Minsky files](http://gosper.org/Minskys/) by Bill Gosper <a id="cite-note-17" href="#cite-ref-17">[17]</a> » [Marvin Minsky](Marvin_Minsky "Marvin Minsky")

## External Links

- [Bill Gosper from Wikipedia](https://en.wikipedia.org/wiki/Bill_Gosper)
- [Twubblesome Twelve - a difficult puzzle](http://gosper.org/)

[R. William Gosper](http://gosper.org/bill.html)
[Rep-tiles](http://www.tweedledum.com/rwg/)

- [HAKMEM from Wikipedia](https://en.wikipedia.org/wiki/HAKMEM), [HAKMEMC -- HAKMEM Programming hacks in C](http://www.cl.cam.ac.uk/~am21/hakmemc.html) by [Alan Mycroft](http://www.cl.cam.ac.uk/~am21/)
- [Gosper's algorithm from Wikipedia](https://en.wikipedia.org/wiki/Gosper%27s_algorithm)
- [Gosper curve from Wikipedia](https://en.wikipedia.org/wiki/Gosper_curve)
- [Hashlife from Wikipedia](https://en.wikipedia.org/wiki/Hashlife)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Mathematician Bill Gosper in March, 2006 at the [Seventh Gathering for Gardner](http://www.ifp.illinois.edu/~sdickson/G4G7/G4G7_Trip_Report.html) (G4G7) in [Atlanta](https://en.wikipedia.org/wiki/Atlanta), [Georgia](https://en.wikipedia.org/wiki/Georgia_%28U.S._state%29), March 16, 2006, Photographer [Thane Plambeck](http://www.flickr.com/people/thane/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Hackers: Heroes of the Computer Revolution](https://en.wikipedia.org/wiki/Hackers:_Heroes_of_the_Computer_Revolution)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Bill Gosper from Wikipedia](https://en.wikipedia.org/wiki/Bill_Gosper)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Twubblesome Twelve - a difficult puzzle](http://gosper.org/) by Bill Gosper
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> *[MIT Computer Loses to Human in Chess](http://news.google.com/newspapers?nid=1928&dat=19670123&id=O2ggAAAAIBAJ&sjid=1GYFAAAAIBAJ&pg=2308,2313204)*. [Sun Journal (Lewiston)](https://en.wikipedia.org/wiki/Sun_Journal_%28Lewiston%29), January 23, 1967, [Google News](https://en.wikipedia.org/wiki/Google_News)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> *[MIT Computer Loses to Human in Chess](https://news.google.com/newspapers?nid=1928&dat=19670123&id=O2ggAAAAIBAJ&sjid=1GYFAAAAIBAJ&pg=2308,2313204&hl=en)*. [Sun Journal (Lewiston)](https://en.wikipedia.org/wiki/Sun_Journal_%28Lewiston%29), January 23, 1967, [Google News](https://en.wikipedia.org/wiki/Google_News)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [HAKMEM from Wikipedia](https://en.wikipedia.org/wiki/HAKMEM)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> Michael Beeler, Bill Gosper, [Rich Schroeppel](https://en.wikipedia.org/wiki/Richard_Schroeppel) (**1972**). *[HAKMEM](https://dspace.mit.edu/handle/1721.1/6086)*, Memo 239, Artificial Intelligence Laboratory, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [HAKMEMC -- HAKMEM Programming hacks in C](http://www.cl.cam.ac.uk/~am21/hakmemc.html) by [Alan Mycroft](http://www.cl.cam.ac.uk/~am21/)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Edward Lasker](https://en.wikipedia.org/wiki/Edward_Lasker) (**1942,1962**) *Chess for Fun and Chess for Blood*. Dover Publications; 2 Edition, ISBN-13: 978-0486201467, [amazon](http://www.amazon.com/Chess-Fun-Blood-Edward-Lasker/dp/0486201465)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> 1.g8=N b5 2.Ne7 Kxb4 3.Nc6#
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [HAKMEM 169](Population_Count#HAKMEM169 "Population Count") by Gosper, Mann, Lenard, (Root and Mann)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> Bill Gosper's [Glider Gun](https://en.wikipedia.org/wiki/Gun_%28cellular_automaton%29) in action — a variation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). This image was made by using [Life32 v2.15 beta](http://psoup.math.wisc.edu/Life32.html) by Johan G. Bontes, 2005, [Gun (cellular automaton) from Wikipedia](https://en.wikipedia.org/wiki/Gun_%28cellular_automaton%29)
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Arithmetic with Continued Fractions](https://perl.plover.com/yak/cftalk/) by [Mark Jason Dominus](https://en.wikiquote.org/wiki/Mark_Jason_Dominus),
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Continued fraction from Wikipedia](https://en.wikipedia.org/wiki/Continued_fraction)
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Gosper's algorithm from Wikipedia](https://en.wikipedia.org/wiki/Gosper%27s_algorithm)
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [The Minsky Circle Algorithm – Random (Blog)](https://nbickford.wordpress.com/2011/04/03/the-minsky-circle-algorithm/) by [Neil Bickford](https://nbickford.wordpress.com/author/nbickford/), April 3, 2011

**[Up one level](People "People")**

