---
title: Occam
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Occam**


**Occam**,  

a private chess program and later also [Arimaa](Arimaa "Arimaa") bot by [Don Dailey](Don_Dailey "Don Dailey") <a id="cite-note-1" href="#cite-ref-1">[1]</a> and [Larry Kaufman](Larry_Kaufman "Larry Kaufman") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, which evolved from [Cilkchess](Cilkchess "Cilkchess") as experimental development version of Don and Larry's later commercial programs. In it's early state, short after the [WCCC 1999](WCCC_1999 "WCCC 1999"), Don explicitly mentioned the [Copy-Make](Copy-Make "Copy-Make") approach in Occam <a id="cite-note-3" href="#cite-ref-3">[3]</a> which he later also preferred in [Doch](Doch#Copy "Doch") <a id="cite-note-4" href="#cite-ref-4">[4]</a> and presumably in [Komodo](Komodo "Komodo").



### Contents


* [1 Position](#position)
* [2 Quotes](#quotes)
	+ [2.1 MTD](#mtd)
	+ [2.2 Arimaa Bot](#arimaa-bot)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Misc](#misc)
* [6 References](#references)






Don gave following [board representation](Board_Representation "Board Representation") and [position](Chess_Position "Chess Position") structure <a id="cite-note-5" href="#cite-ref-5">[5]</a>:




```C++

typedef struct ptag
{
  SQUARES       bd[65];          /* the board                        */
  base_int      king_loc[2];     /* location of kings                */
  u64           hashkey;         /* position key for hash table      */
  int32         mat_sig;         /* signature of material situation  */
  struct ptag   *his[2];         /* pointer to last 2 positions      */
  ev_type       inc_score;       /* incremental component of score   */
  base_int      ply_of_game;     /* even = white to move             */
  base_int      ply_of_search;   /* start at 0                       */
  base_int      pv[PV_LEN];      /* best move from position          */
  base_int      last_move;       /* move that got us here            */
  base_int      null_count;      /* how many recursive null moves?   */
  base_int      in_check;        /* is ctm king in check?            */
} position;

```

## Quotes


### MTD


Reply by [Don Dailey](Don_Dailey "Don Dailey") to [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), July 20, 1999 <a id="cite-note-6" href="#cite-ref-6">[6]</a>:




```C++
I have a primitive program  called "Occam" playing on the chess server now. I don't have any kind  of [aspiration search](Aspiration_Windows "Aspiration Windows") in it, just pure [alpha/beta](Alpha-Beta "Alpha-Beta"), no [PVS](Principal_Variation_Search "Principal Variation Search"), no [MTD](MTD(f) "MTD(f)") or anything. I will implement PVS first so that I  can do comparisions. 

```

### Arimaa Bot


Occam was further test-bed for an [Arimaa](Arimaa "Arimaa") bot which played the first computer-computer challenge in 2004 <a id="cite-note-7" href="#cite-ref-7">[7]</a>. Quote by [Omar Syed](Omar_Syed "Omar Syed") <a id="cite-note-8" href="#cite-ref-8">[8]</a>:




```C++
Soon after the challenge was announced, several members of the game AI-research community attempted to tackle the challenge. The late Don Dailey (developer of the [Komodo](Komodo "Komodo") chess engine) was the first to create an Arimaa engine. Within a couple months Don had a surprisingly strong program offering games in the Arimaa gameroom. In designing Arimaa, I had used the [Zillions-of-Games](Zillions_of_Games "Zillions of Games") [general game-playing](General_Game_Playing "General Game Playing") engine, which allows specifying the rules of the game in a [Lisp](index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)") like language, and then immediately being able to play the game against the Zillions engine. Using only look ahead and no game-specific knowledge, this engine was able to play at a strong level in most games one could dream of. However, it was incredibly lousy at Arimaa due to the high branching factor. This helped build my confidence that Arimaa would be a difficult game for computers if only a [brute-force](Brute-Force "Brute-Force") search was used. However, Don’s program, called OCCAM, surprised me in how well it played when the search engine was much faster and included some game knowledge. When Don realized that there was very little expert knowledge available for Arimaa, he felt that he could not make much progress on his program and went back to developing his chess engine which now has gone on to become the highest rated in the world. 

```

## See also


* [Arimaa](Arimaa "Arimaa")
* [Cilkchess](Cilkchess "Cilkchess")
* [Doch](Doch "Doch")
* [Komodo](Komodo "Komodo")
* [Razoring](Razoring "Razoring")


## Forum Posts


* [MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61058) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 19, 1999


 [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61151) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 20, 1999
 [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61157) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 20, 1999
 [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61218) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 20, 1999
 [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61243) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 21, 1999
## External Links


### Chess Engine


* [Finger Occam](http://www6.chessclub.com/finger/occam) at [Internet Chess Club](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")


### Misc


* [William of Ockham from Wikipedia](https://en.wikipedia.org/wiki/William_of_Ockham)
* [Occam's razor from Wikipedia](https://en.wikipedia.org/wiki/Occam's_razor)
* [occam (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Occam_%28programming_language%29)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61157) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 20, 1999
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Finger Occam](http://www6.chessclub.com/finger/occam) at [Internet Chess Club](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61218) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 20, 1999
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=291570&t=29770) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 16, 2009
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61243) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 21, 1999
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61151) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 20, 1999
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Arimaa Challenge 2004](http://arimaa.com/arimaa/challenge/2004/icgaNews2.html)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Omar Syed](Omar_Syed "Omar Syed") (**2015**). *The Arimaa Challenge: From Inception to Completion*. [ICGA Journal, Vol. 38, No. 1](ICGA_Journal#38_1 "ICGA Journal")

**[Up one Level](Engines "Engines")**







 
