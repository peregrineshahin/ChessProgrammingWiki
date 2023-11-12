---
title: Iteration
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Algorithms](Algorithms "Algorithms") \* Iteration**



 [](http://www.natur-struktur.ch/populationen/iterationen.html) Iteration <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
In computer science, **Iteration** is the act of repeating instructions inside an algorithm, implemented either by the control structure of a [loop](https://en.wikipedia.org/wiki/Loop_%28computing%29#Loops) or by direct or indirect [recursive](Recursion "Recursion") calls. Despite all kinds of low level loops supported by various [programming languages](Languages "Languages"), so called [Iterators](https://en.wikipedia.org/wiki/Iterator) allow for traversing [data container](https://en.wikipedia.org/wiki/Container_%28data_structure%29) hiding the concrete implementation, i.e. [linked list](Linked_List "Linked List") or [array](Array "Array"). While recursion can be considered as a special case of iteration, iteration describes the style of [imperative programming](https://en.wikipedia.org/wiki/Imperative_programming) in contrast to the more [declarative](https://en.wikipedia.org/wiki/Declarative_programming) nature of recursion. In a stricter sense, to distinguish iteration from recursion, iteration implies performing a loop inside the [scope](https://en.wikipedia.org/wiki/Scope_%28computer_science%29) of a [subroutine](https://en.wikipedia.org/wiki/Subroutine) restricted to one [stack frame](https://en.wikipedia.org/wiki/Call_stack) in a call hierarchy, or equivalently processed by the same local iterator object. 



### Learning


[Learning](Learning "Learning") and [automated tuning](Automated_Tuning "Automated Tuning") in computer chess programming deals with algorithms that allow the program to change its behavior based on data acquired during game play against variations of itself or a variety of opponents considering the final outcome and/or the game record. [Evolutionary computation](Genetic_Programming#EvolutionaryComputation "Genetic Programming"), [genetic programming](Genetic_Programming "Genetic Programming") and [simulated annealing](Simulated_Annealing "Simulated Annealing") apply iterative processes where one iteration deals with one generation of the chess or game playing program.



### Game Loop


Playing a [game of chess](Chess_Game "Chess Game") versus a chess program, is a sequential, iterative process. The next iteration either starts after the program played its move and starts [pondering](Pondering "Pondering"), or the user [entered a move](Entering_Moves "Entering Moves"). The [Game Loop](Chess_Game#GameLoop "Chess Game") terminates when the game is finished or aborted.



### Iterative Deepening


In the context of [Iterative Deepening](Iterative_Deepening "Iterative Deepening") in [search algorithms](Search "Search"), an iteration refers the current call of the search routine with a certain [search depth](Depth "Depth") inside the loop body of the ID framework. The resulting sequence is a sequence of [exact scores](Exact_Score "Exact Score") for subsequent incremented search depths.



### Move Loop


The typical [control structure](https://en.wikipedia.org/wiki/Control_flow) inside a [minimax](Minimax "Minimax") [depth-first search](Depth-First "Depth-First") of a chess program is the Move Loop, a [generator](https://en.wikipedia.org/wiki/Generator_%28computer_programming%29) or [iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern) traversing the moves of one [node](Node "Node") or [position](Chess_Position "Chess Position"). The whole implementation details of [move generation](Move_Generation "Move Generation"), [move ordering](Move_Ordering "Move Ordering"), [pruning](Pruning "Pruning"), bookkeeping and accessing a [move list](Move_List "Move List"), might be hidden behind an iterator object and its interface.



### Search


While the "horizontal" iteration of the move loop appears in one node, the "vertical" edges of the [search tree](Search_Tree "Search Tree"), that is actually [making the move](Make_Move "Make Move") and recursively calling the [negamaxed](Negamax "Negamax") [search](Search "Search") routine for the child node, appear in the current depth-first variation started at the [root](Root "Root"). It can be considered as nested iterations of the move loops processed in all upper nodes. Keeping an explicit [stack](Stack "Stack") of move iterators per node further allows to reformulate the recursive search routine as iterative solution, with makes it simpler to unwind the search.



### Recursion to Iteration


[Tail recursion](https://en.wikipedia.org/wiki/Tail_call) is trivially convertible to iteration <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and performed by various optimizing compilers. Since a call as used in recursion is nothing else than a [jump](https://en.wikipedia.org/wiki/Jump_%28computer_science%29) to an address, remembering the next instruction on the stack for the [return](https://en.wikipedia.org/wiki/Return_statement), recursion can always replaced by iteration using an array as explicit stack, an index (stack pointer) for the current nesting level, and [goto](https://en.wikipedia.org/wiki/Goto) instructions, as demonstrated in [Iterative Search](Iterative_Search "Iterative Search"). [Knuth](Donald_Knuth "Donald Knuth") and Moore already introduced an [iterative solution](Knuth-iterative "Knuth-iterative") of [Alpha-Beta](Alpha-Beta "Alpha-Beta") in 1975 <a id="cite-note-4" href="#cite-ref-4">[4]</a> . Iterative solutions of otherwise recursive algorithms are harder to understand and to [debug](Debugging "Debugging") and tend to become [Spaghetti code](https://en.wikipedia.org/wiki/Spagetti_code) <a id="cite-note-5" href="#cite-ref-5">[5]</a>, but are required for certain [parallel search](Parallel_Search "Parallel Search") algorithms like [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting"). There are jumps from inside the move loop body outside (call), and vice versa (return).



## Iterative Algorithms


In [computational mathematics](https://en.wikipedia.org/wiki/Computational_mathematics), an [iterative algorithm](https://en.wikipedia.org/wiki/Iterative_method) or method is a procedure that generates [integer](https://en.wikipedia.org/wiki/Integer_sequence), [fixed point](https://en.wikipedia.org/wiki/Fixed-point_arithmetic), or [floating point](Float "Float") sequences and calculates [Series](https://en.wikipedia.org/wiki/Series_%28mathematics%29). Iterative algorithms are used to approximate [nonlinear equations](https://en.wikipedia.org/wiki/Nonlinear_system) <a id="cite-note-6" href="#cite-ref-6">[6]</a> and to solve certain optimization problems. An iterative method is called convergent if the corresponding sequence converges for given initial approximations. 




### PRNG


In computer chess, iterative algorithms are used for instance directly or indirectly in initializing [Zobrist keys](Zobrist_Hashing "Zobrist Hashing") with [Pseudorandom number generators](Pseudorandom_Number_Generator "Pseudorandom Number Generator") (PRNG), for instance the [linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator), the [Mersenne twister](https://en.wikipedia.org/wiki/Mersenne_twister), the [Xorshift](https://en.wikipedia.org/wiki/Xorshift) by [George Marsaglia](Mathematician#GMarsaglia "Mathematician") or the [KISS](Bob_Jenkins#RKISS "Bob Jenkins") approach by [Bob Jenkins](Bob_Jenkins "Bob Jenkins") similar as used in [Stockfish](Stockfish "Stockfish") <a id="cite-note-7" href="#cite-ref-7">[7]</a>. 



### Fill Algorithms


[Flood-filling](Fill_Algorithms "Fill Algorithms") in [bitboards](Bitboards "Bitboards") is an iterative method as well, consecutively feeding back the propagated output as input. The loop terminates if either the flood stops or has reached a target set.



## See also


* [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Backtracking - Eight Queens puzzle with Bitboards](Backtracking#8QinBitboards "Backtracking")
* [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization")
* [Flood Fill Algorithms](King_Pattern#FloodFillAlgorithms "King Pattern")
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Iterative Search](Iterative_Search "Iterative Search")
* [Mate-in-two](Mate-in-two "Mate-in-two")
* [Pseudorandom Number Generator](Pseudorandom_Number_Generator "Pseudorandom Number Generator")
* [Recursion](Recursion "Recursion")
* [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis")
* [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")
* [Traversing Subsets of a Set](Traversing_Subsets_of_a_Set "Traversing Subsets of a Set")


## Selected Publications


* [Paul Stein](Paul_Stein "Paul Stein") (**1987**). *Iteration of Maps, Strange Attractors, and Number Theory - An Ulamian Potpourri*. in *[Stanislaw Ulam 1909-1984](http://la-science.lanl.gov/lascience15.shtml)*. [Los Alamos Science](http://la-science.lanl.gov/), No. 15, [pdf](https://www.fas.org/sgp/othergov/doe/lanl/pubs/00285739.pdf) » [Stanislaw Ulam](Stanislaw_Ulam "Stanislaw Ulam")


## Forum Posts


* [how to print tree non-recursively](http://www.talkchess.com/forum/viewtopic.php?t=42588) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 24, 2012 » [Search Tree](Search_Tree "Search Tree"), [Recursion](Recursion "Recursion")


## External Links


### General


* [Iteration from Wikipedia](https://en.wikipedia.org/wiki/Iteration)
* [Iterative and incremental development from Wikipedia](https://en.wikipedia.org/wiki/Iterative_and_incremental_development)
* [Recursion from Wikipedia](https://en.wikipedia.org/wiki/Recursion_%28computer_science%29)


### [Control flow](https://en.wikipedia.org/wiki/Control_flow)


* [Control flow: Loops from Wikipedia](https://en.wikipedia.org/wiki/Control_flow#Loops)
* [Inner loop from Wikipedia](https://en.wikipedia.org/wiki/Inner_loop)
* [Idle loop from Wikipedia](https://en.wikipedia.org/wiki/Idle_%28CPU%29)
* [Spinlock loop from Wikipedia](https://en.wikipedia.org/wiki/Spinlock)


### [Iterator](https://en.wikipedia.org/wiki/Iterator)


* [Iterator pattern from Wikipedia](https://en.wikipedia.org/wiki/Iterator_pattern)


 [Generator (computer programming) from Wikipedia](https://en.wikipedia.org/wiki/Generator_%28computer_programming%29)
* [Iterated function from Wikipedia](https://en.wikipedia.org/wiki/Iterated_function)


### [Programming languages](Languages "Languages")


* [iterator - C++ Reference](http://www.cplusplus.com/reference/std/iterator/) » [C++](Cpp "Cpp")
* [Iterator (Java 2 Platform SE 5.0)](http://download.oracle.com/javase/1,5.0/docs/api/java/util/Iterator.html) » [Java](Java "Java")
* [3.5 Iterator Types - Python Library Reference](http://docs.python.org/release/2.5.2/lib/typeiter.html) » [Python](Python "Python")


### [Iterative methods](https://en.wikipedia.org/wiki/Iterative_method)


* [Arnoldi iteration from Wikipedia](https://en.wikipedia.org/wiki/Arnoldi_iteration)
* [Bregman method from Wikipedia](https://en.wikipedia.org/wiki/Bregman_method)
* [Euclidean algorithm from Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)
* [Fixed point iteration from Wikipedia](https://en.wikipedia.org/wiki/Fixed_point_iteration)
* [Gauss–Newton algorithm from Wikipedia](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm)
* [Gauss–Seidel method from Wikipedia](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)
* [Gradient descent from Wikipedia](https://en.wikipedia.org/wiki/Gradient_descent)
* [Hill climbing from Wikipedia](https://en.wikipedia.org/wiki/Hill_climbing)
* [Householder's method from Wikipedia](https://en.wikipedia.org/wiki/Householder%27s_method)
* [Iterated local search from Wikipedia](https://en.wikipedia.org/wiki/Iterated_local_search)
* [Jacobi eigenvalue algorithm from Wikipedia](https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm)
* [Jacobi Iteration for Eigenvectors](http://math.fullerton.edu/mathews/n2003/JacobiMethodMod.html)
* [Jacobi method](https://en.wikipedia.org/wiki/Jacobi_method)
* [Local search (optimization) from Wikipedia](https://en.wikipedia.org/wiki/Local_search_%28optimization%29)
* [Newton's method from Wikipedia](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)
* [Newton's method in optimization](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)
* [Picard Iteration Revisited](http://math.fullerton.edu/mathews/n2003/picarditerationmod.html)
* [Power iteration from Wikipedia](https://en.wikipedia.org/wiki/Power_iteration)
* [Rate of convergence from Wikipedia](https://en.wikipedia.org/wiki/Rate_of_convergence)
* [Root-finding algorithm from Wikipedia](https://en.wikipedia.org/wiki/Root-finding_algorithm)
* [Simulated annealing from Wikipedia](https://en.wikipedia.org/wiki/Simulated_annealing)
* [Subgradient method from Wikipedia](https://en.wikipedia.org/wiki/Subgradient_method)


### [Sequence](https://en.wikipedia.org/wiki/Sequence)


* [Collatz conjecture from Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)
* [Fibonacci number from Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)
* [Integer sequence from Wikipedia](https://en.wikipedia.org/wiki/Integer_sequence)
* [Linear congruential generator from Wikipedia](https://en.wikipedia.org/wiki/Linear_congruential_generator)
* [Recurrence relation from Wikipedia](https://en.wikipedia.org/wiki/Recurrence_relation)


### [Series](https://en.wikipedia.org/wiki/Series_%28mathematics%29)


* [Arithmetic progression from Wikipedia](https://en.wikipedia.org/wiki/Arithmetic_progression)
* [Convergent series from Wikipedia](https://en.wikipedia.org/wiki/Convergent_series)
* [Geometric series from Wikipedia](https://en.wikipedia.org/wiki/Geometric_series)
* [Fourier series from Wikipedia](https://en.wikipedia.org/wiki/Fourier_series)
* [Harmonic series from Wikipedia](https://en.wikipedia.org/wiki/Harmonic_series_%28mathematics%29)
* [Taylor series from Wikipedia](https://en.wikipedia.org/wiki/Taylor_series)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Iterationen](http://www.natur-struktur.ch/populationen/iterationen.html) from [Strukturen in der Biologie](http://www.natur-struktur.ch/) (German)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Recursion - Tail-recursive functions from Wikipedia,](https://en.wikipedia.org/wiki/Recursion_%28computer_science%29#Tail-recursive_functions)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Replace Recursion with Iteration](http://www.refactoring.com/catalog/replaceRecursionWithIteration.html)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Donald Knuth](Donald_Knuth "Donald Knuth"), [Ronald W. Moore](http://dblp.uni-trier.de/pers/hd/m/Moore:Ronald_W=) (**1975**). *[An analysis of alpha-beta pruning](http://www.scribd.com/doc/28194932/An-Analysis-of-Alpha-Beta-Pruning).* Artificial Intelligence, 6:293–326
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Considered harmful from Wikipedia](https://en.wikipedia.org/wiki/Considered_harmful)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Brian J. Shelburne](Mathematician#BJShelburne "Mathematician") (**1999**). *[Zuse's Z3 Square Root Algorithm](https://studylib.net/doc/7921512/zuse-s-z3-square-root-algorithm)*. » [Konrad Zuse](Konrad_Zuse "Konrad Zuse")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [RKISS copyright?](http://www.talkchess.com/forum/viewtopic.php?t=38313) by Giorgio Medeot, [CCC](CCC "CCC"), March 07, 2011

**[Up one Level](Algorithms "Algorithms")**







 
