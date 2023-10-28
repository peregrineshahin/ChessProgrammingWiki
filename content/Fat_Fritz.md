---
title: Fat Fritz
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Fat Fritz**

\[ Unser Fritz [[1]](#cite_note-1)
**Fat Fritz**,

a commercial chess entity by [ChessBase](ChessBase "ChessBase"), the first version released in November 2019 featuring a set of custom made [neural network](Neural_Networks "Neural Networks") weights that work in the open source project [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") within its [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") executable,
while **Fat Fritz 2.0** released in February 2021 is based on [Stockfish 12](Stockfish_NNUE "Stockfish NNUE") and custom [NNUE](NNUE "NNUE") technology.

## Contents

- [1 Fat Fritz 1](#Fat_Fritz_1)
- [2 Fat Fritz 2](#Fat_Fritz_2)
- [3 See also](#See_also)
- [4 Forum Posts](#Forum_Posts)
  - [4.1 2019](#2019)
  - [4.2 2020](#2020)
  - [4.3 2021](#2021)
  - [4.4 2022](#2022)
- [5 Blog Posts](#Blog_Posts)
- [6 External Links](#External_Links)
  - [6.1 Purchase](#Purchase)
  - [6.2 ChessBase News](#ChessBase_News)
    - [6.2.1 2019](#2019_2)
    - [6.2.2 2020](#2020_2)
    - [6.2.3 2021](#2021_2)
  - [6.3 Fritz 17](#Fritz_17)
  - [6.4 Source Code](#Source_Code)
  - [6.5 Rating Lists](#Rating_Lists)
- [7 References](#References)

## Fat Fritz 1

Initially introduced as a cloud project in summer 2019, inspired by [DeepMind's](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)") ground breaking [AlphaZero](AlphaZero "AlphaZero") approach combining [Deep learning](Deep_Learning "Deep Learning") with [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") (MCTS) [[2]](#cite_note-2),
and [Albert Silver's](Albert_Silver "Albert Silver") [Deus X](Deus_X "Deus X") experience, relaxing Leela Chess' "Zero" paradigm of pure [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") due to [supervised learning](Supervised_Learning "Supervised Learning"), Fat Fritz was released in November 2019 as part the [Fritz 17](Fritz "Fritz") package,
best supported by a [GPU](GPU "GPU") card such as [Nvidia](Nvidia "Nvidia") [GeForce 20 series](https://en.wikipedia.org/wiki/GeForce_20_series).
The project and its underlying techniques were emphasized by a talk of [AlphaZero](AlphaZero "AlphaZero") co-author [Thore Graepel](Thore_Graepel "Thore Graepel") at [ChessBase](ChessBase "ChessBase"), attended by German computer chess icon [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") along with his sons and [Math42](https://de.wikipedia.org/wiki/Math42) authors Raphael Nitsche and Maxim Nitsche [[3]](#cite_note-3). Fat Fritz was further supported by [Daniel Uranga](Daniel_Uranga "Daniel Uranga") [[4]](#cite_note-4) [[5]](#cite_note-5).

[](File:Lc0diagram.png)
[](File:Deusx.png)
[Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") and [DeusX](Deus_X "Deus X") aka Fat Fritz components [[6]](#cite_note-6)

## Fat Fritz 2

**Fat Fritz 2**, released on February 09, 2021, is based on [NNUE](NNUE "NNUE") technology and [Stockfish 12](Stockfish "Stockfish") with a double sized network,
and thus, running on a CPU, not requiring expensive [GPU](GPU "GPU") graphic cards for game playing like its predecessor.
The network was trained by [Albert Silver](Albert_Silver "Albert Silver") with the help of [Daniel Uranga](Daniel_Uranga "Daniel Uranga") and [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), who provided scripts and ideas.
Further credits were given to the [Stockfish contributors](Category:Stockfish_Contributor "Category:Stockfish Contributor"), and in particular [Yu Nasu](Yu_Nasu "Yu Nasu") for his groundbreaking work on NNUE, and [Hisayori Noda](Hisayori_Noda "Hisayori Noda") for the initial [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") implementation [[7]](#cite_note-7).
Using the original Fat Fritz as initial supervisor to evaluate chess positions, the learning of Fat Fritz 2 was [reinforced](Reinforcement_Learning "Reinforcement Learning") by Stockfish's [alpha-beta](Alpha-Beta "Alpha-Beta") [search](Search "Search") [[8]](#cite_note-8).
The initial release had the 40 MiB NNUE file embedded inside the Fat Fritz 2 executable,
and was soon separated after the intervention of the Stockfish community due to a possible [GPL license](Free_Software_Foundation#GPL "Free Software Foundation") violation [[9]](#cite_note-9).
While the separated none GPL licensed NNUE file had a replacement on GitHub [[10]](#cite_note-10), it was not identical with the commercial purchased network, yielding in weaker play [[11]](#cite_note-11).
The Stockfish community, denying Fat Fritz 2's originality as claimed by ChessBase, initially reacted with the release of [Stockfish 13](Stockfish "Stockfish") on February 19, 2021 [[12]](#cite_note-12). In summer 2021, the Stockfish team filed a [lawsuit](https://en.wikipedia.org/wiki/Lawsuit) against [ChessBase](ChessBase "ChessBase") to enforce the consequences of the license termination concerning Fat Fritz 2 and the allegedly Stockfish derivative [Houdini 6](Houdini#Stockfish "Houdini") sold by ChessBase [[13]](#cite_note-13). From November 2022, ChessBase has stopped selling both Fat Fritz 2 and [Houdini](Houdini#Stockfish "Houdini") as an agreement with the Stockfish team to end their legal dispute[[14]](#cite_note-14).

## See also

- [AlphaZero](AlphaZero "AlphaZero")
- [Deus X](Deus_X "Deus X")
- [Fat Titz](Fat_Titz "Fat Titz")
- [Fritz](Fritz "Fritz")
- [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
- [NNUE](NNUE "NNUE")
- [YaneuraOu](YaneuraOu "YaneuraOu")

## Forum Posts

## 2019

- ['Deus X' Unveiled as FAT FRITZ PROJECT...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71540) by supersharp77, [CCC](CCC "CCC"), August 13, 2019
- [Match between SF 10 and Fat Fritz](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71658) by Steppenwolf, [CCC](CCC "CCC"), August 26, 2019
- [Chessbase's Albert Silver on LC0 & Fat Fritz](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71661) by supersharp77, [CCC](CCC "CCC"), August 26, 2019
- ["Fat fritz" stronger than Stockfish ?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71906) by Mehdi Amini, [CCC](CCC "CCC"), September 24, 2019
- [UCI Win/Draw/Loss reporting](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72140) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), October 22, 2019
- [Fritz 17](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72170) by sainzlei, [CCC](CCC "CCC"), October 25, 2019
- [Nice review fo Fat Fritz](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72395) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 22, 2019 » [Review](#Review)

## 2020

- [Fat Fritz update](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73275) by Nordlandia, [CCC](CCC "CCC"), March 05, 2020
- [Fat Fritz Update](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76031) by Nordlandia, [CCC](CCC "CCC"), December 09, 2020

[Re: Fat Fritz Update](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76031&start=7) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), December 12, 2020

- [Fat Fritz for Linux](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76105) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), December 20, 2020

## 2021

- [Fat Fritz 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76537) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), February 09, 2021

[Re: Fat Fritz 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76537&start=270) by [gladius](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), February 14, 2021 » [CCRL](CCRL "CCRL")

- [If your idea of innovation ...](https://twitter.com/gcpascutto/status/1359193623171055617?s=20) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [Twitter](https://en.wikipedia.org/wiki/Twitter), February 09, 2021
- [Fat Fratz 2.0 Copyleft Infringement](https://groups.google.com/g/fishcooking/c/VoCCwyRrYT8/m/3N_ShromAgAJ) by Bernt Nicht, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2021

[Re: Fat Fratz 2.0 Copyleft Infringement](https://groups.google.com/g/fishcooking/c/VoCCwyRrYT8/m/V8GrIbdCAgAJ) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2021

- [I'm so disappointed ...](https://twitter.com/tordr/status/1359428424255823875?ref_src=twsrc%5Etfw) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Twitter](https://en.wikipedia.org/wiki/Twitter), February 10, 2021
- [Calling All Armchair GPL Lawyers](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76567) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), February 12, 2021
- [FF2 verses SF, what are the important differences?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76572) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), February 13, 2021
- [Interesting read about Fat Fritz 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76632) by Marc-O Moisan-Plante, [CCC](CCC "CCC"), February 19, 2021
- [Are neural nets (the weights file) copyrightable?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76664) by [Adam Treat](Adam_Treat "Adam Treat"), [CCC](CCC "CCC"), February 21, 2021
- [Fat Fritz 2 nets: Github posted vs commercial](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76673) by Tibono, [CCC](CCC "CCC"), February 22, 2021
- [Why I stood up for Allie is why I stand up for FF2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76686) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), February 23, 2021 » [Allie](Allie "Allie")
- [The distinction between engines and neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76718) by Madeleine Birchfield, [CCC](CCC "CCC"), February 26, 2021
- [An actual interesting computer chess read about FF2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76730) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), February 27, 2021 » [Stephen Ham article](#StephenHam)
- [How to make a double-sized net as good as SF NNUE in a few easy steps](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76742) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), February 28, 2021
- [It walks like a clone, it quacks like a clone ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76826) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), March 09, 2021
- [Time to rethink what Albert Silver has done?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77612) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), July 03, 2021
- [Fat Fritz question](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77752) by Leo Anger, [CCC](CCC "CCC"), July 18, 2021
- [Stockfish: Our lawsuit against ChessBase](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77762) by Kurt Lanc, [CCC](CCC "CCC"), July 20, 2021
- [Stockfish sues Chessbase!](https://prodeo.actieforum.com/t465-stockfish-sues-chessbase) by mwyoung, [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), July 20, 2021

## 2022

- [SF vs ChessBase declared a draw](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=81029) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), November 19, 2022

## Blog Posts

[[15]](#cite_note-15)

- [Fat Fritz 2 - Ein unmoralisches Angebot](https://schach.computer/fat-fritz-2-ein-unmoralisches-angebot/) by [Topschach Benny](https://schach.computer/author/schachfreunde/), February 12, 2021 (German)
- [Statement on Fat Fritz 2](https://blog.stockfishchess.org/post/643239805544792064/statement-on-fat-fritz-2) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [Stockfish Blog](Computer_Chess_Forums "Computer Chess Forums"), February 15, 2021
- [Fat Fritz 2 is a rip-off](https://lichess.org/blog/YCvy7xMAACIA8007/fat-fritz-2-is-a-rip-off), The [Stockfish](Stockfish "Stockfish"), [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") and [Lichess](index.php?title=Lichess&action=edit&redlink=1 "Lichess (page does not exist)") teams, February 16, 2021
- [ChessBase’s Fat Fritz 2 condemned as ‘rip-off’ Stockfish clone](https://chess24.com/en/read/news/chessbase-s-fat-fritz-2-condemned-as-rip-off-stockfish-clone) by [Colin McGourty](index.php?title=Colin_McGourty&action=edit&redlink=1 "Colin McGourty (page does not exist)"), [Chess24](index.php?title=Chess24&action=edit&redlink=1 "Chess24 (page does not exist)"), February 22, 2021
- [Open Source Community Critical Of Chessbase, Fat Fritz 2](https://www.chess.com/news/view/chessbase-fat-fritz-2-stockfish-leela-chess-zero) by [Peter Doggers](Peter_Doggers "Peter Doggers"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), February 24, 2021 » [Matthew L. Ginsberg](Matthew_L._Ginsberg "Matthew L. Ginsberg")
- [Our lawsuit against ChessBase](https://stockfishchess.org/blog/2021/our-lawsuit-against-chessbase/), [The Stockfish Team](Stockfish "Stockfish"), [Stockfish Blog](Computer_Chess_Forums "Computer Chess Forums"), July 20, 2021 » [Houdini 6](Houdini#Stockfish "Houdini")
- [Fat Fritz is not the Only Ripoff and now ChessBase is Getting Sued](https://lichess.org/blog/YPc7GREAACgAevs5/fat-fritz-is-not-the-only-ripoff-and-now-chessbase-is-getting-sued), [Lichess](index.php?title=Lichess&action=edit&redlink=1 "Lichess (page does not exist)"), July 20, 2021
- [Stockfish Developers Sue Chessbase Claiming Copyright Violation](https://www.chess.com/news/view/stockfish-developers-sue-chessbase-claiming-copyright-violation) by [Peter Doggers](Peter_Doggers "Peter Doggers"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), July 23, 2021
- [ChessBase GmbH and the Stockfish team reach an agreement and end their legal dispute](https://stockfishchess.org/blog/2022/chessbase-stockfish-agreement/) by [The Stockfish team](Stockfish "Stockfish"), [Stockfish Blog](index.php?title=Stockfish_Blog&action=edit&redlink=1 "Stockfish Blog (page does not exist)"), November 18, 2022

## External Links

## Purchase

- [Fritz 17 - The giant PC chess program, now with Fat Fritz](https://shop.chessbase.com/en/products/fritz_17) - [ChessBase Shop](ChessBase "ChessBase")
- [Fat Fritz 2 SE](https://shop.chessbase.com/en/products/fat_fritz_2) - [ChessBase Shop](ChessBase "ChessBase")
- [Fat Fritz 2 SE + Fritz Powerbook 2021](https://shop.chessbase.com/en/products/fat_fritz_2_powerbook_2021) - [ChessBase Shop](ChessBase "ChessBase")
- [Fat Fritz 2.0 SE](https://store.steampowered.com/app/1587750/Fat_Fritz_20_SE/) on [Steam](<https://en.wikipedia.org/wiki/Steam_(service)>)
- [Fat Fritz 2.0 SE](https://www.newinchess.com/fat-fritz-2-0), [New In Chess](https://en.wikipedia.org/wiki/New_In_Chess)
- [Fat Fritz 2.0 SE](https://www.houseofstaunton.com/fat-fritz-2-0.html), [House Of Staunton](https://en.wikipedia.org/wiki/House_of_Staunton)
- [Fat Fritz 2.0 SE](https://www.uscfsales.com/fat-fritz-2-0.html), [The Official Chess Shop of the US Chess Federation - Chess Pieces, Chess Sets, Chess Boards, Chess Clocks and More!](https://www.uscfsales.com/)
- [Amazon.com: Fat Fritz 2.0 Chess Playing Software Bundled with Chess Success II Chess Training DVD: Toys & Games](https://www.amazon.com/Playing-Software-Bundled-Success-Training/dp/B08W1WYXG3/ref=sr_1_1?dchild=1&keywords=Fat+Fritz+2&qid=1626991799&sr=8-1)

## ChessBase News

### 2019

- [Fat Fritz – What on Earth is that?](https://en.chessbase.com/post/fat-fritz-what-on-earth-is-that) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), August 13, 2019
- [Using Fat Fritz in the Engine Cloud](https://en.chessbase.com/post/using-fat-fritz-in-the-engine-cloud) by [Nadja Wittmann](https://de.chessbase.com/author/nadja-wittmann), [ChessBase News](ChessBase "ChessBase"), August 15, 2019
- [Analysing your openings repertoire with Fat Fritz](https://en.chessbase.com/post/analysing-your-openings-repertoire-with-fat-fritz), [ChessBase News](ChessBase "ChessBase"), September 02, 2019
- [GM preparation with Fat Fritz](https://en.chessbase.com/post/gm-preparation-with-fat-fritz) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), September 12, 2019
- [Standing on the shoulders of giants](https://en.chessbase.com/post/standing-on-the-shoulders-of-giants) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), September 18, 2019
- [Fat Fritz analysis: A matter of technique](https://en.chessbase.com/post/fat-fritz-analyzes-a-matter-of-technique) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), September 24, 2019
- [Fat Fritz: Small differences, big effect](https://en.chessbase.com/post/fat-fritz-small-differences-big-effect) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), October 09, 2019
- ["Fat Fritz seemed to be from an entirely different plane of existence!"](https://en.chessbase.com/post/fat-fritz-and-the-amateur) by [Tanmay Srinath](https://en.chessbase.com/author/tanmay-srinath), [ChessBase News](ChessBase "ChessBase"), November 04, 2019
- [Fat Fritz defeats Stockfish in 100-game matches](https://en.chessbase.com/post/fat-fritz-defeats-stockfish-match-2) by [Elshan Moradiabadi](https://en.wikipedia.org/wiki/Elshan_Moradi), [ChessBase News](ChessBase "ChessBase"), November 06, 2019 » [Stockfish](Stockfish "Stockfish")
- [Fat Fritz outmatches Stockfish (part 2)](https://en.chessbase.com/post/fat-fritz-defeats-stockfish-match) by [Elshan Moradiabadi](https://en.wikipedia.org/wiki/Elshan_Moradi), [ChessBase News](ChessBase "ChessBase"), November 07, 2019
- [Fat Fritz: what videocard to buy](https://en.chessbase.com/post/fat-fritz-what-videocard-to-buy) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), November 14, 2019
- [Optimizing Fat Fritz, the top rated engine in the world](https://en.chessbase.com/post/optimizing-fat-fritz) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), November 25, 2019
- [Fat Fritz in the cloud](https://en.chessbase.com/post/fat-fritz-in-the-cloud) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), November 28, 2019

### 2020

- [Fat Fritz for the club player](https://en.chessbase.com/post/fat-fritz-and-the-1200) by [Tanmay Srinath](https://en.chessbase.com/author/tanmay-srinath), [ChessBase News](ChessBase "ChessBase"), January 09, 2020
- [Fat Fritz 1.1 update and a small gift](https://en.chessbase.com/post/fat-fritz-update-and-fat-fritz-jr) by [Albert Silver](Albert_Silver "Albert Silver"). [ChessBase News](ChessBase "ChessBase"), March 05, 2020
- [Out-preparing the Candidates with Fat Fritz (Part 1)](https://en.chessbase.com/post/out-preparing-the-candidates-with-fat-fritz-part-1) by [Tanmay Srinath](https://en.chessbase.com/author/tanmay-srinath), [ChessBase News](ChessBase "ChessBase"), March 21, 2020
- [Out-preparing the Candidates with Fat Fritz (Part 2)](https://en.chessbase.com/post/out-preparing-the-candidates-with-fat-fritz-part-2) by [Tanmay Srinath](https://en.chessbase.com/author/tanmay-srinath), [ChessBase News](ChessBase "ChessBase"), March 25, 2020
- [Fat Fritz: strong, creative, original](https://en.chessbase.com/post/fat-fritz-ingenious-without-stereotypes) by [Stephan Oliver Platz](index.php?title=Stephan_Oliver_Platz&action=edit&redlink=1 "Stephan Oliver Platz (page does not exist)"), [ChessBase News](ChessBase "ChessBase"), March 27, 2020
- [Running Leela and Fat Fritz on your notebook](https://en.chessbase.com/post/running-leela-and-fat-fritz-on-your-notebook) by [Evelyn Zhu](https://ratings.fide.com/card.phtml?event=2099713), [ChessBase News](ChessBase "ChessBase"), June 14, 2020 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")

### 2021

- [Fat Fritz 2.0 - The new number 1](https://en.chessbase.com/post/fat-fritz-2-0-the-new-number-1), [ChessBase News](ChessBase "ChessBase"), February 09, 2021

- [Fat Fritz 2: The Best of Both Worlds](https://en.chessbase.com/post/fat-fritz-2-best-of-both-worlds) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), February 11, 2021

- [Interview with Albert Silver - His journey to Fat Fritz 2.0](https://en.chessbase.com/post/interview-with-albert-silver-his-journey-to-fat-fritz-2-0) by [Arne Kaehler](https://www.udemy.com/user/arne-kaehler/), [ChessBase News](ChessBase "ChessBase"), February 12, 2021, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- [How a neural network is made](https://en.chessbase.com/post/how-a-neural-network-is-made) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), February 21, 2021

- [Discussing moves with a neural network](https://en.chessbase.com/post/discussing-moves-with-a-neural-network) by [Stephen Ham](index.php?title=Stephen_Ham&action=edit&redlink=1 "Stephen Ham (page does not exist)"), [ChessBase News](ChessBase "ChessBase"), February 27, 2021 [[16]](#cite_note-16)

- [Steamrolling the king](https://en.chessbase.com/post/steamrolling-the-king), [ChessBase News](ChessBase "ChessBase"), June 15, 2021

- [Solving the impossible](https://en.chessbase.com/post/solving-the-impossible) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), June 24, 2021

## Fritz 17

- [Introducing Fritz 17 with Fat Fritz and other goodies](https://en.chessbase.com/post/fritz-17-with-fat-fritz-and-goodies), [ChessBase News](ChessBase "ChessBase"), November 12, 2019
- [Fat Fritz and Fritz 17: A Review (Part I)](https://new.uschess.org/news/fat-fritz-fritz-17-review-i/) by [John Hartmann](https://en.chessbase.com/author/john-hartmann), [US Chess](https://en.wikipedia.org/wiki/United_States_Chess_Federation), November 17, 2019
- [Fat Fritz and Fritz 17: A Review (Part II)](https://new.uschess.org/news/fat-fritz-fritz-17-review-part-ii/) by [John Hartmann](https://en.chessbase.com/author/john-hartmann), [US Chess](https://en.wikipedia.org/wiki/United_States_Chess_Federation), November 19, 2019 [[17]](#cite_note-17)

## Source Code

- [GitHub - DanielUranga/lc0 at uci-wdl-reporting](https://github.com/DanielUranga/lc0/tree/uci-wdl-reporting) by [Daniel Uranga](Daniel_Uranga "Daniel Uranga")
- [lc0 84 - AppVeyor](https://ci.appveyor.com/project/DanielUranga/lc0)
- [GitHub - kiudee/bayes-skopt: A fully Bayesian implementation of sequential model-based optimization](https://github.com/kiudee/bayes-skopt) by [Karlson Pfannschmidt](Karlson_Pfannschmidt "Karlson Pfannschmidt") [[18]](#cite_note-18)
- [GitHub - yaneurao/YaneuraOu: YaneuraOu is the World's Strongest Shogi engine(AI player), WCSC29 1st winner, educational and USI compliant engine](https://github.com/yaneurao/YaneuraOu) » [YaneuraOu](YaneuraOu "YaneuraOu")
- [GitHub - DanielUranga/Stockfish at ff2](https://github.com/DanielUranga/Stockfish/tree/ff2) by [Daniel Uranga](Daniel_Uranga "Daniel Uranga")

## [ff2 · DanielUranga/Stockfish@e44edde · GitHub](https://github.com/DanielUranga/Stockfish/commit/e44edde482ad06154c5133173245fdd2ad48a8cc#diff-a29c7f79728b32e998f606ae6f2fd2cb7c4a654fb0cef86547335542ca8ac054R38) [FF2 · DanielUranga/Stockfish@faef72a · GitHub](https://github.com/DanielUranga/Stockfish/commit/faef72afbf10273ca8688a4ba1c7863426c93c6e) [Stockfish/FatFritz2_v1.bin at ff2 · DanielUranga/Stockfish · GitHub](https://github.com/DanielUranga/Stockfish/blob/ff2/src/FatFritz2_v1.bin) Rating Lists

- [Fat Fritz](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Fritz&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")
- [Fat Fritz](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Fritz&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## References

1. [↑](#cite_ref-1) [Malakov tower](https://de.wikipedia.org/wiki/Malakow-Turm) (build 1873) of Colliery [Unser Fritz](https://de.wikipedia.org/wiki/Zeche_Unser_Fritz), Shaft 1, in [Herne, North Rhine-Westphalia](https://en.wikipedia.org/wiki/Herne,_North_Rhine-Westphalia), part of [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail") of the [Ruhr area](https://en.wikipedia.org/wiki/Ruhr). Photo by GeorgeIvan, May 15, 2014, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Unser Fritz/Crange](https://de.wikipedia.org/wiki/Unser_Fritz/Crange) is further district of Herne (Wanne), famous for its funfair [Cranger Kirmes](https://en.wikipedia.org/wiki/Cranger_Kirmes), and [SV Unser Fritz](http://www.sv-unser-fritz.de/) the local chess club - eponym of the coal mine was [Frederick III, German Emperor](https://en.wikipedia.org/wiki/Frederick_III,_German_Emperor)
1. [↑](#cite_ref-2) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
1. [↑](#cite_ref-3) [Fat Fritz – What on Earth is that?](https://en.chessbase.com/post/fat-fritz-what-on-earth-is-that) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), August 13, 2019
1. [↑](#cite_ref-4) [Standing on the shoulders of giants](https://en.chessbase.com/post/standing-on-the-shoulders-of-giants) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), September 18, 2019
1. [↑](#cite_ref-5) [GitHub - DanielUranga/lc0 at uci-wdl-reporting](https://github.com/DanielUranga/lc0/tree/uci-wdl-reporting)
1. [↑](#cite_ref-6) [My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822) by [Alexander Lyashuk](Alexander_Lyashuk "Alexander Lyashuk"), [CCC](CCC "CCC"), September 14, 2019 » [TCEC](TCEC "TCEC")
1. [↑](#cite_ref-7) [Fat Fritz 2: The Best of Both Worlds](https://en.chessbase.com/post/fat-fritz-2-best-of-both-worlds) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), February 10, 2021
1. [↑](#cite_ref-8) [Fat Fritz 2.0 - The new number 1](https://en.chessbase.com/post/fat-fritz-2-0-the-new-number-1), [ChessBase News](ChessBase "ChessBase"), February 09, 2021
1. [↑](#cite_ref-9) [Statement on Fat Fritz 2](https://blog.stockfishchess.org/post/643239805544792064/statement-on-fat-fritz-2) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [Stockfish Blog](Computer_Chess_Forums "Computer Chess Forums"), February 15, 2021
1. [↑](#cite_ref-10) [Stockfish/FatFritz2_v1.bin at ff2 · DanielUranga/Stockfish · GitHub](https://github.com/DanielUranga/Stockfish/blob/ff2/src/FatFritz2_v1.bin)
1. [↑](#cite_ref-11) [Re: Fat Fritz 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76537&start=238) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), February 13, 2021
1. [↑](#cite_ref-12) [Stockfish 13](https://blog.stockfishchess.org/post/643570707142492160/stockfish-13), The Stockfish Team, February 19, 2021
1. [↑](#cite_ref-13) [Our lawsuit against ChessBase](https://stockfishchess.org/blog/2021/our-lawsuit-against-chessbase/), [The Stockfish team](Stockfish "Stockfish"), [Stockfish Blog](Computer_Chess_Forums "Computer Chess Forums"), July 20, 2021
1. [↑](#cite_ref-14) [ChessBase GmbH and the Stockfish team reach an agreement and end their legal dispute](https://stockfishchess.org/blog/2022/chessbase-stockfish-agreement/) by [The Stockfish team](Stockfish "Stockfish"), [Stockfish Blog](index.php?title=Stockfish_Blog&action=edit&redlink=1 "Stockfish Blog (page does not exist)"), November 18, 2022
1. [↑](#cite_ref-15) [fatfritz.net](https://www.fatfritz.net/)
1. [↑](#cite_ref-16) [An actual interesting computer chess read about FF2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76730) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), February 27, 2021
1. [↑](#cite_ref-17) [Nice review fo Fat Fritz](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72395) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 22, 2019
1. [↑](#cite_ref-18) [Fat Fritz 1.1 update and a small gift](https://en.chessbase.com/post/fat-fritz-update-and-fat-fritz-jr) by [Albert Silver](Albert_Silver "Albert Silver"). [ChessBase News](ChessBase "ChessBase"), March 05, 2020

**[Up one Level](Engines "Engines")**

