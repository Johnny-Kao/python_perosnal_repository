#_*_coding:utf-8_*_

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# =================================
# 目的：发送邮件
# 功能：单一收件人、任意填写的发信人、任意主题、任意内文、附件
# 待优化：确认附件档案大小/格式、确认可使用的服务器
# 已知可使用stmp.qq.com


# 邮件服务器/登入账号/登录密码或API_Secret
smtp_srv = "YOUR_SERVER_ADDRESS"
_user = "USER_NAME"
_pwd = "USER_PASSWD"

def send_mail(to_addr, title, content, from_addr, att_path = "", att_name = ""):
    # 初始宣告
    msg = MIMEMultipart()

    # 发信人、收件人、主题、内文
    # 发件人可以随意乱填写
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = title
    msg.attach(MIMEText(content))

    # 判定是否有附件路径和附件名称
    if att_name != "" and att_path != "":
        part = MIMEApplication(open(att_path,'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename = att_name)
        msg.attach(part)

    try:
        srv = smtplib.SMTP(smtp_srv, timeout = 30) # 连接smtp邮件服务器,端口默认是25
        srv.login(_user, _pwd) # 登录
        srv.sendmail(_user, to_addr, msg.as_string()) # 发信
        print("发送成功")

    except Exception as e:
        print("发送失败")
    
    finally:
        srv.close()

if __name__ == '__main__':
    # 提示：发信人可以随意填写、附件需为绝对路径、档案名称需加上副档名
    send_mail("RECEIVER_ADDRESS", "TITLE", "CONTENT", "ANY_SENDER", "ATTACHMENT_ADDESS", "ATTACHMENT_NAME")