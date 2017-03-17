from aweber_api import AWeberAPI
import json, csv

class MyApp(object):

    def __init__(self):
        # replace XXX with your keys
        consumer_key = 'AzjDMRiX4wbhtZEdky23tDbv'
        consumer_secret = 'PibOkYKyhTQrLKIAKpUdfNxo9cOmsf8Zb7BIRkbY'
        self.access_token = 'AgzINUhc1zx755e91a2nnCnc'
        self.access_secret = 'qMATjcw05qw0rk8viqpoGTCG2AJlKzuZKcptYrlk'

        self.application = AWeberAPI(consumer_key, consumer_secret)
        self.account = self.application.get_account(self.access_token, self.access_secret)

    def connect_to_AWeber_account(self):
        app_id = '98a30a69'
        authorization_url = 'https://auth.aweber.com/1.0/oauth/authorize_app/%s' % app_id
        print 'Go to this url in your browser: %s' % authorization_url
        authorization_code = raw_input('Type code here: ')

        auth = AWeberAPI.parse_authorization_code(authorization_code)
        consumer_key, consumer_secret, access_key, access_secret = auth
        print auth
        return auth

    def find_list(list):
        lists = self.account.lists.find(name=list)
        return lists[0]

    def find_subscriber(self):
        subscribers = self.account.findSubscribers(email="whtever@example.com")
        return subscribers[0]

    def add_subscriber(self, subscriber, _list):
        list_url = '/accounts/%s/lists/%s' % (self.account.id, _list.id)
        _list = self.account.load_from_url(list_url)

        try:
            new_subscriber = _list.subscribers.create(**subscriber)
            print new_subscriber.email

        except Exception, exc:
            print exc

#class Subscriber(object):

app = MyApp()
#app.connect_to_AWeber_account()
realList  =[]

for _list in app.account.lists:
    print _list.name
    subscribers =_list.subscribers.entries
    print subscribers
    while (True):
        for subscriber in subscribers:
            print subscriber["email"]
            realList.append(json.loads(json.dumps(subscriber)))
        if not hasattr(subscribers, "next_collection_link"):
            print "no further entries"
            break
        subscribers = _list.subscribers.next_collection_link
        
            #print "status: "+subscriber["status"] + ", email: "+ subscriber["email"]
    #subscriber = {
    #    'email': 'johndoe@example.com',
    #    'name': 'john doe',
    #}

print "number of subscribers in list: " + str(len(realList))
#for key, value in realList[0].items() :
#    print (key, value)

f = csv.writer(open("test.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
#f.writerow(["pk", "model", "codename", "name", "content_type"])

#for x in realList:
#    f.writerow([x["pk"],
#                x["model"],
#                x["fields"]["codename"],
#                x["fields"]["name"],
#                x["fields"]["content_type"]])
#app.add_subscriber(subscriber, _list)