---
title: Algol
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Languages](Languages "Languages") * Algol**

\[ Algol rotation <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**ALGOL** (ALGOrithmic Language)

is a family of [imperative](https://en.wikipedia.org/wiki/Imperative_programming) computer programming languages developed jointly by a committee of European and American computer scientists in a meeting in 1958 at [ETH Zurich](ETH_Zurich "ETH Zurich") ([Algol 58](https://en.wikipedia.org/wiki/ALGOL_58)).
Algol 58 introduced code blocks and the begin and end pairs for delimiting them. Two years later, [Algol 60](https://en.wikipedia.org/wiki/ALGOL_60) was specified, as the result of a meeting in Paris in January 1960 by 13 European and American scientists, [Peter Naur](https://en.wikipedia.org/wiki/Peter_Naur), [John Backus](https://en.wikipedia.org/wiki/John_Backus), [John McCarthy](John_McCarthy "John McCarthy"), [Friedrich L. Bauer](Mathematician#Bauer "Mathematician"), [Adriaan van Wijngaarden](Mathematician#AvWijngaarden "Mathematician"), et al. Algol 60 became the standard for the publication of algorithms and had a profound effect on future language development, it was the first language implementing [nested function](https://en.wikipedia.org/wiki/Nested_function) definitions with [lexical scope](https://en.wikipedia.org/wiki/Lexical_scope#Static_versus_dynamic_scoping).
[Algol 68](https://en.wikipedia.org/wiki/ALGOL_68) was designed by [IFIP](IFIP "IFIP"), while [Niklaus Wirth](Mathematician#NEWirth "Mathematician") based his own [Algol W](https://en.wikipedia.org/wiki/ALGOL_W) <a id="cite-note-2" href="#cite-ref-2">[2]</a> on Algol 60 before moving to develop [Pascal](Pascal "Pascal").

## Algol W

A boolean procedure in Algol W from the chess program [Awit](Awit "Awit") by [Tony Marsland](Tony_Marsland "Tony Marsland") <a id="cite-note-3" href="#cite-ref-3">[3]</a> :

```C++

11662 LOGICAL PROCEDURE CLEAR(INTEGER VALUE SQA, SQF, SQT);
11663 BEGIN
11664   INTEGER DIR;
11665   LOGICAL FREE;
11666   FREE := FALSE;
11667   DIR := BOTV(EDGE, OFFSET(SQF)−OFFSET(SQT));
11668   IF DIR ~= 0 THEN BEGIN
11669     FREE := TRUE;
11670     IF SQA ~= SQF AND
11671        DIR = BOTV(EDGE, OFFSET(SQA)−OFFSET(SQT))
11672     THEN FREE := FALSE;
11673     FOR SQ := SQF+DIR STEP DIR UNTIL SQT−DIR
11674     DO IF FREE AND BRD(SQ) ~= 0
11675       THEN FREE := FALSE;
11676   END;
11677   FREE
11678 END CLEAR;

```

## Algol Chess Programs

- [Category Algol](Category:Algol "Category:Algol")

## Selected Publications

- [Klaus Samelson](Mathematician#Samelson "Mathematician"), [Friedrich L. Bauer](Mathematician#Bauer "Mathematician") (**1960**). *[Sequential Formula Translation](http://portal.acm.org/citation.cfm?id=366968)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 3 No. 2
- [Christopher Strachey](Christopher_Strachey "Christopher Strachey"), [Maurice Wilkes](Mathematician#MVWilkes "Mathematician") (**1961**). *[Some Proposals for Improving the Efficiency of ALGOL 60](https://dl.acm.org/doi/10.1145/366813.366816)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 4, No. 11
- [V. I. Sobel'man](http://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=63222), [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") (**1962**). *[Realization of recursive procedures in the language of AlGOL-60](http://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=zvmmf&paperid=7886&option_lang=eng)*. (Реализация Рекурсивных Процедур В Языке Алгол-60) [Zhurnal Vychislitel'noi Matematiki i Matematicheskoi Fiziki](http://www.mathnet.ru/php/archive.phtml?jrnid=zvmmf&option_lang=eng&wshow=statlist), Vol. 2, No. 2

## External Links

- [ALGOL from Wikipedia](https://en.wikipedia.org/wiki/ALGOL)
- [ALGOL 58 from Wikipedia](https://en.wikipedia.org/wiki/ALGOL_58)
- [ALGOL 60 from Wikipedia](https://en.wikipedia.org/wiki/ALGOL_60)
- [ALGOL 68 from Wikipedia](https://en.wikipedia.org/wiki/ALGOL_68)
- [ALGOL W from Wikipedia](https://en.wikipedia.org/wiki/ALGOL_W)
- [History of ALGOL — Software Preservation Group](http://www.softwarepreservation.org/projects/ALGOL) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Algol 58 implementations and dialects — Software Preservation Group](http://www.softwarepreservation.org/projects/ALGOL/algol58impl) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Algol 60 implementations and dialects — Software Preservation Group](http://www.softwarepreservation.org/projects/ALGOL/algol60impl) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Algol 68 implementations and dialects — Software Preservation Group](http://www.softwarepreservation.org/projects/ALGOL/algol68impl) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Трансляторы с Алгола-60 - № 45, 1999](http://www.osp.ru/cw/1999/45/38679/) [Computerworld Россия](Computerworld#Russia "Computerworld") (Russian)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Eclipsing binary star animation, created by [Stanlekub](https://commons.wikimedia.org/wiki/User:Stanlekub) with [Blender](<https://en.wikipedia.org/wiki/Blender_(software)>) and the [GIMP](https://en.wikipedia.org/wiki/GIMP), [Algol (Stern) Wikipedia.de](<https://de.wikipedia.org/wiki/Algol_(Stern)#Bedeckungsver%C3%A4nderlicher_Stern>), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Algol W Language Description](http://webdocs.cs.ualberta.ca/%7Etony/Public/Awit-Wita-ComputerChess/AlgolwSupport/algolw.pdf) (pdf)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Awit Source code in Algol W](http://webdocs.cs.ualberta.ca/%7Etony/Public/Awit-Wita-ComputerChess/AlgolwSupport/awit.pdf) by [Tony Marsland](Tony_Marsland "Tony Marsland") (pdf)

**[Up one Level](Languages "Languages")**

