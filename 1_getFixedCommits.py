# Name: get_fixed_commits
# Author: Harry(Wei) Liu
# Description: Get bug fix comment in a version control reposite. \
#   For course EECS 284, UC Merced
# 
import math
import re

description_regex = re.compile(
    "^.*([B|b]ug)s?|([f|F]ix(es|ed)?|[c|C]lose(s|d)?).*$")

def azureml_main(hotspot_raw = None, dataframe2 = None):
    
    import pandas as pd
    
    result = []
    dates = hotspot_raw['date']
    files = hotspot_raw['file']
    comments = hotspot_raw['message']
    lens = len(files)
    
    for i in range(0, lens):
        if description_regex.search(comments[i]):
            tmp = {}
            tmp['file'] = files[i]
            tmp['date'] = dates[i]
            tmp['message'] = comments[i]
            result.append(tmp)
    
    fixed_commits = pd.DataFrame(result)

    return fixed_commits,
