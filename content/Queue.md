---
title: Queue
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* Queue**



[ Queue <a id="cite-note-1" href="#cite-ref-1">[1]</a>
A **Queue** is a [linear data structure](https://en.wikipedia.org/wiki/List_of_data_structures#Linear_data_structures) to [collect](https://en.wikipedia.org/wiki/Collection_%28computing%29) data entities in [first in, first out order](https://en.wikipedia.org/wiki/FIFO) (FIFO). The only operations are the addition of entries to the rear terminal position (enqueue) and removal of entries from the front terminal position (dequeue). Queues may be instantiated from (shared) [main memory](Memory "Memory"), and therefor accessed with low [latency](https://en.wikipedia.org/wiki/Latency_%28engineering%29) from various [processes](https://en.wikipedia.org/wiki/Process_%28computing%29) or [threads](https://en.wikipedia.org/wiki/Thread_%28computer_science%29), otherwise their hard- and low-level software implementation is hidden by [Middleware](https://en.wikipedia.org/wiki/Middleware) layers. Various free and commercial programming language libraries provide queue implementations. Queuing devices like [pipes](https://en.wikipedia.org/wiki/Pipeline_%28software%29) and [sockets](https://en.wikipedia.org/wiki/Internet_socket) are likely associated with a [stream](https://en.wikipedia.org/wiki/Stream_%28computing%29) or [file descriptor](https://en.wikipedia.org/wiki/File_descriptor). However, in memory, a queue might be implemented with an [array](Array "Array") (likely fixed sized [circular buffer](https://en.wikipedia.org/wiki/Circular_buffer)) or [linked list](Linked_List "Linked List"). 



### Buffering


A [buffer](https://en.wikipedia.org/wiki/Data_buffer) is used to temporarily keep data while it is being moved from one place to another. A buffer often adjusts timing by implementing a queue or FIFO algorithm in memory, simultaneously writing data into the queue at one rate and reading it at another rate.


Within a [physical layer](https://en.wikipedia.org/wiki/Physical_Layer), for instance the [RS-232](https://en.wikipedia.org/wiki/RS-232) (V.24) [serial port](https://en.wikipedia.org/wiki/Serial_port) and their electronic circuits, namely [universal asynchronous receiver/transmitter](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver/transmitter) (UART), FIFOs <a id="cite-note-2" href="#cite-ref-2">[2]</a> in hardware are used to relax [polling](https://en.wikipedia.org/wiki/Polling_%28computer_science%29) or [interrupt request](https://en.wikipedia.org/wiki/Interrupt_request) handling [data link layer](https://en.wikipedia.org/wiki/Data_Link_Layer) from time constrains, which may otherwise yield in possible data overruns and exception handling. Those FIFOs consists of a set of read and write "pointers", [sequential control logic](Sequential_Logic "Sequential Logic") with appropriate storage, likely a set of [flip-flops](Memory#FlipFlop "Memory") or latches. 


One application of RS-232 in computer chess is [Chrilly Donninger's](Chrilly_Donninger "Chrilly Donninger") [Auto232](Auto232 "Auto232") Interface to play automatic matches between chess programs on different computers <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### Message Queue


A [message queue](https://en.wikipedia.org/wiki/Message_queue) is used for [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication), or for inter-thread communication within the same process. Many implementations of message queues work internally within an [operating system](https://en.wikipedia.org/wiki/Operating_system) and its [graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface) like [Windows](Windows "Windows"), i.e. to pass hardware events such as [mouse](https://en.wikipedia.org/wiki/Mouse_%28computing%29) and [keyboard](https://en.wikipedia.org/wiki/Keyboard_%28computing%29) inputs to an application. Since events may have different priorities, i.e. keyboard event and paint event as request to re-paint a window, message queues of most often implemented as [priority queues](index.php?title=Priority_Queue&action=edit&redlink=1 "Priority Queue (page does not exist)").


Other queue implementations allow the passing of messages between different computer systems, connecting multiple applications and multiple operating systems. 


These message queuing systems typically provide enhanced [resilience](https://en.wikipedia.org/wiki/Resilience_%28network%29) functionality and protocols to ensure that messages do not get "lost" in the event of a system failure. It is applied by a [message-oriented middleware](https://en.wikipedia.org/wiki/Message-oriented_middleware), i. e. [remote direct memory access](https://en.wikipedia.org/wiki/RDMA) of [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) queues.



### Pipeline


One related application of a [thread safe](https://en.wikipedia.org/wiki/Thread_safety) queue for [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) is the [pipeline](https://en.wikipedia.org/wiki/Pipeline_%28software%29). The concept is mentioned as [pipes and filters](http://de.wikipedia.org/wiki/Pipes_und_Filter) [design pattern](https://en.wikipedia.org/wiki/Pipeline_%28software%29). The information that flows in these pipelines is a stream of records, [bytes](Byte "Byte") or [bits](Bit "Bit").


In computer chess protocols like the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") or the [Universal Chess Interface](UCI "UCI"), the communication between [engine](Engines "Engines") and the [graphical user interface](GUI "GUI") is likely based on pipelines, redirected from [standard streams](https://en.wikipedia.org/wiki/Standard_streams). 



### Algorithms


The [informal breadth-first algorithm](https://en.wikipedia.org/wiki/Breadth-first_search#Algorithm_.28informal.29) requires a queue to traverse all [nodes](Node "Node") of a [tree](Search_Tree "Search Tree"):



1. Enqueue the root node.
2. Dequeue a node and examine it.


 If the element sought is found in this node, quit the search and return a result.
 Otherwise enqueue any successors (the direct child nodes) that have not yet been discovered.
1. If the queue is empty, every node on the graph has been examined – quit the search and return "not found".
2. Repeat from Step 2.


## See also


* [Array](Array "Array")
* [Linked List](Linked_List "Linked List")
* [Priority Queue](index.php?title=Priority_Queue&action=edit&redlink=1 "Priority Queue (page does not exist)")
* [Stack](Stack "Stack")


## Publications


* [Maged M. Michael](http://www.research.ibm.com/people/m/michael/), [Michael L. Scott](http://www.cs.rochester.edu/~scott/) (**1996**). *Simple, Fast, and Practical Non-Blocking and Blocking Concurrent Queue Algorithms*. Department of Computer Science, [University of Rochester](https://en.wikipedia.org/wiki/University_of_Rochester), [pdf](http://www.cs.rochester.edu/u/scott/papers/1996_PODC_queues.pdf)
* [Donald Knuth](Donald_Knuth "Donald Knuth") (**1997**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/~knuth/taocp.html)*, Volume 1: Fundamental Algorithms (Third Edition), Addison-Wesley, ISBN 0-201-89683-4, 2.2.1: Stacks, Queues, and Deques, pp. 238–243.
* [Richard P. Stanley](Mathematician#RPStanley "Mathematician") (**2005**). *Queue Problems Revisited*. [pdf](http://www-math.mit.edu/~rstan/chess/queue.pdf), [Chess problem](https://en.wikipedia.org/wiki/Chess_problem) related <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* [William N. Scherer III](http://www.cs.rice.edu/~wns1/), [Doug Lea](https://en.wikipedia.org/wiki/Doug_Lea), [Michael L. Scott](http://www.cs.rochester.edu/~scott/) (**2009**). *Scalable Synchronous Queues*. Communications of the ACM, Vol. 52. No. 5, [pdf](http://www.cs.rochester.edu/u/scott/papers/2009_Scherer_CACM_SSQ.pdf)
* [Thomas H. Cormen](Mathematician#THCormen "Mathematician"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Ronald L. Rivest](Ronald_L._Rivest "Ronald L. Rivest"), [Clifford Stein](Mathematician#CliffordStein "Mathematician") (**2009**). *[Introduction to Algorithms, 3rd Edition](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)*. ISBN 0-262-03384-4. 10.1: Stacks and queues


## External Links


* [Queue (abstract data type) from Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
* [queue](http://xlinux.nist.gov/dads//HTML/queue.html) from [Dictionary of Algorithms and Data Structures](http://xlinux.nist.gov/dads/) by [Paul E. Black](http://hissa.nist.gov/~black/), [National Institute of Standards and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)
* [FIFO from Wikipedia](https://en.wikipedia.org/wiki/FIFO)
* [Double-ended queue from Wikipedia](https://en.wikipedia.org/wiki/Double-ended_queue)
* [Named pipe from Wikipedia](https://en.wikipedia.org/wiki/Named_pipe)
* [Queueing theory from Wikipedia](https://en.wikipedia.org/wiki/Queueing_theory)
* [Hartmann pipeline from Wikipedia](https://en.wikipedia.org/wiki/Hartmann_pipeline)
* [Circular buffer from Wikipedia](https://en.wikipedia.org/wiki/Circular_buffer)


 [![Ring buffer.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Ring_buffer.svg/246px-Ring_buffer.svg.png)](http://de.wikipedia.org/wiki/Warteschlange_%28Datenstruktur%29)
### [C](C "C")


* [Pipes and FIFOs](http://www.gnu.org/s/libc/manual/html_node/Pipes-and-FIFOs.html) - [The GNU C Library](Free_Software_Foundation#GLIBC "Free Software Foundation")
* [Sockets](http://www.gnu.org/s/libc/manual/html_node/Sockets.html) - [The GNU C Library](Free_Software_Foundation#GLIBC "Free Software Foundation")


### [C++](Cpp "Cpp")


* [C++ Reference : STL Containers : queue](http://www.cplusplus.com/reference/stl/queue/)
* [queue<T, Sequence>](http://www.sgi.com/tech/stl/queue.html) from [Standard Template Library Programmer's Guide](http://www.sgi.com/tech/stl/index.html)
* [Qt 4.6: QQueue Class Reference](http://doc.qt.nokia.com/4.6/qqueue.html)
* [Boost Graph Library: Breadth-First Search](http://www.boost.org/doc/libs/1_43_0/libs/graph/doc/breadth_first_search.html)


 [Boost C++ Libraries - boost/pending/queue.hpp](http://www.boost.org/doc/libs/1_42_0/boost/pending/queue.hpp)
 [Boost C++ Libraries - libs/graph/example/dave.cpp](http://www.boost.org/doc/libs/1_43_0/libs/graph/example/dave.cpp)
* [Dr Dobbs - Lock-Free Queues](http://www.drdobbs.com/high-performance-computing/208801974;jsessionid=BVBQM504XGJA1QE1GHPSKH4ATMY32JVN)


### [Java](Java "Java")


* [Queue (Java 2 Platform SE 5.0)](http://docs.oracle.com/javase/1.5.0/docs/api/java/util/Queue.html)
* [Java IO Tutorial: Pipes](http://tutorials.jenkov.com/java-io/pipes.html)


### [Perl](index.php?title=Perl&action=edit&redlink=1 "Perl (page does not exist)")


* [Thread::Queue - perldoc.perl.org](http://perldoc.perl.org/Thread/Queue.html)


### [Python](Python "Python")


* [5.10 Queue -- A synchronized queue class](http://docs.python.org/release/2.5.2/lib/module-Queue.html)


### [Ruby](index.php?title=Ruby&action=edit&redlink=1 "Ruby (page does not exist)")


* [Class: Queue](http://www.ensta.fr/~diam/ruby/online/ruby-doc-stdlib/libdoc/thread/rdoc/classes/Queue.html)


### [Tcl](index.php?title=Tcl-Tk&action=edit&redlink=1 "Tcl-Tk (page does not exist)")


* [TCLLIB - Tcl Standard Library: struct::queue](http://tcllib.sourceforge.net/doc/queue.html)


### .NET


* [Queue Class (System.Collections)](http://msdn.microsoft.com/en-us/library/system.collections.queue.aspx) from [MSDN Library](http://msdn.microsoft.com/en-us/library/ms123401.aspx)
* [CHESS-Lock Free Queue](http://www.projectbentley.com/work/chess/lockfreequeue.php) © [Michael Bentley](http://www.projectbentley.com/) 2009 <a id="cite-note-5" href="#cite-ref-5">[5]</a>


### Middleware


* [Advanced Message Queuing Protocol from Wikipedia](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)
* [Advanced Message Queuing Protocol - Website](http://www.amqp.org/confluence/display/AMQP/Advanced+Message+Queuing+Protocol)
* [Java Message Service](https://en.wikipedia.org/wiki/Java_Message_Service)
* [Open Message Queue from Wikipedia](https://en.wikipedia.org/wiki/Open_Message_Queue)
* [Open Message Queue : Open Source Java Message Service (JMS)](https://mq.dev.java.net/)
* [Apache ActiveMQ from Wikipedia](https://en.wikipedia.org/wiki/Apache_ActiveMQ)
* [Apache ActiveMQ - Index](http://activemq.apache.org/)
* [JORAM from Wikipedia](https://en.wikipedia.org/wiki/JORAM)
* [JBoss Messaging from Wikipedia](https://en.wikipedia.org/wiki/JBoss_Messaging)
* [JBossMessaging - JBoss Community](http://community.jboss.org/wiki/jbossmessaging)
* [Oracle Advanced Queuing from Wikipedia](https://en.wikipedia.org/wiki/Oracle_Advanced_Queuing)
* [IBM WebSphere MQ from Wikipedia](https://en.wikipedia.org/wiki/IBM_WebSphere_MQ)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Queue (abstract data type) from Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Serial UART, an in depth tutorial](http://www.lammertbies.nl/comm/info/serial-uart.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Technische Spezifikation des 232-Protokolls](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/636e82fa68d45aa1#), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 8, 1997
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chess Problems](http://www-math.mit.edu/~rstan/chess/)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [CHESS - Microsoft Research](http://research.microsoft.com/en-us/projects/chess/) a tool for finding and reproducing [Heisenbugs](https://en.wikipedia.org/wiki/Unusual_software_bug) in concurrent programs

**[Up one Level](Data "Data")**







 
