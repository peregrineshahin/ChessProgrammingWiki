---
title: Cpp
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Languages](Languages "Languages") * C++**

**C++**,

a pragmatical, [object oriented](https://en.wikipedia.org/wiki/Object-oriented_programming), [general-purpose programming language](https://en.wikipedia.org/wiki/General-purpose_programming_language),
initially an extension of [C](C "C") and designed and implemented in 1979 by [Bjarne Stroustrup](Mathematician#Stroustrup "Mathematician") from [Bell Laboratories](Bell_Laboratories "Bell Laboratories").
C++ is pragmatical because one may write in "usual" C-style, using the [C standard library](https://en.wikipedia.org/wiki/C_standard_library) (printf, strcpy, ...), except perhaps using C++ comments and [references](<https://en.wikipedia.org/wiki/Reference_(C%2B%2B)>) up and then (instead of [pointer](<https://en.wikipedia.org/wiki/Pointer_(computer_programming)>)). On the other hand C++ allows to design classes and interfaces (pure virtual classes) in a more object oriented manner. There are lots of free and commercial class libraries for arithmetics, database related stuff, portable and proprietary window management and whatever else.
Many chess engines are written in C++, varying from using pure C-style, up to extensive use of object oriented stuff and templates as well as [C++11](#11) or [C++17](#17) features.

## Contents

- [1 C Extensions](#C_Extensions)
  - [1.1 References](#References)
  - [1.2 Exception Handling](#Exception_Handling)
- [2 Classes](#Classes)
  - [2.1 Data Definition](#Data_Definition)
  - [2.2 Member Functions](#Member_Functions)
  - [2.3 Modifiers](#Modifiers)
  - [2.4 Pointer to Member Functions](#Pointer_to_Member_Functions)
  - [2.5 Inheritance](#Inheritance)
  - [2.6 Function Overloading](#Function_Overloading)
  - [2.7 Operator Overloading](#Operator_Overloading)
  - [2.8 Late Binding](#Late_Binding)
  - [2.9 Abstract Classes](#Abstract_Classes)
  - [2.10 Pure Abstract Classes](#Pure_Abstract_Classes)
  - [2.11 Multiple Inheritance](#Multiple_Inheritance)
- [3 Templates](#Templates)
- [4 Anonymous Functions](#Anonymous_Functions)
- [5 Smart Pointer](#Smart_Pointer)
- [6 Class Design of a Chess Engine](#Class_Design_of_a_Chess_Engine)
- [7 C++ Compiler](#C.2B.2B_Compiler)
- [8 Libraries](#Libraries)
- [9 See also](#See_also)
- [10 C++ Publications](#C.2B.2B_Publications)
  - [10.1 1985 ...](#1985_...)
  - [10.2 1990 ...](#1990_...)
  - [10.3 1995 ...](#1995_...)
  - [10.4 2000 ...](#2000_...)
  - [10.5 2005 ...](#2005_...)
  - [10.6 2010 ...](#2010_...)
- [11 Forum Posts](#Forum_Posts)
  - [11.1 1997 ...](#1997_...)
  - [11.2 2000 ...](#2000_..._2)
  - [11.3 2005 ...](#2005_..._2)
  - [11.4 2010 ...](#2010_..._2)
  - [11.5 2015 ...](#2015_...)
  - [11.6 2020 ...](#2020_...)
- [12 External Links](#External_Links)
- [13 References](#References_2)

## C Extensions

## References

- [Reference (C++) from Wikipedia](https://en.wikipedia.org/wiki/Reference_%28C%2B%2B%29)

## Exception Handling

- [C++ Programming/Exception Handling from Wikibooks](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Exception_Handling)
- [Exceptions - C++ Reference](http://www.cplusplus.com/doc/tutorial/exceptions/)
- [exception - C++ Reference](http://www.cplusplus.com/reference/std/exception/exception/)

## Classes

Classes as declaration for objects are more or less [C-Structures](C#Struct "C"). None static functions may be declared inside the scope of a class. Those functions, called [member functions](https://en.wikipedia.org/wiki/C%2B%2B_classes#Member_functions), have an implicit parameter called "this", a pointer to this structure, allocated either inside the [data segment](https://en.wikipedia.org/wiki/Data_segment) or [bss](https://en.wikipedia.org/wiki/.bss) as [static](https://en.wikipedia.org/wiki/Local_variable#Static_local_variables) or [global](https://en.wikipedia.org/wiki/Global_variable), via "new" (malloc) on the [heap](https://en.wikipedia.org/wiki/Memory_management#HEAP) or as [automatic object](https://en.wikipedia.org/wiki/Automatic_variable) (variable) on the [stack](https://en.wikipedia.org/wiki/Stack-based_memory_allocation).

- [C++ classes from Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B_classes)

## Data Definition

- [Basic declaration and member variables from Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B_classes#Basic_declaration_and_member_variables)

## Member Functions

- [Member functions from Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B_classes#Member_functions)

## Modifiers

- [Access modifiers from Wikipedia](https://en.wikipedia.org/wiki/Access_modifiers)
- [Static (keyword) from Wikipedia](<https://en.wikipedia.org/wiki/Static_(keyword)>)
- [Class variable from Wikipedia](https://en.wikipedia.org/wiki/Class_variable)
- [Static methods from Wikipedia](<https://en.wikipedia.org/wiki/Method_(computer_programming)#Static_methods>)

## Pointer to Member Functions

For instance an [array](Array "Array") of member function pointers of a class *CNode*, which is indexed by arbitrary pieces code - as switch-case replacement via indirect call/jump.
The special atomic [C++ operator](https://en.wikipedia.org/wiki/Operators_in_C_and_C%2B%2B) '->\*' is used to call the indexed member-functions:

```

class CNode {
  U64 AssertAttack (EnumSquare sq) const;
  U64 wPawnAttacks (EnumSquare sq) const;
  U64 bPawnAttacks (EnumSquare sq) const;
  U64 knightAttacks(EnumSquare sq) const;
  U64 kingAttacks  (EnumSquare sq) const;
  U64 bishopAttacks(EnumSquare sq) const;
  U64 rookAttacks  (EnumSquare sq) const;
  U64 queenAttacks (EnumSquare sq) const;
  ...
  typedef U64 (CNode::*AttackPtrType)(EnumSquare sq) const;
  static AttackPtrType m_scPieceAtta[14];
  ...

  U64 getAttack(EnumSquare sq, EnumPiece piece) const {return (this->*m_scPieceAtta[piece])(sq);}
};

CNode::AttackPtrType CNode::m_scPieceAtta[14] =
{
  AssertAttack,
  AssertAttack,
  wPawnAttacks,
  bPawnAttacks ,
  bishopAttacks,
  bishopAttacks,
  knightAttacks,
  knightAttacks,
  rookAttacks,
  rookAttacks,
  kingAttacks,
  kingAttacks,
  queenAttacks,
  queenAttacks
};

```

## Inheritance

- [Inheritance (object-oriented programming) from Wikipedia](https://en.wikipedia.org/wiki/Inheritance_%28object-oriented_programming%29)
- [Inheritance from Wikibooks](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Classes/Inheritance)
- [C++/Classes and Inheritance - Wikiversity](https://en.wikiversity.org/wiki/C%2B%2B/Classes_and_Inheritance)

## Function Overloading

- [Function overloading from Wikipedia](https://en.wikipedia.org/wiki/Function_overloading)

## Operator Overloading

- [Operator overloading from Wikipedia](https://en.wikipedia.org/wiki/Operator_overloading)
- [Operator Overloading from Wikibooks](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Operators/Operator_Overloading)

## Late Binding

- [Late binding from Wikipedia](https://en.wikipedia.org/wiki/Late_binding)
- [Virtual method table from Wikipedia](https://en.wikipedia.org/wiki/Virtual_method_table)
- [Virtual function from Wikipedia](https://en.wikipedia.org/wiki/Virtual_function)

## Abstract Classes

- [Abstract Classes from Wikibooks](http://en.wikibooks.org/wiki/C++_Programming/Classes/Abstract_Classes)

## Pure Abstract Classes

- [Pure Abstract Classes from Wikibooks](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Classes/Abstract_Classes/Pure_Abstract_Classes)

## Multiple Inheritance

- [Multiple inheritance from Wikipedia](https://en.wikipedia.org/wiki/Multiple_inheritance)

## Templates

- [Template (programming) from Wikipedia](https://en.wikipedia.org/wiki/Template_%28programming%29)
- [List of C++ template libraries from Wikipeadia](https://en.wikipedia.org/wiki/List_of_C%2B%2B_template_libraries)
- [Standard Template Library from Wikipedia](https://en.wikipedia.org/wiki/Standard_Template_Library)
- [Loki (C++) from Wikipedia](https://en.wikipedia.org/wiki/Loki_%28C%2B%2B%29) by [Andrei Alexandrescu](Mathematician#AAlexandrescu "Mathematician") as part of his book *[Modern C++ Design](https://en.wikipedia.org/wiki/Modern_C%2B%2B_Design)*.
- [Boost (C++ libraries) from Wikipedia](https://en.wikipedia.org/wiki/Boost_%28C%2B%2B_libraries%29)
- [Templates - C++ Documentation](http://www.cplusplus.com/doc/tutorial/templates/)
- [Metaprogramming in C++](http://wordaligned.org/docs/metaprogramming/metaprogramming_is_your_friend/cpp.html)
- [C++ Programming/Templates from Wikibooks](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Templates)
- [Template Meta-Programming from Wikibooks](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Templates/Template_Meta-Programming)
- [Barton–Nackman trick from Wikipedia](https://en.wikipedia.org/wiki/Barton%E2%80%93Nackman_trick)
- [Curiously recurring template pattern from Wikipedia](https://en.wikipedia.org/wiki/Curiously_recurring_template_pattern)
- [Variadic template from Wikipedia](https://en.wikipedia.org/wiki/Variadic_template)

## Anonymous Functions

- [Anonymous functions (Blocks) from Wikipedia](<https://en.wikipedia.org/wiki/Anonymous_function#Clang_(C,_C++,_Objective-C,_Objective-C++)>)
- [Anonymous functions (Lambda expressions) from Wikipedia](<https://en.wikipedia.org/wiki/Anonymous_function#C++_(since_C++11)>)

## Smart Pointer

- [Smart pointer from Wikipedia](https://en.wikipedia.org/wiki/Smart_pointer)
- [auto_ptr from Wikipedia](https://en.wikipedia.org/wiki/Auto_ptr) (C++11 deprecated)
- [unique_ptr from Wikipedia](https://en.wikipedia.org/wiki/Smart_pointer#unique_ptr)
- [shared_ptr from Wikipedia](https://en.wikipedia.org/wiki/Smart_pointer#shared_ptr_and_weak_ptr)

## Class Design of a Chess Engine

*main article* [Class Design of a Chess Engine](index.php?title=Class_Design_of_a_Chess_Engine&action=edit&redlink=1 "Class Design of a Chess Engine (page does not exist)")

## C++ Compiler

- [List of C/C++ compilers from Wikipeadia](https://en.wikipedia.org/wiki/List_of_compilers#C++_compilers)
- [GCC](Free_Software_Foundation#GCC "Free Software Foundation")
  - [LLVM from Wikipeadia](https://en.wikipedia.org/wiki/LLVM)
  - [Clang from Wikipeadia](https://en.wikipedia.org/wiki/Clang)
- [Intel C++ Compiler from Wikipeadia](https://en.wikipedia.org/wiki/Intel_C%2B%2B_Compiler)
- [Visual C++ from Wikipeadia](https://en.wikipedia.org/wiki/Visual_C%2B%2B)
- [Compiler Explorer](https://godbolt.org/) by [Matt Godbolt](https://github.com/mattgodbolt)

## Libraries

- [Standard Template Library from Wikipeadia](https://en.wikipedia.org/wiki/Standard_Template_Library)
- [STL Containers - C++ Reference](http://www.cplusplus.com/reference/stl/)
- [C++ Libraries — Software Preservation Group](http://www.softwarepreservation.org/projects/c_plus_plus/library), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")

[NIH Class Library — Software Preservation Group](http://www.softwarepreservation.org/projects/c_plus_plus/library/nihcl), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") [[1]](#cite_note-1)

- [Qt (software) from Wikipedia](<https://en.wikipedia.org/wiki/Qt_(software)>)
- [Loki (C++) from Wikipedia](https://en.wikipedia.org/wiki/Loki_%28C%2B%2B%29) by [Andrei Alexandrescu](Mathematician#AAlexandrescu "Mathematician") as part of his book *[Modern C++ Design](https://en.wikipedia.org/wiki/Modern_C%2B%2B_Design)*.
- [BITSCAN](Pablo_San_Segundo#BITSCAN "Pablo San Segundo"), a [C++ library](#Libraries) for bitstrings by [Pablo San Segundo](Pablo_San_Segundo "Pablo San Segundo")
- [Boost (C++ libraries) from Wikipedia](https://en.wikipedia.org/wiki/Boost_%28C%2B%2B_libraries%29)
- [The Better String Library](http://bstring.sourceforge.net/) by [Paul Hsieh](Paul_Hsieh "Paul Hsieh")
- [log4cplus / Wiki / Home](https://sourceforge.net/p/log4cplus/wiki/Home/)
- [Senjo C++ UCI Adapter](https://github.com/zd3nik/SenjoUCIAdapter) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester") » [Clubfoot](Clubfoot "Clubfoot"), [UCI](UCI "UCI")

## See also

- [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator")
- [Generic Programming](Generic_Programming "Generic Programming")
- [SSE2 - SSE2-Wrapper in C++](SSE2#SSE2WrapperinCpp "SSE2")

## C++ Publications

## 1985 ...

- [Bjarne Stroustrup](Mathematician#Stroustrup "Mathematician") (**1985, 1991, 1997, 2000**). *[The C++ Programming Language](https://en.wikipedia.org/wiki/The_C%2B%2B_Programming_Language)*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Keith E. Gorlen](Keith_Gorlen "Keith Gorlen") (**1987**). *An Object-Oriented Class Library for C++ Programs*. [C++ Workshop 1987](https://dblp.uni-trier.de/db/conf/c++/c++87.html)
- [Bjarne Stroustrup](Mathematician#Stroustrup "Mathematician"), [Andrew Koenig](Andrew_Koenig "Andrew Koenig") (**1989**). *C++: as close as possible to C -- but no closer*. [C++ Report](https://en.wikipedia.org/wiki/C%2B%2B_Report), Vol. 1, no. 7

## 1990 ...

- [Andrew Koenig](Andrew_Koenig "Andrew Koenig"), [Bjarne Stroustrup](Mathematician#Stroustrup "Mathematician") (**1990**). *Exception Handling for C++*. Proc [USENIX C++ Conference 1990](http://dblp.dagstuhl.de/db/conf/c++/c++90.html#KoenigS90), Also, [Journal of Object Oriented Programming](https://dl.acm.org/citation.cfm?id=J472), Vol. 3, No. 2
- [Keith E. Gorlen](Keith_Gorlen "Keith Gorlen"), et al. (**1990**). *[Data abstraction and object-oriented programming in C++](https://www.goodreads.com/book/show/3108432-data-abstraction-and-object-oriented-programming-in-c)*. [Wiley](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons) [[2]](#cite_note-2)
- [Andrew Koenig](Andrew_Koenig "Andrew Koenig"), [Thomas A. Cargill](http://www.profcon.com/profcon/cargill/), [Keith E. Gorlen](Keith_Gorlen "Keith Gorlen"), Robert B. Murray, Michael Vilot (**1991**). *[How Useful is Multiple Inheritance in C++?](https://www.semanticscholar.org/paper/How-Useful-is-Multiple-Inheritance-in-C%2B%2B-Koenig-Cargill/3cab41a20400d12ef38e702166961de280441ecf)* [C++ Conference 1991](https://dblp.uni-trier.de/db/conf/c++/c++91.html)
- [Andrew Koenig](Andrew_Koenig "Andrew Koenig") (**1992**). *[Space-Efficient Trees in C++](https://www.semanticscholar.org/paper/Space-Efficient-Trees-in-C%2B%2B-Koenig/ea7fb1268b06304cffb292f1d8f4ace0ff62c82b)*. [C++ Conference 1992](https://dblp.dagstuhl.de/db/conf/c++/c++92.html)
- [Scott Meyers](https://en.wikipedia.org/wiki/Scott_Meyers) (**1992,2005**). *Effective C++: 50 Specific Ways to Improve Your Programs and Designs*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Andrew Koenig](Andrew_Koenig "Andrew Koenig") (**1994**). *Templates and Generic Algorithms*. [Journal of Object-Oriented Programming](https://dblp.org/db/journals/joop/index), Vol. 7 No. 3
- [Andrew Koenig](Andrew_Koenig "Andrew Koenig") (**1994**). *Generic Iterators*. [Journal of Object-Oriented Programming](https://dblp.org/db/journals/joop/index), Vol. 7, No. 5
- [Bjarne Stroustrup](Mathematician#Stroustrup "Mathematician"), [Andrew Koenig](Andrew_Koenig "Andrew Koenig"), [Barbara Moo](http://www.informit.com/authors/bio/764d4f1b-b868-4115-862e-4fe85e69f321) (**1994**). *The C++ Programming Language*. [Encyclopedia of Software Engineering](https://onlinelibrary.wiley.com/doi/book/10.1002/0471028959), [Wiley](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)

## 1995 ...

- [Andrew Koenig](Andrew_Koenig "Andrew Koenig"), [Bjarne Stroustrup](Mathematician#Stroustrup "Mathematician") (**1995**). *[Foundations for Native C++ Styles](https://dl.acm.org/citation.cfm?id=229732)*. [Software Practice and Experience](https://onlinelibrary.wiley.com/loi/1097024x), Vol 25, special issue S4
- [Patrick Winston](Patrick_Winston "Patrick Winston") (**1995**). *[On To C++](http://people.csail.mit.edu/phw/Books/CPPBACK.HTML)*. [Addison Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Greg Wilson](Greg_Wilson "Greg Wilson"), [Paul Lu](Paul_Lu "Paul Lu") (eds.) (**1996**). *[Parallel Programming Using C++](https://mitpress.mit.edu/books/parallel-programming-using-c)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
- [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal") (**1996**). *[Algorithms and Data Structures in C++](http://home.planet.nl/%7Eammeraal/algds.html)*. [John Wiley](<https://en.wikipedia.org/wiki/Wiley_(publisher)>)
- [Andrew Koenig](Andrew_Koenig "Andrew Koenig"), [Barbara Moo](http://www.informit.com/authors/bio/764d4f1b-b868-4115-862e-4fe85e69f321) (**1997**). *[Ruminations on C++](http://www.informit.com/store/accelerated-c-plus-plus-practical-programming-by-example-9780201703535)*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal") (**1997**). *[STL for C++ Programmers](http://home.planet.nl/%7Eammeraal/stlcpp.html)*. ISBN 0-471-97181-2, Chichester: [John Wiley](http://eu.wiley.com/WileyCDA/Section/id-300022.html)

## 2000 ...

- [Andrew Koenig](Andrew_Koenig "Andrew Koenig"), [Barbara Moo](http://www.informit.com/authors/bio/764d4f1b-b868-4115-862e-4fe85e69f321) (**2000**). *[Accelerated C++](http://www.acceleratedcpp.com/index.html)*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal") (**2000**). *[C++ for Programmers](http://home.planet.nl/%7Eammeraal/cppbook.html)*. ISBN 0-471-60697-9, Chichester: [John Wiley](http://eu.wiley.com/WileyCDA/Section/id-300022.html)
- [Bjarne Stroustrup](Mathematician#Stroustrup "Mathematician"), [Andrew Koenig](Andrew_Koenig "Andrew Koenig"), [Barbara Moo](http://www.informit.com/authors/bio/764d4f1b-b868-4115-862e-4fe85e69f321) (**2001**). *The C++ Programming Language*. [Encyclopedia of Software Engineering](http://onlinelibrary.wiley.com/book/10.1002/0471028959). [Wiley](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)
- [Andrei Alexandrescu](Mathematician#AAlexandrescu "Mathematician") (**2001**). *[Modern C++ Design: Generic Programming and Design Patterns Applied](https://en.wikipedia.org/wiki/Modern_C%2B%2B_Design)*.
- [Robert L. Akers](https://dblp.uni-trier.de/pers/hd/a/Akers:Robert_L=.html), [Ira Baxter](Ira_Baxter "Ira Baxter"), [Michael Mehlich](http://www.semdesigns.com/Company/People/mmehlich/index.html) (**2004**). *Invited application paper: re-engineering C++ components via automatic program transformation*. [PEPM 2004](http://www.informatik.uni-trier.de/~ley/db/conf/pepm/pepm2004.html#AkersBM04), [pdf](http://www.semdesigns.com/Company/Publications/component-reengineering-PEPM-2004.pdf)

## 2005 ...

- [Robert L. Akers](https://dblp.uni-trier.de/pers/hd/a/Akers:Robert_L=.html), [Ira Baxter](Ira_Baxter "Ira Baxter"), [Michael Mehlich](http://www.semdesigns.com/Company/People/mmehlich/index.html), [Brian J. Ellis](https://dblp.uni-trier.de/pers/hd/e/Ellis:Brian_J=), [Kenn R. Luecke](https://dblp.uni-trier.de/pers/hd/l/Luecke:Kenn_R=.html) (**2005**). *[Reengineering C++ Component Models via Automatic Program Transformation](http://www.computer.org/csdl/proceedings/wcre/2005/2474/00/24740013-abs.html)*. [WCRE 2005](http://www.informatik.uni-trier.de/~ley/db/conf/wcre/wcre2005.html#AkersBMEL05)
- [Robert L. Akers](https://dblp.uni-trier.de/pers/hd/a/Akers:Robert_L=.html), [Ira Baxter](Ira_Baxter "Ira Baxter"), [Michael Mehlich](http://www.semdesigns.com/Company/People/mmehlich/index.html), [Brian J. Ellis](https://dblp.uni-trier.de/pers/hd/e/Ellis:Brian_J=), [Kenn R. Luecke](https://dblp.uni-trier.de/pers/hd/l/Luecke:Kenn_R=.html) (**2007**). *Case study: Re-engineering C++ component models via automatic program transformation*. [Information & Software Technology, Vol. 49, No. 3](http://www.informatik.uni-trier.de/~ley/db/journals/infsof/infsof49.html#AkersBMEL07)
- [Bjarne Stroustrup](Mathematician#Stroustrup "Mathematician") (**2008, 2014**). *[Programming -- Principles and Practice Using C++](http://www.stroustrup.com/Programming/)*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)

## 2010 ...

- [Robert C. Seacord](https://en.wikipedia.org/wiki/Robert_C._Seacord) (**2010**). *Dangerous Optimizations and the Loss of Causality*. CS 15-392, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [slides as pdf](https://pubweb.eng.utah.edu/~cs5785/slides-f10/Dangerous+Optimizations.pdf)
- [Anthony Williams](https://stackoverflow.com/users/5597/anthony-williams) (**2012**). *[C++ Concurrency in Action: Practical Multithreading](http://www.cplusplusconcurrencyinaction.com/)*. [[3]](#cite_note-3)
- [Xi Wang](https://pdos.csail.mit.edu/~xi/), [Haogang Chen](https://pdos.csail.mit.edu/~hchen/), [Alvin Cheung](https://homes.cs.washington.edu/~akcheung/), [Zhihao Jia](http://zhihaojia.com/), [Nickolai Zeldovich](http://people.csail.mit.edu/nickolai/), [M. Frans Kaashoek](https://pdos.csail.mit.edu/~kaashoek/) (**2012**). *Undefined Behavior: What Happened to My Code*? [pdf](https://pdos.csail.mit.edu/papers/ub:apsys12.pdf) [[4]](#cite_note-4)
- [Will Dietz](https://wdtz.org/), [Peng Li](https://lipeng28.github.io/), [John Regehr](http://www.cs.utah.edu/~regehr/), [Vikram Adve](https://en.wikipedia.org/wiki/Vikram_Adve) (**2012**). *Understanding Integer Overflow in C/C++*. [pdf](http://www.cs.utah.edu/~regehr/papers/overflow12.pdf)

## Forum Posts

## 1997 ...

- [Search Degredation w/ C++](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/5fba0f94be869f35) by Chris Jason Richards, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 12, 1997

[Re: Search Degredation w/ C++](http://groups.google.com/group/rec.games.chess.computer/msg/e27ff5ad3ac054ff) by [Amir Ban](Amir_Ban "Amir Ban"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 17, 1997

- [Question to Amir Ban](https://www.stmintz.com/ccc/index.php?id=11617) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), November 05, 1997 [[5]](#cite_note-5)
- [object oriented chess programming](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/2d300db2c0e1c70e) by [James Long](James_Swafford "James Swafford"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 31, 1997

[Re: object oriented chess programming](http://groups.google.com/group/rec.games.chess.computer/msg/b048a5f34835f721) by [Dave Fotland](David_Fotland "David Fotland"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 06, 1998

- [C or C++ for chess programming: speed](https://www.stmintz.com/ccc/index.php?id=74219) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), October 20, 1999

## 2000 ...

- [C++ Programming Q: are const and define efficiency the same](https://www.stmintz.com/ccc/index.php?id=342885) by [Federico Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](CCC "CCC"), January 16, 2004
- [Kiwi for Win98 and input-reading stuff](https://www.stmintz.com/ccc/index.php?id=389667) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), September 29, 2004 » [Kiwi](Kiwi "Kiwi"), [Windows](Windows "Windows"), [Thread](Thread "Thread")

## 2005 ...

- [Find The Bug - C / C++](http://bytes.com/topic/c/answers/128755-find-bug) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [bytes.com](http://bytes.com/), July 22, 2005 » [Chezzz](Chezzz "Chezzz")
- [forcing compilers to inline (or to not inline)](http://www.talkchess.com/forum/viewtopic.php?t=21007) by [Wylie Garvin](index.php?title=Wylie_Garvin&action=edit&redlink=1 "Wylie Garvin (page does not exist)"), [CCC](CCC "CCC"), May 04, 2008

## 2010 ...

- [c or c++ ?](http://talkchess.com/forum/viewtopic.php?t=39683) by ethan ara, [CCC](CCC "CCC"), July 10, 2011
- [C++ templates question](http://www.talkchess.com/forum/viewtopic.php?t=42046) by [José C. Martínez Galán](index.php?title=Jos%C3%A9_C._Mart%C3%ADnez_Gal%C3%A1n&action=edit&redlink=1 "José C. Martínez Galán (page does not exist)"), [CCC](CCC "CCC"), January 18, 2012
- [C++11 for chess engines](http://www.talkchess.com/forum/viewtopic.php?t=44999) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), September 03, 2012
- [Has GCC caught up with Intel with respect to performance?](http://www.talkchess.com/forum/viewtopic.php?t=45482) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), October 07, 2012
- [Need Help Getting GCC Working?!?](http://www.talkchess.com/forum/viewtopic.php?t=47841) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), April 23, 2013
- \[[ub](http://www.open-std.org/pipermail/ub/2013-May/000005.html) Objectives and tasks for SG12\] by [Gabriel Dos Reis](http://www.cse.tamu.edu/people/faculty/gdr), [Open Standards](http://www.open-std.org/), [The ub Archives](http://www.open-std.org/pipermail/ub/), May 29, 2013
- [C++ Question](http://www.talkchess.com/forum/viewtopic.php?t=48795) by Ted Wong, [CCC](CCC "CCC"), July 30, 2013 » [Thread](Thread "Thread")
- [C++11 threads seem to get shafted for cycles](http://www.open-chess.org/viewtopic.php?f=5&t=2618) by [User923005](Dann_Corbit "Dann Corbit"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 18, 2014 » [Parallel Search](Parallel_Search "Parallel Search"), [Senpai](Senpai "Senpai"), [Thread](Thread "Thread")
- [c++11 std::atomic and memory_order_relaxed](http://www.talkchess.com/forum/viewtopic.php?t=51824) by Kevin Hearn, [CCC](CCC "CCC"), April 01, 2014 » [Memory](Memory "Memory")
- [C++ puzzle](http://www.talkchess.com/forum/viewtopic.php?t=51966) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), April 12, 2014
- [std::vector\<> considered harmful](http://www.talkchess.com/forum/viewtopic.php?t=53820) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), September 25, 2014 » [Move List](Move_List "Move List"), [Array](Array "Array")

## 2015 ...

- [Polling standard input from C++](http://www.talkchess.com/forum/viewtopic.php?t=56303) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 10, 2015
- [BMI2 intrinsics in gcc](http://www.talkchess.com/forum/viewtopic.php?t=63978) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), May 14, 2017 » [BMI2](BMI2 "BMI2")
- [Advantages of C++11 for Chess?](http://www.talkchess.com/forum/viewtopic.php?t=65523) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), October 23, 2017
- [Wouldn't it be nice if C++ GPU](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70584) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), April 25, 2019 » [GPU](GPU "GPU")
- [Re: Pawn move generation in bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72461&start=3) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), December 05, 2019 » [Bitboards](Bitboards "Bitboards")

## 2020 ...

- [C++20 standard bit operations](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75818) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 15, 2020 » [General Setwise Operations](General_Setwise_Operations "General Setwise Operations"), [Population Count](Population_Count "Population Count"), [BitScan](BitScan "BitScan")
- [C++ type system AKA what is exactly int ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76592) by [JohnWoe](Toni_Helminen "Toni Helminen"), [CCC](CCC "CCC"), February 14, 2021
- [C++ code for board[8][8] representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76817) by [Yves De Billoëz](Yves_De_Billo%C3%ABz "Yves De Billoëz"), [CCC](CCC "CCC"), March 08, 2021 » [8x8 Board](8x8_Board "8x8 Board")

[Re: C++ code for board[8][8] representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76817&start=4) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), March 08, 2021 [[6]](#cite_note-6)

- [Why C++ instead of C#?](http://www.talkchess.com/forum3/viewtopic.php?t=78070) by Henk, [CCC](CCC "CCC"), August 31, 2021
- [Bitboards ?: C# vs C++](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78680) by Bill Beame, [CCC](CCC "CCC"), November 17, 2021 » [Bitboards](Bitboards "Bitboards")

## External Links

- [C++ from Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B)
- [C++03 from Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B03)
- [C++11 from Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B11)
- [C++14 from Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B14)
- [C++17 from Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B17)
- [C++20 from Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B20)
- [C++ Programming from Wikibooks](https://en.wikibooks.org/wiki/C%2B%2B_Programming)
- [More C++ Idioms - Wikibooks](https://en.wikibooks.org/wiki/More_C%2B%2B_Idioms)
- [C++ - Wikiversity](https://en.wikiversity.org/wiki/C%2B%2B)
- [C++ reference - cppreference.com](https://en.cppreference.com/w/cpp)
- [cplusplus.com - The C++ Resources Network](http://www.cplusplus.com/)
- [C++ Notes](http://www.fredosaurus.com/notes-cpp/index.html) by [Fred Swartz](Fred_Swartz "Fred Swartz")
- [C++ Historical Sources Archive — Software Preservation Group](http://www.softwarepreservation.org/projects/c_plus_plus/), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Agner Fog's manuals](https://www.agner.org/optimize/#manuals)

[Calling conventions for different C++ compilers and operating systems](https://www.agner.org/optimize/calling_conventions.pdf) (pdf) by [Agner Fog](http://www.agner.org/)

- [C++ Optimization Strategies and Techniques](http://www.tantalon.com/pete/cppopt/main.htm) by [Pete Isensee](http://www.tantalon.com/pete.htm)
- [C++ Frequently Questioned Answers](http://yosefk.com/c++fqa/index.html) by [Yossi Kreinin](http://yosefk.com/about.html)
- [comp.lang.c++](https://groups.google.com/forum/#!forum/comp.lang.c++) The object-oriented C++ language
- [Bjarne Stroustrup](Mathematician#Stroustrup "Mathematician") - The Essence of C++, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. [↑](#cite_ref-1) [Keith E. Gorlen](Keith_Gorlen "Keith Gorlen"), et al. (**1990**). *[Data abstraction and object-oriented programming in C++](https://www.goodreads.com/book/show/3108432-data-abstraction-and-object-oriented-programming-in-c)*. [Wiley](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)
1. [↑](#cite_ref-2) [NIH Class Library — Software Preservation Group](http://www.softwarepreservation.org/projects/c_plus_plus/library/nihcl), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. [↑](#cite_ref-3) [Information on the C++11 Memory Model](http://scottmeyers.blogspot.co.uk/2012/04/information-on-c11-memory-model.html) by [Scott Meyers](https://en.wikipedia.org/wiki/Scott_Meyers), April 24, 2012
1. [↑](#cite_ref-4) [Re: A note for C programmers](http://www.talkchess.com/forum/viewtopic.php?t=50186&start=80) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), November 28, 2013
1. [↑](#cite_ref-5) [Search Degredation w/ C++](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/5fba0f94be869f35) by Chris Jason Richards, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 12, 1997, post 4 and 6 by [Amir Ban](Amir_Ban "Amir Ban")
1. [↑](#cite_ref-6) [lambda expressions (C++ 11) from Wikipedia](<https://en.wikipedia.org/wiki/Anonymous_function#C++_(since_C++11)>)

**[Up one Level](Languages "Languages")**

