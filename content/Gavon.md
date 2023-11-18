---
title: Gavon
---
**[Home](Home "Home") * [Dedicated Chess Computers](Dedicated_Chess_Computers "Dedicated Chess Computers") * Gavon**

**[Home](Home "Home") * [User Interface](User_Interface "User Interface") * [GUI](GUI "GUI") * Gavon**

[](File:Gavon_tontec.jpg) Gavon 2 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Gavon**,

a portable, commercial chess system by [Josu Bergara Ede](index.php?title=Josu_Bergara_Ede&action=edit&redlink=1 "Josu Bergara Ede (page does not exist)") with the look and feel of the [dedicated chess computers](Dedicated_Chess_Computers "Dedicated Chess Computers") of the 80's, using [Windows](Windows "Windows") [tablet](https://en.wikipedia.org/wiki/Tablet_computer#Windows), [Raspberry Pi](Raspberry_Pi "Raspberry Pi"), [pcDuino](index.php?title=PcDuino&action=edit&redlink=1 "PcDuino (page does not exist)"), or [ODROID](index.php?title=ODROID&action=edit&redlink=1 "ODROID (page does not exist)") with [LCD](https://en.wikipedia.org/wiki/Liquid-crystal_display) and [Keypad](https://en.wikipedia.org/wiki/Keypad) unit <a id="cite-note-2" href="#cite-ref-2">[2]</a> or [TFT displays](https://en.wikipedia.org/wiki/Thin-film-transistor_liquid-crystal_display), and a [SD memory card](https://en.wikipedia.org/wiki/Secure_Digital) with pre-installed [open source chess engines](Category:Open_Source "Category:Open Source"), shipped via [eBay](https://en.wikipedia.org/wiki/EBay).
Gavon can be classified as a chess [GUI](GUI "GUI") similar to [Arena](Arena "Arena") or [Scid vs. PC](Scid_vs._PC "Scid vs. PC") with the chess engines integrated. It is written in [C](C "C"), like the chess engines compiled for the [ARM](index.php?title=ARM11&action=edit&redlink=1 "ARM11 (page does not exist)") processor, running under [Linux](Linux "Linux"), supporting both the [Universal Chess Interface](UCI "UCI") and the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [XBoard](XBoard "XBoard").

## Playing Chess

Gavon allows to play chess without connecting either to a PC or monitor. When the host system [boots](https://en.wikipedia.org/wiki/Booting), it will automatically start the Gavon controller program which loads the chess engines available.
Indicated by its LCD, one can select the engine, level and mode of play via the selection buttons. [Entering moves](Entering_Moves "Entering Moves") is possible via the keypad as well, but Gavon is also able to interface with various [USB](https://en.wikipedia.org/wiki/USB) or [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth) [Sensory boards](Sensory_Board "Sensory Board"), such as the [DGT USB Board](DGT_Board#USB "DGT Board") <a id="cite-note-3" href="#cite-ref-3">[3]</a> , [DGT Bluetooth Board](DGT_Board#Bluetooth "DGT Board") or [Berger's USB Solus Board](index.php?title=SolusChess&action=edit&redlink=1 "SolusChess (page does not exist)") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> Can be connected to classic chess computers such as [Saitek Renaissance](SciSys_Leonardo#Renaissance "SciSys Leonardo") using the [OSA-Link](SciSys_Leonardo#OSA "SciSys Leonardo") interface. Gavon has several opening created from world chess champions or from user custom [PGN](Portable_Game_Notation "Portable Game Notation") files that can be used to play the games. The played moves can be heard by an external speaker connected to the audio output of the Raspberry Pi.

## Available Chess Engines

- [Stockfish](Stockfish "Stockfish") v. 5.0 by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Marco Costalba](Marco_Costalba "Marco Costalba"), and [Joona Kiiski](Joona_Kiiski "Joona Kiiski") 2733
- [Stockfish](Stockfish "Stockfish") v. 6.0 by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Marco Costalba](Marco_Costalba "Marco Costalba"), and [Joona Kiiski](Joona_Kiiski "Joona Kiiski") 2683
- [DON](DON "DON") v. 150914 by [Ehsan Rashid](index.php?title=Ehsan_Rashid&action=edit&redlink=1 "Ehsan Rashid (page does not exist)") 2635
- [Stockfish](Stockfish "Stockfish") v. 3.32 by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Marco Costalba](Marco_Costalba "Marco Costalba"), and [Joona Kiiski](Joona_Kiiski "Joona Kiiski") 2627
- [IvanHoe](IvanHoe "IvanHoe") 999946f by *Yakov Petrovich Golyadkin* et al. 2545
- [Firenzina](Firenzina "Firenzina") v. 2.4.1 by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [Dmitri Gusev](Dmitri_Gusev "Dmitri Gusev") and [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades") 2520
- [Toga II](Toga "Toga") v 1.4 by [Thomas Gaksch](Thomas_Gaksch "Thomas Gaksch") and [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") 2437
- [Protector](Protector "Protector") v. 1.5 by [Raimund Heid](Raimund_Heid "Raimund Heid") 2427
- [Senpai](Senpai "Senpai") v. 1.0 by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") 2425
- [Protector](Protector "Protector") v. 1.8 by [Raimund Heid](Raimund_Heid "Raimund Heid") 2419
- [Protector](Protector "Protector") v. 1.7 by [Raimund Heid](Raimund_Heid "Raimund Heid") 2357
- [Crafty](Crafty "Crafty") v.24.1.by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") 2299
- [Fruit](Fruit "Fruit") v. 2.1 by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") 2297
- [Hakkapeliitta](Hakkapeliitta "Hakkapeliitta") v.2 [Mikko Aarnos](Mikko_Aarnos "Mikko Aarnos") 2294
- [Cheng4](Cheng "Cheng") v. 0.36c by [Martin Sedlak](Martin_Sedlak "Martin Sedlak") 2279
- [DiscoCheck](DiscoCheck "DiscoCheck") v.3.7 by Lucas Braesch 2278
- [Rodent](Rodent "Rodent") v. 1.2 by [Pawel Koziol](Pawel_Koziol "Pawel Koziol") 2246
- [Hakkapeliitta](Hakkapeliitta "Hakkapeliitta") v.1 [Mikko Aarnos](Mikko_Aarnos "Mikko Aarnos") 2229
- [GNU Chess](GNU_Chess "GNU Chess") v 5.07 by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian") 2219
- [GreKo](GreKo "GreKo") v. 10.3 by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev") 2207
- [Pepito](Pepito "Pepito") v1.59-2 by [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho") 2205
- [Diablo](Diablo "Diablo") v. 0.5.1 [Marcus Prewarski](Marcus_Prewarski "Marcus Prewarski") 2100
- [RedQueen](RedQueen "RedQueen") v 1.1.4 by [Ben-Hur Carlos Vieira Langoni Junior](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior") 2089
- [CPW-Engine](CPW-Engine "CPW-Engine") v. 1.1 by [Pawel Koziol](Pawel_Koziol "Pawel Koziol") and [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer") 2047
- [Faile](Faile "Faile") v. 1.2 by [Adrien Regimbald](Adrien_Regimbald "Adrien Regimbald") 2032
- [Jazz](Jazz "Jazz") by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek") 1978
- [Gullydeckel](Gullydeckel "Gullydeckel") v. 2.16 by [Martin Borriss](Martin_Borriss "Martin Borriss") 1967
- [Vice](Vice "Vice") v. 1.0 by [Bluefever](index.php?title=BluefeverSoft&action=edit&redlink=1 "BluefeverSoft (page does not exist)") 1953
- [Ifrit](Ifrit "Ifrit") v. j3.6 by [Andrey Brenkman](index.php?title=Andrey_Brenkman&action=edit&redlink=1 "Andrey Brenkman (page does not exist)")
- [Napoleon](Napoleon "Napoleon") by [Marco Pampaloni](Marco_Pampaloni "Marco Pampaloni") 1931
- [Claudia](Claudia "Claudia") v.02 by [Antonio Garro](index.php?title=Antonio_Garro&action=edit&redlink=1 "Antonio Garro (page does not exist)") 1931
- [Jabba](Jabba "Jabba") v. 1.0 by [Richard Allbert](Richard_Allbert "Richard Allbert") 1888
- [Sissa](index.php?title=Sissa&action=edit&redlink=1 "Sissa (page does not exist)") v. 2.0 by [Christophe Mandin](index.php?title=Christophe_Mandin&action=edit&redlink=1 "Christophe Mandin (page does not exist)") 1867
- [Cinnamon](Cinnamon "Cinnamon") v. 1.2b by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella") 1805
- [AdroitChess](index.php?title=AdroitChess&action=edit&redlink=1 "AdroitChess (page does not exist)") v.0.3 by [Daniel White](Daniel_White "Daniel White") 1749
- [Lime](Lime "Lime") v. 66 by [Richard Allbert](Richard_Allbert "Richard Allbert") 1778
- [Robocide](Robocide "Robocide") by [Daniel White](Daniel_White "Daniel White") 1773
- [Rocinante](Rocinante "Rocinante") v. 2.0 by [Antonio Torrecillas](Antonio_Torrecillas "Antonio Torrecillas") 1743
- [Bismark](Bismark "Bismark") v. 1.2 by [Evgeny Shtranvasser](Evgeny_Shtranvasser "Evgeny Shtranvasser") 1741
- [Maverick](Maverick "Maverick") v. 0.05 by [Steve Maughan](Steve_Maughan "Steve Maughan") 1738
- [Darky](index.php?title=Darky&action=edit&redlink=1 "Darky (page does not exist)") v. 0.5e by [Alex Guerrero](index.php?title=Alex_Guerrero&action=edit&redlink=1 "Alex Guerrero (page does not exist)")
- [RedQueen](RedQueen "RedQueen") v. 0.4 by [Ben-Hur Carlos Vieira Langoni Junior](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior") 1686
- [JFresh](JFresh "JFresh") v. 0.1.a by [Christian Daley](Christian_Daley "Christian Daley") 1603
- [Rocinante](Rocinante "Rocinante") v. 1.01 by [Antonio Torrecillas](Antonio_Torrecillas "Antonio Torrecillas") 1565

## Etymology

The name Gavon is the text reverse of [Novag](Novag "Novag"), in honor to the famous company of dedicated chess computers.

## See also

- [Caddell Chess](Caddell_Chess "Caddell Chess")
- [Dedicated Chess Computers](Dedicated_Chess_Computers "Dedicated Chess Computers")
- [DGT Board](DGT_Board "DGT Board")
- [Micro-Max](Micro-Max "Micro-Max")
- [pcDuino](index.php?title=PcDuino&action=edit&redlink=1 "PcDuino (page does not exist)")
- [PicoChess](PicoChess "PicoChess")
- [Raspberry Pi](Raspberry_Pi "Raspberry Pi")
- [Sensory Boards](Sensory_Board "Sensory Board")
- [SolusChess](index.php?title=SolusChess&action=edit&redlink=1 "SolusChess (page does not exist)")

## Forum Posts

- [GAVON Portable Chess System](http://www.talkchess.com/forum/viewtopic.php?t=51200) by [Bryan Whitby](index.php?title=Bryan_Whitby&action=edit&redlink=1 "Bryan Whitby (page does not exist)"), [CCC](CCC "CCC"), February 08, 2014
- [GAVON Portable Chess System](http://hiarcs.net/forums/viewtopic.php?t=6575&sid=b7c1e806c342b662b536ab62b24d7929) by [Chessmaster Ireland](index.php?title=Bryan_Whitby&action=edit&redlink=1 "Bryan Whitby (page does not exist)"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), February 08, 2014
- [Gavon is here...](http://hiarcs.net/forums/viewtopic.php?t=6599) by Paul Ward, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), February 17, 2014
- [Gavon, der flexible schachcomputer](https://www.schachcomputer.info/forum/showthread.php?t=4906) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [Schachcomputer.info](Computer_Chess_Forums "Computer Chess Forums"), January 25, 2015 (German)
- [Dedicated computers vs PC, PICOCHESS, GAVON](http://www.hiarcs.net/forums/viewtopic.php?t=7158) by chesspcmac, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), April 16, 2015 » [PicoChess](PicoChess "PicoChess")
- [Gavon 2 Chess Test Scores](http://www.hiarcs.net/forums/viewtopic.php?t=7306) by [Spacious Mind](The_Spacious_Mind "The Spacious Mind"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), July 23, 2015
- [Gavon 3 Chess Test Scores](http://www.hiarcs.net/forums/viewtopic.php?t=7490) by [Spacious Mind](The_Spacious_Mind "The Spacious Mind"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), November 02, 2015

## External Links

- [SolusChess connected to Gavon by Josu Bergara](https://sites.google.com/site/bergersprojects/reedcb/gavon)
- [Gavon USB DGT Raspberry Pi chess computer Schach computer, Ajedrez electronico](http://www.ebay.es/itm/Gavon-USB-DGT-Raspberry-Pi-chess-computer-Schach-computer-Ajedrez-electronico-/261506898461?pt=LH_DefaultDomain_186&hash=item3ce3069a1d&_uhb=1) | [eBay](https://en.wikipedia.org/wiki/EBay)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Tontec's](http://www.itontec.com/) 320x480 [TFT display](https://en.wikipedia.org/wiki/Thin-film-transistor_liquid-crystal_display) attached to [Raspberri Pi 2](Raspberry_Pi "Raspberry Pi") and [Mephisto Modular](Mephisto_Module_Systems "Mephisto Module Systems")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Adafruit RGB Positive 16x2 LCD+Keypad Kit for Raspberry Pi](https://www.adafruit.com/products/1109)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [DGT USB e-Board](http://www.dgtprojects.com/site/index.php/products/electronic-boards/usb)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Magnetic USB Chessboard (SolusChess) - Berger's Projects - DIY](https://sites.google.com/site/bergersprojects/reedcb)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [SolusChess connected to Gavon by Josu Bergara](https://sites.google.com/site/bergersprojects/reedcb/gavon)

**[Up one level](Dedicated_Chess_Computers "Dedicated Chess Computers")**

