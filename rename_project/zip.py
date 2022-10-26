import zipfile

with zipfile.ZipFile('temp.zip', 'r') as zip_obj:
    zip_obj.extractall()