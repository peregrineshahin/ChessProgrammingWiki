---
title: Joker IT
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Joker IT**



[ A Joker card <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Joker**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Manlio Morini](Manlio_Morini "Manlio Morini"), developed from 1998 until 2001, 
written in [C++](Cpp "Cpp") with some conditional [x86](X86 "X86") [inline assembly](Assembly#InlineAssembly "Assembly") concerning [population count](Population_Count "Population Count") and [bitscan](BitScan "BitScan") of [bitboards](Bitboards "Bitboards"). 
Joker runs under [BSD](Unix "Unix"), [Linux](Linux "Linux") and [Windows](Windows "Windows"), and was in 2017 published on [GitHub](https://en.wikipedia.org/wiki/GitHub) as [open source](Category:Open_Source "Category:Open Source") as "historical" artifact, 
under the terms of the [MIT license](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### Contents


* [1 Description](#description)
* [2 Features](#features)
	+ [2.1 Board Representation](#board-representation)
	+ [2.2 Search](#search)
	+ [2.3 Evaluation](#evaluation)
	+ [2.4 Misc](#misc)
* [3 Namesake](#namesake)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
	+ [6.1 Chess Engine](#chess-engine)
	+ [6.2 Misc](#misc-2)
* [7 References](#references)






During its lifetime, around Version 0.6.7 in 1999, Joker used [MTD(f)](MTD(f) "MTD(f)") along with [ETC](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, but finally stuck with [PVS](Principal_Variation_Search "Principal Variation Search") and [aspiration](Aspiration_Windows "Aspiration Windows") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. It initially used the [0x88](0x88 "0x88") [board representation](Board_Representation "Board Representation") but evolved to [bitboards](Bitboards "Bitboards"). Quiet [move generation](Move_Generation "Move Generation") of [sliding pieces](Sliding_Pieces "Sliding Pieces") is still done with a nested loop over [directions](Direction "Direction") with pre-increments of [origin](Origin_Square "Origin Square") until [target squares](Target_Square "Target Square") are empty <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 




```

  // Mosse di Alfiere, Torre, Donna.
  for (pezzo pz(alfiere); pz <= donna; ++pz) {
    bb = mappa(c,pz);
    while (bb) {
      const posizione pos(bb.firstone());
      for (const direzione *d = dir[pz]; *d; d++) {
        for (posizione arrivo(pos + *d);
             !arrivo.fuori() && libere[arrivo];
             arrivo += *d) {
          lm->push_back(pos,arrivo,pz,vuoto);
        }
      }
      bb.elimina(pos);
    }
  }

```

However, the more time critical [capture](Captures "Captures") generation is implemented more in the set-wise bitboard fashion similar to the [Tinker](Tinker "Tinker") approach, [traversing](Bitboard_Serialization "Bitboard Serialization") the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") on the [otherwise empty board](On_an_empty_Board "On an empty Board") with opponent pieces, and looking whether the [squares inbetween](Square_Attacked_By#InBetween "Square Attacked By") the sliding [origin](Origin_Square "Origin Square") and potential capture [target](Target_Square "Target Square") are empty .




```

  // Catture di Alfiere, Torre, Donna.
  for (pezzo pz(alfiere); pz <= donna; ++pz) {
    bb = mappa(c,pz);
    while (bb) {
      const posizione pos(bb.firstone());
      const bitboard *const a = bitboard::raggio[pos];
      bitboard prede(mosse[pz][pos] & nemici);
      while (prede) {
        const posizione p_preda(prede.firstone());
        if ( !(a[p_preda] & pezzi) ) {
          const pezzo preda(t_preda(!c,p_preda));
          lm->push_back(pos,p_preda,pz,preda,cattura);
        }
        prede.elimina(p_preda);
      }
      bb.elimina(pos);
    }
  }

```

## Features


### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [PVS](Principal_Variation_Search "Principal Variation Search") [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Transposition Table](Transposition_Table "Transposition Table")
* [History Heuristic](History_Heuristic "History Heuristic")
* [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Fractional Extensions](Extensions#FractionalExtensions "Extensions")
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [MVV/LVA](MVV-LVA "MVV-LVA")


### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")
* [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [King Safety](King_Safety "King Safety")


### Misc


* [Opening Book](Opening_Book "Opening Book")
* [Book Learning](Book_Learning "Book Learning")
* [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")


## Namesake


* [Joker](Joker "Joker") by [Marc-François Baudot](Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot") and [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill")
* [Joker](Joker_NL "Joker NL") by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")


## See also


* [Jester](Jester "Jester") by [Stéphane Nguyen](St%C3%A9phane_Nguyen "Stéphane Nguyen")
* [Jester](Jester_US "Jester US") by [Marty Franz](Marty_Franz "Marty Franz")


## Forum Posts


* [Joker (WB) by Manlio Morini](http://www.talkchess.com/forum/viewtopic.php?t=65146) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), September 12, 2017


## External Links


### Chess Engine


* [Joker - EOS Development](http://www.eosdev.it/joker/)
* [GitHub - morinim/joker: A chess engine from '90s](https://github.com/morinim/joker)


### Misc


* [Joker disambiguation page from Wikipedia](https://en.wikipedia.org/wiki/Joker)
* [Joker (playing card) from Wikipedia](https://en.wikipedia.org/wiki/Joker_%28playing_card%29)
* [Joker (comics) from Wikipedia](https://en.wikipedia.org/wiki/Joker_%28comics%29)
* [Joker (comic book) from Wikipedia](https://en.wikipedia.org/wiki/Joker_%28comic_book%29)
* [Gata Jazz Quartet](https://fandalism.com/mrskylark1987/bw0i) - The Joker, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The Jolly Rosso](https://commons.wikimedia.org/wiki/File:The_Jolly_Rosso.jpg), image by [Trocche100](https://it.wikipedia.org/wiki/Utente:Trocche100), November 30, 2014, [Joker (playing card) from Wikipedia](https://en.wikipedia.org/wiki/Joker_%28playing_card%29), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [joker/README.md at master · morinim/joker · GitHub](https://github.com/morinim/joker/blob/master/README.md)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [joker/history at master · morinim/joker · GitHub](https://github.com/morinim/joker/blob/master/doc/history)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [joker/giocatore.cc at master · morinim/joker · GitHub](https://github.com/morinim/joker/blob/master/src/giocatore.cc), see Ricerca\_radice (root search)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Code snippets from [joker/situazione.cc at master · morinim/joker · GitHub](https://github.com/morinim/joker/blob/master/src/situazione.cc), slightly formatted concerning white spaces and brackets

**[Up one Level](Engines "Engines")**







 
