#!/usr/bin/python3

import sys
from gi.repository import GExiv2


for i in range(1, len(sys.argv)):
    metadata = GExiv2.Metadata(sys.argv[i])
    for key in metadata:
        metadata.__delitem__(key)
    metadata.save_file()
