#!/usr/bin/python

import sys, pyexiv2
for i in range(1,len(sys.argv)):
   metadata = pyexiv2.ImageMetadata(sys.argv[i])
   metadata.read()
   if 'Exif.GPSInfo.GPSImgDirection' in metadata.exif_keys :
      print sys.argv[i] + "\t" + metadata['Exif.GPSInfo.GPSImgDirection'].raw_value
   else :
      print sys.argv[i] + "\t doesn't contain compass information"
