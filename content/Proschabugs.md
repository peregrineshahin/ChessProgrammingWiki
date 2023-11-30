---
title: Proschabugs
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Proscha**


**Proscha**, (**Pro**jekt **Scha**ch)  

a mainframe chess program written in [PL/I](index.php?title=PL_1&action=edit&redlink=1 "PL 1 (page does not exist)") for the [IBM 370](IBM_370 "IBM 370") by a team of students of the [University of Dortmund](University_of_Dortmund "University of Dortmund"). The project was set up end of 1973 as suggested by professor [Volker Claus](Mathematician#VClaus "Mathematician"). The team was headed by [Hagen Huwig](Hagen_Huwig "Hagen Huwig") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, with [Hans-Jürgen Appelrath](Hans-J%C3%BCrgen_Appelrath "Hans-Jürgen Appelrath"), K. Behle, L. Franzen, N. Schulz, R. Schulz, W. Teschers and [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") as team members <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
The aim was not primarily to write a strong chess program but project and team work, structured programming experience, and correctness of the applied algorithms.



## Game Play


### Volker Claus


A few test games were published in the report, self-play, and one test game versus [Volker Claus](Mathematician#VClaus "Mathematician"), time control 45 minutes for the whole game, played via [TSO](https://en.wikipedia.org/wiki/Time_Sharing_Option):




```
[Event "Test Game"]
[Site "University of Dortmund"]
[Date "1974"]
[Round "1"]
[White "Volker Claus"]
[Black "Proscha"]
[Result "1-0"]

1.Nc3 d5 2.Nf3 c5 3.d4 e6 4.Bf4 cxd4 5.Nxd4 Nf6 6.e3 Bc5 7.Ndb5 O-O 
8.Nc7 Bxe3 9.Be5 Bxf2+ 10.Kxf2 Nc6 11.Bxf6 Qxc7 12.Qg4 g6 13.Qh4 Qb6+ 
14.Ke2 Qxb2 15.Qh6 Qxc2+ 16.Ke1 Qb2 17.Qg7#  1-0

```





### First GI Computer Chess


Representing the host university, Proscha played the [First GI Computer Chess Tournament](First_GI_Computer_Chess_Tournament "First GI Computer Chess Tournament") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>, lost from [Daja](Daja "Daja") and [Samiel](Samiel "Samiel"), and won from [Charlie](Charlie "Charlie"). 
In one of his algorithm lectures on [verification](https://en.wikipedia.org/wiki/Verification_and_validation_%28software%29) and [correctness](https://en.wikipedia.org/wiki/Correctness_%28computer_science%29) <a id="cite-note-6" href="#cite-ref-6">[6]</a>, [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") mentioned a [bug](Engine_Testing#bugs "Engine Testing") in Proscha despite it was extensively tested over one year, which appeared exactly during the first round versus [Daja](Daja "Daja"), where Proscha captured its own white king with its own white bishop <a id="cite-note-7" href="#cite-ref-7">[7]</a>.



## Publications


* [Hagen Huwig](Hagen_Huwig "Hagen Huwig") (**1975**). *[Bericht über eine Projektgruppe mit dem Thema Schachprogrammierung](http://www.worldcat.org/title/bericht-uber-eine-projektgruppe-mit-dem-thema-schachprogrammierung/oclc/632360799)*. Bericht Nr. 9, [University of Dortmund](University_of_Dortmund "University of Dortmund") (German)


## External Links


* [Erstes Computer-Schachturnier der Gesellschaft für Informatik](http://www.computerwoche.de/a/computer-logik-im-koeniglichen-spiel,1205123) October 17, 1975, [Computerwoche](Computerworld#Woche "Computerworld") 42/1975 (German)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Hans Decker](https://www.linkedin.com/in/hansdecker/) (**1998**). *EinBlick - Ursprünge der Dortmunder Informatik*. [pdf](http://www.cs.tu-dortmund.de/nps/de/Home/ueber_uns/Historie_der_Dortmunder_Informatik.pdf)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Hagen Huwig](Hagen_Huwig "Hagen Huwig") (**1975**). *[Bericht über eine Projektgruppe mit dem Thema Schachprogrammierung](http://www.worldcat.org/title/bericht-uber-eine-projektgruppe-mit-dem-thema-schachprogrammierung/oclc/632360799)*. Bericht Nr. 9, [University of Dortmund](University_of_Dortmund "University of Dortmund") (German)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Hagen Huwig](Hagen_Huwig "Hagen Huwig") (**1975**). *[Bericht über eine Projektgruppe mit dem Thema Schachprogrammierung](http://www.worldcat.org/title/bericht-uber-eine-projektgruppe-mit-dem-thema-schachprogrammierung/oclc/632360799)*. Bericht Nr. 9, [University of Dortmund](University_of_Dortmund "University of Dortmund") (German)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Erstes Computer-Schachturnier der Gesellschaft für Informatik](http://www.computerwoche.de/a/computer-logik-im-koeniglichen-spiel,1205123) October 17, 1975, [Computerwoche](Computerworld#Woche "Computerworld") 42/1975 (German)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Reinhard Zumkeller](Mathematician#Zumkeller "Mathematician") (**1975**). *Erstes GI Computer-Schach-Turnier, Dortmund 1975*, Bulletin, including a paper by [Konrad Zuse](Konrad_Zuse "Konrad Zuse")
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Vorlesung Algorithmen WS 2014/15](http://www-lehre.inf.uos.de/~ainf/2014/index.html), Di, 18.11.2014 Verifikation: partielle Korrektheit, Terminierung, Halteproblem (Algorithmen-Fee), [YouTube Video](https://youtu.be/D5hZ2kY8KaA?t=514) at 8:34
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> Proscha was disrespectful mentioned by [Daja](Daja "Daja") author [Ludwig Zagler](Ludwig_Zagler "Ludwig Zagler") as "bastelprogram" (tinker program) in [Schach: Die Zugmaschine](http://www.spiegel.de/spiegel/print/d-41238169.html) [Der Spiegel](https://en.wikipedia.org/wiki/Der_Spiegel) 16/1976, April 12, 1976 (German)

**[Up one Level](Engines "Engines")**







 
