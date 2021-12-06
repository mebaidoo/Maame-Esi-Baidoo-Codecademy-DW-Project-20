import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob
#Using glob to get all the csv files whose names start with states
files = glob.glob("states*.csv")
print(files)
#Getting the dataframe of each file and appending to df_list
df_list = []
for filename in files:
  df_list.append(pd.read_csv(filename))
#Combining all the dataframes
us_census = pd.concat(df_list)
#Checking the columns and data types of the dataframe
print(us_census.columns)
print(us_census.dtypes)
#Checking the head of the dataframe to understand wwhy some dtypes are objects
print(us_census.head())
#Taking out the $ signs from the Income column and making it numerical for easy statistical computations
us_census["Income"] = us_census["Income"].replace("[$]", "", regex = True)
us_census["Income"] = pd.to_numeric(us_census["Income"])
print(us_census.head())
print(us_census.dtypes)
#Splitting the strings in the GenderPop column into two different columns
us_census["Male Population"] = us_census["GenderPop"].str.split("_", expand = True)[0]
us_census["Female Population"] = us_census["GenderPop"].str.split("_", expand = True)[1]
print(us_census.head())
#Stripping M and F from the male and female population columns and making the values numeric
us_census["Male Population"] = pd.to_numeric(us_census["Male Population"].str.strip("M"))
us_census["Female Population"] = pd.to_numeric(us_census["Female Population"].str.strip("F"))
print(us_census.head())
print(us_census.dtypes)
#Using matplotlib to make a scatterplot of the number of women in each country to the average income
#plt.scatter(us_census["Female Population"], us_census["Income"])
#plt.show()
#Looks like a lot of the higher-income countries have lesser women
#Checking if the female population column has nan values and then filling nan values with  number
print(us_census["Female Population"])
us_census["Female Population"] = us_census["Female Population"].fillna(us_census["TotalPop"] - us_census["Male Population"])
print(us_census["Female Population"])
#Checking if there are duplicates and dropping the duplicates
print(us_census.duplicated())
us_census = us_census.drop_duplicates()
#Making the female population to average income scatter plot again after dropping any duplicates and filling missing values
#plt.scatter(us_census["Female Population"], us_census["Income"])
#plt.show()
#Drawing histograms from the race olumns
print(us_census.columns)
#Convert the values in the column into a format that is numerical first
us_census["Hispanic"] = pd.to_numeric(us_census["Hispanic"].str.strip("%"))
us_census["White"] = pd.to_numeric(us_census["White"].str.strip("%"))
us_census["Black"] = pd.to_numeric(us_census["Black"].str.strip("%"))
us_census["Native"] = pd.to_numeric(us_census["Native"].str.strip("%"))
us_census["Asian"] = pd.to_numeric(us_census["Asian"].str.strip("%"))
us_census["Pacific"] = pd.to_numeric(us_census["Pacific"].str.strip("%"))
#Filling in missing values with 0 assuming there is no kind of the race in that country
us_census["Hispanic"].fillna(0, inplace = True)
us_census["White"].fillna(0, inplace = True)
us_census["Black"].fillna(0, inplace = True)
us_census["Native"].fillna(0, inplace = True)
us_census["Asian"].fillna(0, inplace = True)
us_census["Pacific"].fillna(0, inplace = True)
print(us_census.head())
#Drawing a histogram for each race to see which race has more countries having more of them
hist_hispanic = us_census["Hispanic"].hist()
plt.show()
plt.clf()
hist_white = us_census["White"].hist()
plt.show()
plt.clf()
hist_black = us_census["Black"].hist()
plt.show()
plt.clf()
hist_native = us_census["Native"].hist()
plt.show()
plt.clf()
hist_asian = us_census["Asian"].hist()
plt.show()
plt.clf()
hist_pacific = us_census["Pacific"].hist()
plt.show()