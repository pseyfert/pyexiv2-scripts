#!/usr/bin/python3

import sys
from gi.repository import GExiv2

deftags = {
    'Exif.Image.Model': "S1234",
    'Exif.Nikon3.SerialNumber': "1234567",
    'Exif.Nikon3.Lens': "180/10 42/23",
    'Exif.Nikon3.LensFStops': "13 37",
    'Exif.Nikon3.LensType': "42",
    'Exif.NikonLd3.LensIDNumber': "100"
}

for i in range(1, len(sys.argv)):
    metadata = GExiv2.Metadata(sys.argv[i])

    for key in metadata:
        if key in deftags:
            metadata[key] = deftags[key]
    metadata.save_file()
