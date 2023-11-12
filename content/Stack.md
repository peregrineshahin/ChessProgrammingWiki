---
title: Stack
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* Stack**



[ Stack <a id="cite-note-1" href="#cite-ref-1">[1]</a>
A **Stack** is a [linear data structure](https://en.wikipedia.org/wiki/List_of_data_structures#Linear_data_structures) to [collect](https://en.wikipedia.org/wiki/Collection_%28computing%29) data elements in [last in, first out order](https://en.wikipedia.org/wiki/LIFO_%28computing%29) (LIFO). The only elementary operations are **push** and **pop**. Push adds one element on the top of stack, while pop removes an entry from the top of the stack and returns that element to the caller. Entries are removed from the stack in the reverse order of their additions. In practice, there is often a third operation. **Peek** retrieves the top element without removing the entry from the stack. 


The stack is a natural structure to remember where to continue after some work was interrupted to do some more important tasks, which itself might be interrupted again, even [recursively](Recursion "Recursion") and multiple times. This applies to [depth-first](Depth-First "Depth-First") tree traversals like [minimax search](Minimax "Minimax") or evaluating nested arithmetical [expressions](https://en.wikipedia.org/wiki/Expression_%28programming%29). 



## Hardware Stack


Most [central processing units](https://en.wikipedia.org/wiki/Central_processing_unit) support a hardware stack (processor stack, call stack) as part of the [main memory](Memory "Memory"). Processors have a special register, pointing to the top of stack (stack pointer), and push and pop instructions respectively. [Intel](Intel "Intel") processors from [8080](8080 "8080") until [x86-64](X86-64 "X86-64") let the stack grow from higher to lower addresses via pre-decrement push and post-increment pop.




```C++

push(register) ::= stack[--sp] := register
pop (register) ::= register := stack[sp++]

```

To implement such hardware stacks was motivated by control flow considerations of calling and returning from [subroutines](https://en.wikipedia.org/wiki/Subroutine), possibly recursively as coined by [Algol-like](Algol "Algol") [programming languages](Languages "Languages"). A call instruction pushes the program address of the next instruction on the stack, just before it sets its [instruction pointer register](https://en.wikipedia.org/wiki/Program_counter) to the subroutine-address. After executing the subroutine, a trailing return instruction pops the return address from the stack into the instruction pointer, to continue the execution flow as expected. Additionally, high level procedural programming languages demanded [local variables](https://en.wikipedia.org/wiki/Local_variable). While [actual parameters](https://en.wikipedia.org/wiki/Parameter_%28computer_science%29) were pushed before the call applying certain [calling conventions](https://en.wikipedia.org/wiki/Calling_convention) of various platforms and compiler <a id="cite-note-2" href="#cite-ref-2">[2]</a><a id="cite-note-3" href="#cite-ref-3">[3]</a>, the callee did accordant stack pointer manipulations, to reserve or [allocate](https://en.wikipedia.org/wiki/Stack-based_memory_allocation) a stack frame for local, automatic variables. Intel's 16-bit [8086](8086 "8086") introduced an additional register, intended as base pointer into a possible variable stack frame, and the option of dynamic frame re-allocation. 


A typical 8086 stack frame with [Pascal calling conventions](https://en.wikipedia.org/wiki/X86_calling_conventions#pascal), where the callee is responsible for balancing the stack. Similar stack layout appears in [x86](X86 "X86") with 32-bit extended registers (esp, ebp) and stack entries <a id="cite-note-4" href="#cite-ref-4">[4]</a>.




```C++

push word para1
push word para2
call foo
...

foo proc near
  push  bp
  mov   bp, sp
  sub   sp, 3*2  ; allocate space for three local 16-bit variables
  ...
  mov   sp, bp
  pop   bp
  ret   4        ; return and "pop" additional four bytes of the parameters

```

with following memory layout inside the scope of *foo*:




```C++

stack growth
^   <---- 16 bit ---->
|  +------------------+            +------+
   | local variable 3 | [bp-6] <---|  SP  |
   +------------------+            +------+
   | local variable 2 | [bp-4]
   +------------------+
   | local variable 1 | [bp-2] 
   +------------------+            +------+
   | saved bp         | <----------|  BP  |
   +------------------+            +------+
   | return address   |
   +------------------+
   | parameter  2     | [bp+4]
   +------------------+
   | parameter  1     | [bp+6]
|  +------------------+
v
higher addresses

```

## Applications


### Stack Calculator


The [Reverse Polish](https://en.wikipedia.org/wiki/Reverse_Polish_notation) or Postfix notation scheme as proposed in 1954 by [Burks](Mathematician#Burks "Mathematician"), Warren, and Wright <a id="cite-note-5" href="#cite-ref-5">[5]</a> , was independently reinvented by [Friedrich L. Bauer](Mathematician#Bauer "Mathematician"), [Klaus Samelson](Mathematician#Samelson "Mathematician") <a id="cite-note-6" href="#cite-ref-6">[6]</a> and [Edsger W. Dijkstra](Mathematician#EWDijkstra "Mathematician") in the early 1960s to coin and utilize the [stack data structure](https://en.wikipedia.org/wiki/Stack_%28data_structure%29) to efficiently evaluate [expressions](https://en.wikipedia.org/wiki/Expression_%28programming%29), likely after [parsing](https://en.wikipedia.org/wiki/Parsing) [infix notation](Recursion#InfixExpression "Recursion") [recursively](Recursion "Recursion"), which is actually a [depth-first](Depth-First "Depth-First") traversal of a expression tree.


**Infix**:




```C++

(1 + 2)*(3 + 4)

```

**Infix Tree**:




```C++

       *
   +       +
 1   2   3   4

```

**Postfix Stack**:




```C++

 push 1
 push 2
 add
 push 3
 push 4
 add
 mul

```

Many todays compiler and interpreter work that way, so does the [Java Virtual Machine](https://en.wikipedia.org/wiki/Java_Virtual_Machine). [Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) is further utilized in the [Forth](Forth "Forth") [Stack-oriented programming language](https://en.wikipedia.org/wiki/Stack-oriented_programming_language).




### Depth-First Search


In computer game programming, a stack of [nodes](Node "Node") is also the appropriate data structure in [depth-first tree search](Depth-First "Depth-First"), like [Minimax](Minimax "Minimax") or [Alpha-beta](Alpha-Beta "Alpha-Beta"). Immediately before a [move is made](Make_Move "Make Move") to search further, the node is pushed on the stack - and popped back while [unmaking](Unmake_Move "Unmake Move"). Despite global state variables like a [board representation](Board_Representation "Board Representation"), which are [updated incrementally](Incremental_Updates "Incremental Updates"), programs implicitly use the processor stack by passing parameters to a [recursive](Recursion "Recursion") search routine with local variables. A software stack is obligatory for an [iterative search](Iterative_Search "Iterative Search"), and likely implemented as [array](Array "Array") indexed by [ply](Ply "Ply").



## See also


* [Array](Array "Array")
* [Forth](Forth "Forth")
* [Linked List](Linked_List "Linked List")
* [Linked List on the Stack](Triangular_PV-Table#LinkedListontheStack "Triangular PV-Table") from [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table")
* [PV-List on the Stack](Principal_Variation#PVListontheStack "Principal Variation") from [Principal variation](index.php?title=Principal_variation&action=edit&redlink=1 "Principal variation (page does not exist)")
* [Queue](Queue "Queue")


## Publications


* [Arthur W. Burks](Mathematician#Burks "Mathematician"), Don W. Warren, [Jesse B. Wright](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/w/Wright:Jesse_B=.html) (**1954**) *[An Analysis of a Logical Machine Using Parenthesis-Free Notation](http://www.jstor.org/pss/2001990)*.
* [Klaus Samelson](Mathematician#Samelson "Mathematician"), [Friedrich L. Bauer](Mathematician#Bauer "Mathematician") (**1960**). *[Sequential Formula Translation](http://portal.acm.org/citation.cfm?id=366968)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 3 No. 2
* [Craig A. Finseth](http://www.finseth.com/parts/index.php) (**1980**). *[Something is Missing (Implementing recursion and stacks in BASIC)](http://www.atariarchives.org/bcc3/showpage.php?page=45)*. [The Best of Creative Computing Volume 3](Creative_Computing#Best3 "Creative Computing") » [Basic](Basic "Basic")
* [Donald Knuth](Donald_Knuth "Donald Knuth") (**1997**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html)*, Volume 1: Fundamental Algorithms (Third Edition), Addison-Wesley, ISBN 0-201-89683-4, 2.2.1: Stacks, Queues, and Deques
* [Thomas H. Cormen](Mathematician#THCormen "Mathematician"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Ronald L. Rivest](Ronald_L._Rivest "Ronald L. Rivest"), [Clifford Stein](Mathematician#CliffordStein "Mathematician") (**2009**).*[Introduction to Algorithms, 3rd Edition](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)*


## Forum Posts


* [LIFO stack based parallel processing?](http://www.talkchess.com/forum/viewtopic.php?t=40493) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), September 22, 2011


## External Links


* [Stack from Wikipedia](https://en.wikipedia.org/wiki/Stack)
* [Stack (abstract data type) from Wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
* [Call stack from Wikipedia](https://en.wikipedia.org/wiki/Call_stack)
* [stack](http://xlinux.nist.gov/dads//HTML/stack.html) from [Dictionary of Algorithms and Data Structures](http://xlinux.nist.gov/dads/) by [Paul E. Black](http://hissa.nist.gov/~black/), [National Institute of Standards and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)
* [LIFO (computing) from Wikipedia](https://en.wikipedia.org/wiki/LIFO_%28computing%29)
* [Call stack from Wikipedia](https://en.wikipedia.org/wiki/Call_stack)
* [Stack overflow from Wikipedia](https://en.wikipedia.org/wiki/Stack_overflow)
* [Stack-based memory allocation from Wikipedia](https://en.wikipedia.org/wiki/Stack-based_memory_allocation)
* [Stack machine from Wikipedia](https://en.wikipedia.org/wiki/Stack_machine)
* [Stack-oriented programming language from Wikipedia](https://en.wikipedia.org/wiki/Stack-based_language)


### [x86](X86 "X86")


* [x86 Disassembly/The Stack from Wikibooks](http://en.wikibooks.org/wiki/X86_Disassembly/The_Stack)
* [x86 Disassembly/Functions and Stack Frames from Wikibooks](http://en.wikibooks.org/wiki/X86_Disassembly/Functions_and_Stack_Frames)
* [Where the top of the stack is on x86](http://eli.thegreenplace.net/2011/02/04/where-the-top-of-the-stack-is-on-x86/) from [Eli Bendersky's website](http://eli.thegreenplace.net/), February 04, 2011


### [x86-64](X86-64 "X86-64")


* [Stack frame layout on x86-64](http://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64/) from [Eli Bendersky's website](http://eli.thegreenplace.net/), September 06, 2011


### [C++](Cpp "Cpp")


* [Stack (C++) from Wikipedia](https://en.wikipedia.org/wiki/Stack_(C%2B%2B))
* [stack<T, Sequence>](http://www.sgi.com/tech/stl/stack.html), [C++ Standard Library](https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library)
* [stack - C++ Reference](http://www.cplusplus.com/reference/stl/stack/)


### [Java](Java "Java")


* [Stack (Java 2 Platform SE v1.4.2)](http://download.oracle.com/javase/1.4.2/docs/api/java/util/Stack.html)


### .NET


* [Stack Class (System.Collections)](http://msdn.microsoft.com/en-us/library/system.collections.stack.aspx)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Stapelspeicher - Wikipedia.de](https://de.wikipedia.org/wiki/Stapelspeicher) (German)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [x86 calling conventions from Wikipedia](https://en.wikipedia.org/wiki/X86_calling_conventions)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Calling conventions for different C++ compilers and operating systems](http://www.agner.org/optimize/calling_conventions.pdf) (pdf) by [Agner Fog](http://www.agner.org/)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [x86 Disassembly/Functions and Stack Frames from Wikibooks](http://en.wikibooks.org/wiki/X86_Disassembly/Functions_and_Stack_Frames)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Arthur W. Burks](Mathematician#Burks "Mathematician"), Don W. Warren, Jesse B. Wright (**1954**) *[An Analysis of a Logical Machine Using Parenthesis-Free Notation](http://www.jstor.org/pss/2001990)*.
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Klaus Samelson](Mathematician#Samelson "Mathematician"), [Friedrich L. Bauer](Mathematician#Bauer "Mathematician") (**1960**). *[Sequential Formula Translation](http://portal.acm.org/citation.cfm?id=366968)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 3 No. 2, pp. 76-83

**[Up one Level](Data "Data")**







 
