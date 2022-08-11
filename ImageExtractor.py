import requests
import os
from bs4 import BeautifulSoup
from pathlib import Path
import re

targetUrl=""
while(targetUrl!='STOP'):
    #getting URL from user STOP to exit
    targetUrl=input("Please paste the URL you want to scrape (enter STOP to exit):")
    if(targetUrl=='STOP'):break
    #requesting the page from website
    page =requests.get(targetUrl)
    #creating BeautifulSoup object to manipulate and filling  it with content from GET
    soup = BeautifulSoup(page.content,'html.parser')

    #contains all of our images from HOMEPAGE
    #urls = soup.find_all("a", class_=["content-thumbnail"])

    images=soup.find_all("img", class_=["alignnone"])
    name=soup.find("h1",class_=["entry-title"])
    filenameproto=name.text
    filenameproto = re.sub('[^0-9a-zA-Z\/]+', '', filenameproto)
    filepathproto=filenameproto
    filecounter=0

    currentpath=Path(os.getcwd())
    filepath=currentpath / filenameproto 
    os.mkdir(filepath)

    print("Processing")
    for i in range(1,len(images)):
        filename=str(filenameproto)+" "+str(filecounter)+".jpg"

        r=requests.get(images[i].attrs['data-src'])
    
        with open(filename,"wb") as file:
            file.write(r.content)

        currentimagepath=currentpath / filename
        destinationimagepath=filepath / filename
        os.rename(currentimagepath,destinationimagepath)
        filecounter=filecounter+1
        filename=filenameproto
    print("Scraped all images!")
print("Thank you for using ImageExtractor9000")
