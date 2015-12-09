import pyipinfodb, csv, codecs
import sys
import json

reload(sys)
sys.setdefaultencoding('UTF8')

ip=[]
x = pyipinfodb.IPInfo('31ff3f5cbbcfe3ddb342e63e9df356d704147782e30ab3038218d2462aa70529')

#filename = str(sys.argv[1])
#filelist = ["Piwik Export _  _ 20 Sep 15 - 23 Sep 15","Piwik Export _  _ 21 Aug 15 - 24 Aug 15","Piwik Export _  _ 24 Sep 15 - 27 Sep 15","Piwik Export _  _ 25 Aug 15 - 27 Aug 15","Piwik Export _  _ 28 Aug 15 - 30 Aug 15","Piwik Export _  _ 28 Sep 15 - 30 Sep 15","Piwik Export _  _ 31 Aug 15 - 3 Sep 15"]
#for i in filelist:
#filename = i
filename = "Piwik Export _  _ 9 Nov 15 - 12 Nov 15"
outfile = filename + "_IP"

with codecs.open(filename+".csv",'rU','utf-16') as f:
    reader=csv.reader(f,delimiter='\t')
    for row in reader:
        val = unicode(row[2]).encode("ascii","ignore")
        ip.append(val)


with open(outfile+".csv",'w') as w:
    c=csv.writer(w,lineterminator='\n')
    c.writerow(["visitIp", "Country Code","Country Name","Region Name","City","Zipcode","Latitude","Longitude"])
    for i in range(1,len(ip)):
        data = x.get_city(ip[i])
        d1=data.split('\000')
        z = json.loads(d1[0].decode('utf-8'))
        print z
        c.writerow([ip[i], z['countryCode'], z['countryName'],z['regionName'],z['cityName'],z['zipCode'], z['latitude'], z['longitude']])

print "DONE for file - " + filename +".csv"