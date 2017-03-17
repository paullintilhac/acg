demo = function(){
  library(lattice)
  wd="~/AWeber-API-Python-Library/"
  messages = data.table(read.csv(paste0(wd,"messages.csv")))
  messages$id = as.integer(as.character(messages$id))
  subscribers = data.table(read.csv(paste0(wd,"subscribers.csv")))
  subscribers$subscribed_at = as.Date(subscribers$subscribed_at)
  subscribers$unsubscribed_at = as.Date(subscribers$unsubscribed_at)
  
  subscriptions = subscribers[,subscribtions:=.N,by= "subscribed_at"]
  unsubscriptions = subscribers[,unsubscriptions:=.N,by = "unsubscribed_at"]
  setnames(subscriptions,"subscribed_at","date")
  setnames(unsubscriptions,"unsubscribed_at","date")
  
  mergeData = merge(subscriptions,unsubscriptions,by = "date")
  xyplot(N~subscribed_at,plotData,type = "l")
  
  mergeData = merge(messages,subscribers,by = "id")
  
  }