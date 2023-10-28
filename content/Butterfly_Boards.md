---
title: Butterfly Boards
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * Butterfly Boards**

[](http://www.mcescher.com/Gallery/symmetry-bmp/E70.jpg) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Symmetry <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Butterfly Boards**,

two-dimensional [arrays](Array "Array") (typically of various history counters for each color), indexed by the [from-](Origin_Square "Origin Square") and [to-square](Target_Square "Target Square") coordinates of (valid and likely [quiet](Quiet_Moves "Quiet Moves")) [moves](Moves "Moves"), which appear inside the [search](Search "Search"). Those counters can then be used for [move ordering](Move_Ordering "Move Ordering") as mentioned in the [history heuristic](History_Heuristic "History Heuristic"), or to decide about [late move reductions](Late_Move_Reductions "Late Move Reductions") and [history leaf pruning](History_Leaf_Pruning "History Leaf Pruning"). Another application is a kind of [killer-](Killer_Heuristic "Killer Heuristic") or [refutation table](Refutation_Table "Refutation Table"), to store a refutation of a specific move <a id="cite-note-2" href="#cite-ref-2">[2]</a>, also base of the [countermove heuristic](Countermove_Heuristic "Countermove Heuristic") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Contents

- [1 Layout](#layout)
- [2 Valid Entries](#valid-entries)
- [3 The Eponym](#the-eponym)
- [4 The Butterfly](#the-butterfly)
  - [4.1 Single Shape](#single-shape)
  - [4.2 Connected Shapes](#connected-shapes)
- [5 C-Code](#c-code)
- [6 Analogy in Astronomy](#analogy-in-astronomy)
- [7 See also](#see-also)
- [8 Publications](#publications)
- [9 External links](#external-links)
  - [9.1 Wikipedia](#wikipedia)
  - [9.2 Misc](#misc)
- [10 References](#references)

## Layout

The size of the [array](Array "Array") is 4K (64 x 64 = 4096) elements for each color, but the density is poor, since most [from-](Origin_Square "Origin Square") and [to-square](Target_Square "Target Square") combinations are illegal moves by the rules of chess. Thus, most entries inside the Butterfly boards are not used. Also, as an additional drawback, from-to coordinates, specially those with [distance](Distance "Distance") one, are ambiguous and may be legal for several [pieces](Pieces "Pieces"). For instance e2-e3 might be a rook-, queen-, king- or white pawn-move. However, knight-, rook- and bishop moves are disjoint, queen moves are the superset from rook- and bishop-moves, king-moves the one-distance subset of queen moves, and [pawn pushes](Pawn_Push "Pawn Push") are subset of rook-moves, while pawn captures and [en passant](En_passant "En passant") (if stored at all) are subset of bishop-moves.

Therefor some programmers omit the origin from-square, but use piece-type instead for denser 12 x 64 tables with only 3/4K entries - or exclude not only captures, but also pawn pushes and/or king moves. Other programmers have abandoned hashing moves for [History Heuristic](History_Heuristic "History Heuristic") and [LMR](Late_Move_Reductions "Late Move Reductions"), and say that given enough search depth, History counters produce just some random noise <a id="cite-note-5" href="#cite-ref-5">[5]</a> .

This is how butterfly boards may be declared in [C](C "C") or [C++](Cpp "Cpp"):

```

counterType arrWhiteButterfly[64][64]; // from, to -> 4K
counterType arrBlackButterfly[64][64]; // from, to -> 4K

```

or

```

counterType arrButterfly[2][64][64]; // color, from, to -> 8K

```

## Valid Entries

As mentioned in [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces"), there are only 1792 (7/16 of 4K) possible valid moves coordinates, 9/16 of the space in the Butterfly boards is "wasted".

|  Piece
|  covers other pieces
|  #
|  div (7\*16)
|
| --- | --- | --- | --- |
|  Rook
|  queen, king and pawn pushes
|  896
|  8
|
|  Bishop
|  queen, king and pawn captures
|  560
|  5
|
|  Knight
|  -
|  336
|  3
|
|  possible from-to move coordinates
|  1792
|  16
|

## The Eponym

The name Butterfly Boards was proposed by [Dap Hartmann](Dap_Hartmann "Dap Hartmann") in 1988, when he introduced the [Butterfly Heuristic](Butterfly_Heuristic "Butterfly Heuristic") in the [ICCA Journal](ICGA_Journal "ICGA Journal") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, and the application of a Butterfly [refutation table](Refutation_Table "Refutation Table") at the [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6") conference in 1990 <a id="cite-note-7" href="#cite-ref-7">[7]</a>. Plotting the illegal move coordinates as black cells **#** inside a 64\*64 sheet, seven [butterfly](https://en.wikipedia.org/wiki/Butterfly) shaped pattern appear along the impossible move diagonal (where squares are equal).

## The Butterfly

## Single Shape

The [thorax](https://en.wikipedia.org/wiki/Thorax) of the Butterfly is centered by the wraps from one rank (or dependent on the [Square Mapping Considerations](Square_Mapping_Considerations "Square Mapping Considerations"), one file) to the next one. With 'a1' as square null mapping, and 'd1' as square 3, 'e2' is square 12, the shape indexed by square coordinates looks as follows, covering two wrapped rank "halfs" including their center files, e.g. d1 - e2:

```

d e f g h a b c d e        d e f g h a b c d e
1 1 1 1 1 2 2 2 2 2        1 1 1 1 1 2 2 2 2 2
##         #           d1   # - - - - # ~ \ | /
  #       # #         e1   - # - - - # # ~ \ |
    #     # # #       f1   - - # - - # # # ~ \
      #   # # # #     g1   - - - # - # # # # ~
        # # # # # #   h1   - - - - # # # # # #
## # # # # #           a2   # # # # # # - - - -
  # # # #   #         b2   ~ # # # # - # - - -
    # # #     #       c2   \ ~ # # # - - # - -
      # #       #     d2   | \ ~ # # - - - # -
        #         #   e2   / | \ ~ # - - - - #

```

That is why Dap Hartmann called it Butterfly Boards.

## Connected Shapes

- one butterfly spans a 10 square range
- n butterflies span an 8\*n + 2 square range
- seven butterflies span 58 square range, from 3 (d1) to 60 (e8)

```

d e f g h a b c d e f g h a b c d e       d e f g h a b c d e f g h a b c d e
1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3       1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3
##         #                          d1   # - - - - # ~ \ | / ~ # # # \ ~ | ~
  #       # #                        e1   - # - - - # # ~ \ | / ~ # # # \ ~ |
    #     # # #                      f1   - - # - - # # # ~ \ | / ~ # # # \ ~
      #   # # # #                    g1   - - - # - # # # # ~ \ | / # # # # \
        # # # # # #                  h1   - - - - # # # # # # ~ \ | # # # # #
## # # # # #                          a2   # # # # # # - - - - - - - | / ~ # #
  # # # #   #                        b2   ~ # # # # - # - - - - - - \ | / ~ #
    # # #     #                      c2   \ ~ # # # - - # - - - - - ~ \ | / ~
      # #       #         #          d2   | \ ~ # # - - - # - - - - # ~ \ | /
        #         #       # #        e2   / | \ ~ # - - - - # - - - # # ~ \ |
                    #     # # #      f2   ~ / | \ ~ - - - - - # - - # # # ~ \
                      #   # # # #    g2   # ~ / | \ - - - - - - # - # # # # ~
                        # # # # # #  h2   # # ~ / | - - - - - - - # # # # # #
                # # # # # #          a3   # # # # # | \ ~ # # # # # # - - - -
                  # # # #   #        b3   \ # # # # / | \ ~ # # # # - # - - -
                    # # #     #      c3   ~ \ # # # ~ / | \ ~ # # # - - # - -
                      # #       #    d3   | ~ \ # # # ~ / | \ ~ # # - - - # -
                        #         #  e3   ~ | ~ \ # # # ~ / | \ ~ # - - - - #

```

## C-Code

Some arbitrary [C](C "C")-code, to produce the plot:

```

##include "stdafx.h"
##include <math.h>

void butterflyBoard(int from, int to) {
   int sq1, sq2, f1, f2, r1, r2, df, dr;
   int nr = 0, nb = 0, nn = 0;
   for (sq2 = from; sq2 <= to; sq2++)
      printf("%c", (sq2 % 10) ? ' ' : '0' + (sq2/10) );
   printf("\n");
   for (sq2 = from; sq2 <= to; sq2++)
      printf("%1d", sq2 % 10 );
   printf("\n");
   for (sq1 = from; sq1 <= to; sq1++) {
      for (sq2 = from; sq2 <= to; sq2++) {
         if ( sq1 != sq2 ) {
            r1 = sq1 >> 3;
            r2 = sq2 >> 3;
            if (r1 == r2) { // same rank
               nr++;
               printf("-");
               continue;
            }
            f1 = sq1 & 7;
            f2 = sq2 & 7;
            if ( f1 == f2 ) { // same file
               nr++;
               printf("|");
               continue;
            }
            if  (f1 - r1 == f2 - r2) { // same diagonal
               nb++;
               printf("/");
               continue;
            }
            if  (f1 + r1 == f2 + r2) { // same anti-diagonal
               nb++;
               printf("\\");
               continue;
            }
            df = abs (f2 - f1);
            dr = abs (r2 - r1);
            if ( df + dr == 3 )    { // knight distance
               nn++;
               printf("~");
               continue;
            }
         }
         printf("#"); // invalid
      }
      printf(" %2d\n", sq1);
   }
   printf("rook   moves %4d\n", nr);
   printf("bishop moves %4d\n", nb);
   printf("knight moves %4d\n", nn);
   printf("total  moves %4d\n", nr + nb + nn);
}

int main(int argc, char* argv[])
{
   butterflyBoard(3, 20); // 0, 63
   return 0;
}

```

## Analogy in Astronomy

[Dap Hartmann](Dap_Hartmann "Dap Hartmann") found a nice analogy in astronomy. [Edward Maunders](https://en.wikipedia.org/wiki/Edward_Walter_Maunder) was the first astronomer (1904) to plot the distribution in [heliographic latitude](http://www.answers.com/topic/heliographic-latitude) of the centers of [sunspot groups](http://www.ips.gov.au/Educational/2/2/3) as a functions of time:

\[
A modern version of the Mauders' sunspot "butterfly diagram" <a id="cite-note-8" href="#cite-ref-8">[8]</a> .

## See also

- [Bobby's Strategic Quiescence Search](Bobby#StrategicQuiescenceSearch "Bobby")
- [Butterfly Heuristic](Butterfly_Heuristic "Butterfly Heuristic")
- [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
- [History Heuristic](History_Heuristic "History Heuristic")
- [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Monarch](Monarch "Monarch")
- [Refutation Table](Refutation_Table "Refutation Table")
- [Relative History Heuristic](Relative_History_Heuristic "Relative History Heuristic")

## Publications

- [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1983**). *The History Heuristic*. [ICCA Journal, Vol. 6, No. 3](ICGA_Journal#6_3 "ICGA Journal")
- [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1988**). *Butterfly Boards*. [ICCA Journal, Vol. 11, Nos. 2/3](ICGA_Journal#11_23 "ICGA Journal")
- [Dap Hartmann](Dap_Hartmann "Dap Hartmann"), [Peter Kouwenhoven](Peter_Kouwenhoven "Peter Kouwenhoven") (**1991**). *Sundry Computer Chess Topics*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
- [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal")

## External links

## Wikipedia

Butterflies from [Wikipedia](https://en.wikipedia.org/wiki/Home) <a id="cite-note-9" href="#cite-ref-9">[9]</a>

- [Butterfly insect](https://en.wikipedia.org/wiki/Butterfly) of the order [Lepidoptera](https://en.wikipedia.org/wiki/Lepidoptera)
- [Butterfly Game](https://en.wikipedia.org/wiki/Butterfly_%28game%29) a [two-player abstract strategy game](https://en.wikipedia.org/wiki/Abstract_strategy_game) from [Mozambique](https://en.wikipedia.org/wiki/Mozambique)
- [BBN Butterfly](https://en.wikipedia.org/wiki/BBN_Butterfly) a massively parallel computer from the 1980s
- [Butterfly diagram](https://en.wikipedia.org/wiki/Butterfly_diagram) in the context of [fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) <a id="cite-note-10" href="#cite-ref-10">[10]</a> algorithms
- [Butterfly or Zassenhaus lemma](https://en.wikipedia.org/wiki/Zassenhaus_lemma)
- [Schmetterlingsgraph](http://de.wikipedia.org/wiki/Schmetterlingsgraph) (German)
- [Butterfly knot](https://en.wikipedia.org/wiki/Butterfly_knot)
- [Butterfly theorem](https://en.wikipedia.org/wiki/Butterfly_theorem) in elementary geometry
- [Butterfly curve (algebraic)](https://en.wikipedia.org/wiki/Butterfly_curve_%28algebraic%29)
- [Butterfly curve (transcendental)](https://en.wikipedia.org/wiki/Butterfly_curve_%28transcendental%29)
- [Butterfly catastrophe](https://en.wikipedia.org/wiki/Butterfly_catastrophe#Butterfly_catastrophe) Catastrophe theory
- [Butterfly options](https://en.wikipedia.org/wiki/Butterfly_%28options%29) a combination option trade strategy
- [Iron Butterfly spread](https://en.wikipedia.org/wiki/Iron_Butterfly_Spread)
- [Iron Butterfly (band)](https://en.wikipedia.org/wiki/Iron_Butterfly)
- [Butterfly ballot](https://en.wikipedia.org/wiki/Butterfly_ballot#Design)
- [Butterfly effect](https://en.wikipedia.org/wiki/Butterfly_effect) in the context of [Chaos theory](https://en.wikipedia.org/wiki/Chaos_theory)
- [The Butterfly Effect (Film)](https://en.wikipedia.org/wiki/The_Butterfly_Effect)
- [The Butterfly Effect (band)](https://en.wikipedia.org/wiki/The_Butterfly_Effect_%28band%29)

## Misc

- [Herbie Hancock](Category:Herbie_Hancock "Category:Herbie Hancock") & [The Headhunters](Category:The_Headhunters "Category:The Headhunters"), [Butterfly](https://en.wikipedia.org/wiki/Thrust_%28album%29), 1974, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Picture gallery "Symmetry"](http://www.mcescher.com/Gallery/gallery-symmetry.htm) from [The Official M.C. Escher Website](http://www.mcescher.com/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Dap Hartmann](Dap_Hartmann "Dap Hartmann"), [Peter Kouwenhoven](Peter_Kouwenhoven "Peter Kouwenhoven") (**1991**). *Sundry Computer Chess Topics*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: History pruning / move ordering question](http://www.talkchess.com/forum/viewtopic.php?t=47953&start=2) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 10, 2013
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: LMR: history or not?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=163477&t=18345) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") from [CCC](Computer_Chess_Forums "Computer Chess Forums"), December 13, 2007
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1988**). *Butterfly Boards*. [ICCA Journal, Vol. 11, Nos. 2/3](ICGA_Journal#11_23 "ICGA Journal")
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Dap Hartmann](Dap_Hartmann "Dap Hartmann"), [Peter Kouwenhoven](Peter_Kouwenhoven "Peter Kouwenhoven") (**1991**). *Sundry Computer Chess Topics*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Edward Walter Maunder, Solar observations](https://en.wikipedia.org/wiki/Edward_Walter_Maunder#Solar_observations) A modern version of the Mauders' sunspot "butterfly diagram". (This version from the solar group at NASA Marshall Space Flight Center.)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Butterfly (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Butterfly_%28disambiguation%29)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Fast Fourier Transform (FFT)](http://www.relisoft.com/Science/Physics/fft.html) from [Reliable Software](http://www.relisoft.com/index.htm)

**[Up one Level](Data "Data")**

