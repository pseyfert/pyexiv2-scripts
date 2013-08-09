pyexiv2-scripts
===============

small python scripts for small tasks working with exif

scripts are developed by reverse engineering what I found in EXIF blocks of
Nikon cameras. Tasks are mainly paranoia inspired: clear all EXIF information,
clear the GPS information, clear all except for the GPS information, fake the
camera model.

paranoia warning
================

the fake is not fully reliable. From the other information in
the block (like apperture) one can still deduce some things about your
photography budget. Similarly if you're really paranoid, then deleting EXIF is
not desired because one will still see that you did remove the EXIF and that
you took the photo.

todo
====

* write nice USAGE messages
* migrate to pyexiv2 replacement
