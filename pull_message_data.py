
#class Subscriber(object):
from Pull.AWeber import MyApp
import json, csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app = MyApp()
#app.connect_to_AWeber_account()
messageList  =[]
f = csv.writer(open("messages.csv", "wb+"))
f.writerow(["cID","msgID", "id", "last_opened", "type","total_opens"])

for _list in app.account.lists:
    print _list.name
    campaigns =_list.campaigns

    for c in campaigns:
        cID = c.id
        messages = c.messages
        for m in messages:
            subLink = m.subscriber_link
            thing=subLink.split("/")
            subID = thing[len(thing)-1]
            print(subID)

            f.writerow([cID,
                        m.id,
                        subID,
                        m.last_opened,
                        m.type,
                        m.total_opens
                        ])
    print(realList)
    print(len(realList))


