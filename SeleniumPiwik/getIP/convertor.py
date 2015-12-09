import pandas as pd

import sys
reload(sys)
sys.setdefaultencoding('UTF8')

filename = "Piwik Export _  _ 9 Nov 15 - 12 Nov 15"
filename2 = filename + "_IP"
finalfile = filename +"_out.csv"

a = pd.read_csv(filename + ".csv",encoding='utf-16',sep='\t')
b = pd.read_csv(filename2 + ".csv",sep=',')
b = b.dropna(axis=1)
merged = b.merge(a, on='visitIp')
merged = merged.drop_duplicates(subset='idVisit')
merged.to_csv(finalfile, index=False)

print "Done merging for file: " + filename + ".csv"
