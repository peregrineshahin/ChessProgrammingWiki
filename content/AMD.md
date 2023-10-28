---
title: AMD
---
**[Home](Home "Home") * [Organizations](Organizations "Organizations") * AMD**

\[ AMD headquarters, [Sunnyvale, California](https://en.wikipedia.org/wiki/Sunnyvale,_California) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Advanced Micro Devices, Inc.** or **AMD**,

an American multinational [semiconductor](https://en.wikipedia.org/wiki/Semiconductor_industry) company based in [Sunnyvale, California](https://en.wikipedia.org/wiki/Sunnyvale,_California), and behind [Intel](Intel "Intel") the second-largest global supplier of microprocessors based on the [x86](X86 "X86") architecture and also one of the largest suppliers of [graphics processing](https://en.wikipedia.org/wiki/Graphics_processing_unit) units <a id="cite-note-2" href="#cite-ref-2">[2]</a> .
In 2003, AMD launched the [Athlon 64](https://en.wikipedia.org/wiki/Athlon_64) (Hammer, AMD64, K8) and pioneered the [x86-64](X86-64 "X86-64") instruction set. Until Intel introduced the [Core 2](https://en.wikipedia.org/wiki/Intel_Core_2) [microarchitecture](https://en.wikipedia.org/wiki/Microarchitecture) in 2006, AMD64 was the dominating architecture for computer chess in the 2000s. With the [Zen](<https://en.wikipedia.org/wiki/Zen_(microarchitecture)>) micro-architecture and the release of the [Ryzen](https://en.wikipedia.org/wiki/Ryzen) processor in early 2017, it seems that AMD can recover lost ground.
However, early Ryzens prior to [Zen 3](https://en.wikipedia.org/wiki/Zen_3) micro-architecture released in November 2020 have problems with [BMI2](BMI2 "BMI2") performance <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> , in particular using [BMI2 PEXT](BMI2#PEXT "BMI2") in chess programs - one should conditionally compile using [magic bitboards](Magic_Bitboards "Magic Bitboards") instead of [PEXT bitboards](BMI2#PEXTBitboards "BMI2"), otherwise preferable for compatible [Intel](Intel "Intel") processors <a id="cite-note-5" href="#cite-ref-5">[5]</a> .

## Contents

- [1 Sponsoring](#sponsoring)
- [2 Photos](#photos)
- [3 x86 Architectures](#x86-architectures)
- [4 SIMD Extensions](#simd-extensions)
- [5 General Purpose Extensions](#general-purpose-extensions)
- [6 See also](#see-also)
- [7 Forum Posts](#forum-posts)
  - [7.1 2010 ...](#2010-...)
  - [7.2 2015 ...](#2015-...)
  - [7.3 2020 ...](#2020-...)
- [8 External Links](#external-links)
- [9 References](#references)

## Sponsoring

- [WMCCC 1997](WMCCC_1997 "WMCCC 1997")
- [BELCT 2001](BELCT_2001 "BELCT 2001")

## Photos

[](http://www.thorstenczub.de/pariswm97.html)
[Christophe Jolly](Christophe_Jolly "Christophe Jolly") and [Walter Bannerman](Walter_Bannerman "Walter Bannerman"), Paris [WMCCC 1997](WMCCC_1997 "WMCCC 1997") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

[](http://www.top-5000.nl/int/aaron.htm)
[Rebel](Rebel "Rebel") vs [Viswanathan Anand](https://en.wikipedia.org/wiki/Viswanathan_Anand), [Ischia](https://en.wikipedia.org/wiki/Ischia), July 1998 - back of [Ed Schröder](Ed_Schroder "Ed Schroder") and [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen") <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>

[](http://www.quarkchess.de/belct/body_index.html)
[Jochen Peussner](Jochen_Peussner "Jochen Peussner") and [Roland Pfister](Roland_Pfister "Roland Pfister"), [BELCT 2001](BELCT_2001 "BELCT 2001") <a id="cite-note-9" href="#cite-ref-9">[9]</a>

## x86 Architectures

<a id="cite-note-10" href="#cite-ref-10">[10]</a>

|  Year
|  Architecture
|
| --- | --- |
|  1991
| [x86](X86 "X86") | [Am386](https://en.wikipedia.org/wiki/Am386) |
|  1993
| [Am486](https://en.wikipedia.org/wiki/Am486) |
|  1996
| [AMD K5](https://en.wikipedia.org/wiki/AMD_K5) |
|  1997
| [AMD K6](https://en.wikipedia.org/wiki/AMD_K6) |
|  1998
| [AMD K6-2](https://en.wikipedia.org/wiki/AMD_K6-2) |
|  1999
| [AMD K7 Athlon](https://en.wikipedia.org/wiki/Athlon) |
|  2003
| [x86-64](X86-64 "X86-64") | [AMD K8 Athlon 64, Opteron](https://en.wikipedia.org/wiki/AMD_K8) |
|  2007
| [AMD K10](https://en.wikipedia.org/wiki/AMD_10h) |
|  2011
| [Bulldozer](https://en.wikipedia.org/wiki/Bulldozer_%28microarchitecture%29) |
|  2012
| [Piledriver](https://en.wikipedia.org/wiki/AMD_Fusion#Piledriver) |
|  2014
| [Steamroller](https://en.wikipedia.org/wiki/Steamroller_%28microarchitecture%29) |
|  2015
| [Excavator](https://en.wikipedia.org/wiki/Excavator_%28microarchitecture%29) |
|  2017
| [Zen](<https://en.wikipedia.org/wiki/Zen_(first_generation_microarchitecture)>) |
|  2018
| [Zen+](https://en.wikipedia.org/wiki/Zen%2B) |
|  2019
| [Zen 2](https://en.wikipedia.org/wiki/Zen_2) |
|  2020
| [Zen 3](https://en.wikipedia.org/wiki/Zen_3) |

## SIMD Extensions

- [AVX](AVX "AVX") (since Bulldozer)
- [AVX2](AVX2 "AVX2") (since Excavator)
- [MMX](MMX "MMX")
- [3DNow!](https://en.wikipedia.org/wiki/3DNow!)
- [SSE](SSE "SSE")
- [SSE2](SSE2 "SSE2")
- [SSE3](SSE3 "SSE3")
- [SSE4](SSE4 "SSE4")
- [SSE5](SSE5 "SSE5") (not implemented)
- [XOP](XOP "XOP") (Bulldozer only)

## General Purpose Extensions

- [BMI](BMI1 "BMI1")
- [BMI2](BMI2 "BMI2") (Zen) <a id="cite-note-11" href="#cite-ref-11">[11]</a>
- [TBM](TBM "TBM")

## See also

- [Intel](Intel "Intel")
- [Microsoft](Microsoft "Microsoft")

## Forum Posts

## 2010 ...

- [Intel vs AMD: which does your engine prefer?](http://www.talkchess.com/forum/viewtopic.php?t=40996) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), November 04, 2011 » [Intel](Intel "Intel")
- [What is your take on AMD's new processor?](http://www.talkchess.com/forum/viewtopic.php?t=45707) by Tano-Urayoan Russi Roman, [CCC](CCC "CCC"), October 24, 2012

## 2015 ...

- [AMD's Ryzen launches March 2, outperforming Intel's Core i7](http://www.talkchess.com/forum/viewtopic.php?t=63246) by Leo Anger, [CCC](CCC "CCC"), February 22, 2017 <a id="cite-note-12" href="#cite-ref-12">[12]</a>
- [New AMD processors](https://groups.google.com/d/msg/computer-go-archive/mXE2UsBDeyA/ljUckKn-AgAJ) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [The Computer-go Archives](http://computer-go.org/pipermail/computer-go/), March 03, 2017
- [Ryzen Fritz Chess Benchmarks ?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32016) by ralunger, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), March 03, 2017
- [Is anyone here already using a Ryzen 1800X processor ?](http://www.talkchess.com/forum/viewtopic.php?t=63564) by Aloisio Ponti, [CCC](CCC "CCC"), March 26, 2017
- [Re: Komodo 11.3](http://www.talkchess.com/forum/viewtopic.php?t=66737&start=4) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), March 04, 2018 » [BMI2 PEXT](#pext), [Komodo 11.3](Komodo#11 "Komodo")
- [Ryzen 2 and BMI2?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67432) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), May 13, 2018 » [BMI2](BMI2 "BMI2")

[Re: Ryzen 2 and BMI2?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67432&start=12) by [Joost Buijs](Joost_Buijs "Joost Buijs"), [CCC](CCC "CCC"), May 18, 2020 » [AVX2](AVX2 "AVX2"), [BMI2](BMI2 "BMI2")

- [Porting Stockfish to GCN on APUs...?](https://groups.google.com/d/msg/fishcooking/svTzAYXesCs/_1smL5wSBwAJ) by [Nick Pelling](Nick_Pelling "Nick Pelling"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 18, 2018 » [Stockfish](Stockfish "Stockfish") <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a>
- [AMD BMI2 question](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70167) by Leo, [CCC](CCC "CCC"), March 10, 2019 » [BMI2](BMI2 "BMI2")
- [Ryzen problems - AGAIN!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72137) by [noobpwnftw](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), October 22, 2019
- [PEXT/PDEP are even slower than you think on Zen](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72538) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), December 09, 2019 » [BMI2 PEXT](#pext)

## 2020 ...

- [AMD's X3D - HBM on CPU - memory wall](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73309) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), March 08, 2020
- [Re: Ryzen 2 and BMI2?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67432&start=12) by [Joost Buijs](Joost_Buijs "Joost Buijs"), [CCC](CCC "CCC"), May 18, 2020 » [AVX2](AVX2 "AVX2"), [BMI2](BMI2 "BMI2")
- [Re: AMD Announces a Red October: Zen 3 on October 8, RDNA2 on October 28](https://www.techpowerup.com/forums/threads/amd-announces-a-red-october-zen-3-on-october-8-rdna2-on-october-28.271981/page-2#post-4344965) by dragontamer5788, [TechPowerUp Forum](https://www.techpowerup.com/forums/), September 9, 2020 » [BMI2 PEXT](#pext)
- [New AMD Zen 3 and Ryzen processors](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75333) by mmt, [CCC](CCC "CCC"), October 09, 2020
- [Will AMD RDNA2 based Radeon RX 6000 series kick butt with Lc0?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75639) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), November 01, 2020 » [GPU](GPU "GPU")
- [Zen3 supports fast PEXT aka BMI2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75691) by [Alayan Feh](index.php?title=Alayan_Feh&action=edit&redlink=1 "Alayan Feh (page does not exist)"), [CCC](CCC "CCC"), November 05, 2020 » [BMI2 PEXT](BMI2#PEXT "BMI2")

## External Links

- [Advanced Micro Devices from Wikipedia](https://en.wikipedia.org/wiki/Advanced_Micro_Devices)
- [List of AMD CPU microarchitectures from Wikipedia](https://en.wikipedia.org/wiki/List_of_AMD_CPU_microarchitectures)
- [Intel Corp. v. Advanced Micro Devices, Inc. from Wikipedia](https://en.wikipedia.org/wiki/Intel_Corp._v._Advanced_Micro_Devices,_Inc.)
- [Advanced Micro Devices, Inc. v. Intel Corp. from Wikipedia](https://en.wikipedia.org/wiki/Advanced_Micro_Devices,_Inc._v._Intel_Corp.)
- [AMD Accelerated Processing Unit from Wikipedia](https://en.wikipedia.org/wiki/AMD_Accelerated_Processing_Unit)
- [Graphics Core Next from Wikipedia](https://en.wikipedia.org/wiki/Graphics_Core_Next)
- [AMD Corporate Website](http://www.amd.com/)
- [Inside AMD's Hammer: the 64-bit architecture behind the Opteron and Athlon 64](https://arstechnica.com/features/2005/02/amd-hammer-1/) by Jon Stokes, [ars technica](http://arstechnica.com/index.ars), February 01, 2005
- [Understanding the detailed Architecture of AMD's 64 bit Core](http://chip-architect.com/news/2003_09_21_Detailed_Architecture_of_AMDs_64bit_Core.html) by [Hans de Vries](http://www.chip-architect.com/), September 21, 2003
- [AMD releases new Ryzen processor](http://en.chessbase.com/post/amd-releases-new-ryzen-processor) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), March 03, 2017

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> AMD headquarters, [Sunnyvale, California](https://en.wikipedia.org/wiki/Sunnyvale,_California), from [Advanced Micro Devices from Wikipedia](https://en.wikipedia.org/wiki/Advanced_Micro_Devices)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Advanced Micro Devices from Wikipedia](https://en.wikipedia.org/wiki/Advanced_Micro_Devices)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Ryzen Fritz Chess Benchmarks ?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32016) by ralunger, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), March 03, 2017
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Ryzen and BMI2: Strange behavior and high latencies](https://www.reddit.com/r/Amd/comments/60i6er/ryzen_and_bmi2_strange_behavior_and_high_latencies/) by DonnieTinyHands, [Reddit](https://en.wikipedia.org/wiki/Reddit), March 20, 2017
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Komodo 11.3](http://www.talkchess.com/forum/viewtopic.php?t=66737&start=4) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), March 04, 2018 » [BMI2 PEXT](BMI2#PEXT "BMI2"), [Komodo 11.3](Komodo#11 "Komodo")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Paris - Trier - Lünen](http://www.thorstenczub.de/pariswm97.html), Photos [WMCCC 1997](WMCCC_1997 "WMCCC 1997") by [Thorsten Czub](Thorsten_Czub "Thorsten Czub")
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [REBEL vs GM Vishy Anand](http://www.top-5000.nl/authors/rebel/chess_5.htm)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [Ed Schröder](Ed_Schroder "Ed Schroder") (**1998**). *Anand versus Rebel 10 exp.* [ICCA Journal, Vol. 21, No. 3](ICGA_Journal#21_3 "ICGA Journal")
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [BELCT 2001 Berlin is worth a trip!](http://www.quarkchess.de/belct/) Photos by [Thomas Mayer](Thomas_Mayer "Thomas Mayer")
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [List of AMD microprocessors from Wikipedia](https://en.wikipedia.org/wiki/List_of_AMD_microprocessors)
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Re: Komodo 11.3](http://www.talkchess.com/forum/viewtopic.php?t=66737&start=4) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), March 04, 2018
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Ryzen from Wikipedia](https://en.wikipedia.org/wiki/Ryzen)
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Graphics Core Next from Wikipedia](https://en.wikipedia.org/wiki/Graphics_Core_Next)
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [AMD Accelerated Processing Unit from Wikipedia](https://en.wikipedia.org/wiki/AMD_Accelerated_Processing_Unit)

**[Up one Level](Organizations "Organizations")**

