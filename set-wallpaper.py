import urllib
import re
import os

dirPath = os.path.dirname(os.path.realpath(__file__))
apodHTML = urllib.urlopen("http://apod.nasa.gov/apod/astropix.html").read()
imageURI = re.search('(?<=href=")image/\d+/[a-zA-Z0-9_.]+', apodHTML)
apodImage = urllib.urlretrieve('http://apod.nasa.gov/apod/'+imageURI.group(0), "wallpaper.jpg")
os.system("gsettings set org.gnome.desktop.background picture-uri file://"+dirPath+"/wallpaper.jpg")
