import  urllib2
import pandas as pd
from time import gmtime, strftime

true_index=[24,25,5,6,27,23,26,7,11,13,14,15,16,17,18,19,21,22,8,9,10,1,3,2,4,12,20]
def download():
    i=1
    while i<28:
        index=true_index[i-1]
        print(index)
        url="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+str(index)+"&year1=2016&year2=2016&type=Mean"
        print(url)
        vhi_url = urllib2.urlopen(url)
        name='vhi_id_'+str(i)+'.csv'
        out = open(name,'wb')
        out.write(vhi_url.read())
        out.close()
        df = pd.read_csv(name,',', header=1,names=['1','SMT','VCI','TCI','VHI'], skip_footer=1)
        df['1']=df['1'].replace('  ',' ', regex=True)
        df['1']=df['1'].replace(' ',',', regex=True)
        df.insert(0,'year',df['1'].str.split(',').str.get(0),allow_duplicates=False)
        df.insert(1,'week',df['1'].str.split(',').str.get(1),allow_duplicates=False)
        df.insert(2,'SMN',df['1'].str.split(',').str.get(2),allow_duplicates=False)
        del df['1']
        df.to_csv('./clean_data/'+name, index=False)
        print "VHI is downloaded..."
        i=i+1

download()
