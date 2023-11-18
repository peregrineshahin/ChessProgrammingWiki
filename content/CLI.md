---
title: CLI
---
**[Home](Home "Home") * [User Interface](User_Interface "User Interface") * Command Line Interface**

**Command Line Interface (CLI)**,

a means of a [user](https://en.wikipedia.org/wiki/User_%28computing%29), [agent](https://en.wikipedia.org/wiki/User_agent) or [client](https://en.wikipedia.org/wiki/Client_%28computing%29), [interacting](https://en.wikipedia.org/wiki/Interaction) with a [computer program](index.php?title=Program&action=edit&redlink=1 "Program (page does not exist)") in form of [plain text-](https://en.wikipedia.org/wiki/Plain_text) or command lines. Programs are either the [operating system](https://en.wikipedia.org/wiki/Operating_system), their [command-line shells](https://en.wikipedia.org/wiki/Operating_system_shell#Command-line_OS_shells), or [application software](https://en.wikipedia.org/wiki/Application_software), for instance chess programs.

## History

The CLI has its origins in [teletype](https://en.wikipedia.org/wiki/Teleprinter) and later [computer terminals](https://en.wikipedia.org/wiki/Computer_terminal) to act as a [system console](https://en.wikipedia.org/wiki/System_console) and sequential [input-](https://en.wikipedia.org/wiki/Input_device) and [output device](https://en.wikipedia.org/wiki/Output_device), where the program [prompts](http://en.wiktionary.org/wiki/prompt) for input, that is, prints a message or symbol on the teletype printer to indicate readiness for user input, and acts upon command lines as they are entered.

## Unix Philosophy

[Unix](Unix "Unix") and its [composable design](https://en.wikipedia.org/wiki/Composability) and [philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) originated by [Ken Thompson](Ken_Thompson "Ken Thompson") was summarized by [Doug McIlroy](https://en.wikipedia.org/wiki/Douglas_McIlroy), contributor to [Unix pipes](https://en.wikipedia.org/wiki/Pipeline_%28Unix%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a>: *Write programs that do one thing and do it well. Write programs to work together. Write programs to handle [text streams](https://en.wikipedia.org/wiki/Standard_streams), because that is a universal interface*.

## Shell and Applications

[Operating systems](https://en.wikipedia.org/wiki/Operating_system) such as [MS-DOS](MS-DOS "MS-DOS"), [Unix](Unix "Unix") or [Linux](Linux "Linux") per default provide a [shell](https://en.wikipedia.org/wiki/Shell_%28computing%29) as CLI, such as [Command.com](https://en.wikipedia.org/wiki/COMMAND.COM) or [Unix shell](https://en.wikipedia.org/wiki/Unix_shell). Modern desktop versions of [Windows](Windows "Windows") use the [Windows shell](https://en.wikipedia.org/wiki/Windows_shell) which is a [graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface), but include a [command prompt window](https://en.wikipedia.org/wiki/Command_Prompt) for [console applications](https://en.wikipedia.org/wiki/Console_application). Most operating systems support [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) with [standard streams](https://en.wikipedia.org/wiki/Standard_streams) or [named pipes](https://en.wikipedia.org/wiki/Named_pipe) and are able to [redirect](https://en.wikipedia.org/wiki/Redirection_%28computing%29) standard streams from and to other [processes](Process "Process"). Command line interfaces are therefor often preferred by advanced users or software developers, as they provide a more concise and powerful way to control a program or operating system, and are generally easier to automate via [scripting](https://en.wikipedia.org/wiki/Scripting_language) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Commands

Text commands as entered via the [keyboard](https://en.wikipedia.org/wiki/Computer_keyboard), are a sequence of [ASCII](https://en.wikipedia.org/wiki/ASCII)- or [Unicode](https://en.wikipedia.org/wiki/Unicode) characters finally confirmed and send to the programs standard input by typing the [Enter key](https://en.wikipedia.org/wiki/Enter_key), which is typically encoded at the end of the command string as [newline](https://en.wikipedia.org/wiki/Newline) character ("\\n") (Posix) or a sequence of [carriage return](https://en.wikipedia.org/wiki/Carriage_return) ("\\r") and newline under [Windows](Windows "Windows") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. [Syntax](https://en.wikipedia.org/wiki/Syntax) and [semantics](https://en.wikipedia.org/wiki/Semantics) of commands and their required or optional [arguments](https://en.wikipedia.org/wiki/Command-line_argument#Arguments) depend on the OS or application of course, its state or [mode](https://en.wikipedia.org/wiki/Game_mechanics#Game_modes). When the command is [parsed](https://en.wikipedia.org/wiki/Parsing), [interpreted](https://en.wikipedia.org/wiki/Interpreter_%28computing%29) and [executed](https://en.wikipedia.org/wiki/Execution_%28computing%29), [acknowledgments](https://en.wikipedia.org/wiki/Acknowledgement_%28data_networks%29), results or answers are send back for a communication according to a [protocol](https://en.wikipedia.org/wiki/Communications_protocol).

## CLI and Chess Engines

Most current chess engines are implemented as [console application](https://en.wikipedia.org/wiki/Console_application) to communicate via a command line interface. This is the most [portable](https://en.wikipedia.org/wiki/Software_portability#Source_code_portability) way, supported by all common operating systems, [programming languages](Languages "Languages") and their [standard libraries](https://en.wikipedia.org/wiki/Standard_library). A proprietary chess engine interface for direct console play may be implemented by printing an [ASCII-board](Graphics_Programming#ASCIIDiagrams "Graphics Programming") and the [game record](Game_Notation "Game Notation"), and prompting for a move or command, also streaming the [iterative](Iterative_Deepening "Iterative Deepening") "thinking process", i.e. formatted text lines with [score](Score "Score"), [depth](Depth "Depth"), and [principal variation](Principal_Variation "Principal Variation") to the console.

## Interruptible

[Pondering](Pondering "Pondering") and the need to [enter moves](Entering_Moves "Entering Moves") and commands even if the program is "thinking", requires an interruptible [search](Search "Search") routine. In single tasking operating systems like [MS-DOS](MS-DOS "MS-DOS"), engines often used [coroutines](https://en.wikipedia.org/wiki/Coroutine) to implement internal [context switching](https://en.wikipedia.org/wiki/Context_switch) between search and user interaction. Today, it is more common to rely on [multithreading](https://en.wikipedia.org/wiki/Multi-threading) abilities of modern operating systems, and to use an explicit [I/O-thread](Thread "Thread"), while the search routine is regularly pondering whether it needs to be interrupted by pending input received by another thread, with the option to asynchronously stop the search.

## Protocols

The UNIX paradigm was further archetype of both primary [protocols](Protocols "Protocols") in computer chess, to communicate with a [GUI](GUI "GUI") or game playing controller or server - the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), and [UCI](UCI "UCI"). In conformance with these chess communication protocols, engines [standard streams](https://en.wikipedia.org/wiki/Standard_streams) are redirected and controlled by a parent process such as the [chess GUI](GUI "GUI"), a game- or match controller like [Cutechess-cli](Cutechess-cli "Cutechess-cli") for automatic [engine-engine matches](Engine_Testing#Matches "Engine Testing") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, or their [proxies](https://en.wikipedia.org/wiki/Proxy_server) inside a [computer network](https://en.wikipedia.org/wiki/Computer_network).

## Chess CLIs

- [Cutechess-cli](Cutechess-cli "Cutechess-cli")
- [c-chess-cli](C-chess-cli "C-chess-cli")

## See also

- [ASCII Diagrams](Graphics_Programming#ASCIIDiagrams "Graphics Programming")
- [CHEKMO-II](CHEKMO-II#PDP8 "CHEKMO-II") on a [PDP-8](PDP-8 "PDP-8") (Video)
- [Chess Game](Chess_Game "Chess Game")
- [CPW-Engine_com](CPW-Engine_com "CPW-Engine com")
- [Banksia](Banksia "Banksia")
- [Entering Moves](Entering_Moves "Entering Moves")
- [Graphical User Interface](GUI "GUI")
- [InBetween](InBetween "InBetween")
- [Protocols](Protocols "Protocols")

## Forum Posts

- [Kiwi for Win98 and input-reading stuff](https://www.stmintz.com/ccc/index.php?id=389667) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), September 29, 2004 » [Kiwi](Kiwi "Kiwi"), [Windows](Windows "Windows"), [C++](Cpp "Cpp"), [Thread](Thread "Thread")
- [Safe I/O (repeated)](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=1622) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 11, 2005
- [Cutechess-cli: A command line tool for engine-engine matches](http://www.talkchess.com/forum/viewtopic.php?t=27024) by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), March 16, 2009
- [Ponder console input move problem](http://www.talkchess.com/forum/viewtopic.php?t=34051) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), April 28, 2010 » [Pondering](Pondering "Pondering")
- [Bash script to start UCI engine and get evaluation](http://www.talkchess.com/forum/viewtopic.php?t=50630) by Scott O'Nan, [CCC](CCC "CCC"), December 25, 2013
- [how to probe egtb from console?](http://www.talkchess.com/forum/viewtopic.php?t=56363) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), May 15, 2015 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [command line engine match?](http://www.talkchess.com/forum/viewtopic.php?t=61988) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), November 06, 2016

## External Links

- [Command-line interface from Wikipedia](https://en.wikipedia.org/wiki/Command-line_interface)
- [List of command-line interpreters from Wikipedia](https://en.wikipedia.org/wiki/List_of_command-line_interpreters)
- [Redirection from Wikipedia](https://en.wikipedia.org/wiki/Redirection_%28computing%29)
- [Shell (computing) from Wikipedia](https://en.wikipedia.org/wiki/Shell_%28computing%29)
- [Command Prompt from Wikipedia](https://en.wikipedia.org/wiki/Command_Prompt)

[COMMAND.COM](https://en.wikipedia.org/wiki/COMMAND.COM)

- [Unix shell from Wikipedia](https://en.wikipedia.org/wiki/Unix_shell)

[Thompson shell](https://en.wikipedia.org/wiki/Thompson_shell) by [Ken Thompson](Ken_Thompson "Ken Thompson")

- [System console from Wikipedia](https://en.wikipedia.org/wiki/System_console)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Unix philosophy - McIlroy: A Quarter Century of Unix - Wikipedia](https://en.wikipedia.org/wiki/Unix_philosophy#McIlroy:_A_Quarter_Century_of_Unix)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Command-line interface from Wikipedia](https://en.wikipedia.org/wiki/Command-line_interface)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [unix2dos from Wikipedia](https://en.wikipedia.org/wiki/Unix2dos)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Cutechess-cli: A command line tool for engine-engine matches](http://www.talkchess.com/forum/viewtopic.php?t=27024) by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), March 16, 2009

**[Up one Level](User_Interface "User Interface")**

