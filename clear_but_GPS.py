#!/usr/bin/python3

import sys
from gi.repository import GExiv2

keeptags = ['Exif.Image.GPSTag',
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
            'Exif.GPSInfo.GPSDateStamp']


for i in range(1, len(sys.argv)):
    metadata = GExiv2.Metadata(sys.argv[i])
    for key in metadata:
        if key not in keeptags:
            metadata.__delitem__(key)
    metadata.save_file()
