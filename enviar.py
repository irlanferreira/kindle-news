import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import shutil
from email.mime.application import MIMEApplication
from pathlib import Path



def enviar():
    smt = smtplib.SMTP('smtp.gmail.com', 587)
    smt.starttls()
    smt.login('irlanferreiradasilva2@gmail.com', 'dfwhlvjwpskbmazm')

    menssagem = MIMEMultipart()
    menssagem['From'] = 'irlanferreiradasilva2@gmail.com'
    menssagem['To'] = 'irlanferreiradasilva2_cpt0db@kindle.com'
    menssagem['Subject'] = 'convert'


    jornal_arq = open('.//arqs//The News.epub', 'rb')
    attach = MIMEBase('application', 'octet-stream')
    attach.set_payload(jornal_arq.read())
    encoders.encode_base64(attach)
    attach.add_header('Content-Disposition', f'attachment; filename=The News.epub')
    jornal_arq.close()

    menssagem.attach(attach)

    smt.sendmail(menssagem['From'], menssagem['To'], menssagem.as_string())

