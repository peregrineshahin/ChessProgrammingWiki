---
title: Dynamic Tree Splitting
---
**[Home](Home "Home") * [Search](Search "Search") * [Parallel Search](Parallel_Search "Parallel Search") * Dynamic Tree Splitting**

\[ Splitted tree <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Dynamic Tree Splitting**, (DTS)

a [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) model of parallelism which divides the [search tree](Search_Tree "Search Tree") among several processors on a [shared memory](Memory#Shared "Memory") parallel machine, devised by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") <a id="cite-note-2" href="#cite-ref-2">[2]</a> , implemented in [Cray Blitz](Cray_Blitz "Cray Blitz") and tested on a 16 processor [Cray C916/1024](Cray_X-MP#C90 "Cray X-MP") with 1024 mebiwords of [memory](Memory "Memory") (8 [gibibytes](https://en.wikipedia.org/wiki/Gibibyte)).DTS overcomes one problem of [principle variation splitting](Parallel_Search#PrincipalVariationSplitting "Parallel Search") (PVS) and enhanced principle variation splitting (EPVS) <a id="cite-note-3" href="#cite-ref-3">[3]</a> with bushy trees, that processors assigned to a [node](Node "Node") become and stay [idle](<https://en.wikipedia.org/wiki/Idle_(CPU)>) while other processors are still busy on the same node. In DTS, busy processors publish their state of the tree in shared memory for idle processors to examine, to let them decide which (if any) of the busy processors to join, and to inform a busy processor of the chosen expceted [all-node](Node_Types#all-nodes "Node Types") or [pv-node](Node_Types#pv-node "Node Types") <a id="cite-note-4" href="#cite-ref-4">[4]</a> , dubbed split point. The busy processor with that subtree in progress in turn, then copies the complete tree state with current [board position](Chess_Position "Chess Position"), [bounds](Bound "Bound"), [move list](Move_List "Move List"), [repetition list](Repetitions#listofkeys "Repetitions") and so forth to a shared memory area, becoming a so called "split block". Owner and helper processors can now extract moves from this shared data to search in parallel <a id="cite-note-5" href="#cite-ref-5">[5]</a> .

## Performance Test

Rather than to use a group of unrelated chess problems, the CB team took a segment of a real chess game from the [ACM 1993](ACM_1993 "ACM 1993") [M-Chess Pro vs. Cray Blitz](ACM_1993#MChessCrayBlitz "ACM 1993"), a sharp [Vienna game](https://en.wikipedia.org/wiki/Vienna_Game) aka delayed [kings gambit accepted](https://en.wikipedia.org/wiki/King%27s_Gambit#King.27s_Gambit_Accepted:_2...exf4) after CB was out of book after 1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. d4 g4 6. Bc4 gxf3 7. o-o d5 8. exd5 Bg4 9. Qd2, 24 positions in total. The results include two sets of numbers for each test, where a test used either one, two, four, eight or sixteen processors. The numbers are the clock time required for the search (wall clock time) and the number of nodes searched which shows how much extra work is added by using additional processors <a id="cite-note-6" href="#cite-ref-6">[6]</a> .

## DTS Speedups

*DTS Cray Blitz speedups on Cray C916/1024 over 24 test positions* <a id="cite-note-7" href="#cite-ref-7">[7]</a>

|  #proc
|  1
|  2
|  4
|  8
|  16
|
| --- | --- | --- | --- | --- | --- |
|  pos
|  sec
|  nodes
|  speedup
|  sec
|  nodes
|  speedup
|  sec
|  nodes
|  speedup
|  sec
|  nodes
|  speedup
|  sec
|  nodes
|  speedup
|
|  1
|  2,830
|  87,735,974
|  1
|  1,415
|  89,052,012
|  2.0
|  832
|  105,025,123
|  3.4
|  435
|  109,467,495
|  6.5
|  311
|  155,514,410
|  9.1
|
|  2
|  2,849
|  88,954,757
|  1
|  1,424
|  90,289,077
|  2.0
|  791
|  100,568,301
|  3.6
|  438
|  110,988,161
|  6.5
|  274
|  137,965,406
|  10.4
|
|  3
|  3,274
|  101,302,792
|  1
|  1,637
|  102,822,332
|  2.0
|  884
|  111,433,074
|  3.7
|  467
|  117,366,515
|  7.0
|  239
|  119,271,093
|  13.7
|
|  4
|  2,308
|  71,726,853
|  1
|  1,154
|  72,802,754
|  2.0
|  591
|  74,853,409
|  3.9
|  349
|  88,137,085
|  6.6
|  208
|  104,230,094
|  11.1
|
|  5
|  1,584
|  49,386,616
|  1
|  792
|  50,127,414
|  2.0
|  440
|  55,834,316
|  3.6
|  243
|  61,619,298
|  6.5
|  178
|  89,506,306
|  8.9
|
|  6
|  4,294
|  133,238,718
|  1
|  2,147
|  135,237,296
|  2.0
|  1,160
|  146,562,594
|  3.7
|  670
|  168,838,428
|  6.4
|  452
|  226,225,307
|  9.5
|
|  7
|  1,888
|  58,593,747
|  1
|  993
|  62,602,792
|  1.9
|  524
|  66,243,490
|  3.6
|  273
|  68,868,878
|  6.9
|  187
|  93,575,946
|  10.1
|
|  8
|  7,275
|  225,906,282
|  1
|  3,637
|  229,294,872
|  2.0
|  1,966
|  248,496,917
|  3.7
|  1,039
|  261,728,552
|  7.0
|  680
|  340,548,431
|  10.7
|
|  9
|  3,940
|  122,264,617
|  1
|  1,970
|  124,098,584
|  2.0
|  1,094
|  138,226,951
|  3.6
|  635
|  159,930,005
|  6.2
|  398
|  199,204,874
|  9.9
|
|  10
|  2,431
|  75,301,353
|  1
|  1,215
|  76,430,872
|  2.0
|  639
|  80,651,716
|  3.8
|  333
|  83,656,702
|  7.3
|  187
|  93,431,597
|  13.0
|
|  11
|  3,062
|  95,321,494
|  1
|  1,531
|  96,751,315
|  2.0
|  827
|  104,853,646
|  3.7
|  425
|  107,369,070
|  7.2
|  247
|  123,994,812
|  12.4
|
|  12
|  2,518
|  79,975,416
|  1
|  1,325
|  85,447,418
|  1.9
|  662
|  85,657,884
|  3.8
|  364
|  94,000,085
|  6.9
|  219
|  112,174,209
|  11.5
|
|  13
|  2,131
|  66,100,160
|  1
|  1,121
|  70,622,802
|  1.9
|  560
|  70,796,754
|  3.8
|  313
|  78,834,155
|  6.8
|  192
|  96,053,649
|  11.1
|
|  14
|  1,871
|  58,099,574
|  1
|  935
|  58,971,066
|  2.0
|  534
|  67,561,507
|  3.5
|  296
|  74,791,668
|  6.3
|  191
|  95,627,150
|  9.8
|
|  15
|  2,648
|  84,143,340
|  1
|  1,324
|  85,405,488
|  2.0
|  715
|  92,557,676
|  3.7
|  378
|  97,486,065
|  7.0
|  243
|  124,516,703
|  10.9
|
|  16
|  2,347
|  75,738,094
|  1
|  1,235
|  80,920,173
|  1.9
|  601
|  79,039,499
|  3.9
|  321
|  84,141,904
|  7.3
|  182
|  94,701,972
|  12.9
|
|  17
|  4,884
|  154,901,225
|  1
|  2,872
|  184,970,278
|  1.7
|  1,878
|  242,480,013
|  2.6
|  1,085
|  279,166,418
|  4.5
|  814
|  416,426,105
|  6.0
|
|  18
|  646
|  20,266,629
|  1
|  358
|  22,856,254
|  1.8
|  222
|  28,443,165
|  2.9
|  124
|  31,608,146
|  5.2
|  84
|  42,454,639
|  7.7
|
|  19
|  2,983
|  93,858,903
|  1
|  1,491
|  95,266,785
|  2.0
|  785
|  100,527,830
|  3.8
|  426
|  108,742,238
|  7.0
|  226
|  114,692,731
|  13.2
|
|  20
|  7,473
|  231,206,390
|  1
|  3,736
|  234,674,482
|  2.0
|  1,916
|  241,284,621
|  3.9
|  1,083
|  271,751,263
|  6.9
|  530
|  264,493,531
|  14.1
|
|  21
|  3,626
|  112,457,464
|  1
|  1,813
|  114,144,324
|  2.0
|  906
|  114,425,474
|  4.0
|  489
|  123,247,294
|  7.4
|  237
|  118,558,091
|  15.3
|
|  22
|  2,560
|  81,302,340
|  1
|  1,347
|  86,865,131
|  1.9
|  691
|  89,432,576
|  3.7
|  412
|  106,348,704
|  6.2
|  264
|  135,196,568
|  9.7
|
|  23
|  2,039
|  63,598,940
|  1
|  1,019
|  64,552,923
|  2.0
|  536
|  68,117,815
|  3.8
|  323
|  81,871,010
|  6.3
|  206
|  103,621,303
|  9.9
|
|  24
|  2,563
|  80,413,971
|  1
|  1,281
|  81,620,179
|  2.0
|  657
|  83,919,196
|  3.9
|  337
|  85,810,169
|  7.6
|  178
|  90,074,814
|  14.4
|
|  avg
|  |  |  1
|  |  |  2.0
|  |  |  3.7
|  |  |  6.6
|  |  |  11.1
|

Despite Robert Hyatt mentioned DTS really will only scale as far as a shared memory architecture scales, and any delays (such as those in some architectures that use a [hierarchical memory organization](NUMA "NUMA") with varying delays depending on how far the memory is from the requesting processor) will certainly have an adverse effect on DTS, the published speedups were heavily criticized by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen") in 2002 <a id="cite-note-8" href="#cite-ref-8">[8]</a> .

## Comparison

*Average Cray Blitz speedups on Cray C916/1024 over 24 test positions*

|  #ProcsAlgorithm
|  1
|  2
|  4
|  8
|  16
|
| --- | --- | --- | --- | --- | --- |
|  PVS
|  1.0
|  1.8
|  3.0
|  4.1
|  4.6
|
|  EPVS
|  1.0
|  1.9
|  3.4
|  5.4
|  6.0
|
|  DTS
|  1.0
|  2.0
|  3.7
|  6.6
|  11.1
|

## Recursive DTS

While searching various subtrees with different [ply](Ply "Ply") levels from the [root](Root "Root") was quite straighforward to implement in [Cray Blitz'](Cray_Blitz "Cray Blitz") [iterative search](Iterative_Search "Iterative Search") written in [Fortran](Fortran "Fortran"), a [recursive](Recursion "Recursion") [Negamax](Negamax "Negamax") would have made it much more difficult, since the [call stack](Stack#Hardware "Stack") is inaccessible to the search code and moving the tree state around would have been more difficult <a id="cite-note-9" href="#cite-ref-9">[9]</a> . A recursive DTS-like algorithm was proposed by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund") in 2013 <a id="cite-note-10" href="#cite-ref-10">[10]</a> , as implemented in [Texel](Texel "Texel").

## See also

- [ABDADA](ABDADA "ABDADA")
- [Jamboree](Jamboree "Jamboree")
- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [NUMA](NUMA "NUMA")
- [SMP](SMP "SMP")
- [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")

## Publications

- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1994**). *[The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html)*.
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1997**). *[The Dynamic Tree-Splitting Parallel Search Algorithm](http://www.craftychess.com/hyatt/search.html)*. [ICCA Journal, Vol. 20, No. 1](ICGA_Journal#20_1 "ICGA Journal")
- [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah") (**2001**). *Parallel Alpha-Beta Search on Shared Memory Multiprocessors*. Masters Thesis, [pdf](http://www.top-5000.nl/ps/Parallel%20Alpha-Beta%20Search%20on%20Shared%20Memory%20Multiprocessors.pdf)
- [David J. Wu](David_J._Wu "David J. Wu") (**2015**). *Designing a Winning Arimaa Program*. [ICGA Journal, Vol. 38, No. 1](ICGA_Journal#38_1 "ICGA Journal"), [pdf](http://icosahedral.net/downloads/djwu2015arimaa_color.pdf) » [Arimaa](Arimaa "Arimaa") <a id="cite-note-11" href="#cite-ref-11">[11]</a>

## Forum Posts

## 2000 ...

- [DTS article robert hyatt - revealing his bad math](https://www.stmintz.com/ccc/index.php?id=249457) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), September 03, 2002

[DTS NUMA](https://www.stmintz.com/ccc/index.php?id=249651) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), September 03, 2002 » [NUMA](NUMA "NUMA")

- [Iterative DTS](http://www.talkchess.com/forum/viewtopic.php?t=14832) by [Fritz Reul](Fritz_Reul "Fritz Reul"), [CCC](CCC "CCC"), July 02, 2007

## 2010 ...

- [DTS Structure](http://www.talkchess.com/forum/viewtopic.php?t=34561) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), May 28, 2010 » Dynamic Tree Splitting, [Iterative Search](Iterative_Search "Iterative Search")
- [DTS-ification of YBWC](http://www.talkchess.com/forum/viewtopic.php?t=34633) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), June 01, 2010
- [Parallelization questions, ABDADA or DTS?](http://www.talkchess.com/forum/viewtopic.php?t=42986) by [Benjamin Rosseaux](index.php?title=Benjamin_Rosseaux&action=edit&redlink=1 "Benjamin Rosseaux (page does not exist)"), [CCC](CCC "CCC"), March 23, 2012 » [ABDADA](ABDADA "ABDADA")
- [Recursive DTS-like search algorithm](http://www.talkchess.com/forum/viewtopic.php?t=48752) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 24, 2013 » [Texel](Texel "Texel")
- [DTS-like SMP](http://www.open-chess.org/viewtopic.php?f=5&t=2378) by [ThinkingALot](ThinkingALot "ThinkingALot"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 25, 2013 » [Gull](Gull "Gull")
- [Dynamic Tree Splitting](http://www.talkchess.com/forum/viewtopic.php?t=55649) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), March 13, 2015
- [Empirical results with Lazy SMP, YBWC, DTS](http://www.talkchess.com/forum/viewtopic.php?t=56019) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 16, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
- [Another take on DTS?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72167) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), October 25, 2019

## External Links

- [The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
- [Porcupine Tree](Category:Porcupine_Tree "Category:Porcupine Tree") - [Octane Twisted](https://en.wikipedia.org/wiki/Octane_Twisted) (2012), recorded at [Riviera Theatre](https://en.wikipedia.org/wiki/Riviera_Theater), [Chicago](https://en.wikipedia.org/wiki/Chicago,_Illinois), April 30, 2010, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A tree with a doubled split trunk on a lawn beside a drive at Feeringbury Manor in the [civil parish](https://en.wikipedia.org/wiki/Civil_parish) of [Feering](https://en.wikipedia.org/wiki/Feering), [Braintree](https://en.wikipedia.org/wiki/Braintree_District), [Essex](https://en.wikipedia.org/wiki/Essex), England. [Image](https://commons.wikimedia.org/wiki/File:Feeringbury_Manor_split_double_trunk_tree,_Feering_Essex_England_1.jpg) © by [Acabashi](https://commons.wikimedia.org/wiki/User:Acabashi), October 02, 2015, [Creative Commons CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en), Source: [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1994**). *[The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html)*
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Bruce W. Suter](Bruce_W._Suter "Bruce W. Suter"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1989**). *A Parallel Alpha-Beta Tree Searching Algorithm*. Parallel Computing, Vol. 10, No. 3.
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: "CUT" vs "ALL" nodes](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=398061&t=38317) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 08, 2011
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1994**). *[The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html)*
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> Table 4 Search Time in Seconds, Table 5 Total Nodes Searched, and Table 6 Parallel Processing Speedup, combined, in [The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), and [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1997**). *[The Dynamic Tree-Splitting Parallel Search Algorithm](http://www.craftychess.com/hyatt/search.html)*. [ICCA Journal, Vol. 20, No. 1](ICGA_Journal#20_1 "ICGA Journal")
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [DTS article robert hyatt - revealing his bad math](https://www.stmintz.com/ccc/index.php?id=249457) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), September 03, 2002
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Recursive DTS-like search algorithm](http://www.talkchess.com/forum/viewtopic.php?t=48752) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 24, 201
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Paper describing "Sharp" the program that won the Arimaa Challenge](https://www.game-ai-forum.org/viewtopic.php?f=2&t=83) by ddyer, [Game-AI Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2016

**[Up one level](Parallel_Search "Parallel Search")**

