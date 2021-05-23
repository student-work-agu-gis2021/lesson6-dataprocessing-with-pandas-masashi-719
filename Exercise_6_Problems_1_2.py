#!/usr/bin/env python
# coding: utf-8

# # Exercise 6: Weather data calculation
# 
# ### Part 1 
# 
# You should start by reading the data file.
# 
# - Read the data file into variable the variable `data`
#     - Skip the second row
#     - Convert the no-data values (`-9999`) into `NaN`


import pandas as pd
import numpy as np

data = None

# YOUR CODE HERE 1
# Put the data in a variable
f="data/1091402.txt"
# Read data according to conditions
# 'delim_whitespace=True'　is use to separate spacce 'skiprows' use to skip the second row and 'na_values' use to  Convert the no-data values (-9999) into NaN
data=pd.read_csv(f,delim_whitespace=True,skiprows=[1],na_values=[-9999])
# Check that the dataframe looks ok:
print(data.head())
# Check the last rows of the data (there should be some NaN values)
print(data.tail())

# ### Part 2 
# 
# In this section, you will calculate simple statistics based on the input data:
# 
# - Calculate how many no-data (NaN) values there are in the `TAVG` column
#     - Assign your answer to a variable called `tavg_nodata_count`.

tavg_nodata_count = None
#YOUR CODE HERE 2
# calicurate the number of Nan in the TAVG clum
# TAVG is 7 th. so I write iloc[:,6] and tne number that i want yo find is NaN .so i added isnull and sum
tavg_nodata_count=data.iloc[:,6].isnull().sum()

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Number of no-data values in column "TAVG":',tavg_nodata_count)
#CAUTION!!! DON'T EDIT THIS PART END


# - Calculate how many no-data (NaN) values there are for the `TMIN` column
#     - Assign your answer into a variable called `tmin_nodata_count`

tmin_nodata_count = None
#YOUR CODE HERE 3
# TAVG is 9 th. so I write iloc[:,8] and tne number that i want yo find is NaN .so i added isnull and sum
tmin_nodata_count=data.iloc[:,8].isnull().sum()
# Calculate how many no-data (NaN) values there are for the TMIN column
# calicurate the number of Nan in the TMIN clum

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Number of no-data values in column "TMIN":', tmin_nodata_count)
#CAUTION!!! DON'T EDIT THIS PART END


# - Calculate the total number of days covered by this data file
#     - Assign your answer into a variable called day_count

day_count = None 
#YOUR CODE HERE 4
# total number of day
day_count=len(data)
#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print("Number of days:", day_count)
#CAUTION!!! DON'T EDIT THIS PART END

# - Find the date of the oldest (first) observation
#     - Assign your answer into a variable called `first_obs`


first_obs = None
 
# YOUR CODE HERE 5
# number of first obseervation day 
first_obs=data.iat[0,4]
#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Date of the first observation:',first_obs)
#CAUTION!!! DON'T EDIT THIS PART END

# - Find the date of the most recent (last) observation
#     - Assign your answer into a variable called `last_obs`

last_obs = None

# YOUR CODE HERE 6
# number of last obseervation day 
last_obs=data.iat[day_count-1,4]
#CAUTION!!! DON'T EDIT THIS PART START
# Print o
# ut the solution:
print('Date of the last observation:', last_obs)
#CAUTION!!! DON'T EDIT THIS PART END


# - Find the average temperature for the whole data file (all observtions) from column `TAVG`
#     - Assign your answer into a variable called `avg_temp`

avg_temp = None

# YOUR CODE HERE 7
# number of average tempreture
avg_temp=np.mean(data.iloc[:,6])
#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Average temperature (F) for the whole dataset:', round(avg_temp, 2))
#CAUTION!!! DON'T EDIT THIS PART END


# - Find the average `TMAX` temperature over the Summer of 1969 (months May, June, July, and August of the year 1969)
#     - Assign your answer into a variable called `avg_temp_1969`

avg_temp_1969 = None

# YOUR CODE HERE 8

# average temperature over the Summer of 1969
avg_temp_1969=data['TMAX'].loc[(data['DATE']>=19690501) & (data['DATE']<=19690831)].mean()



#CAUTION!!! DON'T EDIT THIS PART START
# This test print should print a number
print('Average temperature (F) for the Summer of 69:', round(avg_temp_1969, 2))
#CAUTION!!! DON'T EDIT THIS PART END


# ## Problem 2 - Calculating monthly average temperatures (*3 points*)
# 

monthly_data = None

# YOUR CODE HERE 9
# Create a function
def fahr_to_celcius(temp_fahrenheit):
  # Change from Fahrenheit to Celsius
  converted_temp=(temp_fahrenheit-32)/1.8
  # return the number
  return converted_temp
# Apply a function to the data
  data['TAVG']=data['TAVG'].apply(fahr_to_celcius)
  # create the data frame
  monthly_data=pd.DataFrame()
  # Change to a string
  data['TIME_STR']=data['DATE'].astype(str)
  # Cut out each value
  data['YEAR']=data['TIME_STR'].str.slice(start=0,stop=4)
  # Cut out each value
  data['MONTH']=data['TIME_STR'].str.slice(start=0,stop=6)
  # Put together the data
  grouped=data.groupby(['YEAR','MONTH'])
  # Put a value
  mean_col=['TAVG']
  # for sentence
  for key,group in grouped:
    # get the mean of TAVG
    mean_values=group[mean_col].mean()
    # Add mean_value to monthly_data
    monthly_data=monthly_data.append(mean_values,ignore_index=True)
    new_name={'TAVG':'temp_celsius'}
    # change the name
    monthly_data=monthly_data.rename(columns=new_name)

#CAUTION!!! DON'T EDIT THIS PART START,ignore_index=True
# This test print should print the length of variable monthly_data
print(len(monthly_data))

# This test print should print the column names of monthly_data
print(monthly_data.columns.values)

# This test print should print the mean of temp_celsius
print(round(monthly_data['temp_celsius'].mean(),2))

# This test print should print the median of temp_celsius
print(round(monthly_data['temp_celsius'].median(), 2))
#CAUTION!!! DON'T EDIT THIS PART END

def func1():
    return tavg_nodata_count
def func2():
    return tmin_nodata_count
def func3():
    return day_count
def func4():
    return first_obs
def func5():
    return last_obs
def func6():
    return round(avg_temp,2)
def func7():
    return round(avg_temp_1969,2)
def func8():
    return len(monthly_data)
def func9():
    return monthly_data.columns.values
def func10():
    return round(monthly_data['temp_celsius'].mean(),2)
def func11():
    return round(monthly_data['temp_celsius'].median(),2)