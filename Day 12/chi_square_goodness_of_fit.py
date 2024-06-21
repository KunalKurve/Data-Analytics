'''
Here we use stats.chisquare
Primarily used for conducting a chi-square goodness-of-fit test, which compares observed frequencies with expected frequencies under a specified theoretical distribution
'''

import numpy as np
import pandas as pd
import scipy.stats as stats

# fake demographic data for U.S. and Minnesota state and walk through the chi-square goodness of fit test to check whether they are different:

national = pd.DataFrame(["white"]*100000 + ["hispanic"]*60000 +\
                        ["black"]*50000 + ["asian"]*15000 + ["other"]*35000)
           

minnesota = pd.DataFrame(["white"]*600 + ["hispanic"]*300 + \
                         ["black"]*250 +["asian"]*75 + ["other"]*150)

print(national)
print(minnesota)

# create frequency tables (crosstabs) for both datasets using pd.crosstab. national_table and minnesota_table store the counts of each demographic category.
national_table = pd.crosstab(index=national[0], columns="count")
minnesota_table = pd.crosstab(index=minnesota[0], columns="count")

print( "National")
print(national_table)
print(" ")
print( "Minnesota")
print(minnesota_table)

observed = minnesota_table

national_ratios = national_table/len(national)  # Get population ratios

# calculate the expected counts by multiplying the population ratios in the national dataset by the total number of observations in the Minnesota dataset.
expected = national_ratios * len(minnesota)   # Get expected counts

# calculate the chi-squared statistic by comparing the observed and expected counts and summing the squared differences, normalized by the expected counts.
chi_squared_stat = (((observed-expected)**2)/expected).sum()

print ("Calculated observed value")
print(chi_squared_stat)

'''
Similar to the t-test where we compared the t-test statistic to a critical value based on the t-distribution to determine whether the result is significant, in the chi-square test we compare the chi-square test statistic to a critical value based on the chi-square distribution. The scipy library shorthand for the chi-square distribution is chi2. Let's use this knowledge to find the critical value for 95% confidence level and check the p-value of our result:
'''


# find the critical value for a 95% confidence level with 4 degrees of freedom.

crit = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 4)   # Df = number of variable categories - 1

print("Critical value")
print(crit)

# calculate the p-value based on the chi-squared statistic and degrees of freedom.
p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,  # Find the p-value
                             df=4)
print("P value")
print(p_value)

'''
Since our chi-squared statistic exceeds the critical value, we'd reject the null hypothesis that the two distributions are the same.

You can carry out a chi-squared goodness-of-fit test automatically using the scipy function scipy.stats.chisquare():
'''

print("Observed value through Stats library")
print(stats.chisquare(f_obs= observed,   # Array of observed counts
                f_exp= expected)) 
# The test results agree with the values we calculated above.
