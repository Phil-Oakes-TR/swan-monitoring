#Let's import some libraries to handle file operations and FTP

import sys
import ftplib
import datetime

location = r'ftp://prod.ftp.sparrow.int.thomsonreuters.com/Filings/Regulatory Intelligence (TRRI)/'

#Now log into the Sparrow location and get a file list from the TRRI index

#We'll create an empty list called today_folders to contain things that have updated today.

#Then we'll work through the list of top-level folders and query the subfolders to find out ones with a date that matches today's date

ftp = ftplib.FTP('ftp.swan.int.thomsonreuters.com', 'SWANFTP.PUBLIC', 'XXYO8yb4894TvAkz')
ftp.cwd("Filings/Regulatory Intelligence (TRRI)")

today_folders = []
today = datetime.datetime.today().strftime('%Y-%m-%d')

files = ftp.nlst()

#files is every top-level agent that is running in Sparrow
#print(files)
print(str(len(files)) + " agent folders found")

search_depth = 3
#search_depth is number of days to check for updates

found_folders = []
checked_folders = []
empty_folders = []

print(files)

for f in files:
    #this is ignoring every other itme in the list
    #print(f)
    ftp.cwd("/Filings/Regulatory Intelligence (TRRI)/" + f)
    subfolders = ftp.nlst()
    f_empty = 1
    
    for g in subfolders:
        for k in range(0,search_depth):
            k_day = datetime.datetime.now() - datetime.timedelta(days=k)
            k_day = k_day.strftime('%Y-%m-%d')
        
            checked_folders.append(f + '/' + g + '$' + k_day)
            if g.startswith(k_day):
                #print(f + '/' + g)
                found_folders.append(f + '/' + g)
                f_empty = 0
    
    if f_empty:
        empty_folders.append(f)
        
#print(today_folders)   
ftp.close()
#print('Checked')
#print(checked_folders)
print('Empty')
print(empty_folders)

#print(files)

