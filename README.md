# Attacks on Implementations Coursebook

This is the handbook for the course "Attacks on Secure Implementations", taught in Ben-Gurion University by Dr. Yossi Oren.

To compile the book just run `latexmk`

Online course page: https://moodle2.bgu.ac.il/moodle/enrol/index.php?id=30088

More information: https://iss.oy.ne.ro/Attacks

## HOWTO Compile
### Windows
#### Toolchain Installation
1. Install MikTex from: https://miktex.org/download (with default settings). NOTE that although Tex Live is suposedly a decent alternative to MikTex on windows - attempts to use it for compiling the book failed miserably.
2. Install Perl from: http://strawberryperl.com/
3. [Optional but Recommended] Install VSCode and the **LaTeX Workshop** extension to be able to compile from VSCode.
4. [Optional but Recommended] Install the **LaTex language support** VSCode extension to ease editing in VSCode.
#### Full book Compilation
- From VSCode: open UniversityCourseBookAOI.tex, click on the "TEX" icon in the left sidebar, run the "Build LaTeX project" command.
- Without VSCode: run `latexmk` from the root directory of the book repository

# Course materials

### Lecture 1 - Introduction
- [TEMPEST](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=64) and secure communications, an attack on teletypewriter repeater machine. Part 1 (15 minutes);
- [TEMPEST](https://youtu.be/lQzzB87ADYA) and secure communications, an attack on teletypewriter repeater machine. Part 2 (18 minutes); 
- [Examples of implementation attacks on other machines](https://www.youtube.com/watch?v=lQzzB87ADYA&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=63) (11 minutes);
- [Implementation attacks on secure devices](https://www.youtube.com/watch?v=lQzzB87ADYA&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=61)  (9 minutes);
- [Between theory and implementation](https://www.youtube.com/watch?v=lQzzB87ADYA&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=60): System security, cryptographically secure algorithms and protocols, secure architectures  (19 minutes);
- [Breaking an implementation](https://www.youtube.com/watch?v=lQzzB87ADYA&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=59): The difference between theory and implementation (11 minutes);
- [Constructing and using a threat model](https://www.youtube.com/watch?v=lQzzB87ADYA&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=58): Review of the victim assets and the attacker capabilities (19 minutes);
- [Case studies](https://www.youtube.com/watch?v=lQzzB87ADYA&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=57): Review examples of attacks  (23 minutes);

Basic reading is the first chapter of Coursebook; for further reading, see the paper about the [TEMPEST](https://cryptome.org/nsa-tempest.pdf); here's Thomas Popp's paper [An Introduction to Implementation Attacks and Countermeasures](https://ieeexplore.ieee.org/document/5185386); there's also an [Overview about Attacks on Smart Cards](https://linkinghub.elsevier.com/retrieve/pii/S1363412703001079);

### Lecture 2 - Temporal Side Channels I
- [Countermeasures and their drawbacks](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=56) (14 minutes);
- [A history of temporal Side Channel](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=55) (10 minutes);
- [The definition of Temporal Side Channels](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=54) (6 minutes);
- [A timing attack on passwords](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=53) part 1 (15 minutes);
- [A timing attack on passwords](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=52) part 2 (23 minutes);
- [Countermeasures to timing attack on passwords](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=51): Examples of password checkers. (16 minutes);
- [The Algebra behind RSA](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=50) (16 minutes);
- [Make RSA more efficient via LR and CRT](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=49) (18 minutes);

Basic reading is the second chapter of Coursebook; for additional background reading on timing attacks, see [A Practical Implementation of of the Timing Attack](https://link.springer.com/chapter/10.1007%2F10721064_15); To read more about Montgomery's Modular Multiplications, see [Modular Multiplication Without Trial Division](https://www.ams.org/journals/mcom/1985-44-170/S0025-5718-1985-0777282-X/home.html); there's also an [Overview about Attacks on Smart Cards](https://linkinghub.elsevier.com/retrieve/pii/S1363412703001079);

### Lecture 3 - Temporal Side Channels II
- [Make RSA more efficient via Montgomery reduction](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=48) (18 minutes);
- [An example of a practical timing attack on RSA using Montgomery Reduction](https://youtu.be/-cxhBdt-MHc) - A brief overview of a practical timing attack (9 minutes);
- [The "Vaizata" method - an introduction](https://youtu.be/LxLzLLBZfeU) - An introduction to the Vaizata method, with 5 basic steps: implementation assumption, guessing part of the key, formulating an hypothesis, measurements classification, and drawing out statistical meaning (16 minutes);
- [The "Vaizata" Method in practice - PART 1](https://youtu.be/WFWi-pTZkiM) - A partial example of using the Vaizata method (12 minutes);
- [The "Vaizata" Method in practice - PART 2](https://youtu.be/WFWi-pTZkiM) - The second part of the practical example to the Vaizata method, following each one of the 5 steps (18 minutes)
- [The "Vaizata" Method - wrap up](https://youtu.be/4qL6JrwMDgE) - The final video regarding the Vaizata method, with a statistical analysis demo using Matlab (23 minutes);
- [Countermeasures to RSA timing attacks](https://youtu.be/Ppv_HMWkWdI) - How mitigate and prevent timing attacks (Hiding, Masking, Blinding, Square and Always Multiply) (16 minutes)
- [Bonus : timing attack paper - BlackHat2013](https://youtu.be/m7-wk4a1YVY) - A [link](https://youtu.be/KcOQfYlyIqw) to the 2013 BlackHat session on timing attacks featured by Paul Stone, where he introduces a number new techniques that use JavaScript-based timing attacks to extract sensitive data from browsers (6 minutes for the lecture video, 51 minutes for the YouTube video).


### Lecture 4 - Power-EM Side Channels
- [Basic electric circuit and Ohm's Law](https://youtu.be/KNHn61t1Bmg) - A brief overview/refresh for Ohm's Law(20 minutes);
- [Open and Short Circuits](https://youtu.be/8cvmVmwj0QY) - An overview on short circuits and open circuits(14 minutes);
- [Introdcution to transistors(and other electronic components)](https://youtu.be/6W9VeMXTERI) (15 minutes);
- [Sequential circuits based on FET](https://youtu.be/CNa20b0UpBk)(10 minutes);
- [Computational circuit based on FET - CMOS](https://youtu.be/7YJUMdPCXFA) - Demonstrating combinational circuits and logic gates (17 minutes);
- [Power consumption: Representation and computation](https://youtu.be/P2HB80Af7v4) - How attackers can exploit device clock frequency, circuit activity, and power consumption to gain knowledge about the device for their own benefit (9 minutes);
- [Types of noise & power consumption vs EM](https://youtu.be/1MwLpdDfo1E) - Introducing the 3 different types of Noise, and a short explanation on drawing measurements via Electro Magnetism (11 minutes);
- [Attacker setup explanation & demonstration](https://youtu.be/y0WVhA4yp0k) - Exploring a Power-EM attacker setup  (10 minutes);


### Lecture 5 - Power-EM Side Channels II
- [The New York Times 1998 - Paul Kocher](https://youtu.be/rC6mYV5f1cw) - Revisiting an attack from the 1995 on Smart Cards(10 minutes);
- [MC, ASIC & FPGA](https://youtu.be/lE3S2Nm3L2o)(10 minutes);
- [Simple power analysis of RSA](https://youtu.be/dTCsycglAxg)(13 minutes);
- [Simple Power Analysis Main idea](https://youtu.be/PDWMQ-3It0g)(17 minutes);
- [Basic MC - Virgulator](https://youtu.be/L13p5dFl2P0)(17 minutes) - Examining the Virgulator - a Javascript-implemented micro controller simulator;
- [The history of AES](https://youtu.be/emBHqbA27u4)(17 minutes);
- [AES - Main theme](https://youtu.be/OTvMCIzht8U) - Exploring the AES/Rijndael encryption standard, it's strengths and steps. (23 minutes);


### Lecture 6 - Power-EM Side Channels III
- [Simple poer analysis on AES - Plan A](https://youtu.be/x8WMxbpjdLQ) - Delving into 1 of 2 ways to performing a power analysis of AES. First, by capturing a power trace, then recovering the state bytes from that trace, and then using the state bytes to recover the key. (20 minutes);
- [Simple poer analysis on AES - Plan B](https://youtu.be/jvyTLZlNsHc) - Delving into the 2nd of 2 ways to performing a power analysis of AES. First, by capturing a power trace, then recovering the Hamming Weight from that trace, and then using the Hamming Weights to recover the key. (23 minutes);


### Guest Lecture - Stjepan Picek - CSI NN: Reverse Engineering of Neural Network Architectures Through Electromagnetic Side Channel
- [CSI NN(Reverse NN via EM) - part 1](https://youtu.be/9gQlJZKCTrg) - An intro about how timing attacks can be used for reverse engineering machine learning modules to obtain sensitive information about the invloved datasets (20 minutes);
- [CSI NN(Reverse NN via EM) - part 2](https://youtu.be/Mn6J7LqWdWo) - Exploring which information is required to execute such attacks, and which operations in the model are targeted (22 minutes);
- [CSI NN(Reverse NN via EM) - part 3](https://youtu.be/Vr7KXwLXUbA) - Delving into the reverse engineering process on a Neural Network(9 minutes);
- [CSI NN(Reverse NN via EM) - part 4](https://youtu.be/zf9bZDUKq90) - Examining results of attacks (16 minutes);


### Guest Lecture - Stjepan Picek - Machine Learning and Implementation Attacks
- [SCA via Deep Learning - part 1](https://youtu.be/XyXqInBYae4) - Discussing different types of profiled attacks and Neural Network architecure (19 minutes);
- [SCA via Deep Learning - part 2](https://youtu.be/hWFG1TnAqWM)(16 minutes);

### Lecture 7 - High Data Complexity Attacks Power-EM I
- [Recap - Attacks on AES](https://youtu.be/iWwzi1rqzYg) - A recap of RSA and AES attacks (13 minutes);
- [Recap - Attacks on RSA](https://youtu.be/kp4gv4icZ_c) - A recap of RSA and AES attacks (15 minutes)
- [High data complexity Attacks](https://youtu.be/RqC5hJnRo8k) - Discussing the main idea of high data complexity attacks (DPA/CPA)(15 minutes);
- [DPA With Vaizata](https://youtu.be/sFQJfKHsWxY) - Revisiting the Vaizata method and how to use it with DPA(13 minutes);
- [DPA With Vaizata On AES - Matlab(part 1)](https://youtu.be/cVl9su9Q6Lg) - Demonstrating Vaizata with DPA on Matlab(16 minutes);
- [DPA With Vaizata On AES](https://youtu.be/8A4VLm0Dfh0) - Vaizata with DPA demo - Examining the results (12 minutes);
- [DPA With Vaizata On AES - Matlab(part 2)](https://youtu.be/TXESGYUDAWA) (19 minutes);
- [DPA With Vaizata On AES](https://youtu.be/XLnRHlx7vlk)(18 minutes);

### Lecture 8 - High Data Complexity Attacks Power-EM II
- [Prime & Probe Cache Attack](https://youtu.be/t4jxgga4XIQ) - An explanation of the Prime & Probe cache attack(9 minutes);
- [Spectre - Toy Example](https://youtu.be/h-CEHjEkIm8) - Discussing the Spectre vulnerability(9 minutes);
- [From Prime & Probe To Spectre](https://youtu.be/cQ2-toh-kr0) - Demonstrating Spectre vulnerability using the Virgulator emulator(11 minutes);
- [Defining Micro-Architectural Attacks](https://youtu.be/dFnHC6OH2H4) - Discussing Micro-Architecture attacks between processes (19 minutes);
- [The Cache - Hierarchy and Structure](https://youtu.be/NJEgH9jgifA) - Discussing the need for caches, their structure, mapping policy and hierarachy and (20 minutes);


### Lecture 9 - Fault Attacks
- [Definition of Fault Attacks](https://youtu.be/PSRZaFiDwy8) - Defining Fault Attacks, which are active attacks for extracting information from devices by breaking them (12 minutes);
- [FA Example - Unlooper (1997)](https://youtu.be/urrVGoVhC0s) - Discussing unloopers which were smartcards intended to cause the card to skip one or more instructions by applying a "glitch" in some form to the power or clock signal(8 minutes);
- [Fault Attack Taxonomy](https://youtu.be/9e0fCJMJpQY) - Further discussion of Fault Attacks, fault methods, and targets(25 minutes);



