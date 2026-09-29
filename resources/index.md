---
title: Resources
---

# {% include icon.html icon="fa-solid fa-box-open" %}Resources

## jTRACE

**[Go to the jTRACE page]({{ "resources/jtrace" | relative_url }})**

jTRACE is a reimplementation of the TRACE model with a user-friendly interface and new tools (batch processing, scripting, graphing and visualization).

## Do X in Y

This is a repository of lab notes, where X might be "batch adjust F0 in speech files" and Y might be "Praat", or X in Y = "create a hash table" in "R". The idea is to have a quick place to put our notes about common or uncommon tasks so that we stop reinventing various wheels.

- [Convert values to subject-relative z-scores in R]({{ site.baseurl }}{% post_url 2021-02-09-do-x-in-y-subject-relative-z-scores-in-r %}) (2021)
- [Install lens in Ubuntu linux]({{ site.baseurl }}{% post_url 2018-10-25-do-x-in-y-install-lens-in-ubuntu-linux %}) (2018)
- [Use a function to save many plots to a list in R]({{ site.baseurl }}{% post_url 2018-05-01-do-x-in-y-save-many-plots-to-a-list-in-r %}) (2018)
- [Randomize duration and F0 of speech files in Praat]({{ site.baseurl }}{% post_url 2017-11-20-do-x-in-y-randomize-duration-and-f0-in-praat %}) (2017)

You can also [browse all "Do X in Y" posts on the blog]({{ "blog" | relative_url }}?search=%22tag:%20do-x-in-y%22).

## Growth curve analysis

**Growth Curve Analysis of VWP Data.** These resources have moved to [Dan Mirman's site](http://www.danmirman.org/gca). You will find the original page that accompanied our article as well as Dan's recent extensions.

## Methods reports

{% capture archival %}
**Archival.** The methods reports below date from 2003–2008 and are kept for historical reference. They are obsolete (for example, they target old versions of E-Prime and ISCAN eye trackers), and no support is available. Files are linked only where we still have them.
{% endcapture %}
{% include alert.html type="warning" content=archival %}

These reports represent our lab's effort to promote methods recycling. These reports are freely available to people from outside our lab with the warning that we make no promises to provide technical support, although we will try to answer questions.

Note that a lot of the programming (reports 2003.01 to 2003.06) was done by Jim Magnuson, who simply doesn't know how to program. These all seem to work well enough for us, but they have not yet been subjected to extensive testing, some parts may not work with future revisions of E-Prime, etc.: we're motivated to make these work, but cannot guarantee their quality or continued upgrading and support. That said, please feel to use these, improve them, or put them to new uses. We'd be thrilled to hear comments or suggestions, or, especially, to see improvements or new uses.

| Report | Title | Author | Link | Size | Release | Update |
|--------|-------|--------|------|------|---------|--------|
| 2003.01 | Playing sound from E-Prime InLine Scripts | J. Magnuson | | 335k | 4.22.03 | 4.22.03 |
| 2003.02 | Specifying stimulus paths in E-Prime | J. Magnuson | | 87k | 4.22.03 | 4.22.03 |
| 2003.03 | Constraining and controlling mouse input from E-Prime InLine Scripts | J. Magnuson | | 105k | 4.22.03 | 4.22.03 |
| 2003.04 | Integrating an eye tracker with E-Prime via serial port communication | J. Magnuson | [.zip]({{ "resources/methods/mr2003.04_ET_with_EP.zip" | relative_url }}) | 171k | 4.22.03 | 11.18.03 |
| 2003.05 | *IscanEyeTracker.epk*: An E-Prime package for eye tracking via serial port communication. This is free software as defined by the GPL. See accompanying license. NB: The original version of this package contained a serious timing bug. As of 18 November 2003, the version here corrects that bug and adds several other improvements. *NB: We no longer use ISCAN eye trackers. No support is available for this package, but it would be a good starting point for developing your own package for any eye tracker.* | J. Magnuson | [.zip]({{ "resources/methods/mr2003.05_EtPackage.zip" | relative_url }}) | 434k | 4.22.03 | 11.18.03 |
| 2003.06 | E-Prime example script using sound, mouse control and constraint, eye tracking, and random stimulus placement | J. Magnuson | [.zip]({{ "resources/methods/mr2003.06_allTogether.zip" | relative_url }}) | 1.4M | 4.22.03 | 11.18.03 |
| 2004.01 | Using a mouse-directed focus window in E-Prime. | H. Harris | | 317k | 11.30.04 | 11.30.04 |
| 2004.02 | Building composite images on the fly in E-Prime | H. Harris | | 143k | 11.30.04 | 11.30.04 |
| 2006.01 | Sending signals from E-Prime to the BioSemi EEG system | D. Mirman | | | | |
| 2006.02 | Hindering effects of feedback in the TRACE model of spoken word recognition | T. Strauss | | 744k | 12.04.06 | 12.04.06 |
| 2008.01 | A bunch of snack tools for batch processing audio files | J. Magnuson | | | 04.18.08 | |
| 2008.02 | Installing lens in OS X | J. Magnuson | [html]({{ "resources/methods/lens-os-x" | relative_url }}) | | 06.10.08 | |
