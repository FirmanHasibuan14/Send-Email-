import smtplib
import ssl
sender_email = input("Enter your email account: \n")
email_password = str(input("Enter your password (NOT YOUR EMAIL PASSWORD): \n"))
to_email = input("Enter the destination of your email account: \n")
message = input("Send your message: \n")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as smtp:
    try:
        smtp.login(sender_email,email_password)
        smtp.set_debuglevel(1)
        print("login success")
        smtp.sendmail(sender_email, to_email,message)
        print("Has successfully sent the email message to", to_email)
    except ValueError:
        print("Error")
    print("GOOD JOB")
    smtp.quit()
