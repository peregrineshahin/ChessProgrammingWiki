---
title: PascalTurboPascal
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Languages](Languages "Languages") \* Pascal**



[ [Blaise Pascal](Mathematician#Pascal "Mathematician") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Pascal** is an [imperative](https://en.wikipedia.org/wiki/Imperative_programming), [procedural](https://en.wikipedia.org/wiki/Procedural_programming) [programming language](https://en.wikipedia.org/wiki/Programming_language) developed and published in 1970 by [Niklaus Wirth](Mathematician#NEWirth "Mathematician") from [ETH Zurich](ETH_Zurich "ETH Zurich"). It is a small and efficient language intended to encourage good programming practices using [structured programming](https://en.wikipedia.org/wiki/Structured_programming) and [data structuring](https://en.wikipedia.org/wiki/Data_structure). Pascal is based on [Algol](Algol "Algol") and named in honor of the French mathematician and philosopher [Blaise Pascal](Mathematician#Pascal "Mathematician"), like many programming languages, but unlike [C](C "C"), Pascal allows nested procedure definitions to any level of depth, and also allows most kinds of definitions and declarations inside procedures and functions. 



### Contents


* [1 UCSD Pascal](#ucsd-pascal)
* [2 Turbo Pascal](#turbo-pascal)
	+ [2.1 Inline Assembly](#inline-assembly)
	+ [2.2 Source Sample](#source-sample)
* [3 See also](#see-also)
* [4 Pascal Engines](#pascal-engines)
* [5 Publications](#publications)
* [6 Forum Posts](#forum-posts)
* [7 External Links](#external-links)
* [8 References](#references)






A notable Pascal system was [UCSD-Pascal](https://en.wikipedia.org/wiki/UCSD_Pascal) from [University of California, San Diego](https://en.wikipedia.org/wiki/University_of_California,_San_Diego) that ran on a machine-independent operating system, the UCSD p-System portable. In the early 1980s, UCSD Pascal was ported to [Apple II](Apple_II "Apple II") computers to provide a structured alternative to the [Basic](Basic "Basic") interpreters that came with the machines.




## Turbo Pascal


An increased popularity of Pascal on [home computers](https://en.wikipedia.org/wiki/Home_computer) of the early 80s arose from the fast [one-pass](https://en.wikipedia.org/wiki/One-pass_compiler) [Turbo Pascal](https://en.wikipedia.org/wiki/Turbo_Pascal) compiler, running under [CP/M](https://en.wikipedia.org/wiki/CP/M) for 8-bit [8080](8080 "8080")/[Z80](Z80 "Z80") based computers, as well as [CP/M-86](https://en.wikipedia.org/wiki/CP/M-86) and [MS-DOS](MS-DOS "MS-DOS") for [8086](8086 "8086") and later [x86](X86 "X86") based 16- and 32-bit computers. [Borland](https://en.wikipedia.org/wiki/Borland) licensed the PolyPascal compiler core <a id="cite-note-2" href="#cite-ref-2">[2]</a>, written by [Anders Hejlsberg](https://en.wikipedia.org/wiki/Anders_Hejlsberg), and added user interface and editor, considered as one of the first [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_Development_Environment) for home computers. Anders Hejlsberg later joined the company as an employee and was the architect for all versions of the Turbo Pascal compiler and the first three versions of Borland [Delphi](Delphi "Delphi"). 


By 1995 Borland had dropped Turbo Pascal and replaced it with the [RAD](https://en.wikipedia.org/wiki/Rapid_Application_Development) environment [Delphi](Delphi "Delphi"), based on [Object Pascal](https://en.wikipedia.org/wiki/Object_Pascal). Early versions of Turbo Pascal are free downloadable from [Embarcadero Technologies](https://en.wikipedia.org/wiki/Embarcadero_Technologies) <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### Inline Assembly


Early versions of Turbo Pascal could include inline [machine code](https://en.wikipedia.org/wiki/Machine_code) as [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) [Byte](Byte "Byte") sequence, while later [Inline Assembly](Assembly#InlineAssembly "Assembly") was suported. None portable Inline assembly enabled programmers to access hardware features that were otherwise not directly available, and it was in fact overused by experienced Turbo Pascal programmers, as it could be seen from the source code of [Turbo Chess](Turbo_Chess "Turbo Chess") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, available from the *Turbo GameWorks Book* <a id="cite-note-5" href="#cite-ref-5">[5]</a> by [Kaare Danielsen](Kaare_Danielsen "Kaare Danielsen") <a id="cite-note-6" href="#cite-ref-6">[6]</a>.




### Source Sample


A sample of a [recursive](Recursion "Recursion") [Search](Search "Search") routine in Turbo Pascal from [KC Chess](KC_Chess "KC Chess"): [Kevin](R._Kevin_Phillips "R. Kevin Phillips") & [Craig's](Craig_S._Bruce "Craig S. Bruce") Chess Program <a id="cite-note-7" href="#cite-ref-7">[7]</a>:




```C++

{----------------------------------------------------------------------------}
{  Search:  This routine handles all of the tree searching except the first  }
{  level which of the tree which is handled by the main routine.  Given the  }
{  player, all of his moves are generated, and then each one is made.  The   }
{  enemy's maximum countermove score is subtracted from the move score, and  }
{  this gives the net value for the player making the move.  The maximum     }
{  net score is remembered and returned by this function.  The player's move }
{  is then taken back, and all of his other possible moves are tried in this }
{  same way.  If the score of any move exceeds the given cutoff value, then  }
{  no other of the player's moves are checked, and the score that exceeded   }
{  (or matched) the cutoff value is returned.  If the given depth is one or  }
{  less, then the enemy's countermoves are not checked, only the points for  }
{  taking the pieces, minus the points of the player's piece if the enemy's  }
{  piece is protected.  However, if the current player's move being          }
{  considered is a take and it is given that all of moves to that point      }
{  have been AllTakes, then enemy countermoves will be checked down to a     }
{  given depth of -1.  To calculate the enemy's best score in retaliation    }
{  to the given player's move, this routine is called recursively with the   }
{  enemy as the player to move, and a depth of the one originally given, -1. }
{  The new cutoff value is the score of the move that was just made, minus   }
{  the the best score that was found so far.  If the enemy's countermoves    }
{  score exceeds or matches this countermove value, then the net score of    }
{  the original player's move cannot exceed the best found so far, and the   }
{  move will be thrown out.  The new value for AllTakes is passed on as true }
{  if all moves heretofor have been takes, and the current player's move is  }
{  a take.  This routine is the core of the computer's 'thinking'.           }
{----------------------------------------------------------------------------}
  function Search (Turn: PieceColorType; CutOff, Depth: integer; AllTakes : boolean) : integer;
    var MoveList: MoveListType;
        j, LineScore, Score, BestScore, STCutOff: integer;
        Movement: MoveType;
        Attacked, Protected: integer;
        NoMoves, TakingPiece: boolean;
    begin
      {*** get the player's move list ***}
      GenMoveList (Turn, MoveList);
      NoMoves := true;
      BestScore := NegInfinity;
      j := MoveList.NumMoves;

      {*** go through all of the possible moves ***}
      while (j > 0) do begin
          Movement := MoveList.Move[j];
          {*** make the move ***}
          MakeMove (Movement, false, Score);
          {*** make sure it is legal (not moving into check) ***}
          AttackedBy (Player[Turn].KingRow, Player[Turn].KingCol, Attacked, Protected);
          if (Attacked = 0) then begin
              NoMoves := false;
              if (Score = STALE_SCORE) then
                  {*** end the search on a stalemate ***}
                  LineScore := Score
              else begin
 TakingPiece := Movement.PieceTaken.image <> BLANK; 
                  if (Depth <= 1) and not (AllTakes and TakingPiece and (Depth >= PLUNGE_DEPTH)) then begin
                      {*** have reached horizon node of tree: score points for piece taken ***}
                      {*** but assume own piece will be taken if enemy's piece is protected ***}
 if Movement.PieceTaken.image <> BLANK then begin 
                          AttackedBy (Movement.ToRow, Movement.ToCol, Attacked, Protected);
                          if Attacked > 0 then
 LineScore := Score - CapturePoints[Movement.PieceMoved.image] 
                          else
                              LineScore := Score;
                      end else
                          LineScore := Score;
                  end else begin
                      {*** new cutoff value ***}
                      STCutOff := Score - BestScore;
                      {*** recursive call for enemy's best countermoves score ***}
                      LineScore := Score - Search (EnemyColor[Turn], STCutOff,
                                                   Depth - 1, AllTakes and TakingPiece);
                  end;
              end;
              {*** remember player's maximum net score ***}
              if (LineScore > BestScore) then BestScore := LineScore;
          end;
          {*** un-do the move and check for cutoff ***}
          UnMakeMove (Movement);
          if BestScore >= CutOff then j := 0 else j := j - 1;
      end;
      if (BestScore = STALE_SCORE) then
          BestScore := -STALE_SCORE;   {stalemate means both players lose}
      if NoMoves then
          {*** player cannot move ***}
          if Player[Turn].InCheck then
              {*** if he is in check and cannot move, he loses ***}
              BestScore := - CapturePoints[KING]
          else
              {*** if he is not in check, then both players lose ***}
              BestScore := -STALE_SCORE; {prefer stalemate to checkmate}
      Search := BestScore;
    end; {Search}

```

## See also


* [Algol](Algol "Algol")
* [Delphi](Delphi "Delphi")
* [Modula-2](index.php?title=Modula-2&action=edit&redlink=1 "Modula-2 (page does not exist)")






## Pascal Engines


* [Category:Pascal](Category:Pascal "Category:Pascal")


## Publications


* [Brian W. Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) (**1981**). *[Why Pascal is Not My Favorite Programming Language](http://doc.cat-v.org/bell_labs/why_pascal/)*. [pdf](http://doc.cat-v.org/bell_labs/why_pascal/why_pascal_is_not_my_favorite_language.pdf)
* [Kaare Danielsen](Kaare_Danielsen "Kaare Danielsen") (**1985**). *[Turbo GameWorks](http://openlibrary.org/b/OL2753290M/Turbo_GameWorks)*. [Borland International](https://en.wikipedia.org/wiki/Borland)
* [Don Beal](Don_Beal "Don Beal") (**1986**). *Turbo GameWorks: Tools for Turbo Pascal*. (Review) [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 9, No. 2, pp. 88
* [Christopher Chabris](Christopher_Chabris "Christopher Chabris") (**1987**). *Artificial Intelligence and Turbo Pascal - Book and Disk*. Irwin Professional Pub, [amazon.com](http://www.amazon.com/Artificial-Intelligence-Turbo-Pascal-Book/dp/0870949632/ref=sr_1_10?s=books&ie=UTF8&qid=1352556486&sr=1-10) » [Artificial Intelligence](Artificial_Intelligence "Artificial Intelligence")


## Forum Posts


* [Is it worth to program chess in Pascal ? (Re: My first Chess program !)](http://groups.google.com/group/rec.games.chess.computer/msg/c98eca644be51aae) by [Ren Wu](Ren_Wu "Ren Wu"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 22, 1997
* [Update for Byte Chess 0.5](http://groups.google.com/group/comp.lang.pascal.misc/browse_frm/thread/13268077738fa33) by I Forget, [comp.lang.pascal.misc](http://groups.google.com/group/comp.lang.pascal.misc/topics), June 12, 2005 » [Chess 0.5](Chess_0.5 "Chess 0.5") <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>
* [Critter: Pascal vs C](http://www.talkchess.com/forum/viewtopic.php?t=29562) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), August 27, 2009 » [C](C "C")
* [FreePascal 64 bit question](http://www.talkchess.com/forum/viewtopic.php?t=37721) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), January 21, 2011
* [for Pascal fans: Critter](http://www.talkchess.com/forum/viewtopic.php?t=40414) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), September 16, 2011
* [Announcement: The Bozochess Project](http://www.talkchess.com/forum/viewtopic.php?t=40643) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), October 05, 2011
* [CookieCat Monday release schedule](http://www.talkchess.com/forum/viewtopic.php?t=41522) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 19, 2011 » [CookieCat](CookieCat "CookieCat")
* [CookieCat and perft](http://www.talkchess.com/forum/viewtopic.php?t=45568) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), October 14, 2012
* [New open source chess program](http://www.open-chess.org/viewtopic.php?f=3&t=2491) by [lauriet](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 03, 2013 » [LTChess](LTChess "LTChess")


## External Links


* [Pascal (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Pascal_%28programming_language%29)
* [Pascal Users group Newsletter](http://www.moorecad.com/standardpascal/pug.html)
* [Niklaus Wirth's 2004/10/20 Lecture](http://www.moorecad.com/standardpascal/wirthlect.html) for [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [ANSI-ISO PASCAL](http://www.moorecad.com/standardpascal/) hosted by [Scott Moore](http://www.moorecad.com/standardpascal/scottmoore.html)
* [Embarcadero Delphi from Wikipedia](https://en.wikipedia.org/wiki/Embarcadero_Delphi)
* [Free Pascal from Wikipedia](https://en.wikipedia.org/wiki/Free_Pascal)
* [Free Pascal - Advanced open source Pascal compiler for Pascal and Object Pascal - Home Page](http://www.freepascal.org/)
* [GNU Pascal from Wikipedia](https://en.wikipedia.org/wiki/GNU_Pascal)
* [GNU Pascal](http://www.gnu-pascal.de/gpc/h-index.html)
* [Lazarus (IDE) from Wikipedia](https://en.wikipedia.org/wiki/Lazarus_%28IDE%29)
* [Object Pascal from Wikipedia](https://en.wikipedia.org/wiki/Object_Pascal)
* [Turba Pascal from Wikipedia](https://en.wikipedia.org/wiki/Turbo_Pascal)
* [UCSD-Pascal from Wikipedia](https://en.wikipedia.org/wiki/UCSD_Pascal)
* [Virtual Pascal from Wikipedia](https://en.wikipedia.org/wiki/Virtual_Pascal)
* [comp.lang.pascal](http://groups.google.com/groups/dir?sel=usenet%3Dcomp.lang.pascal%2C&)
* An Interview with [Niklaus Wirth](Mathematician#NEWirth "Mathematician") by [Christian Timmerer](http://www-itec.uni-klu.ac.at/~timse/) with [László Böszörményi](http://de.wikipedia.org/wiki/L%C3%A1szl%C3%B3_B%C3%B6sz%C3%B6rm%C3%A9nyi), Part 2, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Blaise Pascal from Wikipedia](https://en.wikipedia.org/wiki/Blaise_Pascal)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Innovation Happens Elsewhere](http://www.dreamsongs.com/IHE/IHE-12.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Embarcadero Developer Network - Museum](http://edn.embarcadero.com/museum/)
[Antique Software: Turbo Pascal v1.0](http://edn.embarcadero.com/article/20693)
[Antique Software: Turbo Pascal v3.02](http://edn.embarcadero.com/article/20792)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Turbo Pascal - Assembly language](https://en.wikipedia.org/wiki/Turbo_Pascal#Assembly_language)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Turbo GameWorks (Open Library)](http://openlibrary.org/b/OL2753290M/Turbo_GameWorks)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Resume for Kaare Danielsen](http://www.danielsen.com/resume.shtml)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [KC Chess: Kevin & Craig's Chess Program](https://web.archive.org/web/20120411173812/http://www.csbruce.com/~csbruce/chess/) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Chess 0.5, Release 1 - 2005-05-30](http://www.moorecad.com/standardpascal/ByteChess.txt)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Byte Chess 0.5 source code](http://www.moorecad.com/standardpascal/Chess05.pas)

**[Up one Level](Languages "Languages")**







 
