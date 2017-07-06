
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
import email
import os


def run_mail(mail_from, addr_list, mail_subj, mail_text, pasw,
             attach_file=None, mail_coding="utf-8",
             smtp_server="smtp.gmail.com", smtp_port=587):


    multi_msg = MIMEMultipart()
    multi_msg['From'] = Header(mail_from, mail_coding)
    multi_msg['To'] = ', '.join(addr_list)
    multi_msg['Subject'] =  Header(mail_subj, mail_coding)

    msg = MIMEText(mail_text, 'html', mail_coding)
    msg.set_charset(mail_coding)
    multi_msg.attach(msg)

    # присоединяем атач-файл
    if attach_file:
        file = open(attach_file, 'rb')
        attachment = MIMEBase('application', "octet-stream")
        attachment.set_payload(file.read())
        email.encoders.encode_base64(attachment)
        file.close()
        only_name_attach = Header(os.path.basename(attach_file),mail_coding)
        attachment.add_header('Content-Disposition','attachment; filename="%s"' % only_name_attach)
        multi_msg.attach(attachment)


    # отправка
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(mail_from, pasw)
    smtp.sendmail(mail_from, addr_list, multi_msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    mymail = "zaswed76@gmail.com"
    tomail = "sergitland@gmail.com"
    subj = "тема"

    html = """\
<html>
 <head>
  <meta charset="utf-8">
  <title>Тег B</title>
 </head>
 <body>
  <p><b>Lorem ipsum dolor sit amet</b></p>
  <p><b>Lorem ipsum</b> dolor sit amet, consectetuer adipiscing elit,
  sed diem nonummy nibh euismod tincidunt ut lacreet dolore magna aliguam erat
  volutpat. <b>Ut wisis</b> enim ad minim veniam, quis nostrud exerci
  tution ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.</p>
 </body>
</html>
"""
    text = "текст"
    passw = ""
    run_mail(mymail, [tomail], subj, html, passw)
