---
title: GPU
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * GPU**

\[ [Nvidia Tesla](https://en.wikipedia.org/wiki/Nvidia_Tesla) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**GPU** (Graphics Processing Unit),

a specialized processor initially intended for fast [image processing](https://en.wikipedia.org/wiki/Image_processing). GPUs may have more raw computing power than general purpose [CPUs](https://en.wikipedia.org/wiki/Central_processing_unit) but need a specialized and parallelized way of programming. [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") has proven that a [Best-first](Best-First "Best-First") [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") (MCTS) with [deep learning](Deep_Learning "Deep Learning") methodology will work with GPU architectures.

## History

In the 1970s and 1980s RAM was expensive and Home Computers used custom graphics chips to operate directly on registers/memory without a dedicated frame buffer resp. texture buffer, like [TIA](https://en.wikipedia.org/wiki/Television_Interface_Adaptor)in the [Atari VCS](Atari_8-bit "Atari 8-bit") gaming system, [GTIA](https://en.wikipedia.org/wiki/CTIA_and_GTIA)+[ANTIC](https://en.wikipedia.org/wiki/ANTIC) in the [Atari 400/800](Atari_8-bit "Atari 8-bit") series, or [Denise](https://en.wikipedia.org/wiki/Original_Chip_Set#Denise)+[Agnus](https://en.wikipedia.org/wiki/Original_Chip_Set#Agnus) in the [Commodore Amiga](Amiga "Amiga") series. The 1990s would make 3D graphics and 3D modeling more popular, especially for video games. Cards specifically designed to accelerate 3D math, such as [SGI Impact](<https://en.wikipedia.org/wiki/IMPACT_(computer_graphics)>) (1995) in 3D graphics-workstations or [3dfx Voodoo](https://en.wikipedia.org/wiki/3dfx#Voodoo_Graphics_PCI) (1996) for playing 3D games on PCs, emerged. Some game engines could use instead the [SIMD-capabilities](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") of CPUs such as the [Intel](Intel "Intel") [MMX](MMX "MMX") instruction set or [AMD's](AMD "AMD") [3DNow!](X86#3DNow.21 "X86") for [real-time rendering](https://en.wikipedia.org/wiki/Real-time_computer_graphics). Sony's 3D capable chip [GTE](<https://en.wikipedia.org/wiki/PlayStation_technical_specifications#Graphics_processing_unit_(GPU)>) used in the PlayStation (1994) and Nvidia's 2D/3D combi chips like [NV1](https://en.wikipedia.org/wiki/NV1) (1995) coined the term GPU for 3D graphics hardware acceleration. With the advent of the [unified shader architecture](https://en.wikipedia.org/wiki/Unified_shader_model), like in Nvidia [Tesla](<https://en.wikipedia.org/wiki/Tesla_(microarchitecture)>) (2006), ATI/AMD [TeraScale](<https://en.wikipedia.org/wiki/TeraScale_(microarchitecture)>) (2007) or Intel [GMA X3000](https://en.wikipedia.org/wiki/Intel_GMA#GMA_X3000) (2006), GPGPU frameworks like [CUDA](https://en.wikipedia.org/wiki/CUDA) and [OpenCL](OpenCL "OpenCL") emerged and gained in popularity.

## GPU in Computer Chess

There are in main three approaches how to use a GPU for Chess:

- As an accelerator in [Lc0](Leela_Chess_Zero "Leela Chess Zero"): run a neural network for position evaluation on GPU.
- Offload the search in [Zeta](Zeta "Zeta"): run a parallel game tree search with move generation and position evaluation on GPU.
- As an hybrid in [perft_gpu](http://www.talkchess.com/forum3/viewtopic.php?t=64983&start=4#p729152): expand the game tree to a certain degree on CPU and offload to GPU to compute the sub-tree.

## GPU Chess Engines

- [Category:GPU](Category:GPU "Category:GPU")

## GPGPU

Early efforts to leverage a GPU for general-purpose computing required reformulating computational problems in terms of graphics primitives via graphics APIs like [OpenGL](https://en.wikipedia.org/wiki/OpenGL) or [DirextX](https://en.wikipedia.org/wiki/DirectX), followed by first GPGPU frameworks such as [Sh/RapidMind](https://en.wikipedia.org/wiki/Lib_Sh) or [Brook](https://en.wikipedia.org/wiki/BrookGPU) and finally [CUDA](https://en.wikipedia.org/wiki/CUDA) and [OpenCL](https://www.chessprogramming.org/OpenCL).

## Khronos OpenCL

[OpenCL](OpenCL "OpenCL") specified by the [Khronos Group](https://en.wikipedia.org/wiki/Khronos_Group) is widely adopted across all kind of hardware accelerators from different vendors.

- [List of OpenCL Conformant Products](https://www.khronos.org/conformance/adopters/conformant-products/opencl)

- [OpenCL 1.2 Specification](https://www.khronos.org/registry/OpenCL/specs/opencl-1.2.pdf)

- [OpenCL 1.2 Reference](https://www.khronos.org/registry/OpenCL//sdk/1.2/docs/man/xhtml/)

- [OpenCL 2.0 Specification](https://www.khronos.org/registry/OpenCL/specs/opencl-2.0.pdf)

- [OpenCL 2.0 C Language Specification](https://www.khronos.org/registry/OpenCL/specs/2.2/pdf/OpenCL_C.pdf)

- [OpenCL 2.0 Reference](https://www.khronos.org/registry/OpenCL//sdk/2.0/docs/man/xhtml/)

- [OpenCL 3.0 Specifications](https://www.khronos.org/registry/OpenCL/specs/3.0-unified/pdf/)

## AMD

[AMD](AMD "AMD") supports language frontends like OpenCL, HIP, C++ AMP and with OpenMP offload directives. It offers with [ROCm](https://rocmdocs.amd.com/en/latest/) its own parallel compute platform.

- [AMD OpenCL Developer Community](https://community.amd.com/t5/opencl/bd-p/opencl-discussions)
- [ROCm Homepage](https://rocm.github.io/)
- [AMD OpenCL Programming Guide](http://developer.amd.com/wordpress/media/2013/07/AMD_Accelerated_Parallel_Processing_OpenCL_Programming_Guide-rev-2.7.pdf)
- [AMD OpenCL Optimization Guide](http://developer.amd.com/wordpress/media/2013/12/AMD_OpenCL_Programming_Optimization_Guide2.pdf)
- [RDNA Instruction Set](https://gpuopen.com/wp-content/uploads/2019/08/RDNA_Shader_ISA_5August2019.pdf)
- [Vega Instruction Set](https://developer.amd.com/wp-content/resources/Vega_Shader_ISA_28July2017.pdf)

## Apple

Since macOS 10.14 Mojave a transition from OpenCL to [Metal](<https://en.wikipedia.org/wiki/Metal_(API)>) is recommended by [Apple](index.php?title=Apple&action=edit&redlink=1 "Apple (page does not exist)").

- [Apple OpenCL Developer](https://developer.apple.com/opencl/)
- [Apple Metal Developer](https://developer.apple.com/metal/)
- [Apple Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html)
- [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf)

## Intel

Intel supports OpenCL with implementations like BEIGNET and NEO for different GPU architectures and the [oneAPI](<https://en.wikipedia.org/wiki/OneAPI_(compute_acceleration)>) platform with [DPC++](https://en.wikipedia.org/wiki/DPC++) as frontend language.

- [Intel Developer Zone](https://www.intel.com/content/www/us/en/developer/overview.html#gs.pu62bi)
- [Intel oneAPI Programming Guide](https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top.html)

## Nvidia

[CUDA](https://en.wikipedia.org/wiki/CUDA) is the parallel computing platform by [Nvidia](Nvidia "Nvidia"). It supports language frontends like C, C++, Fortran, OpenCL and offload directives via [OpenACC](https://en.wikipedia.org/wiki/OpenACC) and [OpenMP](https://en.wikipedia.org/wiki/OpenMP).

- [Nvidia CUDA Zone](https://developer.nvidia.com/cuda-zone)
- [Nvidia PTX ISA](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html)
- [Nvidia CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/index.html)
- [Nvidia CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)
- [Nvidia CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)

## Further

- [Vulkan](https://en.wikipedia.org/wiki/Vulkan#Planned_features) (OpenGL sucessor of Khronos Group)
- [DirectCompute](https://en.wikipedia.org/wiki/DirectCompute) (Microsoft)
- [C++ AMP](https://en.wikipedia.org/wiki/C%2B%2B_AMP) (Microsoft)
- [OpenACC](https://en.wikipedia.org/wiki/OpenACC) (offload directives)
- [OpenMP](https://en.wikipedia.org/wiki/OpenMP) (offload directives)

## Hardware Model

A common scheme on GPUs with unified shader architecture is to run multiple threads in [SIMT](https://en.wikipedia.org/wiki/Single_instruction,_multiple_threads) fashion and a multitude of SIMT waves on the same [SIMD](https://en.wikipedia.org/wiki/SIMD) unit to hide memory latencies. Multiple processing elements (GPU cores) are members of a SIMD unit, multiple SIMD units are coupled to a compute unit, with up to hundreds of compute units present on a discrete GPU. The actual SIMD units may have architecture dependent different numbers of cores (SIMD8, SIMD16, SIMD32), and different computation abilities - floating-point and/or integer with specific bit-width of the FPU/ALU and registers. There is a difference between a vector-processor with variable bit-width and SIMD units with fix bit-width cores. Different architecture white papers from different vendors leave room for speculation about the concrete underlying hardware implementation and the concrete classification as [hardware architecture](https://en.wikipedia.org/wiki/Flynn%27s_taxonomy). Scalar units present in the compute unit perform special functions the SIMD units are not capable of and MMAC units (matrix-multiply-accumulate units) are used to speed up neural networks further.

Vendor Terminology
|  AMD Terminology  |  Nvidia Terminology
|
|  Compute Unit  |  Streaming Multiprocessor
|
|  Stream Core  |  CUDA Core
|
|  Wavefront  |  Warp
|

### Hardware Examples

Nvidia GeForce GTX 580 ([Fermi](https://en.wikipedia.org/wiki/Fermi_%28microarchitecture%29)) <a id="cite-note-2" href="#cite-ref-2">[2]</a><a id="cite-note-3" href="#cite-ref-3">[3]</a>

- 512 CUDA cores @1.544GHz
- 16 SMs - Streaming Multiprocessors
- organized in 2x16 CUDA cores per SM
- Warp size of 32 threads

AMD Radeon HD 7970 ([GCN)](https://en.wikipedia.org/wiki/Graphics_Core_Next)<a id="cite-note-4" href="#cite-ref-4">[4]</a><a id="cite-note-5" href="#cite-ref-5">[5]</a>

- 2048 Stream cores @0.925GHz
- 32 Compute Units
- organized in 4xSIMD16, each SIMT4, per Compute Unit
- Wavefront size of 64 work-items

### Wavefront and Warp

Generalized the definition of the Wavefront and Warp size is the amount of threads executed in SIMT fashion on a GPU with unified shader architecture.

## Programming Model

A [parallel programming model](https://en.wikipedia.org/wiki/Parallel_programming_model) for GPGPU can be [data-parallel](https://en.wikipedia.org/wiki/Data_parallelism), [task-parallel](https://en.wikipedia.org/wiki/Task_parallelism), a mixture of both, or with libraries and offload-directives also [implicitly-parallel](https://en.wikipedia.org/wiki/Implicit_parallelism). Single GPU threads (work-items in OpenCL) contain the kernel to be computed and are coupled to a work-group, one or multiple work-groups form the NDRange to be executed on the GPU device. The members of a work-group execute the same kernel, can be usually synchronized and have access to the same scratch-pad memory, with an architecture limit of how many work-items a work-group can hold and how many threads can run in total concurrently on the device.

Terminology
|  OpenCL Terminology  |  CUDA Terminology
|
|  Kernel  |  Kernel
|
|  Compute Unit  |  Streaming Multiprocessor
|
|  Processing Element  |  CUDA Core
|
|  Work-Item  |  Thread
|
|  Work-Group  |  Block
|
|  NDRange  |  Grid
|

## Thread Examples

Nvidia GeForce GTX 580 (Fermi, CC2) <a id="cite-note-6" href="#cite-ref-6">[6]</a>

- Warp size: 32
- Maximum number of threads per block: 1024
- Maximum number of resident blocks per multiprocessor: 32
- Maximum number of resident warps per multiprocessor: 64
- Maximum number of resident threads per multiprocessor: 2048

AMD Radeon HD 7970 (GCN) <a id="cite-note-7" href="#cite-ref-7">[7]</a>

- Wavefront size: 64
- Maximum number of work-items per work-group: 1024
- Maximum number of work-groups per compute unit: 40
- Maximum number of Wavefronts per compute unit: 40
- Maximum number of work-items per compute unit: 2560

## Memory Model

OpenCL offers the following memory model for the programmer:

- \_\_private - usually registers, accessable only by a single work-item resp. thread.
- \_\_local - scratch-pad memory shared across work-items of a work-group resp. threads of block.
- \_\_constant - read-only memory.
- \_\_global - usually VRAM, accessable by all work-items resp. threads.

Terminology
|  OpenCL Terminology  |  CUDA Terminology
|
|  Private Memory  |  Registers
|
|  Local Memory  |  Shared Memory
|
|  Constant Memory  |  Constant Memory
|
|  Global Memory  |  Global Memory
|

### Memory Examples

Nvidia GeForce GTX 580 ([Fermi)](https://en.wikipedia.org/wiki/Fermi_%28microarchitecture%29) <a id="cite-note-8" href="#cite-ref-8">[8]</a>

- 128 KiB private memory per compute unit
- 48 KiB (16 KiB) local memory per compute unit (configurable)
- 64 KiB constant memory
- 8 KiB constant cache per compute unit
- 16 KiB (48 KiB) L1 cache per compute unit (configurable)
- 768 KiB L2 cache in total
- 1.5 GiB to 3 GiB global memory

AMD Radeon HD 7970 ([GCN](https://en.wikipedia.org/wiki/Graphics_Core_Next)) <a id="cite-note-9" href="#cite-ref-9">[9]</a>

- 256 KiB private memory per compute unit
- 64 KiB local memory per compute unit
- 64 KiB constant memory
- 16 KiB constant cache per four compute units
- 16 KiB L1 cache per compute unit
- 768 KiB L2 cache in total
- 3 GiB to 6 GiB global memory

### Unified Memory

Usually data has to be copied between a CPU host and a discrete GPU device, but different architectures from different vendors with different frameworks on different operating systems may offer a unified and accessible address space between CPU and GPU.

## Instruction Throughput

GPUs are used in [HPC](https://en.wikipedia.org/wiki/High-performance_computing) environments because of their good [FLOP](https://en.wikipedia.org/wiki/FLOP)/Watt ratio. The instruction throughput in general depends on the architecture (like Nvidia's [Tesla](https://en.wikipedia.org/wiki/Tesla_%28microarchitecture%29), [Fermi](https://en.wikipedia.org/wiki/Fermi_%28microarchitecture%29), [Kepler](https://en.wikipedia.org/wiki/Kepler_%28microarchitecture%29), [Maxwell](https://en.wikipedia.org/wiki/Maxwell_%28microarchitecture%29) or AMD's [TeraScale](https://en.wikipedia.org/wiki/TeraScale_%28microarchitecture%29), [GCN](https://en.wikipedia.org/wiki/Graphics_Core_Next), [RDNA](https://en.wikipedia.org/wiki/AMD_RDNA_Architecture)), the brand (like Nvidia [GeForce](https://en.wikipedia.org/wiki/GeForce), [Quadro](https://en.wikipedia.org/wiki/Nvidia_Quadro), [Tesla](https://en.wikipedia.org/wiki/Nvidia_Tesla) or AMD [Radeon](https://en.wikipedia.org/wiki/Radeon), [Radeon Pro](https://en.wikipedia.org/wiki/Radeon_Pro), [Radeon Instinct](https://en.wikipedia.org/wiki/Radeon_Instinct)) and the specific model.

## Integer Instruction Throughput

- INT32

The 32-bit integer performance can be architecture and operation depended less than 32-bit FLOP or 24-bit integer performance.

- INT64

In general [registers](https://en.wikipedia.org/wiki/Processor_register) and Vector-[ALUs](https://en.wikipedia.org/wiki/Arithmetic_logic_unit) of consumer brand GPUs are 32-bit wide and have to emulate 64-bit integer operations.

- INT8

## Some architectures offer higher throughput with lower precision. They quadruple the INT8 or octuple the INT4 throughput. Floating-Point Instruction Throughput

- FP32

Consumer GPU performance is measured usually in single-precision (32-bit) floating-point FMA (fused-multiply-add) throughput.

- FP64

Consumer GPUs have in general a lower ratio (FP32:FP64) for double-precision (64-bit) floating-point operations throughput than server brand GPUs.

- FP16

## Some GPGPU architectures offer half-precision (16-bit) floating-point operation throughput with an FP32:FP16 ratio of 1:2. Throughput Examples

Nvidia GeForce GTX 580 (Fermi, CC 2.0) - 32-bit integer operations/clock cycle per compute unit <a id="cite-note-10" href="#cite-ref-10">[10]</a>

```C++
   MAD 16
   MUL 16
   ADD 32
   Bit-shift 16
   Bitwise XOR 32

```

Max theoretic ADD operation throughput: 32 Ops x 16 CUs x 1544 MHz = 790.528 GigaOps/sec

AMD Radeon HD 7970 (GCN 1.0) - 32-bit integer operations/clock cycle per processing element <a id="cite-note-11" href="#cite-ref-11">[11]</a>

```C++
   MAD 1/4
   MUL 1/4
   ADD 1
   Bit-shift 1
   Bitwise XOR 1

```

Max theoretic ADD operation throughput: 1 Op x 2048 PEs x 925 MHz = 1894.4 GigaOps/sec

## Tensors

MMAC (matrix-multiply-accumulate) units are used in consumer brand GPUs for neural network based upsampling of video game resolutions, in professional brands for upsampling of images and videos, and in server brand GPUs for accelerating convolutional neural networks in general. Convolutions can be implemented as a series of matrix-multiplications via Winograd-transformations <a id="cite-note-12" href="#cite-ref-12">[12]</a>. Mobile SoCs usually have an dedicated neural network engine as MMAC unit.

## Nvidia TensorCores

## With Nvidia [Volta](<https://en.wikipedia.org/wiki/Volta_(microarchitecture)>) series TensorCores were introduced. They offer FP16xFP16+FP32, matrix-multiplication-accumulate-units, used to accelerate neural networks.<a id="cite-note-13" href="#cite-ref-13">[13]</a> Turing's 2nd gen TensorCores add FP16, INT8, INT4 optimized computation.<a id="cite-note-14" href="#cite-ref-14">[14]</a> Amperes's 3rd gen adds support for BF16, TF32, FP64 and sparsity acceleration.<a id="cite-note-15" href="#cite-ref-15">[15]</a>Ada Lovelaces's 4th gen adds support for FP8.<a id="cite-note-16" href="#cite-ref-16">[16]</a> AMD Matrix Cores

## AMD released 2020 its server-class [CDNA](https://www.amd.com/system/files/documents/amd-cdna-whitepaper.pdf) architecture with Matrix Cores which support MFMA (matrix-fused-multiply-add) operations on various data types like INT8, FP16, BF16, FP32. AMD's CDNA 2 architecture adds FP64 optimized throughput for matrix operations. AMD's RDNA 3 architecture features dedicated AI tensor operation acceleration. Intel XMX Cores

## Intel added XMX, Xe Matrix eXtensions, cores to some of the [Intel Xe](https://en.wikipedia.org/wiki/Intel_Xe) GPU series, like [Arc Alchemist](https://en.wikipedia.org/wiki/Intel_Arc#Alchemist). Host-Device Latencies

One reason GPUs are not used as accelerators for chess engines is the host-device latency, aka. kernel-launch-overhead. Nvidia and AMD have not published official numbers, but in practice there is a measurable latency for null-kernels of 5 microseconds <a id="cite-note-17" href="#cite-ref-17">[17]</a> up to 100s of microseconds <a id="cite-note-18" href="#cite-ref-18">[18]</a>. One solution to overcome this limitation is to couple tasks to batches to be executed in one run <a id="cite-note-19" href="#cite-ref-19">[19]</a>.

## Deep Learning

GPUs are much more suited than CPUs to implement and train [Convolutional Neural Networks](Neural_Networks#Convolutional "Neural Networks") (CNN), and were therefore also responsible for the [deep learning](Deep_Learning "Deep Learning") boom, also affecting game playing programs combining CNN with [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), as pioneered by [Google](index.php?title=Google&action=edit&redlink=1 "Google (page does not exist)") [DeepMind's](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)") [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)") and [AlphaZero](AlphaZero "AlphaZero") entities in [Go](Go "Go"), [Shogi](Shogi "Shogi") and [Chess](Chess "Chess") using [TPUs](https://en.wikipedia.org/wiki/Tensor_processing_unit), and the open source projects [Leela Zero](index.php?title=Leela_Zero&action=edit&redlink=1 "Leela Zero (page does not exist)") headed by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto") for [Go](Go "Go") and its [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") adaption.

## Architectures

The market is split into two categories, integrated and discrete GPUs. The first being the most important by quantity, the second by performance. Discrete GPUs are divided as consumer brands for playing 3D games, professional brands for CAD/CGI programs and server brands for big-data and number-crunching workloads. Each brand offering different feature sets in driver, VRAM, or computation abilities.

## AMD

AMD line of discrete GPUs is branded as Radeon for consumer, Radeon Pro for professional and Radeon Instinct for server.

- [List of AMD graphics processing units on Wikipedia](https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units)

### Navi 3x RDNA3

RDNA3 architecture in Radeon RX 7000 series was announced on November 3, 2022, featuring dedicated AI tensor operation acceleration.

- [AMD Radeon RX 7000 on Wikipedia](https://en.wikipedia.org/wiki/Radeon_RX_7000_series)
- [RDNA3 Instruction Set Architecture](https://developer.amd.com/wp-content/resources/RDNA3_Shader_ISA_December2022.pdf)

### CDNA2

CDNA2 architecture in MI200 HPC-GPU with optimized FP64 throughput (matrix and vector), multi-chip-module design and Infinity Fabric was unveiled in November, 2021.

- [AMD CDNA2 Whitepaper](https://www.amd.com/system/files/documents/amd-cdna2-white-paper.pdf)
- [CDNA2 Instruction Set Architecture](https://developer.amd.com/wp-content/resources/CDNA2_Shader_ISA_4February2022.pdf)

### CDNA

CDNA architecture in MI100 HPC-GPU with Matrix Cores was unveiled in November, 2020.

- [AMD CDNA Whitepaper](https://www.amd.com/system/files/documents/amd-cdna-whitepaper.pdf)
- [CDNA Instruction Set Architecture](https://developer.amd.com/wp-content/resources/CDNA1_Shader_ISA_14December2020.pdf)

### Navi 2x RDNA2

[RDNA2](<https://en.wikipedia.org/wiki/RDNA_(microarchitecture)#RDNA_2>) cards were unveiled on October 28, 2020.

- [AMD Radeon RX 6000 on Wikipedia](https://en.wikipedia.org/wiki/Radeon_RX_6000_series)
- [RDNA 2 Instruction Set Architecture](https://developer.amd.com/wp-content/resources/RDNA2_Shader_ISA_November2020.pdf)

### Navi RDNA

[RDNA](<https://en.wikipedia.org/wiki/RDNA_(microarchitecture)>) cards were unveiled on July 7, 2019.

- [RDNA Whitepaper](https://www.amd.com/system/files/documents/rdna-whitepaper.pdf)
- [Architecture Slide Deck](https://gpuopen.com/wp-content/uploads/2019/08/RDNA_Architecture_public.pdf)
- [RDNA Instruction Set](https://gpuopen.com/wp-content/uploads/2019/08/RDNA_Shader_ISA_5August2019.pdf)

### Vega GCN 5th gen

[Vega](https://en.wikipedia.org/wiki/Radeon_RX_Vega_series) cards were unveiled on August 14, 2017.

- [Architecture Whitepaper](https://www.techpowerup.com/gpu-specs/docs/amd-vega-architecture.pdf)
- [Vega Instruction Set](https://developer.amd.com/wp-content/resources/Vega_Shader_ISA_28July2017.pdf)

### Polaris GCN 4th gen

[Polaris](https://en.wikipedia.org/wiki/Graphics_Core_Next#Graphics_Core_Next_4) cards were first released in 2016.

- [Architecture Whitepaper](https://www.amd.com/system/files/documents/polaris-whitepaper.pdf)

### Southern Islands GCN 1st gen

Southern Island cards introduced the [GCN](https://en.wikipedia.org/wiki/Graphics_Core_Next) architecture in 2012.

- [AMD Radeon HD 7000 on Wikipedia](https://en.wikipedia.org/wiki/Radeon_HD_7000_series)
- [Southern Islands Programming Guide](https://amd.wpenginepowered.com/wordpress/media/2013/10/si_programming_guide_v2.pdf)
- [Southern Islands Instruction Set Architecture](https://amd.wpenginepowered.com/wordpress/media/2013/07/AMD_Southern_Islands_Instruction_Set_Architecture1.pdf)

## Apple

### M series

Apple released its M series SoC (system on a chip) with integrated GPU for desktops and notebooks in 2020.

- [Apple M series on Wikipedia](https://en.wikipedia.org/wiki/Apple_silicon#M_series)

## ARM

The ARM Mali GPU variants can be found on various systems on chips (SoCs) from different vendors. Since Midgard (2012) with unified-shader-model OpenCL support is offered.

- [Mali variants on Wikipedia](<https://en.wikipedia.org/wiki/Mali_(GPU)#Variants>)

### Valhall (2019)

- [Bifrost and Valhall OpenCL Developer Guide](https://developer.arm.com/documentation/101574/latest)

### Bifrost (2016)

- [Bifrost and Valhall OpenCL Developer Guide](https://developer.arm.com/documentation/101574/latest)

### Midgard (2012)

- [Midgard OpenCL Developer Guide](https://developer.arm.com/documentation/100614/latest)

## Intel

### Xe

[Intel Xe](https://en.wikipedia.org/wiki/Intel_Xe) line of GPUs (released since 2020) is divided as Xe-LP (low-power), Xe-HPG (high-performance-gaming), Xe-HP (high-performace) and Xe-HPC (high-performance-computing).

- [List of Intel Gen12 GPUs on Wikipedia](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Gen12)
- [Arc Alchemist series on Wikipedia](https://en.wikipedia.org/wiki/Intel_Arc#Alchemist)

## Nvidia

Nvidia line of discrete GPUs is branded as GeForce for consumer, Quadro for professional and Tesla for server.

- [List of Nvidia graphics processing units on Wikipedia](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units)

### Ada Lovelace Architecture

The [Ada Lovelace microarchitecture](<https://en.wikipedia.org/wiki/Ada_Lovelace_(microarchitecture)>) was announced on September 20, 2022, featuring 4th-generation Tensor Cores with FP8, FP16, BF16, TF32 and sparsity acceleration.

- [Ada GPU Whitepaper](https://images.nvidia.com/aem-dam/Solutions/geforce/ada/nvidia-ada-gpu-architecture.pdf)
- [Ada Tuning Guide](https://docs.nvidia.com/cuda/ada-tuning-guide/index.html)

### Hopper Architecture

The [Hopper GPU Datacenter microarchitecture](<https://en.wikipedia.org/wiki/Hopper_(microarchitecture)>) was announced on March 22, 2022, featuring Transfomer Engines for large language models.

- [Hopper H100 Whitepaper](https://resources.nvidia.com/en-us-tensor-core)
- [Hopper Tuning Guide](https://docs.nvidia.com/cuda/hopper-tuning-guide/index.html)

### Ampere Architecture

The [Ampere microarchitecture](<https://en.wikipedia.org/wiki/Ampere_(microarchitecture)>) was announced on May 14, 2020 <a id="cite-note-20" href="#cite-ref-20">[20]</a>. The Nvidia A100 GPU based on the Ampere architecture delivers a generational leap in accelerated computing in conjunction with CUDA 11 <a id="cite-note-21" href="#cite-ref-21">[21]</a>.

- [Ampere GA100 Whitepaper](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/nvidia-ampere-architecture-whitepaper.pdf)
- [Ampere GA102 Whitepaper](https://www.nvidia.com/content/PDF/nvidia-ampere-ga-102-gpu-architecture-whitepaper-v2.pdf)
- [Ampere GPU Architecture Tuning Guide](https://docs.nvidia.com/cuda/ampere-tuning-guide/index.html)

### Turing Architecture

[Turing](<https://en.wikipedia.org/wiki/Turing_(microarchitecture)>) cards were first released in 2018. They are the first consumer cores to launch with RTX, for [raytracing](<https://en.wikipedia.org/wiki/Ray_tracing_(graphics)>), features. These are also the first consumer cards to launch with TensorCores used for matrix multiplications to accelerate [convolutional neural networks](Neural_Networks#Convolutional "Neural Networks"). The Turing GTX line of chips do not offer RTX or TensorCores.

- [Turing Architecture Whitepaper](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/technologies/turing-architecture/NVIDIA-Turing-Architecture-Whitepaper.pdf)
- [Turing Tuning Guide](https://docs.nvidia.com/cuda/turing-tuning-guide/index.html)

### Volta Architecture

[Volta](<https://en.wikipedia.org/wiki/Volta_(microarchitecture)>) cards were released in 2017. They were the first cards to launch with TensorCores, supporting matrix multiplications to accelerate [convolutional neural networks](Neural_Networks#Convolutional "Neural Networks").

- [Volta Architecture Whitepaper](https://images.nvidia.com/content/volta-architecture/pdf/volta-architecture-whitepaper.pdf)
- [Volta Tuning Guide](https://docs.nvidia.com/cuda/volta-tuning-guide/index.html)

### Pascal Architecture

[Pascal](<https://en.wikipedia.org/wiki/Pascal_(microarchitecture)>) cards were first released in 2016.

- [Pascal Architecture Whitepaper](https://images.nvidia.com/content/pdf/tesla/whitepaper/pascal-architecture-whitepaper.pdf)
- [Pascal Tuning Guide](https://docs.nvidia.com/cuda/pascal-tuning-guide/index.html)

### Maxwell Architecture

[Maxwell](<https://en.wikipedia.org/wiki/Maxwell(microarchitecture)>) cards were first released in 2014.

- [Maxwell Architecture Whitepaper on archiv.org](https://web.archive.org/web/20170721113746/http://international.download.nvidia.com/geforce-com/international/pdfs/GeForce_GTX_980_Whitepaper_FINAL.PDF)
- [Maxwell Tuning Guide](https://docs.nvidia.com/cuda/maxwell-tuning-guide/index.html)

## PowerVR

PowerVR (Imagination Technologies) licenses IP to third parties (most notable Apple) used for system on a chip (SoC) designs. Since Series5 SGX OpenCL support via licensees is available.

### PowerVR

- [PowerVR series on Wikipedia](https://en.wikipedia.org/wiki/PowerVR#PowerVR_Graphics)

### IMG

- [IMG A series on Wikipedia](<https://en.wikipedia.org/wiki/PowerVR#IMG_A-Series_(Albiorix)>)
- [IMG B series on Wikipedia](https://en.wikipedia.org/wiki/PowerVR#IMG_B-Series)

## Qualcomm

Qualcomm offers Adreno GPUs in various types as a component of their Snapdragon SoCs. Since Adreno 300 series OpenCL support is offered.

### Adreno

- [Adreno variants on Wikipedia](https://en.wikipedia.org/wiki/Adreno#Variants)

## Vivante Corporation

Vivante licenses IP to third parties for embedded systems, the GC series offers optional OpenCL support.

### GC-Series

- [GC series on Wikipedia](https://en.wikipedia.org/wiki/Vivante_Corporation#Products)

## See also

- [Deep Learning](Deep_Learning "Deep Learning")
- [FPGA](FPGA "FPGA")
- [Graphics Programming](Graphics_Programming "Graphics Programming")
- [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
  - [MCαβ](MC%CE%B1%CE%B2 "MCαβ")
  - [UCT](UCT "UCT")
- [Parallel Search](Parallel_Search "Parallel Search")
- [Perft(15)](Perft#15 "Perft")
- [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
- [Thread](Thread "Thread")

## Publications

## 1986

- [W. Daniel Hillis](Mathematician#Hillis "Mathematician"), [Guy L. Steele, Jr.](Mathematician#GSteele "Mathematician") (**1986**). *[Data parallel algorithms](https://dl.acm.org/citation.cfm?id=7903)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 29, No. 12, Special Issue on Parallelism

## 1990

- [Guy E. Blelloch](Mathematician#GEBlelloch "Mathematician") (**1990**). *[Vector Models for Data-Parallel Computing](https://dl.acm.org/citation.cfm?id=91254)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), [pdf](https://www.cs.cmu.edu/~guyb/papers/Ble90.pdf)

## 2008 ...

- [Vlad Stamate](Vlad_Stamate "Vlad Stamate") (**2008**). *Real Time Photon Mapping Approximation on the GPU*. in [ShaderX6 - Advanced Rendering Techniques](http://shaderx6.com/TOC.html) <a id="cite-note-22" href="#cite-ref-22">[22]</a>
- [Ren Wu](Ren_Wu "Ren Wu"), [Bin Zhang](http://www.cedar.buffalo.edu/~binzhang/), [Meichun Hsu](http://www.hpl.hp.com/people/meichun_hsu/) (**2009**). *[Clustering billions of data points using GPUs](http://portal.acm.org/citation.cfm?id=1531668)*. [ACM International Conference on Computing Frontiers](http://www.computingfrontiers.org/2009/)
- [Mark Govett](https://github.com/markgovett), [Craig Tierney](https://www.linkedin.com/in/craig-tierney-9568545), [Jacques Middlecoff](Jacques_Middlecoff "Jacques Middlecoff"), [Tom Henderson](https://www.researchgate.net/profile/Tom_Henderson4) (**2009**). *Using Graphical Processing Units (GPUs) for Next Generation Weather and Climate Prediction Models*. [CAS2K9 Workshop](http://www.cisl.ucar.edu/dir/CAS2K9/)
- [Hank Dietz](Hank_Dietz "Hank Dietz"), [Bobby Dalton Young](https://dblp.uni-trier.de/pers/hd/y/Young:Bobby_Dalton) (**2009**). *[MIMD Interpretation on a GPU](https://link.springer.com/chapter/10.1007/978-3-642-13374-9_5)*. [LCPC 2009](https://dblp.uni-trier.de/db/conf/lcpc/lcpc2009.html), [pdf](http://aggregate.ee.engr.uky.edu/EXHIBITS/SC09/mogsimlcpc09final.pdf), [slides.pdf](http://aggregate.org/GPUMC/mogsimlcpc09slides.pdf)
- [Sander van der Maar](https://dblp.uni-trier.de/pid/28/7183.html), [Joost Batenburg](Joost_Batenburg "Joost Batenburg"), [Jan Sijbers](https://scholar.google.com/citations?user=TtXZhj8AAAAJ&hl=en) (**2009**). *[Experiences with Cell-BE and GPU for Tomography](https://link.springer.com/chapter/10.1007/978-3-642-03138-0_33)*. [SAMOS 2009](https://dblp.uni-trier.de/db/conf/samos/samos2009.html#MaarBS09) <a id="cite-note-23" href="#cite-ref-23">[23]</a>

## 2010...

- [Avi Bleiweiss](https://www.linkedin.com/in/avi-bleiweiss-456a5644) (**2010**). *Playing Zero-Sum Games on the GPU*. [NVIDIA Corporation](https://en.wikipedia.org/wiki/Nvidia), [GPU Technology Conference 2010](http://www.nvidia.com/object/io_1269574709099.html), [slides as pdf](http://www.nvidia.com/content/gtc-2010/pdfs/2207_gtc2010.pdf)
- [Mark Govett](https://github.com/markgovett), [Jacques Middlecoff](Jacques_Middlecoff "Jacques Middlecoff"), [Tom Henderson](https://www.researchgate.net/profile/Tom_Henderson4) (**2010**). *[Running the NIM Next-Generation Weather Model on GPUs](https://dl.acm.org/citation.cfm?id=1845128)*. [CCGRID 2010](https://dblp.uni-trier.de/db/conf/ccgrid/ccgrid2010.html)
- John Nickolls, William J. Dally (**2010**). [The GPU Computing Era](https://ieeexplore.ieee.org/document/5446251). [IEEE Micro](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=40).

**2011**

- [Mark Govett](https://github.com/markgovett), [Jacques Middlecoff](Jacques_Middlecoff "Jacques Middlecoff"), [Tom Henderson](https://www.researchgate.net/profile/Tom_Henderson4), [Jim Rosinski](https://cug.org/5-publications/proceedings_attendee_lists/CUG09CD/S09_Proceedings/pages/authors/11-15Wednesday/12A-Rosinski/Rosinski-paper.html), [Craig Tierney](https://www.linkedin.com/in/craig-tierney-9568545) (**2011**). *Parallelization of the NIM Dynamical Core for GPUs*. [slides as pdf](https://is.enes.org/archive-1/archive/documents/Govett.pdf)
- [Ľubomír Lackovič](index.php?title=%C4%BDubom%C3%ADr_Lackovi%C4%8D&action=edit&redlink=1 "Ľubomír Lackovič (page does not exist)") (**2011**). *[Parallel Game Tree Search Using GPU](https://hgpu.org/?p=5772)*. Institute of Informatics and Software Engineering, [Faculty of Informatics and Information Technologies](https://en.wikipedia.org/wiki/Faculty_of_Informatics_and_Information_Technologies), [Slovak University of Technology in Bratislava](https://en.wikipedia.org/wiki/Slovak_University_of_Technology_in_Bratislava), [pdf](http://acmbulletin.fiit.stuba.sk/vol3num2/lackovic.pdf)
- [Dan Anthony Feliciano Alcantara](index.php?title=Dan_Anthony_Feliciano_Alcantara&action=edit&redlink=1 "Dan Anthony Feliciano Alcantara (page does not exist)") (**2011**). *Efficient Hash Tables on the GPU*. Ph. D. thesis, [University of California, Davis](https://en.wikipedia.org/wiki/University_of_California,_Davis), [pdf](http://idav.ucdavis.edu/~dfalcant//downloads/dissertation.pdf) » [Hash Table](Hash_Table "Hash Table")
- [Damian Sulewski](index.php?title=Damian_Sulewski&action=edit&redlink=1 "Damian Sulewski (page does not exist)") (**2011**). *Large-Scale Parallel State Space Search Utilizing Graphics Processing Units and Solid State Disks*. Ph.D. thesis, [University of Dortmund](University_of_Dortmund "University of Dortmund"), [pdf](https://eldorado.tu-dortmund.de/dspace/bitstream/2003/29418/1/Dissertation.pdf)
- [Damjan Strnad](index.php?title=Damjan_Strnad&action=edit&redlink=1 "Damjan Strnad (page does not exist)"), [Nikola Guid](index.php?title=Nikola_Guid&action=edit&redlink=1 "Nikola Guid (page does not exist)") (**2011**). *[Parallel Alpha-Beta Algorithm on the GPU](http://cit.fer.hr/index.php/CIT/article/view/2029)*. [CIT. Journal of Computing and Information Technology](http://cit.fer.hr/index.php/CIT), Vol. 19, No. 4 » [Parallel Search](Parallel_Search "Parallel Search"), [Reversi](Othello "Othello")
- [Balázs Jákó](Bal%C3%A1zs_Jako "Balázs Jako") (**2011**). *Fast Hydraulic and Thermal Erosion on GPU*. M.Sc. thesis, Supervisor [Balázs Tóth](https://hu.linkedin.com/in/bal%C3%A1zs-t%C3%B3th-1b151329), [Eurographics 2011](http://eg2011.bangor.ac.uk/), [pdf](http://old.cescg.org/CESCG-2011/papers/TUBudapest-Jako-Balazs.pdf)

**2012**

- [Liang Li](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)"), [Hong Liu](index.php?title=Hong_Liu&action=edit&redlink=1 "Hong Liu (page does not exist)"), [Peiyu Liu](index.php?title=Peiyu_Liu&action=edit&redlink=1 "Peiyu Liu (page does not exist)"), [Taoying Liu](index.php?title=Taoying_Liu&action=edit&redlink=1 "Taoying Liu (page does not exist)"), [Wei Li](index.php?title=Wei_Li&action=edit&redlink=1 "Wei Li (page does not exist)"), [Hao Wang](index.php?title=Hao_Wang&action=edit&redlink=1 "Hao Wang (page does not exist)") (**2012**). *[A Node-based Parallel Game Tree Algorithm Using GPUs](https://www.semanticscholar.org/paper/A-Node-based-Parallel-Game-Tree-Algorithm-Using-Li-Liu/be21d7b9b91957b700aab4ce002e6753b826ff54)*. CLUSTER 2012 » [Parallel Search](Parallel_Search "Parallel Search")

**2013**

- [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Ali Karami Ali Karami](https://dblp.uni-trier.de/pers/hd/k/Karami:Ali), [Farshad Khunjush](https://dblp.uni-trier.de/pers/hd/k/Khunjush:Farshad) (**2013**). *[A parallel memetic algorithm on GPU to solve the task scheduling problem in heterogeneous environments](https://scholar.google.de/citations?view_op=view_citation&hl=en&user=VvkRESgAAAAJ&citation_for_view=VvkRESgAAAAJ:ufrVoPGSRksC)*. [GECCO '13](http://www.sigevo.org/gecco-2013/program.html)
- [Ali Karami](https://dblp.uni-trier.de/pers/hd/k/Karami:Ali), [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Farshad Khunjush](https://dblp.uni-trier.de/pers/hd/k/Khunjush:Farshad) (**2013**). *[A statistical performance prediction model for OpenCL kernels on NVIDIA GPUs](https://ieeexplore.ieee.org/document/6714232)*. [CADS 2013](https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6708586)
- [Diego Rodríguez-Losada](Diego_Rodr%C3%ADguez-Losada "Diego Rodríguez-Losada"), [Pablo San Segundo](Pablo_San_Segundo "Pablo San Segundo"), [Miguel Hernando](index.php?title=Miguel_Hernando&action=edit&redlink=1 "Miguel Hernando (page does not exist)"), [Paloma de la Puente](https://dblp.uni-trier.de/pers/hd/p/Puente:Paloma_de_la), [Alberto Valero-Gomez](https://dblp.uni-trier.de/pers/hd/v/Valero=Gomez:Alberto) (**2013**). *GPU-Mapping: Robotic Map Building with Graphical Multiprocessors*. [IEEE Robotics & Automation Magazine, Vol. 20, No. 2](https://dblp.uni-trier.de/db/journals/ram/ram20.html), [pdf](https://www.acin.tuwien.ac.at/fileadmin/acin/v4r/v4r/GPUMap_RAM2013.pdf)
- [David Williams](https://dblp.org/pid/28/977-2.html), [Valeriu Codreanu](Valeriu_Codreanu "Valeriu Codreanu"), [Po Yang](https://dblp.org/pid/88/5343-1.html), [Baoquan Liu](https://dblp.org/pid/54/784.html), [Feng Dong](https://www.strath.ac.uk/staff/dongfengprofessor/), [Burhan Yasar](https://dblp.org/pid/136/5430.html), [Babak Mahdian](https://scholar.google.com/citations?user=FZVGYiQAAAAJ&hl=en), [Alessandro Chiarini](https://scholar.google.com/citations?user=8WO6cVUAAAAJ&hl=en), [Xia Zhao](https://zhaoxiahust.github.io/), [Jos Roerdink](https://scholar.google.com/citations?user=jCFYHlkAAAAJ&hl=en) (**2013**). *[Evaluation of Autoparallelization Toolkits for Commodity GPUs](https://link.springer.com/chapter/10.1007/978-3-642-55224-3_42)*. [PPAM 2013](https://dblp.org/db/conf/ppam/ppam2013-1.html#WilliamsCYLDYMCZR13)

**2014**

- [Qingqing Dang](https://dblp.uni-trier.de/pers/hd/d/Dang:Qingqing), [Shengen Yan](https://dblp.uni-trier.de/pers/hd/y/Yan:Shengen), [Ren Wu](Ren_Wu "Ren Wu") (**2014**). *[A fast integral image generation algorithm on GPUs](https://ieeexplore.ieee.org/document/7097862)*. [ICPADS 2014](https://dblp.uni-trier.de/db/conf/icpads/icpads2014.html)
- [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Ali Karami Ali Karami](https://dblp.uni-trier.de/pers/hd/k/Karami:Ali), [Farshad Khunjush](https://dblp.uni-trier.de/pers/hd/k/Khunjush:Farshad) (**2014**). *[A Two-Tier Design Space Exploration Algorithm to Construct a GPU Performance Predictor](https://link.springer.com/chapter/10.1007/978-3-319-04891-8_12)*. [ARCS 2014](https://dblp.uni-trier.de/db/conf/arcs/arcs2014.html), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), Vol. 8350, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Steinar H. Gunderson](Steinar_H._Gunderson "Steinar H. Gunderson") (**2014**). *[Movit: High-speed, high-quality video filters on the GPU](https://archive.fosdem.org/2014/schedule/event/movit/)*. [FOSDEM](https://en.wikipedia.org/wiki/FOSDEM) [2014](https://archive.fosdem.org/2014/), [pdf](https://movit.sesse.net/movit-fosdem2014.pdf)
- [Baoquan Liu](https://dblp.org/pid/54/784.html), [Alexandru Telea](https://scholar.google.com/citations?user=VspO6ZUAAAAJ&hl=en), [Jos Roerdink](https://scholar.google.com/citations?user=jCFYHlkAAAAJ&hl=en), [Gordon Clapworthy](https://dblp.org/pid/87/6797.html), [David Williams](https://dblp.org/pid/28/977-2.html), [Po Yang](https://dblp.org/pid/88/5343-1.html), [Feng Dong](https://www.strath.ac.uk/staff/dongfengprofessor/), [Valeriu Codreanu](Valeriu_Codreanu "Valeriu Codreanu"), [Alessandro Chiarini](https://scholar.google.com/citations?user=8WO6cVUAAAAJ&hl=en) (**2018**). *Parallel centerline extraction on the GPU*. [Computers & Graphics](https://www.journals.elsevier.com/computers-and-graphics), Vol. 41, [pdf](https://strathprints.strath.ac.uk/70614/1/Liu_etal_CG2014_Parallel_centerline_extraction_GPU.pdf)

## 2015 ...

- [Peter H. Jin](index.php?title=Peter_H._Jin&action=edit&redlink=1 "Peter H. Jin (page does not exist)"), [Kurt Keutzer](index.php?title=Kurt_Keutzer&action=edit&redlink=1 "Kurt Keutzer (page does not exist)") (**2015**). *Convolutional Monte Carlo Rollouts in Go*. [arXiv:1512.03375](http://arxiv.org/abs/1512.03375) » [Deep Learning](Deep_Learning "Deep Learning"), [Go](Go "Go"), [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
- [Liang Li](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)"), [Hong Liu](index.php?title=Hong_Liu&action=edit&redlink=1 "Hong Liu (page does not exist)"), [Hao Wang](index.php?title=Hao_Wang&action=edit&redlink=1 "Hao Wang (page does not exist)"), [Taoying Liu](index.php?title=Taoying_Liu&action=edit&redlink=1 "Taoying Liu (page does not exist)"), [Wei Li](index.php?title=Wei_Li&action=edit&redlink=1 "Wei Li (page does not exist)") (**2015**). *[A Parallel Algorithm for Game Tree Search Using GPGPU](https://ieeexplore.ieee.org/document/6868996)*. [IEEE Transactions on Parallel and Distributed Systems](IEEE#TPDS "IEEE"), Vol. 26, No. 8 » [Parallel Search](Parallel_Search "Parallel Search")
- [Simon Portegies Zwart](Simon_Portegies_Zwart "Simon Portegies Zwart"), [Jeroen Bédorf](https://github.com/jbedorf) (**2015**). *[Using GPUs to Enable Simulation with Computational Gravitational Dynamics in Astrophysics](https://www.computer.org/csdl/magazine/co/2015/11/mco2015110050/13rRUx0Pqwe)*. [IEEE Computer](IEEE#Computer "IEEE"), Vol. 48, No. 11

**2016**

- [Sean Sheen](https://www.linkedin.com/in/sean-sheen-b99aba89) (**2016**). *[Astro - A Low-Cost, Low-Power Cluster for CPU-GPU Hybrid Computing using the Jetson TK1](https://digitalcommons.calpoly.edu/theses/1567/)*. Master's thesis, [California Polytechnic State University](https://en.wikipedia.org/wiki/California_Polytechnic_State_University), [pdf](https://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=2723&context=theses) <a id="cite-note-24" href="#cite-ref-24">[24]</a> <a id="cite-note-25" href="#cite-ref-25">[25]</a>
- [Jingyue Wu](https://scholar.google.com/citations?user=YyD7mwcAAAAJ&hl=en), [Artem Belevich](https://scholar.google.com/citations?user=EJcIByYAAAAJ&hl=en), [Eli Bendersky](https://scholar.google.com/citations?user=X5WAGdEAAAAJ&hl=en), [Mark Heffernan](https://www.linkedin.com/in/mark-heffernan-873b663/), [Chris Leary](https://scholar.google.com/citations?user=Guehv9sAAAAJ&hl=en), [Jacques Pienaar](https://scholar.google.com/citations?user=fAmfZAYAAAAJ&hl=en), [Bjarke Roune](http://www.broune.com/), [Rob Springer](https://scholar.google.com/citations?user=Der7mNMAAAAJ&hl=en), [Xuetian Weng](https://scholar.google.com/citations?user=zvfOH0wAAAAJ&hl=en), [Robert Hundt](https://scholar.google.com/citations?user=s7VCtl8AAAAJ&hl=en) (**2016**). *[gpucc: an open-source GPGPU compiler](https://dl.acm.org/citation.cfm?id=2854041)*. [CGO 2016](https://cgo.org/cgo2016/)
- [David Silver](David_Silver "David Silver"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Chris J. Maddison](Chris_J._Maddison "Chris J. Maddison"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [George van den Driessche](index.php?title=George_van_den_Driessche&action=edit&redlink=1 "George van den Driessche (page does not exist)"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Veda Panneershelvam](index.php?title=Veda_Panneershelvam&action=edit&redlink=1 "Veda Panneershelvam (page does not exist)"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Sander Dieleman](index.php?title=Sander_Dieleman&action=edit&redlink=1 "Sander Dieleman (page does not exist)"), [Dominik Grewe](index.php?title=Dominik_Grewe&action=edit&redlink=1 "Dominik Grewe (page does not exist)"), [John Nham](index.php?title=John_Nham&action=edit&redlink=1 "John Nham (page does not exist)"), [Nal Kalchbrenner](index.php?title=Nal_Kalchbrenner&action=edit&redlink=1 "Nal Kalchbrenner (page does not exist)"), [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Madeleine Leach](index.php?title=Madeleine_Leach&action=edit&redlink=1 "Madeleine Leach (page does not exist)"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2016**). *[Mastering the game of Go with deep neural networks and tree search](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 529 » [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)")
- [Balázs Jákó](Bal%C3%A1zs_Jako "Balázs Jako") (**2016**). *[Hardware accelerated hybrid rendering on PowerVR GPUs](https://www.semanticscholar.org/paper/Hardware-accelerated-hybrid-rendering-on-PowerVR-J%C3%A1k%C3%B3/d9d7f5784263c5abdcd6c1bf93267e334468b9b2)*. <a id="cite-note-26" href="#cite-ref-26">[26]</a> [IEEE](IEEE "IEEE") [20th Jubilee International Conference on Intelligent Engineering Systems](https://ieeexplore.ieee.org/xpl/conhome/7547434/proceeding)
- [Diogo R. Ferreira](Diogo_R._Ferreira "Diogo R. Ferreira"), [Rui M. Santos](https://dblp.uni-trier.de/pers/hd/s/Santos:Rui_M=) (**2016**). *[Parallelization of Transition Counting for Process Mining on Multi-core CPUs and GPUs](https://github.com/diogoff/transition-counting-gpu)*. [BPM 2016](https://dblp.uni-trier.de/db/conf/bpm/bpmw2016.html)
- [Ole Schütt](https://dblp.org/pers/hd/s/Sch=uuml=tt:Ole), [Peter Messmer](https://developer.nvidia.com/blog/author/peter-messmer/), [Jürg Hutter](https://scholar.google.ch/citations?user=ajbBWN0AAAAJ&hl=en), [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele") (**2016**). *[GPU Accelerated Sparse Matrix–Matrix Multiplication for Linear Scaling Density Functional Theory](https://onlinelibrary.wiley.com/doi/10.1002/9781118670712.ch8)*. [pdf](https://www.cp2k.org/_media/gpu_book_chapter_submitted.pdf) <a id="cite-note-27" href="#cite-ref-27">[27]</a>

Chapter 8 in [Ross C. Walker](https://scholar.google.com/citations?user=AV307ZUAAAAJ&hl=en), [Andreas W. Götz](https://scholar.google.com/citations?user=PJusscIAAAAJ&hl=en) (**2016**). *[Electronic Structure Calculations on Graphics Processing Units: From Quantum Chemistry to Condensed Matter Physics](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118670712)*. [John Wiley & Sons](<https://en.wikipedia.org/wiki/Wiley_(publisher)>)
**2017**

- [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815) » [AlphaZero](AlphaZero "AlphaZero")
- [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2017**). *[Residual Networks for Computer Go](http://ieeexplore.ieee.org/document/7875402/)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. PP, No. 99, [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/resnet.pdf)
- [Jayvant Anantpur](https://scholar.google.com/citations?user=zLksndkAAAAJ&hl=en), [Nagendra Gulur Dwarakanath](https://dblp.org/pid/09/10702.html), [Shivaram Kalyanakrishnan](https://dblp.org/pid/16/4410.html), [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar"), [R. Govindarajan](https://dblp.org/pid/45/3592.html) (**2017**). *RLWS: A Reinforcement Learning based GPU Warp Scheduler*. [arXiv:1712.04303](https://arxiv.org/abs/1712.04303)

**2018**

- [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2018**). *[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](http://science.sciencemag.org/content/362/6419/1140)*. [Science](<https://en.wikipedia.org/wiki/Science_(journal)>), Vol. 362, No. 6419

## Forum Posts

## 2005 ...

- [Hardware assist](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5480) by [Nicolai Czempin](Nicolai_Czempin "Nicolai Czempin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 27, 2006
- [Monte carlo on a NVIDIA GPU ?](http://www.talkchess.com/forum/viewtopic.php?t=22732) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), August 01, 2008

## 2010 ...

- [Using the GPU](http://www.talkchess.com/forum/viewtopic.php?t=32750) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 19, 2010

**2011**

- [GPGPU and computer chess](http://www.talkchess.com/forum/viewtopic.php?t=38002) by Wim Sjoho, [CCC](CCC "CCC"), February 09, 2011
- [Possible Board Presentation and Move Generation for GPUs?](http://www.talkchess.com/forum/viewtopic.php?t=38478) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), March 19, 2011

[Re: Possible Board Presentation and Move Generation for GPUs](http://www.talkchess.com/forum/viewtopic.php?t=38478&start=8) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), [CCC](CCC "CCC"), March 20, 2011

- [Zeta plays chess on a gpu](http://www.talkchess.com/forum/viewtopic.php?t=39459) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), June 23, 2011 » [Zeta](Zeta "Zeta")
- [GPU Search Methods](http://www.talkchess.com/forum/viewtopic.php?t=39606) by [Joshua Haglund](index.php?title=Joshua_Haglund&action=edit&redlink=1 "Joshua Haglund (page does not exist)"), [CCC](CCC "CCC"), July 04, 2011

**2012**

- [Possible Search Algorithms for GPUs?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=442052&t=41853) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), January 07, 2012 <a id="cite-note-28" href="#cite-ref-28">[28]</a> <a id="cite-note-29" href="#cite-ref-29">[29]</a>
- [uct on gpu](http://www.talkchess.com/forum/viewtopic.php?t=42590) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 24, 2012 » [UCT](UCT "UCT")
- [Is there such a thing as branchless move generation?](http://www.talkchess.com/forum/viewtopic.php?t=43971) by [John Hamlen](John_Hamlen "John Hamlen"), [CCC](CCC "CCC"), June 07, 2012 » [Move Generation](Move_Generation "Move Generation")
- [Choosing a GPU platform: AMD and Nvidia](http://www.talkchess.com/forum/viewtopic.php?t=44014) by [John Hamlen](John_Hamlen "John Hamlen"), [CCC](CCC "CCC"), June 10, 2012
- [Nvidias K20 with Recursion](http://www.talkchess.com/forum/viewtopic.php?t=46277) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), December 04, 2012 <a id="cite-note-30" href="#cite-ref-30">[30]</a>

**2013**

- [Kogge Stone, Vector Based](http://www.talkchess.com/forum/viewtopic.php?t=46974) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), January 22, 2013 » [Kogge-Stone Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") <a id="cite-note-31" href="#cite-ref-31">[31]</a> <a id="cite-note-32" href="#cite-ref-32">[32]</a>
- [GPU chess engine](http://www.talkchess.com/forum/viewtopic.php?t=47344) by Samuel Siltanen, [CCC](CCC "CCC"), February 27, 2013
- [Fast perft on GPU (upto 20 Billion nps w/o hashing)](http://www.talkchess.com/forum/viewtopic.php?t=48387) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), June 22, 2013 » [Perft](Perft "Perft"), [Kogge-Stone Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") <a id="cite-note-33" href="#cite-ref-33">[33]</a>

## 2015 ...

- [GPU chess update, local memory...](http://www.talkchess.com/forum/viewtopic.php?t=60386) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), June 06, 2016
- [Jetson GPU architecture](http://www.talkchess.com/forum/viewtopic.php?t=61761) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 18, 2016 » [Astro](GPU#Astro "GPU")
- [Pigeon is now running on the GPU](http://www.talkchess.com/forum/viewtopic.php?t=61925) by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), [CCC](CCC "CCC"), November 02, 2016 » [Pigeon](Pigeon "Pigeon")

**2017**

- [Back to the basics, generating moves on gpu in parallel...](http://www.talkchess.com/forum/viewtopic.php?t=63346) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), March 05, 2017 » [Move Generation](Move_Generation "Move Generation")
- [Re: Perft(15): comparison of estimates with Ankan's result](http://www.talkchess.com/forum/viewtopic.php?t=64983&start=9) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 26, 2017 » [Perft(15)](Perft#15 "Perft")
- [Chess Engine and GPU](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32317) by Fishpov , [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 09, 2017
- [To TPU or not to TPU...](http://www.talkchess.com/forum/viewtopic.php?t=66025) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), December 16, 2017 » [Deep Learning](Deep_Learning "Deep Learning") <a id="cite-note-34" href="#cite-ref-34">[34]</a>

**2018**

- [Announcing lczero](http://www.talkchess.com/forum/viewtopic.php?t=66280) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), January 09, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [GPU ANN, how to deal with host-device latencies?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67347) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), May 06, 2018 » [Neural Networks](Neural_Networks "Neural Networks")
- [GPU contention](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67357) by [Ian Kennedy](Ian_Kennedy "Ian Kennedy"), [CCC](CCC "CCC"), May 07, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [How good is the RTX 2080 Ti for Leela?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68448) by Hai, September 15, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") <a id="cite-note-35" href="#cite-ref-35">[35]</a>

[Re: How good is the RTX 2080 Ti for Leela?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68448&start=2) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), September 16, 2018

- [My non-OC RTX 2070 is very fast with Lc0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68973) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 19, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [LC0 using 4 x 2080 Ti GPU's on Chess.com tourney?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69400) by M. Ansari, [CCC](CCC "CCC"), December 28, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")

**2019**

- [Generate EGTB with graphics cards?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69447) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), January 01, 2019 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [LCZero FAQ is missing one important fact](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69478) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), January 01, 2019 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [Michael Larabel benches lc0 on various GPUs](https://groups.google.com/d/msg/lczero/I0lTgR-fFFU/NGC3kJDzAwAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2019 » [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") <a id="cite-note-36" href="#cite-ref-36">[36]</a>
- [Using LC0 with one or two GPUs - a guide](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70362) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), March 30, 2019 » [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero")
- [Wouldn't it be nice if C++ GPU](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70584) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), April 25, 2019 » [C++](Cpp "Cpp")
- [Lazy-evaluation of futures for parallel work-efficient Alpha-Beta search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71058) by Percival Tiglao, [CCC](CCC "CCC"), June 06, 2019
- [My home-made CUDA kernel for convolutions](https://www.game-ai-forum.org/viewtopic.php?f=21&t=694) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [Game-AI Forum](Computer_Chess_Forums "Computer Chess Forums"), November 09, 2019 » [Deep Learning](Deep_Learning "Deep Learning")
- [GPU rumors 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72320) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), November 13, 2019

## 2020 ...

- [AB search with NN on GPU...](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74771) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), August 13, 2020 » [Neural Networks](Neural_Networks "Neural Networks") <a id="cite-note-37" href="#cite-ref-37">[37]</a>
- [I stumbled upon this article on the new Nvidia RTX GPUs](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75073) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 10, 2020
- [Will AMD RDNA2 based Radeon RX 6000 series kick butt with Lc0?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75639) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), November 01, 2020
- [Zeta with NNUE on GPU?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76986) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), March 31, 2021 » [Zeta](Zeta "Zeta"), [NNUE](NNUE "NNUE")
- [GPU rumors 2021](https://talkchess.com/forum3/viewtopic.php?f=2&t=77097) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), April 16, 2021
- [Comparison of all known Sliding lookup algorithms \[CUDA\]](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79078) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), January 08, 2022 » [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks")

## External Links

- [Graphics processing unit from Wikipedia](https://en.wikipedia.org/wiki/Graphics_processing_unit)
- [Video card from Wikipedia](https://en.wikipedia.org/wiki/Video_card)
- [Heterogeneous System Architecture from Wikipedia](https://en.wikipedia.org/wiki/Heterogeneous_System_Architecture)
- [Tensor processing unit from Wikipedia](https://en.wikipedia.org/wiki/Tensor_processing_unit)
- [General-purpose computing on graphics processing units (GPGPU) from Wikipedia](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units)
- [List of AMD graphics processing units from Wikipedia](https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units)
- [List of Intel graphics processing units from Wikipedia](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units)
- [List of Nvidia graphics processing units from Wikipedia](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units)
- [NVIDIA Developer](https://developer.nvidia.com/)
- [NVIDIA GPU Programming Guide](https://developer.nvidia.com/nvidia-gpu-programming-guide)

## OpenCL

- [OpenCL from Wikipedia](https://en.wikipedia.org/wiki/OpenCL)
- [Part 1: OpenCL™ – Portable Parallelism - CodeProject](https://www.codeproject.com/Articles/110685/Part-1-OpenCL-Portable-Parallelism)
- [Part 2: OpenCL™ – Memory Spaces - CodeProject](https://www.codeproject.com/Articles/122405/Part-2-OpenCL-Memory-Spaces)

## CUDA

- [CUDA from Wikipedia](https://en.wikipedia.org/wiki/CUDA)
- [CUDA Zone | NVIDIA Developer](https://developer.nvidia.com/cuda-zone)
- [Nvidia CUDA Compiler (NVCC) from Wikipedia](https://en.wikipedia.org/wiki/NVIDIA_CUDA_Compiler)
- [Compiling CUDA with clang](https://llvm.org/docs/CompileCudaWithLLVM.html) — [LLVM](https://en.wikipedia.org/wiki/LLVM) [Clang](https://en.wikipedia.org/wiki/Clang) documentation
- [CppCon 2016](https://github.com/cppcon/cppcon2016): “Bringing Clang and C++ to GPUs: An Open-Source, CUDA-Compatible GPU C++ Compiler" by [Justin Lebar](https://github.com/jlebar), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video <a id="cite-note-38" href="#cite-ref-38">[38]</a>

## : Deep Learning

- [Deep Learning | NVIDIA Developer](https://developer.nvidia.com/deep-learning) » [Deep Learning](Deep_Learning "Deep Learning")
- [NVIDIA cuDNN | NVIDIA Developer](https://developer.nvidia.com/cudnn)
- [Efficient mapping of the training of Convolutional Neural Networks to a CUDA-based cluster](http://parse.ele.tue.nl/education/cluster2)
- [Deep Learning in a Nutshell: Core Concepts](https://devblogs.nvidia.com/parallelforall/deep-learning-nutshell-core-concepts/) by [Tim Dettmers](http://timdettmers.com/), [Parallel Forall](https://devblogs.nvidia.com/parallelforall/), November 3, 2015
- [Deep Learning in a Nutshell: History and Training](https://devblogs.nvidia.com/parallelforall/deep-learning-nutshell-history-training/) by [Tim Dettmers](http://timdettmers.com/), [Parallel Forall](https://devblogs.nvidia.com/parallelforall/), December 16, 2015
- [Deep Learning in a Nutshell: Sequence Learning](https://devblogs.nvidia.com/parallelforall/deep-learning-nutshell-sequence-learning/) by [Tim Dettmers](http://timdettmers.com/), [Parallel Forall](https://devblogs.nvidia.com/parallelforall/), March 7, 2016
- [Deep Learning in a Nutshell: Reinforcement Learning](https://devblogs.nvidia.com/parallelforall/deep-learning-nutshell-reinforcement-learning/) by [Tim Dettmers](http://timdettmers.com/), [Parallel Forall](https://devblogs.nvidia.com/parallelforall/), September 8, 2016
- [Faster deep learning with GPUs and Theano](https://blog.dominodatalab.com/gpu-computing-and-deep-learning/)
- [Theano (software) from Wikipedia](<https://en.wikipedia.org/wiki/Theano_(software)>)
- [TensorFlow from Wikipedia](https://en.wikipedia.org/wiki/TensorFlow)

## Game Programming

- [Advanced game programming | Session 5 - GPGPU programming](http://andy-thomason.github.io/lecture_notes/agp/agp_gpgpu_programming.html) by [Andy Thomason](Andy_Thomason "Andy Thomason")
- [Leela Zero](https://zero.sjeng.org/) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto") » [Leela Zero](index.php?title=Leela_Zero&action=edit&redlink=1 "Leela Zero (page does not exist)")

## [GitHub - gcp/leela-zero: Go engine with no human-provided knowledge, modeled after the AlphaGo Zero paper](https://github.com/gcp/leela-zero) Chess Programming

- [Chess on a GPGPU](https://chessgpgpu.blogspot.com/)
- [GPU Chess Blog](http://gpuchess.blogspot.com/)
- [ankan-ban/perft_gpu · GitHub](https://github.com/ankan-ban/perft_gpu) » [Perft](Perft "Perft") <a id="cite-note-39" href="#cite-ref-39">[39]</a>
- [LCZero · GitHub](https://github.com/LeelaChessZero) » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [GitHub - StuartRiffle/Jaglavak: Corvid Chess Engine](https://github.com/StuartRiffle/Jaglavak) » [Jaglavak](Jaglavak "Jaglavak")
- [Zeta OpenCL Chess](https://zeta-chess.app26.de/) » [Zeta](Zeta "Zeta")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Image](https://commons.wikimedia.org/wiki/File:NvidiaTesla.jpg) by Mahogny, February 09, 2008, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Fermi white paper from Nvidia](https://www.nvidia.com/content/PDF/fermi_white_papers/NVIDIA_Fermi_Compute_Architecture_Whitepaper.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [GeForce 500 series on Wikipedia](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units#GeForce_500_series)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Graphics Core Next on Wikipedia](https://en.wikipedia.org/wiki/Graphics_Core_Next)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Radeon HD 7000 series on Wikipedia](https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units#Radeon_HD_7000_series)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [CUDA Technical_Specification on Wikipedia](https://en.wikipedia.org/wiki/CUDA#Technical_Specification)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [AMD GPU Hardware Basics](https://www.olcf.ornl.gov/wp-content/uploads/2019/10/ORNL_Application_Readiness_Workshop-AMD_GPU_Basics.pdf)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> CUDA C Programming Guide v7.0, Appendix G.COMPUTE CAPABILITIES
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> AMD Accelerated Parallel Processing OpenCL Programming Guide rev2.7, Appendix D Device Parameters, Table D.1 Parameters for 7xxx Devices
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> CUDA C Programming Guide v7.0, Chapter 5.4.1. Arithmetic Instructions
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> AMD_OpenCL_Programming_Optimization_Guide.pdf 3.0beta, Chapter 2.7.1 Instruction Bandwidths
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Re: To TPU or not to TPU...](https://talkchess.com/forum3/viewtopic.php?f=7&t=66025&p=743355#p743355) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), December 16, 2017
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [INSIDE VOLTA](https://on-demand.gputechconf.com/gtc/2017/presentation/s7798-luke-durant-inside-volta.pdf)
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [AnandTech - Nvidia Turing Deep Dive page 6](https://www.anandtech.com/show/13282/nvidia-turing-architecture-deep-dive/6)
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Wikipedia - Ampere microarchitecture](<https://en.wikipedia.org/wiki/Ampere_(microarchitecture)#Details>)
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [- Ada Lovelace microarchitecture](<https://en.wikipedia.org/wiki/Ada_Lovelace_(microarchitecture)>)
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [host-device latencies?](https://devtalk.nvidia.com/default/topic/1047965/cuda-programming-and-performance/host-device-latencies-/post/5318041/#5318041) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), Nvidia CUDA ZONE, Feb 28, 2019
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [host-device latencies?](https://community.amd.com/thread/237337#comment-2902071) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic") AMD Developer Community, Feb 28, 2019
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Re: GPU ANN, how to deal with host-device latencies?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67347#p761239) by [Milos Stanisavljevic](Milos_Stanisavljevic "Milos Stanisavljevic"), [CCC](CCC "CCC"), May 06, 2018
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [NVIDIA Ampere Architecture In-Depth | NVIDIA Developer Blog](https://devblogs.nvidia.com/nvidia-ampere-architecture-in-depth/) by [Ronny Krashinsky](https://people.csail.mit.edu/ronny/), [Olivier Giroux](https://cppcast.com/guest/ogiroux/), [Stephen Jones](https://blogs.nvidia.com/blog/author/stephenjones/), [Nick Stam](https://blogs.nvidia.com/blog/author/nick-stam/) and [Sridhar Ramaswamy](https://en.wikipedia.org/wiki/Sridhar_Ramaswamy), May 14, 2020
1. <a id="cite-ref-21" href="#cite-note-21">↑</a> [CUDA 11 Features Revealed | NVIDIA Developer Blog](https://devblogs.nvidia.com/cuda-11-features-revealed/) by [Pramod Ramarao](https://devblogs.nvidia.com/author/pramarao/), May 14, 2020
1. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Photon mapping from Wikipedia](https://en.wikipedia.org/wiki/Photon_mapping)
1. <a id="cite-ref-23" href="#cite-note-23">↑</a> [Cell (microprocessor) from Wikipedia](<https://en.wikipedia.org/wiki/Cell_(microprocessor)>)
1. <a id="cite-ref-24" href="#cite-note-24">↑</a> [Jetson TK1 Embedded Development Kit | NVIDIA](http://www.nvidia.com/object/jetson-tk1-embedded-dev-kit.html)
1. <a id="cite-ref-25" href="#cite-note-25">↑</a> [Jetson GPU architecture](http://www.talkchess.com/forum/viewtopic.php?t=61761) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 18, 2016
1. <a id="cite-ref-26" href="#cite-note-26">↑</a> [PowerVR from Wikipedia](https://en.wikipedia.org/wiki/PowerVR)
1. <a id="cite-ref-27" href="#cite-note-27">↑</a> [Density functional theory from Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
1. <a id="cite-ref-28" href="#cite-note-28">↑</a> [Yaron Shoham](index.php?title=Yaron_Shoham&action=edit&redlink=1 "Yaron Shoham (page does not exist)"), [Sivan Toledo](index.php?title=Sivan_Toledo&action=edit&redlink=1 "Sivan Toledo (page does not exist)") (**2002**). *[Parallel Randomized Best-First Minimax Search](https://www.sciencedirect.com/science/article/pii/S0004370202001959)*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 137, Nos. 1-2
1. <a id="cite-ref-29" href="#cite-note-29">↑</a> [Alberto Maria Segre](Alberto_Maria_Segre "Alberto Maria Segre"), [Sean Forman](index.php?title=Sean_Forman&action=edit&redlink=1 "Sean Forman (page does not exist)"), [Giovanni Resta](index.php?title=Giovanni_Resta&action=edit&redlink=1 "Giovanni Resta (page does not exist)"), [Andrew Wildenberg](index.php?title=Andrew_Wildenberg&action=edit&redlink=1 "Andrew Wildenberg (page does not exist)") (**2002**). *[Nagging: A Scalable Fault-Tolerant Paradigm for Distributed Search](https://www.sciencedirect.com/science/article/pii/S000437020200228X)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 140, Nos. 1-2
1. <a id="cite-ref-30" href="#cite-note-30">↑</a> [Tesla K20 GPU Compute Processor Specifications Released | techPowerUp](http://www.techpowerup.com/173846/Tesla-K20-GPU-Compute-Processor-Specifications-Released.html)
1. <a id="cite-ref-31" href="#cite-note-31">↑</a> [Parallel Thread Execution from Wikipedia](https://en.wikipedia.org/wiki/Parallel_Thread_Execution)
1. <a id="cite-ref-32" href="#cite-note-32">↑</a> NVIDIA Compute PTX: Parallel Thread Execution, ISA Version 1.4, March 31, 2009, [pdf](http://www.nvidia.com/content/CUDA-ptx_isa_1.4.pdf)
1. <a id="cite-ref-33" href="#cite-note-33">↑</a> [ankan-ban/perft_gpu · GitHub](https://github.com/ankan-ban/perft_gpu)
1. <a id="cite-ref-34" href="#cite-note-34">↑</a> [Tensor processing unit from Wikipedia](https://en.wikipedia.org/wiki/Tensor_processing_unit)
1. <a id="cite-ref-35" href="#cite-note-35">↑</a> [GeForce 20 series from Wikipedia](https://en.wikipedia.org/wiki/GeForce_20_series)
1. <a id="cite-ref-36" href="#cite-note-36">↑</a> [Phoronix Test Suite from Wikipedia](https://en.wikipedia.org/wiki/Phoronix_Test_Suite)
1. <a id="cite-ref-37" href="#cite-note-37">↑</a> [kernel launch latency - CUDA / CUDA Programming and Performance - NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/kernel-launch-latency/62455) by LukeCuda, June 18, 2018
1. <a id="cite-ref-38" href="#cite-note-38">↑</a> [Re: Generate EGTB with graphics cards?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69447&start=1) by [Graham Jones](http://www.indriid.com/), [CCC](CCC "CCC"), January 01, 2019
1. <a id="cite-ref-39" href="#cite-note-39">↑</a> [Fast perft on GPU (upto 20 Billion nps w/o hashing)](http://www.talkchess.com/forum/viewtopic.php?t=48387) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), June 22, 2013

**[Up one Level](Hardware "Hardware")**

