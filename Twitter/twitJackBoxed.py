import os
import sys
#import math
from datetime import date, datetime
import simplejson as json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#from geopy import geocoders
#from pprint import pprint

p_name='St Augustine'       #str(sys.argv[1])         #Name of place given to file
outputlocation=''             #str(sys.argv[2]) #Location of output file
datereq = str(date.today())

ckey = ''
csecret =''
atoken = ''
asecret = ''

class listener(StreamListener):
    def on_data(self, data):
        data = json.loads(data)
        logfile = open(os.path.join(outputlocation,p_name+"-"+datereq+".dat"), "a")
        
        tweet_id = unicode(data['id']).encode("ascii","ignore")
        tweet_day = unicode(data['created_at']).encode("ascii","ignore")[:3]
        tweet_date = unicode(data['created_at']).encode("ascii","ignore")[4:10] + " " + unicode(data['created_at']).encode("ascii","ignore")[-4:]
        tweet_time = unicode(data['created_at']).encode("ascii","ignore")[11:-11]
        text_msg = unicode(data['text']).encode("utf8","ignore").replace(',', ' ').replace("|","").replace("\r","").replace("\n","")
        favorite_count = unicode(data['favorite_count']).encode("ascii","ignore")
        retweet_count = unicode(data['retweet_count']).encode("ascii","ignore")
        entities_user_mentions = data['entities']['user_mentions']
        entities_user_mentions_id = []
        entities_user_mentions_sn = []
        if(entities_user_mentions!=[]):
            temp=[[x['id_str'].encode("ascii","ignore")] for x in entities_user_mentions]
            temp=str(temp)
            temp = temp.replace("[","").replace("]","")
            entities_user_mentions_id = temp
            temp=[[x['screen_name'].encode("ascii","ignore")] for x in entities_user_mentions]
            temp=str(temp)
            temp = temp.replace("[","").replace("]","")
            entities_user_mentions_sn = temp
        else :
            entities_user_mentions_id = ""
            entities_user_mentions_sn = ""
        entities_hashtags = data['entities']['hashtags']
        if(entities_hashtags!=[]):
            temp=[[x['text'].encode("ascii","ignore")] for x in entities_hashtags]
            temp = str(temp)
            temp = temp.replace("[","").replace("]","")
            entities_hashtags = temp
        else :
            entities_hashtags = ""
        entities_expanded_urls = data['entities']['urls']
        if(entities_expanded_urls!=[]):
            temp=[[x['expanded_url'].encode("ascii","ignore")] for x in entities_expanded_urls]
            temp = str(temp)
            temp = temp.replace("[","").replace("]","")
            entities_expanded_urls = temp
        else :
            entities_expanded_urls = ""
        user_id = unicode(data['user']['id']).encode("ascii","ignore")
        user_followers_count = unicode(data['user']['followers_count']).encode("ascii","ignore")
        user_statuses_count = unicode(data['user']['statuses_count']).encode("ascii","ignore")
        user_description = unicode(data['user']['description']).encode("ascii","ignore").replace("|","").replace("\r","").replace("\n","")
        user_friends_count = unicode(data['user']['friends_count']).encode("ascii","ignore")
        user_location = unicode(data['user']['location']).encode("ascii","ignore")
        user_lang = unicode(data['user']['lang']).encode("ascii","ignore")
        #user_favorites_count = unicode(data['user']['favourites_count']).encode("ascii","ignore")
        user_screen_name = unicode(data['user']['screen_name']).encode("ascii","ignore")
        user_created_at = unicode(data['user']['created_at']).encode("ascii","ignore")
        lang = unicode(data['lang']).encode("ascii","ignore")
        place_country_code = unicode(data['place']['country_code']).encode("ascii","ignore")
        place_country = unicode(data['place']['country']).encode("ascii","ignore")
        place_name = unicode(data['place']['name']).encode("ascii","ignore")
        place_full_name = unicode(data['place']['full_name']).encode("ascii","ignore")
        
        if data['coordinates'] == None :
            print '[No geotag for this tweet]'
            longitude = ""
            latitude = ""
        else:
            coord = unicode(data['coordinates']['coordinates']).encode("ascii","ignore")
            longitude = coord[:coord.rfind(',')].replace("[","")
            latitude = coord.split(" ")[1].replace("]","")

            stream_log = tweet_id + "|" + tweet_day + "|" + tweet_date + "|" + tweet_time+ "|" + latitude + "|" + longitude + "|" + text_msg + "|" + favorite_count + "|" + retweet_count + "|" + entities_user_mentions_id + "|" + entities_user_mentions_sn + "|" + entities_hashtags + "|" + entities_expanded_urls + "|" + user_id + "|" + user_followers_count + "|" + user_statuses_count + "|" + user_description + "|" + user_friends_count + "|" + user_location + "|" + user_lang + "|" + user_screen_name + "|" + user_created_at + "|" + lang + "|" + place_country_code + "|" + place_country + "|" + place_name + "|" + place_full_name
            stream_log = stream_log.replace('\n', ' ')
            if((float(longitude)>=-81.6685 and float(longitude) <=-81.2132) and (float(latitude)>=29.6259 and float(latitude)<=30.2530)):
                print '[RECORDED]'
                print >>logfile, stream_log            
        logfile.close()
        return True

    def on_error(self, statut):
        print statut

def main():
    location = [-82.0495, 30.1038, -81.3796, 30.5868]       #Duval County - Jacksonville
    stream_log = 'tweet_id' + "|" + 'tweet_day' + "|" + 'tweet_date' + "|" + 'tweet_time' + "|" + "latitude" + "|" + "longitude" + "|" + 'text_msg' + "|" + 'favorite_count' + "|" + 'retweet_count' + "|" + 'entities_user_mentions_id' + "|" + 'entities_user_mentions_screen_name' + "|" + 'entities_hashtags' + "|" + 'entities_expanded_urls' + "|" + 'user_id' + "|" + 'user_followers_count' + "|" + 'user_statuses_count' + "|" + 'user_description' + "|" + 'user_friends_count' + "|" + 'user_location' + "|" + 'user_lang' + "|" + 'user_screen_name' + "|" + 'user_created_at' + "|" + 'lang' + "|" + 'place_country_code' + "|" + 'place_country' + "|" + 'place_name' + "|" + 'place_full_name'
    logfile = open(os.path.join(outputlocation,p_name+"-"+datereq+".dat"), "a")
    print >>logfile, stream_log
    logfile.close()

    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    while True:                                         #https://github.com/ryanmcgrath/twython/issues/288 - queue overload fixed - for 'NoneType' object has no attribut 'strip' error
        try:
            twitterStream.filter(locations=location)
        except:
            e = sys.exc_info()[0]                       #Get exception info (optional)
            print 'ERROR:',e                            #Print exception info (optional)
            continue
    
main()
