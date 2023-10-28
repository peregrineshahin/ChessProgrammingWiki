---
title: Chess Game
---
**[Home](Home "Home") * [Chess](Chess "Chess") * Game**

[](File:ChessIsenburgII20150928.jpg) A Game of Chess <a id="cite-note-1" href="#cite-ref-1">[1]</a>
The **Game of Chess** which is actually played (or analyzed) by a chess program via its [user interface](GUI "GUI") requires a [game record](Game_Notation "Game Notation"), or game history, which is a [list](Move_List "Move List") or [array](Array "Array") of [moves](Moves "Moves") or a tree of alternative move variants even containing comments. While the game record is necessary to take back moves f.i. after operator errors, the game history needs to be considered if it is about to claim or accepts [draws](Draw "Draw") by [three fold repetitions](Repetitions "Repetitions"), and might therefor be referred by the [search algorithm](Search "Search") as well.

## Contents

- [1 Start of the Game](#start-of-the-game)
- [2 End of the Game](#end-of-the-game)
  - [2.1 Win/Loss](#win.2floss)
  - [2.2 Draw](#draw)
- [3 Game Record](#game-record)
- [4 Game Header](#game-header)
- [5 Longest Game](#longest-game)
- [6 MVC](#mvc)
- [7 The Game Loop](#the-game-loop)
  - [7.1 CLI](#cli)
  - [7.2 Event driven GUIs](#event-driven-guis)
- [8 See also](#see-also)
- [9 Publications](#publications)
- [10 Forum Posts](#forum-posts)
  - [10.1 2010 ...](#2010-...)
  - [10.2 2020 ...](#2020-...)
- [11 External Links](#external-links)
- [12 References](#references)

## Start of the Game

The game of chess starts with the [initial position](Initial_Position "Initial Position"), white to move. Both sides alternately move their pieces until the game is finished.

## End of the Game

There are three possible outcomes of the game, white wins (1-0), black wins (0-1) or [draw](Draw "Draw") (1/2-1/2). Unfinished games may be [adjudicated](https://en.wikipedia.org/wiki/Adjournment#Chess), which was common until the 80s in [computer chess tournaments](Tournaments_and_Matches "Tournaments and Matches"), for instance the adjudicated win of [Cray Blitz](Cray_Blitz "Cray Blitz") against [Schach 2.7](Schach "Schach") during [WCCC 1986](WCCC_1986 "WCCC 1986") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . [Checkmate](Checkmate "Checkmate") and [stalemate](Stalemate "Stalemate") finish the game immediately. Other occurrences usually require communication with the opponent and admission or adjudication of an arbiter instance (i.e. Tournament director), which in computer chess requires a protocol and/or interaction, like claiming a [threefold repetition](Repetitions "Repetitions") draw in over the board computer chess.

*see main article [Rules of Chess](Rules_of_Chess "Rules of Chess")*

## Win/Loss

Since chess is a [Zero-sum game](https://en.wikipedia.org/wiki/Zero-sum_game), the win of one player is the loss of the other player.

- [Checkmate](Checkmate "Checkmate") - if in [check](Check "Check") with an empty set of [legal moves](Legal_Move "Legal Move")
- [Loss on time](Time_Management "Time Management")
- [Resignation](https://en.wikipedia.org/wiki/Resignation) (to resign)

## Draw

The game of chess ends and is [draw](Draw "Draw") after either

- [Stalemate](Stalemate "Stalemate") - if **not** in [check](Check "Check") but no [legal moves](Legal_Move "Legal Move")
- Correct [threefold repetition](Repetitions "Repetitions") claim
- Correct [fifty-move rule](Fifty-move_Rule "Fifty-move Rule") claim
- [Insufficient material](Material#InsufficientMaterial "Material")
- Draw offer accepted

## Game Record

Chess programs (not necessarily the pure (search) engine) keep track of all [moves](Moves "Moves") played in the game from the [initial starting position](Initial_Position "Initial Position") stored inside a [move list](Move_List "Move List"), often in conjunction with a [list](Move_List#SignatureList "Move List") of [Zobrist](Zobrist_Hashing "Zobrist Hashing") or [BCH signatures](BCH_Hashing "BCH Hashing") of the up to 100 last [reversible moves](Reversible_Moves "Reversible Moves") for the purpose to detect twofold or threefold [repetitions](Repetitions "Repetitions").

- [Game Notation](Game_Notation "Game Notation")
  - [Algebraic Chess Notation](Algebraic_Chess_Notation "Algebraic Chess Notation")
  - [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")
- [Move List](Move_List "Move List")

## Game Header

The game header keeps [metadata](https://en.wikipedia.org/wiki/Metadata) of a game, such as player names, date of the game and site of the event and result. For instance, the [PGN](Portable_Game_Notation "Portable Game Notation") game header consists of a set of [attribute value pairs](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair). The so called **Seven Tag Roster** (STR) is mandatory <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

1. Event (the name of the tournament or match event)
1. Site (the location of the event)
1. Date (the starting date of the game)
1. Round (the playing round ordinal of the game)
1. White (the player of the white pieces)
1. Black (the player of the black pieces)
1. Result (the result of the game)

## Longest Game

In 1966, Eero Bonsdorff, [Karl Fabel](https://en.wikipedia.org/wiki/Karl_Fabel), and Olvai Riihimaa gave 5899 as the maximum number of [moves](Moves "Moves") in a chess game, considering the [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## MVC

The chess program and its [user interface](User_Interface "User Interface") can be interpreted as a [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (MVC), an [architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern_%28computer_science%29) that isolates [business logic](https://en.wikipedia.org/wiki/Business_logic) f.i. game administration, [time management](Time_Management "Time Management") and searching a move inside a chess program from input and presentation. The game model represents the domain-specific [data](Data "Data") on which the application operates - Inside a chess program, the information about the [initial position](Initial_Position "Initial Position") and the game record to reproduce the current positions, likely subject of [search](Search "Search") or [pondering](Pondering "Pondering") during game play. The model and controller implement a [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) which controls the game, its [states](https://en.wikipedia.org/wiki/State_%28computer_science%29), state transitions and actions considering various [modes](https://en.wikipedia.org/wiki/Mode_%28computer_interface%29). The view displays the [game notation](Game_Notation "Game Notation"), a [list of moves](Move_List "Move List"), and likely the board with the current [position](Chess_Position "Chess Position"), suitable for [interaction](https://en.wikipedia.org/wiki/Interaction) inside a [user interface](User_Interface "User Interface"). The controller receives input from various sources and devices, such as [keyboard](https://en.wikipedia.org/wiki/Keyboard_%28computing%29), [mouse](https://en.wikipedia.org/wiki/Mouse_%28computing%29), [serial port](https://en.wikipedia.org/wiki/Serial_port) and [internet socket](https://en.wikipedia.org/wiki/Internet_socket), and initiates a response by making calls on model objects.

## The Game Loop

Early chess programs without [Pondering](Pondering "Pondering") used a simple sequential control structure to play the whole game for instance via a [teleprinter](https://en.wikipedia.org/wiki/Teleprinter) or any [Computer terminals](https://en.wikipedia.org/wiki/Computer_terminal) in a sequential manner.

```

state := playGame;
initialize position
print board
while (state != gameover)
   wait for input of a move by the user
   make move (if legal)
   if (mate or stalemate) {
      state := gameOver;
      break;
   }
   search move with allocated time
   make move
   print move and update board
   if (mate or stalemate)
      state := gameOver;
}
print "thank you for playing the game";

```

## CLI

Most current chess engines communicate via a sequential [command-line interface](CLI "CLI"), available in all common [operating systems](https://en.wikipedia.org/wiki/Operating_system). [Pondering](Pondering "Pondering") and the need to [enter moves](Entering_Moves "Entering Moves") and commands even if the program is "thinking", requires a more complicated control structure and an interruptible search routine. Often engines used [coroutines](https://en.wikipedia.org/wiki/Coroutine) to implement internal [context switching](https://en.wikipedia.org/wiki/Context_switch) between search and user interaction. Today, it is more common to rely on [multithreading](https://en.wikipedia.org/wiki/Multi-threading) abilities of recent operating systems, and to use an explicit I/O-thread, while the search routine is regularly pondering whether it needs to be interrupted by pending input received by another thread, with the option to asynchronous stop the search.

## Event driven GUIs

With the advent of operating systems with [graphical user interfaces](https://en.wikipedia.org/wiki/Graphical_user_interface), also encouraged by additional input devices such as a [computer mouse](https://en.wikipedia.org/wiki/Mouse_%28computing%29) for asynchronous user interaction, the embedding of a chess engine with a classical CLI inside the [event-driven architecture](https://en.wikipedia.org/wiki/Event-driven_architecture) of a graphical user interface became more difficult. Today, most programmers rely on external event driven [graphical user interface](GUI "GUI") applications using [standard streams](https://en.wikipedia.org/wiki/Standard_streams) or [pipelines](https://en.wikipedia.org/wiki/Pipeline_%28Unix%29) to communicate with the GUI via protocols such as the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and the [Universal Chess Interface](UCI "UCI"). The external GUI application constitutes the MVC view and controller, and more or less even parts of a (redundant) game model (or even multi-game model), to make the GUI aware of its own game states to even make decisions on behalf of the engine, such as move selection from opening books and [endgame tablebases](Endgame_Tablebases "Endgame Tablebases"), draw claims and offers and to finally declare the game over. These game interacting features of the external GUI application in conjunction with certain protocols such as UCI by far exceeds what a pure chess user interface was initially designed for - controller and view only, enter legal moves and render the state of the game, which has become disputed issue in playing official [tournament](Tournaments_and_Matches "Tournaments and Matches") games.

## See also

- [Board Representation](Board_Representation "Board Representation")
- [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
- [Chess Position](Chess_Position "Chess Position")
- [Contempt Factor](Contempt_Factor "Contempt Factor")
- [Graphical User Interface](GUI "GUI")
- [Match Statistics](Match_Statistics "Match Statistics")
- [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
- [Strategy](Strategy "Strategy")
- [Tactics](Tactics "Tactics")
- [Time Management](Time_Management "Time Management")
- [UCI](UCI "UCI")
- [User Interface](User_Interface "User Interface")

## Publications

- [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1990**). *Compressing Chess Games with the Help of a fast Deterministic Chess Program.* [ICCA Journal, Vol. 13, No. 4](ICGA_Journal#13_4 "ICGA Journal")
- [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1991**): *[Data compression using an intelligent generator: The storage of chess games as an example](http://www.sciencedirect.com/science/article/pii/000437029190026G)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 52, No. 1
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2005**). *[The Representation of Chess Game](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1491153)*. Proceedings of the 27th International Conference on Information Technology Interfaces
- [Nick Pelling](Nick_Pelling "Nick Pelling") (**2013**). *[Chess Superminiatures](https://www.amazon.co.uk/Chess-Superminiatures-Nick-Pelling-ebook/dp/B00HEOZ8B6)*. [eBook](https://en.wikipedia.org/wiki/E-book), [Kindle edition](https://en.wikipedia.org/wiki/Amazon_Kindle), [Amazon](https://en.wikipedia.org/wiki/Amazon.com)

## Forum Posts

## 2010 ...

- [One billion random games](http://www.talkchess.com/forum/viewtopic.php?t=40193) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 27, 2011
- [One billion random games](http://www.talkchess.com/forum/viewtopic.php?t=48542) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 03, 2013
- [Revised source for the random game generator](http://www.talkchess.com/forum/viewtopic.php?t=56328) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 12, 2015
- [Random game mating probabilities](http://www.talkchess.com/forum/viewtopic.php?t=59483) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 12, 2016
- [This should be in the wiki](http://www.talkchess.com/forum/viewtopic.php?t=59841&start=14) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 13, 2016 » [Repetitions](Repetitions "Repetitions")
- [Photographing Chess Clock](http://www.talkchess.com/forum/viewtopic.php?t=61672) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 10, 2016
- [What can be said about 1 - 0 score?](http://www.talkchess.com/forum/viewtopic.php?t=63572) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 28, 2017 » [Match Statistics](Match_Statistics "Match Statistics")

## 2020 ...

- [Open Chess Game Database Standard (OCGDB)](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78464) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), October 20, 2021 » [Chess Databases](Databases "Databases")

## External Links

- [Game Of Chess](http://c2.com/cgi/wiki?GameOfChess)
- [Chess notation from Wikipedia](https://en.wikipedia.org/wiki/Chess_notation)
- [Representation of Chess Game - Computer Architecture and Languages Laboratory](http://labraj.uni-mb.si/en/Representation_of_Chess_Game), [University of Maribor](University_of_Maribor "University of Maribor")
- How many chess games are possible? by [Dr James Grime](http://singingbanana.com/), [numberphile](http://numberphile.com/team/index.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A Game of Chess in the [Middle Ages](https://en.wikipedia.org/wiki/Middle_Ages), Image photographed from an explanation table labeled "Die Essener Isenburg" at the [Isenburg Castle](https://de.wikipedia.org/wiki/Neue_Isenburg) in [Essen](https://en.wikipedia.org/wiki/Essen), Germany, by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), September 28, 2015
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Helmut Horacek](Helmut_Horacek "Helmut Horacek"), (**1986**) *The Fifth World Computer Chess Championship Cologne, 1986*, Research Unit for Information Science and Artificial Intelligence, [University of Hamburg](University_of_Hamburg "University of Hamburg"), from ***Kings move** Welcome to the 1989 AGT World Computer Chess Championship.* pg 21, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Standard: Portable Game Notation Specification and Implementation Guide](http://www.thechessdrum.net/PGN_Reference.txt) by [Steven Edwards](Steven_Edwards "Steven Edwards"), 8.1.1: Seven Tag Roster
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Eero Bonsdorff, [Karl Fabel](https://en.wikipedia.org/wiki/Karl_Fabel), Olvai Riihimaa (**1966**) *Schach und Zahl - Unterhaltsame Schachmathematik*. Seite 11-13, Walter Rau Verlag, Düsseldorf (German)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [50-Züge-Regel - Schachmathematik from Wikipedia.de](http://de.wikipedia.org/wiki/50-Z%C3%BCge-Regel#Schachmathematik) (German)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Defending Humanity's Honor](http://www.xs4all.nl/~timkr/chess2/honor.htm) by [Tim Krabbé](https://en.wikipedia.org/wiki/Tim_Krabb%C3%A9), see game [NewRival](Rival "Rival") - [Faile](Faile "Faile") with 493 moves, and playing 402 moves with bare kings!
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Claude Shannon](Claude_Shannon "Claude Shannon"), [Shannon number](https://en.wikipedia.org/wiki/Shannon_number), [Godfrey Harold Hardy](Mathematician#Hardy "Mathematician"), [A googolplex of Go games](Matthieu_Walraet#googolplex "Matthieu Walraet")

**[Up one Level](Chess "Chess")**

