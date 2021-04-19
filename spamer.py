import pyautogui
import webbrowser
from pyfiglet import Figlet
from lolpython import lol_py 
from datetime import datetime
from random import *
import time


waktu = datetime.now()
jam = waktu.strftime('%H : %M : %S')
tanggal = waktu.strftime('%A, %d - %B - %Y')

# f = Figlet(font='larry3d')
# print(f.renderText('CODER SPAMMER'))
def welcome_menu():
	print("""
┏━┓╋┏┳━━━┳┓┏┓┏┳━━┓┏━━┳━━━┳━━━┳━━━┳━━━┳━━━┓┏━━━┳━━━┳━━━┳━┓┏━┳━┓┏━┳━━━┳━━━┓
┃┃┗┓┃┃┏━━┫┃┃┃┃┃┏┓┃┗┫┣┫┏━━┫┏━┓┃┏━┓┣┓┏┓┃┏━━┛┃┏━┓┃┏━┓┃┏━┓┃┃┗┛┃┃┃┗┛┃┃┏━━┫┏━┓┃
┃┏┓┗┛┃┗━━┫┃┃┃┃┃┗┛┗┓┃┃┃┗━━┫┃╋┗┫┃╋┃┃┃┃┃┃┗━━┓┃┗━━┫┗━┛┃┃╋┃┃┏┓┏┓┃┏┓┏┓┃┗━━┫┗━┛┃
┃┃┗┓┃┃┏━━┫┗┛┗┛┃┏━┓┃┃┃┃┏━━┫┃╋┏┫┃╋┃┃┃┃┃┃┏━━┛┗━━┓┃┏━━┫┗━┛┃┃┃┃┃┃┃┃┃┃┃┏━━┫┏┓┏┛
┃┃╋┃┃┃┗━━╋┓┏┓┏┫┗━┛┣┫┣┫┗━━┫┗━┛┃┗━┛┣┛┗┛┃┗━━┓┃┗━┛┃┃╋╋┃┏━┓┃┃┃┃┃┃┃┃┃┃┃┗━━┫┃┃┗┓
┗┛╋┗━┻━━━┛┗┛┗┛┗━━━┻━━┻━━━┻━━━┻━━━┻━━━┻━━━┛┗━━━┻┛╋╋┗┛╋┗┻┛┗┛┗┻┛┗┛┗┻━━━┻┛┗━┛""")
	print("=====================================================")
	print("CREATE BY IHSAN MAULANA")
	print("TOOLS SPAMMER MESSAGE FOR CHAT ALL SOSMED IN POINTER DEKSTOP")
	print("DATE AND DAY : ", tanggal)
	print("TIME : ", jam, "WIB")
	print("Presented BY NEWBIE CODER TEAM")
	print("=====================================================\n\n")
	get_nama()

# opsi tanya untuk load ke menu utama 
def tanyain():
	pertanyaan = input("apakah anda ingin melanjutkan tool? (yes/no)")
	if pertanyaan == 'yes':
		tampil_list()
	elif pertanyaan == 'no':
		print("Terimakasih telah Menggunakan tools ini")
		time.sleep(3)
		exit()
	else:
		print("Thank youu for using this tools")
# masukin namanya untuk welcome data listnya
def get_nama():
	print("WELCOMEEE SEBELUM NYA MASUKIN NAMA DULUU GANN !!")
	time.sleep(1)
	namalu = input('Masukan nama mu disini gan : ')
	print(f'Hello {namalu} berikut menu nyaa')
	tampil_list()
# membuat fungsi tampil pilih opsi spammer
def tampil_list():
	print('='*10, 'MENU UTAMA SPAMMER', '='*10)
	print('1. Randommode (random jumlah pesan dari 1-30)')
	print('2. Manualmode (input manually)')
	print('3. BomMode (random input jumlah banyak)')
	print('4. Exit/keluar')
	print('='*20, '\n')
	pilih_opsi()
# membuat fungsi pilih_opsi spammer
def pilih_opsi():
	pilihanopsi = input('Masukan Mode input spammer :')
	if pilihanopsi == '1':
		randommode()
	elif pilihanopsi == '2':
		manualmode()
	elif pilihanopsi == '3':
		bommode()
	else:
		print("Anda telah keluar dari program")
		exit()

def randommode():
	jumlahrandom = randint(1, 10)
	pesanrandom = input("Masukan Pesan yang akan di spam (Abaikan jika text dari clipboard) : ")
	print(f'Pesan yang akan di spam yaitu {pesanrandom} dengan jumlah {jumlahrandom}')
	loaded_rand = input("silahkan klik enter untuk meneruskan proses yang berlangsung")
	print("silahkan fokuskan pointer pada kolom chat untuk memproses spammer dalam waktu 3 detik kedepan")
	time.sleep(3)

	for i in range(0,jumlahrandom):
		if pesanrandom != "":
			pyautogui.typewrite(pesanrandom)
			pyautogui.press('enter')
		else:
			pyautogui.hotkey('ctrl', 'v')      
			pyautogui.press("enter")
	print(f'succesfully spam pesan {pesanrandom}')
	tanyain()

def manualmode():
	jumlahmanual = int(input("Masukin Jumlah Pesan spammer nya : "))
	pesanmanual = input("Masukan Pesan yang akan di spam (Abaikan jika text dari clipboard) : ")
	print(f'Pesan yang akan di spam yaitu {pesanmanual} dengan jumlah {jumlahmanual}')
	loaded_man = input("silahkan klik enter untuk meneruskan proses yang berlangsung")
	print("silahkan fokuskan pointer pada kolom chat untuk memproses spammer dalam waktu 3 detik kedepan")
	time.sleep(3)

	for i in range(0,jumlahmanual):
		if pesanmanual != "":
			pyautogui.typewrite(pesanmanual)
			pyautogui.press('enter')
		else:
			pyautogui.hotkey('ctrl', 'v')      
			pyautogui.press("enter")
	print(f'succesfully spam pesan {pesanmanual} sebanyak {jumlahmanual}')
	tanyain()

def bommode():
	jumlahbom = randint(20, 40)
	pesanbom = input("Masukan Pesan yang akan di spam (Abaikan jika text dari clipboard) : ")
	delaybom = int(input("Masukan delay waktu dalam milisec (disarankan 2000) : "))
	print(f'Pesan yang akan di spam yaitu {pesanbom} dengan jumlah {jumlahbom}')
	loaded_bom = input("silahkan klik enter untuk meneruskan proses yang berlangsung")
	print("silahkan fokuskan pointer pada kolom chat untuk memproses spammer dalam waktu 4 detik kedepan")
	time.sleep(4)

	for i in range(0,jumlahbom):
		if pesanbom != "":
			pyautogui.typewrite(pesanbom)
			pyautogui.press('enter')
			time.sleep(delaybom/1000)
		else:
			pyautogui.hotkey('ctrl', 'v')      
			pyautogui.press("enter")
	print(f'succesfully spam pesan {pesanbom} dengan jumlah {jumlahbom} delay {delaybom}')
	tanyain()
if __name__ == '__main__':
	welcome_menu()