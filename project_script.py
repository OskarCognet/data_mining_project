import os
import json
import zipfile

try:
    os.mkdir("images")
except FileExistsError:
    pass

#{"username":"oskarcognet","key":"929baddf391d0a06468ca27bee3c435b"}

#!pip install kaggle
api_token = {"username":"oskarcognet","key":"929baddf391d0a06468ca27bee3c435b"}
with open('/content/.kaggle/kaggle.json', 'w') as file:
    json.dump(api_token, file)
#!chmod 600 /content/.kaggle/kaggle.json
#!kaggle config path -p /content
#!kaggle competitions download -c jigsaw-toxic-comment-classification-challenge
os.chdir('/content/competitions/jigsaw-toxic-comment-classification-challenge')
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall()
    zip_ref.close()