import pandas as pd
import numpy as np
from skimpy import clean_columns


infile_path = '/Users/rhedayati/Desktop/PublicData/All_data.csv'
outfile_path = '/Users/rhedayati/Desktop/PublicData/All_data_edited.csv'
data = pd.read_csv(infile_path)

data.insert(11, 'outbreak severity', np.nan ) 

rowNumber = 0
for item in data['# of total outbreaks']:
    if item == 0:
        data['outbreak severity'][rowNumber] = 'safe'
    if 0 < item < 2:
        data['outbreak severity'][rowNumber] = 'mild'
    if item > 1:
        data['outbreak severity'][rowNumber] = 'severe' 
    rowNumber+=1
    if rowNumber == data.shape[0]:
        exit
data.rename(columns={'# of total outbreaks': 'number of total outbreaks', '# of population over 15': 'number of population over 15'}, inplace=True)

data = clean_columns(data)
empty_df = pd.DataFrame (columns = data.columns, index = range(474,1001,1))

data_new = data.append(data)
data_new = data_new.append(data)
#data_new.drop(data_new.columns[0], axis=1, inplace=True)
print(data_new)
data_new.to_csv(outfile_path)