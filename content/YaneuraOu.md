---
title: YaneuraOu
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* YaneuraOu**


**YaneuraOu**, (やねうら王, Yaneura King)  

an [USI](USI "USI") compliant [open source](Category:Open_Source "Category:Open Source") [Shogi](Shogi "Shogi") engine as well a in 2016 [CSA](CSA "CSA") registered Shogi [search](Search "Search") library by [Motohiro Isozaki](Motohiro_Isozaki "Motohiro Isozaki") aka Yaneurao, written in [C++](Cpp "Cpp"), licensed under the [GPL 3.0](Free_Software_Foundation#GPL "Free Software Foundation"). YaneuraOu with **Otafuku Lab 2019** won the [WCSC29](index.php?title=WCSC29&action=edit&redlink=1 "WCSC29 (page does not exist)") in 2019 <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>, YaneuraOu was mentioned in the library column of many programs participating in the WCSC29, notably runner-up [Kristallweizen](Kristallweizen "Kristallweizen"), third placed [Tanu-King](index.php?title=Tanu-King&action=edit&redlink=1 "Tanu-King (page does not exist)"), and 14 others.



## Bitboards


9x9 Shogi [Bitboards](Bitboards "Bitboards") are defined as [array](Array "Array") of two [quad words](Quad_Word "Quad Word") and similar to [Apery](Apery#Bitboards "Apery"), as conditional compiled [union type](https://en.wikipedia.org/wiki/Union_type) with 128-bit type \_\_m128i, explicitly taking advantage of [SSE2](SSE2 "SSE2") instructions <a id="cite-note-5" href="#cite-ref-5">[5]</a>:




```C++

// Bitboard 本体クラス

struct alignas(16) Bitboard
{
##if defined (USE_SSE2)
	union
	{
		// 64bit each
		u64 p[2];

		// For handling with SSE
		// bit0 represents SQ_11, bit1 represents SQ_12,…, bit81 represents SQ_99.
		// This bit position corresponds to the Square type.
		// However, bit63 is unused. This is a hack to find the rook's advantage with one pext by leaving here.
		// Invented by the magic bitboard sect, including Apery.
		__m128i m;
	};
##else // no SSE
	u64 p[2];
##endif

```

## Forum Posts


* [The Stockfish of shogi](http://talkchess.com/forum3/viewtopic.php?t=72754) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 07, 2020


 [Re: The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754&start=1) by [Fabian Fichter](index.php?title=Fabian_Fichter&action=edit&redlink=1 "Fabian Fichter (page does not exist)"), [CCC](CCC "CCC"), January 07, 2020
## External Links


* [GitHub - yaneurao/YaneuraOu: YaneuraOu is the World's Strongest Shogi engine(AI player), WCSC29 1st winner , educational and USI compliant engine](https://github.com/yaneurao/YaneuraOu)
* [やねうら王 公式サイト | コンピューター将棋 やねうら王 公式サイト Yaneura Ou Official Website](http://yaneuraou.yaneu.com/) (Japanese)
* [やねうら王 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%84%E3%81%AD%E3%81%86%E3%82%89%E7%8E%8B) (Japanese)
* [やねうら王 (@yaneuraou) / Twitter](https://twitter.com/yaneuraou) (Japanese)
* [How to install Yaneuraou with third party evaluation files/opening books and Gikou2](https://www.uuunuuun.com/single-post/2017/12/09/how-to-install-yaneuraou-engine-with-third-party-evaluation-fileopening-book)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [第29回世界コンピュータ将棋選手権 29th World Computer Shogi Championship](http://www2.computer-shogi.org/wcsc29/)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [大阪のAI・人工知能開発に特化したシステム会社 | お多福ラボ | A system company specializing in AI / artificial intelligence development in Osaka | Otafuku Lab](https://otafuku-lab.co/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [How to install Yaneuraou with third party evaluation files/opening books and Gikou2](https://www.uuunuuun.com/single-post/2017/12/09/how-to-install-yaneuraou-engine-with-third-party-evaluation-fileopening-book)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [wcsc29/YaneuraOu/appeal.txt](https://www.apply.computer-shogi.org/wcsc29/appeal/YaneuraOu/appeal.txt)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [YaneuraOu/bitboard.h at master · yaneurao/YaneuraOu · GitHub](https://github.com/yaneurao/YaneuraOu/blob/master/source/bitboard.h)

**[Up one Level](Engines "Engines")**







 
