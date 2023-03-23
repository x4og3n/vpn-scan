#!/usr/bin/env python
# -*- coding : utf-8 -*-
 
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet vpn yoxlama by xtogen")

print("""
ip daxil edin:
""")
hedefip = input("hedef ip yazin : ")
os.system("ike-scan " + hedefip)
