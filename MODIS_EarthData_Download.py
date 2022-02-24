##MODIS_Earthdata_Download
##Author: Martin Rapilly
##script for MODIS imagery downloading through a list of URL obtained from Earthdata website



##first you need to get a list of MODIS images URL from https://earthdata.nasa.gov/ saved in a txt file

import os,sys
import os.path
import webbrowser, time

##opens txt file and creates a loop to check every url
for url in open('E:\...\MOD09A1_links_earthdata.txt'):
##takes out the \n in the list of urls     
    url=url.rstrip('\n')
    print url
    print "waiting..."
##checks if the file has already been downloaded or not    
    if os.path.exists ("E:/.../"+ url[-45:]):
        print "ALREADY DOWNLOADED!"
    else:
##opens web browser to download the file into the download folder   
        webbrowser.open(url)
##if the file hasn't been downloaded, starts the download and waits until completion before downloading next file
        cntr=0
##enter here the download folder path
        while not os.path.exists ("D:/.../Downloads/"+ url[-45:]):
            time.sleep(1)
            print str(cntr)
            cntr=cntr+1
            
    
        
    
    
