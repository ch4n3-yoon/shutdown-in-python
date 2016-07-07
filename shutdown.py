# -*- coding : utf-8 -*-
# 이 프로그램은 컴퓨터를 종료하는 파이썬 프로그램입니다. 
import os
import time

sec = input("컴퓨터를 몇 초 후에 종료시키고 싶으세요? : ")
sec_int = int(sec)
print(sec + "초 뒤에 컴퓨터가 꺼집니다...")

for i in range(0, sec_int):
	print(str(i) + " 초 경과")
	time.sleep(1)
	if i == sec_int:
		print("시간이 되었습니다. 컴퓨터가 종료됩니다! ")

os.system("shutdown -s -t 0")
