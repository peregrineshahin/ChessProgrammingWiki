---
title: Sequential Logic
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* Sequential Logic**



 [](http://web.mit.edu/6.111/www/f2005/tutprobs/sequential.html) Sequential circuit <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
A **Sequential Logic** is a [digital circuit](https://en.wikipedia.org/wiki/Digital_electronics) where one or more outputs are [boolean functions](https://en.wikipedia.org/wiki/Boolean_function) of multiple inputs and the history of the outputs. In contrast to [combinatorial logic](Combinatorial_Logic "Combinatorial Logic"), a sequential logic requires [memory](Memory "Memory") to somehow feed the history of the outputs back to the inputs. Usually, for deterministic and reliable behavior considering internal [latencies](https://en.wikipedia.org/wiki/Latency_%28engineering%29) and [propagation delays](https://en.wikipedia.org/wiki/Propagation_delay), a sequential logic is [synchronous](https://en.wikipedia.org/wiki/Synchronous_logic), that is the memory only change their content on the edge of a [clock signal](https://en.wikipedia.org/wiki/Clock_signal). 



### Contents


* [1 Applications](#applications)
* [2 Sequential Rook Attack](#sequential-rook-attack)
* [3 See also](#see-also)
* [4 Publications](#publications)
* [5 External Links](#external-links)
* [6 References](#references)






Sequential logic, that is [combinatorial logic](Combinatorial_Logic "Combinatorial Logic") combined with [memory](Memory "Memory"), is the base of [Finite-state machines](https://en.wikipedia.org/wiki/Finite_state_machine), [Turing machines](index.php?title=Turing_Machine&action=edit&redlink=1 "Turing Machine (page does not exist)") as well as digital [computers](https://en.wikipedia.org/wiki/Computer).






## Sequential Rook Attack


As an further example, a sequential logic may perform the same task as mentioned in [Combinatorial Attack and Defend Map](Combinatorial_Logic#CombinatorialAttackandDefendMap "Combinatorial Logic"), but with less [gates](https://en.wikipedia.org/wiki/Logic_gates) in up to seven cycles - similar to the [bitboard techniques](Bitboards "Bitboards") like [Dumb7Fill](Dumb7Fill "Dumb7Fill"):




```C++

                                             +-------+
                                +------+     |       |
 o--/64/-- empty(square) -/64/--| 64:1 |---->|       |-----o result reliable / otherwise processing after reset
                                +------+     | Comb. |-----o A8 is attacked by white rook from south
                                   ^         | Logic |
                                +------+     |       |
 o--/64/-- wrook(square) -/64/--| 64:1 |---->|       |-->--+
                                +-----.+     |       |     |
                                   ^      o->|       |     |
                                 /6|      |  +-------+     |
                                   |      |                v
                                +--------------+           |
                                |              |           |
                                |    Latch     |<----------+
                     reset o----|              |
                                +---^----------+
                                    |
                                   clk

```

## See also


* [Belle | Hardware Move Generation](Belle#Hardware "Belle")
* [Combinatorial Logic](Combinatorial_Logic "Combinatorial Logic")
* [FPGA](FPGA "FPGA")
* [Memory](Memory "Memory")
* [Pseudorandom Number Generator](Pseudorandom_Number_Generator "Pseudorandom Number Generator")


## Publications


* [Alan H. Bond](Alan_H._Bond "Alan H. Bond") (**1987**). *Broadcasting Arrays - A Highly Parallel Computer Architecture Suitable For Easy Fabrication*. [pdf](http://www.exso.com/bc.pdf)
* [Alan Clements](http://www.scm.tees.ac.uk/users/a.clements/) (**2005**). *Sequential Logic*. [pdf](http://www.oup.com/uk/orc/bin/9780199273133/clements_ch03.pdf)


## External Links


* [Sequential logic from Wikipedia](https://en.wikipedia.org/wiki/Sequential_logic)
* [Counter from Wikipedia](https://en.wikipedia.org/wiki/Counter)
* [Shift register from Wikipedia](https://en.wikipedia.org/wiki/Shift_register)


 [Linear-feedback shift register from Wikipedia](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)
 [Cyclic redundancy check from Wikipedia](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)
* [Finite-state machine from Wikipedia](https://en.wikipedia.org/wiki/Finite-state_machine)
* [Harry Porter's Relay Computer](http://web.cecs.pdx.edu/%7Eharry/Relay/index.html)
* [Passport](Category:Passport "Category:Passport") - [Infinity Machine](http://www.allmusic.com/album/infinity-machine-mw0000587835), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 1976 lineup: [Klaus Doldinger](Category:Klaus_Doldinger "Category:Klaus Doldinger"), [Curt Cress](Category:Curt_Cress "Category:Curt Cress"), [Wolfgang Schmid](Category:Wolfgang_Schmid "Category:Wolfgang Schmid"), [Kristian Schultze](https://en.wikipedia.org/wiki/Kristian_Schultze)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Sequential Logic](http://web.mit.edu/6.111/www/f2005/tutprobs/sequential.html)

**[Up one Level](Hardware "Hardware")**







 
