---
title: DiscoCheck
---
**[Home](Home "Home") * [Engines](Engines "Engines") * DiscoCheck**

\[ Disco ball <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**DiscoCheck**, (former DoubleCheck)

a free [open source engine](Category:Open_Source "Category:Open Source") by Lucas Braesch, released under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), written in [C++](Cpp "Cpp").
DiscoCheck is [UCI](UCI "UCI") compatible and can be compiled for [Linux](Linux "Linux"), [Android](Android "Android") <a id="cite-note-2" href="#cite-ref-2">[2]</a> , [Windows](Windows "Windows"), and [Mac OS X](Mac_OS "Mac OS").
It performs [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), [LMR](Late_Move_Reductions "Late Move Reductions") and various enhancements inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows").
DiscoCheck determines [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") with [magic bitboards](Magic_Bitboards "Magic Bitboards"), first using [Pradu Kannan's](Pradu_Kannan "Pradu Kannan") implementation, later the GPL conform version by [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković") as used in [MinkoChess](MinkoChess "MinkoChess") (then called Umko)
<a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Early versions used the author's own implementation of [rotated bitboards](Rotated_Bitboards "Rotated Bitboards"), adapted from his earlier engine [BibiChess 0.5](index.php?title=BibiChess&action=edit&redlink=1 "BibiChess (page does not exist)"). In June 2017, a new DiscoChess dubbed [Demolito](Demolito "Demolito") was announced, completely rewritten, featuring [SMP](Parallel_Search "Parallel Search") and [Chess960](Chess960 "Chess960") <a id="cite-note-4" href="#cite-ref-4">[4]</a>
<a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Contents

- [1 See also](#see-also)
- [2 Forum Posts](#forum-posts)
  - [2.1 DoubleCheck](#doublecheck)
  - [2.2 DiscoCheck](#discocheck)
- [3 External Links](#external-links)
  - [3.1 Chess Engine](#chess-engine)
  - [3.2 Misc](#misc)
- [4 References](#references)

## See also

- [BibiChess](index.php?title=BibiChess&action=edit&redlink=1 "BibiChess (page does not exist)")
- [Demolito](Demolito "Demolito")
- [Discovered Check](Discovered_Check "Discovered Check")
- [Double Check](Double_Check "Double Check")

## Forum Posts

## DoubleCheck

- [name for my new engine ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=39837) by Lucas Braesch, [CCC](CCC "CCC"), July 24, 2011
- [New chess engine - DoubleCheck 1.0 (Lucas Braesch)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=39884) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), July 28, 2011
- [DoubleCheck 1.0 for Windows](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=39913) by Lucas Braesch, [CCC](CCC "CCC"), July 30, 2011
- [DoubleCheck 1.2 is out](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=40031) by Lucas Braesch, [CCC](CCC "CCC"), August 11, 2011
- [DoubleCheck 1.3 issues](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=40131) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), August 21, 2011
- [DoubleCheck 2.0 is out](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=40988) by Lucas Braesch, [CCC](CCC "CCC"), November 03, 2011
- [DoubleCheck 2.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=41162) by Lucas Braesch, [CCC](CCC "CCC"), November 21, 2011
- [DoubleCheck 2.3 is out](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=41481) by Lucas Braesch, [CCC](CCC "CCC"), December 17, 2011
- [DoubleCheck 2.7](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=42815) by Lucas Braesch, [CCC](CCC "CCC"), March 10, 2012

## DiscoCheck

- [Discocheck "Boney M" is out](http://www.talkchess.com/forum/viewtopic.php?t=44225) by Lucas Braesch, [CCC](CCC "CCC"), June 28, 2012
- [DiscoCheck 4.0.0 (release candidate)](http://www.talkchess.com/forum/viewtopic.php?t=47009) by Lucas Braesch, [CCC](CCC "CCC"), January 27, 2013
- [DiscoCheck 4.1 released](http://www.talkchess.com/forum/viewtopic.php?t=47582) by Lucas Braesch, [CCC](CCC "CCC"), March 23, 2013
- [DiscoCheck 4.2](http://www.talkchess.com/forum/viewtopic.php?t=48071) by Lucas Braesch, [CCC](CCC "CCC"), May 21, 2013
- [DiscoCheck 4.3 is out](http://www.talkchess.com/forum/viewtopic.php?t=48638) by Lucas Braesch, [CCC](CCC "CCC"), July 14, 2013
- [DiscoCheck 5.0 released](http://www.talkchess.com/forum/viewtopic.php?t=49828) by Lucas Braesch, [CCC](CCC "CCC"), October 25, 2013
- [DiscoCheck 5.1](http://www.talkchess.com/forum/viewtopic.php?t=50380) by Lucas Braesch, [CCC](CCC "CCC"), December 08, 2013
- [DiscoCheck 5.2 released](http://www.talkchess.com/forum/viewtopic.php?t=50861) by Lucas Braesch, [CCC](CCC "CCC"), January 11, 2014
- [New DiscoCheck is cooking](http://www.talkchess.com/forum/viewtopic.php?t=64173) by Lucas Braesch, [CCC](CCC "CCC"), June 04, 2017
- [DiscoCheck performing 200+ ELO better on ONE machine ??](http://www.talkchess.com/forum3/viewtopic.php?t=65716) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), November 13, 2017

## External Links

## Chess Engine

- [Chess Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:chess_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Index of /chess/engines/Jim Ablett/DISCOCHECK](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/DISCOCHECK/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Index of /chess/engines/Jim Ablett/+++ LINUX ENGINES ++/64 BIT/discocheck](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/+++%20LINUX%20ENGINES%20++/64%20BIT/discocheck/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [DiscoCheck](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=DiscoCheck&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/15](CCRL "CCRL")

## Misc

- [Disco (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Disco_%28disambiguation%29)
- [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa") - [Disco Boy](https://en.wikipedia.org/wiki/Disco_Boy), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

lineup: [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa"), [Adrian Belew](Category:Adrian_Belew "Category:Adrian Belew"), [Tommy Mars](https://en.wikipedia.org/wiki/Tommy_Mars), [Peter Wolf](https://en.wikipedia.org/wiki/Peter_Wolf_%28producer%29), [Patrick O'Hearn](https://en.wikipedia.org/wiki/Patrick_O%27Hearn), [Terry Bozzio](Category:Terry_Bozzio "Category:Terry Bozzio"), [Ed Mann](https://en.wikipedia.org/wiki/Ed_Mann)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Disco ball](https://en.wikipedia.org/wiki/Disco_ball), [Image](https://commons.wikimedia.org/wiki/File:Disco_ball4.jpg) by [Sarah](https://www.flickr.com/people/8978957@N07?rb=1), February 24, 2010, [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [UCI and XBoard Engines for Android](http://www.aartbik.com/MISC/eng.html) maintained by [Aart Bik](Aart_Bik "Aart Bik")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Double/DiscoCheck](http://wbec-ridderkerk.nl/html/details1/DoubleCheck.html) from [WBEC Ridderkerk](WBEC "WBEC")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [New DiscoCheck is cooking](http://www.talkchess.com/forum/viewtopic.php?t=64173) by Lucas Braesch, [CCC](CCC "CCC"), June 04, 2017
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [GitHub - lucasart/Demolito: UCI Chess Engine](https://github.com/lucasart/Demolito)

**[Up one Level](Engines "Engines")**

