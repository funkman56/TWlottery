# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:40:36 2019

@author: Relieak
"""

'''
台灣彩券
'''

from bs4 import BeautifulSoup 
import requests

url = "http://www.taiwanlottery.com.tw/"
html = requests.get(url)

html.encoding = 'utf-8'                         #轉成可中文編碼否則會出現亂碼

sp = BeautifulSoup(html.text, 'html.parser')
data1 = sp.select("#rightdown")
#print((data1))            
''' list 格式 '''
#print(data1[0])
''' bs4  格式 '''

while True :

    print("")
    print("~"*9,"歡迎進入台灣彩券查詢系統","~"*9)
    print("查詢威力彩     請按1\n查詢38樂合彩   請按2\n查詢大樂透     請按3\n查詢49樂合彩   請按4\n查詢今彩539    請按5\n查詢39樂合彩   請按6\n查詢3星彩      請按7\n查詢4星彩      請按8\n查詢雙贏彩     請按9\n查詢賓果賓果   請按10\n請按ENTER 離開")
    SearchResult = input("請輸入要搜尋的項目>>")
    print("")

    if SearchResult == "1" or SearchResult == "2" or SearchResult == "3" or SearchResult == "4"  :           # 不可以寫  SearchResult == "1" or "2" or "3" or "4" 會出現無法解決的Bug
        
      
#        data2 = data1[0].find("div",{"class" : "contents_box02"})         #find() 找到第一個符合條件的內容
        
        data2 = data1[0].find_all("div",{"class" : "contents_box02"})      #find_all 找出所有符合條件的內容
        
#        print(data2)             # list 格式                              #看不懂程式記得打開看結果

        if SearchResult == "1" :
            
            data3 = data2[0].find_all("div",{"class" : "ball_tx ball_green"})    
#            print(data3[0])       # html 格式
#            print(data3[0].text)  # text 格式
            
            print("~"*9,"威力彩本期開獎","~"*9)
            print("開出順序 :",data3[0].text,data3[1].text,data3[2].text,data3[3].text,data3[4].text,data3[5].text)
            print("大小順序 :",data3[6].text,data3[7].text,data3[8].text,data3[9].text,data3[10].text,data3[11].text)
            print("第二區   :",data2[0].find("div",{"class" : "ball_red"}).text)
           
        
        elif SearchResult == "2" :      
            
            data3 = data2[1].find_all("div",{"class" : "ball_tx ball_green"})                
            print("~"*9,"38樂合彩本期開獎","~"*9)
            print("開出順序 :",data3[0].text,data3[1].text,data3[2].text,data3[3].text,data3[4].text,data3[5].text)
            print("大小順序 :",data3[6].text,data3[7].text,data3[8].text,data3[9].text,data3[10].text,data3[11].text)

                  
        elif  SearchResult == "3"  :
               
            data3 = data2[2].find_all("div",{"class" : "ball_tx ball_yellow"})
            #print(data3)
            print("~"*9,"大樂透本期開獎","~"*9)
            print("開出順序 :",data3[0].text,data3[1].text,data3[2].text,data3[3].text,data3[4].text,data3[5].text)
            print("大小順序 :",data3[6].text,data3[7].text,data3[8].text,data3[9].text,data3[10].text,data3[11].text)
            print("特別號   :",data2[2].find("div",{"class" : "ball_red"}).text)
            
        elif  SearchResult == "4"  :
            
            data3 = data2[3].find_all("div",{"class" : "ball_tx ball_yellow"})
            print("~"*9,"49樂合彩本期開獎","~"*9)
            print("開出順序 :",data3[0].text,data3[1].text,data3[2].text,data3[3].text,data3[4].text,data3[5].text)
            print("大小順序 :",data3[6].text,data3[7].text,data3[8].text,data3[9].text,data3[10].text,data3[11].text)
    
    elif SearchResult == "5" or SearchResult == "6":
        
        data2 = data1[0].find_all("div",{"class" : "contents_box03"})
#        print(data2)   #list 格式
        if SearchResult == "5" :
            
            data3 = data2[0].find_all("div",{"class" : "ball_tx ball_lemon"})
            print("~"*9,"今彩539本期開獎","~"*9)
        
        elif SearchResult == "6" :
            
            data3 = data2[1].find_all("div",{"class" : "ball_tx ball_lemon"})
            print("~"*9,"39樂合彩本期開獎","~"*9)
        
        
        print("開出順序 :",data3[0].text,data3[1].text,data3[2].text,data3[3].text,data3[4].text)
        print("大小順序 :",data3[5].text,data3[6].text,data3[7].text,data3[8].text,data3[9].text)
        
    elif SearchResult == "7" or SearchResult == "8" :
        
        data2 = data1[0].find_all("div" , {"class" : "contents_box04"})
        #print(data2)   #list 格式
        
        if SearchResult == "7" :
            
            data3 = data2[0].find_all("div",{"class" : "ball_tx ball_purple"})
            
#            print(data3)  #list 格式
            
            print("~"*9,"3星彩本期開獎","~"*9)
            print("中獎號碼 :",data3[0].text,data3[1].text,data3[2].text)
        
        elif SearchResult == "8" :
            
            data3 = data2[1].find_all("div",{"class" : "ball_tx ball_purple"})
            
            print("~"*9,"4星彩本期開獎","~"*9)
            print("中獎號碼 :",data3[0].text,data3[1].text,data3[2].text,data3[3].text)
    
    elif SearchResult == "9" :
        
        data2 = data1[0].find("div" , {"class" : "contents_box06"})
        data3 = data2.find_all("div" , {"class" : "ball_tx ball_blue"})        
#        print(data3)   #list 格式
        
        print("~"*9,"雙贏彩本期開獎","~"*9)
        
        print("開出順序 :")
        for x in range(0,12) :
            print(data3[x].text,end=" ")
        print("\n大小順序 :")
        for i in range(12,24) :
            print(data3[i].text,end=" ")
        print("")
    
    elif SearchResult == "10" :
        
        data2 = data1[0].find("div",{"class" : "contents_box01"})
        data3 = data2.find_all("div",{"class" : "ball_tx ball_yellow"})
#        print(data3) # list格式
        
        print("~"*9,"賓果賓果本期開獎","~"*9)
        
        print("開出獎號 :")
#        for x in range(0,20) :           #全部號碼一起顯示
        for x in range(0,10) :            #拆成兩行號碼顯示
            print(data3[x].text,end=" ")   
        print("\n")                       #斷行       
        for x in range(10,20) :
            print(data3[x].text,end=" ")          
        print("\n")                       #斷行
               
        print("超級獎號 :",data2.find("div",{"class" : "ball_red"}).text)
        print("猜大小 :",data2.find("div",{"class" : "ball_blue_BB1"}).text)
        print("猜單雙 :",data2.find("div",{"class" : "ball_blue_BB2"}).text)
            
            
    elif SearchResult == "" :
        
        
        break
        

    else :
                   
        print("輸入錯誤請重新輸入!!")