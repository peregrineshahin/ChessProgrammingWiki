---
title: Typhoon
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Typhoon**



[ [Typhoon Mike](https://en.wikipedia.org/wiki/Typhoon_Mike) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Typhoon**,  

an [open source chess engine](Category:Open_Source "Category:Open Source") by [Scott Gasch](Scott_Gasch "Scott Gasch"), as successor of [Monsoon](Monsoon "Monsoon") also written in [C](C "C") and compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). 



## Parallel Search


While running on a multi-processor machine, Typhoon uses a tree splitting algorithm somewhat similar to [principal variation splitting](Parallel_Search#PrincipalVariationSplitting "Parallel Search") to [search in parallel](Parallel_Search "Parallel Search") with multiple [threads](Thread "Thread"). 
Splitting occurs after the first move has been searched at [PV-nodes](Node_Types#PV "Node Types") or if the first N moves at [All-nodes](Node_Types#ALL "Node Types") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



## See also


* [Monsoon](Monsoon "Monsoon")


## Forum Posts


* [For Jim Ablett, about problems with new Typhoon builds](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5221) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 19, 2006
* [Typhoon chess engine bug & bugfix](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51322) by [Daniel Uranga](Daniel_Uranga "Daniel Uranga"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 18, 2010


## External Links


### Chess Engine


* [Monsoon/Typhoon Homepage](https://wannabe.guru.org/scott/hobbies/chess/)
* [Typhoon Chess Engine](https://wannabe.guru.org/scott/hobbies/chess/typhoon.html)
* [typhoon - Revision 359: /trunk](https://wannabe.guru.org/svn/typhoon/trunk/)
* [Index of /chess/engines/Jim Ablett/TYPHOON](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/TYPHOON/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Typhoon](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Typhoon&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


### Misc


* [Typhoon from Wikipedia](https://en.wikipedia.org/wiki/Typhoon)


 [Pacific typhoon season](https://en.wikipedia.org/wiki/Pacific_typhoon_season)
* [Typhoon](https://en.wikipedia.org/wiki/Typhoon_%28American_band%29) - Artificial Light, Live At [The Crystal Ballroom](https://en.wikipedia.org/wiki/Crystal_Ballroom_%28Portland,_Oregon%29), November 29, 2013, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Super Typhoon Mike at peak intensity on November 11, 1990 at 2221 UTC. [This image](https://commons.wikimedia.org/wiki/File:Typhoon_Mike_11_nov_1990_2221Z.jpg) was produced from data from NOAA-10, provided by [NOAA](https://en.wikipedia.org/wiki/National_Oceanic_and_Atmospheric_Administration), [Typhoons in the Philippines](https://en.wikipedia.org/wiki/Typhoons_in_the_Philippines) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Monsoon/Typhoon Homepage - Miscellanious](https://wannabe.guru.org/scott/hobbies/chess/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [recogn.c | Copyright (c) Scott Gasch](https://wannabe.guru.org/svn/typhoon/trunk/recogn.c)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [search.c | Copyright (c) Scott Gasch](https://wannabe.guru.org/svn/typhoon/trunk/search.c)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [split.c | Copyright (c) Scott Gasch](https://wannabe.guru.org/svn/typhoon/trunk/split.c)

**[Up one level](Engines "Engines")**







 
