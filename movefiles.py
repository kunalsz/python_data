#Folders : -
#Images = .jpg,.svg,.png
#Videos  = .mp4 , .mkv
#Docs = .txt,.docx,.pdf
#Archives = .tar.xz , .zip , .rar , zxp
#Torrents = .torrent
#Music = .mp3

import os,shutil

cur = '//home//stark//Downloads'

os.chdir(cur)
fileList = os.listdir()


for file in fileList:

    checker = file.endswith

    #IMAGES
    if checker('.svg') or checker('.png') or checker('.jpg'): #Images

        if os.path.exists('Images'):
            shutil.move(file,'Images')
        else:
            os.makedirs('Images')
            shutil.move(file,'Images')


    #VIDEOS
    elif checker('.mp4') or checker('.mkv'): #Videos

        if os.path.exists('Videos'):
            shutil.move(file,'Videos')
        else:
            os.makedirs('Videos')
            shutil.move(file,'Videos')


    #DOCS
    elif checker('.txt') or checker('.docx') or checker('.pdf') or checker('.epub'): #Docs

        if os.path.exists('Docs'):
            shutil.move(file,'Docs')
        else:
            os.makedirs('Docs')
            shutil.move(file,'Docs')


    #ARCHIVE
    elif checker('.tar.xz') or checker('.zip') or checker('.rar') or checker('.zxp'):

        if os.path.exists('Archive'):
            shutil.move(file,'Archive')
        else:
            os.makedirs('Archive')
            shutil.move(file,'Archive')


    #TORRENT
    elif checker('.torrent'): # Torrent

        if os.path.exists('Torrent'):
            shutil.move(file,'Torrent')
        else:
            os.makedirs('Torrent')
            shutil.move(file,'Torrent')


    #MUSIC
    elif checker('.mp3'): # Music

        if os.path.exists('Music'):
            shutil.move(file,'Music')
        else:
            os.makedirs('Music')
            shutil.move(file,'Music')

