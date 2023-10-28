---
title: CookieCat
---
**[Home](Home "Home") * [Engines](Engines "Engines") * CookieCat**

[](http://4.bp.blogspot.com/-e-zuCaeA7No/T5bmrS8kvtI/AAAAAAAAFic/n0gPYVR82PU/s1600/smokey19350407+Smokey+Stover+First+Spooky+Bill+Holman.jpg) Spooky <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**CookieCat**,

an educational [open source chess program](Category:Open_Source "Category:Open Source") by [Steven Edwards](Steven_Edwards "Steven Edwards") designed for pedagogical purposes, written in [Free Pascal](Pascal#FreePascal "Pascal") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. CookieCat evolved from the earlier **Bozochess** project <a id="cite-note-3" href="#cite-ref-3">[3]</a> announced in October 2011 <a id="cite-note-4" href="#cite-ref-4">[4]</a>, renamed in December 2011 <a id="cite-note-5" href="#cite-ref-5">[5]</a>, and first released in January 2012 <a id="cite-note-6" href="#cite-ref-6">[6]</a> under the [permissive](https://en.wikipedia.org/wiki/Permissive_software_licence) [BSD License](https://en.wikipedia.org/wiki/BSD_licenses). However, Steven's wish that his CookieCat should be easily searchable on the net without too many false positives didn't fulfill when [Steven Universe](https://en.wikipedia.org/wiki/Steven_Universe) came up with a fictional character <a id="cite-note-7" href="#cite-ref-7">[7]</a> and ice cream <a id="cite-note-8" href="#cite-ref-8">[8]</a> in 2013.

## Contents

- [1 Description](#description)
  - [1.1 Bitboard Infrastructure](#bitboard-infrastructure)
  - [1.2 Spooky](#spooky)
  - [1.3 Smokey](#smokey)
  - [1.4 Lucky](#lucky)
- [2 Download](#download)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
  - [4.1 2011](#2011)
  - [4.2 2012 ...](#2012-...)
  - [4.3 2020 ...](#2020-...)
- [5 External Links](#external-links)
  - [5.1 Chess Engine](#chess-engine)
  - [5.2 Misc](#misc)
- [6 References](#references)

## Description

CookieCat utilizes [bitboards](Bitboards "Bitboards") as basic data structure [to represent](Board_Representation "Board Representation") the board. Inside CookieCat's source code <a id="cite-note-9" href="#cite-ref-9">[9]</a>, there are three groups of routines named after some of Steven's [feline](https://en.wikipedia.org/wiki/Feline) companions. There are the **Lucky** [positional evaluator](Evaluation "Evaluation") routines, the **Smokey** [mate finder](Mate_Search "Mate Search") routines, and the **Spooky** general [search](Search "Search") routines. The names were chosen not so much to be cute, but rather to make it easier for others to identify the program's functional organization <a id="cite-note-10" href="#cite-ref-10">[10]</a>. CookieCat features five [hash-tables](Hash_Table "Hash Table"), beside the [main transposition table](Transposition_Table "Transposition Table"), an [endgame tablebase](Endgame_Tablebases "Endgame Tablebases") cache, a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table"), [evaluation hash table](Evaluation_Hash_Table "Evaluation Hash Table"), and a dedicated [perft hash table](Perft "Perft"), and can further probe an [opening book](Opening_Book "Opening Book") <a id="cite-note-11" href="#cite-ref-11">[11]</a> and [Edwards' tablebases](Edwards%27_Tablebases "Edwards' Tablebases").

## Bitboard Infrastructure

[Bitboards](Bitboards "Bitboards") are defined as union ([variable structure](http://wiki.freepascal.org/Record#Variable_structure)) of four 16-bit [words](Word "Word") and one 64 bit value:

```

    bbtype =
      record
        case Boolean of
          False: (wvec: array [bbwtype] of bbwspantype); { Array of bitboard words }
          True:  (bv64: ui64type)                        { Unsigned 64 bit value }
      end;

```

[Population count](Population_Count "Population Count") and [BitScan](BitScan "BitScan") rely on [16-bit lookups](Population_Count#Lookup "Population Count"):

```

  function BbCount(var bb: bbtype): cctype; inline;
    var
      myresult: cctype;
      bbw: bbwtype;
  begin
    with bb do
      begin
        myresult := 0;
        for bbw := bbwmin to bbwmax do
          myresult := myresult + bitcountvec[wvec[bbw]]
      end;
    BbCount := myresult
  end; { BbCount }

  function BbFirstSq(var bb: bbtype): sqxtype; inline;
    var
      myresult: sqxtype;
      bbwindex: Integer;
      wordfirstbit: Integer;
  begin
    with bb do
      begin
        myresult := sqnil;
        bbwindex := 0;
        while (myresult = sqnil) and (bbwindex < bbwlen) do
          begin
            wordfirstbit := bitfirstvec[wvec[bbwindex]];
            if wordfirstbit >= 0 then
              myresult := sqxtype(wordfirstbit + (bbwindex * bbwbitlen))
            else
              Inc(bbwindex)
          end
      end;
    BbFirstSq := myresult
  end; { BbFirstSq }

```

## Spooky

CookieCat's [search](Search "Search") dubbed **Spooky** is implemented as [iterative search](Iterative_Search "Iterative Search") using a [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) as nested procedure inside SpookyFindMove, which structure is outlined in following snippet:

```

  { ***** Spooky search routines ***** }
  procedure SpookyFindMove(var ssc: ssctype);
    procedure SpookyPrepareRoot;
    procedure SpookyIterationSequence;
      procedure SpookyIterate;
        procedure SpookySearch;
          procedure SpookyLimitTestNode;
          procedure SpookyMovePick;
            procedure SpookyOrderMoves;
            procedure SpookyPickThis(index: Integer);
          procedure SpookyMinimax;
        begin  { SpookySearch }
          with ssc do
            while pirvec[ply].nss <> nssexit do
              case pirvec[ply].nss of
                nssplystart:    { Search state: Initialize processing at this node }
                nssfirdrawtest: { Search state: Draw tests for fiftymoves/insufficient/repetition }
                nsstbprobe:     { Search state: Probe the tablebases }
                nssstandtest:   { Search state: Gainer (QSearch ed.) search stand-pat evaluation and test }
                nssgenerate:    { Search state: Move generation }
                nssmovepick:    { Search state: Move pick }
                nssexecute:     { Search state: Execute the move and advance one ply }
                nssretract:     { Search state: Retreat one ply and retract the move }
                nsspostscan:    { Search state: Post move scan operations }
                nssplyfinish:   { Search state: Final processing for this node }
        end;  { SpookySearch }
      end; { SpookyIterate }
    end; { SpookyIterationSequence }
  end; { SpookyFindMove }

```

## Smokey

**Smokey** is CookieCat's iterative [mate finder](Mate_Search "Mate Search") with nested procedures outlined below:

```

  { ***** Smokey mate finder routines ***** }
  procedure SmokeyFindMate(var ssc: ssctype; fmvc: Integer);
    procedure SmokeySearch;
      procedure SmokeyApplyKillerBonus;
    begin
      with ssc do
        while pirvec[ply].nss <> nssexit do
          case pirvec[ply].nss of
            nssplystart:
            nsstermtest:
            nssgenerate:
            nssmovepick:
            nssexecute:
            nssretract:
            nsspostscan:
    end; { SmokeySearch }
 end; { SmokeyFindMate }

```

## Lucky

**Lucky**, CookieCat's [evaluation](Evaluation "Evaluation") function with [evaluation hash table](Evaluation_Hash_Table "Evaluation Hash Table") and [pawn hash table](Pawn_Hash_Table "Pawn Hash Table") considers [material](Material "Material"), [pawn structure](Pawn_Structure "Pawn Structure") with focus on [passed pawns](Passed_Pawn "Passed Pawn") <a id="cite-note-12" href="#cite-ref-12">[12]</a>, and [piece mobility](Mobility "Mobility").

## Download

<a id="cite-note-13" href="#cite-ref-13">[13]</a>

- [File:CookieCat.tar](File:CookieCat.tar "File:CookieCat.tar")

## See also

- [Bobcat](Bobcat "Bobcat")
- [Chess 0.5](Chess_0.5 "Chess 0.5")
- [Murka](Murka "Murka")
- [Myopic](Myopic "Myopic")
- [Spector](Spector "Spector")
- [Symbolic](Symbolic "Symbolic")
- [WildCat](WildCat "WildCat")

## Forum Posts

## 2011

- [Announcement: The Bozochess Project](http://www.talkchess.com/forum/viewtopic.php?t=40643) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), October 05, 2011

[Release date target](http://www.talkchess.com/forum/viewtopic.php?t=40643&start=24) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), October 16, 2011

- [BozoChess Monday release schedule](http://www.talkchess.com/forum/viewtopic.php?t=41430) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 12, 2011

[The name change](http://www.talkchess.com/forum/viewtopic.php?t=41430&start=4) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 16, 2011

- [Number sequence puzzle](http://www.talkchess.com/forum/viewtopic.php?t=41467) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 16, 2011 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases") <a id="cite-note-14" href="#cite-ref-14">[14]</a>
- [CookieCat Monday release schedule](http://www.talkchess.com/forum/viewtopic.php?t=41522) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 19, 2011
- [Tablebase class name list available](http://www.talkchess.com/forum/viewtopic.php?t=41524) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 19, 2011 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [CookieCat sample games](http://www.talkchess.com/forum/viewtopic.php?t=41583) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 24, 2011
- [CookieCat goes mulithreaded](http://www.talkchess.com/forum/viewtopic.php?t=41703) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 31, 2011 » [Perft](Perft "Perft")

## 2012 ...

- [CookieCat's opening book implementation](http://www.talkchess.com/forum/viewtopic.php?t=41804) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 05, 2012 » [Opening Book](Opening_Book "Opening Book")
- [CookieCat's pawn structure code](http://www.talkchess.com/forum/viewtopic.php?t=41842) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 07, 2012
- [CookieCat's early search termination](http://www.talkchess.com/forum/viewtopic.php?t=41850) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 07, 2012
- [CookieCat and Cookie Cat](http://www.talkchess.com/forum/viewtopic.php?t=41874) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 08, 2012
- [CookieCat source via the net](http://www.talkchess.com/forum/viewtopic.php?t=42169) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 26, 2012
- [CookieCat and perft](http://www.talkchess.com/forum/viewtopic.php?t=45568) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), October 14, 2012
- [For a limited time, two sources](http://www.talkchess.com/forum/viewtopic.php?t=46964) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 22, 2013 » [Myopic](Myopic "Myopic")

## 2020 ...

- [CookieCat retouched](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73005) by [Roland Chastain](Roland_Chastain "Roland Chastain"), [CCC](CCC "CCC"), February 06, 2020

## External Links

## Chess Engine

- [GitHub - rchastain/cookiecat: Pascal chess program by Steven Edwards](https://github.com/rchastain/cookiecat)

## Misc

- [Cookie from Wikipedia](https://en.wikipedia.org/wiki/Cookie)
- [Cat from Wikipedia](https://en.wikipedia.org/wiki/Cat)
- [Lucky from Wikipedia](https://en.wikipedia.org/wiki/Lucky)
- [Smokey from Wikipedia](https://en.wikipedia.org/wiki/Smokey)
- [Smokey Stover from Wikipedia](https://en.wikipedia.org/wiki/Smokey_Stover)
- [Spooky from Wikipedia](https://en.wikipedia.org/wiki/Spooky)
- [The Dave Pike Set](Category:Dave_Pike "Category:Dave Pike") - Spooky, [Got the Feelin'](https://www.discogs.com/de/The-Dave-Pike-Set-Got-The-Feelin/release/1789749) (1968), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

lineup: [Dave Pike](Category:Dave_Pike "Category:Dave Pike"), [Ruud Jacobs](Category:Ruud_Jacobs "Category:Ruud Jacobs"), [Louis Debij](https://nl.wikipedia.org/wiki/Louis_Debij), [Joop Scholten](https://www.discogs.com/de/artist/287923-Joop-Scholten), [Rob Franken](https://nl.wikipedia.org/wiki/Rob_Franken)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Image from [The first Spooky and the fifth Smokey](http://4.bp.blogspot.com/-e-zuCaeA7No/T5bmrS8kvtI/AAAAAAAAFic/n0gPYVR82PU/s1600/smokey19350407+Smokey+Stover+First+Spooky+Bill+Holman.jpg) (April 7, 1935) from [The Birth of Smokey Stover - First Puffs (1935)](http://screwballcomics.blogspot.de/2012/04/how-smokey-stover-got-started-first.html), [Bill Holman](<https://en.wikipedia.org/wiki/Bill_Holman_(cartoonist)>) [Comics](Category:Comics "Category:Comics"), Copyright, 1935, by [Chicago Tribune](https://en.wikipedia.org/wiki/Chicago_Tribune), [New York News Syndicate Inc.](https://en.wikipedia.org/wiki/Tribune_Media_Services), supplied by [Carl Linich](https://www.blogger.com/profile/12144756085960502977), posted by [Paul Tumey](https://plus.google.com/+PaulTumey), April 24, 2012
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Free Pascal wiki](http://wiki.freepascal.org/Home)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Release date target](http://www.talkchess.com/forum/viewtopic.php?t=40643&start=24) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), October 16, 2011
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Announcement: The Bozochess Project](http://www.talkchess.com/forum/viewtopic.php?t=40643) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), October 05, 2011
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [The name change](http://www.talkchess.com/forum/viewtopic.php?t=41430&start=4) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 16, 2011
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [CookieCat source via the net](http://www.talkchess.com/forum/viewtopic.php?t=42169) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 26, 2012
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Cookie Cat (character) | Steven Universe Wiki](<http://steven-universe.wikia.com/wiki/Cookie_Cat_(character)>)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Cookie Cat | Steven Universe Wiki](http://steven-universe.wikia.com/wiki/Cookie_Cat)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> Description is based on the source code - CookieCat.pas
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [CookieCat and Cookie Cat](http://www.talkchess.com/forum/viewtopic.php?t=41874) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 08, 2012
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a>  [CookieCat's opening book implementation](http://www.talkchess.com/forum/viewtopic.php?t=41804) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 05, 2012
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [CookieCat's pawn structure code](http://www.talkchess.com/forum/viewtopic.php?t=41842) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 07, 2012
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> Source code courtesy [Steven Edwards](Steven_Edwards "Steven Edwards")
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [A018214 - OEIS | Alkane (or paraffin) numbers](http://oeis.org/A018214)

**[Up one level](Engines "Engines")**

