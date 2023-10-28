---
title: OpenCL
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Languages](Languages "Languages") \* OpenCL**


**OpenCL**, (Open Computing Language)  

an open standard for cross-platform, task-based as well as data-based parallel programming of CPUs, [GPUs](GPU "GPU"), [FPGAs](FPGA "FPGA"), [DSPs](https://en.wikipedia.org/wiki/Digital_signal_processor), including the [C99](C "C") based programming language OpenCL C. OpenCL C forbids [recursion](Recursion "Recursion"), and omits [function pointers](https://en.wikipedia.org/wiki/Function_pointer), [bit fields](https://en.wikipedia.org/wiki/Bit_field) and [variable-length](https://en.wikipedia.org/wiki/Variable-length_array) [arrays](Array "Array"), but has fixed-length vector types, supporting [SIMD instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") if available on the target platforms. OpenCL 2.0 adds features like nested parallelism and shared virtual memory, version 2.1 extends OpenCL C to a subset of C++14. OpenCL 3.0 makes version 1.2 functionality a mandatory baseline with 2.x and 3.x as optional features and replaces 'OpenCL C++' with 'C++ for OpenCL' as a subset of C++17. OpenCL is maintained by the [nonprofit](https://en.wikipedia.org/wiki/Nonprofit_organization) technology consortium [Khronos Group](https://en.wikipedia.org/wiki/Khronos_Group), adopted by [Apple](index.php?title=Apple&action=edit&redlink=1 "Apple (page does not exist)")<a id="cite-note-1" href="#cite-ref-1">[1]</a>, [Intel](Intel "Intel"), [Qualcomm](https://en.wikipedia.org/wiki/Qualcomm), [AMD](AMD "AMD"), [Nvidia](Nvidia "Nvidia"), [Altera](https://en.wikipedia.org/wiki/Altera), [Samsung](https://en.wikipedia.org/wiki/Samsung), [Vivante](https://en.wikipedia.org/wiki/Vivante_Corporation), [Imagination Technologies](https://en.wikipedia.org/wiki/Imagination_Technologies) and [ARM](index.php?title=ARM&action=edit&redlink=1 "ARM (page does not exist)").



### Contents


* [1 Specifications](#specifications)
* [2 OpenCL to Vulkan](#opencl-to-vulkan)
* [3 Chess Projects](#chess-projects)
* [4 Publications](#publications)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
* [7 References](#references)






* [OpenCL 1.2 Specification](https://www.khronos.org/registry/OpenCL/specs/opencl-1.2.pdf)
* [OpenCL 1.2 Reference](https://www.khronos.org/registry/OpenCL//sdk/1.2/docs/man/xhtml/)
* [OpenCL 2.0 Specification](https://www.khronos.org/registry/OpenCL/specs/opencl-2.0.pdf)
* [OpenCL 2.0 C Language Specification](https://www.khronos.org/registry/OpenCL/specs/2.2/pdf/OpenCL_C.pdf)
* [OpenCL 2.0 Reference](https://www.khronos.org/registry/OpenCL//sdk/2.0/docs/man/xhtml/)
* [OpenCL 3.0 Specifications](https://www.khronos.org/registry/OpenCL/specs/3.0-unified/pdf/)


## OpenCL to Vulkan


The OpenGL graphics API specified by Khronos Group is deprecated in favor for [Vulkan](https://en.wikipedia.org/wiki/Vulkan), since Vulkan and OpenCL v1.2/v2.x share [SPIR-V](https://en.wikipedia.org/wiki/Standard_Portable_Intermediate_Representation) as an intermediate representation it is possible to cross-compile OpenCL code via SPIR-V to run on Vulkan enabled devices <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



## Chess Projects


* [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
* [Oscar](index.php?title=Oscar&action=edit&redlink=1 "Oscar (page does not exist)"), a [Perft](Perft "Perft") project by [Steven Edwards](Steven_Edwards "Steven Edwards")
* [Zeta](Zeta "Zeta") by [Srdja Matovic](Srdja_Matovic "Srdja Matovic")


## Publications


* [Aaftab Munshi](https://www.informit.com/authors/bio/ba2cf654-0769-47a6-9d60-01b6e6da4a60), [Benedict Gaster](http://www.informit.com/authors/bio/056a0573-0374-4183-96db-e94b962d2046), [Timothy Mattsonm](http://www.informit.com/authors/bio/203bb6b7-d0bb-48ca-984c-a627e8b33ce2), James Fung, [Dan Ginsburg](http://www.informit.com/authors/bio/5bd00f25-b8c1-49de-85a0-423e49663d06) (**2011**). *[OpenCL Programming Guide](http://www.informit.com/store/opencl-programming-guide-9780321749642?w_ptgrevartcl=Programming+with+OpenCL+C_1732873)*. [InformIT](https://en.wikipedia.org/wiki/Pearson_Education) <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Wolfram Schenck](https://scholar.google.de/citations?user=ByAvYg4AAAAJ&hl=en) (**2017**). *OpenCL Basics*. [slides as pdf](https://www.fz-juelich.de/SharedDocs/Downloads/IAS/JSC/EN/slides/opencl/opencl-03-basics.pdf?__blob=publicationFile)


## Forum Posts


* [Zeta, a chess engine in OpenCL](http://www.talkchess.com/forum/viewtopic.php?t=33315) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), March 17, 2010
* [OpenCL perft() Technical Issues](http://www.talkchess.com/forum/viewtopic.php?t=53439) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 26, 2014


## External Links


* [Khronos - OpenCL Conformant Products](https://www.khronos.org/conformance/adopters/conformant-products/opencl)
* [OpenCL - The open standard for parallel programming of heterogeneous systems](https://www.khronos.org/opencl/)
* [OpenCL from Wikipedia](https://en.wikipedia.org/wiki/OpenCL)
* [SimpleOpenCL - a library created to reduce the amount of host code needed to write an OpenCL program. - Google Project Hosting](https://code.google.com/archive/p/simple-opencl/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [OpenGL, OpenCL deprecated in favor of Metal 2 in macOS 10.14 Mojave](https://appleinsider.com/articles/18/06/04/opengl-opencl-deprecated-in-favor-of-metal-2-in-macos-1014-mojave)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [clspv](https://github.com/google/clspv) by [Google](index.php?title=Google&action=edit&redlink=1 "Google (page does not exist)") on GitHub
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Programming with OpenCL C | Writing a Data-Parallel Kernel Using OpenCL C | InformIT](http://www.informit.com/articles/article.aspx?p=1732873)

**[Up one Level](Languages "Languages")**







 
