---
title: Chessterfield
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chessterfield**

**Chessterfield**,

a family of chess engines by [Matthias Lüscher](Matthias_L%C3%BCscher "Matthias Lüscher"), written in [C++](Cpp "Cpp"), first released in April 1998. The free native Chessterfield comes with an own [GUI](GUI "GUI"), the experimental [WinBoard](WinBoard "WinBoard") compliant ChessterfieldCL along with its [learning utility](Learning "Learning") ChessterfieldEN is [open source](Category:Open_Source "Category:Open Source") published under the [GNU General Public Licence V2](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. Chessterfield applies [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), [razoring](Razoring "Razoring") and various [extensions](Extensions "Extensions") inside an [aspirated](Aspiration_Windows "Aspiration Windows") [iterative deepening](Iterative_Deepening "Iterative Deepening") loop.

## Screenshot

[](http://home.datacomm.ch/m.luescher/screenshot.html)
Chessterfield [GUI](GUI "GUI") <a id="cite-note-2" href="#cite-ref-2">[2]</a>

## ChessterfieldCL

While affiliated with [ETH Zurich](ETH_Zurich "ETH Zurich"), inspired by [Michael Buro's](Michael_Buro "Michael Buro") [CG 1998](CG_1998 "CG 1998") paper *From Simple Features to Sophisticated Evaluation Functions* <a id="cite-note-3" href="#cite-ref-3">[3]</a>, covering not only [automated parameter tuning](Automated_Tuning "Automated Tuning") but a procedure for exploring the feature space able to discover new features in a computational feasible way, Matthias Lüscher implemented Buro's [General Linear Evaluation Model (GLEM)](Michael_Buro#GLEM "Michael Buro") inside **ChessterfieldCL**, using a three-layer [neural network](Neural_Networks "Neural Networks") as [evaluation function](Evaluation "Evaluation") - documented in his technical report under supervision of [Thomas Lincke](Thomas_Lincke "Thomas Lincke") and [Christoph Wirth](Christoph_Wirth "Christoph Wirth") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Christoph Wirth's [endgame tablebases](Endgame_Tablebases "Endgame Tablebases") <a id="cite-note-5" href="#cite-ref-5">[5]</a> were used to verify the effectiveness of the trained evaluation function in particular endgames <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## See also

- [Chess Engines with Neural Networks](Neural_Networks#engines "Neural Networks")
- [Chester](Chester "Chester")

## Publications

- [Matthias Lüscher](Matthias_L%C3%BCscher "Matthias Lüscher") (**2000**). *Automatic Generation of an Evaluation Function for Chess Endgames*. [ETH Zurich](ETH_Zurich "ETH Zurich") Supervisors: [Thomas Lincke](Thomas_Lincke "Thomas Lincke") and [Christoph Wirth](Christoph_Wirth "Christoph Wirth"), [pdf](http://www.datacomm.ch/m.luescher/evaluation_function_en.pdf)

## Forum Posts

- [ChessterfieldCL stürzt ständig ab](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=31189) by [Clemens Keck](index.php?title=Clemens_Keck&action=edit&redlink=1 "Clemens Keck (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 24, 2000
- [Combining Neural Networks and Alpha-Beta](https://groups.google.com/d/msg/rec.games.chess.computer/xthKCFRJkeM/CwRxa1j7Q1IJ) by [Matthias Lüscher](Matthias_L%C3%BCscher "Matthias Lüscher"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 01, 2000
- [Learning utility for Chessterfield available](https://groups.google.com/d/msg/rec.games.chess.computer/sdfJVjnz_MA/cg-ibeL_4HYJ) by [Matthias Lüscher](Matthias_L%C3%BCscher "Matthias Lüscher"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 29, 2001
- [Chessterfield Source Code Available](https://www.stmintz.com/ccc/index.php?id=149124) by [Matthias Lüscher](Matthias_L%C3%BCscher "Matthias Lüscher"), [CCC](CCC "CCC"), January 10, 2001
- [Chris Wirth's endgame tablebases](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=6&t=2923) by [Denis P. Mendoza](Denis_Mendoza "Denis Mendoza"), [CCRL Endgame Tablebases](Computer_Chess_Forums "Computer Chess Forums"), December 13, 2007

## External Links

## Chess Engine

- [Chessterfield Chess Program](http://home.datacomm.ch/m.luescher/index.html)
- [ChessterfieldCL Download](http://home.datacomm.ch/m.luescher/download_cl.html)
- [ChessterfieldCL i5a JA](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=ChessterfieldCL%20i5a%20JA) in [KCEC](KCEC "KCEC")

## Chesterfield

- [chesterfield - Wiktionary](https://en.wiktionary.org/wiki/chesterfield)
- [Chesterfield (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Chesterfield_%28disambiguation%29)
- [Chesterfield from Wikipedia](https://en.wikipedia.org/wiki/Chesterfield)
- [Chesterfield Chess Club](http://chesterfieldchessclub.weebly.com/)
- [Chesterfield (cigarette) from Wikipedia](https://en.wikipedia.org/wiki/Chesterfield_%28cigarette%29)
- [Smoking and Cancer: Classic Film Stars Who Died of Cancer](http://www.cancerinsurance.com/blog/smoking-and-cancer-film-stars-who-died-of-cancer)
- [Chesterfield coat from Wikipedia](https://en.wikipedia.org/wiki/Chesterfield_coat)
- [Chesterfield County, South Carolina from Wikipedia](https://en.wikipedia.org/wiki/Chesterfield_County,_South_Carolina)
- [Chesterfield County, Virginia from Wikipedia](https://en.wikipedia.org/wiki/Chesterfield_County,_Virginia)
- [Chesterfield sofa from Wikipedia](https://en.wikipedia.org/wiki/Couch)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [ChessterfieldCL Download](http://home.datacomm.ch/m.luescher/download_cl.html)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Chessterfield GUI screenshot](http://home.datacomm.ch/m.luescher/screenshot.html)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Michael Buro](Michael_Buro "Michael Buro") (**1998**). *[From Simple Features to Sophisticated Evaluation Functions](http://link.springer.com/chapter/10.1007/3-540-48957-6_8)*. [CG 1998](CG_1998 "CG 1998"), [pdf](https://skatgame.net/mburo/ps/glem.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Matthias Lüscher](Matthias_L%C3%BCscher "Matthias Lüscher") (**2000**). *Automatic Generation of an Evaluation Function for Chess Endgames*. [ETH Zurich](ETH_Zurich "ETH Zurich") Supervisors: [Thomas Lincke](Thomas_Lincke "Thomas Lincke") and [Christoph Wirth](Christoph_Wirth "Christoph Wirth"), [pdf](http://www.datacomm.ch/m.luescher/evaluation_function_en.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Christoph Wirth](Christoph_Wirth "Christoph Wirth"), [Jürg Nievergelt](J%C3%BCrg_Nievergelt "Jürg Nievergelt") (**1999**). *Exhaustive and Heuristic Retrograde Analysis of the KPPKP Endgame.* [ICCA Journal, Vol. 22, No. 2](ICGA_Journal#22_2 "ICGA Journal")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a>  [Chris Wirth's endgame tablebases](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=6&t=2923) by [Denis P. Mendoza](Denis_Mendoza "Denis Mendoza"), [CCRL Endgame Tablebases](Computer_Chess_Forums "Computer Chess Forums"), December 13, 2007

**[Up one level](Engines "Engines")**

