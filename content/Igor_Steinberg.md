---
title: Igor Steinberg
---
**[Home](Home "Home") \* [People](People "People") \* Igor Steinberg**



 [](https://www.linkedin.com/in/igor-steinberg-89294136/) Igor Steinberg <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Igor Steinberg**,  

an American computer scientist, [solution architect](https://en.wikipedia.org/wiki/Solution_architecture), teacher, and [program manager](https://en.wikipedia.org/wiki/Program_management), with director-level [IT](https://en.wikipedia.org/wiki/Information_technology) [executive](https://en.wikipedia.org/wiki/Senior_management) experience in the higher education, government, and private sector <a id="cite-note-2" href="#cite-ref-2">[2]</a>. He holds a Ph.D. from [University of Wisconsin-Madison](https://en.wikipedia.org/wiki/University_of_Wisconsin-Madison) in 1991 on the topic of [parallel game tree search](Parallel_Search "Parallel Search") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, 
and researched and published along with his thesis advisor [Marvin Solomon](Marvin_Solomon "Marvin Solomon") on a parallel game tree search algorithm dubbed ER (Evaluate and Refute) algorithm.



### Abstract


*Abstract of Searching Game Trees in Parallel* <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```C++
We present a new parallel game-tree search algorithm. Our approach classifies a processor's available work as either mandatory (necessary for the solution) or speculative (may be necessary for the solution). Due to the nature of parallel game tree search, it is not possible to keep all processors busy with mandatory work. Our algorithm ER allows potential speculative work to be dynamically ordered, thereby reducing starvation without incurring an equivalent increase in speculative loss. Measurements of ER's performance on both random trees and trees from an actual game show that at least 16 processors can be applied profitably to a single search. These results contrast with previously published studies, which report a rapid drop-off of efficiency as the number of processors increases. 

```

### Pseudo Code


[Negamax](Negamax "Negamax") [C++](Cpp "Cpp") like pseudo code implementation of the serial algorithm ER:




```C++

struct Node {
  int val;
  bool done;
  vector<Node> childs;
};

int er(Node& p, int α, int β) {
  p.val = α;
  p.childs = generatedChilds(p);
  int d = p.childs.size();
  if (d ==0 ) return staticEval(p);
  for (int i=0; i < d; ++i) {
    int t = -evalFirst(p.childs[i], -β, -p.val);
    if (p.childs[i].done) {
      p.val = max (t, p.val);
      if (p.val >= β) return p.val;
    }
  }
  sort(p.childs);
  for (int i=0; i < d; ++i) {
    if (!p.childs[i].done) {
      int t = -refuteRest(p.childs[i], -β, -p.val);
      p.val = max (t, p.val);
      if (p.val >= β) return p.val;
    }	
  }
  return p.val;
}  
  
int evalFirst(Node& p, int α, int β) {
  p.val = α;
  p.childs = generatedChilds(p);
  int d = p.childs.size();
  if (d ==0 ) {
    p.done = true;
    return staticEval(p);
  } else {
    int t = -er(p.childs[0], -β, -p.val);
    p.val = max (t, p.val);
    p.done = (p.val >= β) || d == 1;
  }
  return p.val;
}
  
int refuteRest(Node p, int α, int β) {
  p.val = α;
  int d = p.childs.size(); // childs already generated in evalFirst
  for (int i=1; i < d; ++i) { 
    int t = -evalFirst(p.childs[i], -β, -p.val);
    if (!p.childs[i].done)
      t = -refuteRest(p.childs[i], -β, -p.val);
    p.val = max (t, p.val);
    if (p.val >= β) return p.val;
  }
  return p.val;
}

```

## Selected Publications


<a id="cite-note-5" href="#cite-ref-5">[5]</a>



* Igor Steinberg, [Marvin Solomon](Marvin_Solomon "Marvin Solomon") (**1989**). *Searching Game Trees in Parallel*. [University of Wisconsin-Madison](https://en.wikipedia.org/wiki/University_of_Wisconsin-Madison), Technical report 877, [pdf](ftp://ftp.cs.wisc.edu/pub/techreports/1989/TR877.pdf), [pdf](https://pdfs.semanticscholar.org/0814/076db01c0e5e110ef2f40539857c8e8fccd6.pdf)
* Igor Steinberg, [Marvin Solomon](Marvin_Solomon "Marvin Solomon") (**1990**). *Searching Game Trees in Parallel*. [International Conference on Parallel Processing, Volume 3, 1990](http://www.informatik.uni-trier.de/~ley/db/conf/icpp/icpp1990-3.html#SteinbergS90)
* Igor Steinberg (**1991**). *Design and Analysis of Parallel Algorithms for Game-Tree Search*. Ph.D. thesis, [University of Wisconsin-Madison](https://en.wikipedia.org/wiki/University_of_Wisconsin-Madison)


## External Links


* [Igor Steinberg | LinkedIn](https://www.linkedin.com/in/igor-steinberg-89294136/)
* [The Mathematics Genealogy Project - Igor Steinberg](http://genealogy.math.ndsu.nodak.edu/id.php?id=82285)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Igor Steinberg | LinkedIn](https://www.linkedin.com/in/igor-steinberg-89294136/)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Igor Steinberg | LinkedIn](https://www.linkedin.com/in/igor-steinberg-89294136/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> Igor Steinberg (**1991**). *Design and Analysis of Parallel Algorithms for Game-Tree Search*. Ph.D. thesis, [University of Wisconsin-Madison](https://en.wikipedia.org/wiki/University_of_Wisconsin-Madison)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> Igor Steinberg, [Marvin Solomon](Marvin_Solomon "Marvin Solomon") (**1989**). *Searching Game Trees in Parallel*. [University of Wisconsin-Madison](https://en.wikipedia.org/wiki/University_of_Wisconsin-Madison), Technical report 877, [pdf](ftp://ftp.cs.wisc.edu/pub/techreports/1989/TR877.pdf), [pdf](https://pdfs.semanticscholar.org/0814/076db01c0e5e110ef2f40539857c8e8fccd6.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [dblp: Igor Steinberg](http://dblp.uni-trier.de/pers/hd/s/Steinberg:Igor.html)

**[Up one level](People "People")**







 
