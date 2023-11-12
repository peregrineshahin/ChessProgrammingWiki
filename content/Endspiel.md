---
title: Endspiel
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Endspiel**

**Endspiel**,

a [Windows](Windows "Windows") chess program and explanation tool dedicated for simple [Endgames](Endgame "Endgame"), written by [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") in the 90s.
Endspiel combines rule-based [knowledge](Knowledge "Knowledge") with a modified [alpha-beta](Alpha-Beta "Alpha-Beta") search to generate explanations.
The rules cover a large part of the positions of an endgame. For each such position they define a [score](Score "Score") interval guaranteed to contain the true value.
Multiple rules may be applied, resulting in the intersection and narrowing of intervals.
Further, an [alpha-beta](Alpha-Beta "Alpha-Beta") search finds the values for all positions not covered and removes uncertainties
left by too wide intervals in rule-scored positions. Thus, the method yields a correct evaluation for every position and.
furthermore, the rules governing the position of its successors provide some tutorial insight to the user about the reasons behind the evaluations.
Moreover, automatic validation assures that mistakes in the rules will be discovered and then can be eliminated in dialogue
<a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## Rules

For a specific endgame, e.g. [KPK](KPK "KPK"), KQKQ, [KQKP](Queen_versus_Pawn "Queen versus Pawn"), or [KPKP](index.php?title=KPKP&action=edit&redlink=1 "KPKP (page does not exist)"),
a system of rules is developed, which decides for the positions whether they are won, drawn or lost. The remainder of the positions may be left undecided.
The rules may be arranged by [decision trees](https://en.wikipedia.org/wiki/Decision_tree) <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>,
or they may be examined sequentially until applicable to the position involved <a id="cite-note-4" href="#cite-ref-4">[4]</a>.
The rules consist of conditions to match and associated [score](Score "Score") intervals which may express some uncertainty.
A winning position obtains the value of (maxval - k), where maxval is a huge positive integer, i.e. minus [mate score](Checkmate#MateScore "Checkmate"), and k the minimum of

- number of plies on the shortest path to [mate](Checkmate "Checkmate"), and
- minimal number of plies ending with an irreversible move on the winning path

For instance in [KPK](KPK "KPK") (BTM), the case of [opposition](Opposition "Opposition") on the same file, white king on the [stop square](Stop_Square "Stop Square"),
the interval is defined by value\[maxval-8, maxval-4\].

## KPKP

In his 1995 [ICCA Journal](ICGA_Journal#18_3 "ICGA Journal") article on KPKP with [passed pawns](Passed_Pawn "Passed Pawn") <a id="cite-note-5" href="#cite-ref-5">[5]</a>,
Wilhelm Barth elaborates on following six rules applied in his Endspiel program, along with several examples.

|  #
|  Description
|  Conditions
|  Assessment
|
| --- | --- | --- | --- |
|  1
|  wP can promote without support ofits king and bP is blocked
|  ♚∉[□](Rule_of_the_Square "Rule of the Square") ∧ ♔∈[⤋](Pawn_Spans "Pawn Spans") |  White wins
|
|  2
|  wK stops bP definitely
|  ♔∈[■](Rule_of_the_Square "Rule of the Square") ∧ ([D (♔,♟)](Distance "Distance") \< [D (♚,♟)](Distance "Distance") ∨ [D (♔](Distance "Distance"),[🛑)](Stop_Square#Tele "Stop Square") \< [D (♚](Distance "Distance"),[🛑)](Stop_Square#Tele "Stop Square"))
|  White achieves at least a draw
|
|  3
|  wp reaches promotion before bP does
|  𝒘 ::= [D (♙](Distance "Distance"),[♕)](Promotion_Square "Promotion Square") - [D (♟](Distance "Distance"),[♛)](Promotion_Square "Promotion Square")
𝒘 >= 3 usually wins, but 8/3K4/4P3/5p2/8/8/8/5k2 w - -
𝒘 == 2 usually wins, but [rook and bishop pawn cases](Queen_versus_Pawn "Queen versus Pawn")
𝒘 == 1 often wins, but more exceptions with other pawn files
𝒘 == 0 normally draw, but some [skewer](Skewer "Skewer") cases that win
𝒘 == -1 despite exceptional drawn positions, left without evaluation
|  White wins or achieves a draw dependingon 𝒘 and some other conditions
|
|  4
|  wk stops bP definitely after wPhas attracted the bK
|  (𝒘 > 0 ∨ (𝒘 == 0 ∧ ♟[♛](Promotion_Square "Promotion Square"))) ∧ ♚∈[□](Rule_of_the_Square "Rule of the Square") ⇒ [rule 2](#r2) |  White achieves at least a draw
|
|  5
|  with support of its King, wP promotesbefore bP does
|  conditions similar to rule 3
|  White wins or achieves a draw dependingon 𝒘 and some other conditions
|
|  6
|  bP is unstoppable and bK stops wPand wK cannot parry both threats
|  addresses [Réti Endgame Study](R%C3%A9ti_Endgame_Study "Réti Endgame Study") |  Black wins
|

Symbols:

- ∧ - and
- ∨ - or
- ∈ / ∉ - Element of / Not Element of
- ■, □ - [Square of The White, Black Pawn](Rule_of_the_Square "Rule of the Square")
- ⤋ - Black [Pawn's Front Span](Pawn_Spans "Pawn Spans")
- D - [Chebyshev Distance](Distance "Distance")
- 🛑 - Black Pawn's [Tele Stop](Stop_Square#Tele "Stop Square")
- ♕ / ♛ - White / Black Pawn's [Promotion Square](Promotion_Square "Promotion Square")
- !+ - No [Check](Check "Check") after Queening

## See also

- [Chunker](Chunker "Chunker")
- [KQKP](Queen_versus_Pawn "Queen versus Pawn")
- [KPK](KPK "KPK")
- [Pawn Endgame](Pawn_Endgame "Pawn Endgame")

## Selected Publications

- [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth"), [Stephan Barth](index.php?title=Stephan_Barth&action=edit&redlink=1 "Stephan Barth (page does not exist)") (**1991**). *Programme für korrekte Schachendspiele und deren Validierung*. Institutsbericht, Nr. 34. Institut für Computergraphik, [TU Wien](Vienna_University_of_Technology "Vienna University of Technology") (German)
- [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth"), [Stephan Barth](index.php?title=Stephan_Barth&action=edit&redlink=1 "Stephan Barth (page does not exist)") (**1992**). *Validating a Range of Endgame Programs*. [ICCA Journal, Vol. 15, No. 3](ICGA_Journal#15_3 "ICGA Journal") <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") (**1994**). *Computerschach - Ein korrektes Programm für das Endspiel König und Bauer gegen König und Bauer - Unterteilung von Endspielen in Klassen - Behandlung der Stellungswiederholung bei der Intervallbewertung*. Institutsbericht Nr. 36, Institut für Computergraphik, [TU Wien](Vienna_University_of_Technology "Vienna University of Technology") (German)
- [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") (**1995**). *Combining Knowledge and Search to Yield Infallible Endgame Programs A study of passed Pawns in the KPKP endgame.* [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal")
- [Steven Edwards](Steven_Edwards "Steven Edwards") (**1995**). *Comments on Barth’s Article “Combining Knowledge and Search to Yield Infallible Endgame Programs.”* [ICCA Journal, Vol. 18, No. 4](ICGA_Journal#18_4 "ICGA Journal")
- [Heinz Herbeck](Heinz_Herbeck "Heinz Herbeck"), [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") (**1996**). *An Explanation Tool for Chess Endgames Based on the Rule Method*. [ICCA Journal, Vol. 19, No. 2](ICGA_Journal#19_2 "ICGA Journal")

## External Links

- [Neues Schachprogramm für Spezialprobleme](https://idw-online.de/de/news4179), October 28, 1996 (German)
- [Computer Chess site (Barth, Herbeck)](https://web.archive.org/web/20130612090002/https://www.ads.tuwien.ac.at/research/Chess.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") (**1995**). *Combining Knowledge and Search to Yield Infallible Endgame Programs A study of passed Pawns in the KPKP endgame.* [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Ross Quinlan](Ross_Quinlan "Ross Quinlan") (**1983**). *[Learning Efficient Classification Procedures and Their Application to Chess End Games](https://link.springer.com/chapter/10.1007/978-3-662-12405-5_15)*. [Machine Learning: An Artificial Intelligence Approach](https://link.springer.com/book/10.1007%2F978-3-662-12405-5)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Gerhard Mehlsam](Gerhard_Mehlsam "Gerhard Mehlsam"), [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") (**1991**). *[Feature Construction during Tree Learning](https://link.springer.com/chapter/10.1007/978-3-662-02711-0_6)*. [GWAI 1991](https://dblp.uni-trier.de/db/conf/ki/gwai91.html)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1983**). *[Representation of Experts' Knowledge in a Subdomain of Chess Intelligence](https://www.semanticscholar.org/paper/Representation-of-Experts'-Knowledge-in-a-Subdomain-Herik/5f29c029a69f2d69980da4b35402050203421ed4)*. [IJCAI 1983](Conferences#IJCAI1983 "Conferences")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") (**1995**). *Combining Knowledge and Search to Yield Infallible Endgame Programs A study of passed Pawns in the KPKP endgame*. [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Ulrich Thiemonds](Ulrich_Thiemonds "Ulrich Thiemonds") (**1999**). *Ein regelbasiertes Spielprogramm für Schachendspiele*. [University of Bonn](https://en.wikipedia.org/wiki/University_of_Bonn), Diplom thesis (German)

**[Up one level](Engines "Engines")**

