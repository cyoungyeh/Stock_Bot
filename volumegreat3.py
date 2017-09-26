# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:22:32 2015

@author: tim
"""
# 請先安裝 sudo apt-get install sendemail

import os
import sys
#os.path.join(os.path.sep, "home", "tim", "Stock_Bot") 
#os.sys.path.insert(0, '/home/tim/Stock_Bot')
#os.sys.path.insert(0, '/home/tim/Stock_Bot/')
#os.sys.path.insert(0, './')
sys.path.append('/home/tim/Stock_Bot')
sys.path.append('/home/tim/Stock_Bot/')
from datetime import datetime
from grs import BestFourPoint
from grs import Stock
from grs import TWSENo
from grs import OTCNo
from csvv import yields as fields #殖益率
from csvv import yields_otc as fields_otc #殖益率
#from sell_buy_immediately import stock_buy_sell_oneday as oneday #是否為現股當充



OTC_no_name = OTCNo().all_stock     # 所有上櫃股票名稱與代碼字典 type: dict

OTC_no_list = OTCNo().all_stock_no # 所有上櫃股票代碼


content = "贏要衝,輸要縮."   #沒有辦法換行

time_now = datetime.now().strftime("%Y%m%d_%H%M%S") #今天的日期 ex:2015-0411
title = str(time_now+"增3倍") #Email郵件的標題 ex:2015-0411-選股機器人

day = 20

#attachment = str(time_now)+'-'+str(day)+'.txt' #附件名稱使用當日時間 ex:2015-0411.txt

fileopen = open("volumegreat3.txt", 'w') #開啟檔案,w沒有該檔案就新增

f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n
PW = f.readline().strip('\n')




fileopen.write("\n"+"增3倍"+"\n\n")

#=====================

fileopen.write('\n\n\n上櫃公司股票篩選\n\n\n')
index = 1 
for i in OTC_no_list:
    #print i
    try:
        if BestFourPoint(Stock(i,mons=1)).volumegreat3():
           print i,'otc'         #暴量長紅2天

           fileopen.write(str(index)+" "+"-"+OTC_no_name[i].encode("UTF-8")+"-"+i+"-"+"殖益率"+str(fields_otc()[i][2])+"\n")
           index = index + 1 
    except:     # 回傳為None 或 資料不足導致ValueError
        pass

fileopen.close()                #關閉檔案
 
os.system('sendEmail -o \
 -f u160895@taipower.com.tw \
 -t "WEI <weihautin@gmail.com>" \
 -s smtp.gmail.com:587 \
 -xu %s \
 -xp %s \
 -u %s \
 -o message-file=/home/tim/volumegreat3.txt \
 '%(ID, PW, title))

