from imap_tools import MailBox
import getpass
import os
import io
import PIL.Image as Image

my_email = getpass.getpass('dsautomation91@gmail.com')
my_pass = getpass.getpass('GREESHU_225adi')
download_folder = r"C:\Users\desti\OneDrive - Stratford University\Aditya\DataScience\Python\email_attachments"

mailbox =  MailBox('imap.gmail.com').login(my_email, my_pass )
for msg in mailbox.fetch(charset='utf8'):
    for att in msg.attachments:
        print(att.filename)
        bytes = att.payload
        image = Image.open(io.BytesIO(bytes))
        image.save(download_folder+att.filename)
        print('Attachment Saved>>>>>>>>>>>>>>', image)