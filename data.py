# -*- coding: utf-8 -*-


pip install nselib

from nselib import capital_market
d=capital_market.index_data(index='NIFTY 50',from_date='01-01-2019',to_date='31-12-2023')
d.to_csv('output_data4.csv', index=False)

import csv
from datetime import datetime

#  date string to dd/mm/yyyy format
def parse_date(date_str):
    return datetime.strptime(date_str, '%d-%m-%Y')

# converting data into a list of dictionaries
with open('output_data4.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

sorted_data = sorted(data, key=lambda x: parse_date(x['TIMESTAMP']))

# Write sorted data back to a CSV file
with open('sorted_output.csv', 'w', newline='') as csvfile:
    fieldnames = sorted_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in sorted_data:
        writer.writerow(row)

import pandas as pd
data_df = pd.read_csv('sorted_output.csv')
data_df = data_df.rename(columns={'TIMESTAMP': 'DATE'})
data_df

from nselib import derivatives

#Sampe demostration of how to calculate pcr ratio
derivatives.participant_wise_open_interest('02-02-2024')

data = derivatives.participant_wise_open_interest('02-02-2024')
call = data['Option Index Call Short'].sum()
put = data['Option Index Put Short'].sum()
pcr_ratio=round(put/call, 2)
print(pcr_ratio)

def calculate_pcr_ratio(date):
    try:

        data = derivatives.participant_wise_open_interest(date)


        pcr_ratio = data['Option Index Put Short'].sum() / data['Option Index Call Short'].sum()

        return round(pcr_ratio, 2)  # Round to two decimal points
    except Exception as e:
        print(f"Error calculating PCR ratio for {date}: {e}")
        return None


data_df['PCR Ratio'] = data_df['DATE'].apply(calculate_pcr_ratio)

data_df['CLOSE_PRICE'] = data_df['CLOSE_PRICE'].round()
data_df = data_df[data_df['PCR Ratio'].notna()]
data_df.to_csv('output_data10.csv', index=False)
print(data_df)
