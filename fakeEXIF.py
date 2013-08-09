#!/usr/bin/python

deftags = {
'Exif.Image.Model':"S1234"
}
import sys, pyexiv2
for i in range(1,len(sys.argv)):
   metadata = pyexiv2.ImageMetadata(sys.argv[i])
   metadata.read()
   #for key in deftags:
   mykeys = []
   for key,value in deftags:
     mykeys += [key]
   for key,name in metadata.items():
     if key in mykeys :
       metadata[key].raw_value = deftags[key]
   metadata.write(True)

