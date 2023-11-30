---
title: Graphics ProgrammingASCIIDiagrams
---
**[Home](Home "Home") * [Programming](Programming "Programming") * Graphics Programming**

**Graphics Programming** in computer chess is essentially about drawing [chess positions](Chess_Position "Chess Position") or diagrams within a [user interface](User_Interface "User Interface") to give [users](https://en.wikipedia.org/wiki/User_%28computing%29) a visual [feedback](https://en.wikipedia.org/wiki/Feedback) of the game state, while [interacting](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction) with the program.

## Visualization

- [2D Graphics Board](2D_Graphics_Board "2D Graphics Board")
-  

## Pseudo Graphics

## ASCII Diagrams

ASCII Diagrams on [teleprinters](https://en.wikipedia.org/wiki/Teleprinter) were already used by early programs, such as [The Bernstein Chess Program](The_Bernstein_Chess_Program "The Bernstein Chess Program"), and are still appropriate today for a rudimentary text oriented [command line](CLI "CLI") [user interface](User_Interface "User Interface"), to display a position on a [terminal](https://en.wikipedia.org/wiki/Computer_terminal) with [monospaced](https://en.wikipedia.org/wiki/Monospaced_font) [ASCII](https://en.wikipedia.org/wiki/ASCII) [characters](https://en.wikipedia.org/wiki/Character_%28computing%29). One may further store the characters inside "*[human readable](https://en.wikipedia.org/wiki/Human-readable_medium)*" [ASCII files](https://en.wikipedia.org/wiki/Text_file#ASCII) for [logging-](Logging "Logging") or [debugging](Debugging "Debugging") purposes. Several proposals to display an ASCII board were made in [CCC](CCC "CCC") <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> . [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") came up with the left one <a id="cite-note-3" href="#cite-ref-3">[3]</a> , [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl") proposed the right one with the remarks below <a id="cite-note-4" href="#cite-ref-4">[4]</a> :

```C++

kqKQ -
  +------------------------+       +-*--b--c--d--*--f--g--*-+
8 |*R *N:*B *Q:*K *B:*N *R:|     8 |[r][n][b][q][k][b][n][r]|
7 |*P:*P *P:*P *P:*P *P:*P |     7 |[p][p][p][p][p][p][p][p]|
6 |   :::   :::   :::   :::|     6 |   :::   :::   :::   :::|
5 |:::   :::   :::   :::   |     5 |:::   :::   :::   :::   |
4 |   :::   :::   :::   :::|     4 |   :::   :::   :::   :::|
3 |:::   :::   :::   :::   |     3 |:::   :::   :::   :::   |
2 | P :P: P :P: P :P: P :P:|     2 |<P><P><P><P><P><P><P><P>|
1 |:R: N :B: Q :K: B :N: R |     1 |<R><N><B><Q><K><B><N><R>|
  +------------------------+     =>+-*--b--c--d--*--f--g--*-+
    a  b  c  d  e  f  g  h

Remarks:
a) with "*"  is shown, where castling potential resides (FRC specific)
b) with "=>" is shown, which side has to move

```

## Semigraphics

Some of the early [home computers](https://en.wikipedia.org/wiki/Home_computer) had semigraphics characters and [sprites](https://en.wikipedia.org/wiki/Sprite_%28computer_graphics%29) <a id="cite-note-5" href="#cite-ref-5">[5]</a> for a more realistic board representation of chess programs.

[](http://www.computerhistory.org/chess/full_record.php?iid=stl-431e1a080c29f)
[MicroChess](MicroChess "MicroChess") Screen on [TRS-80](TRS-80 "TRS-80"), 1976 <a id="cite-note-6" href="#cite-ref-6">[6]</a>

## High Resolution Graphics

Next generation [home-](https://en.wikipedia.org/wiki/Home_computer) and [personal computers](https://en.wikipedia.org/wiki/Personal_computer) already did support not only [text mode](https://en.wikipedia.org/wiki/Text_mode) and semigraphics, but [graphic](https://en.wikipedia.org/wiki/Computer_graphics) modes for [resolutions](https://en.wikipedia.org/wiki/Graphic_display_resolutions) supported by the [computer monitor](https://en.wikipedia.org/wiki/Computer_monitor) and its [video controller](https://en.wikipedia.org/wiki/Video_card). A [system call](https://en.wikipedia.org/wiki/System_call) was necessary to switch the video card into a mode, where each [pixel](https://en.wikipedia.org/wiki/Pixel) was an element of an [array](Array "Array") [mapped](https://en.wikipedia.org/wiki/Memory-mapped_I/O) into the [main memory](Memory "Memory"), either [bit-wise](Bit "Bit") for [black-and-white](https://en.wikipedia.org/wiki/Black-and-white) or [nibble-](Nibble "Nibble"), [byte-](Byte "Byte") or [word-wise](Word "Word") for sixteen, 256 or more colors or [grayscale](https://en.wikipedia.org/wiki/Grayscale).

## DOS Area

Programs running under [MS-DOS](MS-DOS "MS-DOS") on [IBM PCs](IBM_PC "IBM PC"), initially using a [color graphics adapter](https://en.wikipedia.org/wiki/Color_Graphics_Adapter) (CGA), and later [Hercules graphics cards](https://en.wikipedia.org/wiki/Hercules_Graphics_Card) and [video graphics array](https://en.wikipedia.org/wiki/Video_Graphics_Array) (VGA), needed to use a [BIOS interrupt call](https://en.wikipedia.org/wiki/BIOS_interrupt_call), the [INT 10H](https://en.wikipedia.org/wiki/INT_10H), to switch graphic modes accordantly to make [all points addressable](https://en.wikipedia.org/wiki/All_Points_Addressable). Chess programs usually worked in [fullscreen](https://en.wikipedia.org/wiki/Fullscreen) mode at that times on single tasking operating systems, the program run exclusively and could access whole the hardware and memory. A VGA [resolution](https://en.wikipedia.org/wiki/Display_resolution) of 640x480 was quite sufficient for drawing an ergonomic chess board in [2D](2D_Graphics_Board "2D Graphics Board") or even [3D](3D_Graphics_Board "3D Graphics Board").

## Abstraction

With the advent of [multitasking](https://en.wikipedia.org/wiki/Computer_multitasking) operating systems with [memory protection](https://en.wikipedia.org/wiki/Memory_protection) between [processes](Process "Process") and a [protection ring model](https://en.wikipedia.org/wiki/Ring_%28computer_security%29), and their [graphical user interfaces](https://en.wikipedia.org/wiki/Graphical_user_interface) and window managers, direct access was no longer possible, and video hardware became abstract, accessible via [API-calls](https://en.wikipedia.org/wiki/Application_programming_interface) of kernel- or [graphic libraries](https://en.wikipedia.org/wiki/Graphics_library) or toolkits.

## Screenshots

[](http://www.mobygames.com/game/psion-chess/screenshots)
[Psion](Psion "Psion") for [Atari ST](Atari_ST "Atari ST") <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## See also

- [Chess Position](Chess_Position "Chess Position")
- [Extended Position Description](Extended_Position_Description "Extended Position Description") (EPD)
- [Figurine Algebraic Notation](Algebraic_Chess_Notation#FAN "Algebraic Chess Notation") (FAN)
- [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") (FEN)
- [GPU](GPU "GPU")
- [GUI](GUI "GUI")

## Publications

## 1979

- [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1979**). *Micro Graphics and X-Y Plotter*. [Personal Computing, Vol. 3, No. 2](Personal_Computing#3_2 "Personal Computing"), pp. 75

## 1990 ...

- [Alexander G. M. Smith](index.php?title=Alexander_G._M._Smith&action=edit&redlink=1 "Alexander G. M. Smith (page does not exist)") (**1991**). *[Handyman - A Multiuser Puppeteering System for Computer Graphics Motion Control](http://web.ncf.ca/au829/Handyman/Thesis.html)*. Masters thesis, [Carleton University](https://en.wikipedia.org/wiki/Carleton_University)

## 2000 ...

- [Vlad Stamate](Vlad_Stamate "Vlad Stamate") (**2004**). *Reduction of lighting calculations using Spherical Harmonics*. in [ShaderX3 - Advanced Rendering Techniques](http://www.shaderx3.com/Tables%20of%20Content.htm)
- [Vlad Stamate](Vlad_Stamate "Vlad Stamate") (**2005**). *Real-time damage deformation methods*. in [ShaderX4 - Advanced Rendering Techniques](http://www.shaderx4.com/TOC.html)
- [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**2006**). *[Computergrafik](http://www-lehre.inf.uos.de/%7Ecg/2006/skript/skript.html)*. [pdf](http://www-lehre.inf.uos.de/%7Ecg/2006/PDF/skript.pdf) (German)
- [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [Kang Zhang](http://www.utdallas.edu/%7Ekzhang/) (**2007**). *[Computer Graphics for Java Programmers](http://home.planet.nl/%7Eammeraal/grjava2e.html)*. 2nd edition, [Wiley](<https://en.wikipedia.org/wiki/Wiley_(publisher)>)
- [Michel Goossens](http://goossens.web.cern.ch/goossens/), [Frank Mittelbach](http://www.informit.com/authors/bio.aspx?a=A2624A62-C2B4-40F9-B8ED-E99563F89A27), [Sebastian Rahtz](http://users.ox.ac.uk/~rahtz/), [Denis Roegel](http://www.loria.fr/~roegel/), [Herbert Voß](http://www.uit.co.uk/Authors/HerbVoss) (**2007**). *[The LATEXGraphics Companion](http://xml.web.cern.ch/XML/lgc2/)*. 2nd edition, Addison-Wesley, [sample pdf](http://ptgmedia.pearsoncmg.com/images/9780321508928/samplepages/0321508920_Sample.pdf), 10.1 Chess, 10.2 Xiangqi—Chinese Chess <a id="cite-note-8" href="#cite-ref-8">[8]</a>
- [Vlad Stamate](Vlad_Stamate "Vlad Stamate") (**2008**). *Real Time Photon Mapping Approximation on the GPU*. in [ShaderX6 - Advanced Rendering Techniques](http://shaderx6.com/TOC.html) <a id="cite-note-9" href="#cite-ref-9">[9]</a>

## 2010 ...

- [Eric Lengye](https://en.wikipedia.org/wiki/Eric_Lengyel) (**2011**). *[Mathematics for 3D Game Programming and Computer Graphics, 3rd edition](http://www.mathfor3dgameprogramming.com/)*. [amazon.com](http://www.amazon.com/exec/obidos/tg/detail/-/1435458869)
- [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [Kang Zhang](http://www.utdallas.edu/%7Ekzhang/) (**2017**). *[Computer Graphics for Java Programmers](http://home.planet.nl/~ammeraal/grjava3e.html)*. 3rd edition, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

## Forum Posts

- [ASCII chess boards](https://www.stmintz.com/ccc/index.php?id=113510) by [Steffen Jakob](Steffen_A._Jakob "Steffen A. Jakob"), [CCC](CCC "CCC"), June 05, 2000
- [ASCII Board representation](https://www.stmintz.com/ccc/index.php?id=334290) by [Andreas Guettinger](Andreas_Guettinger "Andreas Guettinger"), [CCC](CCC "CCC"), December 08, 2003
- [How to place a chess piece on a bmp square ?](http://www.talkchess.com/forum/viewtopic.php?start=0&t=27853) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), May 11, 2009
- [Re: piece bitmaps - how to get a transparent background](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51798#p196372) by [H.G.Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), May 23, 2011

## External Links

- [Category:Chess bitmap pieces - Wikimedia Commons](http://commons.wikimedia.org/wiki/Category:Chess_bitmap_pieces)
- [Chess Graphics](http://www.enpassant.dk/chess/grafeng.htm) from [En Passant - Nørresundby Chess Club](http://www.enpassant.dk/chess/homeeng.htm)

## Algorithms

- [Even-odd rule from Wikipedia](https://en.wikipedia.org/wiki/Even-odd_rule)
- [Flood fill from Wikipedia](https://en.wikipedia.org/wiki/Flood_fill)
- [Line drawing algorithm from Wikipedia](https://en.wikipedia.org/wiki/Line_drawing_algorithm)

[Digital Differential Analyzer (graphics algorithm)](https://en.wikipedia.org/wiki/Digital_Differential_Analyzer_%28graphics_algorithm%29)
[Bresenham's line algorithm](https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm)
[Xiaolin Wu's line algorithm](https://en.wikipedia.org/wiki/Xiaolin_Wu%27s_line_algorithm)

- [Ray tracing (graphics) from Wikipedia](https://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29)
- [Spline interpolation from Wikipedia](https://en.wikipedia.org/wiki/Spline_interpolation)

## [De Boor's algorithm](https://en.wikipedia.org/wiki/De_Boor%27s_algorithm) [De Casteljau's algorithm](https://en.wikipedia.org/wiki/De_Casteljau%27s_algorithm) [Coordinates](https://en.wikipedia.org/wiki/Coordinate_system)

- [Coordinate system from Wikipedia](https://en.wikipedia.org/wiki/Coordinate_system)

[Cartesian coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system)
[Curvilinear coordinates](https://en.wikipedia.org/wiki/Curvilinear_coordinates)

- [Coordinate rotations and reflections from Wikipedia](https://en.wikipedia.org/wiki/Coordinate_rotations_and_reflections)
- [Euclidean space from Wikipedia](https://en.wikipedia.org/wiki/Euclidean_space)
- [List of common coordinate transformations from Wikipedia](https://en.wikipedia.org/wiki/List_of_common_coordinate_transformations)
- [Orthogonal group from Wikipedia](https://en.wikipedia.org/wiki/Orthogonal_group)
- [Transformation (function) from Wikipedia](https://en.wikipedia.org/wiki/Transformation_%28function%29)

## [Reflection (mathematics)](https://en.wikipedia.org/wiki/Reflection_%28mathematics%29) [Rotation (mathematics)](https://en.wikipedia.org/wiki/Rotation_%28mathematics%29) [Rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix) [Transformation matrix](https://en.wikipedia.org/wiki/Transformation_matrix) [Translation (geometry)](https://en.wikipedia.org/wiki/Translation_%28geometry%29) [Geometric primitives](https://en.wikipedia.org/wiki/Geometric_primitive)

- [Arc (geometry) from Wikipedia](https://en.wikipedia.org/wiki/Arc_%28geometry%29)
- [B-spline from Wikipedia](https://en.wikipedia.org/wiki/B-spline)
- [Bitmap from Wikipedia](https://en.wikipedia.org/wiki/Bitmap)
- [Bézier curve from Wikipedia](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
- [Circle from Wikipedia](https://en.wikipedia.org/wiki/Circle)
- [Ellipse from Wikipedia](https://en.wikipedia.org/wiki/Ellipse)
- [Line segment from Wikipedia](https://en.wikipedia.org/wiki/Line_segment)
- [Pixel from Wikipedia](https://en.wikipedia.org/wiki/Pixel)
- [Plane (geometry) from Wikipedia](https://en.wikipedia.org/wiki/Plane_%28geometry%29)
- [Polygon from Wikipedia](https://en.wikipedia.org/wiki/Polygon)
- [Polygonal chain from Wikipedia](https://en.wikipedia.org/wiki/Polygonal_chain)
- [Point (geometry) from Wikipedia](https://en.wikipedia.org/wiki/Point_%28geometry%29)
- [Point in polygon from Wikipedia](https://en.wikipedia.org/wiki/Point_in_polygon)
- [Quadrilateral from Wikipedia](https://en.wikipedia.org/wiki/Quadrilateral)
- [Rectangle from Wikipedia](https://en.wikipedia.org/wiki/Rectangle)
- [Spline (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Spline_%28mathematics%29)
- [Texture mapping from Wikipedia](https://en.wikipedia.org/wiki/Texture_mapping)
- [Triangle from Wikipedia](https://en.wikipedia.org/wiki/Triangle)

## Toolkits, Libraries and APIs

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

## [X11.app (XQuartz) from Wikipedia](https://en.wikipedia.org/wiki/X11.app) » [OS X](Mac_OS "Mac OS") Misc

- [Hiromi's Sonicbloom](https://en.wikipedia.org/wiki/Hiromi_Uehara#Hiromi.27s_Sonicbloom) - [XYG](https://en.wikipedia.org/wiki/Beyond_Standard), [Blue Note Tokyo](https://en.wikipedia.org/wiki/Blue_Note_Tokyo), November 29, 2007, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Hiromi Uehara](Category:Hiromi_Uehara "Category:Hiromi Uehara"), [Martin Valihora](https://en.wikipedia.org/wiki/Martin_Valihora), [Tony Grey](https://en.wikipedia.org/wiki/Tony_Grey), [David Fiuczynski](Category:David_Fiuczynski "Category:David Fiuczynski")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [ASCII chess boards](https://www.stmintz.com/ccc/index.php?id=113510) by [Steffen Jakob](Steffen_A._Jakob "Steffen A. Jakob"), [CCC](CCC "CCC"), June 05, 2000
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [ASCII Board representation](https://www.stmintz.com/ccc/index.php?id=334290) by [Andreas Guettinger](Andreas_Guettinger "Andreas Guettinger"), [CCC](CCC "CCC"), December 08, 2003
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: ASCII chess boards](https://www.stmintz.com/ccc/index.php?id=113544) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [CCC](CCC "CCC"), June 05, 2000
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: ASCII Board representation](https://www.stmintz.com/ccc/index.php?id=334328) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), December 08, 2003
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [List of home computers by video hardware from Wikipedia](https://en.wikipedia.org/wiki/List_of_home_computers_by_video_hardware)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Microchess 1.5 running on a Radio Shack TRS-80 microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=stl-431e1a080c29f), 1976, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Psion Chess screenshots](http://www.mobygames.com/game/psion-chess/screenshots) from [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [LaTeX from Wikipedia](https://en.wikipedia.org/wiki/LaTeX)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Photon mapping from Wikipedia](https://en.wikipedia.org/wiki/Photon_mapping)

**[Up one Level](Programming "Programming")**

