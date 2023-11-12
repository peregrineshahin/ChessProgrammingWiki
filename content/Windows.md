---
title: Windows
---
**[Home](Home "Home") \* [Software](Software "Software") \* Windows**



[ Windows Server 2012 Logo [[1]](#cite_note-1)
**Windows**,  

a series of 32-bit and 64-bit [operating systems](https://en.wikipedia.org/wiki/Operating_system) by [Microsoft](Microsoft "Microsoft") for [x86](X86 "X86") and [x86-64](X86-64 "X86-64") [PC's](IBM_PC "IBM PC"), as well as [Windows CE](https://en.wikipedia.org/wiki/Microsoft_Windows_CE) for [embedded systems](https://en.wikipedia.org/wiki/Embedded_system) and the [mobile operating system](https://en.wikipedia.org/wiki/Mobile_operating_system) [Windows Mobile](https://en.wikipedia.org/wiki/Windows_Mobile). Its development started in the early 80s as a [graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface) for 16-bit [MS-DOS](MS-DOS "MS-DOS") operating system, with the ability to perform [cooperative multitasking](https://en.wikipedia.org/wiki/Computer_multitasking#Cooperative_multitasking.2Ftime-sharing) while processing an [event loop](https://en.wikipedia.org/wiki/Event_loop). 



### Contents


* [1 Versions](#Versions)
* [2 Chess Engines](#Chess_Engines)
* [3 Windows Chess GUIs](#Windows_Chess_GUIs)
* [4 Applications](#Applications)
	+ [4.1 Major](#Major)
	+ [4.2 Accessories](#Accessories)
	+ [4.3 Entertainment](#Entertainment)
	+ [4.4 Remote Desktop](#Remote_Desktop)
* [5 Development](#Development)
	+ [5.1 IDE](#IDE)
	+ [5.2 Frameworks](#Frameworks)
	+ [5.3 Subsystems](#Subsystems)
	+ [5.4 SDK](#SDK)
	+ [5.5 API](#API)
		- [5.5.1 Input and Output](#Input_and_Output)
		- [5.5.2 Memory](#Memory)
		- [5.5.3 Interprocess Communications](#Interprocess_Communications)
		- [5.5.4 Dynamic Linking](#Dynamic_Linking)
	+ [5.6 C](#C)
		- [5.6.1 WinMain and the Message loop](#WinMain_and_the_Message_loop)
		- [5.6.2 Window Procedure](#Window_Procedure)
		- [5.6.3 Standard C Library](#Standard_C_Library)
	+ [5.7 C++](#C.2B.2B)
		- [5.7.1 Command-Line Applications](#Command-Line_Applications)
		- [5.7.2 Class Libs](#Class_Libs)
		- [5.7.3 Compiler](#Compiler)
		- [5.7.4 Calling Conventions](#Calling_Conventions)
	+ [5.8 Other Languages](#Other_Languages)
* [6 See also](#See_also)
* [7 Publications](#Publications)
* [8 Forum Posts](#Forum_Posts)
	+ [8.1 1995 ...](#1995_...)
	+ [8.2 2000 ...](#2000_...)
	+ [8.3 2010 ...](#2010_...)
	+ [8.4 2015 ...](#2015_...)
* [9 Further Links](#Further_Links)
* [10 References](#References)








|  |  |
| --- | --- |
| [Windows1FileManager1985.jpg](http://www.digibarn.com/collections/software/microsoft/windows10/page_01.htm) | [Windowa211 286.jpg](http://www.digibarn.com/collections/software/microsoft/windows286/index.html) |
|  Windows 1.0, 1985 [[2]](#cite_note-2) |  Windows/286 2.11, 1987 [[3]](#cite_note-3) |
| [Windowsnt40 screenshot.jpg](http://www.operating-system.org/betriebssystem/_german/bs-winnt40.htm) | [https://en.wikipedia.org/wiki/Windows_10](File:Virtual_Desktops_in_Windows_10.png "https://en.wikipedia.org/wiki/Windows_10") |
|  Windows NT 4.0 [[4]](#cite_note-4) |  Windows 10 [Task View](https://en.wikipedia.org/wiki/Task_View) [[5]](#cite_note-5) |


* [List of Microsoft Windows versions](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions)
* [Windows 1.0](https://en.wikipedia.org/wiki/Windows_1.0)
* [Windows 2.0](https://en.wikipedia.org/wiki/Windows_2.0)
* [Windows 3.0](https://en.wikipedia.org/wiki/Windows_3.0)
* [Windows 95](https://en.wikipedia.org/wiki/Windows_95)
* [Windows NT](https://en.wikipedia.org/wiki/Windows_NT)
* [Windows 2000](https://en.wikipedia.org/wiki/Windows_2000)
* [Windows XP](https://en.wikipedia.org/wiki/Windows_XP)
* [Windows Vista](https://en.wikipedia.org/wiki/Windows_Vista)
* [Windows CE](https://en.wikipedia.org/wiki/Microsoft_Windows_CE)
* [Windows Mobile](https://en.wikipedia.org/wiki/Windows_Mobile)
* [Windows 7](https://en.wikipedia.org/wiki/Windows_7)
* [Windows Phone 7](https://en.wikipedia.org/wiki/Windows_Phone_7)
* [Windows 8](https://en.wikipedia.org/wiki/Windows_8)
* [Windows Phone 8](https://en.wikipedia.org/wiki/Windows_Phone_8)
* [Windows 10](https://en.wikipedia.org/wiki/Windows_10)
* [Windows 10 Mobile](https://en.wikipedia.org/wiki/Windows_10_Mobile)


## Chess Engines


Most current [chess engines](Engines "Engines") are suited to run under Windows, a few with its own proprietary [user interface](GUI "GUI"), but most common as [console application](https://en.wikipedia.org/wiki/Console_application) and [child process](Process "Process") of an external [chess GUI](GUI "GUI") communicating via [redirected](https://en.wikipedia.org/wiki/Redirection_%28computing%29) [standard streams](https://en.wikipedia.org/wiki/Standard_streams) [[6]](#cite_note-6) using protocols like the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") (WinBoard) and/or the [Universal Chess Interface](UCI "UCI") (UCI).



## Windows Chess GUIs




|  |  |
| --- | --- |
| [Arena320.jpg](http://www.playwitharena.com/) | [CPsshot2.png](http://sjeng.org/deepsjeng.html) |
| [Arena](Arena "Arena") [[7]](#cite_note-7) | [Deep Sjeng](Deep_Sjeng "Deep Sjeng") under [ChessPartner](ChessPartner "ChessPartner") [[8]](#cite_note-8) |
| [DeepFritz14d 1.jpg](http://shop.chessbase.com/en/products/deep_fritz_14_english) | [DeepRybkaInAqurium7.png](http://chessok.com/shop/index.php?Home=product_info&cPath=7_1&products_id=344) |
| [Deep Fritz 14 GUI](Fritz#FritzGUI "Fritz") [[9]](#cite_note-9) | [Deep Rybka 4](Rybka "Rybka") [Aquarium](Aquarium "Aquarium") [[10]](#cite_note-10) |


* [Aquarium](Aquarium "Aquarium")
* [Arena](Arena "Arena")
* [Banksia GUI](Banksia_GUI "Banksia GUI")
* [Chess Academy](index.php?title=Chess_Academy&action=edit&redlink=1 "Chess Academy (page does not exist)")
* [ChessGUI](ChessGUI "ChessGUI")
* [ChessPartner GUI](ChessPartner "ChessPartner")
* [ChessX](ChessX "ChessX")
* [Cute Chess](Cute_Chess "Cute Chess")
* [Fritz GUI](Fritz#FritzGUI "Fritz")
* [HIARCS Chess Explorer](HIARCS_Chess_Explorer "HIARCS Chess Explorer")
* [Mayura Chess Board](index.php?title=Mayura_Chess_Board&action=edit&redlink=1 "Mayura Chess Board (page does not exist)")
* [WinBoard](WinBoard "WinBoard")
* [Shredder GUI](Shredder "Shredder")
* [Scid vs. PC](Scid_vs._PC "Scid vs. PC")


## Applications


### Major


* [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer)
* [Microsoft Edge](https://en.wikipedia.org/wiki/Microsoft_Edge)
* [Microsoft Outlook](https://en.wikipedia.org/wiki/Microsoft_Outlook)
* [Microsoft Exchange Server](https://en.wikipedia.org/wiki/Microsoft_Exchange_Server)
* [Microsoft Office](https://en.wikipedia.org/wiki/Microsoft_Office)


 [Microsoft Word](https://en.wikipedia.org/wiki/Microsoft_Word)
 [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel)
 [Microsoft PowerPoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint)
### Accessories


* [Command Prompt](https://en.wikipedia.org/wiki/Cmd.exe)
* [Win32 console](https://en.wikipedia.org/wiki/Win32_console)
* [Windows Explorer](https://en.wikipedia.org/wiki/Windows_Explorer)
* [Notepad](https://en.wikipedia.org/wiki/Notepad_%28Windows%29)
* [Notepad++](https://en.wikipedia.org/wiki/Notepad%2B%2B)
* [Wordpad](https://en.wikipedia.org/wiki/Wordpad)
* [Calculator](https://en.wikipedia.org/wiki/Calculator_%28Windows%29)
* [Paint](https://en.wikipedia.org/wiki/Paint_%28software%29)


### Entertainment


* [Microsoft Entertainment Pack](https://en.wikipedia.org/wiki/Microsoft_Entertainment_Pack)


 [Taipei](https://en.wikipedia.org/wiki/Microsoft_Mahjong) by [David Norris](David_Norris "David Norris")
 [Ziggurat](Ziggurat "Ziggurat") by [David Norris](David_Norris "David Norris")
### Remote Desktop


* [Remote Desktop Protocol](https://en.wikipedia.org/wiki/Remote_Desktop_Protocol)


 [Remote Desktop Services, MSDN](http://msdn.microsoft.com/en-us/library/bb892075%28v=VS.85%29.aspx)
## Development


Covers [integrated development environments](https://en.wikipedia.org/wiki/Integrated_development_environment) (IDE), [Software development kit](https://en.wikipedia.org/wiki/Software_development_kit) (SDK), [Application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) (API), programming languages, compiler and tools.



### IDE


* [Microsoft Visual Studio from Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Visual_Studio)


 [Visual Studio 2010, MSDN](http://msdn.microsoft.com/en-us/library/dd831853%28v=VS.100%29.aspx)
* [Eclipse from Wikipedia](https://en.wikipedia.org/wiki/Eclipse_%28software%29)


 [Eclipse.org home](http://www.eclipse.org/)
### Frameworks


* [.NET Framework from Wikipedia](https://en.wikipedia.org/wiki/.NET_Framework)
* [Comparison of the Java and .NET platforms from Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_the_Java_and_.NET_platforms)
* [Common Language Runtime from Wikipedia](https://en.wikipedia.org/wiki/Common_Language_Runtime)


 [Common Language Runtime Overview, MSDN](http://msdn.microsoft.com/en-us/library/ddk909ch.aspx)
 [Windows Communication Foundation from Wikipedia](https://en.wikipedia.org/wiki/Windows_Communication_Foundation)
### Subsystems


* [Virtual DOS machine from Wikipedia](https://en.wikipedia.org/wiki/Virtual_DOS_machine)
* [Windows on Windows from Wikipedia](https://en.wikipedia.org/wiki/Windows_on_Windows)
* [WOW64 from Wikipedia](https://en.wikipedia.org/wiki/WOW64)


### SDK


* [Microsoft Windows SDK from Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Windows_SDK)
* [MSDN: Microsoft Development](http://msdn.microsoft.com/en-us/default.aspx)
* [Windows Development, MSDN](http://msdn.microsoft.com/en-us/library/ms632593%28v=VS.85%29.aspx)


### API


* [Windows API from Wikipedia](https://en.wikipedia.org/wiki/Windows_API)
* [Windows Runtime from Wikipedia](https://en.wikipedia.org/wiki/Windows_Runtime)
* [Windowing, MSDN](http://msdn.microsoft.com/en-us/library/ms632586%28v=VS.85%29.aspx)
* [Universal Windows Platform from Wikipedia](https://en.wikipedia.org/wiki/Universal_Windows_Platform)


### Input and Output


* [User Input, MSDN](http://msdn.microsoft.com/en-us/library/ms632585%28v=VS.85%29.aspx)
* [Painting and Drawing, MSDN](http://msdn.microsoft.com/en-us/library/dd162759%28v=VS.85%29.aspx)
* [DirectX](https://en.wikipedia.org/wiki/DirectX)
* [File Management, MSDN](http://msdn.microsoft.com/en-us/library/aa364407%28v=VS.85%29.aspx)


### [Memory](Memory "Memory")


* [Memory Management, MSDN](http://msdn.microsoft.com/en-us/library/aa366779%28v=VS.85%29.aspx)
* [Enumerating a Heap, MSDN](http://msdn.microsoft.com/en-us/library/ee175819%28v=VS.85%29.aspx)
* [Allocating Memory from a NUMA Node, MSDN](http://msdn.microsoft.com/en-us/library/aa965223%28v=VS.85%29.aspx) » [NUMA](NUMA "NUMA")
* [NUMA Support (Windows), MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363804(v=vs.85).aspx)
* [Windows Memory Management - CodeProject](http://www.codeproject.com/KB/threads/Memory.aspx)
* [Memory Limits for Applications on Windows](http://software.intel.com/en-us/articles/memory-limits-applications-windows/) by [Steve Lionel](http://software.intel.com/en-us/user/512685) ([Intel](Intel "Intel")), May 16, 2011


### Interprocess Communications


* [Processes and Threads, MSDN](http://msdn.microsoft.com/en-us/library/ms684841%28v=VS.85%29.aspx)
* [Interprocess Communications, MSDN](http://msdn.microsoft.com/en-us/library/aa365574%28v=VS.85%29.aspx)
* [Creating a Child Process with Redirected Input and Output, MSDN](http://msdn.microsoft.com/en-us/library/ms682499%28VS.85%29.aspx)
* [Pipes, MSDN](http://msdn.microsoft.com/en-us/library/aa365780%28v=VS.85%29.aspx)
* [Dynamic Data Exchange](https://en.wikipedia.org/wiki/Dynamic_Data_Exchange) (DDE)
* [Object Linking and Embedding](https://en.wikipedia.org/wiki/Object_Linking_and_Embedding) (OLE)
* [Component Object Model](https://en.wikipedia.org/wiki/Component_Object_Model) (COM)
* [ActiveX](https://en.wikipedia.org/wiki/ActiveX)
* [Distributed Component Object Model](https://en.wikipedia.org/wiki/Distributed_Component_Object_Model) (DCOM)
* [Common Object Request Broker Architecture](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture) (CORBA)
* [Processes, Threads, and Jobs](http://download.microsoft.com/download/5/b/3/5b38800c-ba6e-4023-9078-6e9ce2383e65/c06x1116607.pdf) (pdf) from [Microsoft® Windows® Internals, Fourth Edition: Windows 2000, Windows XP, and Windows Server 2003](http://www.microsoft.com/learning/en/us/book.aspx?ID=6710&locale=en-us) by [David Solomon](http://www.solsem.com/) and [Mark Russinovich](https://en.wikipedia.org/wiki/Mark_Russinovich)


### Dynamic Linking


* [Dynamic-link library from Wikipedia](https://en.wikipedia.org/wiki/Dynamic-link_library)


 [Dynamic-Link Libraries, MSDN](http://msdn.microsoft.com/en-us/library/ms682589%28VS.85%29.aspx)
* [DLL hell from Wikipedia](https://en.wikipedia.org/wiki/DLL_hell)


 [The End of DLL Hell, MSDN](http://msdn.microsoft.com/en-us/library/ms811694.aspx)
C
-


[C](C "C") programmers were faced with some new paradigms from early 16-bit [Windows API](https://en.wikipedia.org/wiki/Windows_API), not to mention the fact that a lot of [C standard library](https://en.wikipedia.org/wiki/C_standard_library) functions were hard and error-prone to use, or even taboo [[11]](#cite_note-11) . [Charles Petzold](https://en.wikipedia.org/wiki/Charles_Petzold): "The original [hello world program](https://en.wikipedia.org/wiki/Hello_world_program) in the [Windows 1.0 SDK](https://en.wikipedia.org/wiki/Microsoft_Windows_SDK) was a bit of a scandal. HELLO.C was about 150 lines long, and the HELLO.RC resource script had another 20 or so more lines". (...) Veteran C programmers often curled up in horror or laughter when encountering the Windows hello-world program." [[12]](#cite_note-12) .



### WinMain and the Message loop


Windows programs are [event-driven](https://en.wikipedia.org/wiki/Event-driven_programming), have no usual main, but [WinMain](http://msdn.microsoft.com/en-us/library/ms633559%28VS.85%29.aspx) to enter a [event loop](https://en.wikipedia.org/wiki/Event_loop) [[13]](#cite_note-13) , where [DispatchMessage](http://msdn.microsoft.com/en-us/library/ms644934%28VS.85%29.aspx) transfers [messages](http://msdn.microsoft.com/en-us/library/ms644958%28VS.85%29.aspx) to a [callback procedure](http://msdn.microsoft.com/en-us/library/ms632593%28v=VS.85%29.aspx) [associated](http://msdn.microsoft.com/en-us/library/ms633570%28v=VS.85%29.aspx#associating_proc) with the [window](http://msdn.microsoft.com/en-us/library/aa931018.aspx) the message refers to, i.e. for keyboard events one window which owns the [keyboard focus](https://en.wikipedia.org/wiki/Focus_%28computing%29). To make Windows applications work flawlessly, keeping its windows up to date, that is processing [paint messages](http://msdn.microsoft.com/en-us/library/dd145213%28v=vs.85%29.aspx), the [I/O bound](https://en.wikipedia.org/wiki/I/O_bound) [GUI](GUI "GUI") [thread](Thread "Thread") needs to be run in the message loop, to react on messages best within 20 ms. In early 16-bit Windows, DispatchMessage implemented [cooperative multitasking](https://en.wikipedia.org/wiki/Computer_multitasking#Cooperative_multitasking.2Ftime-sharing) - but one application being uncooperative could made the whole system hang.




```C++

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
   WNDCLASS wc;
   MSG msg;
   ...
   wc.lpfnWndProc = (WNDPROC) MyWndProc; // associate a Window procedure for this "class" of windows
   if (!RegisterClass(&wc)) // register window class
       return FALSE;
   hwnd = CreateWindow(...);
   ShowWindow(hwnd, SW_SHOW);
   while(GetMessage(&msg, NULL, 0, 0) > 0)
   {
     TranslateMessage(&msg);
     DispatchMessage(&msg);
   }
   return msg.wParam;
}

```

### Window Procedure


The callback or [Window procedure](http://msdn.microsoft.com/en-us/library/ms632593%28v=VS.85%29.aspx) is called from the above message loop.




```C++

LRESULT CALLBACK MyWndProc(
    HWND hwnd,        // handle to window
    UINT uMsg,        // message identifier
    WPARAM wParam,    // first message parameter
    LPARAM lParam)    // second message parameter
{
    PAINTSTRUCT ps;
    HDC hdc;
    switch (uMsg)
    {
        case WM_CREATE:    // Initialize the window
            return 0;
        case WM_PAINT:
            hdc = BeginPaint(hwnd, &ps);
            TextOut(hdc, 0, 0, "Hello, Windows!", 15);
            EndPaint(hwnd, &ps);
            return 0;
        case WM_DESTROY:   // Clean up window-specific data objects
            return 0;
        case WM_CHAR:      // Process Keyboard character events
            return 0;
        case WM_MOUSEMOVE: // Process mouse move events
            return 0;
        // Process other messages
        default:
            return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
    return 0;
}

```

### Standard C Library


* [C standard library from Wikipedia](https://en.wikipedia.org/wiki/C_standard_library)
* [Standard C Library Functions, MSDN](http://msdn.microsoft.com/en-us/library/aa366881%28VS.85%29.aspx)
* [Windows File I/O vs. C Run-time File I/O, MS Support](http://support.microsoft.com/kb/11988/en-us?fr=1)


### C++


Microsoft's proprietary [C++](Cpp "Cpp") [Foundation Classes](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library) wrapped the [handle](https://en.wikipedia.org/wiki/Handle_%28computing%29) based Windows API and hides much of its complexity. Still one of the early class libs, it has a lot of ugly [macros](https://en.wikipedia.org/wiki/Macro_%28computer_science%29), i.e. for [message maps](https://en.wikipedia.org/wiki/Message_Maps). [Borland's](https://en.wikipedia.org/wiki/Borland) counter part was the [Object Windows Library](https://en.wikipedia.org/wiki/Object_Windows_Library).



### Command-Line Applications


Applies for most [UCI](UCI "UCI") and/or [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") ([WinBoard](WinBoard "WinBoard")) compatible [chess engines](Engines "Engines"), relying on an external [GUI](GUI "GUI").



* [Creating Command-Line Applications (C++), MSDN](http://msdn.microsoft.com/en-us/library/bb384834.aspx)
* [Managed Extensions for C++ from Wikipedia](https://en.wikipedia.org/wiki/Managed_Extensions_for_C%2B%2B) now deprecated


### Class Libs


* [Windows Forms from Wikipedia](https://en.wikipedia.org/wiki/Windows_Forms)
* [Microsoft Foundation Classes from Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library)


 [MFC Reference, MSDN](http://msdn.microsoft.com/en-us/library/d06h2x6e%28VS.80%29.aspx)
* [Visual Component Library from Wikipedia](https://en.wikipedia.org/wiki/Visual_Component_Library)
* [Object Windows Library from Wikipedia](https://en.wikipedia.org/wiki/Object_Windows_Library)
* [Interix from Wikipedia](https://en.wikipedia.org/wiki/Interix)
* [Qt (software) from Wikipedia](https://en.wikipedia.org/wiki/Qt_(software))
* [Boost (C++ libraries) from Wikipedia](https://en.wikipedia.org/wiki/Boost_(C%2B%2B_libraries))


### Compiler


* [Visual C++ from Wikipedia](https://en.wikipedia.org/wiki/Visual_C%2B%2B)


 [Visual C++ Tutorials, Library, and More on MSDN](http://msdn.microsoft.com/en-us/visualc/default.aspx)
* [MinGW from Wikipedia](https://en.wikipedia.org/wiki/MinGW), port of the [GNU Compiler Collection](Free_Software_Foundation#GCC "Free Software Foundation") (GCC)


 [MinGW - Minimalist GNU for Windows](http://www.mingw.org/)
* [Cygwin from Wikipedia](https://en.wikipedia.org/wiki/Cygwin), [Unix](Unix "Unix")-like environment and [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface)


 [Cygwin Information and Installation](http://www.cygwin.com/)
* [Intel C++ Compiler from Wikipedia](https://en.wikipedia.org/wiki/Intel_C%2B%2B_Compiler)


 [Intel® Compilers](http://software.intel.com/en-us/intel-compilers/)
 [Intel(R) C++ Compiler User and Reference Guides](http://software.intel.com/sites/products/documentation/hpc/compilerpro/en-us/cpp/win/compiler_c/index.htm) covers Intrinsics » [x86](X86 "X86"), [x86-64](X86-64 "X86-64"), [MMX](MMX "MMX"), [SSE2](SSE2 "SSE2"), [SSSE3](SSSE3 "SSSE3"), [SSE4](SSE4 "SSE4"), [AVX](AVX "AVX")
### Calling Conventions


[Agner Fog](http://www.agner.org/) describes [x86](X86 "X86") and [x86-64](X86-64 "X86-64") [calling conventions](https://en.wikipedia.org/wiki/Calling_convention) for different C++ compilers and operating systems, covering 32-bit and 64-bit Windows [[14]](#cite_note-14) :


The document contains details about data representation, function calling conventions, register usage conventions, name mangling schemes, etc. for many different C++ compilers and operating systems. Discusses compatibilities and incompatibilities between different C++ compilers. Includes information that is not covered by the official [Application Binary Interface](https://en.wikipedia.org/wiki/Application_binary_interface) standards (ABI's). The information provided here is based on my own research and therefore descriptive rather than normative. Intended as a source of reference for programmers who want to make function libraries compatible with multiple compilers or operating systems and for makers of compilers and other development tools who want their tools to be compatible with existing tools.



### Other Languages


* [C#](C_sharp "C sharp")
* [Visual Basic from Wikipedia](https://en.wikipedia.org/wiki/Visual_Basic)
* [Embarcadero Delphi from Wikipedia](https://en.wikipedia.org/wiki/Delphi_programming_language)
* [Intel Fortran Compiler from Wikipedia](https://en.wikipedia.org/wiki/Intel_Fortran_Compiler)
* [Java](Java "Java")


## See also


* [Linux](Linux "Linux")
* [Mac OS](Mac_OS "Mac OS")
* [MS-DOS](MS-DOS "MS-DOS")
* [OS/2 from Wikipedia](https://en.wikipedia.org/wiki/OS/2)
* [Unix](Unix "Unix")


## Publications


* [Pavel Yosifovich](https://github.com/zodiacon), [Mark Russinovich](https://en.wikipedia.org/wiki/Mark_Russinovich), [David Solomon](https://www.youtube.com/watch?v=Uki0MkC4UZw), [Alex Ionescu](http://www.alex-ionescu.com/) (**2017**). *[Microsoft Windows Internals](https://docs.microsoft.com/en-us/sysinternals/learn/windows-internals)*. 7th Edition


## Forum Posts


### 1995 ...


* [hash mem in win-chess progs](https://groups.google.com/d/msg/rec.games.chess.computer/Taxgk4l-S90/ggkiWEVavYsJ) by [Pc Sol](Adrian_Millett "Adrian Millett"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 28, 1995 » [Transposition Table](Transposition_Table "Transposition Table")
* [Win32 based "professional" chess software](http://groups.google.com/group/alt.chess.ics/browse_frm/thread/ce35d86e9dfde6ae) by Chris Smith, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 17, 1997
* [What will be the position of Windows in 3, 4 years in the future?](https://www.stmintz.com/ccc/index.php?id=79963) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), November 29, 1999


### 2000 ...


* [Re: Stormx is this a Crafty Clone??](https://www.stmintz.com/ccc/index.php?id=367073) by [Sean Empey](Sean_Empey "Sean Empey"), [CCC](CCC "CCC"), May 25, 2004 » [Process](Process "Process"), [Thread](Thread "Thread")
* [Kiwi for Win98 and input-reading stuff](https://www.stmintz.com/ccc/index.php?id=389667) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), September 29, 2004 » [Kiwi](Kiwi "Kiwi"), [C++](Cpp "Cpp"), [Thread](Thread "Thread")


### 2010 ...


* [MSVC calloc question](http://www.talkchess.com/forum/viewtopic.php?t=38441) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 17, 2011
* [Windows GCC Development](http://www.talkchess.com/forum/viewtopic.php?t=41908) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), January 10, 2012
* [microsecond-accurate timing on Windows](http://www.talkchess.com/forum/viewtopic.php?t=43864) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), May 28, 2012
* [Windows 8.1 and Visual Studio 2013 preview](http://www.talkchess.com/forum/viewtopic.php?t=48481) by [Jose Mº Velasco](Jose_Maria_Velasco "Jose Maria Velasco"), [CCC](CCC "CCC"), June 30, 2013


### 2015 ...


* [Windows 10 Experience](http://www.talkchess.com/forum/viewtopic.php?t=57236) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), August 10, 2015
* [OT: Full Removal of Windows 10](http://www.talkchess.com/forum/viewtopic.php?t=58587) by Terry McCracken, [CCC](CCC "CCC"), December 13, 2015
* [Weird Windows / WinBoard behavior](http://www.talkchess.com/forum/viewtopic.php?t=61435) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 15, 2016 » [Process](Process "Process"), [WinBoard](WinBoard "WinBoard")
* [Help needed for porting to Windows](http://www.talkchess.com/forum/viewtopic.php?t=61793) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 22, 2016
* [MinGW AlphaBlend](http://www.talkchess.com/forum/viewtopic.php?t=62315) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 29, 2016 » [2D Graphics Board](2D_Graphics_Board "2D Graphics Board"), [WinBoard](WinBoard "WinBoard") [[15]](#cite_note-15)
* [Importance of Windows XP support](http://www.talkchess.com/forum/viewtopic.php?t=63568) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), March 27, 2017
* [DOSBox Windows 95 for Chess](http://hiarcs.net/forums/viewtopic.php?t=9403&start=16) by [The Spacious Mind](The_Spacious_Mind "The Spacious Mind"), [HIARCS Forum](Computer_Chess_Forums "Computer Chess Forums"), March 09, 2019 » [Bringer](Bringer "Bringer"), [Chessmaster](Chessmaster "Chessmaster"), ...


## Further Links


* [Microsoft Windows from Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Windows)
* [Wintel from Wikipedia](https://en.wikipedia.org/wiki/Wintel) » [Intel](Intel "Intel")
* [Wine (software) from Wikipedia](https://en.wikipedia.org/wiki/Wine_%28software%29)
* [Engineering Windows 7 - Windows Desktop Search](http://blogs.msdn.com/e7/archive/2008/10/13/windows-desktop-search.aspx) by [Chris McConnell](Chris_McConnell "Chris McConnell"), October 13, 2008


## References


1. [↑](#cite_ref-1) [Microsoft Windows from Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Windows)
2. [↑](#cite_ref-2) [Microsoft Windows 1.03 and other tools, 1985](http://www.digibarn.com/collections/software/microsoft/windows10/page_01.htm) from [DigiBarn](http://www.digibarn.com/)
3. [↑](#cite_ref-3) [Microsoft Windows/286 2.11 and other tools](http://www.digibarn.com/collections/software/microsoft/windows286/index.html) from [DigiBarn](http://www.digibarn.com/)
4. [↑](#cite_ref-4) [Windows NT 4.0 Workstation Betriebssystem](http://www.operating-system.org/betriebssystem/_german/bs-winnt40.htm)
5. [↑](#cite_ref-5) [<https://en.wikipedia.org/wiki/Task_View> Task View from Wikipedia
6. [↑](#cite_ref-6) [Creating a Child Process with Redirected Input and Output, MSDN](http://msdn.microsoft.com/en-us/library/ms682499%28VS.85%29.aspx)
7. [↑](#cite_ref-7) [Free chess graphical user interface (GUI) Arena for chess engines](http://www.playwitharena.com/)
8. [↑](#cite_ref-8) [Sjeng - chess, audio and misc. software](http://sjeng.org/deepsjeng.html)
9. [↑](#cite_ref-9) [Deep Fritz 14](http://shop.chessbase.com/en/products/deep_fritz_14_english) from [ChessBase](ChessBase "ChessBase")
10. [↑](#cite_ref-10) [ChessOK, Chess Shop from the Developers of Rybka 3 Aquarium](http://chessok.com/shop/index.php?Home=product_info&cPath=7_1&products_id=344)
11. [↑](#cite_ref-11) [Standard C Library Functions](http://msdn.microsoft.com/en-us/library/aa366881%28VS.85%29.aspx) from [MSDN: Microsoft Development](http://msdn.microsoft.com/en-us/default.aspx)
12. [↑](#cite_ref-12) [Windows API from Wikipedia - History](https://en.wikipedia.org/wiki/Windows_API#History)
13. [↑](#cite_ref-13) [Message loop in Microsoft Windows](https://en.wikipedia.org/wiki/Message_loop_in_Microsoft_Windows)
14. [↑](#cite_ref-14) [Calling conventions for different C++ compilers and operating systems](http://www.agner.org/optimize/calling_conventions.pdf) (pdf) by [Agner Fog](http://www.agner.org/)
15. [↑](#cite_ref-15) [MinGW from Wikipedia](https://en.wikipedia.org/wiki/MinGW)

**[Up one Level](Software "Software")**







 
