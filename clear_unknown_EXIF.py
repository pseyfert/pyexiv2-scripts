#!/usr/bin/python3

import sys
from gi.repository import GExiv2

keeptags = ['Exif.Image.Make',
            'Exif.Image.Model',
            'Exif.Image.Orientation',
            'Exif.Image.XResolution',
            'Exif.Image.YResolution',
            'Exif.Image.ResolutionUnit',
            'Exif.Image.Software',
            'Exif.Image.DateTime',
            'Exif.Image.YCbCrPositioning',
            'Exif.Image.ExifTag',
            'Exif.Photo.ExposureTime',
            'Exif.Photo.FNumber',
            'Exif.Photo.ExposureProgram',
            'Exif.Photo.ISOSpeedRatings',
            'Exif.Photo.SensitivityType',
            'Exif.Photo.ExifVersion',
            'Exif.Photo.DateTimeOriginal',
            'Exif.Photo.DateTimeDigitized',
            'Exif.Photo.ComponentsConfiguration',
            'Exif.Photo.CompressedBitsPerPixel',
            'Exif.Photo.ExposureBiasValue',
            'Exif.Photo.MaxApertureValue',
            'Exif.Photo.MeteringMode',
            'Exif.Photo.LightSource',
            'Exif.Photo.Flash',
            'Exif.Photo.FocalLength',
            'Exif.Photo.MakerNote',
            'Exif.MakerNote.Offset',
            'Exif.MakerNote.ByteOrder',
            'Exif.Nikon3.Version',
            'Exif.Nikon3.ISOSpeed',
            'Exif.Nikon3.Quality',
            'Exif.Nikon3.WhiteBalance',
            'Exif.Nikon3.Focus',
            'Exif.Nikon3.FlashSetting',
            'Exif.Nikon3.FlashDevice',
            'Exif.Nikon3.WhiteBalanceBias',
            'Exif.Nikon3.WB_RBLevels',
            'Exif.Nikon3.ProgramShift',
            'Exif.Nikon3.ExposureDiff',
            'Exif.Nikon3.Preview',
            'Exif.NikonPreview.Compression',
            'Exif.NikonPreview.XResolution',
            'Exif.NikonPreview.YResolution',
            'Exif.NikonPreview.ResolutionUnit',
            'Exif.NikonPreview.JPEGInterchangeFormat',
            'Exif.NikonPreview.JPEGInterchangeFormatLength',
            'Exif.NikonPreview.YCbCrPositioning',
            'Exif.Nikon3.FlashComp',
            'Exif.Nikon3.ISOSettings',
            'Exif.Nikon3.ImageBoundary',
            'Exif.Nikon3.FlashExposureComp',
            'Exif.Nikon3.FlashBracketComp',
            'Exif.Nikon3.ExposureBracketComp',
            'Exif.Nikon3.CropHiSpeed',
            'Exif.Nikon3.ExposureTuning',
            'Exif.Nikon3.SerialNumber',
            'Exif.Nikon3.ColorSpace',
            'Exif.NikonVr.Version',
            'Exif.NikonVr.VibrationReduction',
            'Exif.NikonVr.0x0007',
            'Exif.Nikon3.ActiveDLighting',
            'Exif.NikonPc.Version',
            'Exif.NikonPc.Name',
            'Exif.NikonPc.Base',
            'Exif.NikonPc.0x002c',
            'Exif.NikonPc.Adjust',
            'Exif.NikonPc.QuickAdjust',
            'Exif.NikonPc.Sharpness',
            'Exif.NikonPc.Contrast',
            'Exif.NikonPc.Brightness',
            'Exif.NikonPc.Saturation',
            'Exif.NikonPc.HueAdjustment',
            'Exif.NikonPc.FilterEffect',
            'Exif.NikonPc.ToningEffect',
            'Exif.NikonPc.ToningSaturation',
            'Exif.NikonWt.Timezone',
            'Exif.NikonWt.DaylightSavings',
            'Exif.NikonWt.DateDisplayFormat',
            'Exif.NikonIi.ISO',
            'Exif.NikonIi.0x0001',
            'Exif.NikonIi.ISOExpansion',
            'Exif.NikonIi.ISO2',
            'Exif.NikonIi.0x0007',
            'Exif.NikonIi.ISOExpansion2',
            'Exif.NikonIi.0x000c',
            'Exif.NikonIi.0x000d',
            'Exif.Nikon3.0x002b',
            'Exif.Nikon3.0x002c',
            'Exif.Nikon3.0x002d',
            'Exif.Nikon3.0x0032',
            'Exif.Nikon3.LensType',
            'Exif.Nikon3.Lens',
            'Exif.Nikon3.FlashMode',
            'Exif.Nikon3.ShootingMode',
            'Exif.Nikon3.AutoBracketRelease',
            'Exif.Nikon3.LensFStops',
            'Exif.NikonSi02xx.Version',
            'Exif.NikonSi02xx.0x0004',
            'Exif.NikonSi02xx.ShutterCount1',
            'Exif.NikonSi02xx.DeletedImageCount',
            'Exif.NikonSi02xx.0x0072',
            'Exif.NikonSi02xx.VibrationReduction',
            'Exif.NikonSi02xx.0x0076',
            'Exif.NikonSi02xx.VibrationReduction1',
            'Exif.NikonSi02xx.0x0083',
            'Exif.NikonSi02xx.ShutterCount2',
            'Exif.NikonSi02xx.0x0159',
            'Exif.NikonSi02xx.VibrationReduction2',
            'Exif.NikonSi02xx.0x01af',
            'Exif.NikonSi02xx.ISO',
            'Exif.NikonSi02xx.0x0257',
            'Exif.NikonSi02xx.ShutterCount',
            'Exif.NikonSi02xx.0x027a',
            'Exif.Nikon3.NoiseReduction',
            'Exif.NikonCb2b.Version',
            'Exif.NikonCb2b.0x0002',
            'Exif.NikonCb2b.0x008e',
            'Exif.NikonCb2b.WB_RGGBLevels',
            'Exif.NikonCb2b.0x0095',
            'Exif.NikonLd3.Version',
            'Exif.NikonLd3.ExitPupilPosition',
            'Exif.NikonLd3.AFAperture',
            'Exif.NikonLd3.0x0006',
            'Exif.NikonLd3.0x0007',
            'Exif.NikonLd3.FocusPosition',
            'Exif.NikonLd3.0x0009',
            'Exif.NikonLd3.FocusDistance',
            'Exif.NikonLd3.FocalLength',
            'Exif.NikonLd3.LensIDNumber',
            'Exif.NikonLd3.LensFStops',
            'Exif.NikonLd3.MinFocalLength',
            'Exif.NikonLd3.MaxFocalLength',
            'Exif.NikonLd3.MaxApertureAtMinFocal',
            'Exif.NikonLd3.MaxApertureAtMaxFocal',
            'Exif.NikonLd3.MCUVersion',
            'Exif.NikonLd3.EffectiveMaxAperture',
            'Exif.NikonLd3.0x0014',
            'Exif.NikonLd3.0x0015',
            'Exif.NikonLd3.0x0016',
            'Exif.NikonLd3.0x0017',
            'Exif.NikonLd3.0x0018',
            'Exif.NikonLd3.0x0019',
            'Exif.NikonLd3.0x001a',
            'Exif.NikonLd3.0x001b',
            'Exif.NikonLd3.0x001c',
            'Exif.NikonLd3.0x001d',
            'Exif.NikonLd3.0x001e',
            'Exif.NikonLd3.0x001f',
            'Exif.NikonLd3.0x0020',
            'Exif.NikonLd3.0x0021',
            'Exif.NikonLd3.0x0022',
            'Exif.Nikon3.0x009d',
            'Exif.Nikon3.RetouchHistory',
            'Exif.Nikon3.ImageDataSize',
            'Exif.Nikon3.0x00a3',
            'Exif.Nikon3.ShutterCount',
            'Exif.Nikon3.FlashInfo',
            'Exif.Nikon3.VariProgram',
            'Exif.NikonMe.Version',
            'Exif.NikonMe.MultiExposureMode',
            'Exif.NikonMe.MultiExposureShots',
            'Exif.NikonMe.MultiExposureAutoGain',
            'Exif.Nikon3.HighISONoiseReduction',
            'Exif.Nikon3.0x00b6',
            'Exif.NikonAf2.Version',
            'Exif.NikonAf2.ContrastDetectAF',
            'Exif.NikonAf2.AFAreaMode',
            'Exif.NikonAf2.PhaseDetectAF',
            'Exif.NikonAf2.PrimaryAFPoint',
            'Exif.NikonAf2.AFPointsUsed',
            'Exif.NikonAf2.0x000f',
            'Exif.NikonAf2.AFImageWidth',
            'Exif.NikonAf2.AFImageHeight',
            'Exif.NikonAf2.AFAreaXPosition',
            'Exif.NikonAf2.AFAreaYPosition',
            'Exif.NikonAf2.AFAreaWidth',
            'Exif.NikonAf2.AFAreaHeight',
            'Exif.NikonAf2.ContrastDetectAFInFocus',
            'Exif.NikonFi.Version',
            'Exif.NikonFi.0x0004',
            'Exif.NikonFi.DirectoryNumber',
            'Exif.NikonFi.FileNumber',
            'Exif.NikonFi.0x000a',
            'Exif.Nikon3.0x00bb',
            'Exif.Nikon3.0x00bf',
            'Exif.Photo.UserComment',
            'Exif.Photo.SubSecTime',
            'Exif.Photo.SubSecTimeOriginal',
            'Exif.Photo.SubSecTimeDigitized',
            'Exif.Photo.FlashpixVersion',
            'Exif.Photo.ColorSpace',
            'Exif.Photo.PixelXDimension',
            'Exif.Photo.PixelYDimension',
            'Exif.Photo.InteroperabilityTag',
            'Exif.Iop.InteroperabilityIndex',
            'Exif.Iop.InteroperabilityVersion',
            'Exif.Photo.SensingMethod',
            'Exif.Photo.FileSource',
            'Exif.Photo.SceneType',
            'Exif.Photo.CFAPattern',
            'Exif.Photo.CustomRendered',
            'Exif.Photo.ExposureMode',
            'Exif.Photo.WhiteBalance',
            'Exif.Photo.DigitalZoomRatio',
            'Exif.Photo.FocalLengthIn35mmFilm',
            'Exif.Photo.SceneCaptureType',
            'Exif.Photo.GainControl',
            'Exif.Photo.Contrast',
            'Exif.Photo.Saturation',
            'Exif.Photo.Sharpness',
            'Exif.Photo.SubjectDistanceRange',
            'Exif.Thumbnail.Compression',
            'Exif.Thumbnail.XResolution',
            'Exif.Thumbnail.YResolution',
            'Exif.Thumbnail.ResolutionUnit',
            'Exif.Thumbnail.JPEGInterchangeFormat',
            'Exif.Thumbnail.JPEGInterchangeFormatLength',
            'Exif.Thumbnail.YCbCrPositioning',
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
            'Exif.GPSInfo.GPSDateStamp']

for i in range(1, len(sys.argv)):
    metadata = GExiv2.Metadata(sys.argv[i])
    for key in metadata:
        if key not in keeptags:
            metadata.__delitem__(key)
    metadata.save_file()
