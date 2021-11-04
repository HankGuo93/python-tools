import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import xlrd
import os
from xlutils.copy import copy
import time

requests.adapters.DEFAULT_RETRIES = 10000

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}


#------------------HKE-------------------------
try:
    def monthToNum_1(shortMonth):
        return{
                'JAN' : '01',
                'FEB' : '02',
                'MAR' : '03',
                'APR' : '04',
                'MAY' : '05',
                'JUN' : '06',
                'JUL' : '07',
                'AUG' : '08',
                'SEP' : '09', 
                'OCT' : '10',
                'NOV' : '11',
                'DEC' : '12'
        }[shortMonth]

    yesterday = date.today()-timedelta(days=1)
    settleday = yesterday.strftime('%y%m%d')

    response_hhi = requests.get('https://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hhif'+settleday+'.htm')

    lines = response_hhi.text.split('\r')

    a_1 = lines[22:25]

    lines_1 = a_1[0].replace(' ', '_')
    lines_2 = a_1[1].replace(' ', '_')
    lines_3 = a_1[2].replace(' ', '_')

    #print(d,d[0:7],d[86:92],g,g[0:7],g[86:92])

    newlines = [lines_1,lines_2,lines_3]

    extralines1 = []

    for x in newlines:

        extralines1.append(x[1:7])
        if x[86] == '_':
            extralines1.append(x[87:92])
        else:
            extralines1.append(x[86:92])

    extralines2 = []

    for y in range(0, len(extralines1), 2) :

        r_1 = extralines1[y].replace(extralines1[y][0:3],str(monthToNum_1(extralines1[y][0:3])))
        extralines2.append(int(r_1.replace(r_1,('20'+r_1[3:5]+r_1[0:2])))) 

    response_hsi = requests.get('https://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsif'+settleday+'.htm')

    lines = response_hsi.text.split('\r')

    a_2 = lines[22:25]

    lines_4 = a_2[0].replace(' ', '_')
    lines_5 = a_2[1].replace(' ', '_')
    lines_6 = a_2[2].replace(' ', '_')

    #print(d,d[0:7],d[86:92],g,g[0:7],g[86:92])

    newlines = [lines_4,lines_5,lines_6]

    extralines3 = []

    for x in newlines:

        extralines3.append(x[1:7])
        extralines3.append(x[86:92])

    extralines4 = []

    for y in range(0, len(extralines1), 2) :

        r_2 = extralines3[y].replace(extralines3[y][0:3],str(monthToNum_1(extralines3[y][0:3])))
        extralines4.append(int(r_2.replace(r_2,('20'+r_2[3:5]+r_2[0:2]))))  
except:
    pass


#------------------SGX-------------------------
import time
def yearToNum(shortyear):
    return{
            str(time.localtime().tm_year-1)[2:4] : str(time.localtime().tm_year-1),
            str(time.localtime().tm_year)[2:4] : str(time.localtime().tm_year),
            str(time.localtime().tm_year+1)[2:4] : str(time.localtime().tm_year+1),
            str(time.localtime().tm_year+2)[2:4] : str(time.localtime().tm_year+2),
            str(time.localtime().tm_year+3)[2:4] : str(time.localtime().tm_year+3),
            str(time.localtime().tm_year+4)[2:4] : str(time.localtime().tm_year+4),
            str(time.localtime().tm_year+5)[2:4] : str(time.localtime().tm_year+5),
            str(time.localtime().tm_year+6)[2:4] : str(time.localtime().tm_year+6),
            str(time.localtime().tm_year+7)[2:4] : str(time.localtime().tm_year+7),
            str(time.localtime().tm_year+8)[2:4] : str(time.localtime().tm_year+8),
    }[shortyear]
def monthToNum(shortMonth):
    return{
            'f' : '01',
            'g' : '02',
            'h' : '03',
            'j' : '04',
            'k' : '05',
            'm' : '06',
            'n' : '07',
            'q' : '08',
            'u' : '09', 
            'v' : '10',
            'x' : '11',
            'z' : '12',
    }[shortMonth]

#-------------SFC-------------
r = None
while r == None:
    try:
        r = requests.get('https://api.sgx.com/derivatives/v1.0/contract-code/CN?order=asc&orderby=delivery-month&category=futures&session=-1', headers = headers, verify=False) 
        
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'lxml')
        
        xxx = str(soup).split('symbol')
        
        list_1 = []
        
        for y in xxx:
            list_1.append(y.split(','))
        
        del list_1[0]  
        
        list_2 = []
        
        for needed in list_1:
            if needed[20] != 'null':
                if len(needed[20]) > 31:
                    filt =[needed[0],needed[20]]
                    list_2.append(filt)
             
        list_3 = []
        a = 0
        for GGG in list_2:
            list_3.append(int(str(yearToNum(GGG[0][6:8]))+str(monthToNum(GGG[0][5]))))      
            list_3.append(str(int(list_2[a][1][25:32])/100))
            a += 1    
    except:
        pass
 

#-------------SIN-------------
r = None
while r == None:
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        r = requests.get('https://api.sgx.com/derivatives/v1.0/contract-code/IN?order=asc&orderby=delivery-month&category=futures&session=-1', headers = headers, verify=False) 
        
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'lxml')
        
        xxx = str(soup).split('symbol')
        
        list_1_sin = []
        
        for y in xxx:
            list_1_sin.append(y.split(','))
        
        del list_1_sin[0]  
        
        list_2_sin = []
        
        for needed in list_1_sin:
            if needed[20] != 'null':
                if len(needed[20]) > 31:
                    filt =[needed[0],needed[20]]
                    list_2_sin.append(filt)
             
        list_3_sin = []
        a = 0
        for GGG in list_2_sin:
            list_3_sin.append(int(str(yearToNum(GGG[0][6:8]))+str(monthToNum(GGG[0][5]))))         
            list_3_sin.append(str(int(list_2_sin[a][1][25:31])/100))
            a += 1
    except:
        pass

#-------------SID-------------
r = None
while r == None:
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        r = requests.get('https://api.sgx.com/derivatives/v1.0/contract-code/ID?order=asc&orderby=delivery-month&category=futures&session=-1', headers = headers, verify=False) 
        
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'lxml')
        
        xxx = str(soup).split('symbol')
        
        list_1_sid = []
        
        for y in xxx:
            list_1_sid.append(y.split(','))
        
        del list_1_sid[0]  
        
        list_2_sid = []
        
        for needed in list_1_sid:
            if needed[20] != 'null':
                if len(needed[20]) > 31:
                    filt =[needed[0],needed[20]]
                    list_2_sid.append(filt)
             
        list_3_sid = []
        a = 0
        for GGG in list_2_sid:
            list_3_sid.append(int(str(yearToNum(GGG[0][6:8]))+str(monthToNum(GGG[0][5]))))         
            list_3_sid.append(str(int(list_2_sid[a][1][25:31])/100))
            a += 1
    except:
        pass
    

#-------------SGP-------------    
r = None
while r == None:
    try:       
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        r = requests.get('https://api.sgx.com/derivatives/v1.0/contract-code/SGP?order=asc&orderby=delivery-month&category=futures&session=-1', headers = headers, verify=False) 
        
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'lxml')
        
        xxx = str(soup).split('symbol')
        
        list_1_sgp = []
        
        for y in xxx:
            list_1_sgp.append(y.split(','))
        
        del list_1_sgp[0]  
        
        list_2_sgp = []
        
        for needed in list_1_sgp:
            if needed[20] != 'null':
                if len(needed[20]) > 31:
                    filt =[needed[0],needed[20]]
                    list_2_sgp.append(filt)
             
        list_3_sgp = []
        a = 0
        for GGG in list_2_sgp:
            list_3_sgp.append(int(str(yearToNum(GGG[0][7:9]))+str(monthToNum(GGG[0][6]))))         
            list_3_sgp.append(str(int(list_2_sgp[a][1][25:30])/100))
            a += 1
    except:
        pass
    

#-------------STW-------------
r = None
while r == None:
    try:        
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        r = requests.get('https://api.sgx.com/derivatives/v1.0/contract-code/TW?order=asc&orderby=delivery-month&category=futures&session=-1', headers = headers, verify=False) 
        
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'lxml')
        
        xxx = str(soup).split('symbol')
        
        list_1_stw = []
        
        for y in xxx:
            list_1_stw.append(y.split(','))
        
        del list_1_stw[0]  
        
        list_2_stw = []
        
        for needed in list_1_stw:
            if needed[20] != 'null':
                if len(needed[20]) > 31:
                    filt =[needed[0],needed[20]]
                    list_2_stw.append(filt)
             
        list_3_stw = []
        a = 0
        for GGG in list_2_stw:
            list_3_stw.append(int(str(yearToNum(GGG[0][6:8]))+str(monthToNum(GGG[0][5]))))        
            list_3_stw.append(str(int(list_2_stw[a][1][25:30])/100))
            a += 1
    except:
        pass
    

#-------------SSI-------------
r = None
while r == None:
    try:        
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        r = requests.get('https://api.sgx.com/derivatives/v1.0/contract-code/NK?order=asc&orderby=delivery-month&category=futures&session=-1', headers = headers, verify=False) 
        
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'lxml')
        
        xxx = str(soup).split('symbol')
        
        list_1_ssi = []
        
        for y in xxx:
            list_1_ssi.append(y.split(','))
        
        del list_1_ssi[0]  
        
        list_2_ssi = []
        
        for needed in list_1_ssi:
            if needed[20] != 'null':
                if len(needed[20]) > 31:
                    filt =[needed[0],needed[20]]
                    list_2_ssi.append(filt)
             
        list_3_ssi = []
        a = 0
        for GGG in list_2_ssi:
            list_3_ssi.append(int(str(yearToNum(GGG[0][6:8]))+str(monthToNum(GGG[0][5]))))         
            list_3_ssi.append(str(int(list_2_ssi[a][1][25:30])))
            a += 1
    except:
        pass

#------------------EUX-------------------------
try:
    def monthToNum_dax(shortMonth):
        return{
                'Mar' : '03',
                'Jun' : '06',
                'Sep' : '09',
                'Dec' : '12',
        }[shortMonth]

    #日期
    r_date_dax = requests.get('https://www.eurexchange.asia/asia-01/products/equity_index_derivatives/dax/34642!fullOrderBook', headers = headers)

    if r_date_dax.status_code == requests.codes.ok:
        soup_date_dax = BeautifulSoup(r_date_dax.text, 'lxml')

    list_dax_date2 = []    
    date_dax = soup_date_dax.html.find_all('span')

    for b in date_dax:
        if len(b.text) == 8 and b.text.find(',') == -1 and b.text.find('Q') == -1:
            list_dax_date2.append(b.text[4:8] + monthToNum_dax(b.text[0:3]))



    #-------------DAX-------------

    list_dax_udr2 = []
    for i in list_dax_date2:
        r_udr_dax = requests.get('https://www.eurexchange.asia/asia-01/products/equity_index_derivatives/dax/34642!quotesSingleViewFuture?maturityDate=' + i, headers = headers) 

        if r_udr_dax.status_code == requests.codes.ok:
            soup_udr_dax = BeautifulSoup(r_udr_dax.text, 'lxml')

        list_dax_udr1 = []
        udr_dax = soup_udr_dax.html.find_all('span')
        for b in udr_dax:
            if len(b.text) < 10:
                list_dax_udr1.append(b.text)  #24個
        list_dax_udr2.append((list_dax_udr1[24].replace('.','')).replace(',','.'))

    #-------------FESX-------------

    list_fesx_udr2 = []
    for i in list_dax_date2:
        r_udr_fesx = requests.get('https://www.eurexchange.asia/asia-01/products/equity_index_derivatives/euro_stoxx/34652!quotesSingleViewFuture?maturityDate=' + i, headers = headers) 

        if r_udr_fesx.status_code == requests.codes.ok:
            soup_udr_dax = BeautifulSoup(r_udr_fesx.text, 'lxml')

        list_fesx_udr1 = []
        udr_fesx = soup_udr_dax.html.find_all('span')

        for b in udr_fesx:
            if len(b.text) < 10:
                list_fesx_udr1.append(b.text)  #24個
        list_fesx_udr2.append((list_fesx_udr1[24].replace('.','')).replace(',','.'))

     #-------------FESB-------------   

    list_fesb_udr2 = []

    for i in list_dax_date2:
        r_udr_fesb = requests.get('https://www.eurexchange.com/exchange-en/products/idx/stx/esf/34686!quotesSingleViewFuture?maturityDate=' + i, headers = headers) 

        if r_udr_fesb.status_code == requests.codes.ok:
            soup_udr_fesb = BeautifulSoup(r_udr_fesb.text, 'lxml')

        list_fesb_udr1 = []
        udr_fesb = soup_udr_fesb.html.find_all('span')
        for b in udr_fesb:
            if len(b.text) < 10:
                list_fesb_udr1.append(b.text)  #24個
        list_fesb_udr2.append((list_fesb_udr1[24].replace('.','')).replace(',','.'))
except:
    pass

#------------------FINAL STEP------------------
filename = 'manul-settlement.xls'
book_r = xlrd.open_workbook(filename)
book_w = copy(book_r)
sheet1 = book_w.get_sheet(0)

try:
    sheet1.write(0,0,'HHI'),sheet1.write(0,1,extralines2[0]),sheet1.write(0,2,extralines1[1])   #-----HKE
    sheet1.write(1,0,'HHI'),sheet1.write(1,1,extralines2[1]),sheet1.write(1,2,extralines1[3])    
    sheet1.write(2,0,'HHI'),sheet1.write(2,1,extralines2[2]),sheet1.write(2,2,extralines1[5])    
    sheet1.write(3,0,'HSI'),sheet1.write(3,1,extralines4[0]),sheet1.write(3,2,extralines3[1])   
    sheet1.write(4,0,'HSI'),sheet1.write(4,1,extralines4[1]),sheet1.write(4,2,extralines3[3])    
    sheet1.write(5,0,'HSI'),sheet1.write(5,1,extralines4[2]),sheet1.write(5,2,extralines3[5])    
    sheet1.write(6,0,'MCH'),sheet1.write(6,1,extralines2[0]),sheet1.write(6,2,extralines1[1])    
    sheet1.write(7,0,'MCH'),sheet1.write(7,1,extralines2[1]),sheet1.write(7,2,extralines1[3])    
    sheet1.write(8,0,'MCH'),sheet1.write(8,1,extralines2[2]),sheet1.write(8,2,extralines1[5])    
    sheet1.write(9,0,'MHI'),sheet1.write(9,1,extralines4[0]),sheet1.write(9,2,extralines3[1])    
    sheet1.write(10,0,'MHI'),sheet1.write(10,1,extralines4[1]),sheet1.write(10,2,extralines3[3]) 
    sheet1.write(11,0,'MHI'),sheet1.write(11,1,extralines4[2]),sheet1.write(11,2,extralines3[5])
except:
    pass
    '''
    for i in range(12):
        sheet1.write(i,2,'null')
    '''
try:
    sheet1.write(12,0,'SFC'),sheet1.write(12,1,list_3[0]),sheet1.write(12,2,float(list_3[1]))           #----SGX
    sheet1.write(13,0,'SFC'),sheet1.write(13,1,list_3[2]),sheet1.write(13,2,float(list_3[3]))
    sheet1.write(14,0,'SFC'),sheet1.write(14,1,list_3[4]),sheet1.write(14,2,float(list_3[5]))

    sheet1.write(15,0,'SIN'),sheet1.write(15,1,list_3_sin[0]),sheet1.write(15,2,float(list_3_sin[1]))           
    sheet1.write(16,0,'SIN'),sheet1.write(16,1,list_3_sin[2]),sheet1.write(16,2,float(list_3_sin[3]))
    sheet1.write(17,0,'SIN'),sheet1.write(17,1,list_3_sin[4]),sheet1.write(17,2,float(list_3_sin[5]))

    sheet1.write(18,0,'SID'),sheet1.write(18,1,list_3_sid[0]),sheet1.write(18,2,float(list_3_sid[1]))           
    sheet1.write(19,0,'SID'),sheet1.write(19,1,list_3_sid[2]),sheet1.write(19,2,float(list_3_sid[3]))
    sheet1.write(20,0,'SID'),sheet1.write(20,1,list_3_sid[4]),sheet1.write(20,2,float(list_3_sid[5]))

    sheet1.write(21,0,'SSG'),sheet1.write(21,1,list_3_sgp[0]),sheet1.write(21,2,float(list_3_sgp[1]))          
    sheet1.write(22,0,'SSG'),sheet1.write(22,1,list_3_sgp[2]),sheet1.write(22,2,float(list_3_sgp[3]))
    sheet1.write(23,0,'SSG'),sheet1.write(23,1,list_3_sgp[4]),sheet1.write(23,2,float(list_3_sgp[5]))

    sheet1.write(24,0,'STW'),sheet1.write(24,1,list_3_stw[0]),sheet1.write(24,2,float(list_3_stw[1]))          
    sheet1.write(25,0,'STW'),sheet1.write(25,1,list_3_stw[2]),sheet1.write(25,2,float(list_3_stw[3]))
    sheet1.write(26,0,'STW'),sheet1.write(26,1,list_3_stw[4]),sheet1.write(26,2,float(list_3_stw[5]))
    sheet1.write(27,0,'SSI'),sheet1.write(27,1,list_3_ssi[0]),sheet1.write(27,2,float(list_3_ssi[1]))           
    sheet1.write(28,0,'SSI'),sheet1.write(28,1,list_3_ssi[2]),sheet1.write(28,2,float(list_3_ssi[3]))
    sheet1.write(29,0,'SSI'),sheet1.write(29,1,list_3_ssi[4]),sheet1.write(29,2,float(list_3_ssi[5]))
except:
    pass
    '''
    for i in range(12):
        i=i+12
        sheet1.write(i,2,'null')
    '''
try:
    if len(list_dax_udr2) > 2:
        sheet1.write(30,0,'DAX'),sheet1.write(30,1,int(list_dax_date2[0])),sheet1.write(30,2,float(list_dax_udr2[0]))           
        sheet1.write(31,0,'DAX'),sheet1.write(31,1,int(list_dax_date2[1])),sheet1.write(31,2,float(list_dax_udr2[1]))
        sheet1.write(32,0,'DAX'),sheet1.write(32,1,int(list_dax_date2[2])),sheet1.write(32,2,float(list_dax_udr2[2]))
        sheet1.write(33,0,'FDXM'),sheet1.write(33,1,int(list_dax_date2[0])),sheet1.write(33,2,float(list_dax_udr2[0]))           
        sheet1.write(34,0,'FDXM'),sheet1.write(34,1,int(list_dax_date2[1])),sheet1.write(34,2,float(list_dax_udr2[1]))
        sheet1.write(35,0,'FDXM'),sheet1.write(35,1,int(list_dax_date2[2])),sheet1.write(35,2,float(list_dax_udr2[2]))
        sheet1.write(36,0,'FESX'),sheet1.write(36,1,int(list_dax_date2[0])),sheet1.write(36,2,float(list_fesx_udr2[0]))           
        sheet1.write(37,0,'FESX'),sheet1.write(37,1,int(list_dax_date2[1])),sheet1.write(37,2,float(list_fesx_udr2[1]))
        sheet1.write(38,0,'FESX'),sheet1.write(38,1,int(list_dax_date2[2])),sheet1.write(38,2,float(list_fesx_udr2[2]))
        sheet1.write(39,0,'FESB'),sheet1.write(39,1,int(list_dax_date2[0])),sheet1.write(39,2,int(list_fesb_udr2[0])/100)           
        sheet1.write(40,0,'FESB'),sheet1.write(40,1,int(list_dax_date2[1])),sheet1.write(40,2,int(list_fesb_udr2[1])/100)
        sheet1.write(41,0,'FESB'),sheet1.write(41,1,int(list_dax_date2[2])),sheet1.write(41,2,int(list_fesb_udr2[2])/100)

    else:
        sheet1.write(30,0,'DAX'),sheet1.write(30,1,int(list_dax_date2[0])),sheet1.write(30,2,float(list_dax_udr2[0]))           
        sheet1.write(31,0,'DAX'),sheet1.write(31,1,int(list_dax_date2[1])),sheet1.write(31,2,float(list_dax_udr2[1]))
        sheet1.write(32,0,'DAX'),sheet1.write(32,1,'null'),sheet1.write(32,2,'null')
        sheet1.write(33,0,'FDXM'),sheet1.write(33,1,int(list_dax_date2[0])),sheet1.write(33,2,float(list_dax_udr2[0]))           
        sheet1.write(34,0,'FDXM'),sheet1.write(34,1,int(list_dax_date2[1])),sheet1.write(34,2,float(list_dax_udr2[1]))
        sheet1.write(35,0,'FDXM'),sheet1.write(35,1,'null'),sheet1.write(35,2,'null')
        sheet1.write(36,0,'FESX'),sheet1.write(36,1,int(list_dax_date2[0])),sheet1.write(36,2,float(list_fesx_udr2[0]))           
        sheet1.write(37,0,'FESX'),sheet1.write(37,1,int(list_dax_date2[1])),sheet1.write(37,2,float(list_fesx_udr2[1]))
        sheet1.write(38,0,'FESX'),sheet1.write(38,1,'null'),sheet1.write(38,2,'null')
        sheet1.write(39,0,'FESB'),sheet1.write(39,1,int(list_dax_date2[0])),sheet1.write(39,2,int(list_fesb_udr2[0])/100)           
        sheet1.write(40,0,'FESB'),sheet1.write(40,1,int(list_dax_date2[1])),sheet1.write(40,2,int(list_fesb_udr2[1])/100)
        sheet1.write(41,0,'FESB'),sheet1.write(41,1,'null'),sheet1.write(41,2,'null')
except:
    pass
    '''
    for i in range(13):
        i=i+29
        sheet1.write(i,2,'null')
    '''
    
os.remove(filename)
book_w.save(filename)

print('done!')
input()

#vision of JSON  [SGX]
'''
import requests
import datetime
import json

SGX=[]

def sgx_settlement(udr):    
    def monthchange(change):
        return{
                udr.lower()+'f19' : '201901',
                udr.lower()+'g19' : '201902',
                udr.lower()+'h19' : '201903',
                udr.lower()+'j19' : '201904',
                udr.lower()+'k19' : '201905',
                udr.lower()+'m19' : '201906',
                udr.lower()+'n19' : '201907',
                udr.lower()+'q19' : '201908',
                udr.lower()+'u19' : '201909', 
                udr.lower()+'v19' : '201910',
                udr.lower()+'x19' : '201911',
                udr.lower()+'z19' : '201912',
                udr.lower()+'h20' : '202003',
                udr.lower()+'m20' : '202006'
    }[change]
    
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}

    r = requests.get('https://api.sgx.com/derivatives/v1.0/contract-code/'+udr+'?order=asc&orderby=delivery-month&category=futures&session=-1', headers = headers) 
    reqsjson = json.loads(r.text)
    req_key = ['symbol', 'daily-settlement-price']
    sgx_list = reqsjson['data']
    for z in range(0,6):
        info_sgx = [sgx_list[z][x] for x in req_key]
        print(info_sgx)
        if info_sgx[1] != None:
            info_sgx[0]=monthchange(info_sgx[0])
            info_sgx[1]=info_sgx[1]/100
            SGX.append(info_sgx)
'''
