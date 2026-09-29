---
title: "Do X in Y: Convert values to subject-relative z-scores in R"
tags: do-x-in-y
---

I set out to do something that seemed like it shouldn't be too hard in R. I had a dataframe with RTs for a bunch of subjects, and I wanted to convert the RTs to z-scores relative to each subject's own mean. To do this relative to the global mean is super easy:

```r
data$global_zRT <- scale(data$RT)
```

However, getting it scaled by subject mean (which could be useful for visual inspection of data, or for some analyses) turns out not to be trivial, and I was unable to find relevant posts via google search. Before posting to stackoverflow myself, I tried our lab Slack channel. Dave Saltzman and Anne Marie Crinnion produced a solution quickly with dplyr. However, my dplyr calls were getting blocked by plyr. Anne Marie pointed out how to make the command bullet proof. Note that 'subject' here is a column in the dataframe, not a keyword of some sort.

```r
data <- data %>% dplyr::group_by(subject) %>% dplyr::mutate(zRT = scale(RT))
```

— Jim Magnuson
