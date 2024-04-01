### Script for Plotting a Reaction Norm Using Powdery Mildew Screen Data for Hop Release ###
## Author: Patrick Woods ##
## Date: April 1, 2024 ##


library(ggplot2)
pm <- read.csv(file.choose(),header=T)

pm$Identifier <- as.factor(pm$Identifier)
pm$Dish <- as.factor(pm$Dish)
pm$Mildew <- as.factor(pm$Mildew)
pm$Mildew_Code <- as.factor(pm$Mildew_Code)

#reaction norm plot#
ggplot(pm, aes(x = Mildew_Code, y = Colony.count)) +
       stat_summary(aes(group = Identifier, color = Identifier), fun.y = mean, geom = "line") +
       stat_summary(aes(color = Identifier), fun.data = mean_se, geom = "errorbar", width = 0.1) +
       stat_summary(aes(color = Identifier), fun.y = mean, geom = "point", size = 4, alpha=0.6) +
       xlab('Powdery Mildew Race') + ylab('Mean Colony Counts')  + theme_bw()




