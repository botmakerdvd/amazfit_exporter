#!/usr/bin/python3
import sys
import amazfit_exporter

db = sys.argv[1]
dest = sys.argv[2]
amazfit_exporter.db_to_gpx(db,dest)
