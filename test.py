import datetime

time_str = "2022.10.20-20:38"
reference_time = datetime.datetime.strptime(time_str, "%Y.%m.%d-%H:%M")

start_time = reference_time - datetime.timedelta(hours=3)
end_time = reference_time - datetime.timedelta(hours=1.2)
now = datetime.datetime.now()

if end_time <= now <= start_time:
    print ('It is in between')