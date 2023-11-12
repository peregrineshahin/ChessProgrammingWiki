---
title: Fischerle
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Fischerle**

[](http://www.stuckardt.de/index.php/schachengine-fischerle.html) Fischerle Logo
**Fischerle**,

a [Java-based](Java "Java") chess engine that has been developed by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"). Fischerle implements the [UCI](UCI "UCI") protocol. It is recommended to employ it from within the [Arena](Arena "Arena") environment. Additionally, Fischerle has an own [GUI](GUI "GUI") providing supplementary configuration and testing features; in principle, it can thus be used independently of UCI based chess GUIs. Fischerle is available for download at its author's web pages .

## Technology

Fischerle’s representation of chess positions is based on the [rotated bitboard](Rotated_Bitboards "Rotated Bitboards") model. Fischerle employs some well-known techniques of enhanced [alpha-beta](Alpha-Beta "Alpha-Beta") minimax search:

- [NegaScout](NegaScout "NegaScout") algorithm
- [Iterative deepening (ID)](Iterative_Deepening "Iterative Deepening") and [IID](Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Aspiration windows](Aspiration_Windows "Aspiration Windows")
- [History heuristic](History_Heuristic "History Heuristic")
- [Killer heuristic](Killer_Heuristic "Killer Heuristic")
- [Hash tables](Hash_Table "Hash Table")

[Transposition table](Transposition_Table "Transposition Table")
[Evaluation cache](Evaluation_Hash_Table "Evaluation Hash Table")

- [Quiescence search](Quiescence_Search "Quiescence Search")
- [Search extensions:](Extensions "Extensions")

[Promotions](Promotions "Promotions")
[7th rank Passed pawn extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
[Check evasions](Check_Extensions "Check Extensions") only by a singular / a few moves
[Winning recaptures](Recapture_Extensions "Recapture Extensions")
[Singular extensions](Singular_Extensions "Singular Extensions") (restricted implementation that doesn't apply at [Cut nodes](Node_Types "Node Types") and that considers only [transposition table](Transposition_Table "Transposition Table") moves as singularity candidates the value of which is marked there as exact or lower bound)
extension by several plies at the very moment a [pawn endgame](Pawn_Endgame "Pawn Endgame") is reached

- [Tactically](Tactics "Tactics") painless [reductions](Reductions "Reductions") according to the [enhanced model](AEL-Pruning "AEL-Pruning") suggested by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz")

[Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
[Extended Futility Pruning](Futility_Pruning#Extendedfutilityprunning "Futility Pruning")
[Limited Razoring](Razoring#LimitedRazoring "Razoring")

- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Interior node recognition](Interior_Node_Recognizer "Interior Node Recognizer") similar to Heinz’s proposal <a id="cite-note-1" href="#cite-ref-1">[1]</a>
- Dedicated scoring functions for some particular [endgame](Endgame "Endgame") types

The static [evaluation](Evaluation "Evaluation") parameters of Fischerle are amenable to external fine [tuning](Automated_Tuning "Automated Tuning") based on a concept of so-called efb (*evaluation factor block*) files, thus enabling the user to influence, within certain bounds, Fischerle’s playing style (e. g. to prefer closed positions, etc.). Fischerle comes with its own, small [opening book](Opening_Book "Opening Book"), covering about 220K positions and some 540K moves. Fischerle supports [pondering](Pondering "Pondering") via its [UCI](UCI "UCI") interface.

## Latest Version

Fischerle **0.9.80 SE** <a id="cite-note-2" href="#cite-ref-2">[2]</a> - a slightly more aggressive forward [pruning](Pruning "Pruning") scheme is now applied; [quiescence search](Quiescence_Search "Quiescence Search") has been mildly refined (adding, in particular, [delta pruning](Delta_Pruning "Delta Pruning")); the piece value assigned to [bishops](Bishop "Bishop") and the [bishop pair](Bishop_Pair "Bishop Pair") bonus have been slightly reduced; [king safety](King_Safety "King Safety") ealuation has been refined; the mate approaching scheme has been enhanced.

## Etymology

[](https://www.dorisneidl.net/illustration?lightbox=image_14xa) Die Blendung by [Doris Neidl](Category:Doris_Neidl "Category:Doris Neidl") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
*"Ein Mensch, was ka Schach spielt, ist ka Mensch"* <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## Auto-da-Fé

Fischerle <a id="cite-note-5" href="#cite-ref-5">[5]</a> is named after a famous character of [Elias Canetti’s](https://en.wikipedia.org/wiki/Elias_Canetti) novel [„Die Blendung“](http://de.wikipedia.org/wiki/Die_Blendung) ([„Auto-da-Fé“](https://en.wikipedia.org/wiki/Auto-da-F%C3%A9)) <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a> , which plays in [Vienna](https://en.wikipedia.org/wiki/Vienna) <a id="cite-note-8" href="#cite-ref-8">[8]</a> around protagonist [Peter Kien](https://en.wikipedia.org/wiki/Auto-da-F%C3%A9#Plot_and_themes), a middle-aged philologist and [Sinologist](https://en.wikipedia.org/wiki/Sinology): **Siegfried Fischerle** <a id="cite-note-9" href="#cite-ref-9">[9]</a> , a [Jewish](https://en.wikipedia.org/wiki/Jews) <a id="cite-note-10" href="#cite-ref-10">[10]</a> [hunchbacked](https://en.wikipedia.org/wiki/Kyphosis) [dwarf](https://en.wikipedia.org/wiki/Dwarf) and [pander](https://en.wikipedia.org/wiki/Procuring_%28prostitution%29), is a [chess addict](Morphy#ChessFever "Morphy") whose dream is it to go to America to challenge chess champion [José Raúl Capablanca](https://en.wikipedia.org/wiki/Jos%C3%A9_Ra%C3%BAl_Capablanca) in order to get rich and famous. Canetti wrote his novel in the years 1930/31, coincidentally more than one decade before [Nazi German](https://en.wikipedia.org/wiki/Nazi_Germany) [Oberfeldwebel](https://en.wikipedia.org/wiki/Feldwebel#Reichswehr_and_Wehrmacht) [Siegfried Fischer](https://en.wikipedia.org/wiki/Siegfried_Fischer) was decorated with the [Knight's Cross of the Iron Cross](https://en.wikipedia.org/wiki/Knight%27s_Cross_of_the_Iron_Cross), Jewish artist and poet [Peter Kien](https://en.wikipedia.org/wiki/Peter_Kien) died in [Auschwitz concentration camp](https://en.wikipedia.org/wiki/Auschwitz_concentration_camp), and more than two decades before chess genius [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer) entered the international chess scene <a id="cite-note-11" href="#cite-ref-11">[11]</a> .

## Fischers Fritz

The German [tongue-twister](https://en.wikipedia.org/wiki/Tongue-twister) "Fischers Fritz fischt frische Fische. Frische Fische fischt Fischers Fritz." (Fisher's Fritz fishes fresh fish, fresh fish are fished by fisher's Fritz) is not related to [Fritz Fischer](https://en.wikipedia.org/wiki/Fritz_Fischer_%28biathlete%29) but may be to Fischerle's famous brother [Fritz](Fritz "Fritz")?

## Publications

<a id="cite-note-12" href="#cite-ref-12">[12]</a>

- [Elias Canetti](https://en.wikipedia.org/wiki/Elias_Canetti) (**1936**). *[Die Blendung](http://de.wikipedia.org/wiki/Die_Blendung)*. Wien 1936, [Editio princeps](https://en.wikipedia.org/wiki/Editio_princeps) (German)
- [Elias Canetti](https://en.wikipedia.org/wiki/Elias_Canetti) (**1946**). *[Auto-da-Fe](https://en.wikipedia.org/wiki/Auto-da-F%C3%A9)*. Translated by [Veronica Wedgwood](https://en.wikipedia.org/wiki/Veronica_Wedgwood)
- Peter Jansen (**1980**). *Die Komik des Sprechens. Zur sprachlich-ästhetischen Erfahrung des Komischen am Beispiel von Canettis Roman "Die Blendung"*. in [Sprache im technischen Zeitalter](http://de.wikipedia.org/wiki/Sprache_im_technischen_Zeitalter), 76 (German)
- [Nicola Riedner](http://www.worldcat.org/search?q=au%3ARiedner%2C+Nicola.&qt=hot_author) (**1994**). *[Canettis Fischerle: eine Figur zwschischen Masse, Macht und Blendung](http://www.worldcat.org/title/canettis-fischerle-eine-figur-zwischen-masse-macht-und-blendung/oclc/30632821&referer=brief_results)*. [Königshausen und Neumann](https://en.wikipedia.org/wiki/K%C3%B6nigshausen_%26_Neumann) (German)
- [Harriet Murphy](http://www.barnesandnoble.com/c/harriet-murphy) (**1996**). *[Canetti and Nietzsche: Theories of Humor in Die Blendung](http://www.barnesandnoble.com/w/canetti-and-nietzsche-harriet-murphy/1115275227?ean=9780791431337)*. [State University of New York Press](https://en.wikipedia.org/wiki/State_University_of_New_York_Press) <a id="cite-note-13" href="#cite-ref-13">[13]</a>
- [Ritchie Robertson](https://en.wikipedia.org/wiki/Ritchie_Robertson) (**1999**). *[The 'Jewish Question' in German Literature 1749 - 1939 Emancipation and Discontents](http://www.questia.com/library/1826902/the-jewish-question-in-german-literature-1749-1939)*. [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press) <a id="cite-note-14" href="#cite-ref-14">[14]</a>
- [William Collins Donahue](http://fds.duke.edu/db/aas/German/wcd2) (**2001**). *[The End of Modernism : Elias Canetti's Auto-da-fâe](http://www.questia.com/library/104788411/the-end-of-modernism-elias-canetti-s-auto-da-fae)*. [University of North Carolina Press](https://en.wikipedia.org/wiki/University_of_North_Carolina_Press) <a id="cite-note-15" href="#cite-ref-15">[15]</a>
- [Marcus Puknatis](http://www.barnesandnoble.com/c/marcus-puknatis) (**2002,2007**). *[Elias Canettis 'Die Blendung' - Typische Österreichische Nationalliteratur?](http://www.barnesandnoble.com/w/elias-canettis-die-blendung-typische-sterreichische-nationalliteratur-marcus-puknatis/1114561378?ean=9783638802758)* [GRIN Verlag](https://de.wikipedia.org/wiki/GRIN_Verlag) (German)
- Yun Chen (**2003**). *[Canetti und die chinesische Kultur](http://docserv.uni-duesseldorf.de/servlets/DocumentServlet?id=2534)*. [Dissertation](https://en.wikipedia.org/wiki/Thesis), [Heinrich Heine University Düsseldorf](https://en.wikipedia.org/wiki/University_of_D%C3%BCsseldorf) (German)
- [Hidas Ildikó](http://mek.oszk.hu/08200/08294/) (**2008**). *Elias Canettis Roman Die Blendung im Schnittpunkt zeitgenössischer Diskurse*. Ph.D. thesis, [Pázmány Péter Catholic University](https://en.wikipedia.org/wiki/P%C3%A1zm%C3%A1ny_P%C3%A9ter_Catholic_University), [Piliscsaba](https://en.wikipedia.org/wiki/Piliscsaba), [pdf](http://mek.oszk.hu/08200/08294/08294.pdf) (German)

## See also

- [Bobby](Bobby "Bobby")
- [Capablanca Edition](Morphy#Capablanca "Morphy")
- [Chess Fever (Shakhmatnaya goryachka)](Morphy#ChessFever "Morphy")

## Forum Posts

## 2014

- [Nice move by Fischerle (Division 7 engine in my Amateurs)](http://www.talkchess.com/forum/viewtopic.php?t=50858) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), January 11, 2014
- [A good 64-bit Java chess engine unknown here](http://www.talkchess.com/forum/viewtopic.php?t=51250) by [Ruxy Sylwyka](http://www.talkchess.com/forum/profile.php?mode=viewprofile&u=881), [CCC](CCC "CCC"), February 12, 2014
- [No GUI problems with Fischerle](http://www.talkchess.com/forum/viewtopic.php?t=51324) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), February 18, 2014
- [Re: 32-bit and 64-bit java engines](http://www.talkchess.com/forum/viewtopic.php?t=51279&start=3) by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"), [CCC](CCC "CCC"), February 24, 2014
- [New Fischerle Versions (64 and 32 Bit)](http://www.talkchess.com/forum/viewtopic.php?t=52327) by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"), [CCC](CCC "CCC"), May 15, 2014
- [New Fischerle Version: 0.9.60](http://www.talkchess.com/forum/viewtopic.php?t=53967) by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"), [CCC](CCC "CCC"), October 07, 2014

## 2015 ...

- [New Fischerle Version: 0.9.65](http://www.talkchess.com/forum/viewtopic.php?t=57676) by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"), [CCC](CCC "CCC"), September 17, 2015
- [New Fischerle Version: 0.9.70 SE](http://www.talkchess.com/forum/viewtopic.php?t=59624) by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"), [CCC](CCC "CCC"), March 25, 2016
- [New Fischerle Version: 0.9.80 SE](http://www.talkchess.com/forum/viewtopic.php?t=63546) by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"), [CCC](CCC "CCC"), March 24, 2017

## External Links

## Chess Engine

- [Schachengine Fischerle](http://www.stuckardt.de/index.php/schachengine-fischerle.html) (German)

[Schachengine Fischerle - Techniken im Überblick](http://www.stuckardt.de/index.php/schachengine-fischerle/techniken-im-ueberblick.html)
[Schachengine Fischerle - Benutzeroberfläche](http://www.stuckardt.de/index.php/schachengine-fischerle/benutzeroberflaeche.html)

- [Fischerle](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Fischerle&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Fischer - Wiktionary](https://en.wiktionary.org/wiki/Fischer)
- [Fischer from Wikipedia](https://en.wikipedia.org/wiki/Fischer)

[Bobby Fischer from Wikipedia](https://en.wikipedia.org/wiki/Bobby_Fischer)

- [Auto-da-Fé from Wikipedia](https://en.wikipedia.org/wiki/Auto-da-F%C3%A9)
- [Fisherman from Wikipedia](https://en.wikipedia.org/wiki/Fisherman)
- [Fish from Wikipedia](https://en.wikipedia.org/wiki/Fish)
- [Fish anatomy from Wikipedia](https://en.wikipedia.org/wiki/Fish_anatomy)
- [Fischerle](http://www.muno.pl/news/fischerle-the-big-sleep-u-cover-album-konkurs/) - The Love Bruises, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[Efficient Interior-Node Recognition](http://people.csail.mit.edu/heinz/dt/node33.html).* [ICCA Journal, Vol. 21, No. 3](ICGA_Journal#21_3 "ICGA Journal")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Fischerle 0.9.80 SE](http://www.stuckardt.de/rsdokumente/Fischerle_0_9_80_SE_64_or_32.rar) (March 24, 2017)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Die Blendung - Illustrations - Gallery](https://www.dorisneidl.net/illustration), capturing the crazy and wondrous journey of [Sinologist](https://en.wikipedia.org/wiki/Sinology) [Peter Kien](https://en.wikipedia.org/wiki/Auto-da-F%C3%A9#Plot_and_themes). Copyright © 2013 by [Doris Neidl](Category:Doris_Neidl "Category:Doris Neidl")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> "A person who does not play chess, is not a man", [direct speech](https://en.wikipedia.org/wiki/Direct_speech) in [Viennese German](https://en.wikipedia.org/wiki/Viennese_German) of Fischerle to [Kien](https://en.wikipedia.org/wiki/Auto-da-F%C3%A9#Plot_and_themes), in
   [Elias Canetti](https://en.wikipedia.org/wiki/Elias_Canetti) (**1936**). *[Die Blendung](http://de.wikipedia.org/wiki/Die_Blendung)*. Wien 1936, [Editio princeps](https://en.wikipedia.org/wiki/Editio_princeps), p. 191.
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Fischerle - [Diminutive form](https://en.wikipedia.org/wiki/Diminutive) of [Fischer](https://en.wikipedia.org/wiki/Fischer)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Auto-da-fé from Wikipedia](https://en.wikipedia.org/wiki/Auto-da-f%C3%A9)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Talk Literature: Auto-da-Fé - Elias Canetti](http://members4.boardhost.com/readliterature/msg/1266773491.html) by Lale, February 21, 2010
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [History of the Jews in Vienna - from Wikipedia](https://en.wikipedia.org/wiki/History_of_the_Jews_in_Vienna)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Nicola Riedner](http://www.worldcat.org/search?q=au%3ARiedner%2C+Nicola.&qt=hot_author) (**1994**). *[Canettis Fischerle: eine Figur zwischen Masse, Macht und Blendung](http://www.worldcat.org/title/canettis-fischerle-eine-figur-zwischen-masse-macht-und-blendung/oclc/30632821&referer=brief_results)*. [Königshausen und Neumann](https://en.wikipedia.org/wiki/K%C3%B6nigshausen_%26_Neumann), page 40, footnote 174, [Google books](http://books.google.de/books?id=P87wy187bqAC&lpg=PA1&vq=page%2040&hl=de&pg=PA40#v=onepage&q&f=true), "Peter Jansen behauptet fälschlicherweise, daß Fischerle eigentlich Fischer hieße und nur aufgrund seiner Gestalt das Verkleinerungssuffix durch andere hinzubekommen hätte". Peter Jansen (**1980**). *Die Komik des Sprechens. Zur sprachlich-ästhetischen Erfahrung des Komischen am Beispiel von Canettis Roman "Die Blendung"*. in [Sprache im technischen Zeitalter](http://de.wikipedia.org/wiki/Sprache_im_technischen_Zeitalter), 76
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> further in [Nicola Riedner](http://www.worldcat.org/search?q=au%3ARiedner%2C+Nicola.&qt=hot_author) (**1994**). *[Canettis Fischerle: eine Figur zwschischen Masse, Macht und Blendung](http://www.worldcat.org/title/canettis-fischerle-eine-figur-zwischen-masse-macht-und-blendung/oclc/30632821&referer=brief_results)*. [Königshausen und Neumann](https://en.wikipedia.org/wiki/K%C3%B6nigshausen_%26_Neumann), page 41-42, During the time of writing of the novel (1930/31) the German given name [Siegfried](https://en.wikipedia.org/wiki/Siegfried_%28given_name%29) for Jewish children was indication of Jewish will for [assimilation](https://en.wikipedia.org/wiki/Cultural_assimilation), footnote 179, Konrad Krause (**1943**). *[Die jüdische Namenswelt](http://www.worldcat.org/title/judische-namenwelt/oclc/2041274)*. [Essener Verlagsanstalt](http://de.wikipedia.org/wiki/Essener_Verlagsanstalt), Publisher of the [Nazi Party](https://en.wikipedia.org/wiki/Nazi_Party), S. 11, "Denn es ist bekannt, in welchem Ausmaß die Juden \[...\] unsere herrlichen alten Namen z.T. nahezu entwertet haben. Dieses Schicksal erlitten besonders die 'Sieg'namen ..."
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> Bobby Fischer, whose mother was Jewish, and whose possible biological father was also Jewish, made numerous [Anti-semitic](https://en.wikipedia.org/wiki/Antisemitism) statements, see [Bobby Fischer - Anti-semitic statements - from Wikipedia](https://en.wikipedia.org/wiki/Bobby_Fischer#Anti-semitic_statements)
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Elias Canetti: Sekundärliteratur](http://www.tour-literatur.de/sekundlit_autoren/canetti_sekundlit.htm) (German)
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Friedrich Nietzsche from Wikipedia](https://en.wikipedia.org/wiki/Friedrich_Nietzsche)
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Jewish question from Wikipedia](https://en.wikipedia.org/wiki/Jewish_question)
1. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [German: Willkommen](http://fds.duke.edu/db/aas/German/faculty/wcd2/publications)

**[Up one level](Engines "Engines")**

