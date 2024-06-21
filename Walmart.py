# -*- coding: utf-8 -*-
"""
Question Number 4: The purchase analysis of walmart.
a. What is the average Purchase Price?
b. What were the highest and lowest purchase prices?
c. How many people have English 'en' as their Language of choice on the website?
d. What is the email of the person with the following Credit Card Number: 4926535242672853
e. Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
f. How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
g. How many people have a credit card that expires in 2025?
h. What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) ?
i. What are the 5 most common Job Titles?
j. How many people made the purchase during morning and evening time?

"""

import pandas as pd

df = pd.read_csv("walmart_purchase_data.csv")
print(df.head())

purchase_price_avg = df['Purchase Price'].mean()
print("Average Purchase Price:",purchase_price_avg)

lowest_purchase_price = df['Purchase Price'].min()
print("Lowest Purchase Price:",lowest_purchase_price)

highest_purchase_price = df['Purchase Price'].max()
print("Highest Purchase Price:",highest_purchase_price)

english_count = df['Language'].value_counts()['en']
print("English Count:",english_count)

email = df[df['Credit Card'] == 4926535242672853]['Email'].values[0]
print("Email of CC 4926535242672853:", email)

lot_pp = df[df["Lot"] == "90 WT"]["Purchase Price"].values[0]
print("Purchase Price of lot '90WT':", lot_pp)

people_count = df[(df["CC Provider"] == "American Express") & (df["Purchase Price"] > 95)].count()[1]
print("People Count:", people_count)
# df["\nCC Exp Date"].unique()

people_count_cc = df["CC Exp Date"].str.split("/").str[1].value_counts()["25"]
print("People Count:", people_count_cc)

email_lst = df["Email"].apply(lambda x:x.split("@")[1]).value_counts().head()
print("Top 5 most popular Email List:")
print(email_lst)

job_lst = df["Job"].value_counts().head()
print("Top 5 most common Job List:")
print(job_lst)

people_lst = df["AM or PM"].value_counts()
print("People made the purchase during morning and evening time:")
print(people_lst)