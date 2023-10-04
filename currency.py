#import libraries 
import requests
import tkinter as tk

from tkinter import *

from tkinter import ttk

#from forex_python.converter import CurrencyRates,CurrencyCodes


#creating GUI 
root = tk.Tk()
root.title('Currency Converter')
root.geometry('500x650')
root['bg']='gray81'

 
#creating variable
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)


#setting variables 
variable1.set("choose currency")
variable2.set("choose currency")


#Creating Header 
lbl_txt = Label(root,text = 'Currency Converter',font=("Time New Roman",'18','bold'),bg='gray81')
lbl_txt.place(x=135)


#Function for currency conversion
def currencyconversion():

    from_currency = variable1.get()
    to_currency = variable2.get()
    url = 'https://api.apilayer.com/fixer/latest?base=INR&symbols=AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAN,BGN,BGD,BDT,BBD,BWP,BND,BOB,BHD,BIF,BSD,BRL,BMD,BTC,BTN,BYN,BYR,BZD,CAD,CDF,CHF,CLF,CLP,CNY,COP,CRC,CUC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,FJD,FKP,GBP,GEL,GGP,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IMP,INR,IQD,IRR,ISK,JEP,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LRD,LSL,LTL,LVL,LYD,MAD,MDL,MGA,MKD,MMK,MNT,MOP,MRO,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SHP,SLE,SLL,SOS,SRD,SSP,STD,SVC,SYP,SZL,THB,TJS,TMT,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,USD,UYU,UZS,VEF,VES,VND,VUV,WST,XAF,XAG,XAU,XCD,XDR,XOF,XPF,YER,ZAR,ZMK,ZMW,ZWL&amount=5&date=2023-10-01'
    
    headers = {
        "apikey":"LcuMIw3xRrFZixXlcCtLLTONGuJsuEr1"
    }
    response = requests.get(url,headers=headers)
    convert_data = response.json()
    amount = float(sor_amount.get())
    result = (convert_data['rates'][to_currency]*amount)/convert_data['rates'][from_currency]

    #convert_amount = c.convert(from_currency,to_currency,float(sor_amount.get()))
    new_amount = float("{:.4f}".format(result))
    des_amount.insert(0,str(new_amount))
    return des_amount


#Function for clearing all values
def clear_all():
    sor_amount.delete(0,tk.END)
    des_amount.delete(0,tk.END)


#creating label Amount 
lbl_txt = Label(root,text="Amount             :",font=("Helvetica",'15','bold'),bg='gray81')
lbl_txt.place(x=50,y=60)


#Taking value from user
sor_amount = tk.Entry(root,font=('Helvetica','18','bold'),bg='White')
sor_amount.place(x=220,y=65,height= 25,width = 200) 


#list of currencies
list= ['AED','AFN','ALL','AMD','ANG','AOA','ARS','AUD','AWG','AZN','BAN','BGN','BGD','BDT','BBD','BWP','BND','BOB','BHD','BIF','BSD','BRL','BMD','BTC','BTN','BYN','BYR','BZD','CAD','CDF','CHF','CLF','CLP','CNY','COP','CRC','CUC','CUP','CVE','CZK','DJF','DKK','DOP','DZD','EGP','ERN','ETB','EUR','FJD','FKP','GBP','GEL','GGP','GHS','GIP','GMD','GNF','GTQ','GYD','HKD','HNL','HRK','HTG','HUF','IDR','ILS','IMP','INR','IQD','IRR','ISK','JEP','JMD','JOD','JPY','KES','KGS','KHR','KMF','KPW','KRW','KWD','KYD','KZT','LAK','LBP','LKR','LRD','LSL','LTL','LVL','LYD','MAD','MDL','MGA','MKD','MMK','MNT','MOP','MRO','MUR','MVR','MWK','MXN','MYR','MZN','NAD','NGN','NIO','NOK','NPR','NZD','OMR','PAB','PEN','PGK','PHP','PKR','PLN','PYG','QAR','RON','RSD','RUB','RWF','SAR','SBD','SCR','SDG','SEK','SGD','SHP','SLE','SLL','SOS','SRD','SSP','STD','SVC','SYP','SZL','THB','TJS','TMT','TND','TOP','TRY','TTD','TWD','TZS','UAH','UGX','USD','UYU','UZS','VEF','VES','VND','VUV','WST','XAF','XAG','XAU','XCD','XDR','XOF','XPF','YER','ZAR','ZMK','ZMW','ZWL']

#Creating label from currency 
lbl_txt = tk.Label(root,text="From Currency :",font=("Helvetica",'15','bold'),bg='gray81')
lbl_txt.place(x=50,y=100)


#Creating label to currency 
lbl_txt = tk.Label(root,text="To Currency     :",font=("Helvetica",'15','bold'),bg='gray81')
lbl_txt.place(x=50,y=140)


#Creating label Converted amount 
lbl_txt=tk.Label(root,text="Converted Amo:",font=("Helvetica",15,'bold'),bg='Gray81')
lbl_txt.place(x=50,y=240) 
des_amount=Entry(root,font=('Helvetica','15','bold'),bg='white')
des_amount.place(x=220,y=240,height=25,width=200)


FromCurrency_option = tk.OptionMenu(root,variable1,*list)
ToCurrency_option = tk.OptionMenu(root, variable2,*list)
 

FromCurrency_option.place(x=270,y=105,height=25,width=150)
ToCurrency_option.place(x=270,y=140,height=25,width=150)


#Convert button
Btn1 = Button(root,text="Convert",font=("Helvetica",'18','bold'),bg='darkslategray3',command= currencyconversion)
Btn1.place(x=120,y=190,height = 30,width = 120)


#Clear all button 
Btn2 = Button(root,text="Clear All",font=("Helvetica",'18','bold'),bg='darkslategray3',command=clear_all)
Btn2.place(x=120,y=280,height = 30,width = 120)


root.mainloop()
