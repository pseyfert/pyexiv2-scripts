#!/usr/bin/python3

import sys
from gi.repository import GExiv2

for i in range(1, len(sys.argv)):
    metadata = GExiv2.Metadata(sys.argv[i])
    print("direction:")
    if 'Exif.GPSInfo.GPSImgDirection' in metadata:
        print("{}\t{}".format(
            sys.argv[i], metadata['Exif.GPSInfo.GPSImgDirection']))
    else:
        print("{}\tdoesn't contain compass information".format(sys.argv[i]))

    print("altitude:")
    if 'Exif.GPSInfo.GPSAltitude' in metadata:
        print("{}\t{}".format(sys.argv[i],
                              metadata['Exif.GPSInfo.GPSAltitude']))
    else:
        print("{}\tdoesn't contain altitude information".format(sys.argv[i]))

    print("latitude, longitude:")
    if 'Exif.GPSInfo.GPSLatitude' in metadata:
        print("{}\t{},{}".format(
            sys.argv[i], metadata['Exif.GPSInfo.GPSLatitude'], metadata['Exif.GPSInfo.GPSLongitude']))
    else:
        print("{}\tdoesn't contain location information".format(sys.argv[i]))
