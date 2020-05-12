from datetime import datetime, timezone

#print("hello world at " + str(datetime.datetime.now()))
print("hello world at " + datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")) 