import subprocess
import time

import bs4
import imapclient
import email
from bs4 import BeautifulSoup
import os
import requests
import zipfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
import shutil
from enviar import enviar

if os.path.exists('arqs'):
    pass
else:
    os.makedirs('arqs')

def salvarimg(src, n):
    img = requests.get(src)
    img_nome = n
    extensao = os.path.splitext(src)[1]
    with open(f'.//arqs//{img_nome}{extensao}', 'wb') as img_arq:
        for chunk in img.iter_content(100000000):
            img_arq.write(chunk)
    jornalzip.write(f'.//arqs//{img_nome}{extensao}', compress_type=zipfile.ZIP_DEFLATED)
    return f'{img_nome}{extensao}'

def converter():
    imap_server = 'imap.gmail.com'
    meu_email = 'irlanferreiradasilva2@gmail.com'
    password = 'dfwhlvjwpskbmazm'

    imap = imapclient.IMAPClient(imap_server, ssl=True)
    imap.login(meu_email, password)

    imap.select_folder('INBOX', readonly=True)
    ids = imap.search(['FROM', 'contato@thenewscc.com.br'])

    raw = imap.fetch([ids[-1]], ['BODY[]'])
    message = email.message_from_bytes(raw[ids[-1]][b'BODY[]'])
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == 'text/html':
                html = part.get_payload(decode=True).decode('utf8')
                break
    else:
        html = message.get_payload(decode=True).decode('utf-8')



    sopa = BeautifulSoup(html, 'html.parser')



    cont = 0
    for img in sopa.find_all('img'):
        src = img.get('src')
        path = salvarimg(src, cont)
        html = html.replace(src, f'{path}')
        cont += 1
    with open('.//arqs//index.html', 'w') as arq:
        arq.write(html)
    jornalzip.write('.//arqs//index.html', compress_type=zipfile.ZIP_DEFLATED)
    jornalzip.close()

    imap.logout()
    time.sleep(5)
    enviar()

    shutil.rmtree('arqs')
jornalzip = zipfile.ZipFile(f'.//arqs//The News.epub','w')