---
title: Doch
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Doch**

**Doch**,

an [UCI](UCI "UCI") compliant chess engine by primary author [Don Dailey](Don_Dailey "Don Dailey"), supported by chess advisor and evaluation expert and Don's long time collaborator [Larry Kaufman](Larry_Kaufman "Larry Kaufman").
The development started in 2007 <a id="cite-note-1" href="#cite-ref-1">[1]</a>, and it was first released to the public as free engine in fall 2009 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Komodo

In January 2010, Doch evolved to [Komodo](Komodo "Komodo") <a id="cite-note-3" href="#cite-ref-3">[3]</a> to become one of the strongest programs ever.

## Etymology

Doch is [acronym](Category:Acronym "Category:Acronym") of Don's Chess. Quote from a [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") interview, December 2009 <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```C++Doch was never intended to be the name that would stick. When I first decided to write this program I needed a name and did not want to spend days obsessing over it. I did not want to call it "chess" but it needed a name to give it some personality. Doch stands for DOn's CHess. I never got around to giving it a proper name and I feel a bit immodest calling it after my own name! 

```

## Copy-Make

Doch was a 64-bit aka [bitboard](Bitboards "Bitboards") program, applying a [Copy-Make](Copy-Make "Copy-Make") approach with a [position](Chess_Position "Chess Position") state of 192 byte allocated on the [stack](Stack "Stack") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```C++
position search( position_state *prev,  ...  )
{
   position_state  new_position;
   ... other stuff
   foreach move in movelist do {
       make( prev, &new_position, move );
   }
} 

```

## See also

- [Komodo](Komodo "Komodo")
- [Occam](Occam "Occam")

## Forum Posts

- [Doch 09.980 (uci) by Don Dailey available](http://www.talkchess.com/forum/viewtopic.php?t=30598) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), November 13, 2009
- [Doch (64-bit Version)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=30830) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), November 28, 2009
- [Doch 1.2 update (uci) by Don Dailey available](http://www.talkchess.com/forum/viewtopic.php?t=31082) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), December 15, 2009
- [Doch 1.3.1](http://www.talkchess.com/forum/viewtopic.php?t=31493) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), January 05, 2010
- [A New Name for Doch....](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316228&t=31534) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), January 07, 2010

## External Links

## Chess Engine

- [Index of /chess/engines/Jim Ablett/DOCH](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/DOCH/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Computerschach, Interview with Don Dailey](http://www.schach-welt.de/schach/computerschach/interviews/don-dailey) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Schachwelt.de](http://www.schach-welt.de/), December 18-20, 2009

## Misc

- [doch - Wiktionary](http://en.wiktionary.org/wiki/doch)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [About Komodo](https://komodochess.com/store/pages.php?cmsid=13) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Doch 09.980 (uci) by Don Dailey available](http://www.talkchess.com/forum/viewtopic.php?t=30598) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), November 13, 2009
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Komodo credit](http://www.talkchess.com/forum/viewtopic.php?t=31920) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), January 22, 2010
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Computerschach, Interview with Don Dailey](http://www.schach-welt.de/schach/computerschach/interviews/don-dailey) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Schachwelt.de](http://www.schach-welt.de/), December 18-20, 2009
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=291570&t=29770) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 16, 2009
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=291586&t=29770) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 16, 2009

**[Up one Level](Engines "Engines")**

