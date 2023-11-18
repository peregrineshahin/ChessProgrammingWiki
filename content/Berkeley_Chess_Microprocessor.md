---
title: Berkeley Chess Microprocessor
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * Berkeley Chess Microprocessor**

\[ [The Campanile](https://en.wikipedia.org/wiki/Sather_Tower), UC Berkeley <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Berkeley Chess Microprocessor**, (BCM)

a chess microprocessor developed by [James Testa](James_Testa "James Testa") and [Alvin M. Despain](Alvin_M._Despain "Alvin M. Despain") at [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley") <a id="cite-note-2" href="#cite-ref-2">[2]</a> , introduced in May 1990 at the *Custom Integrated Circuits Conference* <a id="cite-note-3" href="#cite-ref-3">[3]</a>, also mentioned in [Marc Boulé's](Marc_Boul%C3%A9 "Marc Boulé") 2002 thesis <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

The BCM was a 200,000 [transistor](https://en.wikipedia.org/wiki/Transistor) [VLSI chip](VLSI_Design "VLSI Design"), 1.2 [micron](https://en.wikipedia.org/wiki/Micrometre) [CMOS](https://en.wikipedia.org/wiki/CMOS) [die](https://en.wikipedia.org/wiki/Die_%28integrated_circuit%29), 11 mm by 9 mm in area, able to [generate](Move_Generation "Move Generation") three million [legal moves](Legal_Move "Legal Move") per second. The chip incorporates a move generator, a basic [positional evaluator](Evaluation "Evaluation") and [search](Search "Search") control, can detect [pins](Pin "Pin") and [X-ray attacks](</X-ray_Attacks_(Bitboards)> "X-ray Attacks (Bitboards)"), and has an [ALU](Combinatorial_Logic#ALU "Combinatorial Logic") for each [square](Squares "Squares") to sum the values of attacking pieces to perform a kind of parallel [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") for [move ordering](Move_Ordering "Move Ordering") and [evaluation](Evaluation "Evaluation") purposes such as [mobility](Mobility "Mobility") and [square control](Square_Control "Square Control").

## Move Generation

While the [move generation](Move_Generation "Move Generation") design is similar to [Belle's](Belle "Belle"), legal move generation in hardware was already designed by Alvin Despain in the 70s, as described by [Ozalp Babaoglu](Ozalp_Babaoglu "Ozalp Babaoglu") in his 1977 thesis <a id="cite-note-5" href="#cite-ref-5">[5]</a> , but as noted by [Joe Condon](Joe_Condon "Joe Condon") and [Ken Thompson](Ken_Thompson "Ken Thompson"), never obtained funding for full construction <a id="cite-note-6" href="#cite-ref-6">[6]</a> . Both, attackers and victims, emit signals in all directions simultaneously so that it is a matter of [combinatorial logic](Combinatorial_Logic "Combinatorial Logic") in the square receivers to detect pins. [Find victim](Belle#FindVictim "Belle") and [find attacker](Belle#FindAggressor "Belle") cycles use programmable priority arbiters for [move ordering](Move_Ordering "Move Ordering") during full width as well as [quiescence search](Quiescence_Search "Quiescence Search"). A 25–level ply [stack](Stack "Stack") to enable or disable [origin-](Origin_Square "Origin Square") and [target squares](Target_Square "Target Square") keeps track of the move generation stage, and controls which move is generated next. This is how the bookkeeping works in sequential [C](C "C") like pseudo code with [Bitboards](Bitboards "Bitboards") (omitting legal move logic):

```C++

disable[ply] = depth <= 0 ? emptySquares : 0; /* enable to-squares */
while ( ( to = findMVV(disable[ply])) >= 0 ) {
  disable[ply] &= ~ownPieces;  /* enable all possible from-squares */
  while ( ( from = findLVA(disable[ply])) >= 0 ) {
    make(from, to);            /* ply++ */
    ....
    unmake(from, to);          /* ply-- */
    disable[ply] |= 1 << from; /* disable from-square */
  }
  disable[ply] |= 1 << to;     /* disable to-square */
}

```

## Zerker

The Berkeley Chess Microprocessor lacked participation in computer chess competitions. A chess entity of BCM's co-author [James Testa](James_Testa "James Testa") dubbed [Zerker](Zerker "Zerker") was registered for the [ACM 1990](ACM_1990 "ACM 1990") tournament, noted as promising newcomer, as it reported 7,000,000 moves per second <a id="cite-note-7" href="#cite-ref-7">[7]</a>, roughly three times faster than [Deep Thought](Deep_Thought "Deep Thought") at that time. Unfortunately, a damage to the machine during shipment from California forced its withdrawal <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>, and it seems the project was later abandoned.

## See also

- [Belle](Belle "Belle")
- [CHEOPS](CHEOPS "CHEOPS")
- [Zerker](Zerker "Zerker")

## Publications

- [Ozalp Babaoglu](Ozalp_Babaoglu "Ozalp Babaoglu") (**1977**). *Hardware implementation of the legal move generation and relative ordering functions for the game of chess*. Master's thesis, [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley")
- [James Testa](James_Testa "James Testa"), [Alvin M. Despain](Alvin_M._Despain "Alvin M. Despain") (**1990**). *[A CMOS VLSI chess microprocessor](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&arnumber=124744&contentType=Conference+Publications&searchWithin%3Dp_Authors%3A.QT.Testa%2C+J..QT.)*. [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley"), [IEEE](IEEE "IEEE") Custom Integrated Circuit Conference
- [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn"))

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [The Campanile](https://en.wikipedia.org/wiki/Sather_Tower) and [Mt. Tamalpais](https://en.wikipedia.org/wiki/Mount_Tamalpais) from [Memorial Stadium](https://en.wikipedia.org/wiki/California_Memorial_Stadium) at sunset, 2006 by Tristan Harward, [University of California, Berkeley - Wikipedia](https://en.wikipedia.org/wiki/University_of_California,_Berkeley)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [James Testa](James_Testa "James Testa"), [Alvin M. Despain](Alvin_M._Despain "Alvin M. Despain") (**1990**). *[A CMOS VLSI chess microprocessor](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&arnumber=124744&contentType=Conference+Publications&searchWithin%3Dp_Authors%3A.QT.Testa%2C+J..QT.)*. [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley"), [IEEE](IEEE "IEEE") Custom Integrated Circuit Conference
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Custom Integrated Circuits Conference, 1990, Proceedings of the IEEE 1990](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=140)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn")), [pdf](http://www.iml.ece.mcgill.ca/%7Emboule/files/mbthesis02.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Ozalp Babaoglu](Ozalp_Babaoglu "Ozalp Babaoglu") (**1977**). *Hardware implementation of the legal move generation and relative ordering functions for the game of chess*. Master's thesis, [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1982**). *Belle Chess Hardware*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3"), Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [The 21st Annual ACM North American Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cbb95) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1990_21st_NACCC/1990%20NACCC.062303065.sm.pdf)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Quick moves claim computer-chess title - Free Online Library](http://www.thefreelibrary.com/Quick+moves+claim+computer-chess+title.-a09145976), November 24, 1990
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Monty Newborn](Monroe_Newborn "Monroe Newborn"), [Danny Kopec](Danny_Kopec "Danny Kopec") (**1991**). *[The 21st ACM North American Computer Chess Championship](http://dl.acm.org/citation.cfm?id=125497)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 34, No. 11, [online](http://www.accessmylibrary.com/article-1G1-11640254/21st-acm-north-american.html)

**[Up one Level](Hardware "Hardware")**

