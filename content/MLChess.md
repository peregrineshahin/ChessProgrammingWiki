---
title: MLChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* MLChess**



 [](http://www.hpcalc.org/details.php?id=3067) MLChess [GUI](GUI "GUI") <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**MLChess**,  

[Peter Österlund's](Peter_%C3%96sterlund "Peter Österlund") [open source chess program](Category:Open_Source "Category:Open Source") for the [HP 48 series](https://en.wikipedia.org/wiki/HP_48_series) of [Graphing calculators](https://en.wikipedia.org/wiki/Graphing_calculator) with its 131×64 pixel [LCD](https://en.wikipedia.org/wiki/Liquid_crystal_display), released in 1995 under the [GNU GPL](Free_Software_Foundation#GPL "Free Software Foundation"). MLChess is written mainly in machine language aka [Saturn assembly](Assembly#HPSATURN "Assembly") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Initial [RPL](https://en.wikipedia.org/wiki/RPL_%28programming_language%29) routines were subsequently replaced by assembly code <a id="cite-note-3" href="#cite-ref-3">[3]</a> . 



### Contents


* [1 Description](#description)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
	+ [3.1 1995 ...](#1995-...)
	+ [3.2 2000 ...](#2000-...)
* [4 External Links](#external-links)
* [5 References](#references)






MLChess uses [negamax](Negamax "Negamax") [alpha-beta](Alpha-Beta "Alpha-Beta") with a [search depth](Depth "Depth") of 2, 3 or 4 [plies](Ply "Ply") for three different levels, [captures](Captures "Captures") are [extented](Capture_Extensions "Capture Extensions") up to 4 additional plies. 
The [evaluation](Evaluation "Evaluation") is based on a few heuristic rules, most are simplified versions of heuristics taken from [GNU Chess](GNU_Chess "GNU Chess"). On level 2, the program will always find a [mate-in-one](Checkmate "Checkmate"), and on level 3 the program will always avoid a mate-in-one by the opponent if it is possible <a id="cite-note-4" href="#cite-ref-4">[4]</a> .



## See also


* [HpChess](HpChess "HpChess")


## Forum Posts


### 1995 ...


* [MLChess V1.01](https://groups.google.com/d/msg/comp.sys.hp48/FWmYmytpmwg/R5mt8DCZlHcJ) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [comp.sys.hp48](https://groups.google.com/forum/#!forum/comp.sys.hp48), December 17, 1995
* [MLChess 1.04](https://groups.google.com/d/msg/comp.sys.hp48/zx0VIxwgpxs/yzGSUhQZLXAJ) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [comp.sys.hp48](https://groups.google.com/forum/#!forum/comp.sys.hp48), December 26, 1995
* [MLChess 1.06](https://groups.google.com/d/msg/comp.sys.hp48/NARPRs2EBEM/Uf-2vP7h9IIJ) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [comp.sys.hp48](https://groups.google.com/forum/#!forum/comp.sys.hp48), July 17, 1996
* [MLChess 1.07](https://groups.google.com/d/msg/comp.sys.hp48/tC6Nfzdoq8s/pS0nsVNR6D4J) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [comp.sys.hp48](https://groups.google.com/forum/#!forum/comp.sys.hp48), August 10, 1996
* [What and where is the BEST hp48 chess program?](https://groups.google.com/d/msg/comp.sys.hp48/4ZGmjGpEyDU/EGgupAvhkfIJ) by Chris Gotwalt, [comp.sys.hp48](https://groups.google.com/forum/#!forum/comp.sys.hp48), March 04, 1997
* [MLChess 1.09](https://groups.google.com/d/msg/comp.sys.hp48/hPZF-1AFo4E/0fb14iuzbjYJ) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [comp.sys.hp48](https://groups.google.com/forum/#!forum/comp.sys.hp48), May 08, 1999


### 2000 ...


* [MLChess V1.11 with experimental HP49 support](https://groups.google.com/d/msg/comp.sys.hp48/ZtVPbkjGZWs/IV06qlXTlvoJ) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [comp.sys.hp48](https://groups.google.com/forum/#!forum/comp.sys.hp48), March 12, 2000
* [Re: New pictures of HP Prime in hand](http://www.hpmuseum.org/cgi-sys/cgiwrap/hpmuseum/archv021.cgi?read=244965) by [Gerson W. Barbosa](http://www.hpmuseum.org/cgi-sys/cgiwrap/hpmuseum/archv021.cgi?contact=244971), [HP Forum Archive 21](http://www.hpmuseum.org/cgi-sys/cgiwrap/hpmuseum/archv021.cgi), June 13, 2013


## External Links


* [Peter Osterlund's homepage - MLChess](http://hem.bredband.net/petero2b/)


 [MLChess.txt V1.14](http://hem.bredband.net/petero2b/mlchess/MLChess.txt)
 [ChangeLog](http://hem.bredband.net/petero2b/mlchess/revision.txt)
* [Detailed information for MLChess](https://www.hpcalc.org/details/3067), Part of the [HP Calculator Archive](https://www.hpcalc.org/) © [Eric Rechlin](https://www.hpcalc.org/contact.php)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Image from [Detailed information for MLChess](http://www.hpcalc.org/details.php?id=3067), Part of the [HP Calculator Archive](http://www.hpcalc.org/) © [Eric Rechlin](http://www.hpcalc.org/contact.php)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Gilbert Fernandes](https://www.hpcalc.org/authors/706), [Eric Rechlin](https://www.hpcalc.org/authors/1) (**2005**). *[Introduction to Saturn Assembly Language](https://www.hpcalc.org/details/1693)*. Third edition, Part of the [HP Calculator Archive](https://www.hpcalc.org/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [MLChess 1.07](https://groups.google.com/d/msg/comp.sys.hp48/tC6Nfzdoq8s/pS0nsVNR6D4J) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [comp.sys.hp48](https://groups.google.com/forum/#!forum/comp.sys.hp48), August 10, 1996
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Description based on [MLChess.txt V1.14](http://hem.bredband.net/petero2b/mlchess/MLChess.txt)

**[Up one level](Engines "Engines")**







 
