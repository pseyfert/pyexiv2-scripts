#!/usr/bin/python

phototags = {
    'Exif.Photo.ExposureTime':"Belichtung:\t",
    'Exif.Photo.FNumber':"Blende:\t\tF",
    #'Exif.Photo.ExposureProgram',
    'Exif.Photo.ISOSpeedRatings':"ISO:\t\t",
    #'Exif.Photo.SensitivityType',
    #'Exif.Photo.ExifVersion',
    #'Exif.Photo.DateTimeOriginal',
    #'Exif.Photo.DateTimeDigitized',
    #'Exif.Photo.ComponentsConfiguration',
    #'Exif.Photo.CompressedBitsPerPixel',
    #'Exif.Photo.ExposureBiasValue',
    #'Exif.Photo.MaxApertureValue',
    #'Exif.Photo.MeteringMode',
    #'Exif.Photo.LightSource',
    #'Exif.Photo.Flash',
    'Exif.Photo.FocalLength':"Brennweite:\t"
    #'Exif.Photo.MakerNote'
    }
import sys, pyexiv2
for i in range(1,len(sys.argv)):
   metadata = pyexiv2.ImageMetadata(sys.argv[i])
   metadata.read()
   print "file:\t\t", sys.argv[i]
   for key in phototags.keys():
    if key in metadata.exif_keys :
      print phototags[key],  metadata[key].value
   print "-----------------------------\n"
