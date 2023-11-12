---
title: Linked List
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* Linked List**


**Linked List**,  

a data structure to [collect](https://en.wikipedia.org/wiki/Collection_%28abstract_data_type%29) data entities in [sequential](https://en.wikipedia.org/wiki/Sequence) order. Unlike an [array](Array "Array") or vector, where consecutive nodes or elements remain in sequential order in [memory](Memory "Memory") for sequential as well as random access, each node of a linked list is composed of a datum and one or more explicit links, a [pointer](https://en.wikipedia.org/wiki/Pointer_%28computer_programming%29), [reference](https://en.wikipedia.org/wiki/Reference_%28computer_science%29) or index to the next and/or previous node of the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence, without copying other nodes around but only to update some references. The ratio of the pure data size to the complete size of a node with its references is somehow a measure of the lists data efficiency. In choosing data structures like arrays versus linked lists, one has to consider [time complexity](https://en.wikipedia.org/wiki/Time_complexity) issues in traversing and maintaining the collection, that is in [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation) constant O(1) versus linear O(n). 



### Iteration


[Iteration](Iteration "Iteration") is the act of repeating instructions inside an [algorithm](Algorithms "Algorithms") with associated [data](Data "Data"), for instance all elements of a linked list.




```C++

TNode* pNode = m_pHead;
while ( pNode ) {
   doSomething( pNode );
   pNode = pNode->pNext;
}

```

### Lookup


To find a particular node requires traversal, that is iteration, starting from the head of the list. Since some actions require modifications on the previous node, not only the found node if any is returned, but also the pointer to the previous node if any.




```C++

TNode* TList::findNode(Property property, TNode **ppPrevious) {
  TNode* pNode = m_pHead;
  *ppPrevious = NULL
  while ( pNode ) {
    if ( pNode->hasProperty(property) )
       return pNode;
    *ppPrevious = pNode;
    pNode = pNode->pNext;
  }
  return NULL; /* not found */
}

```

### Insertion


To insert behind a found node requires modification of two references. The found node need to refer the new node, and the new node to refer the node which was previously the next node of the found node. If no node is found, the new node is appended at the end of the list. If the list is empty, the head is set accordantly, with the new node's next referring nil.




```C++

TNode* TList::insertBehind(TNode *pNewNode, Property property) {
  TNode* pPrevious;
  TNode* pNode = findNode(property, &pPrevious);
  if ( pNode ) {
    pNewNode->pNext = pNode->pNext;
    pNode->pNext = pNewNode;
  } else if ( pPrevious ) {
    pNewNode->pNext  = NULL;
    pPrevious->pNext = pNewNode;
  } else {
    pNewNode->pNext = NULL;
    m_pHead = pNewNode;
  }
  return pNewNode;
}

```

[ <a id="cite-note-2" href="#cite-ref-2">[2]</a>
### Removal


The removal of a node requires to refer the previous node no longer to the found node to be removed, but to its next node. In case the found node is the first one, the head reference is modified to skip that node as well.




```C++

TNode* TList::remove(Property property) {
  TNode* pPrevious;
  TNode* pNode = findNode(property, &pPrevious);
  if ( pNode ) {
    if ( pPrevious ) {
      pPrevious->pNext = pNode->pNext;
    } else {
      m_pHead = pNode->pNext;
    }
  }
  return pNode; /* if NULL, nothing was removed */
}

```

[ <a id="cite-note-3" href="#cite-ref-3">[3]</a>
### Keeping a Tail


As demonstrated above, appending nodes at the end of the forward list has a [asymptotic computational complexity](https://en.wikipedia.org/wiki/Asymptotic_computational_complexity) of O(n), because one has to traverse the entire list from its head. Therefor to speed up appending, some implementations keep not only the head as reference the first element of the list, but also a reference to the last element, dubbed tail. In an video interview, [Anders Hejlsberg](https://en.wikipedia.org/wiki/Anders_Hejlsberg) elaborates on the question on his favorite data structure. Instead of a singly linked list with a head, he preferred a circularly linked list with a tail pointer only, to avoid traversal of the complete lists in order to append at the end, and to use tail->next to point to the head.



 [](C_sharp#References "C sharp#References") 
[Anders Hejlsberg](https://en.wikipedia.org/wiki/Anders_Hejlsberg) on his favorite data structure <a id="cite-note-4" href="#cite-ref-4">[4]</a>




## Doubly Linked List


[ <a id="cite-note-5" href="#cite-ref-5">[5]</a>
A doubly linked list allows efficient list traversal in forward and backward direction, and therefor each node requires one forward and backward reference to both next and previous node with little bit more effort to insert and remove nodes.



## Linked Lists in Programming Languages


Programming languages such as the [functional](https://en.wikipedia.org/wiki/Functional_programming) [Lisp](index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)") and [Scheme](index.php?title=Scheme&action=edit&redlink=1 "Scheme (page does not exist)") have singly linked lists built in along with [cons](https://en.wikipedia.org/wiki/Cons). In fact, Lisp derives from "LISt Processing". [Imperative](https://en.wikipedia.org/wiki/Imperative_programming), [object oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) programming languages such as [C++](Cpp "Cpp") or [Java](Java "Java") or their libraries provide [abstract](https://en.wikipedia.org/wiki/Container_%28abstract_data_type%29) or [generic](Generic_Programming "Generic Programming") container with an [interface](https://en.wikipedia.org/wiki/Protocol_%28object-oriented_programming%29) to [iterate](Iteration "Iteration") the elements of the container in sequential fashion. For instance [C++](Cpp "Cpp") std::forward\_list <a id="cite-note-6" href="#cite-ref-6">[6]</a> with an iterator in a for-loop:




```C++

  std::forward_list<TSquare> knightTargetsd4 = {e6,f5,f3,e2,c2,b3,b5,c6};

  std::cout << "knight on d4 attacks:";
  for ( auto it = mylist.begin(); it != mylist.end(); ++it )
    std::cout << " " << *it;
  std::cout << std::endl;

```

or, alternatively with modifying or non-modifying sequence operation <a id="cite-note-7" href="#cite-ref-7">[7]</a> :




```C++

  std::forward_list<TSquare> knightTargetsd4 = {e6,f5,f3,e2,c2,b3,b5,c6};
  std::cout << "knight on d4 attacks:";
  for_each (knightTargetsd4.begin(), knightTargetsd4.end(), print);
  std::cout << std::endl;

```

## Lists in Computer Chess


In chess programming lists are applied with [squares](Squares "Squares"), [pieces](Pieces "Pieces") and [moves](Moves "Moves"), most often used within the [search](Search "Search") algorithm, implemented as pre-allocated arrays on the [heap](https://en.wikipedia.org/wiki/Memory_pool), [stack](Stack "Stack") or as static list in the [data](https://en.wikipedia.org/wiki/Data_segment) or [bss](https://en.wikipedia.org/wiki/.bss) segment. Typical examples are [piece-](Piece-Lists "Piece-Lists") and [move-lists](Move_List "Move List") inside the search, or move-lists inside a [game record](Chess_Game "Chess Game"). A [bitboard](Bitboards "Bitboards") is a kind of [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_%28object-oriented_programming%29) of a list of squares through an iterator interface, and requires [serialization](Bitboard_Serialization "Bitboard Serialization") to produce an explicit list.


Linked lists have applications in piece-lists, where due to [captures](Captures "Captures") pieces are removed in [make move](Make_Move "Make Move"), and re-inserted in [unmake move](Unmake_Move "Unmake Move"), where modifying references is versatile rather than copying elements of an array around, or to tag pieces as removed, and to traverse always 16 elements rather than a few in the late [endgame](Endgame "Endgame") with most pieces captured. A sample declaration and code was given by [Daniel Shawul](Daniel_Shawul "Daniel Shawul") in [CCC](CCC "CCC") <a id="cite-note-8" href="#cite-ref-8">[8]</a>. A special form of a linked list is the conditional [skip list](https://en.wikipedia.org/wiki/Skip_list), as proposed in [table-driven move generation](Table-driven_Move_Generation "Table-driven Move Generation").



## See also


* [Array](Array "Array")
* [De Bruijn Sequence](De_Bruijn_Sequence "De Bruijn Sequence")
* [Iteration](Iteration "Iteration")
* [Move List](Move_List "Move List")
* [Piece-Lists](Piece-Lists "Piece-Lists")
* [Priority Queue](index.php?title=Priority_Queue&action=edit&redlink=1 "Priority Queue (page does not exist)")
* [Queue](Queue "Queue") (FIFO)
* [Stack](Stack "Stack") (LIFO)
* [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation")


## External Links


* [List (abstract data type) from Wikipedia](https://en.wikipedia.org/wiki/List_%28abstract_data_type%29)
* [Linked data structure from Wikipedia](https://en.wikipedia.org/wiki/Linked_data_structure)
* [Linked list from Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
* [Doubly linked list from Wikipedia](https://en.wikipedia.org/wiki/Doubly_linked_list)
* [Dancing Links from Wikipedia](https://en.wikipedia.org/wiki/Dancing_Links)
* [Self-organizing list from Wikipedia](https://en.wikipedia.org/wiki/Self-organizing_list)
* [Skip list from Wikipedia](https://en.wikipedia.org/wiki/Skip_list)
* [Unrolled linked listfrom Wikipedia](https://en.wikipedia.org/wiki/Unrolled_linked_list)
* [VList from Wikipedia](https://en.wikipedia.org/wiki/VList)
* [XOR linked list from Wikipedia](https://en.wikipedia.org/wiki/XOR_linked_list)


### [C++](Cpp "Cpp")


* [forward\_list - C++ Reference](http://www.cplusplus.com/reference/stl/forward_list/)
* [list - C++ Reference](http://www.cplusplus.com/reference/stl/list/)
* [Boost | Non-standard containers - 1.51.0 | slist](http://www.boost.org/doc/libs/1_51_0/doc/html/container/non_standard_containers.html#container.non_standard_containers.slist)
* [QList | Documentation | Qt Developer Network](http://qt-project.org/doc/qt-4.8/qlist.html)
* [QLinkedList | Documentation | Qt Developer Network](http://qt-project.org/doc/qt-4.8/qlinkedlist.html)
* [CList Class (MFC)](http://msdn.microsoft.com/de-de/library/bxde0zae%28v=vs.80%29.aspx)
* [A Beginner's Guide to the Linked List - CodeProject](http://www.codeproject.com/Articles/662/A-Beginner-s-Guide-to-the-Linked-List)


### [Java](Java "Java")


* [LinkedList (Java Platform SE 6)](http://docs.oracle.com/javase/6/docs/api/java/util/LinkedList.html)


### [Lisp](index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)")


* [Common Lisp the Language, 2nd Edition | 15 Lists](http://www.cs.cmu.edu/Groups/AI/html/cltl/clm/node147.html) by [Guy L. Steele Jr.](Mathematician#GSteele "Mathematician"), 1989
* [Lisp Lists - Programming in Emacs Lisp](http://www.gnu.org/software/emacs/emacs-lisp-intro/html_node/Lisp-Lists.html)


### [Perl](index.php?title=Perl&action=edit&redlink=1 "Perl (page does not exist)")


* [PERL -- Array and List Functions](http://www.cs.cmu.edu/afs/cs/usr/rgs/mosaic/pl-exp-arr.html)
* [Perl Lists](http://www.misc-perl-info.com/perl-lists.html)
* [List::Util - perldoc.perl.org](http://perldoc.perl.org/List/Util.html)


### [Python](Python "Python")


* [5. Data Structures — Python v2.7.3 documentation](http://docs.python.org/tutorial/datastructures.html)
* [An Introduction to Python Lists](http://effbot.org/zone/python-list.htm) by Fredrik Lundh | August 2006
* [Python - List Data Types](http://www.tutorialspoint.com/python/python_lists.htm)
* [Python Lists | Computer Science | Khan Academy](http://www.khanacademy.org/science/computer-science/v/python-lists)
* [Dive Into Python | 3.2. Introducing Lists](http://www.diveintopython.net/native_data_types/lists.html)


### [Ruby](index.php?title=Ruby&action=edit&redlink=1 "Ruby (page does not exist)")


* [angref.org - ruby - Lists](http://langref.org/ruby/lists)


### [TCL](index.php?title=TCL-TK&action=edit&redlink=1 "TCL-TK (page does not exist)")


* [Tcl Data Structures 101 - The list](http://www.tcl.tk/man/tcl/tutorial/Tcl14.html)
* [Tcl Reference Manual](http://tmml.sourceforge.net/doc/tcl/)


### .NET


* [List(T) Class (System.Collections.Generic)](http://msdn.microsoft.com/en-us/library/6sh2ey19.aspx) [MSDN Library](https://en.wikipedia.org/wiki/MSDN_Library)
* [C# List Examples](http://www.dotnetperls.com/list)


### Misc


* [Kraan](Category:Kraan "Category:Kraan") - Head, 1972, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A linked list whose nodes contain two fields: an integer value and a link to the next node. The last node is linked to a terminator used to signify the end of the list, Diagram of a singly linked list made in [Inkscape](https://en.wikipedia.org/wiki/Inkscape), [Linked list from Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Diagram of inserting a node into a singly linked list, for [linked list](https://en.wikipedia.org/wiki/Linked_list) article. Made and granted into the public domain by [Derrick Coetzee](https://en.wikipedia.org/wiki/User:Dcoetzee) in [Adobe Photoshop](https://en.wikipedia.org/wiki/Adobe_Photoshop) and [Illustrator](https://en.wikipedia.org/wiki/Adobe_Illustrator), April 24, 2011, [Linked list from Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Diagram of deleting a node from a singly linked list, for [linked list](https://en.wikipedia.org/wiki/Linked_list) article. Created and released into the public domain by [Derrick Coetzee](https://en.wikipedia.org/wiki/User:Dcoetzee) in [Adobe Photoshop](https://en.wikipedia.org/wiki/Adobe_Photoshop) and [Illustrator](https://en.wikipedia.org/wiki/Adobe_Illustrator), April 24, 2011, [Linked list from Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
 4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> image from [Behind the Code](C_sharp#References "C sharp") with [Anders Hejlsberg](https://en.wikipedia.org/wiki/Anders_Hejlsberg), from 0:50:52, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video 
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Diagram of a doubly linked list made in [Inkscape](https://en.wikipedia.org/wiki/Inkscape), [Linked list from Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [forward\_list::begin - C++ Reference](http://www.cplusplus.com/reference/stl/forward_list/begin/)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [STL Algorithms - C++ Reference](http://www.cplusplus.com/reference/algorithm/)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: Is there such a thing as branchless move generation?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=468678&t=43971) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 10, 2012

**[Up one Level](Data "Data")**







 
