# Name: get_hot_spot
# Author: Harry(Wei) Liu
# Description: Get the hot spot, which could use for bug pridiciton. \
#   For course EECS 284, UC Merced
# 
import math

def azureml_main(hotspot_raw = None, dataframe2 = None):
    
    import pandas as pd
    
    result = {}
    time_ratio = hotspot_raw['time_ratio']
    files = hotspot_raw['file']
    comments = hotspot_raw['message']
    lens = len(files)
    
    for i in range(0, lens):
        if files[i] not in result:
            result[files[i]] = 0
        hotspot_factor = 1/(1+math.exp((-12 * time_ratio[i]) + 12))
        result[files[i]] += hotspot_factor
    
    hotspot = []
    for key, value in result.iteritems():
        hotspot.append({key: value})

    return pd.DataFrame(hotspot),
    # return pd.DataFrame(result),
