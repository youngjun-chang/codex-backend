# Copyright (C) 2016 Deloitte Argentina.
# This file is part of CodexGigas - https://github.com/codexgigassys/
# See the file 'LICENSE' for copying permission.
import pathmagic
from pymongo import MongoClient
import gridfs
from env import envget

# file_id="906f21f436b0dbb2c9cf37b80a90cdeb061ced3d"
# file_id="109bf9de7b82ffd7b8194aa3741b5d42ee878ebb"
file_id = "6abec077e93226f4d9d9a5351092f3e0baef6d78"

client = MongoClient(envget('files.host'), envget('files.port'))
db = client[envget('db_files_name')]
fs = gridfs.GridFS(db)
f = fs.find_one({"filename": file_id})
if(f is None):
    print("File does not exist.")
    exit(0)
data = f.read()
fd = open(file_id, "w+")
fd.write(data)
fd.close()
print("File found")
