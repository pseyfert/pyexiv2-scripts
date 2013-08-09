#!/usr/bin/python

deftags = [
'Exif.Image.GPSTag',
'Exif.GPSInfo.GPSVersionID',
'Exif.GPSInfo.GPSLatitudeRef',
'Exif.GPSInfo.GPSLatitude',
'Exif.GPSInfo.GPSLongitudeRef',
'Exif.GPSInfo.GPSLongitude',
'Exif.GPSInfo.GPSAltitudeRef',
'Exif.GPSInfo.GPSAltitude',
'Exif.GPSInfo.GPSTimeStamp',
'Exif.GPSInfo.GPSSatellites',
'Exif.GPSInfo.GPSImgDirectionRef',
'Exif.GPSInfo.GPSImgDirection',
'Exif.GPSInfo.GPSMapDatum',
'Exif.GPSInfo.GPSDateStamp'
]
import sys, pyexiv2
for i in range(1,len(sys.argv)):
   metadata = pyexiv2.ImageMetadata(sys.argv[i])
   metadata.read()
   #for key in deftags:
   for key,name in metadata.items():
     if not key in deftags :
       metadata.__delitem__(key)
   metadata.write(True)
#     else :
#      print sys.argv[i] + "\t doesn't contain compass information"

