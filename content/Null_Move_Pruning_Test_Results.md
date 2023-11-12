---
title: Null Move Pruning Test Results
---
**[Home](Home "Home") \* [Engine Testing](Engine_Testing "Engine Testing") \* Null Move Pruning Test Results**  

**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* [Pruning](Pruning "Pruning") \* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") \* Test Results**  



Here you can find some experimental [test results](Engine_Testing#TestResults "Engine Testing") on [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") by varying [R](Depth_Reduction_R "Depth Reduction R") on [Depth](Depth "Depth") and other features.



### Mark Lefler


One scheme tested by [Mark Lefler](Mark_Lefler "Mark Lefler") on 25 October 2007 is as follows:




```C++

R=3;
if (side to move has 2 or more pieces) and (depth>7) then R=4;

```

In a 100 game 1/1 match between [Now](Now "Now") with and without this change, the change was worth just over 50 [Elo](https://en.wikipedia.org/wiki/Elo_rating_system). I am now testing against other programs. Followup testing showed only about a 20 Elo gain, with about 100 games against a variety of opponents. Within the error of testing.



## See also


* [Late Move Reduction Test Results](Late_Move_Reduction_Test_Results "Late Move Reduction Test Results")
* [Null Move Test-Positions](Null_Move_Test-Positions "Null Move Test-Positions")


## Forum Posts


* [verified null move](http://www.talkchess.com/forum/viewtopic.php?t=28561) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 21, 2009
* [my first cluster test result with R](http://www.talkchess.com/forum/viewtopic.php?t=32152) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 29, 2010
* [value of LMR and null-move](http://www.open-chess.org/viewtopic.php?f=3&t=435) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 12, 2010
* [Extended Null-Move Reductions](http://www.talkchess.com/forum/viewtopic.php?p=367283) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), August 20, 2010 » [Null Move Reductions](Null_Move_Reductions "Null Move Reductions")


**[Up one level](Null_Move_Pruning "Null Move Pruning")**







 
