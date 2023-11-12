---
title: Combinatorial LogicAdder
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * Combinatorial Logic**

\[ [half adder circuit diagram](https://en.wikipedia.org/wiki/Half_adder)
A **Combinatorial Logic** (also Combinational Logic) is a [digital circuit](https://en.wikipedia.org/wiki/Digital_electronics) where one or more outputs are [boolean functions](https://en.wikipedia.org/wiki/Boolean_function) of multiple inputs. The basic boolean operations [conjunction](https://en.wikipedia.org/wiki/Logical_conjunction), [disjunction](https://en.wikipedia.org/wiki/Logical_disjunction) and [logical negation](https://en.wikipedia.org/wiki/Logical_negation) are sufficient to derive all other boolean as well as arithmetical operations. Opposed to a [sequential logic](Sequential_Logic "Sequential Logic"), outputs are not dependent on their history, that is a combinatorial logic does not require [memory](Memory "Memory").

## Contents

- [1 Implementation](#implementation)
- [2 Basic Operations](#basic-operations)
  - [2.1 AND](#and)
    - [2.1.1 Truth Table](#truth-table)
    - [2.1.2 Symbols and Circuits](#symbols-and-circuits)
  - [2.2 OR](#or)
    - [2.2.1 Truth Table](#truth-table-2)
    - [2.2.2 Symbols and Circuits](#symbols-and-circuits-2)
  - [2.3 NOT](#not)
    - [2.3.1 Truth Table](#truth-table-3)
    - [2.3.2 Symbols and Circuits](#symbols-and-circuits-3)
- [3 Derived Operations](#derived-operations)
  - [3.1 NAND](#nand)
    - [3.1.1 Truth Table](#truth-table-4)
    - [3.1.2 Symbols and Circuits](#symbols-and-circuits-4)
  - [3.2 NOR](#nor)
    - [3.2.1 Truth Table](#truth-table-5)
    - [3.2.2 Symbols and Circuits](#symbols-and-circuits-5)
  - [3.3 XOR](#xor)
    - [3.3.1 Truth Table](#truth-table-6)
    - [3.3.2 Symbols and Circuits](#symbols-and-circuits-6)
- [4 DNF and CNF](#dnf-and-cnf)
- [5 ALU](#alu)
  - [5.1 Adder](#adder)
  - [5.2 Combinatorial Attacks](#combinatorial-attacks)
    - [5.2.1 C Syntax](#c-syntax)
    - [5.2.2 Circuit](#circuit)
- [6 Publications](#publications)
- [7 See also](#see-also)
- [8 External Links](#external-links)
- [9 References](#references)

## Implementation

In hardware, combinatorial logic can either realized with hardwired [gates](https://en.wikipedia.org/wiki/Logic_gates) of certain [logic families](https://en.wikipedia.org/wiki/Logic_families) or [programmable logic devices](https://en.wikipedia.org/wiki/Programmable_logic_device). If the number of inputs is reasonable small, a once programmed [ROM](Memory#ROM "Memory") or [LUT](https://en.wikipedia.org/wiki/Lookup_table#Hardware_LUTs) can act as combinatorial logic. The inputs are the address, while one output is associated with a data-pin. In software this is like performing ALU-operations versus a memory lookup with pre-calculated outputs for all relevant inputs, related to the [space-time tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff").

## Basic Operations

Operator symbols, [truth tables](https://en.wikipedia.org/wiki/Truth_table), [IEC](https://en.wikipedia.org/wiki/International_Electrotechnical_Commission) and [ANSI](https://en.wikipedia.org/wiki/American_National_Standards_Institute) [circuit diagram](https://en.wikipedia.org/wiki/Circuit_diagram) [symbols](https://en.wikipedia.org/wiki/Electronic_symbol), as well as discrete and relay logic circuits are given.

## AND

An [AND gate](https://en.wikipedia.org/wiki/AND_gate) implements a [logical conjunction](https://en.wikipedia.org/wiki/Logical_conjunction).

```C++
a ∧ b

```

### Truth Table

|  a
|  b
|  a and b
|
| --- | --- | --- |
|  0
|  0
|  0
|
|  0
|  1
|  0
|
|  1
|  0
|  0
|
|  1
|  1
|  1
|

### Symbols and Circuits

|  |  |  |  |
| --- | --- | --- | --- |
| [IEC AND label.svg](File:IEC_AND_label.svg) | [AND ANSI Labelled.svg](File:AND_ANSI_Labelled.svg) | [Diode-AND2.png](File:Diode-AND2.png) | [Relay and.svg](File:Relay_and.svg) |

## OR

An [OR gate](https://en.wikipedia.org/wiki/OR_gate) implements a [logical disjunction](https://en.wikipedia.org/wiki/Logical_disjunction).

```C++
a ∨ b

```

### Truth Table

|  a
|  b
|  a or b
|
| --- | --- | --- |
|  0
|  0
|  0
|
|  0
|  1
|  1
|
|  1
|  0
|  1
|
|  1
|  1
|  1
|

### Symbols and Circuits

|  |  |  |  |
| --- | --- | --- | --- |
| [IEC OR label.svg](File:IEC_OR_label.svg) | [Or-gate-en.svg](File:Or-gate-en.svg) | [Diode-OR2.png](File:Diode-OR2.png) | [Relay or.svg](File:Relay_or.svg) |

## NOT

A [NOT gate](https://en.wikipedia.org/wiki/NOT_gate) or **Inverter** implements a [logical negation](https://en.wikipedia.org/wiki/Logical_negation).

```C++
¬a

```

### Truth Table

|  a
|  not a
|
| --- | --- |
|  0
|  1
|
|  1
|  0
|

### Symbols and Circuits

|  |  |  |  |
| --- | --- | --- | --- |
| [IEC NOT label.svg](File:IEC_NOT_label.svg) | [Not-gate-en.png](File:Not-gate-en.png) | [Transistor pegelumsetzer.svg](File:Transistor_pegelumsetzer.svg) | [Relay not.svg](File:Relay_not.svg) |

## Derived Operations

Concrete electronic gates often combine AND and OR with trailing NOT for so called [NAND](https://en.wikipedia.org/wiki/NAND_gate) and [NOR gates](https://en.wikipedia.org/wiki/NOR_gate). As application of [De Morgan's laws](General_Setwise_Operations#DeMorganslaws "General Setwise Operations") a NAND can also be interpreted as OR of inverted inputs, and NOR as AND of inverted inputs.

## NAND

A [NAND gate](https://en.wikipedia.org/wiki/NAND_gate) is the inversion of AND, NOT AND.

```C++
a ⊼ b

```

### Truth Table

|  a
|  b
|  not(a and b)
|
| --- | --- | --- |
|  0
|  0
|  1
|
|  0
|  1
|  1
|
|  1
|  0
|  1
|
|  1
|  1
|  0
|

### Symbols and Circuits

|  |  |  |  |
| --- | --- | --- | --- |
| [IEC NAND label.svg](File:IEC_NAND_label.svg) | [AND ANSI Labelled.svg](File:AND_ANSI_Labelled.svg) | [TTL npn nand.svg](File:TTL_npn_nand.svg) | [Relay nand.svg](File:Relay_nand.svg) |

## NOR

A [NOR gate](https://en.wikipedia.org/wiki/NOR_gate) is the inversion of OR, NOT OR.

```C++
a ⊽ b

```

### Truth Table

|  a
|  b
|  not(a or b)
|
| --- | --- | --- |
|  0
|  0
|  1
|
|  0
|  1
|  0
|
|  1
|  0
|  0
|
|  1
|  1
|  0
|

### Symbols and Circuits

|  |  |  |  |
| --- | --- | --- | --- |
| [IEC NOR label.svg](File:IEC_NOR_label.svg) | [NOR ANSI Labelled.svg](File:NOR_ANSI_Labelled.svg) | [MC717 Circuit.svg](File:MC717_Circuit.svg) | [Relay nor.svg](File:Relay_nor.svg) |

## XOR

A [XOR gate](https://en.wikipedia.org/wiki/XOR_gate) implements a [exclusive disjunction](https://en.wikipedia.org/wiki/Exclusive_disjunction), which might be derived from AND/OR/NOT, for instance from four NAND gates.

```C++
a ⊻ b

```

### Truth Table

|  a
|  b
|  a xor b
|
| --- | --- | --- |
|  0
|  0
|  0
|
|  0
|  1
|  1
|
|  1
|  0
|  1
|
|  1
|  1
|  0
|

### Symbols and Circuits

|  |  |  |  |
| --- | --- | --- | --- |
| [IEC XOR label.svg](File:IEC_XOR_label.svg) | [XOR ANSI.svg](File:XOR_ANSI.svg) | [XOR from NAND.svg](File:XOR_from_NAND.svg) | [Relay xor.svg](File:Relay_xor.svg) |

## DNF and CNF

Combinational logic can be visualized by [truth tables](https://en.wikipedia.org/wiki/Truth_table) and the construction is generally done using [disjunctive](https://en.wikipedia.org/wiki/Disjunctive_normal_form) (sum of products) or [conjunctive normal form](https://en.wikipedia.org/wiki/Conjunctive_normal_form) (products of sums), and using [boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra_%28logic%29) or [Karnaugh maps](https://en.wikipedia.org/wiki/Karnaugh_map) to simplify the expression.

## ALU

Combinatorial logic is a huge part of the [arithmetic logic unit](https://en.wikipedia.org/wiki/Arithmetic_logic_unit) (ALU) of [processors](https://en.wikipedia.org/wiki/Central_processing_unit), which provides accordant boolean logical instructions working on all [bits](Bit "Bit") of a register in parallel as mentioned in [General Setwise Operations](General_Setwise_Operations "General Setwise Operations") of [Bitboards](Bitboards "Bitboards"). Therefor each Combinatorial Logic can of course emulated in [software](Software "Software").

## Adder

A [half adder](https://en.wikipedia.org/wiki/Adder_%28electronics%29#Half_adder) performs an addition on two one-bit binary numbers. Output of an AND gate is the carry, while a XOR gate leaves the one-bit sum. A [full adder](https://en.wikipedia.org/wiki/Adder_%28electronics%29#Full_adder) with tad more gates adds three one-bit binary numbers, the third usually to feed in the carry from the previous digit, usually in [carry look ahead](https://en.wikipedia.org/wiki/Carry_lookahead_adder) architectures, such as [Kogge-Stone adder](https://en.wikipedia.org/wiki/Kogge-Stone_adder), also mentioned as [parallel prefix algorithm](Parallel_Prefix_Algorithms#KoggeStoneAdder "Parallel Prefix Algorithms").

\[
[Full Adder](https://en.wikipedia.org/wiki/Half_adder#Full_adder)

\[
[4-bit adder](https://en.wikipedia.org/wiki/Adder_%28electronics%29#Carry_look-ahead_adders) with [Carry Look Ahead](https://en.wikipedia.org/wiki/Carry_lookahead_adder)

## Combinatorial Attacks

Assuming there are 13 times 64 digital inputs from a hardware wired [chessboard](Chessboard "Chessboard"). The 13 inputs per [square](Squares "Squares") has one exclusive "one" signal for either one of the twelve [pieces](Pieces "Pieces") or an empty signal. For each square a number of attacks/defend outputs may be defined to implement a huge Combinatorial Logic as a "zero cycle" [attack table](Attack_and_Defend_Maps "Attack and Defend Maps"), i. e. output *a8 is attacked from south by white rook* as DNF (sum of products).

### C Syntax

With [C](C "C")-like operators, that is '&' for AND and '|' for OR, the DNF would look like this:

```C++

southAttackByWhiteRook(a8) ::=
    wrook(a7)
| ( empty(a7) & wrook(a6) )
| ( empty(a7) & empty(a6) & wrook(a5) )
| ( empty(a7) & empty(a6) & empty(a5) & wrook(a4) )
| ( empty(a7) & empty(a6) & empty(a5) & empty(a4) & wrook(a3) )
| ( empty(a7) & empty(a6) & empty(a5) & empty(a4) & empty(a3) & wrook(a2) )
| ( empty(a7) & empty(a6) & empty(a5) & empty(a4) & empty(a3) & empty(a2) & wrook(a1) )

```

### Circuit

The same sample as circuit f. i. in [Diode logic](https://en.wikipedia.org/wiki/Diode_logic) with 34 [diodes](https://en.wikipedia.org/wiki/Diode) and 7 [resistors](https://en.wikipedia.org/wiki/Resistor):

```C++

 Board bus
 empty                    white rook                    
 a1 a2 a3 a4 a5 a6 a7 a8  a1 a2 a3 a4 a5 a6 a7 a8      ANDs (MIN)         OR (MAX)
 |  |  |  |  |  |  |  |   |  |  |  |  |  |  |  |		   
    |  |  |  |  |  |      |  |  |  |  |  |  |			   
    o--|--|--|--|--|------|--|--|--|--|--|--|----------|<|-----o---| R1 |---o +Vcc
       o--|--|--|--|------|--|--|--|--|--|--|----------|<|-----|
       |  o--|--|--|------|--|--|--|--|--|--|----------|<|-----|  D1-D7
       |  |  o--|--|------|--|--|--|--|--|--|----------|<|-----|
       |  |  |  o--|------|--|--|--|--|--|--|----------|<|-----|
       |  |  |  |  o------|--|--|--|--|--|--|----------|<|-----|
       |  |  |  |  |      o--|--|--|--|--|--|----------|<|-----o----------|>|------o  D28
       |  |  |  |  |         |  |  |  |  |  |                                      |
       o--|--|--|--|---------|--|--|--|--|--|----------|<|-----o---| R2 |---o +Vcc |
          o--|--|--|---------|--|--|--|--|--|----------|<|-----|                   |
          |  o--|--|---------|--|--|--|--|--|----------|<|-----|  D8-D13           |
          |  |  o--|---------|--|--|--|--|--|----------|<|-----|                   |
          |  |  |  o---------|--|--|--|--|--|----------|<|-----|                   |
          |  |  |  |         o--|--|--|--|--|----------|<|-----o----------|>|------o  D29
          |  |  |  |            |  |  |  |  |                                      |
          o--|--|--|------------|--|--|--|--|----------|<|-----o---| R3 |---o +Vcc |
             o--|--|------------|--|--|--|--|----------|<|-----|                   |
             |  o--|------------|--|--|--|--|----------|<|-----|  D14-18           |
             |  |  o------------|--|--|--|--|----------|<|-----|                   |
             |  |  |            o--|--|--|--|----------|<|-----o----------|>|------o  D30
             |  |  |               |  |  |  |                                      |
             o--|--|---------------|--|--|--|----------|<|-----o---| R4 |---o +Vcc |
                o--|---------------|--|--|--|----------|<|-----|  D19-D22          |
                |  o---------------|--|--|--|----------|<|-----|                   |
                |  |               o--|--|--|----------|<|-----o----------|>|------o  D31
                |  |                  |  |  |                                      |
                o--|------------------|--|--|----------|<|-----o---| R5 |---o +Vcc |
                   o------------------|--|--|----------|<|-----|  D23-D25          |
                   |                  o--|--|----------|<|-----o----------|>|------o  D32
                   |                     |  |                                      |
                   o---------------------|--|----------|<|-----o---| R6 |---o +Vcc |
                                         |  |                  |  D26-D27          |
                                         o--|----------|<|-----o----------|>|------o  D33
                                            |                                      |  D34
                                            o------------------o----------|>|------o-->--o a8 attacked  
                                                                                   |       by white rook
                                                                                   _       from south
                                                                                  | |  R7
                                                                                  |_|
                                                                                   |
                                                                                 --o--
                                                                                  ---   gnd
                                                                                   -

```

## Publications

- [Claude Shannon](Claude_Shannon "Claude Shannon") (**1938**). *[A Symbolic Analysis of Relay and Switching Circuits](https://en.wikipedia.org/wiki/A_Symbolic_Analysis_of_Relay_and_Switching_Circuits)*. [Transactions of the AIEE](https://en.wikipedia.org/wiki/American_Institute_of_Electrical_Engineers), Vol. 57, No 12, Master's thesis 1940, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- [Victor I. Shestakov](Mathematician#VIShestakov "Mathematician") (**1941**). *Algebra of Two Poles Schemata*. [Automatics and Telemechanics](https://en.wikipedia.org/wiki/Automation_and_Remote_Control), Vol. 5, No 2
- [John P. Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1990**). *[A Depth-Decreasing Heuristic for Combinational Logic: Or How To Convert a Ripple-Carry Adder Into A Carry-Lookahead Adder Or Anything in-between](https://www.semanticscholar.org/paper/A-Depth-Decreasing-Heuristic-for-Combinational-Or-a-Fishburn/3fc16ca5e4588a5150391305a43cdc914b3d206d)*. [DAC 1990](http://dblp.uni-trier.de/db/conf/dac/dac90.html)

## See also

- [Belle | Hardware Move Generation](Belle#Hardware "Belle")
- [CHEOPS](CHEOPS "CHEOPS")
- [General Setwise Operations](General_Setwise_Operations "General Setwise Operations")
- [Sequential Logic](Sequential_Logic "Sequential Logic")

## External Links

- [Combinational logic from Wikipedia](https://en.wikipedia.org/wiki/Combinational_logic)
- [Combinational Logic & Systems Tutorial Guide](http://www.ee.surrey.ac.uk/Projects/Labview/combindex.html)
- [Proposition (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Proposition_(disambiguation)>)
- [Propositional calculus from Wikipedia](https://en.wikipedia.org/wiki/Propositional_calculus)
- [Logic gate from Wikipedia](https://en.wikipedia.org/wiki/Logic_gates)

[AND gate](https://en.wikipedia.org/wiki/AND_gate)
[OR Gate](https://en.wikipedia.org/wiki/OR_gate)
[NOT Gate](https://en.wikipedia.org/wiki/NOT_gate)
[NAND gate](https://en.wikipedia.org/wiki/NAND_gate)
[NOR gate](https://en.wikipedia.org/wiki/NOR_gate)
[XOR gate](https://en.wikipedia.org/wiki/XOR_gate)
[XNOR gate](https://en.wikipedia.org/wiki/XNOR_gate)
[Fredkin gate](https://en.wikipedia.org/wiki/Fredkin_gate)
[Toffoli gate](https://en.wikipedia.org/wiki/Toffoli_Gate) <a id="cite-note-1" href="#cite-ref-1">[1]</a>

- [Logic family from Wikipedia](https://en.wikipedia.org/wiki/Logic_families)

[Relay](https://en.wikipedia.org/wiki/Relay)
[Diode logic](https://en.wikipedia.org/wiki/Diode_logic)
[Resistor–transistor logic](https://en.wikipedia.org/wiki/Resistor%E2%80%93transistor_logic)
[Diode–transistor logic](https://en.wikipedia.org/wiki/Diode%E2%80%93transistor_logic)
[Transistor–transistor logic](https://en.wikipedia.org/wiki/Transistor%E2%80%93transistor_logic)
[Emitter-coupled logic](https://en.wikipedia.org/wiki/Emitter-coupled_logic)
[Complementary metal–oxide–semiconductor](https://en.wikipedia.org/wiki/CMOS)
[Integrated injection logic](https://en.wikipedia.org/wiki/Integrated_injection_logic)

- [Address decoder from Wikipedia](https://en.wikipedia.org/wiki/Address_decoder)
- [Lookup table from Wikipedia](https://en.wikipedia.org/wiki/Lookup_table)
- [Curved Air](https://en.wikipedia.org/wiki/Curved_Air) - [Propositions](<https://en.wikipedia.org/wiki/Air_Conditioning_(album)>) (1971), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Edward Fredkin](Edward_Fredkin "Edward Fredkin"), [Tommaso Toffoli](https://en.wikipedia.org/wiki/Tommaso_Toffoli) (**1982**). *Conservative logic*. [International Journal of Theoretical Physics](https://en.wikipedia.org/wiki/International_Journal_of_Theoretical_Physics), Vol. 21, [pdf](http://web.archive.org/web/20061017232512/http://www.digitalphilosophy.org/download_documents/ConservativeLogic.pdf)

**[Up one Level](Hardware "Hardware")**

