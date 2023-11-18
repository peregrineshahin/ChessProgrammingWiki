---
title: CLOP
---
**[Home](Home "Home") * [Automated Tuning](Automated_Tuning "Automated Tuning") * CLOP**

**CLOP** for Noisy Black-Box Parameter Optimization,
a program used for [parameter tuning](Automated_Tuning "Automated Tuning"), created by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"). The CLOP principle, which stands for [Confident](http://en.wiktionary.org/wiki/confidence) [Local OPtimization](https://en.wikipedia.org/wiki/Local_search_%28optimization%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a>, is an approach to [local regression](https://en.wikipedia.org/wiki/Local_regression) that overcomes problems with very [noisy](https://en.wikipedia.org/wiki/Statistical_noise) outputs and nonnegative [Hessians](https://en.wikipedia.org/wiki/Hessian_matrix) <a id="cite-note-2" href="#cite-ref-2">[2]</a> in a simple and efficient way. CLOP is suited to tune several parameters simultaneously, and requires polynomial [time](https://en.wikipedia.org/wiki/Time_complexity) for each additional parameter to verify the tuned values, that is playing a lot of games <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## See also

- [Match Statistics](Match_Statistics "Match Statistics")
- [Cutechess-cli](Cutechess-cli "Cutechess-cli")
- [SPSA](SPSA "SPSA")

## Publications

- [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") (**2011**). *[CLOP: Confident Local Optimization for Noisy Black-Box Parameter Tuning](http://remi.coulom.free.fr/CLOP/)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13"), [slides as pdf](http://remi.coulom.free.fr/CLOP/CLOPSlides.pdf)
- [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") (**2012**). *[CLOP: Confident Local Optimization for Noisy Black-Box Parameter Tuning](http://link.springer.com/chapter/10.1007%2F978-3-642-31866-5_13)*. [Advances in Computer Games](http://link.springer.com/book/10.1007/978-3-642-31866-5), [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), Vol. 7168, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

## Forum Posts

## 2011 ...

- [CLOP for Noisy Black-Box Parameter Optimization](http://talkchess.com/forum/viewtopic.php?t=40237) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), September 01, 2011
- [To Ilari : CLOP + cutechess-cli](http://www.talkchess.com/forum/viewtopic.php?t=40687) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), October 09, 2011

**2012**

- [Re: win rate bias and CLOP](http://computer-go.org/pipermail/computer-go/2012-January/004429.html) by [Brian Sheppard](Brian_Sheppard "Brian Sheppard"), [Computer-go Archives](http://computer-go.org/pipermail/computer-go/), January 03, 2012
- [CLOP + cutechess cli](http://www.talkchess.com/forum/viewtopic.php?t=41816) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [CCC](CCC "CCC"), January 05, 2012 » [Cutechess-cli](Cutechess-cli "Cutechess-cli")
- [EXchess v6.10 released](http://www.talkchess.com/forum/viewtopic.php?t=42202) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 29, 2012 » [EXchess](EXchess "EXchess")
- [CLOP on Stockfish](http://www.talkchess.com/forum/viewtopic.php?p=454327) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), March 10, 2012 » [Stockfish](Stockfish "Stockfish")

**2013**

- [CLOP and Stockfish](https://groups.google.com/d/msg/fishcooking/8zN5TZfEN8w/KIZYLnO8c08J) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), March 31, 2013 » [Stockfish](Stockfish "Stockfish")
- [CLOP tuning](https://groups.google.com/d/msg/fishcooking/y9maHKLrhQQ/68_yqILvcWYJ) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 19, 2013
- [CLOP tests are active](https://groups.google.com/d/msg/fishcooking/6Jis--X-L20/QcJ7XqUZ2-EJ) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), July 03, 2013
- [Question regarding CLOP and cutechess-cli](http://www.talkchess.com/forum/viewtopic.php?t=48847) by [Jacob Børs Lind](index.php?title=Jacob_B%C3%B8rs_Lind&action=edit&redlink=1 "Jacob Børs Lind (page does not exist)"), [CCC](CCC "CCC"), August 05, 2013 » [Cutechess-cli](Cutechess-cli "Cutechess-cli")
- [Clop and cutechess](http://www.talkchess.com/forum/viewtopic.php?t=49410) by [Alcides Schulz](Alcides_Schulz "Alcides Schulz"), [CCC](CCC "CCC"), September 21, 2013
- [CLOP tests are active (finally)](https://groups.google.com/d/msg/fishcooking/EczR5D1BKhU/thmLRG5uBdkJ) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 10, 2013
- [CLOP overhead](https://groups.google.com/d/msg/fishcooking/gmE5A05jWsg/4toIYFI6z80J) by Lucas Braesch, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 14, 2013

**2014**

- [needed CLOP for cluster](http://www.talkchess.com/forum/viewtopic.php?t=51020) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 23, 2014
- [Help with CLOP](http://www.talkchess.com/forum/viewtopic.php?t=51167) by Arjun Temurnikar, [CCC](CCC "CCC"), February 05, 2014
- [Problem with CLOP and clop-cutechess-cli.py? (long post)](https://groups.google.com/d/msg/fishcooking/0uRw0Zila0M/s2siUjVzFFwJ) by joster, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 10, 2014
- [Goodbye CLOP, hello SPSA)](https://groups.google.com/d/msg/fishcooking/WNrxeXAJ6VI/ZkCnRv4I_qEJ) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 17, 2014
- [Port of Coulom's CLOP algorithm to Python](https://groups.google.com/d/msg/fishcooking/bW1l9oesAb8/-uMnp3Ky4UwJ) by Kamyar, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 03, 2014

## 2015 ...

- [Working with CLOP](http://www.talkchess.com/forum/viewtopic.php?t=55042) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), January 22, 2015
- [CLOP: when to stop?](http://www.talkchess.com/forum/viewtopic.php?t=62012) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), November 07, 2016
- [CLOP in cutechess-cli debug](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67529) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), May 22, 2018 » [Cutechess-cli](Cutechess-cli "Cutechess-cli")
- [New CLOP settings give Leela huge tactics boost](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67646) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), June 04, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")

## 2020 ...

- [Trying to CLOP again](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72848) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), January 19, 2020

## External Links

- [CLOP: Confident Local Optimization for Noisy Black-Box Parameter Tuning](http://remi.coulom.free.fr/CLOP/)
- [cutechess-cly Python script fo CLOP](https://github.com/cutechess/cutechess/blob/master/tools/clop-cutechess-cli.py)
- [Black box from Wikipedia](https://en.wikipedia.org/wiki/Black_box)
- [Black box (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Black_box_%28disambiguation%29)
- [Les Paul](Category:Les_Paul "Category:Les Paul") - Black Box <a id="cite-note-4" href="#cite-ref-4">[4]</a>, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [CLOP: Confident Local Optimization for Noisy Black-Box Parameter Tuning](http://remi.coulom.free.fr/CLOP/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Second partial derivative test from Wikipedia](https://en.wikipedia.org/wiki/Second_partial_derivative_test)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: How Do You Automatically Tune Your Evaluation Tables](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=552257&t=50823) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 31, 2014
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [The Inventions - Les Paul](http://www.les-paul.com/timeline/les-the-inventor/)

**[Up one Level](Automated_Tuning "Automated Tuning")**

