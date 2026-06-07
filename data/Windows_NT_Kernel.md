


Windows NT is a proprietary graphical operating system produced by Microsoft as part of its Windows product line, the first version of which, Windows NT 3.1, was released on July 27, 1993. Originally made for the workstation, office, and server markets, the Windows NT line was made available to consumers with the release of Windows XP in 2001. The underlying technology of Windows NT continues to exist to this day with incremental changes and improvements, with the latest version of Windows based on Windows NT being Windows Server 2025 announced in 2024.


The name "Windows NT" originally denoted the major technological advancements that it had introduced to the Windows product line, including eliminating the 16-bit memory access limitations of earlier Windows releases such as Windows 3.1. Each Windows release built on this technology is considered to be based on, if not a revision of Windows NT, even though the Windows NT name itself has not been used in any other Windows releases since Windows NT 4.0 in 1996.


Windows NT provides many more features than other Windows releases, among them being support for multiprocessing, multi-user systems, a "pure" 32-bit kernel with 32-bit memory addressing, support for instruction sets other than x86, and many other system services such as Active Directory and more. Newer versions of Windows NT support 64-bit computing, with a 64-bit kernel and 64-bit memory addressing.


## Product line

Windows NT is a group or family of products—like Windows is a group or family. Windows NT is a sub-grouping of Windows.


The first version of Windows NT, 3.1, was produced for workstation and server computers. It was commercially focused—and intended to complement consumer versions of Windows that were based on MS-DOS (including Windows 1.0 through Windows 3.1x). In 1996, Windows NT 4.0 was released, including the new shell from Windows 95.


Eventually, Microsoft incorporated the Windows NT technology into the Windows product line for personal computing and deprecated the Windows 9x family. Starting with Windows 2000, "NT" was removed from the product name yet is still in several low-level places in the system—including for a while as part of the product version.


## Installing

Versions of Windows NT are installed using Windows Setup, which, starting with Windows Vista, uses the Windows Preinstallation Environment, which is a lightweight version of Windows NT made for deployment of the operating system.


Since Windows Vista, the Windows installation files, as well as the preinstallation environment used to install Windows, are stored in the Windows Imaging Format. It is possible to use the Deployment Image Servicing and Management (DISM) tool to install Windows from the command line and skip the GUI installer.


## Naming

It has been suggested that Dave Cutler intended the initialism "WNT" as a play on VMS, incrementing each letter by one. However, the project was originally intended as a follow-on to OS/2 and was referred to as "NT OS/2" before receiving the Windows brand. Two of the original NT developers, Mark Lucovsky and Dave W. Plummer, state that the name was taken from the original target processor—the Intel i860, code-named N10 ("N-Ten"). A 1991 video featuring Bill Gates and Microsoft products specifically says that "Windows NT stands for 'New Technology'". Seven years later in 1998, during a question-and-answer (Q&A) session, he then revealed that the letters were previously expanded to such but no longer carry any specific meaning. The letters were dropped from the names of releases from Windows 2000 and later, though Microsoft described that product as being "Built on NT Technology".


"NT" was a trademark of Northern Telecom (later Nortel), which Microsoft was forced to acknowledge on the product packaging.


## Major features

One of the main purposes of NT is hardware and software portability. Various versions of NT family operating systems have been released for a variety of processor architectures, initially IA-32, MIPS, and DEC Alpha, with PowerPC, Itanium, x86-64 and ARM supported in later releases. An initial idea was to have a common code base with a custom Hardware Abstraction Layer (HAL) for each platform. However, support for MIPS, Alpha, and PowerPC was later dropped in Windows 2000. Broad software compatibility was initially achieved with support for several API "personalities", including Windows API, POSIX, and OS/2 APIs—the latter two were phased out starting with Windows XP. Partial MS-DOS and Windows 16-bit compatibility is achieved on IA-32 via an integrated DOS Virtual Machine—although this feature is not available on other architectures.


NT has supported per-object (file, function, and role) access control lists allowing a rich set of security permissions to be applied to systems and services. NT
has also supported Windows network protocols, inheriting the previous OS/2 LAN Manager networking, as well as TCP/IP networking (for which Microsoft used to implement a TCP/IP stack derived at first from a STREAMS-based stack from Spider Systems, then later rewritten in-house).


Windows NT 3.1 was the first version of Windows to use 32-bit flat virtual memory addressing on 32-bit processors. Its companion product, Windows 3.1, used segmented addressing and switches from 16-bit to 32-bit addressing in pages.


Windows NT 3.1 featured a core kernel providing a system API, running in supervisor mode (ring 0 in x86; referred to in Windows NT as "kernel mode" on all platforms), and a set of user-space environments with their own APIs which included the new Win32 environment, an OS/2 1.3 text-mode environment and a POSIX environment. The full preemptive multitasking kernel could interrupt running tasks to schedule other tasks, without relying on user programs to voluntarily give up control of the CPU, as in Windows 3.1 applications (although MS-DOS applications were preemptively multitasked in Windows starting with Windows/386).


Notably, in Windows NT 3.x, several I/O driver subsystems, such as video and printing, were user-mode subsystems. In Windows NT 4.0, the video, server, and printer spooler subsystems were moved into kernel mode. Windows NT's first GUI was strongly influenced by (and programmatically compatible with) that from Windows 3.1; Windows NT 4.0's interface was redesigned to match that of the brand-new Windows 95, moving from the Program Manager to the Windows shell design.


NTFS, a journaled, secure file system, is a major feature of NT. Windows NT also allows for other installable file systems; NT can also be installed on FAT file systems, and versions 3.1, 3.5, and 3.51 could be installed on HPFS file systems.


Windows NT introduced its own driver model, the Windows NT driver model, and is incompatible with older driver frameworks. With Windows 2000, the Windows NT driver model was enhanced to become the Windows Driver Model, which was first introduced with Windows 98, but was based on the NT driver model. Windows Vista added native support for the Windows Driver Foundation, which is also available for Windows XP, Windows Server 2003 and to an extent, Windows 2000.


## Development

Microsoft decided to create a portable operating system, compatible with OS/2 and POSIX and supporting multiprocessing, in October 1988. When development started in November 1989, Windows NT was to be known as OS/2 3.0, the third version of the operating system developed jointly by Microsoft and IBM. To ensure portability, initial development was targeted at the Intel i860XR RISC processor, switching to the MIPS R3000 in late 1989, and then the Intel i386 in 1990. Microsoft also continued parallel development of the DOS-based and less resource-demanding Windows environment, resulting in the release of Windows 3.0 in May 1990.


Windows 3.0 was eventually so successful that Microsoft decided to change the primary application programming interface for the still unreleased NT OS/2 (as it was then known) from an extended OS/2 API to an extended Windows API. This decision caused tension between Microsoft and IBM and the collaboration ultimately fell apart.


IBM continued OS/2 development alone while Microsoft continued work on the newly renamed Windows NT. Though neither operating system would immediately be as popular as Microsoft's MS-DOS or Windows products, Windows NT would eventually be far more successful than OS/2.


Microsoft hired a group of developers from Digital Equipment Corporation led by Dave Cutler to build Windows NT, and many elements of the design reflect earlier DEC experience with Cutler's VMS, VAXELN and RSX-11, but also an unreleased object-based operating system developed by Cutler at Digital codenamed MICA. The team was joined by selected members of the disbanded OS/2 team, including Moshe Dunie.


Although NT was not an exact clone of Cutler's previous operating systems, DEC engineers almost immediately noticed the internal similarities. Parts of VAX/VMS Internals and Data Structures, published by Digital Press, accurately describe Windows NT internals using VMS terms. Furthermore, parts of the NT codebase's directory structure and filenames matched that of the MICA codebase. Instead of a lawsuit, Microsoft agreed to pay DEC $65–100 million, help market VMS, train Digital personnel on Windows NT, and continue Windows NT support for the DEC Alpha.


Windows NT and VMS memory management, processes, and scheduling are very similar. Windows NT's process management differs by implementing threading, which DEC did not implement until VMS 7.0 in 1995.


Like VMS, Windows NT's kernel mode code distinguishes between the "kernel", whose primary purpose is to implement processor- and architecture-dependent functions, and the "executive". This was designed as a modified microkernel, as the Windows NT kernel was influenced by the Mach microkernel developed by Richard Rashid at Carnegie Mellon University, but does not meet all of the criteria of a pure microkernel. Both the kernel and the executive are linked together into the single loaded module ntoskrnl.exe; from outside this module, there is little distinction between the kernel and the executive. Routines from each are directly accessible, as for example from kernel-mode device drivers.


API sets in the Windows NT family are implemented as subsystems atop the publicly undocumented "native" API; this allowed the late adoption of the Windows API (into the Win32 subsystem). Windows NT was one of the earliest operating systems to use UCS-2 and UTF-16 internally.


## Architecture

Windows NT uses a layered design architecture that consists of two main components, user mode and kernel mode. Programs and subsystems in user mode are limited in terms of what system resources they have access to, while the kernel mode has unrestricted access to the system memory and external devices. Kernel mode in Windows NT has full access to the hardware and system resources of the computer. The Windows NT kernel is a hybrid kernel; the architecture comprises a simple kernel, hardware abstraction layer (HAL), drivers, and a range of services (collectively named Executive), which all exist in kernel mode.


The booting process of Windows NT begins with NTLDR in versions before Vista and the Windows Boot Manager in Vista and later. The boot loader is responsible for accessing the file system on the boot drive, starting the kernel, and loading boot-time device drivers into memory. Once all the boot and system drivers have been loaded, the kernel starts the Session Manager Subsystem. This process launches winlogon, which allows the user to log in. Once the user is logged in File Explorer is started, loading the graphical user interface of Windows NT.


### Programming language

Windows NT is written in C and C++, with a very small amount written in assembly language. C is mostly used for the kernel code while C++ is mostly used for user-mode code. Assembly language is avoided where possible because it would impede portability and its usage is limited to just the most performance-critical portions (e.g. trap handlers, interrupt dispatch, system call stubs, context switching, HAL low‑level routines) of the codebase.


## Releases

The following are the releases of Windows based on the Windows NT technology.


Windows NT 3.1 to 3.51 incorporated the Program Manager and File Manager from the Windows 3.1 series. Windows NT 4.0 onwards replaced those programs with Windows Explorer (including a taskbar and Start menu), which originally appeared in Windows 95.


The first release was given version number 3.1 to match the contemporary 16-bit Windows; magazines of that era claimed the number was also used to make that version seem more reliable than a ".0" release. Also the Novell IPX protocol was apparently licensed only to 3.1 versions of Windows software.


The NT version number is not now generally used for marketing purposes, but is still used internally, and said to reflect the degree of changes to the core of the operating system. However, for application compatibility reasons, Microsoft kept the major version number as 6 in releases following Vista, but changed it later to 10 in Windows 10. The build number is an internal identifier used by Microsoft's developers and beta testers.


Starting with Windows 8.1, Microsoft changed the Version API Helper functions' behavior. If an application is not manifested for Windows 8.1 or later, the API will always return version 6.2, which is the version number of Windows 8. This is because the manifest feature was introduced with Windows 8.1, to replace GetVersion and related functions.


## Supported platforms

### 32-bit platforms

In order to prevent Intel x86-specific code from slipping into the operating system, due to developers being used to developing on x86 chips, Windows NT 3.1 was initially developed using non-x86 development systems and then ported to the x86 architecture. This work was initially based on the Intel i860-based Dazzle system and, later, the MIPS R3000-based Jazz platform. Both systems were designed internally at Microsoft.


Windows NT 3.1 was released for Intel x86 PC compatible and PC-98 platforms, and for DEC Alpha and ARC-compliant MIPS platforms. Windows NT 3.51 added support for the PowerPC processor in 1995, specifically PReP-compliant systems such as the IBM ThinkPad Power Series laptops and Motorola PowerStack series; but despite meetings between Michael Spindler and Bill Gates, not on the Power Macintosh as the PReP compliant Power Macintosh project failed to ship.


Intergraph Corporation ported Windows NT to its Clipper architecture and later announced an intention to port Windows NT 3.51 to Sun Microsystems' SPARC architecture, in conjunction with the company's planned introduction of UltraSPARC models in 1995, but neither version was sold to the public as a retail product.


Only two of the Windows NT 4.0 variants (IA-32 and Alpha) have a full set of service packs available. All of the other ports done by third parties (Motorola, Intergraph, etc.) have few, if any, publicly available updates.


Windows NT 4.0 was the last major release to support Alpha, MIPS, or PowerPC, though development of Windows 2000 for Alpha continued until August 1999, when Compaq stopped support for Windows NT on that architecture; and then three days later Microsoft also canceled their AlphaNT program, even though the Alpha NT 5 (Windows 2000) release had reached RC1 status.


On January 5, 2011, Microsoft announced that the next major version of the Windows NT family will include support for the ARM architecture. Microsoft demonstrated a preliminary version of Windows (version 6.2.7867) running on an ARM-based computer at the 2011 Consumer Electronics Show. This eventually led to the commercial release of the Windows 8-derived Windows RT on October 26, 2012, and the use of Windows NT, rather than Windows CE, in Windows Phone 8.


The original Xbox and Xbox 360 run a custom operating system based upon a heavily modified version of Windows 2000, an approach that Microsoft engineer Don Box called "fork and run". It exports APIs similar to those found in Microsoft Windows, such as Direct3D. The Xbox One and Xbox Series X/S consoles use a stripped-down version of the Windows operating system.


Windows 11 is the first non-server version of Windows NT that does not support 32-bit platforms.


### 64-bit platforms

The 64-bit versions of Windows NT were originally intended to run on Itanium and DEC Alpha; the latter was used internally at Microsoft during early development of 64-bit Windows. This continued for some time after Microsoft publicly announced that it was cancelling plans to ship 64-bit Windows for Alpha. Because of this, Alpha versions of Windows NT are 32-bit only.


While Windows 2000 only supports Intel IA-32 (32-bit), Windows XP, Server 2003, Server 2008 and Server 2008 R2 each have one edition dedicated to Itanium-based systems. In comparison with Itanium, Microsoft adopted x64 on a greater scale: every version of Windows since Windows XP (which has a dedicated x64 edition) has x64 editions.


The first version of Windows NT to support ARM64 devices with Qualcomm processors was Windows 10, version 1709. This is a full version of Windows, rather than the cut-down Windows RT.


## Hardware requirements

The minimum hardware specification required to run each release of the professional workstation version of Windows NT has been fairly slow-moving until the 6.0 (Vista) release, which requires a minimum of 15 GB of free disk space, a tenfold increase in free disk space alone over the previous version, and the 2021 10.0 (11) release which excludes most systems built before 2018.

