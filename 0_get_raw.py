# Name: get_raw_commits
# Author: Harry(Wei) Liu
# Description: Get comments in a version control reposite. \
#   For course EECS 284, UC Merced
# 

import sys
import csv

from vcstools import vcs_abstraction
    
def get_commits(path):
    vcs = get_current_vcs(path)
    logs_raw = vcs.get_log()
    logs = []
    tmp_log = {}
    for log in logs_raw:
        tmp_log = {
            'date': log['date'],
            'email': log['email'],
            'message': log['message'],
            'id': log['id'],
            'author': log['author'],
            'files': vcs.get_affected_files(log['id'])
        }
        logs.append(tmp_log)
    return logs
    
def get_current_vcs(path="."):
    for vcs_type in vcs_abstraction.get_registered_vcs_types():
        vcs = vcs_abstraction.get_vcs(vcs_type)
        if vcs.static_detect_presence(path):
            return vcs(path)
    raise Exception("Not found a valid VCS repository")
    
def write_to_csv(cmts):
    if not cmts:
        print("Didn't found commits")
        sys.exit(-1)
        
    with open('hotspot_raw.csv', 'w+') as csvfile:
        fieldnames = ['date', 'email', 'message', 'id', 'author', 'file']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for cmt in cmts:
            for file in cmt['files']:
                writer.writerow({'date': cmt['date'], 'email': cmt['email'], 'message': cmt['message'], 'id': cmt['id'], 'author': cmt['author'], 'file': file})
        # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    

def main():
    path = raw_input('Please input your repository path: (default: projects/Lab213)') \
     or '/Users/harry/Documents/projects/Lab213' 
    comments = get_commits(path)
    write_to_csv(comments)
    
main()