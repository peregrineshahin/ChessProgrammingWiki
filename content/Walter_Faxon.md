---
title: Walter Faxon
---
**[Home](Home "Home") \* [People](People "People") \* Walter Faxon**


**Walter G. Faxon**,  

an American chess player, computer scientist, and [bit scan](BitScan "BitScan") pioneer. His [magic bitscan](BitScan#WalterFaxonsmagicBitscan "BitScan"), invented in the 80s is still one of the most competitive on 32-bit architectures . On June 09, 2003 Walter made a thought-provoking [appeal](#appeal) in [CCC](CCC "CCC"). 



## Magic BitScan


Walter Faxon's 32-bit friendly [magic bitscan](BitScan#WalterFaxonsmagicBitscan "BitScan") <a id="cite-note-2" href="#cite-ref-2">[2]</a> uses a fast none minimal [perfect hashing](Hash_Table#PerfectHashing "Hash Table") function:




```C++
const char LSB_64_table[154] =
{
##define __ 0
   22,__,__,__,30,__,__,38,18,__, 16,15,17,__,46, 9,19, 8, 7,10,
   0, 63, 1,56,55,57, 2,11,__,58, __,__,20,__, 3,__,__,59,__,__,
   __,__,__,12,__,__,__,__,__,__, 4,__,__,60,__,__,__,__,__,__,
   __,__,__,__,21,__,__,__,29,__, __,37,__,__,__,13,__,__,45,__,
   __,__, 5,__,__,61,__,__,__,53, __,__,__,__,__,__,__,__,__,__,
   28,__,__,36,__,__,__,__,__,__, 44,__,__,__,__,__,27,__,__,35,
   __,52,__,__,26,__,43,34,25,23, 24,33,31,32,42,39,40,51,41,14,
   __,49,47,48,__,50, 6,__,__,62, __,__,__,54
##undef __
};

/**
 * bitScanForward
 * @author Walter Faxon, slightly modified
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of least significant one bit
 */
int bitScanForward(U64 bb)
{
   unsigned int t32;
   assert(bb);
   bb  ^= bb - 1;
   t32  = (int)bb ^ (int)(bb >> 32);
   t32 ^= 0x01C5FC81;
   t32 +=  t32 >> 16;
   t32 -= (t32 >> 8) + 51;
   return LSB_64_table [t32 & 255]; // 0..63
}

```





## Appeal


<a id="cite-note-3" href="#cite-ref-3">[3]</a>




```C++Musings on nonstandard computer chess techniques.

```


```C++What's new on the computer chess front? I note that [Sergei S. Markoff's](Sergei_Markoff "Sergei Markoff") new program [SmarThink](SmarThink "SmarThink") (http:*www.aigroup.narod.ru/detailse.htm) is supposed to use (among many other things) some of former world chess champion [M.M. Botvinnik's](Mikhail_Botvinnik "Mikhail Botvinnik") ideas. Botvinnik's "Computers, Chess and Long-Range Planning" (Springer, 1970) and "Chess: Solving Inexact Search Problems" (Springer, 1983) described a method that apparently only Botvinnik's programmer/protege [Boris Stilman](Boris_Stilman "Boris Stilman") believed would work, which Stilman later generalized in his own book "Linguistic Geometry: From Search to Construction" (Kluwer, 2000). Markoff's own on-line writings on chess algorithms (http:*www.aigroup.narod.ru/indexe.htm) are only in Russian, so far. (I am assuming that the SmarThink download doesn't include source.)

```


```C++Markoff also writes that his first program included ideas from the authors of [Kaissa](Kaissa "Kaissa"). Those authors published papers in the 1970's on "the method of analogies" to reduce search work, but they did not use it in their competitive program. If you recall, [Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") wrote in "Behind Deep Blue" (Princeton Univ. Pr., 2002) that he had implemented a stripped-down version of the analogies method for [Deep Blue](Deep_Blue "Deep Blue"). It is the unpublished intellectual property of IBM.

```


```C++Sometimes I wonder if chess program authors mention intriguing nonsense just to throw their competitors off the track. I recall someone once letting slip that he had used Botvinnik's method for an early hardware-limited microcomputer program. That seems unlikely. Nearly 15 years ago an author ([Kittinger](David_Kittinger "David Kittinger")?) dropped hints that he had adopted [McAllester's](David_McAllester "David McAllester") 1988 method [conspiracy numbersearch](Conspiracy_Number_Search "Conspiracy Number Search") (aka conspiracy search) for his program, using the term "nodulation". Published results indicate that plain conspiracy numbers don't work very well for chess. As far as I know, today only experiments on multiprocessor machines are being conducted; no competitive microcomputer program uses it at all. So was it a mirage -- or a trick? David McAllester and [Deniz Yuret](Deniz_Yuret "Deniz Yuret") did finally publish their revised work ([Alpha-Beta Conspiracy Search](index.php?title=Alpha-Beta_Conspiracy_Search&action=edit&redlink=1 "Alpha-Beta Conspiracy Search (page does not exist)"). [ICGA Journal](ICGA_Journal "ICGA Journal"), Vol. 25, No. 1 (March 2002), pp. 16-35), nearly ten years after their initial experiments with the multiprocessor program [Star-Socrates](Star_Socrates "Star Socrates"). And ten years from now?...

```


```C++And what about [Berliner's](Hans_Berliner "Hans Berliner") [B\*](B* "B*") algorithm? (Actually [Palay's](Andrew_James_Palay "Andrew James Palay") probabilistic B* using a probability distribution for evaluation instead of a simple range, today suggestive that techniques from fuzzy logic might be applied.) The chess machine [Hitech](HiTech "HiTech") was originally built for it in the early 1980's (equal first on points but second on tiebreak, [WCCC 1986](WCCC_1986 "WCCC 1986")) -- and finally began using it. As of mid-1993 it was "almost as good as regular Hitech". In mid-1995 it was still "not quite as good as brute force searching." In the abstract of his last word on the subject (Hans J. Berliner and [Chris McConnell](Chris_McConnell "Chris McConnell"). B* probability based search. Artificial Intelligence, Volume 86, Issue 1, September 1996, Pages 97-156) Berliner writes, "Analysis of the data indicates that should additional power become available, the B* technique will scale up considerably better than brute-force techniques." Berliner is now retired. More power is available. Where are the later papers? Where is B* today?

```


```C++My suggestion: you are writing a chess program. Go ahead, put in [negascout](NegaScout "NegaScout"), [null-move pruning](Null_Move_Pruning "Null Move Pruning"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), everything everybody is already doing. Then, look to the literature and find some method that everybody is _not_ doing. Implement it, experiment with it, and _publish_ your results. Please.

```


```C++- Walter 

```

## No Go


(was Re: Markoff -- Botvinnik -- Kaissa -- Hsu -- ABC -- Berliner) <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```C++ ... I have been from time-to-time disappointed that there is not more AI content on CCC. It very much seems to be a hobbyist board, playing with the current programs and building duplicates of them, albeit with minor differences in emphasis and implementation. I've been guilty of this myself in the bitscan threads. But the few times I have tried to raise the level of discussion have been met with, mostly, silence. My last post was to an extent, a "last gasp". 

```

## Forum Posts


### 2002 ...


* [Another hacky method for bitboard bit extraction](https://www.stmintz.com/ccc/index.php?id=265635) by Walter Faxon, [CCC](CCC "CCC"), November 17, 2002
* [Re: Bit Scan Timings -- possible artifact?](https://www.stmintz.com/ccc/index.php?id=272454) by Walter Faxon, [CCC](CCC "CCC"), December 22, 2002
* [Re: Beating Bitscan to Death -- yet again](https://www.stmintz.com/ccc/index.php?id=273932) by Walter Faxon, [CCC](CCC "CCC"), December 30, 2002
* [Re: Computer Chess Went The Wrong Way...](https://www.stmintz.com/ccc/index.php?id=275418) by Walter Faxon, [CCC](CCC "CCC"), January 07, 2003
* [Markoff - Botvinnik - Kaissa - Hsu - ABC - Berliner](https://www.stmintz.com/ccc/index.php?id=299987) by Walter Faxon, [CCC](CCC "CCC"), June 09, 2003
* [65 bits!](https://www.stmintz.com/ccc/index.php?id=322847) by Walter Faxon, [CCC](CCC "CCC"), October 21, 2003


### 2005 ...


* [Steven Edwards & Symbolic](https://www.stmintz.com/ccc/index.php?id=407324) by Walter Faxon, [CCC](CCC "CCC"), January 24, 2005 » [Symbolic](Symbolic "Symbolic")
* [Old chess program in BASIC (long post)](https://www.stmintz.com/ccc/index.php?id=417664) by Walter Faxon, [CCC](CCC "CCC"), March 20, 2005 » [Basic](Basic "Basic")
* [What do you do in "hard" positions?](https://www.stmintz.com/ccc/index.php?id=419898) by Walter Faxon, [CCC](CCC "CCC"), April 06, 2005
* [Quantum computing and chess](https://www.stmintz.com/ccc/index.php?id=420763) by Walter Faxon, [CCC](CCC "CCC"), April 13, 2005
* [(Obvious troll) Kasparov vs DB-I was a disaster for human chess](https://www.stmintz.com/ccc/index.php?id=424608) by Walter Faxon, [CCC](CCC "CCC"), May 06, 2005 » [Deep Blue](Deep_Blue "Deep Blue")


## External Links


* [The chess games of Walter G Faxon](http://www.chessgames.com/perl/chessplayer?pid=153699) from [chessgames.com](http://www.chessgames.com/index.html)
* [US Open 1970, Boston](http://www.chessgames.com/perl/chesscollection?cid=1020934), [chessgames.com](http://www.chessgames.com/index.html)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chess](https://www.nytimes.com/1970/06/07/archives/chess-brookline-wins-high-school-event.html) by [Al Horowitz](https://en.wikipedia.org/wiki/Israel_Albert_Horowitz), [The New York Times](https://en.wikipedia.org/wiki/The_New_York_Times), June 7, 1970
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Another hacky method for bitboard bit extraction](https://www.stmintz.com/ccc/index.php?id=265635) by Walter Faxon, [CCC](CCC "CCC"), November 17, 2002
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Markoff - Botvinnik - Kaissa - Hsu - ABC - Berliner](https://www.stmintz.com/ccc/index.php?id=299987) by Walter Faxon, [CCC](CCC "CCC"), June 09, 2003
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [No Go (was Re: Markoff -- Botvinnik -- Kaissa -- Hsu -- ABC -- Berliner)](https://www.stmintz.com/ccc/index.php?id=300412) by Walter Faxon, [CCC](CCC "CCC"), June 11, 2003

**[Up one level](People "People")**







 
