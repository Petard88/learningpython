import zipfile
with zipfile.ZipFile("hola.zip","r") as zip_ref:
    zip_ref.extractall("hej2")