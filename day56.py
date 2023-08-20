import csv
import os
import re

def sanitize_name(name):
    sanitized = re.sub(r'[\\/:*?"<>|]', '_', name)
    return sanitized

try:
    os.makedirs("day56folder")
except FileExistsError:
    pass

with open(os.path.join("day56folder","day56100MostStreamedSongs.csv"), encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        artistname = sanitize_name(row["Artist(s)"])
        songname = sanitize_name(row["Song"])
        foldercheck = os.listdir("day56folder")
        if artistname not in foldercheck:
            makefolder = os.path.join("day56folder", artistname)
            os.makedirs(makefolder)
        songpath = os.path.join(makefolder, songname+".txt")
        f = open(songpath, "w")
        f.close()