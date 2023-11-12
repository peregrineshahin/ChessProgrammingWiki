---
title: MAPP
---
**[Home](Home "Home") \* [Knowledge](Knowledge "Knowledge") \* [Cognition](Cognition "Cognition") \* MAPP**


**MAPP**, (Memory-aided Pattern Perceiver)   

a program by [Kevin J. Gilmartin](Kevin_J._Gilmartin "Kevin J. Gilmartin") and [Herbert Simon](Herbert_Simon "Herbert Simon") to simulate the [chess board reconstruction task](William_Chase#Perception "William Chase") examined by [William Chase](William_Chase "William Chase") and Herbert Simon <a id="cite-note-1" href="#cite-ref-1">[1]</a>. MAPP contains a [learning](Learning "Learning") component to acquire and store a large set of configurations of chess pieces and a performance component to carry out the the board reconstruction task. From [Miller's](https://en.wikipedia.org/wiki/George_Armitage_Miller) [chunking hypothesis](Chunking "Chunking") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, [EPAM](EPAM "EPAM") theory, and the limited capacity of short-term [memory](Memory "Memory"), one would predict that a chessboard can be reconstructed from information held in short-term memory if, and only if, it can be encoded in not more than about seven familiar perceptual chunks. If a single piece on a particular square constitutes a chunk for the subject, then it should be able to recall only about seven pieces. If it can recall the positions of more than twenty pieces, then it must be that each chunk consists, on average, of a configuration of about three pieces <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Perception


When a [chess position](Chess_Position "Chess Position") is presented, a simplified version of the [eye movement](Eye_Movements "Eye Movements") simulation program [Perceiver](Perceiver "Perceiver") is used to scan the board in order to notice the pieces and their relations. When a piece is [fixated](https://en.wikipedia.org/wiki/Fixation_%28visual%29) ([salient](https://en.wiktionary.org/wiki/salient) piece), an EPAM-like discrimination process seeks to recognize cluster of pieces surrounding the fixated piece as a familar chunk. If it is successful, the symbol designating this chunk is stored in short-term memory. This process is repeated at successive points of fixation until no more pieces become salient or memory capacity is reached (no more than seven chunks). 



## Reconstruction


In the reconstruction phase, the EPAM net is used to decode the symbols held in short-term memory into locational information for each of the pieces in a chunk. In various experiments, MAPP was able to reconstruct positions with 73% accuracy <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



## See also


* [CHREST](CHREST "CHREST")
* [CHUMP](CHUMP "CHUMP")
* [Chunking](Chunking "Chunking")
* [EPAM](EPAM "EPAM")
* [Mater](Mater "Mater")
* [Perceiver](Perceiver "Perceiver")
* [Perception](William_Chase#Perception "William Chase")
* [Perception - Video](William_Chase#Video "William Chase")


## Publicatons


* [Herbert Simon](Herbert_Simon "Herbert Simon"), [Kevin J. Gilmartin](Kevin_J._Gilmartin "Kevin J. Gilmartin") (**1973**). *[A Simulation of Memory for Chess Positions](https://psycnet.apa.org/record/1974-08458-001)*. [Cognitive Psychology](https://en.wikipedia.org/wiki/Cognitive_Psychology_(journal)), Vol. 5, No. 1, reprinted in [Herbert Simon](Herbert_Simon "Herbert Simon") (**1979**). *[Models of Thought](https://yalebooks.yale.edu/book/9780300024326/models-thought)*, [Yale University Press](https://en.wikipedia.org/wiki/Yale_University_Press)
* [Herbert Simon](Herbert_Simon "Herbert Simon"), [William Chase](William_Chase "William Chase") (**1973**). *Skill in Chess*. [American Scientist](https://en.wikipedia.org/wiki/American_Scientist), Vol. 61, No. 4, reprinted in [David Levy](David_Levy "David Levy") (ed.) (**1988**) *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*, [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=44582)
* [Neil Charness](index.php?title=Neil_Charness&action=edit&redlink=1 "Neil Charness (page does not exist)") (**1976**). *[Memory for Chess Positions: Resistance to Interference](https://psycnet.apa.org/record/1977-07430-001)*. Journal of Experimental Psychology: Human Learning and Memory, Vol. 2, No. 6
* [Michael George](index.php?title=Michael_George&action=edit&redlink=1 "Michael George (page does not exist)"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1990**). *Chunking for Experience*. [ICCA Journal, Vol. 13, No. 3](ICGA_Journal#13_3 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~jonathan/publications/ai_publications/mach.pdf)
* [Fernand Gobet](Fernand_Gobet "Fernand Gobet") (**2005**). *[Chunking Models of Expertise: Implications for Education](https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.1110)*. Applied Cognitive Psychology, Vol. 19, No. 2


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [William Chase](William_Chase "William Chase"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1973**). *[Perception in chess](http://www.sciencedirect.com/science/article/pii/0010028573900042)*. [Cognitive Psychology](http://www.elsevier.com/wps/find/journaldescription.cws_home/622807/description#description), Vol. 4, No. 1
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [George Armitage Miller](https://en.wikipedia.org/wiki/George_Armitage_Miller) (**1956**). *[The Magical Number Seven, Plus or Minus Two](https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two)*. [Psychological Review](https://en.wikipedia.org/wiki/Psychological_Review), Vol. 101, No. 2, [pdf](http://www.psych.utoronto.ca/users/peterson/psy430s2001/Miller%20GA%20Magical%20Seven%20Psych%20Review%201955.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Herbert Simon](Herbert_Simon "Herbert Simon"), [William Chase](William_Chase "William Chase") (**1973**). *Skill in Chess*. [American Scientist](https://en.wikipedia.org/wiki/American_Scientist), Vol. 61, No. 4, pp. 401, reprinted in [David Levy](David_Levy "David Levy") (ed.) (**1988**) *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*, [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=44582)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Expertise in Memory - Evidence for Chunking Theory](http://snitkof.com/cg156/chesschunkingtheory.php) by [Victor Long](http://snitkof.com/cg156/contact.php), [Chandra Singh](http://snitkof.com/cg156/contact.php) and [David Snitkof](https://www.linkedin.com/in/davidsnitkof), [Brown University](https://en.wikipedia.org/wiki/Brown_University), see also Figure 6 in [Herbert Simon](Herbert_Simon "Herbert Simon"), [William Chase](William_Chase "William Chase") (**1973**). *Skill in Chess*. [American Scientist](https://en.wikipedia.org/wiki/American_Scientist), Vol. 61, No. 4, pp. 401, reprinted in [David Levy](David_Levy "David Levy") (ed.) (**1988**) *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*, [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=44582)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Herbert Simon](Herbert_Simon "Herbert Simon"), [Kevin J. Gilmartin](Kevin_J._Gilmartin "Kevin J. Gilmartin") (**1973**). *A Simulation of Memory for Chess Positions*. Cognitive Psychology, Vol. 5, pp. 29-46
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Michael George](index.php?title=Michael_George&action=edit&redlink=1 "Michael George (page does not exist)"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1990**). *[Chunking for Experience](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.2766)*. [ICCA Journal, Vol. 13, No. 3](ICGA_Journal#13_3 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~jonathan/publications/ai_publications/mach.pdf)

**[Up one Level](Cognition "Cognition")**







 
