# Sphoorthi Oum
## Load the dataSet and practise below exercises

demographics <- read.csv("demographicsgraphics.csv")

View(demographics)

### how to filter (select) your data in base R using subsets

### a new data frame, demographics2, will be created each time

### keep the married subjects only
### (one filter variable)

demographics2 <- subset(demographics, marital == "Married")

View(demographics2)

### retain the married subjects aged over 35
### (two filter variables)

demographics2 <- subset(demographics, marital == "Married" & age > 35)

View(demographics2)

### keep the first three variables only
### (age, marital status, income)

demographics2 <- subset(demographics, marital == "Married" & age > 35, select = c(1:3))

View(demographics2)

### drop variables 4, 5, 6 and 8
### (education, car price, car category, retired)

demographics2 <- subset(demographics, marital == "Married" & age > 35, select = -c(4:6, 8))

View(demographics2)
