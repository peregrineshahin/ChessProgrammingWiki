---
title: Java
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Languages](Languages "Languages") \* Java**


**Java** has been developed by [Sun Microsystems](index.php?title=Sun_Microsystems&action=edit&redlink=1 "Sun Microsystems (page does not exist)") since 1991 and is mostly connected with [James Gosling](https://en.wikipedia.org/wiki/James_Gosling). The aim was to design a language that uses as [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) and is thus capable to run on any OS. The initial goal was that Java can be also used to control all devices as coffee machines. But he the fact that Java was quite free and OS independent has made Java very popular <a id="cite-note-1" href="#cite-ref-1">[1]</a>. And so the environment has grown to several platforms for normal programming ([SE](https://en.wikipedia.org/wiki/Java_Platform,_Standard_Edition)), Enterprise Programming ([EE](https://en.wikipedia.org/wiki/Java_Platform,_Enterprise_Edition)) and Mobile Programming ([ME](https://en.wikipedia.org/wiki/Java_Platform,_Micro_Edition)). The most important aspect is that Java compiles to a [bytecode](https://en.wikipedia.org/wiki/Bytecode). And this bytecode is then interpreted by virtual machine, or [JIT compiled](https://en.wikipedia.org/wiki/Just-in-time_compilation). And Java is a [object oriented](https://en.wikipedia.org/wiki/Object_oriented) language with a lot of additional feature as a good security concept, [reflection](https://en.wikipedia.org/wiki/Reflection_(computer_science)), annotations, [generics](https://en.wikipedia.org/wiki/Generics_in_Java), etc. For chess programming Java has lots of advantages but also some disadvantages.



## Disadvantages


* Java was long time called a slow engine. Especially by game developers who needed fast graphics speed. In fact Java wasn't designed to deliver fast graphics. But on the other hand Java is not that slow as most people expected. It is one of the fastest vm languages available. A look on benchmarks like the [shootout](http://dada.perl.it/shootout/) shows that Java is fast. Unfortunately it is about 2-10 times slower that pure [C](C "C") or [C++](Cpp "Cpp"). So in order to have the best **engine performance**, most developers tend to use C and C++ and not Java.
* The Java environment can not easily generate **\*.exe** files that represent chess engines. So a bat file has to be called to run the java vm. And this can make trouble in some Chess GUIs.
* Java has **no unsigned long** data type that is e.g. used by [bitboards](Bitboards "Bitboards"). Thus one has to use [unsigned right shift operator >>>](https://chessprogramming.wikispaces.com/General+Setwise+Operations#Shifting%20Bitboards) <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
* The Java **garbage collector** makes ram usage and the response time a little non-deterministic. But this is mostly not regarded as a real problem for chess developers.






## Java Engines


* [Category:Java](Category:Java "Category:Java") <a id="cite-note-4" href="#cite-ref-4">[4]</a>:


## See also


* [Generic Programming](Generic_Programming "Generic Programming")
* [Hyperbola Quintessence in Java](Hyperbola_Quintessence#Java "Hyperbola Quintessence")
* [Java-Bitscan](Java-Bitscan "Java-Bitscan")


## Books & Papers


### 1995 ...


* [Gary McGraw](https://en.wikipedia.org/wiki/Gary_McGraw), [Ed Felten](Ed_Felten "Ed Felten") (**1996**). *[Java Security - Hostile Applets, Holes & Antidotes](https://openlibrary.org/books/OL7612897M/Java_Security)*. [John Wiley & Sons](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)
* [Andrew Appel](index.php?title=Andrew_Appel&action=edit&redlink=1 "Andrew Appel (page does not exist)") (**1998**). *[Modern Compiler Implementation in Java](https://www.cs.princeton.edu/~appel/modern/java/)*. [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
* [Liwu Li](Liwu_Li "Liwu Li") (**1998**). *[Java - Data Structures and Programming](https://link.springer.com/book/10.1007%2F978-3-642-95851-9)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Erik D. Demaine](Erik_D._Demaine "Erik D. Demaine") (**1998**). *[C to Java: Converting Pointers into References](http://erikdemaine.org/papers/CPE98/)*. [Concurrency: Practice and Experience, Vol. 10](https://dblp.org/db/journals/concurrency/concurrency10.html), Nos. 11-13


### 2000 ...


* [Barbara Liskov](Barbara_Liskov "Barbara Liskov"), [John Guttag](https://en.wikipedia.org/wiki/John_Guttag) (**2000**). *[Program Development in Java; Abstraction, Specification, and Object-oriented Design](https://www.amazon.com/Program-Development-Java-Specification-Object-Oriented/dp/0201657686/ref=sr_1_1?s=books&ie=UTF8&qid=1344621866&sr=1-1)*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
* [Raimond Reichert](http://beat.doebe.li/bibliothek/p01018.html), [Jürg Nievergelt](J%C3%BCrg_Nievergelt "Jürg Nievergelt"), [Werner Hartmann](http://beat.doebe.li/bibliothek/p00342.html) (**2000**). *[Ein spielerischer Einstieg in die Programmierung mit Java](http://beat.doebe.li/bibliothek/t02012.html)*. Informatik Spektrum (German)
* [Patrick Winston](Patrick_Winston "Patrick Winston"), [Sundar Narasimhan](https://www.sabre.com/about/executive-leadership/sundar-narasimhan/) (**2001**). *[On To Java](http://people.csail.mit.edu/phw/OnToJava/)*. 3rd edition
* [Yue Yang](https://dblp.uni-trier.de/pers/hd/y/Yang:Yue), [Ganesh Gopalakrishnan](https://dblp.uni-trier.de/pers/hd/g/Gopalakrishnan:Ganesh), [Gary Lindstrom](Gary_Lindstrom "Gary Lindstrom") (**2002**). *Specifying Java Thread Semantics Using a Uniform Memory Model*. [Java Grande 2002](https://dblp.uni-trier.de/db/conf/java/java2002.html), [pdf](http://formalverification.cs.utah.edu/yyang/papers/umm_old.pdf)
* [Andrew Appel](index.php?title=Andrew_Appel&action=edit&redlink=1 "Andrew Appel (page does not exist)"), [Jens Palsberg](https://dblp.uni-trier.de/pers/hd/p/Palsberg:Jens) (**2002**). *[Modern Compiler Implementation in Java](http://www.cambridge.org/catalogue/catalogue.asp?isbn=9780521820608)*. 2nd edition, [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
* [Amy J. Kerr](https://dblp.uni-trier.de/pers/hd/k/Kerr:Amy_J=), [Todd W. Neller](Todd_W._Neller "Todd W. Neller"), [Christopher J. La Pilla](https://dblp.uni-trier.de/pers/hd/p/Pilla:Christopher_J=_La) , [Michael D. Schompert](https://dblp.uni-trier.de/pers/hd/s/Schompert:Michael_D=) (**2002**). *[Java Resources for Teaching Reinforcement Learning](https://www.semanticscholar.org/paper/Java-Resources-for-Teaching-Reinforcement-Learning-Kerr-Neller/3d84018eb8b8668c13d1d4f6efca4442af2915b4)*. [PDPTA 2003](https://dblp.uni-trier.de/db/conf/pdpta/pdpta2003-3.html) » [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
* [Liwu Li](Liwu_Li "Liwu Li") (**2004**). *[Extending the Java Language with Dynamic Classification](http://www.jot.fm/contents/issue_2004_07/article2.html)*. [Journal of Object Technology](https://en.wikipedia.org/wiki/The_Journal_of_Object_Technology), Vol. 3, No 7


### 2005 ...


* [Liwu Li](Liwu_Li "Liwu Li") (**2005**). *[Implementing the π-Calculus in Java](http://www.jot.fm/issues/issue_2005_03/article5/)*. [Journal of Object Technology](https://en.wikipedia.org/wiki/The_Journal_of_Object_Technology), Vol. 4, No. 2 <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [Paul Fischer](Paul_Fischer "Paul Fischer") (**2005**). *An Introduction to Graphical User Interfaces with Java Swing*. [Pearson Education](https://en.wikipedia.org/wiki/Pearson_Education), [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley), [Amazon.de](http://www.amazon.de/Introduction-Graphical-User-Interfaces-Swing/dp/0321220706) » [GUI](GUI "GUI")
* [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [Kang Zhang](http://www.utdallas.edu/~kzhang/) (**2007**). *[Computer Graphics for Java Programmers, 2nd Edition](http://home.planet.nl/%7Eammeraal/grjava2e.html)*, ISBN-13: 978-0-470-03160-5, [John Wiley](http://eu.wiley.com/WileyCDA/Section/id-300022.html)
* [David J. Barnes](David_J._Barnes "David J. Barnes"), [Michael Kölling](https://en.wikipedia.org/wiki/Michael_K%C3%B6lling) (**2008, 2012**). *[Objects First with Java: A Practical Introduction using BlueJ](https://www.bluej.org/objects-first/)*. [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall) / [Pearson Education](https://en.wikipedia.org/wiki/Pearson_PLC)
* [Carl Burch](http://www.cburch.com/index.html) (**2009**). *[Programming via Java](http://www.toves.org/books/java/index.html)*. On-line Book


### 2010 ...


* [Mark Watson](Mark_Watson "Mark Watson") (**2016**). *Practical Artificial Intelligence Programming With Java*. Sixth Edition <a id="cite-note-6" href="#cite-ref-6">[6]</a> » [Artificial Intelligence](Artificial_Intelligence "Artificial Intelligence")


## Forum Posts


### 1997 ...


* [Java chess program?](https://groups.google.com/d/msg/rec.games.chess.computer/o3AMPvhmY3o/sh0xjWnVyHMJ) by Robert Epps, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 28, 1997
* [bitboards in java?](https://www.stmintz.com/ccc/index.php?id=48176) by vitor, [CCC](CCC "CCC"), April 06, 1999 » [Bitboards](Bitboards "Bitboards")
* [Saboteur - A Java chess engine](https://www.stmintz.com/ccc/index.php?id=72423) by [Josh Levine](index.php?title=Josh_Levine&action=edit&redlink=1 "Josh Levine (page does not exist)"), [CCC](CCC "CCC"), October 09, 1999 » [Saboteur](index.php?title=Saboteur&action=edit&redlink=1 "Saboteur (page does not exist)")


### 2000 ...


* [ChessPartner Summer updates + Java chess](https://www.stmintz.com/ccc/index.php?id=118709) by [Lex Loep](Lex_Loep "Lex Loep"), [CCC](CCC "CCC"), July 11, 2000 » [ChessPartner](ChessPartner "ChessPartner")
* [Java vs. C++ Chess Programming Question](https://www.stmintz.com/ccc/index.php?id=169936) by Sam Gross, [CCC](CCC "CCC"), May 15, 2001
* [Java versus C Speed Comparison](https://www.stmintz.com/ccc/index.php?id=275303) by Graham Laight, [CCC](CCC "CCC"), January 06, 2003
* [Use of Java UCI/WB Chess Engines](https://www.stmintz.com/ccc/index.php?id=368309) by Manfred Rosenboom, [CCC](CCC "CCC"), May 31, 2004
* [Java chess engines](https://www.stmintz.com/ccc/index.php?id=375592) by Eydun Lamhauge, [CCC](CCC "CCC"), July 10, 2004
* [Java Application Server and Chess](https://www.stmintz.com/ccc/index.php?id=387745) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), September 15, 2004
* [Java Chess](http://www.talkchess.com/forum/viewtopic.php?t=13046) by [William H. Rogers](William_H._Rogers "William H. Rogers"), [CCC](CCC "CCC"), April 12, 2007
* [Magic bitboards, Java](http://www.talkchess.com/forum/viewtopic.php?t=15896) by Sargon, [CCC](CCC "CCC"), August 19, 2007 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [Java & Magic Bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49948) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 03, 2009 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [OliThink GUI in Java... Complete source posted](http://www.talkchess.com/forum/viewtopic.php?t=30793) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), November 25, 2009 » [OliThink](OliThink "OliThink"), [GUI](GUI "GUI")


### 2010 ...


* [Winboard/Java help](http://www.talkchess.com/forum/viewtopic.php?t=43411) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), April 22, 2012 » [WinBoard](WinBoard "WinBoard")
* [32-bit and 64-bit java engines](http://www.talkchess.com/forum/viewtopic.php?t=51279) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), February 14, 2014


 [Re: Yes](http://www.talkchess.com/forum/viewtopic.php?t=51279&start=3) by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"), [CCC](CCC "CCC"), February 24, 2014 » [Fischerle](Fischerle "Fischerle")
* [java engines](http://www.talkchess.com/forum/viewtopic.php?t=58080) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), October 28, 2015
* [Java problem!](http://www.talkchess.com/forum/viewtopic.php?t=65718) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), November 13, 2017
* [Bitboards and Java](http://www.talkchess.com/forum/viewtopic.php?t=65724) by [Fred Hamilton](index.php?title=Fred_Hamilton&action=edit&redlink=1 "Fred Hamilton (page does not exist)"), [CCC](CCC "CCC"), November 14, 2017 » [Bitboards](Bitboards "Bitboards")


### 2020 ...


* [Java vs C. It's not like one would think](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74256) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 22, 2020 » [OliThink](OliThink "OliThink"), [C](C "C")


## External Links


### Language


* [Java (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Java_%28programming_language%29)
* [Java applet from Wikipedia](https://en.wikipedia.org/wiki/Java_applet)
* [Java virtual machine from Wikipedia](https://en.wikipedia.org/wiki/Java_virtual_machine)
* [Generics in Java from Wikipedia](https://en.wikipedia.org/wiki/Generics_in_Java)
* [Java Native Interface from Wikipedia](https://en.wikipedia.org/wiki/Java_Native_Interface)
* [log4j from Wikipedia](https://en.wikipedia.org/wiki/Log4j)
* [Java Basics Lessons](http://leepoint.net/JavaBasics/index.html) by [Fred Swartz](Fred_Swartz "Fred Swartz")
* [Java implementation of algorithms](https://github.com/aimacode/aima-java) from [Norvig](Peter_Norvig "Peter Norvig") and [Russell's](Stuart_Russell "Stuart Russell") *[Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu/)*. 3rd edition
* [Java IAQ: Infrequently Answered Questions](http://norvig.com/java-iaq.html) by [Peter Norvig](Peter_Norvig "Peter Norvig")
* [Lambda-search Java-code (version 2.0)](http://www.t-t.dk/go/cg2000/code20.html) by [Thomas Thomsen](index.php?title=Thomas_Thomsen&action=edit&redlink=1 "Thomas Thomsen (page does not exist)") » [Lambda-Search](index.php?title=Lambda-Search&action=edit&redlink=1 "Lambda-Search (page does not exist)")
* [comp.lang.java](https://groups.google.com/forum/#!forum/comp.lang.java)


### Chess Libraries


* [GitHub - ljgw/syzygy-bridge: Java bridge to use the Syzygy Tablebases via JNI](https://github.com/ljgw/syzygy-bridge) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen") » [FrankWalter](FrankWalter "FrankWalter"), [Syzygy Bases](Syzygy_Bases "Syzygy Bases")


### Video Tutorials


* [Simple Java Chess Engine Tutorial Series](https://www.youtube.com/playlist?list=PLQV5mozTHmaffB0rBsD6m9VN1azgo5wXl) by [Jonathan Warkentin](Jonathan_Warkentin "Jonathan Warkentin"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos


 
* [Advanced Java Chess Engine Tutorial Series](https://www.youtube.com/playlist?list=PLQV5mozTHmacMeRzJCW_8K3qw2miYqd0c) by [Jonathan Warkentin](Jonathan_Warkentin "Jonathan Warkentin")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [TIOBE Index](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Java chess program?](https://groups.google.com/d/msg/rec.games.chess.computer/o3AMPvhmY3o/1yZhMk3_VlIJ) by [Moritz Berger](Moritz_Berger "Moritz Berger"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 29, 1997 » [Shifting Bitboards](General_Setwise_Operations#ShiftingBitboards "General Setwise Operations")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Bitboards and Java](http://www.talkchess.com/forum/viewtopic.php?t=65724) by [Fred Hamilton](index.php?title=Fred_Hamilton&action=edit&redlink=1 "Fred Hamilton (page does not exist)"), [CCC](CCC "CCC"), November 14, 2017
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [java engines](http://www.talkchess.com/forum/viewtopic.php?t=58080) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), October 28, 2015
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [π-calculus from Wikipedia](https://en.wikipedia.org/wiki/%CE%A0-calculus)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Mark Watson · GitHub](https://github.com/mark-watson)

**[Up one Level](Languages "Languages")**







 
