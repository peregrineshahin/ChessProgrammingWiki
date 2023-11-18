---
title: Array
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * Array**

\[ [ENIAC](https://en.wikipedia.org/wiki/ENIAC) [vacuum tube](https://en.wikipedia.org/wiki/Vacuum_tube) array <a id="cite-note-1" href="#cite-ref-1">[1]</a>
An **Array** is a [linear data structure](https://en.wikipedia/.org/wiki/List_of_data_structures#Linear_data_structures) to [collect](https://en.wikipedia.org/wiki/Collection_%28computing%29) data elements or entities by [random access](https://en.wikipedia.org/wiki/Random_access), which also includes [sequential access](https://en.wikipedia.org/wiki/Sequential_access). The [address](https://en.wikipedia.org/wiki/Memory_address) of each array element can be identified by one or more integer indices. Array structures are the computer analog of the mathematical concepts of [vector](https://en.wikipedia.org/wiki/Vector_space) and [matrix](https://en.wikipedia.org/wiki/Matrix_%28mathematics%29).

Therefore, an [one-dimensional](https://en.wikipedia.org/wiki/Dimension) array is often synonymously called vector, either in the context of a [vector processors](https://en.wikipedia.org/wiki/Vector_processor) and [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instruction sets, operating on multiple data, or as [vector container](https://en.wikipedia.org/wiki/Vector_%28C%2B%2B%29), for instance as [class template](https://en.wikipedia.org/wiki/Template_%28programming%29#Class_templates) in the [C++](Cpp "Cpp") [Standard Template Library](https://en.wikipedia.org/wiki/Standard_Template_Library), which works like a dynamic array.

## One-Dimensional Array

A one-dimensional or linear Array contains n elements indexed by one integer. Each element has the same size. Arrays exploit the addressing machinery of computers, whose [random-access memory](Memory#RAM "Memory") is treated as one-dimensional array of [bytes](Byte "Byte") or [words](Word "Word"), and indices are their addresses. One-dimensional arrays are therefore very efficient, and used to implement many other data structures, such as multidimensional arrays, [linked lists](Linked_List "Linked List"), [queues](Queue "Queue"), [stacks](Stack "Stack"), [hash tables](Hash_Table "Hash Table"), [trees](Search_Tree "Search Tree") and [strings](https://en.wikipedia.org/wiki/String_%28computer_science%29).

[](http://net.pku.edu.cn/%7Ecourse/cs201/2003/mirrorWebster.cs.ucr.edu/Page_AoAWin/HTML/Arrays.html)
Array in [memory](Memory "Memory") <a id="cite-note-2" href="#cite-ref-2">[2]</a>

## Multidimensional Array

## Homogeneous

A homogeneous two- or multidimensional array may be interpreted as array of commensurate, embedded arrays, typically associated with the [array data structure](https://en.wikipedia.org/wiki/Array_data_structure). A one-dimensional address calculation from an index tuple is a simple, multiplicative formula.

```C++

int zobristKeys[12][64];
zobristKey[piece][square]

```

With following one-dimensional translation:

```C++

int zobristKeys[12*64];
zobristKey[piece*64 + square]

```

Often, those index translations are already done by the (chess) programmer, i.e. a classical [8x8 board](8x8_Board "8x8 Board") is most often treated as one-dimensional array indexed by square rather than a two-dimensional array indexed by a tuple of [file](Files "Files") and [rank](Ranks "Ranks").

[](http://net.pku.edu.cn/%7Ecourse/cs201/2003/mirrorWebster.cs.ucr.edu/Page_AoAWin/HTML/Arraysa2.html)
Multidimensional Array <a id="cite-note-3" href="#cite-ref-3">[3]</a>

## Array of Arrays

If sub-arrays of a multidimensional array have different sizes, they are allocated elsewhere and referred by a pointer or reference. In [Java](Java "Java"), multidimensional arrays are treated that way implicitly as [array data type](https://en.wikipedia.org/wiki/Array_data_type), in [C](C "C") and [C++](Cpp "Cpp") they need to be implemented explicitly. Due to the additional indirection(s), the access is slightly slower.

Arrays of different sized sub-arrays are f. i. used in [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards") to safe memory for "denser" squares. A [triangular PV-table](Triangular_PV-Table "Triangular PV-Table") is often implemented as a one-dimensional array either with accordant index calculation, or wasting some space for commensurate, maximum sized sub-arrays for each [PV](index.php?title=Principal_variation&action=edit&redlink=1 "Principal variation (page does not exist)").

\[
Array of Arrays <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## Fixed Sized Arrays

An Array whose size is already determined at [compile time](https://en.wikipedia.org/wiki/Compile_time) is [allocated statically](https://en.wikipedia.org/wiki/Static_memory_allocation) if either declared as fixed sized [global](https://en.wikipedia.org/wiki/Global_variable) array, or in [C](C "C") equivalently as [static](https://en.wikipedia.org/wiki/Static_variable) array inside the [scope](https://en.wikipedia.org/wiki/Scope_%28programming%29) of a [subroutine](https://en.wikipedia.org/wiki/Subroutine) or [module](https://en.wikipedia.org/wiki/Module_%28programming%29), whose [lifetime](https://en.wikipedia.org/wiki/Object_lifetime) extends across the run of the program. Alternatively, fixed sized arrays may be allocated once from the dynamic [heap](https://en.wikipedia.org/wiki/Dynamic_memory_allocation), or created temporary as [local](https://en.wikipedia.org/wiki/Local_variable) array-variable on the [stack](Stack "Stack") of the processor, valid inside a scope of a routine.

These arrays work most efficiently, since one array access of a word or integer element directly translates into an appropriate machine instruction using a (scaled) [index register](https://en.wikipedia.org/wiki/Index_register) in conjunction with an [immediate address or base register](https://en.wikipedia.org/wiki/Addressing_mode#Base_plus_index) for the [base address](https://en.wikipedia.org/wiki/Base_address) of the array. The danger without any runtime [bounds checking](https://en.wikipedia.org/wiki/Bounds_checking) is that (a probably very rare) index-overflow will either cause the program to crash, or even harder to find, to make the program behave sporadically erroneous. Some programmers, often provide a debug [assertion](https://en.wikipedia.org/wiki/Assertion_%28computing%29) <a id="cite-note-5" href="#cite-ref-5">[5]</a> to check array bounds at runtime in a debug version.

```C++

// assuming signed index
assert (index >= 0 && index < MAX_PLY);
alpha[index] = a;

```

While global and static arrays may be initialized at compile time as well, as often used for [lookup tables](https://en.wikipedia.org/wiki/Lookup_table), arrays located in the [bss-segment](https://en.wikipedia.org/wiki/.bss) or allocated from the heap or stack may require [runtime](https://en.wikipedia.org/wiki/Run_time_%28computing%29) initialization depending on the application.

## Dynamic Arrays

Dynamic arrays can be created at [runtime](https://en.wikipedia.org/wiki/Run_time_%28computing%29) with a size or number of elements actually needed. Once created, they may be treated as static arrays without further bound checking, or they may be [re-allcoated](https://en.wikipedia.org/wiki/Malloc#realloc) to dynamically shrink or grow their size. [Abstract arrays](https://en.wikipedia.org/wiki/Array_data_type#Abstract_arrays) support a random access interface, and may pre-check the index to perform a dynamic re-allocation policy if required.

## On the Heap

Dynamic arrays are usually allocated from the heap, a [dynamic data area](https://en.wikipedia.org/wiki/Dynamic_memory_allocation) supported by the [operating system](https://en.wikipedia.org/wiki/Operating_system) and underlying [BIOS](https://en.wikipedia.org/wiki/BIOS). In [C](C "C"), dynamic arrays can be created by [malloc](https://en.wikipedia.org/wiki/Malloc) (sizeof(type)\*size), in [C++](Cpp "Cpp") by \[new type [size](https://en.wikipedia.org/wiki/New_%28C%2B%2B%29)\]. Memory areas should be explicitly freed if no longer needed, in C++ by \[delete[](https://en.wikipedia.org/wiki/Delete_%28C%2B%2B%29)\]. Various configurable sized [hash tables](Hash_Table "Hash Table") like the [transposition table](Transposition_Table "Transposition Table") are usually allocated from the heap by explicit runtime initialization.

## On the Stack

Some operating systems provide [C](C "C") library calls which allow runtime dynamic allocation from the stack rather than the heap, e. g. in [Unix](Unix "Unix") with *alloca* <a id="cite-note-6" href="#cite-ref-6">[6]</a> and *malloca* <a id="cite-note-7" href="#cite-ref-7">[7]</a> for [Windows](Windows "Windows"). Further, [C99](https://en.wikipedia.org/wiki/C99) supports [variable-length arrays](https://en.wikipedia.org/wiki/Variable-length_array) (VLA). Like other automatic variables or fixed sized arrays on the stack, this memory is freed automatically after leaving the scope of the routine.

## Array Samples

Definitions and usage in various [programming languages](Languages "Languages"):

## [Assembly](Assembly "Assembly")

```C++

 board db 64 dup (?)
 square dd

 mov ebx, [square]
 mov al, [board+ebx]

```

## [C](C "C") / [C++](Cpp "Cpp")

Note that in C and C++, pointer may be treated as array.

```C++

 static const int magicTable[64] = {
   0, 1,48, 2,57,49,28, 3,
  61,58,50,42,38,29,17, 4,
  62,55,59,36,53,51,43,22,
  45,39,33,30,24,18,12, 5,
  63,47,56,27,60,41,37,16,
  54,35,52,21,44,32,23,11,
  46,26,40,15,34,20,31,10,
  25,14,19, 9,13, 8, 7, 6,
 };

 int board[64];
 int distance[64][64];
 int zobristKeys[12][64];
 int* pBoard = malloc(sizeof(int) * 64);

 int* pboard = new int[64];
 for (int sq = 0; sq < 64; ++sq)
    pboard[sq] = board[sq]; // in C/C++ identical to *(pboard + sq) = board[sq];
 ...
 delete[] pboard;

```

## [Java](Java "Java")

```C++

 static private final int[] magicTable = {
   0, 1,48, 2,57,49,28, 3,
  61,58,50,42,38,29,17, 4,
  62,55,59,36,53,51,43,22,
  45,39,33,30,24,18,12, 5,
  63,47,56,27,60,41,37,16,
  54,35,52,21,44,32,23,11,
  46,26,40,15,34,20,31,10,
  25,14,19, 9,13, 8, 7, 6,
 };
 
 int[] board = new int[64];

```

## Arrays inside a Chess Program

## Lookup Tables

[Lookup tables](https://en.wikipedia.org/wiki/Lookup_table) are arrays containing pre-calculated values. They are indexed by or related to:

### [Square](Squares "Squares")

- [Center Distance](Center_Distance "Center Distance")
- [Center Manhattan-Distance](Center_Manhattan-Distance "Center Manhattan-Distance")
- [BitScan by De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan")

### Two [Squares](Squares "Squares")

- [Distance](Distance "Distance")
- [Direction](Direction "Direction")
- [Legality Test](Square_Attacked_By#LegalityTest "Square Attacked By")
- [Manhattan-Distance](Manhattan-Distance "Manhattan-Distance")

### [Square](Squares "Squares") and [Occupancies](Occupancy "Occupancy")

- [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")

### [Square](Squares "Squares") and [Piece](Pieces "Pieces")

- [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")

### [Material](Material "Material")

- [Material Tables](Material_Tables "Material Tables")

## Read/Write

Those are indexed by or related to:

### [Square](Squares "Squares")

- [Mailbox](Mailbox "Mailbox")

[8x8 Board](8x8_Board "8x8 Board")
[10x12 Board](10x12_Board "10x12 Board")
[Vector Attacks](Vector_Attacks "Vector Attacks")
[0x88](0x88 "0x88")

- [Array of Nibbles](Nibble#ArrayOfNibbles "Nibble")

### Two [Squares](Squares "Squares")

- [Butterfly Boards](Butterfly_Boards "Butterfly Boards") (also by piece, square)

### [Ply](Ply "Ply")

- [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table")
- [Move List](Move_List "Move List")
- [Nodes](Node "Node") or [state variables](https://en.wikipedia.org/wiki/State_variable) of a [depth-first](Depth-First "Depth-First") [search](Search "Search")

### [Pieces](Pieces "Pieces")

- [Piece-Lists](Piece-Lists "Piece-Lists")
- [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition")

### Hash key

- [Transposition Table](Transposition_Table "Transposition Table")

## See also

- [Array of Nibbles](Nibble#ArrayOfNibbles "Nibble")
- [Hash Table](Hash_Table "Hash Table")
- [Initial Position](Initial_Position "Initial Position") (also dubbed array)
- [Iteration](Iteration "Iteration")
- [Linked List](Linked_List "Linked List")
- [Memory](Memory "Memory")
- [Queue](Queue "Queue")
- [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
- [Stack](Stack "Stack")

## Publications

- [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227, [Chapter 3: Board Games](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p003.htm)
- [Gerard Zieliński](Gerard_Zieli%C5%84ski "Gerard Zieliński") (**1976**). *[Arrays for Programming Chess](http://www.emeraldinsight.com/doi/abs/10.1108/eb005412)*. [Kybernetes](http://www.emeraldinsight.com/loi/k), Vol. 5, No. 2
- [Hsiang-Tsung Kung](Mathematician#Kung "Mathematician"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") (**1979**). *[Systolic arrays (for VLSI)](https://apps.dtic.mil/docs/citations/ADA066060)*. [Sparse Matrix Proceedings](https://searchworks.stanford.edu/view/786087) 1978 <a id="cite-note-8" href="#cite-ref-8">[8]</a>
- [Alan H. Bond](Alan_H._Bond "Alan H. Bond") (**1987**). *Broadcasting Arrays - A Highly Parallel Computer Architecture Suitable For Easy Fabrication*. [pdf](http://www.exso.com/bc.pdf)

## Forum Posts

- [std::vector\<> considered harmful](http://www.talkchess.com/forum/viewtopic.php?t=53820) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), September 25, 2014 » [Move List](Move_List "Move List"), [C++](Cpp "Cpp")
- [Initializing portions of arrays](http://www.talkchess.com/forum/viewtopic.php?t=55301) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), February 12, 2015
- [Initializing Arrays at compile time with macros... fun!!!](http://www.talkchess.com/forum/viewtopic.php?t=55853) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), April 01, 2015
- [Stockfish and latest +6 ELO patch!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73273) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), March 05, 2020 » [Distance](Distance "Distance"), [Stockfish](Stockfish "Stockfish") <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Removing Large Arrays](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73319) by Deberger, [CCC](CCC "CCC"), March 10, 2020 » [Space-Time Tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff")

## External Links

- [Array from Wikipedia](https://en.wikipedia.org/wiki/Array)
- [Array data structure from Wikipedia](https://en.wikipedia.org/wiki/Array_data_structure)
- [Array data type from Wikipedia](https://en.wikipedia.org/wiki/Array_data_type)
- [Dynamic array from Wikipedia](https://en.wikipedia.org/wiki/Dynamic_array)
- [Lookup table from Wikipedia](https://en.wikipedia.org/wiki/Lookup_table)
- [Bounds checking from Wikipedia](https://en.wikipedia.org/wiki/Bounds_checking)
- [Associative array from Wikipedia](https://en.wikipedia.org/wiki/Associative_array)
- [Vector processor from Wikipedia](https://en.wikipedia.org/wiki/Vector_processor)
- [Global array (GA) from Wikipedia](https://en.wikipedia.org/wiki/Global_array)
- [Collection (computing) from Wikipedia](https://en.wikipedia.org/wiki/Collection_%28computing%29)
- [Data Structures/Arrays from Wikibooks](http://en.wikibooks.org/wiki/Data_Structures/Arrays)
- [Systolic array from Wikipedia](https://en.wikipedia.org/wiki/Systolic_array)

## [Assembly](Assembly "Assembly")

- [Chapter Four Arrays](http://net.pku.edu.cn/%7Ecourse/cs201/2003/mirrorWebster.cs.ucr.edu/Page_AoAWin/HTML/Arrays.html) from [Art of Assembly Language Programming and HLA](http://homepage.mac.com/randyhyde/webster.cs.ucr.edu/index.html) by [Randall Hyde](https://en.wikipedia.org/wiki/Randall_Hyde)
- [Multidimensional Arrays](http://net.pku.edu.cn/%7Ecourse/cs201/2003/mirrorWebster.cs.ucr.edu/Page_AoAWin/HTML/Arraysa2.html) from [Art of Assembly Language Programming and HLA](http://homepage.mac.com/randyhyde/webster.cs.ucr.edu/index.html) by [Randall Hyde](https://en.wikipedia.org/wiki/Randall_Hyde)
- [x86 Assembly Guide](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html)

## [Basic](Basic "Basic")

- [QBasic/Arrays and Types from Wikibooks](http://en.wikibooks.org/wiki/QBasic/Arrays_and_Types)
- [Visual Basic/Arrays from Wikibooks](http://en.wikibooks.org/wiki/Visual_Basic/Arrays)
- [Visual Basic .NET/Arrays from Wikibooks](http://en.wikibooks.org/wiki/Visual_Basic_.NET/Arrays)
- [Arrays in Visual Basic](http://msdn.microsoft.com/en-us/library/wak0wfyt%28v=VS.100%29.aspx) from [MSDN Library](http://msdn.microsoft.com/en-us/library/ms123401.aspx)

## [C](C "C")

- [C Programming/Arrays from Wikibooks](http://en.wikibooks.org/wiki/C_Programming/Arrays)
- [C Programming/Pointers and arrays from Wikibooks](http://en.wikibooks.org/wiki/C_Programming/Pointers_and_arrays)
- [String and Array Utilities](http://www.gnu.org/software/hello/manual/libc/String-and-Array-Utilities.html#String-and-Array-Utilities) - [The GNU C Library](Free_Software_Foundation#GLIBC "Free Software Foundation")

## [C++](Cpp "Cpp")

- [Dynamic Allocation of Arrays](http://www.fredosaurus.com/notes-cpp/newdelete/50dynamalloc.html) from [C++ Notes](http://www.fredosaurus.com/notes-cpp/index.html) by [Fred Swartz](Fred_Swartz "Fred Swartz")
- [Vector (C++) from Wikipedia](https://en.wikipedia.org/wiki/Vector_%28C%2B%2B%29)

## [D](</D_(Programming_Language)> "D (Programming Language)")

- [Arrays - D Programming Language 2.0 - Digital Mars](http://www.digitalmars.com/d/2.0/arrays.html)

## [Java](Java "Java")

- [Arrays (Java 2 Platform SE v1.4.2)](http://download.oracle.com/javase/1.4.2/docs/api/java/util/Arrays.html)
- [Arrays](http://leepoint.net/notes-java/data/arrays/arrays.html) from [Java Programming Notes](http://leepoint.net/notes-java/index.html) by [Fred Swartz](Fred_Swartz "Fred Swartz")
- [Arrays - The Java™ Tutorials > Learning the Java Language > Language Basics](http://download.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html)

## [Lisp](index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)")

- [17. Arrays](http://www.cs.cmu.edu/Groups/AI/html/cltl/clm/node157.html) from [Common Lisp the Language, Second Edition](http://www.cs.cmu.edu/Groups/AI/html/cltl/clm/clm.html) by [Guy L. Steele Jr.](Mathematician#GSteele "Mathematician")

## [Pascal](Pascal "Pascal")

- [Pascal Programming/Arrays from Wikibooks](http://en.wikibooks.org/wiki/Pascal_Programming/Arrays)

## [Perl](index.php?title=Perl&action=edit&redlink=1 "Perl (page does not exist)")

- [Search results for query "Array"](http://perldoc.perl.org/search.html?q=Array) from [perldoc.perl.org](http://perldoc.perl.org/index.html)
- [perllol - Declaration and Access of Arrays of Arrays](http://perldoc.perl.org/perllol.html) from [perldoc.perl.org](http://perldoc.perl.org/index.html)
- [What is the difference between a list and an array?](http://perldoc.perl.org/perlfaq4.html#What-is-the-difference-between-a-list-and-an-array%3F) from [perldoc.perl.org](http://perldoc.perl.org/index.html)

## [Python](Python "Python")

- [8.6. array — Efficient arrays of numeric values](http://docs.python.org/library/array.html) - [Python v2.7 documentation](http://docs.python.org/index.html)

## [Ruby](index.php?title=Ruby&action=edit&redlink=1 "Ruby (page does not exist)")

- [Class: Array](http://ruby-doc.org/core/classes/Array.html) from [Ruby-Doc.org: Documenting the Ruby Language](http://ruby-doc.org/)

## [TCL](index.php?title=Tcl-Tk&action=edit&redlink=1 "Tcl-Tk (page does not exist)")

- [Arrays / Hash Maps](http://wiki.tcl.tk/532)
- [Array Operations](http://philip.greenspun.com/tcl/array-operations.adp) part of [Tcl for Web Nerds](http://philip.greenspun.com/tcl/index.adp) by [Hal Abelson](http://groups.csail.mit.edu/mac/users/hal/hal.html), [Philip Greenspun](http://philip.greenspun.com/), and Lydia Sandon

## .NET

- [Visual Basic .NET/Arrays from Wikibooks](http://en.wikibooks.org/wiki/Visual_Basic_.NET/Arrays)
- [Vector Structure](http://msdn.microsoft.com/en-us/library/system.windows.vector.aspx) from [MSDN Library](http://msdn.microsoft.com/en-us/library/ms123401.aspx)

## Math

- [Costas array - Wikipedia](https://en.wikipedia.org/wiki/Costas_array) by [John P. Costas](Mathematician#JPCostas "Mathematician") and independently by [Edgar Gilbert](Mathematician#EGilbert "Mathematician")

## Misc

- [Ada Programming/Types/array from Wikibooks](http://en.wikibooks.org/wiki/Ada_Programming/Types/array)
- [Haskell/Hierarchical libraries/Arrays from Wikibooks](http://en.wikibooks.org/wiki/Haskell/Hierarchical_libraries/Arrays)
- [MATLAB Programming/Arrays from Wikibooks](http://en.wikibooks.org/wiki/MATLAB_Programming/Arrays)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Computer memory from Wikipedia](https://en.wikipedia.org/wiki/Computer_memory)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chapter Four Arrays](http://net.pku.edu.cn/%7Ecourse/cs201/2003/mirrorWebster.cs.ucr.edu/Page_AoAWin/HTML/Arrays.html) from [Art of Assembly Language Programming and HLA](http://homepage.mac.com/randyhyde/webster.cs.ucr.edu/index.html) by [Randall Hyde](https://en.wikipedia.org/wiki/Randall_Hyde)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Multidimensional Arrays](http://net.pku.edu.cn/%7Ecourse/cs201/2003/mirrorWebster.cs.ucr.edu/Page_AoAWin/HTML/Arraysa2.html) from [Art of Assembly Language Programming and HLA](http://homepage.mac.com/randyhyde/webster.cs.ucr.edu/index.html) by [Randall Hyde](https://en.wikipedia.org/wiki/Randall_Hyde)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Array data type from Wikipedia](https://en.wikipedia.org/wiki/Array_data_type)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [assert.h from Wikipedia](https://en.wikipedia.org/wiki/Assert.h)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [alloca](http://www.freebsd.org/cgi/man.cgi?alloca)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [\_malloca](http://msdn.microsoft.com/en-us/library/5471dc8s.aspx) from [MSDN Library](http://msdn.microsoft.com/en-us/library/ms123401.aspx)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Systolic array from Wikipedia](https://en.wikipedia.org/wiki/Systolic_array)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Use equations for PushAway and PushClose · official-stockfish/Stockfish@5a7b45e · GitHub](https://github.com/official-stockfish/Stockfish/commit/5a7b45eac9dedbf7ebc61d9deb4dd934058d1ca1#diff-4cd6bcdb505b124d7bdc612c4789dc26L57-R59)

**[Up one Level](Data "Data")**

