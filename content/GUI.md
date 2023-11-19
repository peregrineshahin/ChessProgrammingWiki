---
title: GUI
---
**[Home](Home "Home") * [User Interface](User_Interface "User Interface") * Graphical User Interface**

[](File:Machackdisplay02.jpg) Mac Hack [display](Lawrence_J._Krakauer#DEC340 "Lawrence J. Krakauer") <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>
**Graphical User Interface** (GUI),

a user interface where [interaction](https://en.wikipedia.org/wiki/Interaction) between user and a (chess) program takes place. Opposed to the sequential nature of a pure text based [command-line interface](CLI "CLI"), where a program prints its output and prompts for input, a [graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface) allows a more sophisticated, graphical presentation of the programs output, as well within its [event-driven architecture](https://en.wikipedia.org/wiki/Event-driven_architecture) a more flexible user interaction not only by typing text commands, but using a [pointingdevice](https://en.wikipedia.org/wiki/Pointing_device), a [mouse](https://en.wikipedia.org/wiki/Mouse_%28computing%29) or a pen or finger pointing on and touching a [graphics tablet](https://en.wikipedia.org/wiki/Graphics_tablet) with its [touchscreen](https://en.wikipedia.org/wiki/Touchscreen), for random and [direct manipulation](https://en.wikipedia.org/wiki/Direct_manipulation) of graphical elements. A GUI dedicated to play chess typically has a graphical [board](Chessboard "Chessboard") and [game](Chess_Game "Chess Game") representation, where the user may [enter moves](Entering_Moves "Entering Moves") by [clicking](https://en.wikipedia.org/wiki/Point-and-click) and [dragging](https://en.wikipedia.org/wiki/Drag-and-drop) a piece, quite similar to moving a piece on a "real" chess board.

## Historical Chess GUI

[](http://www.flickr.com/photos/10261668@N05/sets/72157600922175252/)
[Chris Daly](Chris_Daly "Chris Daly") interacting with [Daly CP](Daly_CP "Daly CP"), 1970 <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> on an [IDIIOM](Kenneth_L._King#IDIIOM "Kenneth L. King") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

## Playing Chess

The sequential nature of the [game of chess](Chess_Game "Chess Game"), along with the both fundamental states of a chess engine while playing a game, that is calculating a move and [pondering](Pondering "Pondering"), should be appropriately indicated by the GUI, for instance to allow the interaction of entering moves only for the opponent side while pondering. There may be other modes than pure game playing, for instance to replay and analyze a game, allowing the user to click and drag the moves of the [game notation](Game_Notation "Game Notation") [move list](Move_List "Move List"), which needs appropriate indication and ergonomic control.

## MVC

The chess program and its [user interface](User_Interface "User Interface") can be interpreted as a [Model–view–controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (MVC), an [architectural pattern](https://en.wikipedia.org/wiki/Architectural_pattern_%28computer_science%29) that isolates [business logic](https://en.wikipedia.org/wiki/Business_logic) f.i. game administration, [time management](Time_Management "Time Management") and searching a move inside a chess program from input and presentation. The game model represents the domain-specific [data](Data "Data") on which the application operates - Inside a chess program, the information about the [initial position](Initial_Position "Initial Position") and the game record to reproduce the current positions, likely subject of [search](Search "Search") or [pondering](Pondering "Pondering") during game play. The model and controller implement a [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) which controls the game, its [states](https://en.wikipedia.org/wiki/State_%28computer_science%29), state transitions and actions considering various [modes](https://en.wikipedia.org/wiki/Mode_%28computer_interface%29). The view displays the [game notation](Game_Notation "Game Notation"), a [list of moves](Move_List "Move List"), and likely the board with the current [position](Chess_Position "Chess Position"), suitable for [interaction](https://en.wikipedia.org/wiki/Interaction) inside a [user interface](User_Interface "User Interface"). The controller receives input from various sources and devices, such as [keyboard](https://en.wikipedia.org/wiki/Keyboard_%28computing%29), [mouse](https://en.wikipedia.org/wiki/Mouse_%28computing%29), [serial port](https://en.wikipedia.org/wiki/Serial_port) and [internet socket](https://en.wikipedia.org/wiki/Internet_socket), and initiates a response by making calls on model objects.

## Chess GUI Issues

Today, most programmers rely on external event driven GUI applications using [standard streams](https://en.wikipedia.org/wiki/Standard_streams) or [pipelines](https://en.wikipedia.org/wiki/Pipeline_%28Unix%29) to communicate with the GUI via [protocols](Protocols "Protocols") such as the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") or the [Universal Chess Interface](UCI "UCI"). The external GUI application constitutes the [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) view and controller, and more or less even parts of a (redundant) game model (or even multi-game model), to make the GUI aware of its own game states to even make decisions on behalf of the engine, such as move selection from opening books and [endgame tablebases](Endgame_Tablebases "Endgame Tablebases"), draw claims and offers and to finally declare the game over. These game interacting features of the external GUI application in conjunction with certain protocols such as UCI by far exceeds what a pure chess user interface was initially designed for - controller and view only, enter legal moves and render the state of the game. Sharing code of external GUIs, with potential game decisive move selection, time allocation and draw claiming, by multiple engines in official [tournaments](Tournaments_and_Matches "Tournaments and Matches") is a heavily discussed topic <a id="cite-note-7" href="#cite-ref-7">[7]</a> .

## Front End

Beside a pure user versus engine game playing interface, modern general purpose Chess GUIs implement features and modes for multiple engine tournament play, and can be used as [front end](https://en.wikipedia.org/wiki/Front_and_back_ends) for [chess server](Chess_Server "Chess Server") and [chess database](Databases "Databases") back ends.

## Chess GUIs

- [APwin](APwin "APwin")
- [Aquarium](Aquarium "Aquarium")
- [Arena](Arena "Arena")
- [Banksia GUI](Banksia_GUI "Banksia GUI")
- [Banksia GUI for iOS](index.php?title=Banksia_GUI_for_iOS&action=edit&redlink=1 "Banksia GUI for iOS (page does not exist)")
- [Caddell Chess](Caddell_Chess "Caddell Chess")
- [Chess Academy](index.php?title=Chess_Academy&action=edit&redlink=1 "Chess Academy (page does not exist)")
- [Chess Assistant](Chess_Assistant "Chess Assistant")
- [Chess for Android](Chess_for_Android "Chess for Android")
- [Chess for Glass](Chess_for_Glass "Chess for Glass")
- [ChessBase (Database)](</ChessBase_(Database)> "ChessBase (Database)")
- [ChessGUI](ChessGUI "ChessGUI")
- [Chess King](index.php?title=Chess_King&action=edit&redlink=1 "Chess King (page does not exist)")
- [ChessPartner GUI](ChessPartner "ChessPartner")
- [Chess Wizard](</index.php?title=Chess_Wizard_(GUI)&action=edit&redlink=1> "Chess Wizard (GUI) (page does not exist)")
- [ChessX](ChessX "ChessX")
- [Cute Chess](Cute_Chess "Cute Chess")
- [DreamChess](DreamChess "DreamChess")
- [DroidFish](DroidFish "DroidFish")
- [EBoard](index.php?title=EBoard&action=edit&redlink=1 "EBoard (page does not exist)")
- [EchoBoard](index.php?title=EchoBoard&action=edit&redlink=1 "EchoBoard (page does not exist)")
- [Fancy](index.php?title=Fancy&action=edit&redlink=1 "Fancy (page does not exist)")
- [Fritz GUI](Fritz#FritzGUI "Fritz")
- [Gavon](Gavon "Gavon")
- [Glaurung GUI](Glaurung#GUI "Glaurung")
- [glChess](index.php?title=GlChess&action=edit&redlink=1 "GlChess (page does not exist)")
- [GNOME Chess](index.php?title=GNOME_Chess&action=edit&redlink=1 "GNOME Chess (page does not exist)")
- [HIARCS Chess Explorer](HIARCS_Chess_Explorer "HIARCS Chess Explorer")
- [Jerry](Jerry "Jerry")
- [jose](index.php?title=Jose&action=edit&redlink=1 "Jose (page does not exist)")
- [Kvetka](Kvetka "Kvetka")
- [LittleBlitzer](LittleBlitzer "LittleBlitzer")
- [Lucas Chess](Lucas_Chess "Lucas Chess")
- [Mayura Chess Board](index.php?title=Mayura_Chess_Board&action=edit&redlink=1 "Mayura Chess Board (page does not exist)")
- [Millennium Chess System](Millennium_Chess_System "Millennium Chess System")
- [PyChess](PyChess "PyChess")
- [Python Easy Chess GUI](index.php?title=Python_Easy_Chess_GUI&action=edit&redlink=1 "Python Easy Chess GUI (page does not exist)")
- [SCID](SCID "SCID")
- [Scid vs. PC](Scid_vs._PC "Scid vs. PC")
- [Shredder GUI](Shredder#GUI "Shredder")
- [Tarrasch](Tarrasch "Tarrasch")
- [Uragano](Uragano "Uragano")
- [WinBoard](WinBoard "WinBoard")
- [XBoard](XBoard "XBoard")

## GUI Shots

|  |  |
| --- | --- |
| [Arena320.jpg](http://www.playwitharena.com/) | [CPsshot2.png](http://sjeng.org/deepsjeng.html) |
| [Arena](Arena "Arena") under [Windows](Windows "Windows") <a id="cite-note-8" href="#cite-ref-8">[8]</a> | [ChessPartner](ChessPartner "ChessPartner") under [Windows](Windows "Windows") running [Deep Sjeng](Deep_Sjeng "Deep Sjeng") <a id="cite-note-9" href="#cite-ref-9">[9]</a> |

## GUI Elements

A GUI consists of multiple [elements](https://en.wikipedia.org/wiki/Graphical_user_interface_elements) or [widgets](https://en.wikipedia.org/wiki/GUI_widget), based on a visual rectangular area called [window](https://en.wikipedia.org/wiki/Window_%28computing%29). Windows have [recursive](Recursion "Recursion") hierarchical relationships, that is a window may contain several child windows, which are usually restricted and clipped to the area of the parent window. The [desktop metaphor](https://en.wikipedia.org/wiki/Desktop_metaphor) as root, and all child and grand child windows of one or more applications can be interpreted as a tree structure, traversed in a [depth-first](Depth-First "Depth-First") manner if looking up graphical coordinates or visible areas, as already mentioned by [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") at the [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9") conference in 1999 <a id="cite-note-10" href="#cite-ref-10">[10]</a> .

A GUI application usually has one main- or frame-window, often sizable and movable, and child of the desktop. The main window further contains various standard child windows at its top and bottom areas, a caption bar, often configurable and dockable [menu](https://en.wikipedia.org/wiki/Menu_bar)-, and/or [toolbars](https://en.wikipedia.org/wiki/Toolbar), and [status bar](https://en.wikipedia.org/wiki/Status_bar). The [look and feel](https://en.wikipedia.org/wiki/Look_and_feel) depends on the [operating system](https://en.wikipedia.org/wiki/Operating_system) and its [window manager](https://en.wikipedia.org/wiki/Window_manager), there are quite common techniques and standardizations, also encouraged by cross platform [widget toolkits](https://en.wikipedia.org/wiki/Widget_toolkit).

## Main Window

Beside its default child windows of the frame, the inner area also referred as [workspace](https://en.wikipedia.org/wiki/Workspace), may contain one or more so called document windows, to reduce clutter and make the desktop easier to navigate with multiple applications. A main window applies either a [single](https://en.wikipedia.org/wiki/Single_document_interface) (SDI), a [multiple](https://en.wikipedia.org/wiki/Multiple_document_interface) (MDI) or a [tabbed document interface](https://en.wikipedia.org/wiki/Tab_%28GUI%29) (TDI). Further modeless and often [tabbed](https://en.wikipedia.org/wiki/Tab_%28GUI%29) tool-, output log or miscellaneous windows for various purposes may share the workspace or may be docked on the borders or various areas of the mainframe, also called an [IDE-style interface](https://en.wikipedia.org/wiki/Integrated_development_environment).

## Dialog Windows

Another class of windows, [dialog boxes](https://en.wikipedia.org/wiki/Dialog_box) apply [modal](https://en.wikipedia.org/wiki/Modal_window) [transactions](https://en.wikipedia.org/wiki/Transaction) like saving a document to a file. They contain all kinds of child widgets to enter data, and most often [buttons](https://en.wikipedia.org/wiki/Button_%28computing%29) to confirm (OK) or cancel the transaction. There are further [tabbed](https://en.wikipedia.org/wiki/Tab_%28GUI%29) dialogs and multi-page wizard or assistants with next, previous and finish buttons to guide users through a sequence of transactions which are dependent on each other or partly optional.

## Chess GUI Elements

A document or model usually refers to a [game of chess](Chess_Game "Chess Game") and its [game notation](Game_Notation "Game Notation") as [move-list](Move_List "Move List"), whether still in progress or loaded from a [database](Databases "Databases").

## Game Window

A game window, associated with the game document or model, is usually a frame around a board- and notation window, which represent two views of the same model.

## Board Window

A pure [2D board](2D_Graphics_Board "2D Graphics Board") window should be [isotropic](https://en.wikipedia.org/wiki/Isotropy) and quadratic. If the board window has keyboard [focus](https://en.wikipedia.org/wiki/Focus_%28computing%29), one may control a square [cursor](https://en.wikipedia.org/wiki/Cursor_%28computers%29) to select two squares to make a move, similar to clicking with the mouse.

- [2D Graphics Board](2D_Graphics_Board "2D Graphics Board")
- [3D Graphics Board](3D_Graphics_Board "3D Graphics Board")

## Notation Window

The notation window represents the [game notation](Game_Notation "Game Notation") or score-sheet of the chess game, the [list of moves](Move_List "Move List") of the game. It works like a multiple line [text box](https://en.wikipedia.org/wiki/Text_box) or multiple column [grid view](https://en.wikipedia.org/wiki/Grid_view) or [list box](https://en.wikipedia.org/wiki/List_box) often scrollable and indicated by a vertical [scrollbar](https://en.wikipedia.org/wiki/Scrollbar). A [cursor](https://en.wikipedia.org/wiki/Cursor_%28computers%29) inside the notation window might be associated with a [half-move index](Ply "Ply") in the range from zero (before first half-move played, [initial position](Initial_Position "Initial Position")), to N (after last half-move played, current game position), and determines the position displayed in the board window. If the game window has keyboard [focus](https://en.wikipedia.org/wiki/Focus_%28computing%29), it receives input of moves via move coordinates or [algebraic notation](Algebraic_Chess_Notation "Algebraic Chess Notation").

## Information Windows

Information windows are associated with an engine actually playing or analyzing a game. It displays [search](Search "Search") information like [principal variations](Principal_Variation "Principal Variation") and associated [scores](Score "Score"), times and that like. It is often implemented as scrollable logging window, always appending text at top or bottom lines.

## Mobile GUIs

- [Chess for Android](Chess_for_Android "Chess for Android")
- [Banksia GUI for iOS](index.php?title=Banksia_GUI_for_iOS&action=edit&redlink=1 "Banksia GUI for iOS (page does not exist)")
- [DroidFish](DroidFish "DroidFish")
- [PocketGrandmaster](PocketGrandmaster "PocketGrandmaster")

## Operating Systems

- [Android](Android "Android")
- [Linux](Linux "Linux")
- [iOS](index.php?title=IOS&action=edit&redlink=1 "IOS (page does not exist)")
- [Mac OS](Mac_OS "Mac OS")
- [MS-DOS](MS-DOS "MS-DOS")
- [Windows](Windows "Windows")

## Quotes

[Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") wrote on a [Talkchess](Talkchess "Talkchess") thread <a id="cite-note-11" href="#cite-ref-11">[11]</a>

```C++
Beware that writing a GUI is between 10 and 100 times more work than writing an engine.

```

## See also

- [Chess Game](Chess_Game "Chess Game")
- [Chess Server](Chess_Server "Chess Server")
- [Command Line Interface](CLI "CLI")
- [CPW-Engine_com](CPW-Engine_com "CPW-Engine com")
- [Graphics Programming](Graphics_Programming "Graphics Programming")
- [InBetween](InBetween "InBetween")
- [Protocols](Protocols "Protocols")

## Publications

- [Duane Szafron](Duane_Szafron "Duane Szafron"), Brian Wilkerson (**1986**). *Some Effects of Graphical Interfaces in Programming Environments*. CIPS/ACI Congress 86, [pdf](https://webdocs.cs.ualberta.ca/~duane/publications/pdf/1986cips.pdf)
- [Haiying Wang](index.php?title=Haiying_Wang&action=edit&redlink=1 "Haiying Wang (page does not exist)") (**1994**). *[An application-oriented user interface model and development system](https://era.library.ualberta.ca/files/2227mr67d)*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/files/2227mr67d/NN11407.pdf) » [Abyss](Abyss "Abyss")
- [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**2001**). *How the Computer-Chess Methods Help to Build Better User Interfaces.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
- [Paul Fischer](Paul_Fischer "Paul Fischer") (**2005**). *An Introduction to Graphical User Interfaces with Java Swing*. [Pearson Education](https://en.wikipedia.org/wiki/Pearson_Education), [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley), [Amazon.de](http://www.amazon.de/Introduction-Graphical-User-Interfaces-Swing/dp/0321220706) » [Java](Java "Java")
- [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**2006**). *[Computergrafik](http://www-lehre.inf.uos.de/%7Ecg/2006/skript/skript.html)*. [pdf](http://www-lehre.inf.uos.de/%7Ecg/2006/PDF/skript.pdf) (German)
- [Timo Klaustermeyer](Timo_Haupt "Timo Haupt") (**2006**). *Wandel von Interaktion zwischen Menschen und Maschine am Beispiel des Schachspiels*. Diplom thesis, [Paderborn University](Paderborn_University "Paderborn University"), advisors [Gerd Szwillus](https://dblp.uni-trier.de/pers/hd/s/Szwillus:Gerd) and [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [abstract as pdf](http://www.team-oh.de/files/Abstract%20Diplomarbeit.pdf) (German)

## Forum Posts

## 2000 ...

- [chess GUI under Linux](https://www.stmintz.com/ccc/index.php?id=356135) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), March 23, 2004 » [Linux](Linux "Linux")

## 2005 ...

- [Programming models in graphical chess interfaces](https://www.stmintz.com/ccc/index.php?id=487610) by [Federico Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](CCC "CCC"), February 18, 2006
- [What's the role of the GUI?](http://www.talkchess.com/forum/viewtopic.php?t=21168) by Zlatnik, [CCC](CCC "CCC"), May 15, 2008
- [programming gui questions](http://www.talkchess.com/forum/viewtopic.php?t=21261) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 20, 2008
- [programming engine, programming GUI](http://www.talkchess.com/forum/viewtopic.php?t=25541) by Eric Lang, [CCC](CCC "CCC"), December 20, 2008
- [GUI in Visual Basic](http://www.talkchess.com/forum/viewtopic.php?t=26783) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), February 28, 2009 » [Basic](Basic "Basic")
- [OliThink GUI in Java... Complete source posted](http://www.talkchess.com/forum/viewtopic.php?t=30793) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), November 25, 2009 » [OliThink](OliThink "OliThink"), [Java](Java "Java")

## 2010 ...

- [Which GUI toolkits are best?](http://www.talkchess.com/forum/viewtopic.php?t=31432) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), January 02, 2010
- [A Suggestion for GUI makers. Double-Click a Piece to Capture](http://www.talkchess.com/forum/viewtopic.php?t=32386) by Zagalo Martini, [CCC](CCC "CCC"), February 05, 2010
- [Aquarium (other GUIs too?) and WB support => I am shocked](http://www.talkchess.com/forum/viewtopic.php?t=32952) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), February 27, 2010
- [Which compiler & IDE best for developing chess GUI?](http://talkchess.com/forum3/viewtopic.php?t=36520) by mrerk, [CCC](CCC "CCC"), October 29, 2010
- [It is time to revolutionize chess GUIs](http://talkchess.com/forum3/viewtopic.php?t=38283) by Ponti, [CCC](CCC "CCC"), March 04, 2011
- [New opensource GUI on android for UCI engines](http://www.talkchess.com/forum/viewtopic.php?t=39118) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang"), [CCC](CCC "CCC"), May 19, 2011
- [Suggestion for GUI developers](http://talkchess.com/forum3/viewtopic.php?t=43130) by Jose Carlos, [CCC](CCC "CCC"), April 02, 2012
- [Peer-to-peer GUI adapter](http://www.talkchess.com/forum/viewtopic.php?t=44450) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 15, 2012
- [Help us make Cute Chess GUI better](http://talkchess.com/forum3/viewtopic.php?t=44843) by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), August 20, 2012
- [Problem with UCI engines hash in Arena](http://talkchess.com/forum3/viewtopic.php?t=46586) by carldaman, [CCC](CCC "CCC"), December 27, 2012
- [Most wanted missing features for a chess GUI](http://www.talkchess.com/forum/viewtopic.php?t=50493) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), December 14, 2013
- [To GUI developers and Linux engine packagers](http://www.talkchess.com/forum/viewtopic.php?t=53674) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 12, 2014 » [Linux](Linux "Linux")

## 2015 ...

- [Interfacing with a GUI](http://www.open-chess.org/viewtopic.php?f=5&t=2933) by ppyvabw, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 08, 2015
- [Object model for chess GUI?](http://www.talkchess.com/forum/viewtopic.php?t=58687) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 25, 2015
- [Linux Chess GUI that's good for engine matches/tournaments](http://www.talkchess.com/forum/viewtopic.php?t=60506) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), June 16, 2016 » [Linux](Linux "Linux")
- [Elements of the ULTIMATE Chess GUI?](http://www.talkchess.com/forum/viewtopic.php?t=65485) by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](CCC "CCC"), October 19, 2017
- [Old chess GUIs](http://www.talkchess.com/forum/viewtopic.php?t=66811) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), March 12, 2018
- [Python Easy Chess GUI](https://talkchess.com/forum3/viewtopic.php?t=71048) by Ferdy, [CCC](CCC "CCC"), June 20, 2019
- [Banksia GUI released](http://talkchess.com/forum3/viewtopic.php?f=2&t=72350) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), November 18, 2019

## 2020 ...

- [960 Compliant Chess Guis and engines](http://talkchess.com/forum3/viewtopic.php?t=74286) by kk, [CCC](CCC "CCC"), June 26, 2020
- ["New" Engines (lc0, MCTS, SFNNUE) and suitable GUIs](http://talkchess.com/forum3/viewtopic.php?t=74891) by Hamster, [CCC](CCC "CCC"), August 25, 2020
- [Web based GUI for UCI chess engine: YouTube series](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75352) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 10, 2020 » [Web GUI Tutorial](#Tutorial)
- [UCI Gui to remote Linux Engine](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75992) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), December 05, 2020 » [UCI](UCI "UCI"), [Linux](Linux "Linux")
- [GUI for easy engine - engine outplay positions](https://talkchess.com/forum3/viewtopic.php?t=76137) by Matthias Richter, [CCC](CCC "CCC"), December 24, 2020
- [Listening for GUI input when searching](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77189) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 27, 2021 » [Search](Search "Search"), [Thread](Thread "Thread"), [UCI](UCI "UCI")

## External Links

## General

- [Graphical user interface from Wikipedia](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [Graphical desktop environment from Wikipedia](https://en.wikipedia.org/wiki/Desktop_environment)
- [Graphical user interface elements from Wikipedia](https://en.wikipedia.org/wiki/Elements_of_graphical_user_interfaces)
- [History of the graphical user interface from Wikipedia](https://en.wikipedia.org/wiki/History_of_the_graphical_user_interface)
- [Style guide from Wikipedia](https://en.wikipedia.org/wiki/Style_guide)
- [IBM Common User Access from Wikipedia](https://en.wikipedia.org/wiki/IBM_Common_User_Access)
- [X Window System from Wikipedia](https://en.wikipedia.org/wiki/X_Window_System)
- [X window manager from Wikipedia](https://en.wikipedia.org/wiki/X_window_manager)
- [GNOME from Wikipedia](https://en.wikipedia.org/wiki/GNOME)
- [KDE from Wikipedia](https://en.wikipedia.org/wiki/KDE)

## Computer Chess

- [Graphical User Interfaces for Computer Chess](http://adamsccpages.blogspot.de/p/graphical-user-interfaces-for-computer.html) by [Adam Hair](Adam_Hair "Adam Hair")
- [GUI Protocol List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:gui_protocol_support_list) from [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home) by [Ron Murawski](Ron_Murawski "Ron Murawski")
- [Septober - Computerschach](http://www.septober.de/chess/index.htm) by [Herbert Marquardt](index.php?title=Herbert_Marquardt&action=edit&redlink=1 "Herbert Marquardt (page does not exist)") (program list with screenshots)

## Web Development

- [Ajax from Wikipedia](https://en.wikipedia.org/wiki/Ajax_%28programming%29)
- [Rich Internet application from Wikipedia](https://en.wikipedia.org/wiki/Rich_Internet_application)
- [Rich AJAX Platform from Wikipedia](https://en.wikipedia.org/wiki/Rich_AJAX_Platform)
- [Rich client platform from Wikipedia](https://en.wikipedia.org/wiki/Rich_client_platform)
- [chessboard3.js](http://jtiscione.github.io/chessboard3js/play.html) [JavaScript](JavaScript "JavaScript") GUI by [Jason Tiscione](index.php?title=Jason_Tiscione&action=edit&redlink=1 "Jason Tiscione (page does not exist)")

## Tutorial

- [Web based GUI for UCI chess engine](https://www.youtube.com/watch?v=_0uKZbHWVKM&list=PLmN0neTso3Jz-6--Mj51Hc3jiLhkQm0DB) [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos by [Maksim Korzh](Maksim_Korzh "Maksim Korzh") » [BBC GUI](BBC#GUI "BBC") <a id="cite-note-12" href="#cite-ref-12">[12]</a>

## Toolkits, Libraries and API

- [DirectX from Wikipedia](https://en.wikipedia.org/wiki/DirectX) » [Windows](Windows "Windows")

[Direct2D from Wikipedia](https://en.wikipedia.org/wiki/Direct2D)
[Direct3D from Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Direct3D)
[DirectDraw from Wikipedia](https://en.wikipedia.org/wiki/DirectDraw)
[DirectDraw Surface from Wikipedia](https://en.wikipedia.org/wiki/DirectDraw_Surface)

- [Fast Light Tool Kit (FLTK) from Wikipedia](https://en.wikipedia.org/wiki/FLTK)
- [GDK](https://en.wikipedia.org/wiki/GDK) / [XLib from Wikipedia](https://en.wikipedia.org/wiki/Xlib) » [Unix](Unix "Unix"), [Linux](Linux "Linux")
- [Graphics Device Interface from Wikipedia](https://en.wikipedia.org/wiki/Graphics_Device_Interface) (GDI) » [Windows](Windows "Windows")

[CDC Class - Device Context](http://msdn.microsoft.com/de-de/library/fxhhde73%28v=VS.100%29.aspx), [Microsoft Foundation Class Library](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library), [MSDN](https://en.wikipedia.org/wiki/Microsoft_Developer_Network)

- [GTK+ (GIMP Toolkit) from Wikipedia](https://en.wikipedia.org/wiki/GTK%2B)

[gtkmm from Wikipedia](https://en.wikipedia.org/wiki/Gtkmm)
[Gtk Sharp from Wikipedia](https://en.wikipedia.org/wiki/Gtk_Sharp)

- [Google Web Toolkit (GWT) from Wikipedia](https://en.wikipedia.org/wiki/Google_Web_Toolkit)

[lib-gwt-svg « vectomatic](http://www.vectomatic.org/libs/lib-gwt-svg)
[vectomatic - standard dynamic 2D graphics in web browsers - Google Project Hosting](https://code.google.com/p/vectomatic/)

- [List of widget toolkits from Wikipedia](https://en.wikipedia.org/wiki/List_of_widget_toolkits)
- [Motif (widget toolkit) from Wikipedia](https://en.wikipedia.org/wiki/Motif_%28widget_toolkit%29)
- [OpenGL from Wikipedia](https://en.wikipedia.org/wiki/OpenGL)

[Graphics Programming - Introduction to OpenGL](http://graphics.usc.edu/~suyay/class/Programming.pdf) (pdf)
[Comparison of OpenGL and Direct3D from Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_OpenGL_and_Direct3D)

- [Quartz from Wikipedia](https://en.wikipedia.org/wiki/Quartz_%28graphics_layer%29) » [OS X](Mac_OS "Mac OS")
- [QuickDraw from Wikipedia](https://en.wikipedia.org/wiki/QuickDraw) » [OS X](Mac_OS "Mac OS")
- [QT toolkit from Wikipedia](https://en.wikipedia.org/wiki/Qt_%28toolkit%29)
- [S3 Texture Compression from Wikipedia](https://en.wikipedia.org/wiki/S3_Texture_Compression)
- [Scalable Vector Graphics from Wikipedia](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)
- [Standard Widget Toolkit from Wikipedia](https://en.wikipedia.org/wiki/Standard_Widget_Toolkit) » [Java](Java "Java")
- [Swing from Wikipedia](https://en.wikipedia.org/wiki/Swing_%28Java%29) » [Java](Java "Java")
- [Texture compression from Wikipedia](https://en.wikipedia.org/wiki/Texture_compression)
- [Tk (framework) from Wikipedia](https://en.wikipedia.org/wiki/Tk_%28framework%29)
- [Vector Graphics from Wikipedia](https://en.wikipedia.org/wiki/Vector_graphics)
- [Visual Component Library (VCL) from Wikipedia](https://en.wikipedia.org/wiki/Visual_Component_Library)
- [Widget toolkit from Wikipedia](https://en.wikipedia.org/wiki/Widget_toolkit)
- [wxWidgets from Wikipedia](https://en.wikipedia.org/wiki/WxWidgets)
- [X Window System (X11) from Wikipedia](https://en.wikipedia.org/wiki/X_Window_System) » [Unix](Unix "Unix"), [Linux](Linux "Linux")

## [X11.app (XQuartz) from Wikipedia](https://en.wikipedia.org/wiki/X11.app) » [OS X](Mac_OS "Mac OS") References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [I resign](http://ljkrakauer.com/LJK/60s/resign.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chess stories](http://ljkrakauer.com/LJK/60s/chess1.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> see also [63-chess.mp4](http://projects.csail.mit.edu/video/history/aifilms/63-chess.mp4) hosted by [MIT CSAIL](https://www.csail.mit.edu/)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> Picture dated November 14, 1970, [Chess in Space - NASA 1970 First Chess Experiments](https://sites.google.com/site/caroluschess/modern-history/chess-in-space) from [Carolus Chess](https://sites.google.com/site/caroluschess/home)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [14.Unique Computers: Flickr](http://www.flickr.com/photos/10261668@N05/sets/72157600922175252/) by [Chewbanta](Steve_Blincoe "Steve Blincoe")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Don Bissell](http://dl.acm.org/author_page.cfm?id=81100488426&coll=DL&dl=ACM&trk=0&cfid=94733554&cftoken=96327999) (**1998**). *[Was the IDIIOM the First Stand-Alone CAD Platform?](http://www.computer.org/portal/web/csdl/doi/10.1109/85.667292)* [IEEE Annals of the History of Computing](https://en.wikipedia.org/wiki/IEEE_Annals_of_the_History_of_Computing), Vol. 20, No. 2
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [What's the role of the GUI?](http://www.talkchess.com/forum/viewtopic.php?t=21168) by Zlatnik, [CCC](CCC "CCC"), May 15, 2008
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Free chess graphical user interface (GUI) Arena for chess engines](http://www.playwitharena.com/)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Sjeng - chess, audio and misc. software](http://sjeng.org/deepsjeng.html)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**2001**). *How the Computer-Chess Methods Help to Build Better User Interfaces.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Re: Object model for chess GUI?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=58687&hilit=winboard#p653469) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 26, 2015 » [Protocols](Protocols "Protocols")
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Web based GUI for UCI chess engine: YouTube series](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75352) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 10, 2020

**[Up one Level](User_Interface "User Interface")**

