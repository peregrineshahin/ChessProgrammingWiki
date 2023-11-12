---
title: Loop Program
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Loop**



[ [Tiger and Turtle](https://en.wikipedia.org/wiki/Tiger_and_Turtle_%E2%80%93_Magic_Mountain) - illuminated looping <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Loop**,  

an [UCI](UCI "UCI") compliant chess engine by [Fritz Reul](Fritz_Reul "Fritz Reul") with different [board representations](Board_Representation "Board Representation") for 32-bit and 64-bit platforms, at times commercial. Loop became subject of its author's Ph.D. thesis *New Architectures in Computer Chess* <a id="cite-note-2" href="#cite-ref-2">[2]</a> . Despite different board representation, both Loop versions presumably share same [search](Search "Search") and [evaluation](Evaluation "Evaluation") with similar features and weights. 



## 64-bit Loop


The [bitboard](Bitboards "Bitboards") based Loop applies [Magic Bitboards](Magic_Bitboards "Magic Bitboards") for [sliding piece attack generation](Sliding_Piece_Attacks "Sliding Piece Attacks"). Further, iterative [alpha-beta](Alpha-Beta "Alpha-Beta") bounded [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") was applied to *Loop Amsterdam* <a id="cite-note-6" href="#cite-ref-6">[6]</a> , also performing a [parallel search](Parallel_Search "Parallel Search") for a quad-core processor, which played a strong [WCCC 2007](WCCC_2007 "WCCC 2007") in [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam), and became Third, behind the later disqualified [Rybka](Rybka "Rybka"), and [Zappa](Zappa "Zappa") <a id="cite-note-7" href="#cite-ref-7">[7]</a>.


Fritz Reul on an essential reason of Loop's success in Amsterdam in his thesis <a id="cite-note-8" href="#cite-ref-8">[8]</a> :




```C++
A complete computer-chess architecture based on hash functions and magic multiplications for the examination of bitboards is implemented in the computerchess engine Loop Amsterdam. This engine was able to reach the 3rd place at the 15th World Computer-Chess Championship, Amsterdam (NL) 2007. An essential reason for the success of this 64-bit computer-chess engine was the use of highly sophisticated perfect hash functions and magic multipliers for the computation of compound bit-patterns (bitboards) via perfect hashing. 

```

## Evaluation


### Preliminary Considerations


Evaluation was only marginally covered in Reul's thesis. In *Preliminary Considerations* he mentioned discussions with [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") and [Tord Romstad](Tord_Romstad "Tord Romstad"), and the exchange of source codes <a id="cite-note-9" href="#cite-ref-9">[9]</a> :




```C++
This thesis also does not aim at the explicit consideration of known computer-chess architectures, such as [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards") <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a> or the [0x88](0x88 "0x88") representation <a id="cite-note-12" href="#cite-ref-12">[12]</a>. Many a reference used in this thesis is not available in a scientifically elaborate form. This includes personal conversations with programmers <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a>, and the **exchange of source codes** as well as discussions via email. In this way the contents of this thesis can be regarded to be on a state-of the-art level of the research and development in the field of the computer-chess architectures. 

```

### Fruit Evaluation Overlap


During the [ICGA Investigations](ICGA_Investigations "ICGA Investigations") concerning the [Rybka Controversy](Rybka_Controversy "Rybka Controversy") and [evaluation overlaps](Evaluation_Overlap "Evaluation Overlap"), 64-bit Loop was inspected by [Mark Watkins](Mark_Watkins "Mark Watkins") who found congruence with the evaluation of [Fruit 2.1](Fruit "Fruit") <a id="cite-note-16" href="#cite-ref-16">[16]</a> . As confirmed by [David Levy](David_Levy "David Levy") <a id="cite-note-17" href="#cite-ref-17">[17]</a>, the [ICGA](ICGA "ICGA") has received a complaint on Loop by Fruit author [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") and an investigation has been started about this case, as already mentioned by Watkins in August 2011 <a id="cite-note-18" href="#cite-ref-18">[18]</a> .




## Complaints


[ICGA](ICGA "ICGA") President [David Levy](David_Levy "David Levy"), May 09, 2014 <a id="cite-note-19" href="#cite-ref-19">[19]</a>




```C++
The ICGA has received formal complaints against the Chess programs LOOP and [THINKER](Thinker "Thinker"), both of which have participated in the World Computer Chess Championship. LOOP was entered by Fritz Reul into the [2007 WCCC](WCCC_2007 "WCCC 2007") in Amsterdam. THINKER was entered into the [2010 WCCC](WCCC_2010 "WCCC 2010") in Kanazawa.
...
Here we present extracts from the first section of each of [Mark Watkins](Mark_Watkins "Mark Watkins") reports.

```


```C++
**Loop**  “The version examined here is Loop 2007 (64-bit), which was released at approximately the same time as the WCCC. There is notable similarity to Fruit in the evaluation function (other components were not examined).”
...
Based on the above mentioned reports by Mark Watkins the ICGA is convinced that, at the very least, both Fritz Reul and [Kerwin Medina](Kerwin_Medina "Kerwin Medina") have a case to answer. Depending on how Reul and/or Medina respond to these allegations the ICGA might decide to conduct further investigations and/or take some form of strong sanctioning action against the programmers.  However, the ICGA does not intend to proceed further along the route to strong sanctions for the time being, in order to give these programmers more time in which to make contact with the ICGA President and present their defence to the allegations. If either or both of these programmers fail to do so by December 31st 2014, or refuses to do so, the ICGA will disqualify them from all their results in ICGA events.  In the meantime the ICGA has decided to suspend both Fritz Reul and Kerwin Medina from participation in all ICGA events until such time as they have made contact and offered a defence. 

```

## See also


* [Coiled](Coiled "Coiled")
* [Iteration](Iteration "Iteration")
* [Iterative Search](Iterative_Search "Iterative Search")
* [List](List_(Program) "List (Program)")
* [Wii Chess](Wii_Chess "Wii Chess")


## Publications


* [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. thesis, [pdf](https://pure.uvt.nl/ws/portalfiles/portal/1098572/Proefschrift_Fritz_Reul_170609.pdf)
* [Fritz Reul](Fritz_Reul "Fritz Reul") (**2010**). *Static Exchange Evaluation with αβ-Approach*. [ICGA Journal, Vol. 33, No. 1](ICGA_Journal#33_1 "ICGA Journal")


## Forum Posts


### 2005 ...


* [Loop List available soon](https://www.stmintz.com/ccc/index.php?id=455003) by [Fritz Reul](Fritz_Reul "Fritz Reul"), [CCC](CCC "CCC"), October 11, 2005


 [Re: Loop List commercially available soon](https://www.stmintz.com/ccc/index.php?id=455043) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), October 11, 2005
* [Loop 13.6 soon available](http://www.talkchess.com/forum/viewtopic.php?t=13270) by [Gerhard Sonnabend](index.php?title=Gerhard_Sonnabend&action=edit&redlink=1 "Gerhard Sonnabend (page does not exist)"), [CCC](CCC "CCC"), April 20, 2007
* [doing undoing](http://www.talkchess.com/forum/viewtopic.php?t=13764) by [Fritz Reul](Fritz_Reul "Fritz Reul"), [CCC](CCC "CCC"), May 14, 2007
* [Iterative DTS](http://www.talkchess.com/forum/viewtopic.php?t=14832) by [Fritz Reul](Fritz_Reul "Fritz Reul"), [CCC](CCC "CCC"), July 02, 2007
* [Re: Bob Hyatt says that...](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=213390&t=23375) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), August 29, 2008
* [Re: Bob Hyatt says that...](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=213593&t=23375) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), August 30, 2008


### 2010 ...


* [Loop 2007 / Fruit 2.1](http://www.open-chess.org/viewtopic.php?f=5&t=1353) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 18, 2011 » [Fruit](Fruit "Fruit")
* [Loop as a Fruit clone](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=27681) by [Rebel](Ed_Schroder "Ed Schroder"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), September 20, 2013
* [Complaints against the Chess programs LOOP and THINKER](http://hiarcs.net/forums/viewtopic.php?t=6707) by [Harvey Williamson](Harvey_Williamson "Harvey Williamson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), May 12, 2014
* [Complaints against the Chess programs LOOP and THINKER](http://www.talkchess.com/forum/viewtopic.php?t=52325) by [Harvey Williamson](Harvey_Williamson "Harvey Williamson"), [CCC](CCC "CCC"), May 14, 2014


### 2015 ...


* [Re: FIDE Rules on ICGA - Rybka controversy](http://www.open-chess.org/viewtopic.php?f=3&t=2808&start=81) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), May 08, 2015


## External Links


### Chess Engine


* [Loop Computer Chess](https://www.loopchess.com/)
* [List's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=123) (covers Loop)
* [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
* [Loop](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Loop-List&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/40](CCRL "CCRL")
* [Wii Chess from Wikipedia](https://en.wikipedia.org/wiki/Wii_Chess)
* [ICGA/Rybka controversy: Feedback - Allegations against another Chess Engine – The LOOP Program](https://en.chessbase.com/post/icga-rybka-controversy-feedback) by [David Levy](David_Levy "David Levy"), [ChessBase News](ChessBase "ChessBase"), February 17, 2012
* [Allegations against two more Chess Engines – The LOOP Program](https://icga.org/?p=354) by [David Levy](David_Levy "David Levy"), [ICGA](ICGA "ICGA") president, May 22, 2012 » [Thinker](Thinker "Thinker")
* [Complaints against the Chess programs LOOP and THINKER](https://icga.org/?p=919) by [David Levy](David_Levy "David Levy"), [ICGA](ICGA "ICGA") President, May 9, 2014


### Misc


* [Loop disambiguation page from Wikipedia](https://en.wikipedia.org/wiki/Loop)
* [The Loop disambiguation page from Wikipedia](https://en.wikipedia.org/wiki/The_Loop)
* [Looping disambiguation page from Wikipedia](https://en.wikipedia.org/wiki/Looping)
* [Loop control flow from Wikipedia](https://en.wikipedia.org/wiki/Control_flow#Loops)


 [For loop](https://en.wikipedia.org/wiki/For_loop)
 [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
 [While loop](https://en.wikipedia.org/wiki/While_loop)
 [Do while loop](https://en.wikipedia.org/wiki/Do_while_loop)
 [Infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)
* [Dirty Loops](https://en.wikipedia.org/wiki/Dirty_Loops) - Songs for Lovers - Coffee Break is over, Guitar cover with [Sandeep Mohan](Category:Sandeep_Mohan "Category:Sandeep Mohan"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Tiger and Turtle – Magic Mountain](https://en.wikipedia.org/wiki/Tiger_and_Turtle_%E2%80%93_Magic_Mountain) is a monument in the [Angerpark](https://de.wikipedia.org/wiki/Angerpark) in [Duisburg](https://en.wikipedia.org/wiki/Duisburg), Germany. Here you see its illuminated looping at night, [Image](https://commons.wikimedia.org/wiki/File:Tigerandturtle.jpg) by Kleunam, November 18, 2011, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), [Category:Tiger and Turtle – Magic Mountain](https://commons.wikimedia.org/wiki/Category:Tiger_and_Turtle_%E2%80%93_Magic_Mountain), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. thesis
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 2.2.2 Nintendo Wii Chess, pp. 11
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 2.2.1 The Chess Machine Hydra, pp. 11
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 5.1.1 Non-Bitboard Architectures, pp. 96
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2010**). *Static Exchange Evaluation with αβ-Approach*. [ICGA Journal, Vol. 33, No. 1](ICGA_Journal#33_1 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [15th World Computer Chess Championship - Amsterdam 2007 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/tournament.php?id=173)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 5.1.2 Magic Hash Functions for Bitboards, pp. 97
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 1.2 Preliminary Considerations, pp. 3-4
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft") (**1984**). *Bitmap move generation in Chess*. [ICCA Journal, Vol. 7, No. 3](ICGA_Journal#7_3 "ICGA Journal")
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Rotated Bitmaps, a New Twist on an Old Idea](http://www.cis.uab.edu/hyatt/bitmaps.html)*. [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [0x88 Move Generation](http://web.archive.org/web/20070716111804/www.brucemo.com/compchess/programming/0x88.htm) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland")
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**2006**). *Discussion with Dr. Christian Donninger*.
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") (**2006**). *Personal discussion with Fabien Letouzey*.
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [Tord Romstad](Tord_Romstad "Tord Romstad") (**2007**). *Discussion with Tord Romstad*.
16. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [Loop 2007 / Fruit 2.1](http://www.open-chess.org/viewtopic.php?f=5&t=1353) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 18, 2011
17. <a id="cite-ref-17" href="#cite-note-17">[17]</a> [ICGA/Rybka controversy: Feedback - Allegations against another Chess Engine – The LOOP Program](https://en.chessbase.com/post/icga-rybka-controversy-feedback) by [David Levy](David_Levy "David Levy"), [ChessBase News](ChessBase "ChessBase"), February 17, 2012
18. <a id="cite-ref-18" href="#cite-note-18">[18]</a> [Re: Loop 2007 / Fruit 2.1](http://www.open-chess.org/viewtopic.php?f=5&t=1353#p13794) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 22, 2011
19. <a id="cite-ref-19" href="#cite-note-19">[19]</a> [Complaints against the Chess programs LOOP and THINKER](https://icga.org/?p=919) by [David Levy](David_Levy "David Levy"), [ICGA](ICGA "ICGA") President, May 9, 2014

**[Up one level](Engines "Engines")**







 
