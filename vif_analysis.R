##################################################################################
## Script original: vif_analysis.R
##
## Dummy example of calculating the Variance Inflation Factor(VIF)
##
##################################################################################


setwd("c:/Users/MIKLOS/Data/_Python_projects/_github/")

library("readxl")

df <- read.csv("titanic-data.csv")

# Delete Rows Containing NaN Using 
df <- na.omit(df)

# create linear model
model <- lm(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare, data = df)
# summary(model)

#load the car library
library(car)

#calculate the VIF for each predictor variable in the model
vif <- vif(model)
# print(vif)

library(data.table)
vif <- data.frame(as.list(vif)) 

#transpose data frame
df_vif <- transpose(vif)

#redefine row and column names
rownames(df_vif) <- colnames(vif)
colnames(df_vif) <- c("VIF")

# print the stuff
print(df_vif)

