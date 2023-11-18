---
title: User Interface
---
**[Home](Home "Home") \* User Interface**



[ User Interface of [The Turk](https://en.wikipedia.org/wiki/The_Turk) <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>
The **User Interface** is the space where [Human-computer interaction](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction) takes place <a id="cite-note-6" href="#cite-ref-6">[6]</a> . The [user](https://en.wikipedia.org/wiki/User_%28computing%29) [interface](https://en.wikipedia.org/wiki/Interface_%28computer_science%29) includes [hardware](Hardware "Hardware") (physical) and [software](Software "Software") (logical) components, and allow users to manipulate a system ([Input](https://en.wikipedia.org/wiki/Input_device)), i.e. to [enter moves](Entering_Moves "Entering Moves") inside a chess program, and the system to indicate the effects of the users' manipulation ([Output](https://en.wikipedia.org/wiki/Output_device)), i.e. display moves and [positions](Chess_Position "Chess Position"). Chess programs require support by the underlaying [BIOS](https://en.wikipedia.org/wiki/BIOS) and [operating system](https://en.wikipedia.org/wiki/Operating_system), accessible by embedded [programming language](Languages "Languages") features, or via an [Application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) (API) of a [standard](https://en.wikipedia.org/wiki/Standard_library) or external [library](https://en.wikipedia.org/wiki/Library_%28computer_science%29).



## The Game Loop


Early chess programs, running on [mainframe computers](https://en.wikipedia.org/wiki/Mainframe_computer), like [The Bernstein Chess Program](The_Bernstein_Chess_Program "The Bernstein Chess Program") on an [IBM 704](IBM_704 "IBM 704"), used a simple sequential control structure to play the whole [game](Chess_Game "Chess Game"). As feedback for user interactions or indicating state transitions, for instance if the [search](Search "Search") finished with a move played on the internal board, [ASCII diagrams](Graphics_Programming#ASCIIDiagrams "Graphics Programming") and [move lists](Move_List "Move List") were printed or displayed on a [teleprinter](https://en.wikipedia.org/wiki/Teleprinter), [CRT (cathode ray tube)](https://en.wikipedia.org/wiki/Cathode_ray_tube) or any other [Computer terminal](https://en.wikipedia.org/wiki/Computer_terminal), to prompt [input](https://en.wikipedia.org/wiki/Input_device) which the user had to [enter](Entering_Moves "Entering Moves") by a dedicated or standard teletype <a id="cite-note-8" href="#cite-ref-8">[8]</a> [keyboard](https://en.wikipedia.org/wiki/Computer_keyboard). Initially, after start of the program, or during game play, while prompting a move, certain [commands](https://en.wikipedia.org/wiki/Command_%28computing%29) may be entered, either to switch modes, to set the game level, to start the game, to force or take-back a move, to switch sides, and whatever else. The usual syntax to input moves is to enter [algebraic coordinates](Algebraic_Chess_Notation#PureCoordinateNotation "Algebraic Chess Notation"), that is [file letter](Files "Files"), [rank number](Ranks "Ranks") of [origin](Origin_Square "Origin Square") and [target square](Target_Square "Target Square") of a move to play, confirmed and sent to the program after entering [carriage return](https://en.wikipedia.org/wiki/Carriage_return).



## MVC


The chess program and its user interface can be interpreted as a [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (MVC), an [architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern_%28computer_science%29) that isolates [business logic](https://en.wikipedia.org/wiki/Business_logic) f.i. game administration, [time management](Time_Management "Time Management") and searching a move inside a chess program from input and presentation. The game model represents the domain-specific [data](Data "Data") on which the application operates - Inside a chess program, the information about the [initial position](Initial_Position "Initial Position") and the game record to reproduce the current positions, likely subject of [search](Search "Search") or [pondering](Pondering "Pondering") during game play. The model and controller implement a [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) which controls the game, its [states](https://en.wikipedia.org/wiki/State_%28computer_science%29), state transitions and actions considering various [modes](https://en.wikipedia.org/wiki/Mode_%28computer_interface%29). The view displays the [game notation](Game_Notation "Game Notation"), a [list of moves](Move_List "Move List"), and likely the board with the current [position](Chess_Position "Chess Position"), suitable for [interaction](https://en.wikipedia.org/wiki/Interaction) inside a user interface. The controller receives input from various sources and devices, such as [keyboard](https://en.wikipedia.org/wiki/Keyboard_%28computing%29), [mouse](https://en.wikipedia.org/wiki/Mouse_%28computing%29), [serial port](https://en.wikipedia.org/wiki/Serial_port) and [internet socket](https://en.wikipedia.org/wiki/Internet_socket), and initiates a response by making calls on model objects.



### CLI


*see main article [Command Line Interface](CLI "CLI")*.


Most current chess engines communicate via a sequential [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface), available in all common [operating systems](https://en.wikipedia.org/wiki/Operating_system). [Pondering](Pondering "Pondering") and the need to enter moves and commands even if the program is "thinking", requires a more complicated control structure and an interruptible search routine. Often engines used [coroutines](https://en.wikipedia.org/wiki/Coroutine) to implement internal [context switching](https://en.wikipedia.org/wiki/Context_switch) between search and user interaction. Today, it is more common to rely on [multithreading](https://en.wikipedia.org/wiki/Multi-threading) abilities of recent operating systems, and to use an explicit [I/O-thread](Thread "Thread"), while the search routine is regularly pondering whether it needs to be interrupted by pending input received by another thread, with the option to asynchronous stop the search.



### Event driven GUIs


*see main article [Graphical User Interface](GUI "GUI")*.


With the advent of operating systems with [graphical user interfaces](https://en.wikipedia.org/wiki/Graphical_user_interface), also encouraged by additional input devices such as a [computer mouse](https://en.wikipedia.org/wiki/Mouse_%28computing%29) for asynchronous user interaction, the embedding of a chess engine with a classical CLI inside the [event-driven architecture](https://en.wikipedia.org/wiki/Event-driven_architecture) of a graphical user interface became more difficult. Today, most programmers rely on an external event driven [graphical user interface](GUI "GUI") applications using [standard streams](https://en.wikipedia.org/wiki/Standard_streams) or [pipelines](https://en.wikipedia.org/wiki/Pipeline_%28Unix%29) to communicate with the GUI via [protocols](Protocols "Protocols") such as the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and the [Universal Chess Interface](UCI "UCI"). The external GUI application constitutes the MVC view and controller, and more or less even parts of a (redundant) game model (or even multi-game model), to make the GUI aware of its own game states to even make decisions on behalf of the engine, such as move selection from opening books and [endgame tablebases](Endgame_Tablebases "Endgame Tablebases"), draw claims and offers and to finally declare the game over. These game interacting features of the external GUI application in conjunction with certain protocols such as UCI by far exceeds what a pure chess user interface was initially designed for - controller and view only, enter legal moves and render the state of the game, which has become disputed issue in playing official [tournament](Tournaments_and_Matches "Tournaments and Matches") games.



## UI Topics


* [Command Line Interface](CLI "CLI")
* [Graphics Programming](Graphics_Programming "Graphics Programming")
* [Entering Moves](Entering_Moves "Entering Moves")
* [Graphical User Interface](GUI "GUI")
* [Piece Recognition](Piece_Recognition "Piece Recognition")
* [Sensory Board](Sensory_Board "Sensory Board")
* [Voice User Interface](index.php?title=Voice_User_Interface&action=edit&redlink=1 "Voice User Interface (page does not exist)")


## See also


* [Chess Game](Chess_Game "Chess Game")
* [Dedicated Chess Computers](Dedicated_Chess_Computers "Dedicated Chess Computers")
* [Game Notation](Game_Notation "Game Notation")
* [Protocols](Protocols "Protocols")
* [Robots](Robots "Robots")
* [Square Off](index.php?title=Square_Off&action=edit&redlink=1 "Square Off (page does not exist)")


## Publications


* [Judith S. Reitman Olson](index.php?title=Judith_Spencer_Olson&action=edit&redlink=1 "Judith Spencer Olson (page does not exist)"), [William B. Whitten II](http://fordhamgraded.blogspot.de/2011/03/faculty-profiles-dr-william-b-whitten.html), [Thomas M. Gruenenfelder](http://www.pubfacts.com/author/Thomas+M+Gruenenfelder) (**1984**). *[A general User-Interface for Creating and Displaying Tree-structures, Hierarchies, Decision Trees, and Nested Menus](http://dl.acm.org/citation.cfm?id=2105)*. in [Yannis Vassiliou](http://www.ece.ntua.gr/en/people/faculty?view=profile&id=3) (ed.) *Human Factors and Interactive Computer Systems*. [Ablex Publishing](https://en.wikipedia.org/wiki/Ablex_Publishing)
* [Nick Cercone](http://arnetminer.org/viewperson.do?naid=10306), [Paul McFetridge](http://www.sfu.ca/linguistics/people/faculty/mcfetridge.html), [Jiawei Han](http://www.cs.uiuc.edu/homes/hanj/), [Fred Popowich](Fred_Popowich "Fred Popowich") (**1993**). *Human-Computer Interfaces: DBLEARN and System X*. RSKD 1993: 32-43
* [James R. Slagle](James_R._Slagle "James R. Slagle"), [Zbigniew Wieckowski](http://wiki.tcl.tk/13) a.k.a. Bishak (**1994**). *[Ideas for Intelligent User Interface Design](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.48.2996)*.
* [Susan E. McDaniel](http://www.informatik.uni-trier.de/~ley/pers/hd/m/McDaniel:Susan_E=.html), [Gary M. Olson](http://www.ics.uci.edu/~golson/), [Judith S. Olson](index.php?title=Judith_Spencer_Olson&action=edit&redlink=1 "Judith Spencer Olson (page does not exist)") (**1994**). *Methods in Search of Methodology - combining HCI and Object Orientation*. [CHI 1994](http://www.informatik.uni-trier.de/~ley/db/conf/chi/chi1994.html#McDanielOO94a), [pdf](http://www.ics.uci.edu/~jsolson/publications/Design/McDaniel%20Methods.pdf) <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a>
* [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**2001**). *How the Computer-Chess Methods Help to Build Better User Interfaces.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
* [David Urting](http://be.linkedin.com/pub/david-urting/4/82b/448), [Yolande Berbers](http://distrinet.cs.kuleuven.be/people/showMember.do?memberID=u0006685) (**2003**). *[MarineBlue: A Low-Cost Chess Robot](https://lirias.kuleuven.be/handle/123456789/132621?mode=full&submit_simple=Show+full+item+record)*. [Katholieke Universiteit Leuven](https://en.wikipedia.org/wiki/Katholieke_Universiteit_Leuven), [RA 2003](http://dblp.uni-trier.de/db/conf/ra/ra2003.html#UrtingB03). [pdf](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=CE76646F8F250AB5DAA36951D4D28335?doi=10.1.1.83.6961&rep=rep1&type=pdf)
* [Chua Huiyan](http://de.scientificcommons.org/huiyan_chua), Le Vinh, [Wong Lai Kuan](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/k/Kuan:Wong_Lai.html) (**2007**). *Chess Vision*. [School of Computing](https://en.wikipedia.org/wiki/NUS_School_of_Computing), [National University of Singapore](https://en.wikipedia.org/wiki/National_University_of_Singapore), [slides as pdf](http://www.comp.nus.edu.sg/%7Ecs4243/showcase/chess_vision/Chess-Vision-Presentation.pdf)


## Forum Posts


* [Voice synthesis, part 1](http://www.talkchess.com/forum/viewtopic.php?t=38584) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 29, 2011
* [Engines with interfaces for slightly nerdish people](http://www.talkchess.com/forum/viewtopic.php?t=59367) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), February 26, 2016


## External Links


* [User interface from Wikipedia](https://en.wikipedia.org/wiki/User_interface)
* [User interface design from Wikipedia](https://en.wikipedia.org/wiki/User_interface_design)
* [Brain–computer interface from Wikipedia](https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface)
* [Command-line interface from Wikipedia](https://en.wikipedia.org/wiki/Command-line_interface) » [Command Line Interface](CLI "CLI")
* [Graphical user interface from Wikipedia](https://en.wikipedia.org/wiki/Graphical_user_interface) » [Graphical User Interface](GUI "GUI")
* [History of the graphical user interface from Wikipedia](https://en.wikipedia.org/wiki/History_of_the_graphical_user_interface)
* [Human-computer interaction from Wikipedia](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction)
* [Intelligent user interface from Wikipedia](https://en.wikipedia.org/wiki/Intelligent_user_interface)
* [Kinetic user interface from Wikipedia](https://en.wikipedia.org/wiki/Kinetic_user_interface)
* [Natural user interface from Wikipedia](https://en.wikipedia.org/wiki/Natural_user_interface)
* [Object-oriented user interface -Wikipedia](https://en.wikipedia.org/wiki/Object-oriented_user_interface)
* [Tangible User Interface from Wikipedia](https://en.wikipedia.org/wiki/Tangible_User_Interface)
* [Voice user interface from Wikipedia](https://en.wikipedia.org/wiki/Voice_user_interface)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Copper engraving from the book: [Freiherr Joseph Friedrich zu Racknitz](https://en.wikipedia.org/wiki/Joseph_Friedrich_Freiherr_von_Racknitz), *Ueber den Schachspieler des [Herrn von Kempelen](https://en.wikipedia.org/wiki/Wolfgang_von_Kempelen)*, [Leipzig](https://en.wikipedia.org/wiki/Leipzig) und [Dresden](https://en.wikipedia.org/wiki/Dresden) 1789
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [The Turk from Wikipedia](https://en.wikipedia.org/wiki/The_Turk)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Wolfgang von Kempelen from Wikipedia](https://en.wikipedia.org/wiki/Wolfgang_von_Kempelen)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Johann Nepomuk Maelzel from Wikipedia](https://en.wikipedia.org/wiki/Johann_Nepomuk_Maelzel)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Maelzel's Chess Player from Wikipedia](https://en.wikipedia.org/wiki/Maelzel%27s_Chess_Player)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [ACM SIGCHI Curricula for Human-Computer Interaction](http://old.sigchi.org/cdg/)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Chua Huiyan](http://de.scientificcommons.org/huiyan_chua), Le Vinh, [Wong Lai Kuan](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/k/Kuan:Wong_Lai.html) (**2007**). *Chess Vision*. [School of Computing](https://en.wikipedia.org/wiki/NUS_School_of_Computing), [National University of Singapore](https://en.wikipedia.org/wiki/National_University_of_Singapore), [slides as pdf](http://www.comp.nus.edu.sg/~cs4243/showcase/chess_vision/Chess-Vision-Presentation.pdf)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [TELETYPE CORPORATION - Teletype Model 28 Page Printer (1)](http://hans.presto.tripod.com/scan/teletype/28_01.html)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Human–computer interaction - Wikipedia](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Object-oriented user interface -Wikipedia](https://en.wikipedia.org/wiki/Object-oriented_user_interface)

**[Up one Level](Home "Home")**







 
