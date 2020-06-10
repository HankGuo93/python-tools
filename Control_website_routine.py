# -*- coding: utf-8 -*-
"""
Created on Wed May  1 07:52:39 2019

@author: user1
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException  
import pyautogui      
from time import sleep
from fpdf import FPDF
#import pyautogui
from datetime import timedelta
import datetime

L = input()
P = int(L)
J = int(L)
#昨天日期
yesterday = datetime.datetime.today() + timedelta(P*-1)
#Date = yesterday.strftime('%m%d')
Friday = yesterday.strftime('%Y%m%d')
SaveDate = datetime.datetime.today() + timedelta(-1)
Date = SaveDate.strftime('%m%d')

driver = webdriver.Ie()
driver.implicitly_wait(10)
driver.get("https://jsreport.jsidc.com/PineReport/wslogin.aspx")

alert = driver.switch_to.alert
alert.accept()


username = driver.find_element_by_id("txt_USR_UERID")
username.clear()
username.send_keys("P123919658")

elem_pd = driver.find_element_by_id("txt_USR_PASSWD")
elem_pd.clear()
elem_pd.send_keys("Anztw2033")
elem_login=driver.find_element_by_id('btn_sure')
elem_login.click()

#@@@@@@@@@@@.............假日判斷.............@@@@@@@@@@@@@@@@@@@
   
driver.switch_to.frame('syscom_LMenu')
driver.find_element_by_id('h報表查詢列印').click()
driver.find_element_by_id('pMTS160R').click()

driver.switch_to.parent_frame() #切回主frame
driver.switch_to.frame('syscom_RMain')        # frame括號裡面是他的id

#報表下拉選單
select = Select(driver.find_element_by_name('ddl_TRK_RPTID'))
#禮拜六給禮拜五日期
Datefriday = driver.find_element_by_id("ymd_StartDate")
Datefriday.clear()
Datefriday.send_keys(Friday)
 
    #================================報表列印=========================================

def reportno(z,a,b,xX):  #函數式 a=報表名稱  b=報表名稱 C=儲存鈕位置
    select = Select(driver.find_element_by_name('ddl_TRK_RPTID'))
    select.select_by_value(a)
    driver.find_element_by_id('btn_Query').click() #點擊查詢
    driver.find_element_by_id('dGrid_btn_S_'+xX).click()  #點擊儲存
    #切換視窗    

    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    sleep(0.5)
    driver.switch_to.window(window_after)  
    #顯性等待  
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("btn_Confirm"))
    c = 'Z:\\03-外期帳務作業\\01-每日作業\\'+z+'\\'+Date+b
    driver.find_element_by_id('txt_FolderName').send_keys(c)
    driver.find_element_by_id('btn_Confirm').click()   
    alert.accept()

    #切回右主頁
    driver.switch_to.window(window_before)
    driver.switch_to.frame('syscom_RMain')  
            
    return;

#早班 
reportno('00-國內外單量表\\代接','FFP920M         ','',str(0+1*J)) 
reportno('12-對帳歷史資料','FFP900C         ','',str(0+1*J))    
reportno('15-IXF','FFP900H         ','-900-9',str(0+1*J)) #保證金追繳
reportno('15-IXF','FFP900I3        ','-900-11',str(1+2*J)) 
reportno('15-IXF','FFP900M         ','-900-12',str(0+1*J))  
reportno('15-IXF','FFP920J         ','-9752622',str(0+1*J)) 

#晚班
reportno('24-900&920大1P','FFP900A         ','-999買報',str(0+4*J))
reportno('24-900&920大1P','FFP900A         ','-錯帳買報',str(1+4*J))
reportno('9753883買報','FFP900A         ','-9753883買報',str(2+4*J))
reportno('9753896買報','FFP900A         ','-9753896買報',str(3+4*J))
reportno('25-900-20上手買賣報告書','FFP900N         ','-999上手',str(0+2*J))
reportno('25-900-20上手買賣報告書','FFP900N         ','-000上手',str(1+2*J))
reportno('24-900&920大1P','FFP900T         ','-999權益',str(0+4*J))
reportno('24-900&920大1P','FFP900T         ','-X01權益',str(2+4*J))
reportno('24-900&920大1P','FFP900T         ','-X02權益',str(1+4*J))

reportno('24-900&920大1P','FFP900T         ','-000權益',str(3+4*J))
reportno('24-900&920大1P','FFP920G         ','-999幣別佣收',str(0+3*J))
reportno('24-900&920大1P','FFP920G         ','-000幣別佣收',str(1+3*J))
reportno('24-900&920大1P','FFP920G         ','-含IB幣別佣收',str(2+3*J))
reportno('24-900&920大1P','FFP920H         ','-999AE佣收',str(0+3*J))
reportno('24-900&920大1P','FFP920H         ','-000AE佣收',str(1+3*J))
reportno('24-900&920大1P','FFP920H         ','-含IBAE佣收',str(2+3*J))
reportno('24-900&920大1P','FFP920I         ','-存提權益',str(0+1*J))
reportno('24-900&920大1P','FFP920K         ','-交易分析',str(0+1*J))
reportno('24-900&920大1P','FFS391          ','-客戶淨額1',str(0+3*J))
reportno('24-900&920大1P','FFS391          ','-客戶淨額2',str(1+3*J))
reportno('24-900&920大1P','FFS391          ','-上手淨額',str(2+3*J))
reportno('24-900&920大1P','FFS703          ','-703',str(0+1*J))  
reportno('24-900&920大1P','FFS714          ','-714',str(0+1*J))
reportno('37.給財務的900U','FFP900U         ','-900U',str(0+1*J))


#=================TXT TO PDF ================

sleep(1)
filename1 = 'Z:\\03-外期帳務作業\\01-每日作業\\9753883買報\\'+Date+'-9753883買報'
with open(filename1+'.txt') as f:
    AA1 = f.read()
print('轉成pdf中，請稍後...')
pdfA1 = FPDF()
pdfA1.add_page()
pdfA1.add_font('fireflysung', '', 'fireflysung.ttf', uni=True)
pdfA1.set_font('fireflysung', '', 12)
pdfA1.multi_cell(0,5,AA1)
pdfA1.output('Z:\\03-外期帳務作業\\01-每日作業\\9753883買報\\'+Date+'-9753883買報.pdf', 'F')

sleep(1)
filename2 = 'Z:\\03-外期帳務作業\\01-每日作業\\9753896買報\\'+Date+'-9753896買報'
with open(filename2+'.txt') as f:
    AA2 = f.read()
print('轉成pdf中，請稍後...')
pdfA2 = FPDF()
pdfA2.add_page()
pdfA2.add_font('fireflysung', '', 'fireflysung.ttf', uni=True)
pdfA2.set_font('fireflysung', '', 12)
pdfA2.multi_cell(0,5,AA2)
pdfA2.output('Z:\\03-外期帳務作業\\01-每日作業\\9753896買報\\'+Date+'-9753896買報.pdf', 'F')