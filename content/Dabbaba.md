---
title: Dabbaba
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Dabbaba**

\[ Stone-throwing machine <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Dabbaba**,

a chess playing program by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), written from May 1995 to November 1998 in [Turbo C](C "C") to run on [PC's](IBM_PC "IBM PC") under [DOS](MS-DOS "MS-DOS") in graphics mode <a id="cite-note-2" href="#cite-ref-2">[2]</a>,
also able to play [chess variants](Chess#Variants "Chess") like [Knightmate Chess](Knightmate_Chess "Knightmate Chess") <a id="cite-note-3" href="#cite-ref-3">[3]</a>,
[Shatranj](Shatranj "Shatranj") and many others <a id="cite-note-4" href="#cite-ref-4">[4]</a>.
During its [iterative search](Iterative_Search "Iterative Search") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>,
maintaining a [ply](Ply "Ply") [stack](Stack "Stack") of irreversible aspects of the [position](Chess_Position "Chess Position"), that is [castling rights](Castling_Rights "Castling Rights"), [en passant target](En_passant "En passant"), [halfmove clock](Halfmove_Clock "Halfmove Clock"), and hash-keys,
it updates its [mailbox board](Mailbox "Mailbox") and [piece-lists](Piece-Lists "Piece-Lists") [incrementally](Incremental_Updates "Incremental Updates") during [make](Make_Move "Make Move") and [unmake move](Unmake_Move "Unmake Move").
A feature of Dabbaba is that it starts its search by using up to 20% of the allotted time for a move using a [mate search](Mate_Search "Mate Search") at [depth](Depth "Depth") zero,
following long sequences of [checks](Check "Check") to see if it results in a [mate](Checkmate "Checkmate"), [material](Material "Material") gain or perhaps a saving [draw](Draw "Draw").
To avoid a [search explosion](Search_Explosion "Search Explosion"), Dabbaba considers ply-distance to the [root](Root "Root") and number of replies so that shallow lines are searched deeper than wide lines <a id="cite-note-7" href="#cite-ref-7">[7]</a>.
In May 2008, [Jim Ablett](Jim_Ablett "Jim Ablett") released a [WinBoard](WinBoard "WinBoard") version of Dabbaba <a id="cite-note-8" href="#cite-ref-8">[8]</a>,
and in August 2012, Jens Bæk Nielsen as well <a id="cite-note-9" href="#cite-ref-9">[9]</a>.

## Etymology

The [Dabbaba](https://en.wikipedia.org/wiki/Dabbaba_%28chess%29) (or dabaaba, dabbabah) is a [Fairy chess piece](https://en.wikipedia.org/wiki/Fairy_chess_piece) that jumps two squares orthogonally, leaping over intermediate pieces like a [knight](Knight "Knight"), also called [(2,0)-leaper](https://en.wikipedia.org/wiki/Fairy_chess_piece#Leapers).
The [Arabic](https://en.wikipedia.org/wiki/Arabic_language) word [dabbāba](https://en.wikipedia.org/wiki/Dabb%C4%81ba) formerly meant a type of [medieval siege engine](https://en.wikipedia.org/wiki/Siege_engine#Medieval_siege_engines), and nowadays an [army tank](https://en.wikipedia.org/wiki/Tank).

## Screenshot

[](http://www.jens-musik.dk/skak.htm)
Dabbaba Screen <a id="cite-note-10" href="#cite-ref-10">[10]</a>

## Forum Posts

- [Dabbaba needs an openingbook](https://www.stmintz.com/ccc/index.php?id=19369) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), May 27, 1998 » [Opening Book](Opening_Book "Opening Book")
- [Dabbaba 0.98 with Winboard support available](http://www.talkchess.com/forum/viewtopic.php?t=21051) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), May 08, 2008
- [Re: agChess -- an agressive chess variant](http://www.talkchess.com/forum/viewtopic.php?t=22588&start=8) by [H.G.Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 26, 2008
- [Dabbaba 6.50 has been released](http://www.talkchess.com/forum/viewtopic.php?t=44802) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), August 15, 2012
- [Dabbaba And The Cupcake](http://www.talkchess.com/forum/viewtopic.php?t=44807) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), August 16, 2012
- [True iterative search...](http://www.talkchess.com/forum/viewtopic.php?t=46175) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), November 27, 2012 » [Iterative Search](Iterative_Search "Iterative Search")
- [Having fun with the evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=46689) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), December 31, 2012 » [Evaluation](Evaluation "Evaluation")
- [Human killer engine - a cafè-monster](http://www.talkchess.com/forum/viewtopic.php?t=47165) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), February 09, 2013

## External Links

## Chess Engine

- [Chess / Skak](http://www.jens-musik.dk/skak.htm) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen")
- [Dabbaba](http://www.jens-musik.dk/dabbaba.htm) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen")

[DABBABA.C](http://www.jens-musik.dk/DABBABA.C)

- [The Chess Variant Pages - Dabbaba](https://www.chessvariants.com/programs.dir/dabbaba.html)
- [Dabbaba](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Dabbaba&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRl 40/4](CCRL "CCRL")

## Dabbaba

- [Dabbaba (chess) from Wikipedia](https://en.wikipedia.org/wiki/Dabbaba_%28chess%29)
- [Fairy chess piece from Wikipedia](https://en.wikipedia.org/wiki/Fairy_chess_piece)
- [Dabbāba (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Dabb%C4%81ba)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A [stone-throwing machine](https://en.wikipedia.org/wiki/Siege_engine) set to defend a gate, in the fresco of [Guidoriccio da Fogliano](https://en.wikipedia.org/wiki/Guidoriccio_da_Fogliano) by [Simone Martini](https://en.wikipedia.org/wiki/Simone_Martini) (14th century), [Siege engine from Wikipedia](https://en.wikipedia.org/wiki/Siege_engine)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Turbo C Graphics - initgraph function](http://www.softwareandfinance.com/Turbo_C/Graphics/initgraph.html)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: agChess -- an agressive chess variant](http://www.talkchess.com/forum/viewtopic.php?t=22588&start=8) by [H.G.Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 26, 2008
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [The Chess Variant Pages - Dabbaba](http://www.chessvariants.org/programs.dir/dabbaba.html)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [comp.lang.c FAQ list · Question 17.10](http://c-faq.com/style/stylewars.html)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Spaghetti code from Wikipedia](https://en.wikipedia.org/wiki/Spaghetti_code)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Dabbaba](http://www.jens-musik.dk/dabbaba.htm) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen")
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Dabbaba 0.98 with Winboard support available](http://www.talkchess.com/forum/viewtopic.php?t=21051) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), May 08, 2008
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Dabbaba 6.50 has been released](http://www.talkchess.com/forum/viewtopic.php?t=44802) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), August 15, 2012
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Chess / Skak](http://www.jens-musik.dk/skak.htm) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen")

**[Up one Level](Engines "Engines")**

