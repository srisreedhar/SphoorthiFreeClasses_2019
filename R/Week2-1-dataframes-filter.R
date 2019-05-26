
# Sphoorthi Oum
## Load data from the CSV folder, download and save it in the directory


demographicsgraphics <- read.csv("demographicsgraphics.csv")

View(demographics)

### how to filter (select) your data data in base R using brackets 

### a new data frame, demographics2, will be created each time

######
### one filter variable
######

### select the female subjects 

demographics2 <- demographics[demographics$gender == "Female",]

View(demographics2)

### retain the subjects with the income greater than 100

demographics2 <- demographics[demographics$income > 100,]

View(demographics2)

### if you want to keep only the variables 1, 3 and 7
### (age, income and gender)

demographics2 <- demographics[demographics$income > 100, c(1,3,7)]

View(demographics2)

### if you want to drop variables 6, 7 and 8
### (car category, gender and retired)

demographics2 <- demographics[demographics$income > 100, -c(6:8)]

View(demographics2)

######
### two or more filter variables
######

### select the female subjects with the income over 100

demographics2 <- demographics[demographics$gender == "Female" & demographics$income > 100,]

View(demographics2)
