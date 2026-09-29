---
title: "Do X in Y: Use a function to save many plots to a list in R"
tags: do-x-in-y
---

You know that miserable feeling when you realize you are copying and pasting snippets of code and modifying them with hard-coded variables? I usually ignore it and press on, but last night, I took the time to convert my code to a function. It was surprisingly easy (it took maybe 5 minutes), and had unexpected benefits. For example, the task I was doing required creating many (e.g., 8-30) ggplot objects, pushing them into a list, and then using multiplot to create PDFs. Every time I ran a chunk of code for one set of graphs, I found myself fidgeting while R Studio created each of the graphs in the plot window. My efforts to suppress that unwanted plotting were for naught, but when I converted to a function, all that extra plotting went away. Creating a 16-panel plot is probably 10x faster using the function! Here's the code for the function (apologies to any programmers whose sensibilities I offend; I'm a hack, not a hacker).

{% raw %}
```r
#####################################################################################
# 2018.04.30, Jim Magnuson
library(foreach)
library(ggplot2)
library(scales)

plot.to.list <- function(dat, x.vars, x.names, y.vars, y.names, textsize=12,
                         jitteramount=0.1, ...) {
  someplots <- list()
  at = 0
  foreach(xvar=x.vars, xname=x.names) %do% {
    foreach(yvar=y.vars,yname=y.names) %do% {
      # First, get correlation between the current pair
      # NB: the 'get' command is crucial for evaluating the
      # strings as variable names, but this doesn't work in
      # the ggplot code below
      acor = sprintf("%.3f",with(dat, cor(get(xvar),get(yvar)) ))
      at = at + 1 # increment list position
      # now add a ggplot object to the list
      # NB: instead of 'get', we use 'aes_string' in place of 'aes'
      someplots[[at]] <- ggplot(dat,aes_string(x=xvar,y=yvar)) +
        geom_jitter(position=position_jitter(jitteramount)) +
        geom_smooth(method='lm', se=FALSE, linetype="dashed") +
        scale_x_continuous(breaks= pretty_breaks()) + # from scales, try it, you'll like it
        scale_y_continuous(breaks= pretty_breaks()) +
        theme(plot.title = element_text(hjust = 1)) + # right justify title
        theme(panel.background = element_rect(colour="black", fill="white"),
              axis.text.x = element_text(size=textsize, face="plain", colour="black"),
              axis.text.y = element_text(size=textsize, face="plain", colour="black"),
              axis.title.x = element_text(size=textsize, face="bold", colour="black", vjust=-.4),
              plot.title = element_text(size=11),
              axis.title.y = element_text(size=textsize, face="bold", colour="black", vjust=1)) +
        xlab(xname) + ylab(yname) +
        ggtitle(paste("r =",acor)) # plot r as title
    }
  }
  return(someplots)
}
####################################################################################

yvars=c("RT","RT_lenC") # variables w/in trace.sub I want to be on y axes
ynames=c("RT", "Adjusted RT") # Better labels than the variable names
xvars=c("NB", "DEL", "ADD", "SUB") # more trace.sub vars that I want on x axes
xnames=c("Neighbors", "Deletions", "Additions", "Substitutions") # Better labels
# now call the function:
nb.plots = plot.to.list(dat=trace.sub, x.vars=xvars, y.vars=yvars,
                        x.names=xnames, y.names=ynames)

# now create a PDF with all the plots
pdf("trace_neighbor_types.pdf",height=7,width=13.7)
# get multiplot function here:
#      http://www.cookbook-r.com/Graphs/Multiple_graphs_on_one_page_(ggplot2)/
multiplot(plotlist = nb.plots, cols=4)
dev.off()
```
{% endraw %}
