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

### Lecture 1 
- [TEMPEST](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=64) and unsecure communications, an attack on teletypewriter repeater machine. Part 1 (15 minutes) 
- [TEMPEST](https://www.youtube.com/watch?v=m7FYn4XMONE&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=62) and unsecure communications, an attack on teletypewriter repeater machine. Part 2 (15 minutes) 
- [Examples of implementation attacks on other machines](https://www.youtube.com/watch?v=lQzzB87ADYA&list=UUKK5uxRGT-0Jtq1bGAg7XkQ&index=63)(11 minutes)
- 