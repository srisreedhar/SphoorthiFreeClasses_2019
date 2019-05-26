
# Sphoorthi Oum


# for complete dplyr tutorial on 
# Select
# Filter
# arrange
# mutate
# summarize
# groupby

# refer to class notes. 
# I've only included filtering here .


demographics <- read.csv("demographicsgraphics.csv")

View(demographics)

### how to filter (select) your data using the dplyr package

### a new data frame, demographics2, will be created each time

### load the package

require(dplyr)

### keep the unmarried subjects only
### (one filter variable)

demographics2 <- filter(demographics, marital == "Unmarried")

View(demographics2)

### keep the unmarried subjects only aged under 50
### (two filter variables)

demographics2 <- filter(demographics, marital == "Unmarried", age < 50)

View(demographics2)

### if you want to keep some variables only,
### you must first specify the variables you want to keep

### suppose we want to keep only the first three variables
### (age, marital status, income)

demographics2 <- select(demographics, age, marital, income)

View(demographics2)

### next we filter our new data frame demographics2, 
### keeping only the unmarried persons aged under 50

demographics2 <- filter(demographics2, marital == "Unmarried", age < 50)

View(demographics2)
