#!/usr/bin/env Rscript 

# Boxplot of MPG by Car Cylinders 
boxplot(mpg~cyl,data=mtcars, main="Car Milage Data", 
    xlab="Number of Cylinders", ylab="Miles Per Gallon")
