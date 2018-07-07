import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import smtplib
from email.mime.text import MIMEText

def do_ranking():
    res = urllib.request.urlopen("http://itpro.nikkeibp.co.jp/NSW/?rt=nocnt")
    soup = BeautifulSoup(res,'html.parser')
    res.close()

    ranking = ''
    for i, a in enumerate(soup.select('td.txt8 > a'), start=1):
        ranking = ranking + str(i) + '位：' + a.text + ' http://itpro.nikkeibp.co.jp' + a['href']  + '\n'
    print('ランキングを取得しました')
    return ranking

def do_mail(ranking):
    msg = MIMEText(ranking)
    msg['Subject'] = '本日のアクセスランキング'
    msg['From'] = 'hashimoto0106@gmail.com'
    msg['To'] = 'hashimoto0106@gmail.com'

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('hashimoto0106@gmail.com','taniken84')
    s.send_message(msg)
    s.close()
    print('ランキングをメールしました')

if __name__ == '__main__':
    while True:
        do_mail(do_ranking())
        sleep(3600)
