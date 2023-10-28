---
title: Guido Schimmels
---
**[Home](Home "Home") * [People](People "People") * Guido Schimmels**

**Guido Schimmels**,

a German software developer contributing to [FSF GNU](Free_Software_Foundation "Free Software Foundation") and similar projects, such as [GNU TeXmacs](https://en.wikipedia.org/wiki/GNU_TeXmacs) <a id="cite-note-1" href="#cite-ref-1">[1]</a>, and the [ROX Desktop](https://en.wikipedia.org/wiki/ROX_Desktop) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
He further is contributor of the [Ultimate++](https://en.wikipedia.org/wiki/Ultimate%2B%2B) framework <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
In the late 90s and early 2000s, Guido Schimmels was engaged in computer chess programming, and made a couple of posts in [CCC](CCC "CCC").

## Contents

- [1 PVS vs. NegaScout](#pvs-vs.-negascout)
  - [1.1 PVS](#pvs)
  - [1.2 NegaScout](#negascout)
- [2 Forum Posts](#forum-posts)
- [3 References](#references)

## PVS vs. NegaScout

Guido Schimmels in a [CCC](CCC "CCC") post on the difference of [PVS](Principal_Variation_Search "Principal Variation Search") vs. [NegaScout](NegaScout "NegaScout") <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```
The difference is how they handle re-searches: PVS passes alpha/beta while NegaScout passes the value returned by the null window search instead of alpha. But then you can get a fail-low on the research due to [search anonomalies](Search_Instability "Search Instability"). If that happens NegaScout returns the value from the first search. That means you will have a crippled [PV](Principal_Variation "Principal Variation"). Then there is a refinement [Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") suggests which is to ommit the re-search at the last two plies (depth > 1) - but that won't work in a real program because of [search extensions](Extensions "Extensions"). NegaScout is slightly an [ivory tower](https://en.wikipedia.org/wiki/Ivory_Tower) variant of PVS (IMHO).  

```

## PVS

```

value = PVS(-(alpha+1),-alpha)
if(value > alpha && value < beta) {
  value = PVS(-beta,-alpha);
}

```

## NegaScout

```

value = NegaScout(-(alpha+1),-alpha)
if(value > alpha && value < beta && depth > 1) {
  value2 = NegaScout(-beta,-value)
  value = max(value,value2);
}

```

## Forum Posts

- [Re: Hash Table Size Versus Performance](https://www.stmintz.com/ccc/index.php?id=19790) by Guido Schimmels, [CCC](CCC "CCC"), June 02, 1998 » [Transposition Table](Transposition_Table "Transposition Table")
- [Question to Bob: Crafty , Alpha and FindBit()](https://www.stmintz.com/ccc/index.php?id=20057) by Guido Schimmels, [CCC](CCC "CCC"), June 05, 1998 » [Crafty](Crafty "Crafty"), [DEC Alpha](DEC_Alpha "DEC Alpha"), [BitScan](BitScan "BitScan")
- [Re: Zero-width Window Null Move Search](https://www.stmintz.com/ccc/index.php?id=20868) by Guido Schimmels, [CCC](CCC "CCC"), June 18, 1998 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), [NegaScout](NegaScout "NegaScout")
- [Failing low at the root](https://www.stmintz.com/ccc/index.php?id=23672) by Guido Schimmels, [CCC](CCC "CCC"), August 03, 1998 » [Root](Root "Root")
- [Books that help for evaluation](https://www.stmintz.com/ccc/index.php?id=25012) by Guido Schimmels, [CCC](CCC "CCC"), August 18, 1998 » [Evaluation](Evaluation "Evaluation")
- [Re: Atheist IQ vs Theist IQ](https://groups.google.com/d/msg/alt.religion.kibology/vMQhc1hJc7Q/xpnuVGQYZa4J) by Guido Schimmels, [alt.religion.kibology](https://groups.google.com/forum/?fromgroups=#!forum/alt.religion.kibology), August 18, 1999
- [Re: GCC 3.1 fastest compiler at K7 !!](https://www.stmintz.com/ccc/index.php?id=230559) by Guido Schimmels, [CCC](CCC "CCC"), May 20, 2002

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [About TeXmacs (FSF GNU project)](http://www.texmacs.org/tmweb/manual/webman-about.en.html)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Tango Theme | ROX Desktop](http://rox.sourceforge.net/desktop/node/270.html)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Copyright © 1999-2019 Ultimate++ team :: Ultimate++](http://www.ultimatepp.org/app$ide$About$en-us.html)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Zero-width Window Null Move Search](https://www.stmintz.com/ccc/index.php?id=20868) by Guido Schimmels, [CCC](CCC "CCC"), June 18, 1998

**[Up one level](People "People")**

