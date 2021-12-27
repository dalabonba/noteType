from gtts import gTTS
from playsound import playsound
#Error 263 for command==>pip install playsound==1.2.2 https://stackoverflow.com/questions/68531326/what-is-the-error-in-the-code-for-this-playsound-module-even-though-the-syntax-i
#[Errno 13] Permission denied，第一次可以正常撥放聲音，但之後檔案位置只要存在同名的檔案，就會報錯[Errno13]==>每次執行完就把檔案刪除 https://stackoverflow.com/questions/39818922/errno-13-permission-denied-file-mp3-python

import os

s=gTTS("abc.mp3")

file="abc.mp3"

s.save(file)
playsound(file)

os.remove(file)