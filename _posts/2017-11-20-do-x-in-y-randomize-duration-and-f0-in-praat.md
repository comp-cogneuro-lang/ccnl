---
title: "Do X in Y: Randomize duration and F0 of speech files in Praat"
tags: do-x-in-y
---

**Summary:** I describe a script that makes random modifications to duration and pitch. It can serve as an example for how to read in all .wav files in a directory and modify them from the command line.

For a machine learning project, we wanted to induce variability in a set of speech files without recording more tokens of our critical words. We thought, "let's just use a Praat script to randomly jigger duration and F0 — that can't be hard, can it?" Well, it is harder than I thought given that I don't really grok Praat scripting — it is the most foreign and strange programming language I've ever encountered.

After consulting with various colleagues, I remembered that Sergey Kornilov had used a script to compress lots of files for a project. He sent me his script. I found a script by Shigeto Kawahara of Keio U. in Japan that modified pitch. Putting them together, I now have a script that is called from the command line and reads in all .wav files in a directory (the directory where the script is located), randomly compresses/expands the file according to a hard-coded range (i.e., you have to change the values in the file), randomly adjusts pitch (by multiplying by a scalar), and writes the resulting file in a folder called `output` that must exist in the starting directory. The file names include tags indicating how duration and pitch were modified. Here's the script. I hope someone else finds it helpful! You can copy the code and paste it into a text document that you might call something like `vary_duration_and_pitch.praat`.

— jim magnuson

{% raw %}
```praat
# 2017.11.17, Jim Magnuson, based on a compression script by
# Sergey Kornilov and a pitch modification script by
# Shigeto KAWAHARA of Keio U.
# (http://user.keio.ac.jp/~kawahara/scripts/changeF0_e.praat)
# kludgy script to shift pitch by random factor between
# minF0 and maxF0 and compress/expand by random factor between
# minComp and maxComp.
# It does this for every .wav file in the directory where the
# script is located, and writes resulting files in ./output
# (so you must create a folder called output; note
# that the script will overwrite files in that directory
# without warning!).
# The output files have _dur_X and _f0_Y inserted in their
# names. For example, _dur_87 means compression to factor of
# 0.87, _dur_108 means compression (expansion) to factor of
# 1.08, etc.

# set locations
inputDir$ = "./"
outputDir$ = "./output/"

# set ranges for pitch and compression
minF0 = 0.5
maxF0 = 2.0
minComp = 0.5
maxComp = 2.0

# used to incorporate duration and F0 changes
# in out file name
resolution = 100

# read *.wav filenames into strings
strings = Create Strings as file list: "list", inputDir$ + "/*.wav"
numberOfFiles = Get number of strings

# now loop through .wav list
for ifile to numberOfFiles

    # open file in position ifile in string list
    filename$ = Get string... ifile

    # give a little info on the console re: progress
    appendInfoLine: "Working on " + inputDir$ + filename$

    # read the actual file
    Read from file: inputDir$ + filename$

    # set random duration factor
    duration_scalar = randomUniform(minComp, maxComp)

    # LENGTHEN AND RESYTHESIZE IN ONE STEP USING PSOLA
    # 75 and 600 are standard parameters for the
    # frequency range (hz) used in periodicity analysis;
    # the last argument is the compression factor
    Lengthen (PSOLA)... 75 600 duration_scalar

    # RANDOMIZING F0
    # this is going to require Manipulation commands,
    # so we need to select the sound; let's name it
    this_sound$ = selected$ ("Sound")

    # grab it + give params for onset of analysis window and
    # frequency range used for periodicty analysis
    To Manipulation... 0.01 75 600

    # pop pitch tier into memory (apparently)
    Extract pitch tier

    # set random pitch change factor
    pitch_scalar = randomUniform(minF0, maxF0)

    # modify pitch of the pitch tier in memory
    Formula... self * pitch_scalar;

    # reselect the sound and replace pitch tier
    select Manipulation 'this_sound$'
    plus PitchTier 'this_sound$'
    Replace pitch tier

    # reselect the sound??? and resythesize
    select Manipulation 'this_sound$'
    Get resynthesis (PSOLA)

    # SAVE RESULTING FILES
    # create rounded versions of the pitch and
    # duration factors for use in filename
    pitch_scalar_rounded = round(pitch_scalar * resolution)
    duration_scalar_rounded = round(duration_scalar * resolution)
    filenameDur$ = " 'filename$'" - ".wav" + "_dur" + "_" + string$(duration_scalar_rounded) + "_f0" + "_" + string$(pitch_scalar_rounded) + ".wav"

    # update user and write to file
    appendInfoLine: "* writing to " + outputDir$ + filenameDur$
    Write to WAV file: outputDir$ + filenameDur$
    select Strings list

endfor

select all
Remove

# end of script
```
{% endraw %}
