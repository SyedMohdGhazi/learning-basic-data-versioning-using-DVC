import pandas as pd
import os

#Sample Dataframe
data = {
        'Name' : ['Alan', 'Walker', 'Priya'],
        'Age' : ['20', '50', '69'],
        'City' : ['New York', 'Bhatinda', 'Talwandi Sabu']
        }

df = pd.DataFrame(data)

#New row added for v2
new_row_loc = {'Name' : 'Pannu', 'Age' : '88', 'City' : 'Beas'}
df.loc[len(df.index)] = new_row_loc


#New row added for v2
# new_row_loc = {'Name' : 'Pannu', 'Age' : '88', 'City' : 'Beas'}
# df.loc[len(df.index)] = new_row_loc


data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")