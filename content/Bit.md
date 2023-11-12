---
title: Bit
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * Bit**

[](http://ljkrakauer.com/LJK/essays/bits.htm) [PDP-6](PDP-6 "PDP-6") [flip-flop](Memory#FlipFlop "Memory") stores one bit <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Bit**,

the [basic unit](https://en.wikipedia.org/wiki/Units_of_information) of [information](https://en.wikipedia.org/wiki/Information) in [information theory](https://en.wikipedia.org/wiki/Information_theory) and [computing](https://en.wikipedia.org/wiki/Computing) - a binary digit, either 0 or 1 in the arithmetical sense, 'false' or 'true' in the boolean sense, black (dark) or white (light) as a [Color](Color "Color") in [Chess](Chess "Chess"), etc..

## Quote

by [Claude Shannon](Claude_Shannon "Claude Shannon") in *A Mathematical Theory of Communication* 1948 <a id="cite-note-2" href="#cite-ref-2">[2]</a>:

```C++
The choice of a logarithmic base corresponds to the choice of a unit for measuring information. If the base 2 is used the resulting units may be called binary digits, or more briefly bits, a word suggested by [J. W. Tukey](https://en.wikipedia.org/wiki/John_Tukey). A device with two stable positions, such as a [relay](https://en.wikipedia.org/wiki/Relay) or a [flip-flops](Memory#FlipFlop "Memory") circuit, can store one bit of information. 

```

## Aggregations

Aggregations of bits are used to code numbers, integers or floating point values, characters, codes and sets. Four bits are called a [Nibble](Nibble "Nibble") with 16 states - written as one hexadecimal digit {'0'..'9', 'A'-'F'}. A group of eight Bits, two Nibbles or one [Byte](Byte "Byte") with 256 states (e.g. unsigned numbers 0..255) is most often the smallest addressable unit in computer architectures. [Bitboards](Bitboards "Bitboards") are set-wise bit aggregations which covers all 64 [squares](Squares "Squares") of a [Chessboard](Chessboard "Chessboard").

## Bitwise Arithmetic

Bitwise addition (Modulo 2) and subtraction with aggregations of Bits without overflows can be applied by bitwise [exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations"):

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

## See also

- [Nibble](Nibble "Nibble")
- [Byte](Byte "Byte")
- [Word](Word "Word")
- [Double Word](Double_Word "Double Word")
- [Quad Word](Quad_Word "Quad Word")
- [Bitboards](Bitboards "Bitboards")
- [BitScan](BitScan "BitScan")
- [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling")
- [General Setwise Operations](General_Setwise_Operations "General Setwise Operations")

## [Least Significant One Bit](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") [Most Significant One Bit](General_Setwise_Operations#TheMostSignificantOneBitMS1B "General Setwise Operations") External Links

- [Bit from Wikipedia](https://en.wikipedia.org/wiki/Bit)
- [Bit (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Bit_%28disambiguation%29)
- [Nat (information) from Wikipedia](https://en.wikipedia.org/wiki/Nat_%28information%29)
- [Ban (information) from Wikipedia](https://en.wikipedia.org/wiki/Ban_%28information%29)
- [Qubit from Wikipedia](https://en.wikipedia.org/wiki/Qubit)
- [shannon (unit) from Wikipedia](<https://en.wikipedia.org/wiki/Shannon_(unit)>)
- [Bits](http://ljkrakauer.com/LJK/essays/bits.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Bits](http://ljkrakauer.com/LJK/essays/bits.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Claude Shannon](Claude_Shannon "Claude Shannon") (**1948**). *A Mathematical Theory of Communication*, [pdf reprint](http://cm.bell-labs.com/cm/ms/what/shannonday/shannon1948.pdf)

**[Up one level](Data "Data")**

