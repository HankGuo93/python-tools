# -*- coding: utf-8 -*-

import win32com.client as win32
import datetime
from datetime import timedelta

if datetime.date.today().weekday() == 0:
    yesterday = datetime.datetime.today() + timedelta(-3)
    Date = yesterday.strftime('%m%d')
    YDate = yesterday.strftime('%Y%m%d')
else:
    yesterday = datetime.datetime.today() + timedelta(-1)
    Date = yesterday.strftime('%m%d')
    YDate = yesterday.strftime('%Y%m%d')

# --------------------------------900-12 營業員排行表-------------------------------------  
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'someOne'
mail.CC ="someOnem"
mail.Subject = '營業員業績排行表'
mail.Body = ''
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\15-IXF\\"+Date+"-900-12.txt")
mail.Send()

#--------------------------------------追繳明細------------------------------------------
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'someOne'
mail.CC ="someOne"
mail.Subject = YDate+'追繳明細'
mail.Body = ''
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\15-IXF\\"+Date+"-900-11.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\15-IXF\\"+Date+"-900-9.txt")
mail.Send()

#--------------------------------------9752622亞洲-------------------------------------------
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'someOne'
mail.CC ='someOne'
mail.Subject = YDate+'報告書'
mail.Body = '附檔為即時買賣報告書,其資料內容同買賣報告書。'
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\15-IXF\\"+Date+"-.txt")
mail.Send()

#--------------------------------------淨額調整-------------------------------------------
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'someOne'
mail.CC ="someOne"
mail.Subject = YDate+'客戶與上手淨額調整表'
mail.Body = ''
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-上手淨額.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-客戶淨額1.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-客戶淨額2.txt")
mail.Send()

#--------------------------------------手上買賣報告書、權益、傭收----------------------
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'someOne;'
mail.CC ="someOne"
mail.Subject = YDate+'上手買賣報告書,權益,傭收等'
mail.Body = ''
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-000AE佣收.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-000幣別佣收.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-000權益.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-999AE佣收.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-999買報.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-999幣別佣收.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-999權益.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-X01權益.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-X02權益.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-上手淨額.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-客戶淨額1.txt")

mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-客戶淨額2.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-存提權益.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-含IBAE佣收.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-含IB幣別佣收.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-交易分析.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-錯帳買報.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-703.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-714.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\25-900-20上手買賣報告書\\"+Date+"-999上手.txt")     
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\25-900-20上手買賣報告書\\"+Date+"-000上手.txt")             
mail.Send()

#================#9753883買報================================
# 需要先製作一個pdf 
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To ="someOne"
mail.CC ="someOne"
mail.Subject = '買賣報告書-'+YDate
mail.Body = '報表如附檔 , thanks'
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\買報\\"+Date+"-買報.pdf")
mail.Send()

#================#9753896買報================================
# 需要先製作一個pdf 
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To ="someOne"
mail.CC ="someOne"
mail.Subject = '買賣報告書-'+YDate
mail.Body = '報表如附檔 , thanks'
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\買報\\"+Date+"-買報.pdf")
mail.Send()

#================#138 ================================

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To ="someOne"
mail.CC ="someOne"
mail.Subject = YDate+'-外期每日對帳單'
mail.Body = '此文件僅供所屬營業員核對用,請勿轉予客戶'
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\23-129&138&580\\"+Date+".pdf")
mail.Send()

#==========================自營買報================================

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'someOne;'
mail.CC ="someOne"
mail.Subject = YDate+'自營帳務報表'
mail.Body = ''

mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-999AE佣收.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-999買報.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-999幣別佣收.txt")
mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\24-900&920大1P\\"+Date+"-999權益.txt")
        
mail.Send()


#==========================900-21 900U================================

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'someOne'
mail.CC ="someOne"
mail.Subject = YDate+'900U'
mail.Body = ''

mail.Attachments.Add("Z:\\03-外期帳務作業\\01-每日作業\\37.給財務的900U\\"+Date+"-900U.txt")
        
mail.Send()

