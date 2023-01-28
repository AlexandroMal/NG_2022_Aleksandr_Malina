import os
import zipfile
from pathlib import Path
import threading


#add image in zip archive
def archiver_image():
    zip_clear()
    zip_file = zipfile.ZipFile(".\\Images.zip", "a") 
    num = 0
    while num < len(list(Path('.\\images').glob('*.*'))):
        zip_file.write(f'.\\images\\image{num}.png')
        num += 1
        print(f'Image {num} added in Zip!')
    

#path to directory with archive
def path_zipfile():
    path = (str(os.path.abspath(".\\Images.zip")))
    return path
    
#create new directory
def directory_new():
    try:
        for file in os.scandir(".\\images"):
            os.remove(file.path)
    except:
        os.mkdir(".\\images")
        
#create new zip file     
def zip_clear():
    if os.path.exists(".\\Images.zip"):
        os.remove(".\\Images.zip")
       
#save image in some threading
def manager_zip():
    thr = threading.Thread(target=archiver_image,)
    
    thr.start()
    thr.join()
