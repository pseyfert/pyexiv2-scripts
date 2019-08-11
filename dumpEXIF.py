#!/usr/bin/python3

import sys
from gi.repository import GExiv2

for i in range(1, len(sys.argv)):
    metadata = GExiv2.Metadata(sys.argv[i])
    for key in metadata:
        print("{}: {}".format(key, metadata[key]))
