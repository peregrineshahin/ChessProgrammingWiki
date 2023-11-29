---
title: Iterative Deepening
---
**[Home](Home "Home") \* [Search](Search "Search") \* Iterative Deepening**



 [](http://ray.sakura.ne.jp/search_problem/i_deepening.html) Iterative deepening search <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Iterative deepening** (ID) has been adopted as the basic [time management](Time_Management "Time Management") strategy in [depth-first searches](Depth-First "Depth-First"), but has proved surprisingly beneficial as far as [move ordering](Move_Ordering "Move Ordering") is concerned in [alpha-beta](Alpha-Beta "Alpha-Beta") and its enhancements. It has been noticed, that even if one is about to search to a given depth, that iterative deepening is faster than searching for the given depth immediately. This is due to dynamic move ordering techniques such as; [PV-](PV-Move "PV-Move"), [hash-](Hash_Move "Hash Move") and [refutation moves](Refutation_Move "Refutation Move") determined in previous [iteration(s)](Iteration "Iteration"), as well the [history heuristic](History_Heuristic "History Heuristic"). 



## History


Iterative or progressive deepening was first mentioned by [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") in *Thought and Choice in Chess* <a id="cite-note-2" href="#cite-ref-2">[2]</a> . [Richard Korf](Richard_Korf "Richard Korf") on its "discovery" in *Depth-first Iterative-Deepening: An Optimal Admissible Tree Search* <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> :




```C++Depth-first iterative-deepening has no doubt been rediscovered many times independently. The first use of the algorithm that is documented in the literature is in [Slate](David_Slate "David Slate") and [Atkin's](Larry_Atkin "Larry Atkin") [Chess 4.5](Chess_(Program) "Chess (Program)") program <a id="cite-note-5" href="#cite-ref-5">[5]</a>. [Berliner](Hans_Berliner "Hans Berliner") <a id="cite-note-6" href="#cite-ref-6">[6]</a> has observed that breadth-first search is inferior to the iterative-deepening algorithm. [Winston](Patrick_Winston "Patrick Winston") <a id="cite-note-7" href="#cite-ref-7">[7]</a> shows that for two-person game searches where only terminal-node static evaluations are counted in the cost, the extra computation required by iterative-deepening is insignificant. [Pearl](Judea_Pearl "Judea Pearl") initially suggested the iterative-deepening extension of [A\*](index.php?title=A*&action=edit&redlink=1 "A* (page does not exist)"), and [Berliner](Hans_Berliner "Hans Berliner") and [Goetsch](Gordon_Goetsch "Gordon Goetsch") <a id="cite-note-8" href="#cite-ref-8">[8]</a> have implemented such an algorithm concurrently with this work. 

```

[Tony Marsland](Tony_Marsland "Tony Marsland") in *Computer Chess and Search* on the History of ID <a id="cite-note-9" href="#cite-ref-9">[9]</a> :




```C++In the early 1970’s several people tried a variety of ways to control the exponential growth of the tree search. A simple fixed depth search is inflexible, especially if it must be completed within a specified time. This difficulty was noted by [Scott](John_J._Scott "John J. Scott") <a id="cite-note-10" href="#cite-ref-10">[10]</a> who reported in 1969 on the effective use of an iterated search. [Jim Gillogly](James_Gillogly "James Gillogly"), author of the [Tech](Tech "Tech") chess program <a id="cite-note-11" href="#cite-ref-11">[11]</a> , coined the term iterative deepening to distinguish a full-width search to increasing depths from the progressively more focused search described by [de Groot](Adriaan_de_Groot "Adriaan de Groot"). About the same time [David Slate](David_Slate "David Slate") and [Larry Atkin](Larry_Atkin "Larry Atkin") (1977) sought a better time control mechanism, and introduced an improved iterated search for carrying out a progressively deeper and deeper analysis. For example, an iterated series of 1-ply, 2-ply, 3-ply ... searches is carried out, with each new search first retracing the best path from the previous iteration and then extending the search by one ply. Early experimenters with this scheme were surprised to find that the iterated search often required less time than an equivalent direct search... 

```

## See also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Best-First](Best-First "Best-First")
* [Depth-First](Depth-First "Depth-First")
* [Effective Branching Factor](Branching_Factor#EffectiveBranchingFactor "Branching Factor")
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [Move Ordering](Move_Ordering "Move Ordering")
* [MTD(f)](MTD(f) "MTD(f)")
* [Odd-Even Effect](Odd-Even_Effect "Odd-Even Effect")
* [Time Management](Time_Management "Time Management")
* [Transposition Table](Transposition_Table "Transposition Table")


## Publications


### 1965 ...


* [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") (**1965**). *Thought and Choice in Chess.* Mouton & Co Publishers, The Hague, The Netherlands. Second edition **1978**. ISBN 90-279-7914-6. ([amazon](http://www.amazon.com/gp/reader/9027979146/ref=sib_dp_pt#reader-link))
* [John J. Scott](John_J._Scott "John J. Scott") (**1969**). *A Chess Playing Program*. in [Machine Intelligence 4](http://www.doc.ic.ac.uk/~shm/MI/mi4.html) (ed. [Donald Michie](Donald_Michie "Donald Michie")), pp. 255-265 <a id="cite-note-12" href="#cite-ref-12">[12]</a>


### 1970 ...


* [James Gillogly](James_Gillogly "James Gillogly") (**1972**). *The Technology Chess Program*. Artificial Intelligence, Vol. 3, pp. 145-163. ISSN 0004-3702. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")


### 1980 ...


* [William Fink](William_Fink "William Fink") (**1982**). *An Enhancement to the Iterative, Alpha-Beta, Minimax Search Procedure*. [ICCA Newsletter](ICGA_Journal "ICGA Journal"), Vol. 5, No. 1
* [Hans Berliner](Hans_Berliner "Hans Berliner") (**1983**). *Search*, Artificial Intelligence Syllabus, Department of Computer Science, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
* [Richard Korf](Richard_Korf "Richard Korf") (**1984**). *The Complexity of Brute Force Search*. Technical Report, Department of Computer Science, [Columbia University](Columbia_University "Columbia University") <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a>
* [Richard Korf](Richard_Korf "Richard Korf") (**1985**). *Depth-first Iterative-Deepening: An Optimal Admissible Tree Search*. [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.91.288)


### 1990 ...


* [Matthew L. Ginsberg](Matthew_L._Ginsberg "Matthew L. Ginsberg"), [William D. Harvey](Mathematician#WDHarvey "Mathematician") (**1990**). *Iterative Broadening*. [AAAI 90](Conferences#AAAI-90 "Conferences"), [pdf](https://www.aaai.org/Papers/AAAI/1990/AAAI90-033.pdf)
* [Matthew L. Ginsberg](Matthew_L._Ginsberg "Matthew L. Ginsberg") (**1993**). *[Essentials of artificial intelligence](https://searchworks.stanford.edu/view/2746445)*. [Morgan Kaufmann Publishers](https://en.wikipedia.org/wiki/Morgan_Kaufmann_Publishers), 3.3 Iterative Deepening
* [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1994**). *Enhanced Iterative-Deepening Search.* [Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 16, No. 7, [pdf](http://webdocs.cs.ualberta.ca/%7Etony/RecentPapers/pami94.pdf)


## Forum Posts


### 1988


* [Re: "Iterative Deeping" reference wanted](http://fox.cs.vt.edu/VAD1/DOWN/AILIST/V8/N138) by [Ira Baxter](Ira_Baxter "Ira Baxter"), AIList Digest, December 06, 1988


### 1990 ...


* [Re: Computer Chess and alpha-beta pruning](https://groups.google.com/d/msg/rec.games.chess/XQWb-ZjSsy0/gsXMq42a-FAJ) by [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 22, 1993 » [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Tricks in iterative deepening; was Re: AEGON '97](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/530959055901588a) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 26, 1997 » [Aegon 1997](Aegon_1997 "Aegon 1997")
* [Iterative Deepening](https://groups.google.com/d/msg/rec.games.chess.computer/24sL-_prZzw/3km3MA9ADxoJ) by John Scalo, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 27, 1997
* [pv score oscillation](https://www.stmintz.com/ccc/index.php?id=10903) by [Willie Wood](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), October 18, 1997
* [Selective deepening and Hashtables](https://www.stmintz.com/ccc/index.php?id=21654) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), June 30, 1998


### 2000 ...


* [Iterative deepening deep increment](https://www.stmintz.com/ccc/index.php?id=156310) by [Alvaro Jose Povoa Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), February 27, 2001
* [iterative deepening and branching factor](http://www.talkchess.com/forum/viewtopic.php?t=14963) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), July 09, 2007 » [Effective Branching Factor](Branching_Factor#EffectiveBranchingFactor "Branching Factor")
* [Even more search questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6666) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 17, 2007


### 2010 ...


* [Node counts at a given depth/iteration in search](http://www.open-chess.org/viewtopic.php?f=5&t=1403) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), May 23, 2011
* [Bigger steps when branching factor < 2?](http://www.talkchess.com/forum/viewtopic.php?t=41001) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), November 05, 2011 » [Effective Branching Factor](Branching_Factor#EffectiveBranchingFactor "Branching Factor")
* [Restarting iterative deepening](http://www.talkchess.com/forum/viewtopic.php?t=58542) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 09, 2015 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows"), [Fail-Low](Fail-Low "Fail-Low")
* [How do you signal stalemate in iterative deepening?](http://www.talkchess.com/forum/viewtopic.php?t=59281) by Kenneth Jones, [CCC](CCC "CCC"), February 17, 2016 » [Stalemate](Stalemate "Stalemate")
* [Iterative Deepening](http://www.open-chess.org/viewtopic.php?f=5&t=2959) by kickstone, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 26, 2016
* [TT and Iterative Deepening](http://www.open-chess.org/viewtopic.php?f=5&t=2961) by kuket15, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 26, 2016 » [Transposition Table](Transposition_Table "Transposition Table")
* [Iterative Deepening Question](http://www.talkchess.com/forum/viewtopic.php?t=60916) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), July 23, 2016 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [(I)ID and PV dropout](http://www.talkchess.com/forum/viewtopic.php?t=64321) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 17, 2017 » [Fail-Low](Fail-Low "Fail-Low"), [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")


## External Links


* [Iterative deepening depth-first search from Wikipedia](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
* [Iterative deepening notes](http://cseweb.ucsd.edu/%7Eelkan/130fall99/itdeep.html) by [Charles Elkan](Charles_Elkan "Charles Elkan")
* [Chapter 3 Solving Problems by Searching](http://homepages.ius.edu/RWISMAN/C463/html/Chapter3.htm) from [C463 Artificial Intelligence Syllabus](http://homepages.ius.edu/RWISMAN/C463/html/syllabus.htm) by [Raymond F. Wisman](http://homepages.ius.edu/RWISMAN/)
* [µ-Max Search: Iterative Deepening](http://home.hccnet.nl/h.g.muller/deepen.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
* [Michał Urbaniak](Category:Michal_Urbaniak "Category:Michal Urbaniak") - [Always Ready](https://www.discogs.com/de/Micha%C5%82-Urbaniak-Urbaniak/release/1641078) (1977), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [Michał Urbaniak](Category:Michal_Urbaniak "Category:Michal Urbaniak"), [Zbigniew Namysłowski](https://en.wikipedia.org/wiki/Zbigniew_Namys%C5%82owski), [Urszula Dudziak](Category:Urszula_Dudziak "Category:Urszula Dudziak"), [Kenny Kirkland](https://en.wikipedia.org/wiki/Kenny_Kirkland), [Tony Bunn](https://en.wikipedia.org/wiki/Tony_Bunn), [Laurenda Featherstone](https://www.discogs.com/artist/608833-Lurenda-Featherstone)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Iterative deepening （反復深化法）](http://ray.sakura.ne.jp/search_problem/i_deepening.html)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") (**1965**). *Thought and Choice in Chess.* Mouton & Co Publishers, The Hague, The Netherlands. Second edition **1978**. ISBN 90-279-7914-6. ([amazon](http://www.amazon.com/gp/reader/9027979146/ref=sib_dp_pt#reader-link))
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Richard Korf](Richard_Korf "Richard Korf") (**1985**). *Depth-first Iterative-Deepening: An Optimal Admissible Tree Search*. [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.91.288)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2010**). *Depth-First Iterative-Deepening: An Optimal Admissible Tree Search by [R. E. Korf](Richard_Korf "Richard Korf")*, slides as [pdf](http://www.iis.sinica.edu.tw/~tshsu/tcg2010/slides/slide3.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1983**). *Search*. Artificial Intelligence Syllabus, Department of Computer Science, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Patrick Winston](Patrick_Winston "Patrick Winston") (**1984**). *[Artificial Intelligence](http://people.csail.mit.edu/phw/Books/index.html#AI)*. Addison-Wesley, Reading, MA
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Hans Berliner](Hans_Berliner "Hans Berliner"), [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch") (**1984**). *A quantitative study of search methods and the effect of constraint satisfaction*. Tech. Report CMU-CS-84-147, Department of Computer Science, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), Pittsburgh, PA.
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Computer Chess and Search*. Encyclopedia of Artificial Intelligence (2nd ed.) John Wiley & Sons, Inc. [pdf preprint](http://webdocs.cs.ualberta.ca/~tony/RecentPapers/Marsland-CCandSearch-1991.pdf)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [John J. Scott](John_J._Scott "John J. Scott") (**1969**). *A chess-playing program*. [Machine Intelligence 4](http://www.doc.ic.ac.uk/~shm/MI/mi4.html)
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [James Gillogly](James_Gillogly "James Gillogly") (**1972**). *The Technology Chess Program*. Artificial Intelligence, Vol. 3, pp. 145-163. ISSN 0004-3702. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Re: "Iterative Deeping" reference wanted](http://fox.cs.vt.edu/VAD1/DOWN/AILIST/V8/N138) by [Ira Baxter](Ira_Baxter "Ira Baxter"), AIList Digest, December 06, 1988
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> quoted by [Hans Berliner](Hans_Berliner "Hans Berliner"), [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch") (**1985**). *A Study of Search Methods : The Effect of Constraint Satisfaction and Adventurousness*. [pdf](https://www.ijcai.org/Proceedings/85-2/Papers/083.pdf)
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> Paper is mentioned by [Richard Korf](Richard_Korf#JudeaPearl "Richard Korf") at [Judea Pearl Symposium](Judea_Pearl#Symposium "Judea Pearl"), 2010

**[Up one Level](Search "Search")**







 
