# retrieve tweets containing given keywords from Twitter (http://twitter.com).

def filter_non_printable(str):
      return ''.join([c for c in str if (ord(c) > 31 and ord(c) <> 127)])

import os, sys; sys.path.insert(0, os.path.join("..", ".."))
from pattern.db  import Datasheet
from datetime import date, datetime
from twitter import *
import string

bool_since_id=False

consumer_key="iAwecz40dNjlBIn8P8vm0AhmQ"
consumer_secret="4QDBjOFW9cO55lyMbH9SeC35QUE0cwVSwPbGlyTYHYGYnL4DXd"
access_token_key="3609410777-49rc83R03fr1NgB65JvkTGLdZli8k8c9ZVnwioS"
access_token_secret="uK0Tn65UytvPfRcsGlbWuXhPtDOvjsGnue6rEQEmvv29s"

lst_param=['idTweet','language','text','created_at','coordinates','urls','expanded_urls','hashtags','user_mentions','in_reply_to_screen_name','in_reply_to_user_id_str',
           'retweet_count','favorite_count','iso_language_code','contributors','lang','place','geo',
           'user_id','user_name','user_verified','user_followers_count','user_listed_count','user_statuses_count','user_description',
           'user_location','user_utc_offset','user_friends_count','user_screen_name','user_lang','user_favourites_count','user_created_at'
           ]



def searchTwitter(Request,FileOut,language):
    FileOutTxt=FileOut+str(date.today())+".dat" #append file with search results
    strFout=FileOut+".log"
    Fout=open(strFout,mode='a') #append log file with info on code run
    try: 
        # We store tweets in a Table that can be saved as a text file.
        # In the first column, we'll store a unique ID for each tweet.
        # We only want to add the latest tweets, i.e. those we haven't previously encountered.
        # With an on the first column we can quickly check if an ID already exists.
        # The index becomes important once more and more rows are added to the table (speed).
        table = Datasheet.load(FileOutTxt, separator = '|')
        index = list(table.columns[0])[1:]
        maxIndex=max(index)
    except:
        table = Datasheet()
        table.append(lst_param)
        index = []
        maxIndex=0

    engine = Twitter( auth=OAuth(access_token_key, access_token_secret,consumer_key, consumer_secret) )
    if bool_since_id: since_id=maxIndex
    else: since_id=0
    tweets=engine.search.tweets(q=Request['q'],result_type=Request['result_type'],count=Request['count'],since_id=since_id,include_entities=Request['include_entities'])

    nAdded=0
    for t in tweets['statuses']:

        idTweet=t.get('id')
        
        urls=''; expanded_urls=''
        for url in t.get('entities').get('urls'):
            if urls=='':
                  urls=url.get('url');    expanded_urls=url.get('expanded_url')
            else:
                  urls+='^'+url.get('url');expanded_urls+='^'+url.get('expanded_url')

        hashtags=''
        for hashtag in t.get('entities').get('hashtags'):
            if hashtags=='':hashtags=hashtag.get('text')
            else: hashtags+='#'+hashtag.get('text')
            
        user_mentions=''
        for user_mention in t.get('entities').get('user_mentions'):
            if user_mentions=='':user_mentions=user_mention.get('id_str')
            else: user_mentions+='@'+user_mention.get('id_str')

        lstTweet=[idTweet,
                  language,
                  (t.get('text','')),
                  t.get('created_at'),
                  (t.get('coordinates')),
                  (urls),
                  (expanded_urls),
                  (hashtags),
                  str(user_mentions),
                  (t.get('in_reply_to_screen_name')),
                  (t.get('in_reply_to_user_id_str')),
                  str(t.get('retweet_count')),
                  str(t.get('favorite_count')),
                  (t.get('metadata').get('iso_language_code')),
                  (t.get('contributors')),
                  (t.get('lang')),
                  (t.get('place')),
                  (t.get('geo')),
                  str(t.get('user').get('id')),
                  (t.get('user').get('name')),
                  (t.get('user').get('verified')),
                  str(t.get('user').get('followers_count')),
                  str(t.get('user').get('listed_count')),
                  str(t.get('user').get('statuses_count')),
                  (t.get('user').get('description')),
                  (t.get('user').get('location')),
                  str(t.get('user').get('utc_offset')),
                  str(t.get('user').get('friends_count')),
                  (t.get('user').get('screen_name')),
                  (t.get('user').get('lang')),
                  str(t.get('user').get('favourites_count')),
                  (t.get('user').get('created_at'))
                 ]
        for i in range(1,len(lstTweet)):
            if lstTweet[i]==None: lstTweet[i]=''
            if lstTweet[i]==True: lstTweet[i]='Y'
            if lstTweet[i]==False: lstTweet[i]='N'
            if type(lstTweet[i])==str or type(lstTweet[i])==unicode:
                lstTweet[i]=filter_non_printable(lstTweet[i])
                lstTweet[i]=lstTweet[i].replace('|',' ')

        if unicode(idTweet) not in index:
            table.append(lstTweet)
            nAdded+=1
                  
    table.save(FileOutTxt, separator = '|')

    print "Total results:", len(table)
    Fout.write(str(nAdded)+'\t'+str(datetime.now())+'\n')
    Fout.close()


#do only if this scipt is run as stand-alone        
import os,pprint,sys
if __name__ == "__main__": 
    #see if there are arguments in the command line; if not use defaul arguments
    if len(sys.argv)<>4:
        print "Use: Python searchTwitter Request FileOut language"
        print "Bad input: running default"
        #Request=u"'изменения климата' OR 'глобальное потепление'"
        Request={'q':'#NEMO','result_type':'recent','count':100,'include_entities':'true'}
        FileOut="test"
        language='en'
    else:
        strRequest=sys.argv[1]
        Request={'q':strRequest,'result_type':'recent','count':100,'include_entities':'true'}
        print Request
        FileOut=sys.argv[2]
        language=sys.argv[3]
    searchTwitter(Request,FileOut,language)
    


