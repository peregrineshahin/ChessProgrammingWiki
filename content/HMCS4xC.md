---
title: HMCS4xC
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * HMCS4xC**

**HMCS4xC**, (HMCS44, HMCS44C, HD44801)

a family of [Hitachi](https://en.wikipedia.org/wiki/Hitachi) [4-bit](https://en.wikipedia.org/wiki/4-bit_computing) [CMOS](https://en.wikipedia.org/wiki/CMOS)[microcontroller](https://en.wikipedia.org/wiki/Microcontroller) (MCU) .
The single-chip controller series provide various amounts of [ROM](Memory#ROM "Memory") of 10-bit words (code and pattern) and [RAM](Memory#RAM "Memory") of up to 160 [nibbles](Nibble "Nibble"),
[parallel I(O](https://en.wikipedia.org/wiki/Parallel_I/O) aimed for driving dot matrix [LCD](https://en.wikipedia.org/wiki/Liquid-crystal_display), timer/counter and [interrupt controller](https://en.wikipedia.org/wiki/Programmable_interrupt_controller).

## Architecture

The HMCS44C has four nibble registers and two 1-bit registers (carry, status) available to the programmer.
The status flag latches the result of arithmetical or logical operations (none zero, overflow), and affects conditional branch instructions.
The 4-bit accumulator (A) is expanded by carry bit for ALU input and output, carry can bet set, reset and tested using appropriate instructions.
Register B acts as sub-accumulator or counter, while the X and Y registers are used to address RAM, organized as file (X 0..9) and digit (Y 0..0x0F), Y further addresses 1-bit discrete I/O.
Both index registers may by stacked by corresponding spy-registers, SPX and SPY.
The ROM address range is divided by 5 page bits (page 0-31) with 64 10-bit words each, addressed by the 11-bit [program counter](https://en.wikipedia.org/wiki/Program_counter).
A stack of four registers (ST1-ST4) is used to call subroutines by the CAL instructions and to return by RTN <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## See also

- [160 Nibble Challenge](Mini_Chess#160_Nibble_Challenge "Mini Chess")
- [SAM](SAM "SAM")

## Chess Programs

- [Category:HMCS4xC](Category:HMCS4xC "Category:HMCS4xC")

## Publications

- [Steve A. Money](https://www.amazon.com/Steve-A-Money/e/B001KIF2N6/ref=dp_byline_cont_book_1) (**1990, 2014**). *[Microprocessor Data Book](https://books.google.de/books/about/Microprocessor_Data_Book.html?id=e0SoBQAAQBAJ&redir_esc=y)*. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press)

## Manuals

- [Hitachi HD44801](https://cdn.datasheetspdf.com/pdf-down/H/D/4/HD44801_Hitachi.pdf) (pdf)

## External Links

- [HMCS40 - Hitachi - WikiChip](https://en.wikichip.org/wiki/hitachi/hmcs40)
- [Hitachi HD44801](https://www.schach-computer.info/wiki/index.php?title=Hitachi_HD44801) - [Schachcomputer.info Wiki](https://www.schach-computer.info/wiki/index.php?title=Hauptseite_En)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Hitachi HD44801](https://cdn.datasheetspdf.com/pdf-down/H/D/4/HD44801_Hitachi.pdf) (pdf)

**[Up one Level](Hardware "Hardware")**

