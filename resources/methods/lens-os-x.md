---
title: "Methods Report 2008.02: Installing lens in Mac OS X"
---

# {% include icon.html icon="fa-solid fa-file-lines" %}Installing *lens* in Mac OS X

[&larr; Back to Resources]({{ "resources" | relative_url }})

{% capture obsolete %}
**Archival note:** This methods report is obsolete and is kept for historical reference only. Many of the links and resources below no longer exist. For a more recent (but also dated) set of notes on building *lens* under Linux, see the [Do X in Y: Install lens in Ubuntu linux]({{ site.baseurl }}{% post_url 2018-10-25-do-x-in-y-install-lens-in-ubuntu-linux %}) post.
{% endcapture %}
{% include alert.html type="warning" content=obsolete %}

**Cognitive Neuroscience of Language Laboratory (MagLab)**<br>
Department of Psychology, University of Connecticut

**Methods Report 2008.02**<br>
Original version, 10 June 2008

**Installing *lens* in Mac OS X**<br>
Jim Magnuson<br>
james.magnuson@uconn.edu

---

## 2012.05.09: Note that this report is obsolete. The resources below do not exist any longer.

The good news, though, is there is a .dmg port!! Get [LENSOSX](http://hbrouwer.github.com/lensosx/)!

**2012.05.09**

That said, if you are trying to install on linux, see <http://www.cs.rug.nl/~jurjen/ApprenticesNotes/ch27s16.html> for some important notes, most notably:

- in Src/command.c, replace all occurrences of CLK_TCK with CLOCKS_PER_SEC
- You can try `sudo apt-get install -y tk8.3 tk8.3-dev` and `sudo apt-get install -y tcl8.3 tcl8.3-dev`
- Or you may be able to force the old tcl and tk libraries to work just by copying them from the Bin/x86 folder to /usr/lib. Probably not a good idea.

Okay, back to the sadly deprecated methods report…

---

*lens,* Doug Rohde's "light, efficient, neural simulator," provides a tcl/tk GUI and scripting environment on top of very fast C code. As of spring, 2008, even though Doug Rohde no longer supports the software and has apparently left academia, more and more labs appear to be using the *lens* simulator. This is because *lens* is fast, easy to use, and has many great features (especially the GUI). Various labs are initiating efforts to extend lens (e.g., to parallel/grid environments). It's pretty easy to install under windows (with cygwin installed), and very easy in linux, but pretty tough on your own under Macintosh OS X. Luckily, it appears the kind people in the [Language Imaging Lab at the Medical College of Wisconsin](http://www.neuro.mcw.edu) have smoothed the way by creating a 'port' of *lens* (lensnns) for MacPorts. The following instructions work for us for installing *lens* in OS X (and are nearly identical to steps sent to me by Jarrod Lewis-Peacock of the University of Wisconsin).

1. Make sure you have the version of [XCode developer tools](https://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/getSoftware?bundleID=19897) for your version of OS X.
2. Download and install [macports](http://www.macports.org/install.php)
3. Add the following lines to your ~/.bashrc or ~/.bash_profile

   ```bash
   export PATH=/opt/local/bin:/opt/local/sbin:$PATH
   export LENSDIR=/opt/local/share/lensnns
   ```

4. Download and run the "update_mri_ports" script as described [here](http://www.neuro.mcw.edu/Ports/update_mri_ports.html) (also from the kind folks of WI!)
5. Install *lens* with ports using:

   ```bash
   sudo nice port install lensnns
   ```

**Doug, wherever you are: many, many thanks.**

***lens* rocks.**
