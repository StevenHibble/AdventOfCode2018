import os
import pandas as pd

os.chdir('Day 04')

### Setup
with open('Input.txt', 'r') as f:
    data = f.read().splitlines()

# Remove leading '[' and provide datetime format
scrubDate = lambda x: pd.datetime.strptime(x.replace('[', ''), '%Y-%m-%d %H:%M')

data = pd.read_csv('Input.txt', 
                    sep = ']', 
                    header = None, 
                    names = ['TimeStamp', 'Action'],
                    parse_dates = ['TimeStamp'],
                    date_parser = scrubDate)

# Sort by Timestamp so fillna works properly in next step
data = data.sort_values(['TimeStamp'])

# Split Guard and Action into separate columns
data['Guard']  = data['Action'].str.extract('#(\d+)').fillna(method = "ffill")
data['Action'] = data['Action'].str.replace('^.*#\d+ ', '')


### Part One

# Remove the shift beinning (we already have Guard #)
sleep_patterns = data[data['Action'] != 'begins shift']

#sleep_patterns['Minute'] = sleep_patterns['TimeStamp'].apply(pd.to_datetime)#.dt.minute

print(sleep_patterns.head(10))