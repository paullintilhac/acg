
#class Subscriber(object):
from Pull.AWeber import MyApp
import json, csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app = MyApp()
#app.connect_to_AWeber_account()
realList  =[]
f = csv.writer(open("subscribers.csv", "wb+"))
f.writerow(["id", "name", "email", "status","subscribed_at", "unsubscribed_at"])


for _list in app.account.lists:
    print _list.name
    subscribers =_list.subscribers

    for s in subscribers:
        realList.append(s.name)
        if s.subscribed_at:
            sub = (s.subscribed_at.encode("utf-8"))[0:10]
        else:
            sub = "NA"
        if s.unsubscribed_at:
            unsub = (s.unsubscribed_at.encode("utf-8"))[0:10]
        else:
            unsub = "NA"


        print "sub: " + sub
        print "unsub:" + unsub
        f.writerow([s.id,
                    s.name,
                    s.email,
                    s.status,
                    sub,
                    unsub
                    ])
    print(realList)
    print(len(realList))


print "number of subscribers in list: " + str(len(realList))



