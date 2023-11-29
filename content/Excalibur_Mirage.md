---
title: Excalibur Mirage
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Excalibur Mirage**

[](Excalibur_Mirage#Video "Excalibur Mirage#Video") Excalibur Mirage <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Excalibur Mirage**,

a [robot type](Robots "Robots") [dedicated chess computer](Dedicated_Chess_Computers "Dedicated Chess Computers") by [Excalibur Electronics](Excalibur_Electronics "Excalibur Electronics"), released in 1996 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
The computer features a [X-Y plotter](https://en.wikipedia.org/wiki/X%E2%80%93Y_plotter) type [actuator](https://en.wikipedia.org/wiki/Actuator) with motor driven [leadscrews](https://en.wikipedia.org/wiki/Leadscrew) and [solenoid](https://en.wikipedia.org/wiki/Solenoid) able to pick up and move the magnetic pieces,
a [sensory board](Sensory_Board "Sensory Board"), [LCD](https://en.wikipedia.org/wiki/Liquid-crystal_display), and a control button panel. The program is [Ron Nelson's](Ron_Nelson "Ron Nelson") initial chess program developed for Excalibur, and ran on [Hitachi's](https://en.wikipedia.org/wiki/Hitachi) [H8](H8 "H8") controller at 10 MHz with 48 KiB [ROM](Memory#ROM "Memory") and 2 KiB [RAM](Memory#RAM "Memory").
The development was supported by chess consultant and [opening book author](Category:Opening_Book_Author "Category:Opening Book Author") [Larry Kaufman](Larry_Kaufman "Larry Kaufman") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Failure Rates

Quote by [Ron Nelson](Ron_Nelson "Ron Nelson") <a id="cite-note-5" href="#cite-ref-5">[5]</a>

```C++But the Pop-Up Tent, Inc mechanical “engineer”, screwed up on the Mirage housing design and the main motor mounting was off axis and caused high [failure rates](https://en.wikipedia.org/wiki/Failure_rate). 

```

## Attack Maps

Quote by [Ron Nelson](Ron_Nelson "Ron Nelson") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```C++In 1981 at the [California ACM Computer Chess Tournament](ACM_1981 "ACM 1981"), [Kathy](Kathe_Spracklen "Kathe Spracklen") introduced me to their friend [Ken Thompson](Ken_Thompson "Ken Thompson"). I asked him about his [Belle](Belle "Belle") hardware chess machine, and he was quick to explain how the Hardware [Attack Bitmaps](Attack_and_Defend_Maps "Attack and Defend Maps") worked. I realized that attack bitmap approach was now in a [Chess Challenger](Chess_Challenger "Chess Challenger"), but in software. I used the Belle Attack Map generation on my [H8](H8 "H8") program.

```

## Tactical Quiescence

Further Quote by [Ron Nelson](Ron_Nelson "Ron Nelson") <a id="cite-note-7" href="#cite-ref-7">[7]</a>

```C++But it was my watching the [games](Chess_Game "Chess Game") and the [PRVs](Principal_Variation "Principal Variation") like you do, and we did at [ACM tournaments](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship") that started me asking questions of [Dan](Dan_Spracklen "Dan Spracklen"). Why can we not [generate](Move_Generation "Move Generation") [checks](Check "Check") in the [quiescent search](Quiescence_Search "Quiescence Search")? He said because it would [blow up](Search_Explosion "Search Explosion") the [search](Search "Search") and slow down. Ok, I said, but what if we only generated checks that didn't occur as often, like a knight check that [forked](Double_Attack "Double Attack") a major piece. He said, ummm,,, that would not take much and the search would not blow up.  So that is how we slowly started developing a [tactical](Tactics "Tactics") quiescent search that had all of the things a strong chess player explores when thinking of a tactical position. But I would see that the PRV was missing these obvious strong player "tricks" and have Dan look to see if he could add them. Because of the attack map, all this type of information was easily divined. At the [Micro Tournament](WMCCC_1988 "WMCCC 1988") in Spain, it was music to my ears to have the Chess Master commentator, perhaps [Mike Valvo](Michael_Valvo "Michael Valvo"), say The [Fidelity](Fidelity "Fidelity") unit was playing moves it had never before been capable of playing. Just like the Masters we played to get the certified rating, who were amazed.

```

```C++I used this same type of tactical threat generation on the H8 machine, since I had attack maps with the needed information. 

```

## See also

- [Alexandra The Great](index.php?title=Alexandra_The_Great&action=edit&redlink=1 "Alexandra The Great (page does not exist)")
- [Excalibur Grandmaster](Excalibur_Grandmaster "Excalibur Grandmaster")
- [Excalibur Igor](Excalibur_Igor "Excalibur Igor")
- [Excalibur Phantom Force](Excalibur_Phantom_Force "Excalibur Phantom Force")
- [Fidelity Phantom](Fidelity_Phantom "Fidelity Phantom")
- [Ivan The Terrible](Ivan_The_Terrible "Ivan The Terrible")
- [Ivan II The Conqueror](Ivan_II_The_Conqueror "Ivan II The Conqueror")
- [Milton Bradley Phantom](Milton_Bradley_Phantom "Milton Bradley Phantom")
- [Mirage](Mirage "Mirage")
- [Robots](Robots "Robots")

## Manual

- [Excalibur Mirage User Manual | ManualsLib](https://www.manualslib.com/products/Excalibur-Mirage-3749788.html)

## Forum Posts

- [Playing Ron Nelson Programs, Today](http://www.talkchess.com/forum3/viewtopic.php?t=12970) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), April 08, 2007
- [Help with repair of Excalibur Mirage](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=48691) by jcgdijkstra, [CCC](CCC "CCC"), July 19, 2013
- [Re: Ron Nelson Ever Copied, Used , Cloned the Spracklen?](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=68) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 21, 2015

[Excalibur Electronics](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=78) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 22, 2015
[Excalibur Electronics](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=82) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 22, 2015
[Ron Nelson](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=105) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 23, 2015 » [Excalibur](Excalibur_Electronics "Excalibur Electronics")
[Ron Nelson](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=108) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 23, 2015 » [Fidelity Electronics](Fidelity_Electronics "Fidelity Electronics"), [Sidney Samole](Sidney_Samole "Sidney Samole")
[Re: Ron Nelson](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=122) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 24, 2015 » Excalibur Mirage, [Eric White](Eric_White "Eric White")
[Re: Ron Nelson](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=170) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 29, 2015

- [Excalibur Chess Products Ron Nelson designed/programmed](http://www.hiarcs.net/forums/viewtopic.php?t=7591) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), January 05, 2016

[Chess Products Ron Nelson designed/programmed](http://www.hiarcs.net/forums/viewtopic.php?t=7591&start=8) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2016

- [My Experience With The Excalibur Mirage](http://www.hiarcs.net/forums/viewtopic.php?t=7632) by Cyberchess, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), January 21, 2016

## External Links

## Chess Computer

- [Excalibur Mirage](http://www.ismenio.com/chess_excalibur_mirage.html) by [Ismenio Sousa](index.php?title=Ismenio_Sousa&action=edit&redlink=1 "Ismenio Sousa (page does not exist)")
- [Excalibur Mirage Marble](http://www.chesscomputeruk.com/html/excalibur_mirage_marble.html) by [Mike Watters](Mike_Watters "Mike Watters")
- [Excalibur Mirage - Los Proyectos de Berger - DIY](https://sites.google.com/site/proyectosdeberger/reparaciones/ajedrez/excalibur_mirage)
- [Excalibur Mirage](https://www.schach-computer.info/wiki/index.php/Excalibur_Mirage) - [Schachcomputer.info Wiki](https://www.schach-computer.info/wiki/index.php?title=Hauptseite_En) (German)
- [Excalibur Electronic Chess Computer Collection](http://www.spacious-mind.com/html/excalibur.html), [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
- Excalibur Mirage - Testing after repair, November 18, 2017, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## Misc

- [Excalibur - Wiktionary](https://en.wiktionary.org/wiki/Excalibur)
- [Excalibur from Wikipedia](https://en.wikipedia.org/wiki/Excalibur)
- [mirage - Wiktionary](https://en.wiktionary.org/wiki/mirage)
- [Mirage from Wikipedia](https://en.wikipedia.org/wiki/Mirage)
- [Mirage (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Mirage_(disambiguation)>)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Capture from the [Video](#video)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chess Products Ron Nelson designed/programmed](http://www.hiarcs.net/forums/viewtopic.php?t=7591&start=8) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2016
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Excalibur Electronics](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=78) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 22, 2015
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Ron Nelson](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=112) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 23, 2015
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Ron Nelson](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=108) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 23, 2015
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Excalibur Electronics](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=78) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 22, 2015
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Ron Nelson](http://www.hiarcs.net/forums/viewtopic.php?t=6768&start=170) by [ChessChallenger](Ron_Nelson "Ron Nelson"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 29, 2015

**[Up one level](Engines "Engines")**

