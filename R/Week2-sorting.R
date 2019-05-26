demographics <- read.csv("demographicsgraphics.csv")

View(demographics)

### how to sort a data frame

### a new data frame, demographics2, will be created each time

### sort by income, ascending (default)

demographics2 <- demographics[order(demographics$income),]

View(demographics2)

### sort by income, descending

demographics2 <- demographics[order(-demographics$income),]

View(demographics2)

### sort by income and age 

demographics2 <- demographics[order(demographics$income, demographics$age),]

View(demographics2)


### sort by income (ascending) and age (descending)

demographics2 <- demographics[order(demographics$income, -demographics$age),]

View(demographics2)
