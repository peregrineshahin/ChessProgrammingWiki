---
title: Iterative Search
---
**[Home](Home "Home") \* [Search](Search "Search") \* Iterative Search**



 [](File:SpaghettiCode.JPG) Spaghetti Code <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
The more common search structure is the [recursive](Recursion "Recursion") [depth-first search](Depth-First "Depth-First"), as used in the [Negamax algorithm](Negamax "Negamax") example. The function calls itself with a decremented depth parameter until depth reaches zero. Opposed to that the **Iterative Search** always remains on the same layer on the call [stack](Stack "Stack"). 



### Contents


* [1 Introduction](#introduction)
* [2 Considerations](#considerations)
	+ [2.1 Parallel Search](#parallel-search)
* [3 Implementations](#implementations)
	+ [3.1 Goto](#goto)
	+ [3.2 Switch](#switch)
* [4 See also](#see-also)
* [5 Forums Posts](#forums-posts)
	+ [5.1 2005 ...](#2005-...)
	+ [5.2 2010 ...](#2010-...)
	+ [5.3 2015 ...](#2015-...)
* [6 References](#references)






[Knuth](Donald_Knuth "Donald Knuth") and Moore already introduced an [iterative solution](Knuth-iterative "Knuth-iterative") of [Alpha-Beta](Alpha-Beta "Alpha-Beta") in 1975 <a id="cite-note-2" href="#cite-ref-2">[2]</a>: 




```
It is interesting to convert this recursive procedure to an iterative (non-recursive) form by a sequence of mechanical transformations, and to apply simple optimizations which preserve program correctness. The resulting procedure is surprisingly simple, but not as easy to prove correct as the recursive form.

```

## Considerations


Generally every Recursive Function can also be converted into an Iterative Search by means of replacing the function calls by jumps ([goto](C#Goto "C"), break, continue) within the function itself <a id="cite-note-3" href="#cite-ref-3">[3]</a>. The result is usually more efficient as the calling of a function is slower than just jumps within the function. The main downside however is the increased complexity and decreased readability <a id="cite-note-4" href="#cite-ref-4">[4]</a>.


In the Recursive Search the function can store local values, this doesn't work for the Iterative Structure, as all plies are using the same function. As a result a separate structure has to be maintained with all the relevant information for each ply. [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") (**2008**) <a id="cite-note-5" href="#cite-ref-5">[5]</a> also pointed out that this gives more control to the programmer as to where the stack data maps in cache, allowing for more efficient implementations. Furthermore [Onno Garms](Onno_Garms "Onno Garms") (**2010**) <a id="cite-note-6" href="#cite-ref-6">[6]</a> said that the Iterative Search favors [Profiling](index.php?title=Profiling&action=edit&redlink=1 "Profiling (page does not exist)"), as avoids all the cycles in the call tree.



### Parallel Search


Especially for the [Parallel Search Algorithm](Parallel_Search "Parallel Search") [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting") having an Iterative Search Structure is essential. It relies on threads frequently changing ownership of certain nodes, which requires full control over search stacks <a id="cite-note-7" href="#cite-ref-7">[7]</a>. Furthermore it gives more flexibility in the selection of Split Points as the information on nodes in the current search branch is freely available.



## Implementations


### Goto


[Onno Garms](Onno_Garms "Onno Garms") suggests the use of [goto](C#Goto "C") with a [switch](C#Switch "C") at the bottom to jump to the label specified in ret\_addr as applied in his engine [Onno](Onno "Onno"):




```

namespace Label
{
  enum _ {after_scout, after_research, ...};
}

class Node
{
  int alpha, beta;
  Move move;
  MoveList moves;
  int value;
  Label::_ ret_addr;
};

search ()
{
  Node* node = &d_nodes[0];
  Node* child = node+1;

recurse:
  node->moves.init();
  while ((node->move = node->moves.next()))
  {
    child->alpha = ...
    child->beta = ...
    child->ret_addr = Label::after_scout;
    ++node;
    ++child;
    goto recurse;
    // when we return here, node and child have their original values
    // and child is evaluated
after_scout:
    if (child->value < -node->alpha)
    {
      child->alpha = ...
      child->beta = ...
      child->ret_addr = Label::after_research;
      ++node
      ++child;
      goto recurse;
    after_research:
      ...
    }
    if (cutoff)
    {
      node->value = ...
      goto node_done;
    }
  }
node_done:
  --node;
  --child;
  switch (child->ret_addr)
  {
    case Label::after_research:
      goto after_research;
    ...
  }
}

```

[Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer") suggested to use a branch table, which at the beginning gets filled with addresses of all return points. The difference to the code shown by Onno Garms is that this would avoid the additional indirection of the switch statement in the end.



### Switch


[Teemu Pudas](Teemu_Pudas "Teemu Pudas") suggests a way how to use switch statements hiding behinds macros that emulate the typical function calls <a id="cite-note-8" href="#cite-ref-8">[8]</a>:




```

enum { RETURN, NEW_NODE };

##define be_recursive() \
   switch (state) { \
   case NEW_NODE
##define end_recursion() \
   default:assert(false); return best; }

##define return(foo) return best = foo, RETURN
##define recurse() return(best), NEW_NODE

##define search(depth,alpha,beta) do { \
   next->init(NEW_NODE,depth,alpha,beta); \
   state = __LINE__; \
   recurse(); \
   case __LINE__:; } while (0)


inline int Node::do_search() {

// any variable not declared inside this function is a member of Node

Node *const next = this + 1;

be_recursive(): // Please.

   gen_moves(list);
   if (list.empty()) return(in_check ? MATE_IN_ONE : DRAW);

   while (move = list.next()) {
      make(move);
      search(depth-1,-beta,-alpha);
      unmake();
      if (ret_val > best) {
         best = ret_val;
         if (best >= beta) return(best);
      }
   }
   return(best);

end_recursion();
}

int drive_search(int depth, int alpha, int beta) { // called from root_search()
   Node stack[MaxPly];
   Node *node = &stack[1]; // stack[0] would be root
   node->init(NEW_NODE,depth,alpha,beta);
   while (true) {
      switch (node->do_search()) {
      case RETURN:
         node--;
         node->ret_val = -node[1].best;
         if (node == stack) return node->ret_val;
         break;
      case NEW_NODE:
         node++;
      }
   }
}

```

[Zach Wegner](Zach_Wegner "Zach Wegner"), the author of [ZCT](ZCT "ZCT") uses a large switch branch spanning across the search function with labels for every return point <a id="cite-note-9" href="#cite-ref-9">[9]</a>.



## See also


* [ABDADA](ABDADA "ABDADA")


 [Recursive vs. Iterative Search](ABDADA#Recursion "ABDADA")
* [Backtracking - Eight Queens puzzle with Bitboards](Backtracking#8QinBitboards "Backtracking")
* [Knuth's](Donald_Knuth "Donald Knuth") [Iterative Solution](Knuth-iterative "Knuth-iterative") of [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Iteration](Iteration "Iteration")
* [Parallel Search](Parallel_Search "Parallel Search")
* [Recursion](Recursion "Recursion")


## Forums Posts


### 2005 ...


* [recusive null move in iterative search](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2071) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 25, 2005 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Iterative alpha-beta search?](https://www.stmintz.com/ccc/index.php?id=478627) by [Andrew Wagner](index.php?title=Andrew_Wagner&action=edit&redlink=1 "Andrew Wagner (page does not exist)"), [CCC](CCC "CCC"), January 11, 2006
* [Iterative DTS](http://www.talkchess.com/forum/viewtopic.php?t=14832) by [Fritz Reul](Fritz_Reul "Fritz Reul"), [CCC](CCC "CCC"), July 02, 2007
* [Interesting Scorpio design](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49618&p=187476) by [Kerwin Medina](Kerwin_Medina "Kerwin Medina"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 05, 2008
* [Iterative version of Alpha-beta instead recursive](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=264977) by Samuele Giraudo, [CCC](CCC "CCC"), May 02, 2009


### 2010 ...


* [DTS Structure](http://www.talkchess.com/forum/viewtopic.php?t=34561) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), May 28, 2010
* [True iterative search...](http://www.talkchess.com/forum/viewtopic.php?t=46175) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), November 27, 2012
* [Re: goto thread (split)](http://www.talkchess.com/forum/viewtopic.php?t=48812&start=6) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 01, 2013 » [Symbolic](Symbolic "Symbolic") <a id="cite-note-10" href="#cite-ref-10">[10]</a>
* [Non recursive perft()](http://www.talkchess.com/forum/viewtopic.php?t=53408) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 24, 2014 » [Perft](Perft "Perft")


### 2015 ...


* [Parallel iterative search function](http://www.talkchess.com/forum/viewtopic.php?t=55563) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), March 05, 2015 » [Parallel Search](Parallel_Search "Parallel Search")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Irmgard Potthoff](index.php?title=Category:Irmgard_Potthoff&action=edit&redlink=1 "Category:Irmgard Potthoff (page does not exist)") - Keine Schonkost, 2010, Überschriften aus Tageszeitungen, Teller, Messer, Gabel, Tisch (headlines from daily newspapers, plate, knife, fork, table), [Flottmann 30 hoch](http://flottmann-hallen.de/event/884/flottmann-30-hoch) - 30 years anniversary exhibition, [Flottmann-Hallen](Category:Flottmann "Category:Flottmann") in [Herne](https://en.wikipedia.org/wiki/Herne,_North_Rhine-Westphalia), [North Rhine-Westphalia](https://en.wikipedia.org/wiki/North_Rhine-Westphalia), [Germany](https://en.wikipedia.org/wiki/Germany), part of [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail") of the [Ruhr area](https://en.wikipedia.org/wiki/Ruhr), Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), September 18, 2016
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Donald Knuth](Donald_Knuth "Donald Knuth"), [Ronald W. Moore](http://dblp.uni-trier.de/pers/hd/m/Moore:Ronald_W=) (**1975**). *An analysis of alpha-beta pruning.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), 6:293–326
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [comp.lang.c FAQ list · Question 17.10](http://c-faq.com/style/stylewars.html)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Spaghetti code from Wikipedia](https://en.wikipedia.org/wiki/Spaghetti_code)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Interesting Scorpio design](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49618&p=187476#p187458) by [H.G. Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 05, 2008
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: DTS Structure](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=351576&t=34561) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), May 28, 2010
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [See remark on Recursion](ABDADA#Recursion "ABDADA") by [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") on [recursive](Recursion "Recursion") versus [iterative](Iteration "Iteration") implementation of [ABDADA](ABDADA "ABDADA")
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: Interesting Scorpio design](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49618&p=187476#p187476) by [Teemu Pudas](Teemu_Pudas "Teemu Pudas"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 05, 2008
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: DTS Structure](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=351606&t=34561) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), May 29, 2010
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Considered harmful from Wikipedia](https://en.wikipedia.org/wiki/Considered_harmful)

**[Up one level](Search "Search")**







 
