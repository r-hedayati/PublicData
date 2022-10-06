import pandas as pd
import numpy as np
from skimpy import clean_columns


infile_path = '/Users/rhedayati/Desktop/PublicData/edmonton_data_LHA.csv'
outfile_path = '/Users/rhedayati/Desktop/PublicData/All_data1_edited.csv'
data = pd.read_csv(infile_path)

data = clean_columns(data)
data.to_csv(outfile_path)
