---
title: jTRACE
---

# {% include icon.html icon="fa-solid fa-diagram-project" %}jTRACE

*An easy-to-use, cross-platform, reimplementation of TRACE with a new graphical user interface and many other features*

jTRACE is a freely-available *re*-implementation of the TRACE model of spoken word recognition. It is implemented in Java, and runs on any computer that supports Java. Researchers can run simulations quickly and easily, using code that has been validated against the original TRACE code. Advanced programmers can extend the jTRACE model to implement new behaviors.

jTRACE was created by the Magnuson Lab at the [University of Connecticut](https://uconn.edu/) with the support of the [National Institute of Deafness and Other Communications Disorders](https://www.nidcd.nih.gov/). Primary code development was done by Ted Strauss and Harlan Harris.

## What's TRACE?

TRACE is a highly influential model of speech perception and spoken word recognition, created by Jay McClelland and Jeff Elman (1986). The original implementation of that model was used to run dozens of simulations comparing TRACE's behavior with results from experimental studies with human subjects. TRACE's behavior accounted for human behavior in a number of important ways, and it is still frequently cited as the canonical *interactive-activation* model of speech perception and spoken word recognition. TRACE has proved remarkably robust, accounting for results in paradigms that were developed 10 years after the model (e.g., fine-grained time course measures from eye tracking).

## Features, and version history

![jTRACE screenshot]({{ "resources/jtrace/jtrace-screen.jpg" | relative_url }})

- Underlying model is functionally equivalent to the original TRACE code.
- Graphical user interface is powerful and easy to use.
- Node activations are visualized as the simulation progresses.
- Graphical analyses of word and phoneme activations over time.
- Powerful scripting capabilities.
- Parameter and other files are saved in flexible XML format.
- Alpha.55 (current version)
  - Phoneme panel for editing/adding phoneme representations
  - 'Duration scalar' parameter for modifying the temporal extent of phonemes.
  - Input panel for designing ambiguous and spliced input representations
  - Lexicon validation; sorting on lexicon table.

## Requirements

- Any computer with [Java 2 1.4.2](https://www.java.com/) or later installed (most up-to-date computers will already have Java)

## Downloads

The zip file below is for **all operating systems.** There is no installer.

- To get started, unzip the contents of the file into a *new* directory.
  - On Windows run the "jtrace.bat" file.
  - On Linux or Mac OS X, run the "jtrace.sh" file. (In Linux or OS X: open a terminal window, get to the new directory where you have unzipped jTRACE, and enter "./jtrace.sh" or "sh ./jtrace.sh"). See the [Release Notes]({{ "resources/jtrace/release-notes" | relative_url }}).

*NOTE: The following is a functional but not polished pre-release (beta) version of the software. Significant interface and usability bugs may remain.*

- Download [jtrace-a64]({{ "resources/jtrace/jtrace-a64.zip" | relative_url }}) (version 0.64 alpha, 12.8 mb, last updated 01/10/2010)
- [Release notes]({{ "resources/jtrace/release-notes" | relative_url }})
- This [appendix]({{ "resources/jtrace/analysis-notes.pdf" | relative_url }}) to the user's manual distinguishes between the analysis options available in the graph panel.
- We'd like to know who is using jTRACE and what we can do to help (when we have time). Please send an email to [Jim Magnuson](mailto:james.magnuson@uconn.edu) to let him know you're using the system. We'll also keep you updated on improvements to the software.

### For advanced users

- The jTRACE source code is available here: <https://github.com/ted-strauss-K1/jTRACE>
- People interested in validating jTRACE against the original implementation may download our instrumented version of TRACE, called cTRACE. Instructions are included. [ctrace.zip]({{ "resources/jtrace/ctrace.zip" | relative_url }})

## Documentation

- [jTRACE instruction manual]({{ "resources/jtrace/users-guide" | relative_url }})
- Tutorial slides: "Computational Modeling of Spoken Language Processing"
  - [1-page abstract]({{ "resources/jtrace/jTRACETutorial-Abstract.pdf" | relative_url }})
  - [module 1]({{ "resources/jtrace/jTRACETutorial-Module01.pdf" | relative_url }})
  - [module 2]({{ "resources/jtrace/jTRACETutorial-Module02.pdf" | relative_url }})
  - [module 3]({{ "resources/jtrace/jTRACETutorial-Module03.pdf" | relative_url }})
  - [module 4]({{ "resources/jtrace/jTRACETutorial-Module04.pdf" | relative_url }})
  - [module 5]({{ "resources/jtrace/jTRACETutorial-Module05.pdf" | relative_url }})
- Strauss, T. J., Harris, H. D., & Magnuson, J. S. (2007). jTRACE: A reimplementation and extension of the TRACE model of speech perception and spoken word recognition. *Behavior Research Methods, 39,* 19-30. [[Publications]({{ "publications" | relative_url }})]
- [Replications]({{ "resources/jtrace/TRACE-replications.pdf" | relative_url }}) of earlier TRACE simulations done with jTRACE

## Tutorial

- 8:30-12:00, July 26th, 2006: **Speech Perception: Linking Computational Models and Human Data**. Strauss, T.J., Mirman, D., & Magnuson, J.S. [*28th Annual Conference of the Cognitive Science Society*](http://www.cogsci.rpi.edu/~rsun/cogsci2006/). Vancouver, Canada. 2006.

## Contact

For questions or problems with this web page, contact [Jim Magnuson](mailto:james.magnuson@uconn.edu).

## Citation

If you use jTRACE in your research, please cite this article:

- Strauss, T. J., Harris, H. D., & Magnuson, J. S. (2007). jTRACE: A reimplementation and extension of the TRACE model of speech perception and spoken word recognition. *Behavior Research Methods, 39,* 19-30. [[Publications]({{ "publications" | relative_url }})]

## References

There are three foundational papers on TRACE. [Jay McClelland](http://psychology.stanford.edu/~jlm/) has made them all available on his [publications](http://psychology.stanford.edu/~jlm/papers/) page.

1. McClelland and Elman (1986). The TRACE model of speech perception. *Cognitive Psychology, 18,* 1-86. **[This is the main original paper about the familiar version of TRACE that maps from subphonemic representations to words, which is technically "TRACE II".]**
   - An overview of this paper is presented in chapter 15 of:
     - McClelland, J. L., Rumelhart, D. E., and the PDP research group. (1986). *Parallel distributed processing: Explorations in the microstructure of cognition. Volume II.* Cambridge, MA: MIT Press.
2. Elman, J. L., & McClelland, J. L. (1986). Exploiting the lawful variability in the speech wave. In J. S. Perkell and D. H. Klatt (Eds.), *Invariance and variability of speech processes.* Hillsdale, NJ: Lawrence Erlbaum Associates, Inc. **[This chapter describes TRACE I, which focused on mapping from actual speech to phonemes. It was, however, abandoned. The time may be right for re-examining the positive aspects of this approach…]**
3. McClelland, J. L. (1991). Stochastic interactive processes and the effect of context on perception. *Cognitive Psychology, 23,* 1-44. **[In this paper, McClelland develops a stochastic (nondeterministic) version of TRACE to answer criticisms of the original model.]**

Some other papers using TRACE (PDFs of lab papers are available via our [publications]({{ "publications" | relative_url }}) page):

- Allopenna, P. D., Magnuson, J. S., and Tanenhaus, M. K. (1998). Tracking the time course of spoken word recognition using eye movements: Evidence for continuous mapping models. *Journal of Memory and Language, 38*, 419-439. **[The paper establishing the linking hypothesis between eye movements in the visual world paradigm (VWP) and response probabilities derived from TRACE.]**
- Magnuson, J. S., Dahan, D., & Tanenhaus, M. K. (2001). On the interpretation of computational models: The case of TRACE. In J. S. Magnuson and K.M. Crosswhite (Eds.), University of Rochester Working Papers in the Language Sciences, 2 (1), 71 – 91. **[The paper where we tested 3 implementations of frequency for TRACE.]**
- Dahan, D., Magnuson, J. S., Tanenhaus, M. K., and Hogan, E. M. (2001). Tracking the time course of subcategorical mismatches: Evidence for lexical competition. *Language and Cognitive Processes, 16 (5/6)*, 507-534. **[This paper demonstrates that the VWP linking hypothesis can predict very subtle patterns of eye movement behavior, including changes as a function of whether or not competitors are present in the display.]**
- Dahan, D., Magnuson, J. S., and Tanenhaus, M. K. (2001). Time course of frequency effects in spoken-word recognition: Evidence from eye movements. *Cognitive Psychology, 42*, 317-367. **[The paper where we tested 3 implementations of frequency for TRACE.]**
- Spivey, M., Grosjean, M., & Knoblich, G. (2005). Continuous attraction toward phonological competitors. Proceedings of the National Academy of Sciences, 102(29), 10393-10398. **[Links TRACE to a recurrence-normalization model to predict continuous mouse movements linked to on-line spoken word recognition.]**

## Known bugs and workarounds

If you encounter a bug in jTRACE, please carefully document the problem and the circumstances under which it occurs. Please email bug reports to [Jim Magnuson](mailto:james.magnuson@uconn.edu), with 'jtrace bug' in the subject line. Known bugs will be resolved in order of priority.

- **Help window doesn't appear.**
  - If the help documentation does not open when told, navigate to the jTRACE/doc folder and open manual.html file in a web browser.
- **Scripting**
  - Some edits made during scripting *do not cause an update of the interface*. In other words, after you change something, you don't see the result of it. This problem usually affects adding and deletion of items. As a workaround, to see the results of these changes, it is necessary to save and reload the script file.
  - *I run the script, but nothing happens.* Currently, jTRACE does not validate the contents of a script when it is run. Save and reload the script, double-check the logic of the script. If it still doesn't work, let us know.

## 3rd Party Software

jTRACE is coded in Java. The Java Web Services Developers Pack (JWSDP 1.5) is used. Two third party libraries are also included. Licenses governing their use are included in the THIRDPARTYLICENSES.txt file, included with the jTRACE download. Permission to use these tools has greatly enhanced jTRACE functionality.

- [JFreeChart](https://www.jfree.org/jfreechart/) – jfree.org
- [JaxFront](http://www.jaxfront.com/) – xcentric technology and consulting GmbH

## License

This software is copyright under the following conditions:

Permission to use, copy, and modify this software and its documentation for any purpose other than distribution-for-profit is hereby granted without fee, provided that the above copyright notice and this permission notice appear in all copies of the software and related documentation.

Permission to distribute the software or modified or extended versions thereof on a not-for-profit basis is explicitly granted, under the above conditions. HOWEVER, THE RIGHT TO DISTRIBUTE THE SOFTWARE OR MODIFIED OR EXTENDED VERSIONS THEREOF FOR PROFIT IS \*NOT\* GRANTED EXCEPT BY PRIOR ARRANGEMENT AND WRITTEN CONSENT OF THE COPYRIGHT HOLDERS.

THE SOFTWARE IS PROVIDED "AS-IS" AND WITHOUT WARRANTY OF ANY KIND, EXPRESS, IMPLIED OR OTHERWISE, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

IN NO EVENT SHALL THE UNIVERSITY OF CONNECTICUT BE LIABLE FOR ANY SPECIAL, INCIDENTAL, INDIRECT OR CONSEQUENTIAL DAMAGES OF ANY KIND, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER OR NOT ADVISED OF THE POSSIBILITY OF DAMAGE, AND ON ANY THEORY OF LIABILITY, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
