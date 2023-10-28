---
title: J. Biit
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* J. Biit**



[ Just Because it is there <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**J. Biit**,  

[Hans Berliner's](Hans_Berliner "Hans Berliner") first chess program, written in the late 60s in [PL/I](index.php?title=PL_1&action=edit&redlink=1 "PL 1 (page does not exist)") to ran on an [IBM System/360](IBM_360 "IBM 360") [mainframe computer](https://en.wikipedia.org/wiki/Mainframe_computer) <a id="cite-note-2" href="#cite-ref-2">[2]</a> . It played the [First United States Computer Chess Championship](ACM_1970 "ACM 1970") 1970 in [New York City](https://en.wikipedia.org/wiki/New_York_City), and won versus [Wita](Awit "Awit"), lost from [Chess 3.0](Chess_(Program) "Chess (Program)") and drew [Coko III](Coko "Coko"). 


Along with [Daly CP](Daly_CP "Daly CP"), J. Biit was one of the first chess programs operated through a [Graphical User Interface](GUI "GUI"). The UI was written at [Columbia University](Columbia_University "Columbia University") for the [IBM 2250 Display Unit](https://en.wikipedia.org/wiki/IBM_2250), and later evolved along with J. Biit to become the [Columbia Computer Chess Program](CCCP_(US) "CCCP (US)") dubbed CCCP <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### Contents


* [1 Etymology](#etymology)
* [2 Description](#description)
* [3 Quotes](#quotes)
* [4 Publications](#publications)
* [5 External Links](#external-links)
	+ [5.1 Chess Program](#chess-program)
	+ [5.2 Misc](#misc)
* [6 References](#references)






J. Biit is the acronym of "Just Because it is there", probably in dependance of the famous quote <a id="cite-note-4" href="#cite-ref-4">[4]</a> by English mountaineer [George Mallory](https://en.wikipedia.org/wiki/George_Mallory), having replied to the question "Why do you want to climb [Mount Everest](https://en.wikipedia.org/wiki/Mount_Everest)?". 



## Description


J. Biit was a selective search ([Shannon type B](Type_B_Strategy "Type B Strategy")) program <a id="cite-note-5" href="#cite-ref-5">[5]</a> that places considerable emphasis on chess knowledge and restricting the number of positions to be examined, as it scored only 30-100 positions during a search using [alpha-beta](Alpha-Beta "Alpha-Beta") and [incremental board updating](Incremental_Updates "Incremental Updates"). The program was developed in [PL/I](https://en.wikipedia.org/wiki/PL/I) on the [IBM 360/65](IBM_360 "IBM 360") at [CMU](Carnegie_Mellon_University "Carnegie Mellon University"), but was unable to use that system for the [1970 ACM tournament](ACM_1970 "ACM 1970"). Since the 360 line was supposedly compatable, Kenneth M. King <a id="cite-note-6" href="#cite-ref-6">[6]</a> offered the services of [Columbia's](Columbia_University "Columbia University") more powerful IBM 360/91. Unfortunately they discovered that it wasn't as compatable as expected and Berliner and assistants spent two rather frantic weeks making program changes. It used about 200 [Kibibyte](https://en.wikipedia.org/wiki/Kibibyte) of [memory](Memory "Memory") and was about 3500 PL/I statements. The program searches a very small tree. Berliner claimed that, on average, only 30 nodes were examined for a move that required 65 seconds of computation. It used a "[free form of search which terminated in quiescent positions](Quiescence_Search "Quiescence Search") ... (with) the only bound being the absolute depth limit of 14 ply." It searched two plies for begining and [middle games](Middlegame "Middlegame"), and 4 plies for [end games](Endgame "Endgame") .



## Quotes


[Hans Berliner](Hans_Berliner "Hans Berliner") in his Oral History, March 2005 <a id="cite-note-7" href="#cite-ref-7">[7]</a> :




```
And I wrote a program which actually played chess. And I did it in the way [Greenblatt](Richard_Greenblatt "Richard Greenblatt") said it ought to be done <a id="cite-note-8" href="#cite-ref-8">[8]</a>. It wasn’t anywhere’s near as good a [Greenblatt’s program](Mac_Hack "Mac Hack") and I wasn’t really a very good programmer obviously, since that was the first time I had written a program...

```


```
So it played. Let’s see, I’ve got to get the timeline right here. Now this was in 1970. Now in 1970 I had already left IBM. I left IBM in 1969, and went to [Carnegie Mellon](Carnegie_Mellon_University "Carnegie Mellon University") as a doctoral student.

```


```
And, of course, their attraction with [Newell](Allen_Newell "Allen Newell") and [Simon](Herbert_Simon "Herbert Simon") was they would like to find somebody to push their ideas further forward, and that was me. And so I had this program which, in retrospect, was pretty woesome. 

```

## Publications


* [Hans Berliner](Hans_Berliner "Hans Berliner") (**1970**). *Experiences Gained in Constructing and Testing a Chess Program*. [IEEE](IEEE "IEEE") Symposium System Science and Cybernetics, reprinted in [David Levy](David_Levy "David Levy") (ed.) (**1988**). *[Computer Games I](https://link.springer.com/book/10.1007/978-1-4613-8716-9)*.


## External Links


### Chess Program


* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-9" href="#cite-ref-9">[9]</a>


### Misc


* [Michael Hedges](Category:Michael_Hedges "Category:Michael Hedges") - Because It's There <a id="cite-note-10" href="#cite-ref-10">[10]</a>, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 July 1986 at the [Wolf Trap National Park for the Performing Arts](https://en.wikipedia.org/wiki/Wolf_Trap_National_Park_for_the_Performing_Arts) in [Vienna, Virginia](https://en.wikipedia.org/wiki/Vienna,_Virginia) 
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Everest from [Kala Patthar](https://en.wikipedia.org/wiki/Kala_Patthar) in [Nepal](https://en.wikipedia.org/wiki/Nepal), [Mount Everest from Wikipedia](https://en.wikipedia.org/wiki/Mount_Everest)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [George Atkinson](index.php?title=George_Atkinson&action=edit&redlink=1 "George Atkinson (page does not exist)") (**1998**). *[Chess and Machine Intuition](http://books.google.com/books?id=ZuTvVo4zo6oC&printsec=frontcover&dq=Chess+and+machine+intuition#v=onepage&q&f=false)*. (Intellect Ltd.) pp 61
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Recollections of CUCC 1968-70 -The CCCP Chess Program](http://www.columbia.edu/cu/computinghistory/elliott-frank.html#cccp)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [George Mallory - Because it is there - Wikiquote](http://en.wikiquote.org/wiki/George_Mallory)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Description based on [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [The IBM 7090](http://www.columbia.edu/cu/computinghistory/7090.html)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Oral History of Hans Berliner](http://www.computerhistory.org/chess/related_materials/oral-history/hans_berliner.oral_history.2005.102630824/index.php?iid=orl-43343bb768f00), Interviewed by: [Gardner Hendrie](http://www.computerhistory.org/trustee/gardner-hendrie), Recorded: March 7, 2005, [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/oral-history/hans_berliner.oral_history.2005.102630824/berliner.oral_history_transcript.2005.103630824.pdf), pp. 12-13
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *The Greenblatt Chess Program*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Naomi Uemura from Wikipedia](https://en.wikipedia.org/wiki/Naomi_Uemura)

**[Up one Level](Engines "Engines")**







 
