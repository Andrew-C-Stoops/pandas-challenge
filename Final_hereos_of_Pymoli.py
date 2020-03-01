#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


pd.read_csv("Resources/purchase_data.csv")  


# In[4]:


purchasedata_df = pd.read_csv("Resources/purchase_data.csv")


# In[5]:


purchasedata_df


# In[6]:


#
#Player Count
#Display the total number of players
total_players = len(purchasedata_df['SN'].value_counts())
Total_Players = pd.DataFrame({"Total Players": total_players}, index=[0])
Total_Players


# In[7]:


#Purchasing Analysis (Total)
#Run basic calculations to obtain number of unique items, average price, etc.
#Create a summary data frame to hold the results
#$Optional: give the displayed data cleaner formatting
#Display the summary data frame
unique_items = len(purchasedata_df['Item ID'].value_counts())


average_price = purchasedata_df['Price'].mean()


total_purchases = purchasedata_df['Item Name'].count()



total_revenue = purchasedata_df['Price'].sum()


purchasing_analysis = pd.DataFrame({"Number of Unique Items": [unique_items],
                                   "Average Price": [average_price],
                                   "Total Purchases": [total_purchases],
                                   "Total Revenue": [total_revenue],
                                
})


# In[8]:


purchasing_analysis = purchasing_analysis[["Number of Unique Items", "Average Price","Total Purchases", "Total Revenue"]]


# In[9]:


purchasing_analysis


# In[10]:


purchasing_analysis["Average Price"] = purchasing_analysis["Average Price"].map("${0:,.2f}".format)
purchasing_analysis["Total Revenue"] = purchasing_analysis["Total Revenue"].map("${0:,.2f}".format)


# In[11]:


purchasing_analysis


# In[12]:


#Gender Demographics¶
#Percentage and Count of Male Players
#Percentage and Count of Female Players
#Percentage and Count of Other / Non-Disclosed
gender_count_df = purchasedata_df.groupby("Gender")["SN"].nunique()
gender_count_df.head()


# In[13]:


gender_percentage_df = gender_count_df/573
gender_percentage_df.round(2)

gender_demographics = pd.DataFrame({"TOTAL COUNT": gender_count_df,
                              "TOTAL PERCENTAGE OF PLAYERS": gender_percentage_df})
gender_demographics["TOTAL PERCENTAGE OF PLAYERS"] = gender_demographics["TOTAL PERCENTAGE OF PLAYERS"].map("{:.2%}".format)
gender_demographics


# In[14]:



#Purchasing Analysis (Gender)
#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
#Create a summary data frame to hold the results
#Optional: give the displayed data cleaner formatting
#Display the summary data frame
gender_df = purchasedata_df.groupby('Gender')
male_purchase_count = gender_df.count().Age.Male
female_purchase_count = gender_df.count().Age.Female
other_purchase_count = gender_df.count().Age["Other / Non-Disclosed"]
f_avg_purchase_price = gender_df.mean().Price.Female
m_avg_purchase_price = gender_df.mean().Price.Male
o_avg_purchase_price = gender_df.mean().Price["Other / Non-Disclosed"]
f_total_purchase_value = gender_df.sum().Price.Female
m_total_purchase_value = gender_df.sum().Price.Male
o_total_purchase_value = gender_df.sum().Price["Other / Non-Disclosed"]
purchasing_analysis = {
    "Gender": ["Female", "Male", "Other / Non-Disclosed"],
    "Purchase Count": [female_purchase_count, male_purchase_count, other_purchase_count],
    "Average Purchase Price": [f_avg_purchase_price, m_avg_purchase_price, o_avg_purchase_price],
    "Total Purchase Value": [f_total_purchase_value, m_total_purchase_value, o_total_purchase_value],}
purchasing_analysis_df = pd.DataFrame(purchasing_analysis).set_index("Gender")

purchasing_analysis_df['Average Purchase Price'] = purchasing_analysis_df['Average Purchase Price'].map('${0:,.2f}'.format)
purchasing_analysis_df['Total Purchase Value'] = purchasing_analysis_df['Total Purchase Value'].map('${0:,.2f}'.format)
purchasing_analysis_df


# In[15]:



#Age Demographics
#Establish bins for ages
#Categorize the existing players using the age bins. Hint: use pd.cut()
#Calculate the numbers and percentages by age group
#Create a summary data frame to hold the results
#Optional: round the percentage column to two decimal points
#Display Age Demographics Table
group_names=["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
bins=[0,9,14,19,24,29,34,39,120]

purchasedata_df["Age Group"]=pd.cut(purchasedata_df["Age"],bins, labels=group_names)
group_age=purchasedata_df.groupby("Age Group")


age_total=group_age["SN"].count().rename("Total Count")

age_demographics_df=pd.DataFrame(age_total)
age_demographics_df["Percentage of Players"]=age_demographics_df["Total Count"]*100/age_demographics_df["Total Count"].sum()
age_demographics_df["Percentage of Players"]=age_demographics_df["Percentage of Players"].round(2)
age_demographics_df=age_demographics_df[["Percentage of Players", "Total Count"]]
age_demographics_df["Percentage of Players"] = age_demographics_df["Percentage of Players"].map("{:.2f}%".format)
age_demographics_df


# In[18]:



#Purchasing Analysis (Age)
#Bin the purchase_data data frame by age
#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
#Create a summary data frame to hold the results
#Optional: give the displayed data cleaner formatting
#Display the summary data frame

bins=[0,9,14,19,24,29,34,39,120]
Age_ranges = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

pd.cut(purchasedata_df["Age"], bins, labels = Age_ranges).head()

purchasedata_df["Age Range"] = pd.cut(purchasedata_df["Age"],bins,labels = Age_ranges)



group = purchasedata_df.groupby("Age Range")


sn_count = purchasedata_df.groupby(["Age Range"]).count()["Age"]



average_price = purchasedata_df.groupby(["Age Range"]).mean()["Price"]



total_purch_v = purchasedata_df.groupby(["Age Range"]).sum()["Price"]



table = pd.DataFrame({"Purchase Count": sn_count, 
                      "Total Purchase Value": total_purch_v, 
                      "Average Purchase Value": average_price, })

table["Average Purchase Value"] = table["Average Purchase Value"].map("${:.2f}".format)

table["Total Purchase Value"] = table["Total Purchase Value"].map("${:.2f}".format)


table


# In[20]:


#Top Spenders
#Run basic calculations to obtain the results in the table below
#Create a summary data frame to hold the results
#Sort the total purchase value column in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the summary data frame
opurchase_data_df = pd.DataFrame(purchasedata_df)
gSNtopspendor_df = opurchase_data_df.groupby("SN")
analysis_df = pd.DataFrame(gSNtopspendor_df["Purchase ID"].count())
tpurchasevalueSN = gSNtopspendor_df["Price"].sum()
avg_purchase_price_SN = gSNtopspendor_df["Price"].mean()
dlr_avg_purchase_price_SN = avg_purchase_price_SN.map("${:,.2f}".format)
analysis_by_SPENDOR_df["Average Purchase Price"] = dlr_avg_purchase_price_SN
analysis_by_SPENDOR_df["Total Purchase Value"] = total_purchase_value_SN 
SUM_SN_purchased_data_df = analysis_by_SPENDOR_df.rename(columns={"Purchase ID":"Purchase Count"})
TOP5_spendors_df=SUM_SN_purchased_data_df.sort_values("Total Purchase Value", ascending=False)
dlr_total_purchase_value_SN = total_purchase_value_SN.map("${:,.2f}".format)
TOP5_spendors_df["Total Purchase Value"] = dlr_total_purchase_value_SN
TOP5_spendors_df.head()


# In[28]:



#Most Popular Items¶
#Retrieve the Item ID, Item Name, and Item Price columns
#Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
#Create a summary data frame to hold the results
#Sort the purchase count column in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the summary data frame
pop_items=purchasedata_df[["Item ID", "Item Name", "Price"]]
pop_items_grp=pop_items.groupby(["Item ID", "Item Name"])

pop_count=pop_items_grp["Item ID"].count()
pop_totals=pop_items_grp["Price"].sum()
pop_price=pop_totals/pop_count
pop_df=pd.concat([pop_count, pop_price, pop_totals], axis=1)
pop_df.columns=["Purchase Count", "Item Price", "Total Purchase Value"]
sort_df=pop_df.sort_values("Purchase Count", ascending=False)
sort_df["Item Price"]=sort_df["Item Price"].map("${:,.2f}".format)
sort_df["Total Purchase Value"]=sort_df["Total Purchase Value"].map("${:,.2f}".format)
sort_df


# In[31]:



#Most Profitable Items
#Sort the above table by total purchase value in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the data frame
profit_df=pop_df.sort_values("Total Purchase Value", ascending=False)
profit_df["Item Price"]=profit_df["Item Price"].map("${:,.2f}".format)
profit_df["Total Purchase Value"]=profit_df["Total Purchase Value"].map("${:,.2f}".format)
profit_df


# In[ ]:




