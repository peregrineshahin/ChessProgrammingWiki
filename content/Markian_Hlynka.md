---
title: Markian Hlynka
---
**[Home](Home "Home") \* [People](People "People") \* Markian Hlynka**



 [](http://webdocs.cs.ualberta.ca/~darse/Photos/Friends/) Markian Hlynka <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Markian Hlynka**,  

a Canadian computer scientist and systems analyst at [University of Alberta](University_of_Alberta "University of Alberta"). Along with [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") et al., Markian Hlynka researched and published on [search](Search "Search") enhancements and [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning"). 




### Contents


* [1 Pre-Search](#pre-search)
	+ [1.1 Abstract](#abstract)
	+ [1.2 Pseudo Code](#pseudo-code)
* [2 Fotos](#fotos)
* [3 Selected Publications](#selected-publications)
* [4 External Links](#external-links)
* [5 References](#references)






<a id="cite-note-2" href="#cite-ref-2">[2]</a>



### Abstract



```
This paper introduces the idea of pre-searching a position — searching it before [αβ](Alpha-Beta "Alpha-Beta") determines that it needs to be searched. Consider the case where an iteration of αβ search comes across a position p that needs to be searched to [depth](Depth "Depth") d1, and the [transposition table](Transposition_Table "Transposition Table") reveals that p will likely need to be searched later in that iteration to depth d2 greater than d1. Pre-searching involves speculatively searching p to depth d2, even though it has not been demonstrated that search to this depth is needed. If the gamble is successful, then additional accuracy is introduced to the search (using a result with extra search depth d2 − d1). While any search extension scheme is not without some risk, empirical results indicate that the impact on the αβ search tree size is small, but the additional accuracy that is introduced improves program performance. 

```

### Pseudo Code



```

// Assumptions:
// * search depth counts down to 0 (leaf node)
// * IDDepth is the iterative deepening search depth
// * searches are to a fixed depth
int AlphaBeta( state, depth, alpha, beta, presearch ) {
  if( TerminalNode( state ) || depth == 0 )
    return( Evaluate( state ) );

  save_alpha = alpha;
  save_beta = beta;
  tt_found = TTLook( state, &tt_depth, &tt_value, &tt_bound, &tt_iteration );

  if( tt_found == TRUE && tt_depth >= depth ) {
    if( tt_bound == LOWER ) alpha = MAX( alpha, tt_score );
    if( tt_bound == UPPER ) beta = MIN( beta, tt_score );
    if( tt_bound == ACCURATE ) alpha = beta = tt_bound;
    if( alpha >= beta ) return( alpha );
  }
  // Check for pre-search conditions
  if( tt_found && // node is in TT
      tt_iteration != IDDepth && // not updated this iteration
      // Check that entry has deeper search needs
      tt_depth + ( IDDepth - tt_iteration) >= depth ) {
    // Found a shallow node
    new_depth = tt_depth + ( IDDepth - tt_iteration );
    if( presearchFilter( newdepth, depth, tt_depth, tt_iteration, presearch ) ) {
      presearch = true;
      depth = new_depth;
    }
  }
  score = -INFINITY;
  num_moves = Generate( state, moves[] );
  for( i = 1; i <= num_moves; i++ ) {
    result = -AlphaBeta( state.moves[i], depth-1, -beta, -alpha, presearch );
    score = MAX( score, result );
    alpha = MAX( alpha, score );
    if( alpha >= beta )
      break;
  }
  // Normal TT update, but need to also save IDDepth
  TTUpdate( state, score, save_alpha, save_beta, depth, IDDepth );
  return( score );
}


bool presearchFilter( new_depth, depth, tt_depth, tt_iteration, presearch ) {
  // Do not allow a pre-search in a pre-search
  if( presearch ) return( false);

  // Ensure that we are searching deeper
  if( new_depth <= depth ) return( false );

  // Limit the amount of the search extension
  if( new_depth - depth > Risk ) return( false );

  // Prefer deep nodes close to the root
  if( tt_iteration - tt_depth > NearRoot ) return( false );

  // Prefer shallow nodes that are not close to the leaves
  if( depth < NearLeaf ) return( false );

  // Pre-search
  return( true );
}

```

## Fotos


 [](http://www.iis.sinica.edu.tw/Conference/ICGA2005/icga/img/2005_09_04/slides/IMG_0255.html) 
[10th Computer Olympiad](10th_Computer_Olympiad "10th Computer Olympiad"), [Go 9x9](10th_Computer_Olympiad#Go9x9 "10th Computer Olympiad"), [Taipei](https://en.wikipedia.org/wiki/Taipei) 2005, [Shih-Chieh Huang](Shih-Chieh_Huang "Shih-Chieh Huang") and Markian Hlynka operating  
[Go Intellect](https://www.game-ai-forum.org/icga-tournaments/program.php?id=98) and [NeuroGo](https://www.game-ai-forum.org/icga-tournaments/program.php?id=104), [Fredrik Niemelä](index.php?title=Fredrik_Niemel%C3%A4&action=edit&redlink=1 "Fredrik Niemelä (page does not exist)") watching <a id="cite-note-3" href="#cite-ref-3">[3]</a>



## Selected Publications


<a id="cite-note-4" href="#cite-ref-4">[4]</a>



* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), Markian Hlynka, [Vili Jussila](index.php?title=Vili_Jussila&action=edit&redlink=1 "Vili Jussila (page does not exist)") (**2001**). *[Temporal Difference Learning Applied to a High-Performance Game-Playing Program](https://www.semanticscholar.org/paper/Temporal-Difference-Learning-Applied-to-a-Program-Schaeffer-Hlynka/85941af287e2158bd201a633cbcc763693652c7f)*. [CGW@IJCAI 2001](Conferences#IJCAI2001 "Conferences")
* Markian Hlynka, [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2004**). *Pre-Searching*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~jonathan/publications/ai_publications/PreSearch.pdf)
* Markian Hlynka, [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2005**). *[Automatic Generation of Search Engines](https://link.springer.com/chapter/10.1007/11922155_3)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11")


## External Links


* [Markian Hlynka Full Circle | Information Services and Technology UoA](https://web.archive.org/web/20180727083721/https://ist.ualberta.ca/blog/culture/full-circle) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), July 2018)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Photo Gallery: Friends and Peers](http://webdocs.cs.ualberta.ca/~darse/Photos/Friends/) by [Darse Billings](Darse_Billings "Darse Billings")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Markian Hlynka, [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2004**). *Pre-Searching*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [CO 10 and ACG 11](http://www.iis.sinica.edu.tw/Conference/ICGA2005/icga/e1.htm), Pictures 09/04/2005
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [dblp: Markian Hlynka](https://dblp.org/pers/h/Hlynka:Markian.html)

**[Up one level](People "People")**







 
