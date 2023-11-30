---
title: Recursion
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Algorithms](Algorithms "Algorithms") \* Recursion**



 [](File:Bottrop_Halde_Beckstra%C3%9Fe_Tetraeder.JPG) [Tetrahedron in Bottrop](https://en.wikipedia.org/wiki/Tetrahedron_in_Bottrop) <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Recursion** is a technique to define a function, or process of repeating objects, in a [self-similar](https://en.wikipedia.org/wiki/Self-similarity) way. In computer science it is a method or algorithm where the solution to a problem depends on solutions to smaller instances of the same problem.



## Recursive Definitions


A [recursive definition](https://en.wikipedia.org/wiki/Recursive_definition) of an object refers inductive terms of itself. A function set need to specify the function for some discrete values like zero, one or empty (base case), and to reduce all other cases by [divide and conquer](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm) toward the base case. [Recurrence relation](https://en.wikipedia.org/wiki/Recurrence_relations) is an equation that recursively defines a sequence of symbols or numbers <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 


*Some more or less computer chess related examples ...*



### PGN Syntax


The [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form)-like [Syntax](https://en.wikipedia.org/wiki/Syntax) of the [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") by [Steven Edwards](Steven_Edwards "Steven Edwards") contains some recursive definitions, most [tail recursion](https://en.wikipedia.org/wiki/Tail_recursion) for iteration of games, and tag-pairs and elements inside a game <a id="cite-note-3" href="#cite-ref-3">[3]</a> :




```C++

<PGN-database> ::= <PGN-game> <PGN-database>
                   <empty>

<tag-section> ::= <tag-pair> <tag-section>
                  <empty>

<element-sequence> ::= <element> <element-sequence>
                       <recursive-variation> <element-sequence>
                       <empty>

<recursive-variation> ::= ( <element-sequence> )

```

### Index of PV-Array


An index of a [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table") may be defined recursively that way ...




```C++
index(0) = 0
index(ply+1) = index(ply) + N - ply

```

...which can be trivially transformed from [tail recursion](https://en.wikipedia.org/wiki/Tail_recursion) to [iteration](https://en.wikipedia.org/wiki/Iteration), finally applying a [summation](https://en.wikipedia.org/wiki/Summation):




```C++
index(ply) = ½ ply (2N + 1 - ply )

```

### Population Count


The recursive definition of [population count](Population_Count "Population Count") (number of one-bits in a computer word i. e. a [bitboard](Bitboards "Bitboards")) can be transformed to iteration as well, but lacks an arithmetical sum-formula:




```C++
popcnt(0) = 0
popcnt(n) = popcnt(n ÷ 2) + (n mod 2)

```





### Infix Expression


[Formal syntax](https://en.wikipedia.org/wiki/Syntax_%28programming_languages%29) of [programming languages](Languages "Languages") likely contain recursive definitions, i. e. [parsing](https://en.wikipedia.org/wiki/Parsing) of arithmetical (and/or boolean) [infix notation](https://en.wikipedia.org/wiki/Infix_notation) therefor implies indirect recursion, as demonstrated in following example with constants and [elementary arithmetic](https://en.wikipedia.org/wiki/Elementary_arithmetic) only, which might even evaluated at [compile time](https://en.wikipedia.org/wiki/Compile_time):


*[Terminal and none terminal symbols](https://en.wikipedia.org/wiki/Terminal_and_nonterminal_symbols) of a variant of [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) below are embedded in ' ' resp. < >.*




```C++

<expression> ::= <term>   [ {'+' | '-'} <term> ]...
      <term> ::= <factor> [ {'*' | '/'} <factor> ]...
    <factor> ::= <constant> | '(' <expression> ')'

```

## Implementation


In [procedual programming](https://en.wikipedia.org/wiki/Procedural_programming), recursion is done by a procedure aka [subroutine](https://en.wikipedia.org/wiki/Subroutine), method or function, which calls itself if no base case is determined, utilizing the [processor stack](Stack "Stack"). One has to take care the nesting is not too deep or infinite, which yields in a [Stack overflow](https://en.wikipedia.org/wiki/Stack_buffer_overflow) and abnormal program termination or crashing. 



## Recursive Data types


[Recursive data types](https://en.wikipedia.org/wiki/Recursive_data_type) contain references (i. e. pointer in [C](C "C")) to objects of the same type to build [directed graphs](https://en.wikipedia.org/wiki/Directed_graph), such as [linked lists](Linked_List "Linked List") or [trees](Search_Tree "Search Tree").



## Recursive Algorithms


### Searching


Tree-like data structures which are traversed in [depth-first](index.php?title=Depth-first&action=edit&redlink=1 "Depth-first (page does not exist)") manner can be implemented with recursion using a [stack](Stack "Stack") of nodes. [Minimax](Minimax "Minimax") and [alpha-beta](Alpha-Beta "Alpha-Beta") are typical examples of indirect recursive routines, where Min calls Max and Max calls Min, and [Negamax](Negamax "Negamax") turns the indirect recursion to a direct one. While [tail recursion](https://en.wikipedia.org/wiki/Tail_recursion) or [primitive recursion](https://en.wikipedia.org/wiki/Primitive_recursive_function) can easily turned into iterative solutions, it is more complicated for not primitive recursion. However, recursion can turned to a non-recursive version based on the use of [continuations](https://en.wikipedia.org/wiki/Continuation), see [Iterative Search](Iterative_Search "Iterative Search").


[Knuth](Donald_Knuth "Donald Knuth") and Moore already introduced an [iterative solution](Knuth-iterative "Knuth-iterative") of [Alpha-Beta](Alpha-Beta "Alpha-Beta") in 1975 <a id="cite-note-4" href="#cite-ref-4">[4]</a> :




```C++
It is interesting to convert this recursive procedure to an iterative (non-recursive) form by a sequence of mechanical transformations, and to apply simple optimizations which preserve program correctness. The resulting procedure is surprisingly simple, but not as easy to prove correct as the recursive form.

```

So called recursive [pruning](Pruning "Pruning"), especially [null move pruning](Null_Move_Pruning "Null Move Pruning"), or [extensions](Extensions "Extensions") refers to the fact that these events may occur multiple times inside a variation or path of the (recursive) search process. 



### Sorting


A well-known [sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm) is [Quicksort](https://en.wikipedia.org/wiki/Quicksort) developed in 1960 by [C. A. R. Hoare](Mathematician#CARHoare "Mathematician"). It recursively partitions and sorts two sub-lists from a list, whose elements are either less and greater a chosen [pivot element](https://en.wikipedia.org/wiki/Pivot_element). However, for [move ordering](Move_Ordering "Move Ordering") to sort [move lists](Move_List "Move List") in [alpha-beta](Alpha-Beta "Alpha-Beta"), most chess programmer use a [selection sort](https://en.wikipedia.org/wiki/Selection_sort) to pick a [move](Moves "Moves") with best assigned score, since the effort to sort other moves may needless in case of a [beta-cutoff](Beta-Cutoff "Beta-Cutoff"). 



[
Visualization of the [quicksort algorithm](https://en.wikipedia.org/wiki/Quicksort) <a id="cite-note-5" href="#cite-ref-5">[5]</a>



## See also


* [ABDADA](ABDADA "ABDADA")


 [Recursive vs. Iterative Search](ABDADA#Recursion "ABDADA")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Backtracking](Backtracking "Backtracking")
* [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator")
* [Depth-First](Depth-First "Depth-First")
* [Iteration](Iteration "Iteration")
* [Iterative Search](Iterative_Search "Iterative Search")
* [Jamboree](Jamboree "Jamboree")
* [Minimax](Minimax "Minimax")
* [Negamax](Negamax "Negamax")
* [Parallel Alpha-Beta](Cilk#ParallelAlphaBeta "Cilk") in [Cilk](Cilk "Cilk")


## Publications


* [John McCarthy](John_McCarthy "John McCarthy") (**1960**). *Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I*, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://www-formal.stanford.edu/jmc/recursive.pdf)
* [V. I. Sobel'man](http://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=63222), [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") (**1962**). *[Realization of recursive procedures in the language of AlGOL-60](http://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=zvmmf&paperid=7886&option_lang=eng)*. (Реализация Рекурсивных Процедур В Языке Алгол-60) [Zhurnal Vychislitel'noi Matematiki i Matematicheskoi Fiziki](http://www.mathnet.ru/php/archive.phtml?jrnid=zvmmf&option_lang=eng&wshow=statlist), Vol. 2, No. 2
* [Michael Levin](Michael_Levin "Michael Levin") (**1963**). *Primitive Recursion*. AIM-055, reprint available from [DSpace](http://dspace.mit.edu/handle/1721.1/6109) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
* [Craig A. Finseth](http://www.finseth.com/parts/index.php) (**1980**). *[Something is Missing (Implementing recursion and stacks in BASIC)](http://www.atariarchives.org/bcc3/showpage.php?page=45)*. [The Best of Creative Computing Volume 3](Creative_Computing#Best3 "Creative Computing") » [Basic](Basic "Basic")
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1988**). *On the Complexity of Searching Game Trees and Other Recursion Trees*. Journal of Algorithms, Vol. 9, No. 4
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1991**) *On pathology in game tree and other recursion tree models*. Habilitation Thesis, [University of Bielefeld](https://en.wikipedia.org/wiki/University_of_Bielefeld)
* [Donald Knuth](Donald_Knuth "Donald Knuth") (**1991**). *Textbook examples of recursion*. [arXiv:cs/9301113](https://arxiv.org/abs/cs/9301113)
* [Raymond Smullyan](Raymond_Smullyan "Raymond Smullyan") (**1993**). *Recursion Theory for Metamathematics*. [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press) <a id="cite-note-6" href="#cite-ref-6">[6]</a>
* [Richard J. Lorentz](Richard_J._Lorentz "Richard J. Lorentz") (**1994**). *[Recursive algorithms](http://www.abebooks.com/book-search/isbn/0893919136/)*. Intellect Books
* [Kevin Coplan](Kevin_Coplan "Kevin Coplan") (**1998**). *Synthesis of Chess and Chess-like Endgames by Recursive Optimisation*. [ICCA Journal, Vol. 21, No. 3](ICGA_Journal#21_3 "ICGA Journal")
* [David Slate](David_Slate "David Slate"), [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**2009**). *Recursive Binary Partitioning, Old Dogs with New Tricks*, [KDD Conference 2009](http://www.sigkdd.org/kdd2009/index.html), slides as [pdf](http://clopinet.com/isabelle/Projects/KDDcup09/Slides/Frey_slides.pdf) <a id="cite-note-7" href="#cite-ref-7">[7]</a>


## Forum Posts


* [Was ist rekursiv? irrelevant!](http://hr.userweb.mwn.de/tmp/nat-cf.html) by [Helmut Richter](Helmut_Richter "Helmut Richter"), [sci.lang](http://groups.google.com/group/sci.lang/topics), September 29, 1998
* [how to print tree non-recursively](http://www.talkchess.com/forum/viewtopic.php?t=42588) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 24, 2012 » [Search Tree](Search_Tree "Search Tree"), [Iteration](Iteration "Iteration")
* [Recursive DTS-like search algorithm](http://www.talkchess.com/forum/viewtopic.php?t=48752) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 24, 2013 » [Texel](Texel "Texel"), [Parallel Search](Parallel_Search "Parallel Search")


## External Links


### Recursion


* [Recursion from Wikipedia](https://en.wikipedia.org/wiki/Recursion)
* [Recursion](http://mathworld.wolfram.com/Recursion.html) by [Weisstein, Eric W.](http://mathworld.wolfram.com/about/author.html) from [Wolfram MathWorld](http://mathworld.wolfram.com/)
* [Recursion (computer science) from Wikipedia](https://en.wikipedia.org/wiki/Recursion_%28computer_science%29)
* [Recursive acronym from Wikipedia](https://en.wikipedia.org/wiki/Recursive_acronym)
* [Recursive data type from Wikipedia](https://en.wikipedia.org/wiki/Recursive_data_type)
* [Recursive definition from Wikipedia](https://en.wikipedia.org/wiki/Recursive_definition)
* [Recursion in Nature, Mathematics and Art](http://www.mi.sanu.ac.rs/vismath/bridges2005/burns/index.html) by [Anne M. Burns](Mathematician#AMBurns "Mathematician")
* [Recursion theory from Wikipedia](https://en.wikipedia.org/wiki/Recursion_theory)


### Recursive Functions


* [Recursive function from Wikipedia](https://en.wikipedia.org/wiki/Recursive_function)


 [Primitive recursive function from Wikipedia](https://en.wikipedia.org/wiki/Primitive_recursive_function)
 [Leaf subroutine from Wikipedia](https://en.wikipedia.org/wiki/Leaf_subroutine)
 [Tail call from Wikipedia](https://en.wikipedia.org/wiki/Tail_call)
### Ackermann Function


* [Ackermann function from Wikipedia](https://en.wikipedia.org/wiki/Ackermann_function) » [Wilhelm Ackermann](Mathematician#WAckermann "Mathematician")
* [Ackermann Function](http://mathworld.wolfram.com/AckermannFunction.html) by [Weisstein, Eric W.](http://mathworld.wolfram.com/about/author.html) from [Wolfram MathWorld](http://mathworld.wolfram.com/)


### McCarthy 91-Function


Introduced by [Zohar Manna](Mathematician#Manna "Mathematician"), [Amir Pnueli](Mathematician#APnueli "Mathematician") and [John McCarthy](John_McCarthy "John McCarthy") in 1970.



* [McCarthy 91 function from Wikipedia](https://en.wikipedia.org/wiki/McCarthy_91_function)
* [McCarthy 91-Function](http://mathworld.wolfram.com/McCarthy91-Function.html) by [Weisstein, Eric W.](http://mathworld.wolfram.com/about/author.html) from [Wolfram MathWorld](http://mathworld.wolfram.com/)


### Tak


* [Tak (function) from Wikipedia](https://en.wikipedia.org/wiki/Tak_(function))
* [TAK Function](http://mathworld.wolfram.com/TAKFunction.html) by [Weisstein, Eric W.](http://mathworld.wolfram.com/about/author.html) from [Wolfram MathWorld](http://mathworld.wolfram.com/)


### Self-reference


* [Self-reference from Wikipedia](https://en.wikipedia.org/wiki/Self-reference)
* [Droste effect from Wikipedia](https://en.wikipedia.org/wiki/Droste_effect)


 [
 [Escher and the Droste effect](http://escherdroste.math.leidenuniv.nl/) - [Universiteit Leiden](Leiden_University "Leiden University") » [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher")
* [Mise en abyme from Wikipedia](https://en.wikipedia.org/wiki/Mise_en_abyme)
* [Ouroboros from Wikipedia](https://en.wikipedia.org/wiki/Ouroboros)


 [
* [The Treachery of Images](https://en.wikipedia.org/wiki/The_Treachery_of_Images) by [René Magritte](index.php?title=Category:Ren%C3%A9_Magritte&action=edit&redlink=1 "Category:René Magritte (page does not exist)")


 [](https://en.wikipedia.org/wiki/The_Treachery_of_Images) 
### Fractals


* [Fractal from Wikipedia](https://en.wikipedia.org/wiki/Fractal)


 [Hilbert curve from Wikipedia](https://en.wikipedia.org/wiki/Hilbert_curve) » [David Hilbert](Mathematician#Hilbert "Mathematician")
 [Koch snowflake from Wikipedia](https://en.wikipedia.org/wiki/Koch_snowflake) » [Helge von Koch](Mathematician#HvKoch "Mathematician")
 [
 [Peano curve from Wikipedia](https://en.wikipedia.org/wiki/Peano_curve) » [Giuseppe Peano](Mathematician#Peano "Mathematician")
 [Sierpinski triangle from Wikipedia](https://en.wikipedia.org/wiki/Sierpinski_triangle) » [Wacław Sierpiński](Mathematician#Sierpinski "Mathematician")
### Misc


* [Divide and conquer algorithm from Wikipedia](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm)
* [Eternal return from Wikipedia](https://en.wikipedia.org/wiki/Eternal_return)
* [Lambda Calculus from Wikipedia](https://en.wikipedia.org/wiki/Lambda_calculus)
* [Knights of the Lambda Calculus from Wikipedia](https://en.wikipedia.org/wiki/Knights_of_the_Lambda_Calculus) » [Alonzo Church](Mathematician#Church "Mathematician")
* [Mathematical induction from Wikipedia](https://en.wikipedia.org/wiki/Mathematical_induction)
* [Recurrence relation from Wikipedia](https://en.wikipedia.org/wiki/Recurrence_relations)
* [Reentrant (subroutine) from Wikipedia](https://en.wikipedia.org/wiki/Reentrant_%28subroutine%29)
* [Turing completeness from Wikipedia](https://en.wikipedia.org/wiki/Turing_completeness)
* [Return to Forever](Category:Return_to_Forever "Category:Return to Forever"), [San Sebastian Jazz Festival](https://en.wikipedia.org/wiki/San_Sebastian_Jazz_Festival), July 25, 2008, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Chick Corea](Category:Chick_Corea "Category:Chick Corea"), [Stanley Clarke](Category:Stanley_Clarke "Category:Stanley Clarke"), [Al Di Meola](Category:Al_Di_Meola "Category:Al Di Meola"), [Lenny White](Category:Lenny_White "Category:Lenny White")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Tetrahedron](https://en.wikipedia.org/wiki/Tetrahedron) in [Bottrop](https://en.wikipedia.org/wiki/Bottrop), [North Rhine-Westphalia](https://en.wikipedia.org/wiki/North_Rhine-Westphalia), Germany, part of [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail"), [Image](https://commons.wikimedia.org/wiki/File:Bottrop_-_Halde_Beckstra%C3%9Fe_-_Tetraeder_03_ies.jpg) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), April 08, 2017. The design is reminiscent of the [Sierpinski tetrix](https://en.wikipedia.org/wiki/Sierpinski_triangle#Analogues_in_higher_dimensions) : placing four half-size tetrahedra corner to corner and adding an octahedron in the middle, a full-size tetrahedron is formed; this process can be repeated recursively to form larger and larger tetrahedra, from [Tetrahedron in Bottrop from Wikipedia](https://en.wikipedia.org/wiki/Tetrahedron_in_Bottrop), [Category:Tetraeder Bottrop](https://commons.wikimedia.org/wiki/Category:Tetraeder_Bottrop) - [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Halden im Ruhrgebiet](http://www.halden.ruhr/halden.html) (German)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Hofstadter sequence from Wikipedia](https://en.wikipedia.org/wiki/Hofstadter_sequence)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Standard: Portable Game Notation Specification and Implementation Guide](http://www.thechessdrum.net/PGN_Reference.txt) by [Steven Edwards](Steven_Edwards "Steven Edwards"), 18: Formal syntax
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Donald Knuth](Donald_Knuth "Donald Knuth"), [Ronald W. Moore](http://www.informatik.uni-trier.de/~ley/pers/hd/m/Moore:Ronald_W=) (**1975**). *[An analysis of alpha-beta pruning](http://www.scribd.com/doc/28194932/An-Analysis-of-Alpha-Beta-Pruning).* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Quicksort from Wikipedia](https://en.wikipedia.org/wiki/Quicksort)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Metamathematics from Wikipedia](https://en.wikipedia.org/wiki/Metamathematics)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Results of the KDD cup 2009](http://www.kddcup-orange.com/winners.php)

**[Up one Level](Algorithms "Algorithms")**







 
