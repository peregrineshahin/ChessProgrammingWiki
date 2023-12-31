---
title: Stockfish NNUEHalfKA
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* [Stockfish](Stockfish "Stockfish") \* NNUE**



 [](File:Sfnnue.png) Stockfish NNUE Logo <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Stockfish NNUE**,  

a Stockfish branch by [Hisayori Noda](Hisayori_Noda "Hisayori Noda") aka Nodchip, which uses [Efficiently Updatable Neural Networks](NNUE "NNUE") - stylized as **ƎUИИ** or reversed as **NNUE** - to replace its standard [evaluation](Stockfish#Evaluation "Stockfish").
NNUE, introduced in 2018 by [Yu Nasu](Yu_Nasu "Yu Nasu") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, 
were previously successfully applied in [Shogi](Shogi "Shogi") evaluation functions embedded in a Stockfish based search <a id="cite-note-3" href="#cite-ref-3">[3]</a>, such as [YaneuraOu](YaneuraOu "YaneuraOu") <a id="cite-note-4" href="#cite-ref-4">[4]</a>,
and [Kristallweizen](Kristallweizen "Kristallweizen") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. YaneuraOu's author [Motohiro Isozaki](Motohiro_Isozaki "Motohiro Isozaki") made an unbelievable prediction that NNUE can help to increase Stockfish strength by around 100 points, almost one year before revealing <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>.
In 2019, Nodchip incorporated NNUE into Stockfish 10 - as a proof of concept, and with the intention to give something back to the Stockfish community <a id="cite-note-8" href="#cite-ref-8">[8]</a>.
After support and announcements by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)") in May 2020 <a id="cite-note-9" href="#cite-ref-9">[9]</a> 
and subsequent enhancements, Stockfish NNUE was established and recognized. In summer 2020, with more people involved in [testing](Engine_Testing "Engine Testing") and [training](Learning "Learning"), 
the computer chess community bursts out enthusiastically due to its rapidly raising [playing strength](Playing_Strength "Playing Strength") with different networks trained using a mixture of [supervised](Supervised_Learning "Supervised Learning") and [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") methods. Despite the approximately halved search speed, Stockfish NNUE became stronger than its original <a id="cite-note-10" href="#cite-ref-10">[10]</a>. 


In August 2020, [Fishtest](Stockfish#Fishtest "Stockfish") revealed Stockfish NNUE was stronger than the classical one at least 80 Elo <a id="cite-note-11" href="#cite-ref-11">[11]</a>. In July 2020, the playing code of NNUE was put into the official Stockfish repository as a branch for further development and examination. In August that playing code merged to the master branch and become an official part of the engine. The training code still remained in Nodchip's repository <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a> for a while then replaced by [PyTorch](https://en.wikipedia.org/wiki/PyTorch) NNUE training<a id="cite-note-14" href="#cite-ref-14">[14]</a><a id="cite-note-15" href="#cite-ref-15">[15]</a>. On September 02, 2020, **Stockfish 12** was released with a huge jump in playing strength due to the introduction of [NNUE](NNUE "NNUE") and further tuning <a id="cite-note-16" href="#cite-ref-16">[16]</a>.



### HalfKP


The so called **HalfKP** structure consists of two halves covering input layer and first hidden layer, each half of the input layer associated to one of the two [kings](King "King"), cross coupled with the side to move or not to move halves of the first hidden layer.
For each either black or white king placement, the 10 none king pieces on their particular squares are the boolean {0,1} inputs, along with a relict from Shogi piece drop (BONA\_PIECE\_ZERO), 
64 x (64 x 10 + 1) = 41,024 inputs for each half, which are multiplied by a 16-bit integer weight vector for 256 outputs per half, in total, 256 x 41,024 = 10,502,144 weights.
As emphasized by [Ronald de Man](Ronald_de_Man "Ronald de Man") in a [CCC](CCC "CCC") forum discussion <a id="cite-note-18" href="#cite-ref-18">[18]</a>, 
the input weights are arranged in such a way, that [color flipped](Color_Flipping "Color Flipping") king-piece configurations in both halves share the same index.
However, and that seems also a relict from Shogi with its [180 degrees rotational](https://en.wikipedia.org/wiki/Rotational_symmetry) 9x9 board symmetry, instead of [vertical flipping](Vertical_Flipping "Vertical Flipping") (xor 56), [rotation](Flipping_Mirroring_and_Rotating#Rotationby180degrees "Flipping Mirroring and Rotating") is applied (xor 63) <a id="cite-note-19" href="#cite-ref-19">[19]</a>.


The efficiency of [NNUE](NNUE "NNUE") is due to [incremental update](Incremental_Updates "Incremental Updates") of the input layer outputs in [make](Make_Move "Make Move") and [unmake move](Unmake_Move "Unmake Move"),
where only a tiny fraction of its neurons need to be considered in case of none king moves.
The remaining three layers with 2x256x32, 32x32 and 32x1 weights are computational less expensive, hidden layers apply a [ReLu activation](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) <a id="cite-note-20" href="#cite-ref-20">[20]</a> <a id="cite-note-21" href="#cite-ref-21">[21]</a>, best calculated using appropriate [SIMD instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") performing fast [8-bit](Byte "Byte")/[16-bit](Word "Word") integer vector arithmetic, like [MMX](MMX "MMX"), [SSE2](SSE2 "SSE2") or [AVX2](AVX2 "AVX2") on [x86](X86 "X86")/[x86-64](X86-64 "X86-64"), or, if available, [AVX-512](AVX-512 "AVX-512").



 [](File:StockfishNNUELayers.png) 
NNUE layers in action <a id="cite-note-22" href="#cite-ref-22">[22]</a>


Explanation by [Ronald de Man](Ronald_de_Man "Ronald de Man") <a id="cite-note-23" href="#cite-ref-23">[23]</a>, who did the Stockfish NNUE port to [CFish](CFish "CFish") <a id="cite-note-24" href="#cite-ref-24">[24]</a>:




```C++
The accumulator has a "white king" half and a "black king" half, where each half is a 256-element vector of 16-bit ints, which is equal to the sum of the weights of the "active" (pt, sq, ksq) features  plus a 256-element vector of 16-bit biases.

```


```C++
The "transform" step of the NNUE evaluation forms a 512-element vector of 8-bit ints where the first half is formed from the 256-element vector of the side to move and the second half is formed from the 256-element vector of the other side. In this step the 16-bit elements are clipped/clamped to a value from 0 to 127. This is the output of the input layer.

```


```C++
This 512-element vector of 8-bit ints is then multiplied by a 32x512 matrix of 8-bit weights to get a 32-element vector of 32-bit ints, to which a vector of 32-bit biases is added. The sum vector is divided by 64 and clipped/clamped to a 32-element vector of 8-bit ints from 0 to 127. This is the output of the first hidden layer.

```


```C++
The resulting 32-element vector of 8-bit ints is multiplied by a 32x32 matrix of 8-bit weights to get a 32-element vector of 32-bit ints, to which another vector of 32-bit biases is added. These ints are again divided by 64 and clipped/clamped to 32 8-bit ints from 0 to 127. This is the output of the second hidden layer.

```


```C++
This 32-element vector of 8-bits ints is then multiplied by a 1x32 matrix of 8-bit weights (i.e. the inner product of two vectors is taken). This produces a 32-bit value to which a 32-bit bias is added. This gives the output of the output layer.

```


```C++
The output of the output layer is divided by FV_SCALE = 16 to produce the NNUE evaluation. SF's evaluation then take some further steps such as adding a Tempo bonus (even though the NNUE evaluation inherently already takes into account the side to move in the "transform" step) and scaling the evaluation towards zero as rule50_count() approaches 50 moves.

```

### HalfKA


In subsequent Stockfish versions the network architecture was further improved by [Tomasz Sobczyk](Tomasz_Sobczyk "Tomasz Sobczyk") et al.. The **HalfKA** architecture uses 12x64x64 = 45056 inputs for each of the 12 piece types times 64 squares for each of the 64 own king squares, times two, for both the side to move and other side perspective, further using the [vertical flip](Vertical_Flipping "Vertical Flipping") instead of the HalfKP rotate. 
**HalfKAv2** as applied in Stockfish **14** saves some space considering the king square redundancy using 11x64x64 = 45056 inputs per side, mapped to a 2x520 linear feature transformer <a id="cite-note-25" href="#cite-ref-25">[25]</a> <a id="cite-note-26" href="#cite-ref-26">[26]</a> <a id="cite-note-27" href="#cite-ref-27">[27]</a>, further feeding 8x2 outputs of this feature transformer directly to the output for better learning of unbalanced material configurations <a id="cite-note-28" href="#cite-ref-28">[28]</a>. Another improvement was using eight 512x2->16->32->1 output sub-networks discriminated by (piece\_count-1) div 4 in the 0 to 7 range
<a id="cite-note-29" href="#cite-ref-29">[29]</a>.



 [](File:HalfKAv2.png) 
HalfKAv2 architecture by [Tomasz Sobczyk](Tomasz_Sobczyk "Tomasz Sobczyk") <a id="cite-note-30" href="#cite-ref-30">[30]</a>



## Network


Networks were built by volunteers, uploaded into [Fishtest](Stockfish#Fishtest "Stockfish") for testing. 
Networks with good test results are released officially on the Fishtest website <a id="cite-note-31" href="#cite-ref-31">[31]</a> with average speed of 2 weeks per network <a id="cite-note-32" href="#cite-ref-32">[32]</a>. 
After long discussing the best way to publish networks with Stockfish <a id="cite-note-33" href="#cite-ref-33">[33]</a>, the developing team decided to embed the default network into Stockfish binaries, making sure NNUE always works as well as bringing more convenience to users.


In late 2020, [Gary Linscott](Gary_Linscott "Gary Linscott") started an implementation of the Stockfish NNUE training in [PyTorch](https://en.wikipedia.org/wiki/PyTorch) <a id="cite-note-34" href="#cite-ref-34">[34]</a> <a id="cite-note-35" href="#cite-ref-35">[35]</a> using [GPU](GPU "GPU") resources to efficiently train networks. 
Further, the collaboration with the [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") team in February 2021 <a id="cite-note-36" href="#cite-ref-36">[36]</a> payed off, in providing billions of positions to train the new networks <a id="cite-note-37" href="#cite-ref-37">[37]</a>.



## Hybrid


In August 2020 a new patch changed Stockfish NNUE into a hybrid engine: it uses NNUE evaluation only on quite balanced material positions, otherwise uses the classical one. It could speed up to 10% and gain 20 Elo <a id="cite-note-38" href="#cite-ref-38">[38]</a>. At that point, NNUE helped to increase already around 100 Elo for Stockfish. In the same month, Stockfish changed the default mode of using evaluation functions from classic to hybrid one, the last step to completely accept NNUE.



## Strong Points


### For Users


* Runs with CPU only, and doesn't require expensive [video cards](https://en.wikipedia.org/wiki/Video_card), as well the need for installing drivers and 3rd specific libraries. Thus it is much easier to install (compared to engines using [deep](Neural_Networks#Deep "Neural Networks") [convolutional neural networks](Neural_Networks#Convolutional "Neural Networks"), such as [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")) and suitable for almost all modern computers. Using a [GPU](GPU "GPU") is even not practical for that small net - host-device-latency aka. kernel-launch-overhead <a id="cite-note-39" href="#cite-ref-39">[39]</a> <a id="cite-note-40" href="#cite-ref-40">[40]</a> to a then underemployed GPU are not sufficient for the intended [NPS](Nodes_per_Second "Nodes per Second") range <a id="cite-note-41" href="#cite-ref-41">[41]</a>
* Releases with only one network (via [UCI](UCI "UCI") options), that help to delete users' confusion from finding, selecting and setting up. The network is selected carefully from [Fishtest](Stockfish#Fishtest "Stockfish")


### For Developers


* Requires small training sets. Some high score networks can be built with the effort of one or a few people within a few days. It doesn't require the massive computing from a supercomputer and/or from community
* Doesn’t require complicated systems such as a sophisticated [client-server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model) to train networks. Just a single binary from Nodchip’ repo is enough to train
* The NNUE code is independent and can be separated easily from the rest and integrated to other engines <a id="cite-note-42" href="#cite-ref-42">[42]</a>


Being attracted by new advantages as well as being encouraged by some impressive successes, many developers joined or continued to work. The [Official Stockfish](#Source) repository shows the numbers of commits, ideas increased significantly after merging NNUE.



## Elo gain


[Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele") has created a graph to show how Stockfish gains Elo with NNUE after a year:<a id="cite-note-43" href="#cite-ref-43">[43]</a>



 [](File:NNEUOneYearEloGain.png) 
## Suggestions


In reply to [Unai Corzo](index.php?title=Unai_Corzo&action=edit&redlink=1 "Unai Corzo (page does not exist)"), [Motohiro Isozaki](Motohiro_Isozaki "Motohiro Isozaki") aka Yaneurao, suggested 3 techniques that applied successfully to Shogi and can be brought back to Stockfish NNUE and may improve it another 100 - 200 Elo <a id="cite-note-44" href="#cite-ref-44">[44]</a> <a id="cite-note-45" href="#cite-ref-45">[45]</a>:



* Optimizing all parameters together by [stochastic optimization](https://en.wikipedia.org/wiki/Stochastic_optimization)
* Switching between multi-evaluation functions, according to [game phases](Game_Phases "Game Phases")
* Automatic generation of [opening book](Opening_Book "Opening Book") on the fly


## See also


* [Category: Neural Network Engines](Category:NN "Category:NN")
* [Fat Fritz 2.0](Fat_Fritz#Fat_Fritz_2 "Fat Fritz")
* [Neural Networks](Neural_Networks "Neural Networks")
* [NNUE](NNUE "NNUE")
* [Winter](Winter "Winter")


## Forum Posts


### 2020 ...


### January ...


* [The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 07, 2020 » [Shogi](Shogi "Shogi")
* [Stockfish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74058) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), May 31, 2020 » [Stockfish](Stockfish "Stockfish")
* [Stockfish NN release (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74059) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), May 31, 2020
* [nnue-gui 1.0 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74212) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), June 17, 2020
* [stockfish-NNUE as grist for SF development?](https://groups.google.com/d/msg/fishcooking/rIAO2SXkT00/48-DFzHFBwAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), June 21, 2020


### July


* [How strong is Stockfish NNUE compared to Leela..](https://groups.google.com/d/msg/lczero/BvhCa-muLt0/ZzINQk_vCQAJ) by OmenhoteppIV, [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), July 13, 2020 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
* [Can the sardine! NNUE clobbers SF](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74484) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), July 16, 2020
* [End of an era?](https://groups.google.com/d/msg/fishcooking/8j68W3GL6Q0/__Pf0FRNCQAJ) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), July 20, 2020
* [Sergio Vieri second net is out](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74520) by Sylwy, [CCC](CCC "CCC"), July 21, 2020
* [NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), July 21, 2020


 [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=1) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 23, 2020
 [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=5) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 24, 2020
 [Re: NNUE accessible explanation](#Continue) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), August 03, 2020
* [Stockfisch NNUE macOS binary requested](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74564) by Steppenwolf, [CCC](CCC "CCC"), July 25, 2020
* [Stockfish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74565) by Lion, [CCC](CCC "CCC"), July 25, 2020
* [7000 games testrun of SFnnue sv200724\_0123 finished](https://groups.google.com/d/msg/fishcooking/fDY3dXqxgIQ/7Z5V0tATAQAJ) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), July 26, 2020
* [SF-NNUE going forward...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74585) by Zenmastur, [CCC](CCC "CCC"), July 27, 2020
* [New sf+nnue play-only compiles](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74594) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), July 27, 2020
* [Stockfish+NNUEsv +80 Elo vs Stockfish 17jul !!](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=33622)  by Kris, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 28, 2020
* [LC0 vs. NNUE - some tech details...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74607) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), July 29, 2020 » [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero")
* [Stockfish NNUE and testsuites](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74613) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), July 29, 2020
* [Stockfish NNue [download ]](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74627) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 30, 2020


### August


* [Repository for Stockfish+NNUE Android Builds](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74654) by [AdminX](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), August 02, 2020
* [SF NNUE Problem](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74666) by [Stephen Ham](index.php?title=Stephen_Ham&action=edit&redlink=1 "Stephen Ham (page does not exist)"), [CCC](CCC "CCC"), August 03, 2020
* [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=8) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), August 03, 2020 » [NNUE accessible explanation](#NNUEaccExp)
* [[NNUE] Worker update on fishtest](https://groups.google.com/d/msg/fishcooking/6OI3AejYvpQ/dNmluMLBAgAJ) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), August 03, 2020
* [this will be the merge of a lifetime : SF 80 Elo+](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74680) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), August 04, 2020


 [Re: this will be the merge of a lifetime : SF 80 Elo+](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74680&start=22) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), August 04, 2020 
* [You can now look inside NNUE and look at its Per square value estimation](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74681) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), August 04, 2020
* [Is this SF NN almost like 20 MB book?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74683) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), August 04, 2020
* [NNUE evaluation merged in master](https://groups.google.com/d/msg/fishcooking/Kzw1W_Yr1d8/YNEmCqIyBAAJ) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), August 06, 2020
* [What happens with my hyperthreading?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74705) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 06, 2020 » [Thread](Thread "Thread")
* [Stockfish NNUE style](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74722) by Rowen, [CCC](CCC "CCC"), August 08, 2020
* [SF NNUE training questions](http://www.talkchess.com/forum3/viewtopic.php?t=74739) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), August 10, 2020
* [Progress of Stockfish in 6 days](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74765) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 12, 2020
* [Neural Networks weights type](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74777) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), August 13, 2020
* [Don't understand NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74780) by Lucasart, [CCC](CCC "CCC"), August 14, 2020
* [SF+NNUE reach the ceiling?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74901) by Corres, [CCC](CCC "CCC"), August 27, 2020
* [The most stupid idea by the Stockfish Team](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74933) by Damir, [CCC](CCC "CCC"), August 30, 2020


### September


* [Stockfish 12](https://groups.google.com/d/msg/fishcooking/TJHsiI61yQ4/liQoZ-AzAgAJ) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 02, 2020
* [Stockfish 12 is released today!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74974) by Nay Lin Tun, [CCC](CCC "CCC"), September 02, 2020
* [Stockfish 12 has arrived!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74978) by daniel71, [CCC](CCC "CCC"), September 02, 2020
* [AVX2 optimized SF+NNUE and processor temperature](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75008) by corres, [CCC](CCC "CCC"), September 05, 2020 » [AVX2](AVX2 "AVX2")


### October


* [BONA\_PIECE\_ZERO](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75296) by [elcabesa](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), October 04, 2020
* [SF NNUE/Classical](https://groups.google.com/d/msg/fishcooking/yjh1YOxy7nw/rJA6u1ODAAAJ) by [Fauzi](Fauzi_Akram_Dabat "Fauzi Akram Dabat"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), October 05, 2020
* [How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 17, 2020 » Stockfish NNUE, [Scorpio NNUE](Scorpio#NNUE "Scorpio")
* [Embedding Stockfish NNUE to ANY CHESS ENGINE: YouTube series](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75418) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 17, 2020 » [BBC NNUE](BBC#NNUE "BBC")
* [NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 23, 2020 » [NNUE Structure](#NNUE_Structure)


 [Re: NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=7) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), October 23, 2020
 [Re: NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=9) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), October 23, 2020
### 2021 ...


* [Shouldn't positional attributes drive SF's NNUE input features (rather than king position)?](https://groups.google.com/g/fishcooking/c/cad1MGSdpU4/m/Ury4iBqSBgAJ) by [Nick Pelling](Nick_Pelling "Nick Pelling"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), January 10, 2021
* [stockfish NNUE question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76381) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 21, 2021
* [256 in NNUE?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76437) by Ted Wong, [CCC](CCC "CCC"), January 28, 2021
* [Fat Fritz 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76537) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), February 09, 2021 » [Fat Fritz 2.0](Fat_Fritz#Fat_Fritz_2 "Fat Fritz")
* [NNUE Research Project](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76833) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), March 10, 2021 » [NNUE](NNUE "NNUE")
* [NNUE ranking](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76844) by Jim Logan, [CCC](CCC "CCC"), March 12, 2021
* [Stockfish with new NNUE architecture and bigger net released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77344) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), May 19, 2021 <a id="cite-note-46" href="#cite-ref-46">[46]</a>
* [Why NNUE trainer requires an online qsearch on each training position?](http://talkchess.com/forum3/viewtopic.php?f=7&t=79020) by [nkg114mc](index.php?title=Nkg114mc&action=edit&redlink=1 "Nkg114mc (page does not exist)"), [CCC](CCC "CCC"), January 01, 2022


## External Links


### Basics


* [Stockfish NNUE – The Complete Guide](http://yaneuraou.yaneu.com/2020/06/19/stockfish-nnue-the-complete-guide/), June 19, 2020 (Japanese and English)
* [3 technologies in shogi AI that could be used for chess AI](http://yaneuraou.yaneu.com/2020/08/21/3-technologies-in-shogi-ai-that-could-be-used-for-chess-ai/) by [Motohiro Isozaki](Motohiro_Isozaki "Motohiro Isozaki"), August 21, 2020
* [Stockfish NNUE Wiki](https://www.qhapaq.org/shogi/shogiwiki/stockfish-nnue/)
* [NNUE merge · Issue #2823 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/issues/2823) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), July 25, 2020 <a id="cite-note-47" href="#cite-ref-47">[47]</a>
* [Stockfish Evaluation Guide](https://hxim.github.io/Stockfish-Evaluation-Guide/?p=nnue) <a id="cite-note-48" href="#cite-ref-48">[48]</a>
* [NNUE Guide (nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub)](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md) hosted by [Gary Linscott](Gary_Linscott "Gary Linscott")
* [One year of NNUE.... · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/discussions/3628) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), July 26, 2021


### Source


* [GitHub - Official-stockfish](https://github.com/official-stockfish/Stockfish)
* [GitHub - nodchip/Stockfish: UCI chess engine](https://github.com/nodchip/Stockfish) by [Nodchip](Hisayori_Noda "Hisayori Noda")
* [GitHub - vondele/Stockfish at nnue-player-wip](https://github.com/vondele/Stockfish/tree/nnue-player-wip) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele")
* [GitHub - tttak/Stockfish: UCI chess engine](https://github.com/tttak/Stockfish)
* [GitHub - joergoster/Stockfish-NNUE: UCI Chess engine Stockfish with an Efficiently Updatable Neural-Network-based evaluation function](https://github.com/joergoster/Stockfish-NNUE) hosted by [Jörg Oster](index.php?title=J%C3%B6rg_Oster&action=edit&redlink=1 "Jörg Oster (page does not exist)")
* [GitHub - FireFather/sf-nnue: Stockfish NNUE (efficiently updateable neural network)](https://github.com/FireFather/sf-nnue) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt")
* [GitHub - FireFather/nnue-gui: basic windows application for using nodchip's stockfish-nnue software](https://github.com/FireFather/nnue-gui) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt")


### Networks


* [Neural Net download and statistics](https://tests.stockfishchess.org/nns)
* [Index of /~sergio-v/nnue](https://www.comp.nus.edu.sg/~sergio-v/nnue/) by [Sergio Vieri](Sergio_Vieri "Sergio Vieri")


### Rating


* [Regression Tests](https://github.com/glinscott/fishtest/wiki/Regression-Tests)
* [Stockfish 14 64-bit 8CPU](http://ccrl.chessdom.com/ccrl/404/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Stockfish%2014%2064-bit%208CPU#Stockfish_14_64-bit_8CPU) in [CCRL Blitz](CCRL "CCRL")
* [Stockfish 12 64-bit](http://ccrl.chessdom.com/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Stockfish%2012%2064-bit#Stockfish_12_64-bit) in [CCRL Blitz](CCRL "CCRL")
* [Stockfish+NNUE 150720 64-bit 4CPU](http://computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Stockfish%2BNNUE%20150720%2064-bit%204CPU#Stockfish%2BNNUE_150720_64-bit_4CPU) in [CCRL Blitz](CCRL "CCRL")


### Misc


* [Stockfish from Wikipedia](https://en.wikipedia.org/wiki/Stockfish)
* [Nue from Wikipedia](https://en.wikipedia.org/wiki/Nue)
* [Senri Kawaguchi](Category:Senri_Kawaguchi "Category:Senri Kawaguchi") - [The Quarantuned Music Festival](https://ameliaray.net/quarantuned), May 2020, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


  
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Stockfish NNUE Logo from [GitHub - nodchip/Stockfish: UCI chess engine](https://github.com/nodchip/Stockfish) by [Nodchip](Hisayori_Noda "Hisayori Noda")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Yu Nasu](Yu_Nasu "Yu Nasu") (**2018**). *ƎUИИ Efficiently Updatable Neural-Network based Evaluation Functions for Computer Shogi*. Ziosoft Computer Shogi Club, [pdf](https://github.com/ynasu87/nnue/blob/master/docs/nnue.pdf) (Japanese with English abstract) [GitHub - asdfjkl/nnue translation](https://github.com/asdfjkl/nnue)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 07, 2020
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [GitHub - yaneurao/YaneuraOu: YaneuraOu is the World's Strongest Shogi engine(AI player), WCSC29 1st winner, educational and USI compliant engine](https://github.com/yaneurao/YaneuraOu)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [GitHub - Tama4649/Kristallweizen: 第29回世界コンピュータ将棋選手権 準優勝のKristallweizenです。](https://github.com/Tama4649/Kristallweizen/)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [将棋ソフト開発者がStockfishに貢献する日 The day when shogi software developers contribute to Stockfish](http://yaneuraou.yaneu.com/2019/06/24/%E5%B0%86%E6%A3%8B%E3%82%BD%E3%83%95%E3%83%88%E9%96%8B%E7%99%BA%E8%80%85%E3%81%8Cstockfish%E3%81%AB%E8%B2%A2%E7%8C%AE%E3%81%99%E3%82%8B%E6%97%A5/) by [Motohiro Isozaki](Motohiro_Isozaki "Motohiro Isozaki"), June 2019
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [shogi engine developer claims he can make Stockfish stronger](https://www.reddit.com/r/chess/comments/cltich/shogi_engine_developer_claims_he_can_make/), [Reddit](Computer_Chess_Forums "Computer Chess Forums"), August 2019
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Stockfish NNUE – The Complete Guide](http://yaneuraou.yaneu.com/2020/06/19/stockfish-nnue-the-complete-guide/), June 19, 2020 (Japanese and English)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Stockfish NN release (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74059) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), May 31, 2020
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Can the sardine! NNUE clobbers SF](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74484) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), July 16, 2020
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Introducing NNUE Evaluation](https://blog.stockfishchess.org/post/625828091343896577/introducing-nnue-evaluation), August 06, 2020
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [NNUE merge · Issue #2823 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/issues/2823) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), July 25, 2020
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [GitHub - nodchip/Stockfish: UCI chess engine](https://github.com/nodchip/Stockfish) by [Nodchip](Hisayori_Noda "Hisayori Noda")
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Pytorch NNUE training](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75724) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), November 08, 2020
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Why NNUE trainer requires an online qsearch on each training position?](http://talkchess.com/forum3/viewtopic.php?f=7&t=79020) by [nkg114mc](index.php?title=Nkg114mc&action=edit&redlink=1 "Nkg114mc (page does not exist)"), [CCC](CCC "CCC"), January 01, 2022
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Stockfish 12](https://blog.stockfishchess.org/post/628172810852925440/stockfish-12), The Stockfish Team, [Stockfish Blog](https://blog.stockfishchess.org/), September 02, 2020
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=1) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 23, 2020
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Re: NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=7) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), October 23, 2020
19. <a id="cite-ref-19" href="#cite-note-19">↑</a> [NNUE eval rotate vs mirror · Issue #3021 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/issues/3021) by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), August 17, 2020
20. <a id="cite-ref-20" href="#cite-note-20">↑</a> [Stockfish/halfkp\_256x2-32-32.h at master · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/blob/master/src/nnue/architectures/halfkp_256x2-32-32.h#L42)
21. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Stockfish/clipped\_relu.h at master · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/blob/master/src/nnue/layers/clipped_relu.h#L82)
 22. <a id="cite-ref-22" href="#cite-note-22">↑</a> Image courtesy Roman Zhukov, revised version of the image posted in [Re: Stockfish NN release (NNUE)](http://talkchess.com/forum3/viewtopic.php?f=2&t=74059&start=139) by Roman Zhukov, [CCC](CCC "CCC"), June 17, 2020, labels corrected October 23, 2020, see [Re: NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=1) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 23, 2020 
23. <a id="cite-ref-23" href="#cite-note-23">↑</a> [Re: NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=9) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), October 23, 2020
24. <a id="cite-ref-24" href="#cite-note-24">↑</a> [Cfish/nnue.c at master · syzygy1/Cfish · GitHub](https://github.com/syzygy1/Cfish/blob/master/src/nnue.c)
25. <a id="cite-ref-25" href="#cite-note-25">↑</a> [New NNUE architecture and net · official-stockfish/Stockfish@e8d64af · GitHub](https://github.aom/official-stockfish/Stockfish/commit/e8d64af1230fdac65bb0da246df3e7abe82e0838)
26. <a id="cite-ref-26" href="#cite-note-26">↑</a> [Update default net to nn-8a08400ed089.nnue by Sopel97 · Pull Request #3474 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3474)
27. <a id="cite-ref-27" href="#cite-note-27">↑</a> [HalfKAv2 feature set | nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md#halfkav2-feature-set)
28. <a id="cite-ref-28" href="#cite-note-28">↑</a> [A part of the feature transformer directly forwarded to the output | nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md#a-part-of-the-feature-transformer-directly-forwarded-to-the-output)
29. <a id="cite-ref-29" href="#cite-note-29">↑</a> [Multiple PSQT outputs and multiple subnetworks | nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md#multiple-psqt-outputs-and-multiple-subnetworks)
 30. <a id="cite-ref-30" href="#cite-note-30">↑</a> [HalfKAv2.png](https://user-images.githubusercontent.com/8037982/118656988-553a1700-b7eb-11eb-82ef-56a11cbebbf2.png) Image courtesy by [Tomasz Sobczyk](Tomasz_Sobczyk "Tomasz Sobczyk") 
31. <a id="cite-ref-31" href="#cite-note-31">↑</a> [Neural Net download and statistics](https://tests.stockfishchess.org/nns)
32. <a id="cite-ref-32" href="#cite-note-32">↑</a> [One year of NNUE.... · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/discussions/3628#discussioncomment-1047323) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), July 26, 2021
33. <a id="cite-ref-33" href="#cite-note-33">↑</a> [Improve dealing with the default net? Issue ##3030 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/issues/3030) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), August 19, 2020
34. <a id="cite-ref-34" href="#cite-note-34">↑</a> [Pytorch NNUE training](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75724) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), November 08, 2020
35. <a id="cite-ref-35" href="#cite-note-35">↑</a> [GitHub - glinscott/nnue-pytorch: NNUE (Chess evaluation) trainer in Pytorch](https://github.com/glinscott/nnue-pytorch)
36. <a id="cite-ref-36" href="#cite-note-36">↑</a> [Stockfish 13](https://groups.google.com/g/fishcooking/c/AzYDbbv-Coo) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), February 19, 2021
37. <a id="cite-ref-37" href="#cite-note-37">↑</a> [Stockfish 14](https://stockfishchess.org/blog/2021/stockfish-14/), The Stockfish Team, July 02, 2021
38. <a id="cite-ref-38" href="#cite-note-38">↑</a> [NNUE evaluation threshold by MJZ1977 · Pull Request #2916 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/2916), August 06, 2020
39. <a id="cite-ref-39" href="#cite-note-39">↑</a> [AB search with NN on GPU...](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74771) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), August 13, 2020 » [GPU](GPU "GPU")
40. <a id="cite-ref-40" href="#cite-note-40">↑</a> [kernel launch latency - CUDA / CUDA Programming and Performance - NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/kernel-launch-latency/62455) by LukeCuda, June 18, 2018
41. <a id="cite-ref-41" href="#cite-note-41">↑</a> [stockfish with graphics card](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74702) by h1a8, [CCC](CCC "CCC"), August 06, 2020
42. <a id="cite-ref-42" href="#cite-note-42">↑</a> [NNUE Engines](NNUE#NNUE_Engines "NNUE")
43. <a id="cite-ref-43" href="#cite-note-43">↑</a> [One year of NNUE.... · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/discussions/3628#discussioncomment-1047728) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), July 26, 2021
44. <a id="cite-ref-44" href="#cite-note-44">↑</a> [3 technologies in shogi AI that could be used for chess AI](http://yaneuraou.yaneu.com/2020/08/21/3-technologies-in-shogi-ai-that-could-be-used-for-chess-ai/), [Motohiro Isozaki](Motohiro_Isozaki "Motohiro Isozaki"), August 2020
45. <a id="cite-ref-45" href="#cite-note-45">↑</a> [GitHub - NNUE ideas and discussion (post-merge). #2915](https://github.com/official-stockfish/Stockfish/issues/2915#issuecomment-678112885,), August 2020
46. <a id="cite-ref-46" href="#cite-note-46">↑</a> [Update default net to nn-8a08400ed089.nnue by Sopel97 · Pull Request #3474 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3474) by [Tomasz Sobczyk](Tomasz_Sobczyk "Tomasz Sobczyk")
47. <a id="cite-ref-47" href="#cite-note-47">↑</a> [An info](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74560) by Sylwy, [CCC](CCC "CCC"), July 25, 2020
48. <a id="cite-ref-48" href="#cite-note-48">↑</a> [You can now look inside NNUE and look at its Per square value estimation](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74681) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), August 04, 2020

**[Up one Level](Stockfish "Stockfish")**







 
