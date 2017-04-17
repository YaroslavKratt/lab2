import  urllib2
import pandas as pd
from time import gmtime, strftime
df = pd.read_csv('/home/yarik/SRP/lab2/clean_data/vhi_id_'+str(5)+'.csv',',')

#df = pd.read_csv('vhi_id_13.csv',',', header = 1, names =['Year','SMT','VCI','TCI','VHI'], skipfooter = 1)

df = df[['year','week','SMN','SMT','VCI','TCI','VHI']]
print (df )
  		#if func == "VHI":