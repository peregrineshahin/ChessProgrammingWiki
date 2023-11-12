---
title: CTG
---
**[Home](Home "Home") * [Knowledge](Knowledge "Knowledge") * [Opening Book](Opening_Book "Opening Book") * CTG**

**CTG**, (ChessBase Opening Tree of Games)

an opening book format by [ChessBase](ChessBase "ChessBase"), supported by their [Fritz GUI](Fritz#FritzGUI "Fritz") and [ChessBase GUI](</ChessBase_(Database)> "ChessBase (Database)"), and therefore used by all chess engines compatible with these commercial user interfaces. While the book format is proprietary, a partial specification was leaked for the purpose of interoperability <a id="cite-note-1" href="#cite-ref-1">[1]</a>. Each Chessbase book consists of four files, the binary **CTG** file contains the real data, the **INI** text file provides auxilliary information, the **CTB** file some kind of bitmap over free pages in the CTG file, and the **CTO** file, containing a lookup table into the CTG file for fast indexed access.
Only White to move [positions](Chess_Position "Chess Position") along with its [moves](Moves "Moves"), annotations and engine recommendations, and statistics are stored, probing black positions requires [color flipping](Color_Flipping "Color Flipping"), of course including [en passant](En_passant "En passant") square and [castling rigths](Castling_Rights "Castling Rights"). Further, if the white king is on files a-d, and neither side has any castling rights remaining, the board is [mirrored horizontally](Horizontal_Mirroring "Horizontal Mirroring"). The CTG file is organized in 4KiB pages, the first page contains header information such as the number of games, followed by consecutive data pages. Each data page starts with an header specifying the number of positions and bytes per page, followed by a [list](Linked_List "Linked List") of a variable length position entries.

## See also

- [ABK](ABK "ABK") - [Arena's](Arena "Arena") book format
- [BIN](PolyGlot "PolyGlot") - [PolyGlot](PolyGlot "PolyGlot") book format

## Open Source Engines

- [Brutus](Brutus_NL "Brutus NL")
- [Daydreamer](Daydreamer "Daydreamer")

## Forum Posts

- [CTG specification](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=2319) by [Sesse](Steinar_H._Gunderson "Steinar H. Gunderson"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), September 30, 2007
- [Brutus v8.5 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50747) by [Stephan Vermeire](Stephan_Vermeire "Stephan Vermeire"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 25, 2010 » [Brutus](Brutus_NL "Brutus NL")
- [CTG to polyglot format](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=52972) by matematiko, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 23, 2013 » [PolyGlot](PolyGlot "PolyGlot")
- [My new book is out: Noomen.ctg](http://www.talkchess.com/forum/viewtopic.php?t=60237) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), May 22, 2016
- [Scid / Scid vs. PC - ChessBase (.ctg) and Arena (.abk)](http://www.talkchess.com/forum/viewtopic.php?t=61165) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 19, 2016 » [ABK](ABK "ABK"), [SCID](SCID "SCID")
- [Noomen.ctg: UPDATE](http://www.talkchess.com/forum/viewtopic.php?t=61176) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), August 20, 2016

## External Links

- [Free Opening Book Downloads](http://www.hiarcs.com/chess-opening-book-free.htm) from [HIARCS Chess Software](HIARCS "HIARCS")
- [GitHub - sshivaji/ctgexporter: Converter for the CTG chess format. Export CTG to polyglot and other formats](https://github.com/sshivaji/ctgexporter) by [Shivkumar Shivaji](index.php?title=Shivkumar_Shivaji&action=edit&redlink=1 "Shivkumar Shivaji (page does not exist)") <a id="cite-note-2" href="#cite-ref-2">[2]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [CTG specification](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=2319) by [Sesse](Steinar_H._Gunderson "Steinar H. Gunderson"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), September 30, 2007
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [CTG to polyglot format](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=52972) by matematiko, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 23, 2013

**[Up one Level](Opening_Book "Opening Book")**

