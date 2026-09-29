---
title: "Do X in Y: Install lens in Ubuntu linux"
tags: do-x-in-y
---

Doug Rohde's [*lens*](http://tedlab.mit.edu/~dr/Lens) (light, efficient, neural simulator) is an awesome tool. However, given that it has not been actively maintained since 2000, its shelf-life is probably limited. I still have some legacy projects that were developed in lens (mainly using SRNs) and like to be able to re-run and tweak them. At some point, I'll move them to tensorflow, but in the meantime, if I can get them running on linux, that would be great.

My primary linux box is a virtual machine under VirtualBox on a Mac running Ubuntu 18.04.1 LTS. I got lens running here by consulting [this page](http://www.cs.rug.nl/~jurjen/ApprenticesNotes/ch27s16.html). My notes are a bit more compact than the details at that page, and actually add crucial details now that it is hard to find legacy packages for tcl/tk.

1. Get tcl and tk packages:
   - tcl: <http://old-releases.ubuntu.com/ubuntu/pool/universe/t/tcl8.3/>
     - Get both tcl8.3_8.3.5-14_amd64.deb and the corresponding tcl8.3-dev package.
   - tk: <http://old-releases.ubuntu.com/ubuntu/pool/universe/t/tk8.3/>
     - Get matching tk8.3 and tk8.3-dev packages
2. Install those guys, following instructions like [these](https://unix.stackexchange.com/questions/159094/how-to-install-a-deb-file-by-dpkg-i-or-by-apt), to wit:
   - `sudo apt install ./name.deb`
   - replace 'name.deb' with a package name; I assume you should tcl8.3 first, followed by tcl8.3-dev, tk8.3, and tk8.3-dev
3. Choose where you will install lens. Personally, I like easy access to it right off my home directory in a folder called LENS.
4. Download the code to that directory and unpack it:
   - `sudo wget http://tedlab.mit.edu/~dr/Lens/Dist/lens.tar.gz`
   - `sudo tar zxf lens.tar.gz`
   - `sudo rm lens.tar.gz`
5. Replace every instance of CLK_TCK with CLOCKS_PER_SEC in the files in Src; a one-line way of doing this from [this page](http://www.cs.rug.nl/~jurjen/ApprenticesNotes/ch27s16.html):
   - `sed -i 's%CLK_TCK%CLOCKS_PER_SEC%g' ./Src/command.c ./TclTk/tcl8.3.4/unix/tclUnixPort.h`
6. In Src/system.h, comment out the "`include <bits/nan.h>`" line; those functions have been integrated into math.h, which is also included. Not doing this leads to errors at compile.
7. Edit the Makefile. Minimally, replace the line "`CFLAGS = -Wall -O4 -march=i486`" with "`CFLAGS = -Wall -O4`". I also had some weird problems where it was generating a HOSTTYPE directory for i586 that would not work that went away when I simply commented out every other HOSTTYPE section except the default one. Inelegant, but it worked.
8. Then build it: `sudo make all`
   - If it didn't work, I'm sorry. That's all I've got…
9. Then deviate slightly from the installation directions. In your ~/.bashrc, add these lines (and save it and then start a new terminal or '`source ~/.bashrc`'):
   - `export LENSDIR=${HOME}/LENS # or whatever your location is`
   - `export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${LENSDIR}/Bin`
   - `export PATH=${PATH}:${LD_LIBRARY_PATH}:${LENSDIR}/Bin`
10. You should now be able to execute lens anywhere by typing '`lens`'
