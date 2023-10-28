---
title: TechTech2
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Tech**



 [](File:Technophilia.JPG) [Technophilia](https://en.wikipedia.org/wiki/Technophilia) <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**The Technology Chess Program**,  

abbreviated **Tech**, was one of the predecessors of modern chess programs, using a [Shannon](Claude_Shannon "Claude Shannon") [Type A Strategy](Type_A_Strategy "Type A Strategy"). In [1970](Timeline#1970 "Timeline") Tech was written in [BLISS](https://en.wikipedia.org/wiki/BLISS), a system programming language developed at [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), and in 1977 ported to [C](C "C"). Primary Author was [James Gillogly](James_Gillogly "James Gillogly") from Carnegie Mellon. [Hans Berliner](Hans_Berliner "Hans Berliner") helped in developing the positional analysis ([evaluation](Evaluation "Evaluation")). The basic idea of the Tech program is due in large part to [Allen Newell](Allen_Newell "Allen Newell"). In 1978 Gillogly wrote his Ph.D. Thesis about the performance analysis of Tech <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Tech competed at three [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), and was two times runner-up at [ACM 1971](ACM_1971 "ACM 1971") and [ACM 1972](ACM_1972 "ACM 1972"). 



### Contents


* [1 Quotes](#quotes)
	+ [1.1 Abstract](#abstract)
	+ [1.2 Chess and Technology](#chess-and-technology)
	+ [1.3 Acknowledgments](#acknowledgments)
* [2 Selected Games](#selected-games)
* [3 Tech 2](#tech-2)
* [4 Tech 3](#tech-3)
* [5 See also](#see-also)
* [6 Publications](#publications)
* [7 External Links](#external-links)
	+ [7.1 Chess Program](#chess-program)
	+ [7.2 Misc](#misc)
* [8 References](#references)






Quotes from *The Technology Chess Program* by [James Gillogly](James_Gillogly "James Gillogly") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### Abstract


A chess program has been developed which plays good chess (for a program) using a very simple structure. It is based on a [brute force search](Brute-Force "Brute-Force") of the move tree with no [forward pruning](Pruning "Pruning"), using [material](Material "Material") as the only terminal evaluation function, and using a limited positional analysis at the top level for a tiebreak between moves which are materially equal. Because of the transparent structure, this program is proposed as a technological [benchmark](Category:Benchmark "Category:Benchmark") for chess programs which will continue to improve as computer technology increases. 



### Chess and Technology


Until recently the main effort in chess programming has been to develop programs which selectively (and hopefully "intelligently") examine a small subset of the legal moves in any position. The surprising performance of the [Varian minicomputer](Daly_CP "Daly CP") (programmed by [K. King](Kenneth_L._King "Kenneth L. King") and [C. Daly](Chris_Daly "Chris Daly")) in the [First Annual Computer Chess Championship](ACM_1970 "ACM 1970") (New York 1970), although due primarily to good luck in the pairings, led to increased speculation about the possibility of playing respectable chess with an unselective "brute force" program. 



### Acknowledgments


I am indebted to [Hans Berliner](Hans_Berliner "Hans Berliner"), World Correspondence Chess Champion, who developed the elegant techniques used in the positional analysis, and whose patient discussion helped to clarify many of the conceptional problems. The basic idea of the Technology Program is due in large part to [Allen Newell](Allen_Newell "Allen Newell"). 



## Selected Games


[ACM 1971](ACM_1971 "ACM 1971"), round 3, [Coko 3](Coko "Coko") - Tech <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```

[Event "ACM 1971"]
[Site "Chicago USA"]
[Date "1971.08.04"]
[Round "3"]
[White "Coko 3"]
[Black "Tech"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d3 d5 5.Bxd5 Nxd5 6.exd5 Qxd5 7.Nc3 Bb4 8.O-O Bxc3 
9.bxc3 O-O 10.Ng5 Bf5 11.Rb1 f6 12.c4 Qc5 13.Nh3 Bxh3 14.Be3 Nd4 15.gxh3 Qc6 16.c3 
Nf3+ 17.Kh1 Nd2+ 18.f3 Nxf1 19.Qxf1 f5 20.Rb5 f4 21.Rc5 Qe6 22.Bc1 c6 23.d4 Rae8 
24.Rxe5 Qg6 25.Rxe8 Qxe8 26.Qf2 Qe6 27.Qf1 Rf5 28.h4 c5 29.d5 Qd6 30.Qh3 Qe5 31.Qf1 
Qxc3 32.d6 Qd4 33.Qe2 Qxd6 34.Qe8+ Rf8 35.Qa4 Rf5 36.Qe8+ Rf8 37.Qa4 Qe6 38.Qb3 Qe2 
39.h3 Rd8 40.Bxf4 Rd1+ 0-1

```





## Tech 2


[MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")-student [Alan Baisley](Alan_Baisley "Alan Baisley"), who already contributed as chess expert and [opening book-author](Category:Opening_Book_Author "Category:Opening Book Author"), implemented **Tech 2** in [assembly](Assembly "Assembly") language on a [PDP-10](PDP-10 "PDP-10") and gained about 25% in speed over the BLISS version on the same machine <a id="cite-note-5" href="#cite-ref-5">[5]</a>. *Tech 2* competed at the [1st World Computer Chess Championship](WCCC_1974 "WCCC 1974") in Stockholm 1974 and became fifth with two wins and losses against [Kaissa](Kaissa "Kaissa") and [Chess 4.0](Chess_(Program) "Chess (Program)") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, placed second at the [ACM 1973](ACM_1973 "ACM 1973"), and further played the [ACM 1974](ACM_1974 "ACM 1974") <a id="cite-note-7" href="#cite-ref-7">[7]</a> .




## Tech 3


**Tech 3** was an own program in the spirit of Tech by [Alexander Szabo](Alexander_Szabo "Alexander Szabo") as subject of his Masters thesis at [University of British Columbia](https://en.wikipedia.org/wiki/University_of_British_Columbia) in 1984. Tech 3 performed a [brute force](Brute-Force "Brute-Force") [alpha-beta search](Alpha-Beta "Alpha-Beta") with [quiescence](Quiescence_Search "Quiescence Search") and [iterative deepening](Iterative_Deepening "Iterative Deepening") with [aspiration windows](Aspiration_Windows "Aspiration Windows") , using a [transposition table](Transposition_Table "Transposition Table") with [Zobrist hashing](Zobrist_Hashing "Zobrist Hashing"), and still the rudimentary [evaluation](Evaluation "Evaluation") only based on [material balance](Material "Material"). Tech 3 was written in [Fortran](Fortran "Fortran") and [IBM 370](IBM_370 "IBM 370") [Assembly](Assembly "Assembly") to run on a [Amdahl 470V/8](Amdahl_470 "Amdahl 470"), the source code listing is given in Appendix 1 of the thesis <a id="cite-note-8" href="#cite-ref-8">[8]</a>. 



## See also


* [Brute-Force](Brute-Force "Brute-Force")
* [Daly CP](Daly_CP "Daly CP")
* [HiTech](HiTech "HiTech")
* [MAX](MAX_(Gillogly) "MAX (Gillogly)")
* [StarTech](StarTech "StarTech")
* [The Technology Curve](Alexander_Szabo#TechnologyCurve "Alexander Szabo")
* [Type A Strategy](Type_A_Strategy "Type A Strategy")


## Publications


* [James Gillogly](James_Gillogly "James Gillogly") (**1971**). *[The Technology Chess Program](http://oai.dtic.mil/oai/oai?verb=getRecord&metadataPrefix=html&identifier=AD0736043)*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), CS-71-109, [pdf](http://repository.cmu.edu/cgi/viewcontent.cgi?article=2974&context=compsci)
* [James Gillogly](James_Gillogly "James Gillogly") (**1972**). *[The Technology Chess Program](http://www.sciencedirect.com/science/article/pii/0004370272900458)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 3, pp. 145-163, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Paul Rushton](Paul_Rushton "Paul Rushton"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1973**). *Current Chess Programs: A Summary of their Potential and Limitations*. INFOR Journal of the Canadian Information Processing Society Vol. 11, No. 1, [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Rushton-Marsland-Feb73.pdf)
* [James Gillogly](James_Gillogly "James Gillogly") (**1978**). *Performance Analysis of the Technology Chess Program*. Ph.D. Thesis. Tech. Report CMU-CS-78-189, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [CMU-CS-77 pdf](http://reports-archive.adm.cs.cmu.edu/anon/anon/usr/ftp/scan/CMU-CS-77-gillogly.pdf)
* [Alexander Szabo](Alexander_Szabo "Alexander Szabo") (**1984**). *[Computer-Chess Tactics and Strategy](https://circle.ubc.ca/handle/2429/24780)*. M.Sc. Thesis, [University of British Columbia](https://en.wikipedia.org/wiki/University_of_British_Columbia)


## External Links


### Chess Program


* [Tech's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=44)
* [its/src/rg at master · PDP-10/its · GitHub](https://github.com/PDP-10/its/tree/master/src/rg) (Tech 2 source code) maintained by [Lars Brinkhoff](User:Larsbrinkhoff "User:Larsbrinkhoff") and [Eric Swenson](https://github.com/eswenson1)
* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-9" href="#cite-ref-9">[9]</a>


### Misc


* [Tech from Wikipedia](https://en.wikipedia.org/wiki/Tech)
* [Technology (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Technology_%28disambiguation%29)
* [Technology from Wikipedia](https://en.wikipedia.org/wiki/Technology)
* [Portal:Technology from Wikipedia](https://en.wikipedia.org/wiki/Portal:Technology)
* [Technological singularity from Wikipedia](https://en.wikipedia.org/wiki/Technological_singularity)
* [Techno from Wikipedia](https://en.wikipedia.org/wiki/Techno)
* [Technophilia from Wikipedia](https://en.wikipedia.org/wiki/Technophilia)
* [All pages with prefix technology from Wikipedia](https://en.wikipedia.org/wiki/Special:PrefixIndex/technology)
* [Jan Klare's](Category:Jan_Klare "Category:Jan Klare") [The Dorf](Category:The_Dorf "Category:The Dorf") - Technoid, [Kulturgut Haus Nottbeck](https://de.wikipedia.org/wiki/Museum_f%C3%BCr_Westf%C3%A4lische_Literatur_Haus_Nottbeck), [Oelde](https://en.wikipedia.org/wiki/Oelde), September 24, 2016, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Terracotta artwork](https://en.wikipedia.org/wiki/Ceramic_art#Terracotta_.28artworks.29) by [Gerhard Hahn](index.php?title=Category:Gerhard_Hahn&action=edit&redlink=1 "Category:Gerhard Hahn (page does not exist)"), from the [Technophilia](https://www.lwl.org/industriemuseum/standorte/henrichshuette-hattingen/sonderausstellung/technophilia) art exhibition at [Henrichshütte Ironworks - Museum of iron and steel](Category:Henrichsh%C3%BCtte "Category:Henrichshütte"), [Hattingen](https://en.wikipedia.org/wiki/Hattingen), [North Rhine-Westphalia](https://en.wikipedia.org/wiki/North_Rhine-Westphalia), [Germany](https://en.wikipedia.org/wiki/Germany), part of [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail") of the [Ruhr area](https://en.wikipedia.org/wiki/Ruhr), Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), October 01, 2016
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [James Gillogly](James_Gillogly "James Gillogly") (**1978**). *Performance Analysis of the Technology Chess Program*. Ph.D. Thesis. Tech. Report CMU-CS-78-189, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [CMU-CS-77 pdf](http://reports-archive.adm.cs.cmu.edu/anon/anon/usr/ftp/scan/CMU-CS-77-gillogly.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [James Gillogly](James_Gillogly "James Gillogly") (**1972**). *[The Technology Chess Program](http://www.sciencedirect.com/science/article/pii/0004370272900458)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 3, pp. 145-163, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [PGN Download NACCC](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=60&Itemid=26&lang=en), [CSVN](CSVN "CSVN") site
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [James Gillogly](James_Gillogly "James Gillogly") (**1978**). *Performance Analysis of the Technology Chess Program*. Ph.D. Thesis. Tech. Report CMU-CS-78-189, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [CMU-CS-77 pdf](http://reports-archive.adm.cs.cmu.edu/anon/anon/usr/ftp/scan/CMU-CS-77-gillogly.pdf)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Tech's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=44)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [The eleventh ACM's North American Computer Chess Championship, Nashville, Tennessee October 26-28, 1980](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cdeeb), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.1980_11th_ACM_NACCC/The_Eleventh_ACMs_North_American_Computer_Chess_Championship.1980.062303015.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), see History of ACM events pg 11
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Alexander Szabo](Alexander_Szabo "Alexander Szabo") (**1984**). *[Computer-Chess Tactics and Strategy](https://circle.ubc.ca/handle/2429/24780)*. M.Sc. Thesis, [University of British Columbia](https://en.wikipedia.org/wiki/University_of_British_Columbia)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one Level](Engines "Engines")**







 
