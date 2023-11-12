---
title: Chess Query Language
---
**[Home](Home "Home") * [Chess](Chess "Chess") * Chess Query Language**

The **Chess Query Language** (CQL) is a structured [query language](https://en.wikipedia.org/wiki/Query_language) to search for games, problems, and studies that match specific themes from a collection in [Portable Game Notation](Portable_Game_Notation "Portable Game Notation"). CQL was developed by [Gady Costeff](Gady_Costeff "Gady Costeff") and [Lewis Stiller](Lewis_Stiller "Lewis Stiller"). It is Copyright (c) 2003-2021 and is free. The current version is **6.1** and the documentation and download of the executable can be found on the website of Gady Costeff <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## Sample query

<a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>

```C++

;; look for positions where a rook circles in a 4x3 rectangle
;; we use the rectangle g2, d2, d6, g6 together with shift and flip
;;
(match :pgn input.pgn
       :output output.pgn
       :forany piece [Rr]
       (position
        $piece[g2]
        :and (
              (position :gappedsequence ((position :movefrom $piece[g6,d2] :moveto ?g2)))
              (position :gappedsequence ((position :movefrom $piece[d6,g2] :moveto ?d2)))
              (position :gappedsequence ((position :movefrom $piece[d6,g2] :moveto ?g6)))
              (position :gappedsequence ((position :movefrom $piece[g6,d2] :moveto ?d6)))
             )
        :shift
        :flip
       )
)

```

## See also

- [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")
- [SCID](SCID "SCID")

## Publications

- [Gady Costeff](Gady_Costeff "Gady Costeff") (**2004**). *The Chess Query Language: CQL*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal"), [pdf](http://gadycosteff.com/chess_query_language.pdf)
- [Miha Bizjak](index.php?title=Miha_Bizjak&action=edit&redlink=1 "Miha Bizjak (page does not exist)"), [Matej Guid](Matej_Guid "Matej Guid") (**2021**). *Automatic Recognition of Similar Chess Motifs*. [Advances in Computer Games 17](Advances_in_Computer_Games_17 "Advances in Computer Games 17")

## Forum Posts

- [CQL Users?](https://www.stmintz.com/ccc/index.php?id=381879) by [Guy Haworth](Guy_Haworth "Guy Haworth"), [CCC](CCC "CCC"), August 11, 2004
- [CQL - Stalemate with 2 pieces pinned](https://www.stmintz.com/ccc/index.php?id=437137) by James Constance, [CCC](CCC "CCC"), July 17, 2005
- [Chess Query Language](http://www.talkchess.com/forum/viewtopic.php?t=40049) by [David Dahlem](index.php?title=David_Dahlem&action=edit&redlink=1 "David Dahlem (page does not exist)"), [CCC](CCC "CCC"), August 13, 2011
- [Chess Query Language](http://www.talkchess.com/forum/viewtopic.php?t=60090) by Giovanni Lavorgna, [CCC](CCC "CCC"), May 07, 2016
- [Scid vs PC with CQL , build issue](http://www.talkchess.com/forum/viewtopic.php?t=65815) by [Steven Atkinson](Steven_Atkinson "Steven Atkinson"), [CCC](CCC "CCC"), November 25, 2017 » [Scid vs. PC](Scid_vs._PC "Scid vs. PC")
- [Scid vs PC CQL 5.2 feature](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66562) by [Steven Atkinson](Steven_Atkinson "Steven Atkinson"), [CCC](CCC "CCC"), February 11, 2018 » [Scid vs. PC](Scid_vs._PC "Scid vs. PC")
- [CQL 6.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77520) by Mark Thellen, [CCC](CCC "CCC"), June 20, 2021

## External Links

- [CQL Introduction](http://www.gadycosteff.com/cql/) by [Gady Costeff](Gady_Costeff "Gady Costeff")
- [CQL Introduction](https://web.archive.org/web/20140130143815/http://www.rbnn.com/cql/) hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)
- [Sample CQL files about themes or manoeuvres and with some studies shown as results](http://www.arves.org/arves/index.php/en/endgamestudies/cql-sample-files) from [ARVES](https://de.wikipedia.org/wiki/ARVES)
- [Chess Query Language](http://www.xs4all.nl/~timkr/chess2/cql.htm) from [Tim Krabbé's](https://en.wikipedia.org/wiki/Tim_Krabb%C3%A9) Chess Site (March 2004)
- [Chess Query Language from Wikipedia](https://en.wikipedia.org/wiki/Chess_Query_Language)
- [CQL VisualCQL](http://www.vlasak.biz/vcql.htm) by [Emil Vlasák](index.php?title=Emil_Vlas%C3%A1k&action=edit&redlink=1 "Emil Vlasák (page does not exist)")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [CQL Introduction](http://www.gadycosteff.com/cql/) by [Gady Costeff](Gady_Costeff "Gady Costeff")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Sample CQL files](https://web.archive.org/web/20140130143815/http://www.rbnn.com/cql/examples.html) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [An html version of rookrectangle.cql](https://web.archive.org/web/20140130143815/http://www.rbnn.com/cql/rookrectangle.html) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))

**[Up one Level](Chess "Chess")**

