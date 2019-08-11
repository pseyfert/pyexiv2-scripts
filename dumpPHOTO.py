#!/usr/bin/python3

import sys
from gi.repository import GExiv2

phototags = {
    'Exif.Photo.ExposureTime': "Belichtung:\t",
    'Exif.Photo.FNumber': "Blende:\t\tF",
    # 'Exif.Photo.ExposureProgram',
    'Exif.Photo.ISOSpeedRatings': "ISO:\t\t",
    # 'Exif.Photo.SensitivityType',
    # 'Exif.Photo.ExifVersion',
    # 'Exif.Photo.DateTimeOriginal',
    # 'Exif.Photo.DateTimeDigitized',
    # 'Exif.Photo.ComponentsConfiguration',
    # 'Exif.Photo.CompressedBitsPerPixel',
    # 'Exif.Photo.ExposureBiasValue',
    # 'Exif.Photo.MaxApertureValue',
    # 'Exif.Photo.MeteringMode',
    # 'Exif.Photo.LightSource',
    # 'Exif.Photo.Flash',
    'Exif.Photo.FocalLength': "Brennweite:\t"
    # 'Exif.Photo.MakerNote'
}

for i in range(1, len(sys.argv)):
    metadata = GExiv2.Metadata(sys.argv[i])
    print("file: {}".format(sys.argv[i]))
    for key in phototags:
        try:
            print("{}:  {}".format(phototags[key], metadata[key]))
        except KeyError:
            continue
