# Name: get_time_ratio
# Author: Harry(Wei) Liu
# Description: Get the time ratio, which could use for bug pridiciton. \
#   For course EECS 284, UC Merced
# 
import time
import math

def to_seconds_float(timedelta):
    return (timedelta.seconds + timedelta.microseconds / 1E6)

def time_diff(from_t, to):
    return to_seconds_float(from_t - to)
    
def get_time_ratio(base, now, time):
    return 1 - (now - time) / (now -  base)

def azureml_main(hotspot_raw = None, dataframe2 = None):
    
    import pandas as pd
    
    result = []
    dates = hotspot_raw['date']
    files = hotspot_raw['file']
    comments = hotspot_raw['message']
    lens = len(files)
    
    last_dt = min(dates)
    current_dt = time.time()
    print "The oldest date is: ", last_dt
    
    for i in range(0, lens):
        tmp = {}
        tmp['file'] = files[i]
        tmp['time_ratio'] = get_time_ratio(last_dt, current_dt, dates[i])
        tmp['message'] = comments[i]
        result.append(tmp)
    
    hotspot = pd.DataFrame(result)

    return hotspot,
