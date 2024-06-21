# -*- coding: utf-8 -*-
"""
Q. Indians and elections are the things which keeps on happening almost every month and every year.
Well, Loksabha elections is one such which happens after every 5 years, well we have data of
candidates and electors from 2009 and 2014. Compare the dataset and compute the results visually
1. Create grand alliances
a. 'INC','NCP', 'RJD', 'DMK', 'IUML',
'JMM','JD(s)','KC(M)','RLD','RSP','CMP(J)','KC(J)','PPI','MD' as UPA
b. 'BJP','SS', 'LJP', 'SAD', 'RLSP',
'AD','PMK','NPP','AINRC','NPF','RPI(A)','BPF','JD(U)','SDF','NDPP','MNF','RIDALOS','KM
DK','IJK','PNK','JSP','GJM','MGP','GFP','GVP','AJSU','IPFT','MPP','KPP','JKPC','KC(T)','BDJ
S','AGP','JSS','PPA','UDP','HSPDP','PSP','JRS','KVC','PNP','SBSP','KC(N)','PDF','MDPF' as
NDA
c. 'YSRCP','AAAP', 'IND', 'AIUDF', 'BLSP', 'JKPDP', 'JD(S)', 'INLD', 'CPI', 'AIMIM',
'KEC(M)','SWP', 'NPEP', 'JKN', 'AIFB', 'MUL', 'AUDF', 'BOPF', 'BVA', 'HJCBL',
'JVM','MDMK' as Others
2. Create Winning seats distribution by Major Political Parties & Alliances for 2009 & 2014
3. How many seats won by Alliances and Major Political Parties ?

4. Plot comparatively seats won based on candidate category as General, ST and SC for 2009 &
2014
5. Plot the age distribution of winners of both 2014 and 2009 elections
6. Separately plot age distribution of NDA & UPA candidates
7. Plot Gender distributions of 2009 & 2014 elections
8. Plot gender distribution of NDA and UPA separately for 2009 elections
9. Plot gender distribution of NDA and UPA separately for 2014 elections
10. Plot the poll percentage of states for 2009 & 2014 elections

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv("LS2009Electors.xls")
print(df1.info())

df2 = pd.read_csv("LS2009Candidate.xls")
print(df2.info())

df3 = pd.read_csv("LS2014Electors.xls")
print(df3.info())

df4 = pd.read_csv("LS2014Candidate.xls")
print(df4.info())

# Create Alliances
UPA_parties = ['INC','NCP', 'RJD', 'DMK', 'IUML','JMM','JD(s)','KC(M)','RLD','RSP','CMP(J)','KC(J)','PPI','MD']
NDA_parties = ['BJP','SS', 'LJP', 'SAD', 'RLSP','AD','PMK','NPP','AINRC','NPF','RPI(A)','BPF','JD(U)','SDF','NDPP','MNF','RIDALOS','KMDK','IJK','PNK','JSP','GJM','MGP','GFP','GVP','AJSU','IPFT','MPP','KPP','JKPC','KC(T)','BDJS','AGP','JSS','PPA','UDP','HSPDP','PSP','JRS','KVC','PNP','SBSP','KC(N)','PDF','MDPF']
Others_parties = ['YSRCP','AAAP', 'IND', 'AIUDF', 'BLSP', 'JKPDP', 'JD(S)', 'INLD', 'CPI', 'AIMIM','KEC(M)','SWP', 'NPEP', 'JKN', 'AIFB', 'MUL', 'AUDF', 'BOPF', 'BVA', 'HJCBL','JVM','MDMK']

def classify_alliance(party):
    if party in UPA_parties:
        return 'UPA'
    elif party in NDA_parties:
        return 'NDA'
    else:
        return 'Others'
    
# Create new column of Alliance
df2['Alliance'] = df2['Party Abbreviation'].apply(classify_alliance)
df4['Alliance'] = df4['Party Abbreviation'].apply(classify_alliance)

concat_can_df = pd.concat([df2, df4])
print("Alliance Info: ")
print(concat_can_df['Alliance'].value_counts())

winner_df = concat_can_df[concat_can_df['Position'] == 1]
winner_df.info()

concat_ele_df = pd.concat([df1, df3])

seats_09 = winner_df[winner_df['Year']==2009]
seats_09_won = seats_09['Alliance'].value_counts()


# plt.figure(figsize=(10, 8))
plt.pie(seats_09_won, labels=seats_09_won.index,  autopct='%1.1f%%')
plt.title('Winning Seats Distribution by Alliances in 2009')
plt.legend()
plt.tight_layout()
plt.show()

seats_14 = winner_df[winner_df['Year']==2014]
seats_14_won = seats_14['Alliance'].value_counts()


# plt.figure(figsize=(10, 8))
plt.pie(seats_14_won, labels=seats_14_won.index,  autopct='%1.1f%%')
plt.title('Winning Seats Distribution by Alliances in 2014')
plt.legend()
plt.tight_layout()
plt.show()

print("Seats won by Alliance in 2009: ",seats_09_won.head())
print("\nSetas won by Allaince in 2014: ",seats_14_won)

# category
cat_counts_2009 = seats_09['Candidate Category'].value_counts()
cat_counts_2014 = seats_14['Candidate Category'].value_counts()

# Create a DataFrame from the counts
category_df = pd.DataFrame({
    '2009': cat_counts_2009,
    '2014': cat_counts_2014
})

# Plot the data
category_df.plot(kind='bar')
plt.title('Seats Won Based on Candidate Category for 2009 & 2014')
plt.xlabel('Candidate Category')
plt.ylabel('Number of Seats Won')
plt.xticks(rotation=0)
plt.legend(title='Year')
plt.tight_layout()
plt.show()

# Plot the poll percentage for each state in 2009 & 2014
# 2009
plt.hist(seats_09['Candidate Age'], bins=20, alpha=0.5, label='2009 Winners')
# 2014
plt.hist(seats_14['Candidate Age'], bins=20, alpha=0.5, label='2014 Winners')

plt.title('Age Distribution of Winners in 2009 and 2014 Elections')
plt.xlabel('Age')
plt.ylabel('Number of Winners')
plt.legend()
plt.show()

# create seperate dataframes of the NDA ans UPA 
nda_candidates = winner_df[winner_df['Alliance'] == 'NDA']
upa_candidates = winner_df[winner_df['Alliance'] == 'UPA']

# Plot the age distribution
# plt.figure(figsize=(12, 6))
sns.histplot(nda_candidates['Candidate Age'], color='blue', label='NDA', kde=True)
sns.histplot(upa_candidates['Candidate Age'], color='orange', label='UPA', kde=True)
plt.title('Age Distribution of NDA & UPA Candidates')
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend()
plt.show()

gender_distribution = winner_df.groupby(['Year', 'Candidate Sex']).size().unstack()

# Plot the gender distribution
gender_distribution.plot(kind='bar')
plt.title('Gender Distribution of 2009 & 2014 Elections')
plt.xlabel('Year')
plt.ylabel('Number of Candidates')
plt.xticks(rotation=0)
plt.legend(title='Sex')
plt.tight_layout()
plt.show()

gender_distri_2009 = seats_09.groupby(['Alliance', 'Candidate Sex']).size().unstack()

# Plot the gender distribution for NDA and UPA in 2009
gender_distri_2009.plot(kind='bar')
plt.title('Gender Distribution of NDA & UPA Candidates (2009)')
plt.xlabel('Alliance')
plt.ylabel('Number of Candidates')
plt.xticks(rotation=0)
plt.legend(title='Sex')
plt.tight_layout()
plt.show()

gender_distri_2014 = seats_14.groupby(['Alliance', 'Candidate Sex']).size().unstack()

# Plot the gender distribution for NDA and UPA in 2014
gender_distri_2014.plot(kind='bar')
plt.title('Gender Distribution of NDA & UPA Candidates (2014)')
plt.xlabel('Alliance')
plt.ylabel('Number of Candidates')
plt.xticks(rotation=0)
plt.legend(title='Sex')
plt.tight_layout()
plt.show()

# Plot the poll percentage for state in 2009 & 2014
plt.figure(figsize=(15,8))
plt.bar(df1['STATE'], df1['POLL PERCENTAGE'], width=0.4, label='2009', align='center')
plt.bar(df3['STATE'], df3['POLL PERCENTAGE'], width=0.4, label='2014', align='edge')
plt.xlabel('State name')
plt.ylabel('Poll Percentage')
plt.title('Poll Percentage of States for 2009 & 2014 Elections')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()