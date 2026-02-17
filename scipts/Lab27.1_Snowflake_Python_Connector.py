/*
Step 1: Install Anaconda3 for Python from google
Step 2: Install Snowflake connector for Python, run below command from cmd prompt
 pip install snowflake-connector-python==3.0.0
Step 3: Import that connector in your python program
Step 4: Use snowflake.connector.connect to connect to your snowflake account.*/


#!/usr/bin/env python
import snowflake.connector
import pandas as pd
import csv

sfconn = snowflake.connector.connect(
    user='sg99snowflake', #user='your-username'
    password='Sg39@admin', #password='your-password'
    account='sq97273.central-india.azure' # your account id
    )

sf = sfconn.cursor()

sf.execute("SELECT TABLE_SCHEMA, TABLE_NAME, ROW_COUNT from SNOWFLAKE_SAMPLE_DATA.INFORMATION_SCHEMA.TABLES WHERE TABLE_CATALOG='SNOWFLAKE_SAMPLE_DATA' and TABLE_TYPE='BASE TABLE';")

counts = sf.fetchall()
print(counts)

df=pd.DataFrame(counts)
print(df)

with open('C:/Users/shivam Gupta/training/snwflake_training/snowflake_table_counts.csv', 'w', newline='') as file:
     writer = csv.writer(file, delimiter='|')
     writer.writerows(counts)
    
sf.close()
