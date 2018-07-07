import urllib.request
import smtplib
from email.mime.text import MIMEText

def do_mail():
    msg = MIMEText('test')
    msg['Subject'] = 'テストメール'
    msg['From'] = 'hashimoto0106@gmail.com'
    msg['To'] = 'hashimoto0106@gmail.com'

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('hashimoto0106@gmail.com','taniken84')
    s.send_message(msg)
    s.close()
    print('メール送信完了')

if __name__ == '__main__':
        do_mail()
