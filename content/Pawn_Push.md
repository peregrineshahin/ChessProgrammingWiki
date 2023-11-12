---
title: Pawn Push
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Moves](Moves "Moves") \* Pawn Push**


A **Pawn Push** is a [quiet](Quiet_Moves "Quiet Moves"), [irreversible](Irreversible_Moves "Irreversible Moves") move of a [pawn](Pawn "Pawn") one single step forward, or optionally but only from its initial [rank](Ranks "Ranks"), two steps forward. The condition for a [pseudo-legal](Pseudo-Legal_Move "Pseudo-Legal Move") pawn push is that its [target square](Target_Square "Target Square") ahead, the [stop square](Stop_Square "Stop Square"), is [empty](Occupancy "Occupancy"), while the [origin square](Origin_Square "Origin Square") is obviously occupied by the pawn of the [side to move](Side_to_move "Side to move"). 



## Double Push


The double pawn push from the initial rank requires both squares ahead empty. [Making](Make_Move "Make Move") a double push is a precondition to set the [en passant](En_passant "En passant") target square in the obtained [position](Chess_Position "Chess Position"), as specified by initial [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") (FEN) unconditionally, where todays programs are instructed to set [en passant target square](Forsyth-Edwards_Notation#Enpassanttargetsquare "Forsyth-Edwards Notation") if the en passant would be [pseudo-legal](Pseudo-Legal_Move "Pseudo-Legal Move") (an opponent pawn left or right) or even better strictly [legal](Legal_Move "Legal Move") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, also considering [updating](Incremental_Updates "Incremental Updates") [Zobist keys](Zobrist_Hashing "Zobrist Hashing") during [make move](Make_Move "Make Move") to avoid dissimilarity of otherwise [repeated](Repetitions "Repetitions") [positions](Chess_Position "Chess Position") if the first occurrence happened after a double pawn push with no en passant capture actually possible <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



## See also


* [Pawn Pushes (Bitboards)](Pawn_Pushes_(Bitboards) "Pawn Pushes (Bitboards)")


## External Links


* [Pawn Movement from Wikipedia](https://en.wikipedia.org/wiki/Pawn_%28chess%29#Movement)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: Arasan test suite update](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=219015&t=23806) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](Computer_Chess_Forums "Computer Chess Forums"), September 19, 2008
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [en passant and hash key calculation](http://www.talkchess.com/forum/viewtopic.php?t=33397) by [Fred Hamilton](index.php?title=Fred_Hamilton&action=edit&redlink=1 "Fred Hamilton (page does not exist)"), [CCC](Computer_Chess_Forums "Computer Chess Forums"), March 21, 2010

**[Up one Level](Moves "Moves")**







 
