---
title: Negamax
---
**[Home](Home "Home") \* [Search](Search "Search") \* Negamax**


**Negamax**,  

a common way of implementing [minimax](Minimax "Minimax") and derived algorithms. Instead of using two separate subroutines for the Min player and the Max player, it passes on the negated score due to following mathematical relation:




```C++

max(a, b) == -min(-a, -b)

```

### Contents


* [1 Negated Minimax](#negated-minimax)
* [2 How to Use NegaMax](#how-to-use-negamax)
* [3 See also](#see-also)
* [4 Publications](#publications)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
* [7 References](#references)






This is how the pseudo-code of the [recursive](Recursion "Recursion") algorithm looks like. For clarity [move](Moves "Moves") [making](Make_Move "Make Move") and [unmaking](Unmake_Move "Unmake Move") is omitted.




```C++

int negaMax( int depth ) {
    if ( depth == 0 ) return evaluate();
    int max = -oo;
    for ( all moves)  {
        score = -negaMax( depth - 1 );
        if( score > max )
            max = score;
    }
    return max;
}

```

## How to Use NegaMax


Once you have your negaMax function – there are two questions which arise – i) how do you initially call negaMax, and ii) if negaMax is only returning an optimal score, then just how is it that you can know which particular move this score is related to? These two questions are related.


One calls negaMax with another root negaMax which makes the call to the negaMax proper with the default search depth. In the body of the loop of this root negaMax, in the loop which generates all the root moves – there one holds a variable as you call negaMax on the movement of each piece – and that is where you find the particular move attached to the score – in the line where you find *score > max*, right after you keep track of it by adding *max = score* – in the root negamax, that is where you pick out your move – which is what the root negaMax will return (instead of a score).


**Note!** In order for negaMax to work, your Static Evaluation function must return a score relative to the side to being evaluated, e.g. the simplest score evaluation could be: 




```C++
score = materialWeight * (numWhitePieces - numBlackPieces) * who2move 

```

where `who2move = 1` for white, and `who2move = -1` for black.



## See also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Iterative Search](Iterative_Search "Iterative Search")
* [NegaScout](NegaScout "NegaScout")
* [NegaC\*](NegaC* "NegaC*")


## Publications


* [Warren D. Smith](Warren_D._Smith "Warren D. Smith") (**1992**). *Fixed Point for Negamaxing Probability Distributions on Regular Trees*. [NEC Research Institute](https://en.wikipedia.org/wiki/NEC_Corporation_of_America), [ps](http://scorevoting.net/WarrenSmithPages/homepage/kuczma.ps) <a id="cite-note-1" href="#cite-ref-1">[1]</a>


## Forum Posts


* [NegaMax etc. (Beginner difficulity)](https://www.stmintz.com/ccc/index.php?id=16665) by Mats Forsén, [CCC](CCC "CCC"), April 08, 1998
* [Negamax algorithm??](https://www.stmintz.com/ccc/index.php?id=105506) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), April 11, 2000


## External Links


* [Negamax from Wikipedia](https://en.wikipedia.org/wiki/Negamax)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Online list of Warren D. Smith's works](http://scorevoting.net/WarrenSmithPages/homepage/works.html)

**[Up one Level](Search "Search")**







 
