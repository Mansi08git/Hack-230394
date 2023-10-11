#import libraries
import requests
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import threading
from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model


#creating GUI 
root = tk.Tk()
root.title('Currency Converter')
root.geometry('500x450')
root['bg']='azure2'


#creating variable
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)


#setting variables 
variable1.set("choose currency")
variable2.set("choose currency")


#Creating Header 
lbl_txt = Label(root,text = 'CURRENCY CONVERTER',font=("Time New Roman",'18','bold'),bg='azure2')
lbl_txt.place(x=110)


#url of api key 
url = 'https://api.apilayer.com/exchangerates_data/latest?base=INR&symbols=EUR,INR,ZAR,USD,AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BGN,BDT,BBD,BWP,BND,BOB,BHD,BIF,BSD,BRL,BMD,BTC,BTN,BYN,BYR,BZD,CAD,CDF,CHF,CLF,CLP,CNY,COP,CRC,CUC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,FJD,FKP,GBP,GEL,GGP,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IMP,IQD,IRR,ISK,JEP,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LRD,LSL,LTL,LVL,LYD,MAD,MDL,MGA,MKD,MMK,MNT,MOP,MRO,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SHP,SLE,SLL,SOS,SRD,SSP,STD,SVC,SYP,SZL,THB,TJS,TMT,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,UYU,UZS,VEF,VES,VND,VUV,WST,XAF,XAG,XAU,XCD,XDR,XOF,XPF,YER,ZMK,ZMW,ZWL&amount=5&date=2023-10-01' 
headers = {
       "apikey":"s5eYjJ3Abu2kTs5tdEqaWAk7qWbDcM0L"
    }
response = requests.get(url,headers=headers)


#Creating function for getting exchange rates
def get_exchange_rates(base_currency,target_currency):
    base_currency=variable1.get()
    target_currency=variable2.get()
    if response.status_code==200:
        data = response.json()
        exchange_rates = data["rates"].get(target_currency)
        return exchange_rates,4
    else:
        print("Failes to fetch exchange rates")
        return None
    

#Function for currency conversion
def currencyconversion():

    base_currency = variable1.get()
    target_currency = variable2.get()
    
    if response.status_code==200:
        convert_data = response.json()
        amount = 1
        result = (convert_data['rates'][target_currency]*amount)/convert_data['rates'][base_currency]
        new_amount = float("{:.4f}".format(result))
        des_amount.insert(0,f"1 {base_currency} = {new_amount} {target_currency}")
        return des_amount
    else:
        print("Fails to fetch exchange rates")
        return None

class Message(Model):
    message: str


# Create an agent for sending alerts
alert = Agent(name="alert", seed="alert_notifier")


# Function to monitor exchange rates and send alerts
def monitor_exchange_rate():
    while True:
        try:
            base_currency = variable1.get()
            target_currency = variable2.get()
            threshold_up = float(thres_up.get())
            threshold_down = float(thres_down.get())
            convert_data = response.json()
            current_rate=(convert_data['rates'][target_currency]*1)/convert_data['rates'][base_currency]
 
            
            
            if current_rate is not None:
                if current_rate > threshold_up:
                   
                    @alert.on_interval(period=30)
                    async def warn(ctx: Context):
                        warnings = ctx.send(destination="destination_here", message=Message(message="Threshold limit exceeded"))
                        messagebox.showinfo("Exchange Rate Alert","Exchange rate more than upper limit")
   
                       
                elif current_rate < threshold_down:
                    @alert.on_interval(period=30)
                    async def warn(ctx: Context):
                        warnings = ctx.send(destination="destination_here", message=Message(message="Threshold limit exceeded"))
                        messagebox.showinfo("Exchange Rate Alert","Exchange rate less than lower limit")
   

        except ValueError:
            pass  # Handle invalid threshold values gracefully
        time.sleep(300)
def combined():
    currency_conversion_thread = threading.Thread(target=currencyconversion)
    exchange_rate_thread = threading.Thread(target=monitor_exchange_rate)
    
    currency_conversion_thread.start()
    exchange_rate_thread.start()


#Function for clearing all values
def clear_all():
    des_amount.delete(0,tk.END)
    thres_down.delete(0,tk.END)
    thres_up.delete(0,tk.END)
    

#list of currencies
list= ['EUR','INR','ZAR','USD','AED','AFN','ALL','AMD','ANG','AOA','ARS','AUD','AWG','AZN','BGN','BGD','BDT','BBD','BWP','BND','BOB','BHD','BIF','BSD','BRL','BMD','BTC','BTN','BYN','BYR','BZD','CAD','CDF','CHF','CLF','CLP','CNY','COP','CRC','CUC','CUP','CVE','CZK','DJF','DKK','DOP','DZD','EGP','ERN','ETB','FJD','FKP','GBP','GEL','GGP','GHS','GIP','GMD','GNF','GTQ','GYD','HKD','HNL','HRK','HTG','HUF','IDR','ILS','IMP','IQD','IRR','ISK','JEP','JMD','JOD','JPY','KES','KGS','KHR','KMF','KPW','KRW','KWD','KYD','KZT','LAK','LBP','LKR','LRD','LSL','LTL','LVL','LYD','MAD','MDL','MGA','MKD','MMK','MNT','MOP','MRO','MUR','MVR','MWK','MXN','MYR','MZN','NAD','NGN','NIO','NOK','NPR','NZD','OMR','PAB','PEN','PGK','PHP','PKR','PLN','PYG','QAR','RON','RSD','RUB','RWF','SAR','SBD','SCR','SDG','SEK','SGD','SHP','SLE','SLL','SOS','SRD','SSP','STD','SVC','SYP','SZL','THB','TJS','TMT','TND','TOP','TRY','TTD','TWD','TZS','UAH','UGX','UYU','UZS','VEF','VES','VND','VUV','WST','XAF','XAG','XAU','XCD','XDR','XOF','XPF','YER','ZMK','ZMW','ZWL']


#Creating label from currency 
lbl_txt = tk.Label(root,text="Base Currency :",font=("Helvetica",'15','bold'),bg='azure2')
lbl_txt.place(x=50,y=100)


#Creating label to currency 
lbl_txt = tk.Label(root,text="Target Currency     :",font=("Helvetica",'15','bold'),bg='azure2')
lbl_txt.place(x=50,y=140)


lbl_txt = tk.Label(root,text="Upper Limit    :",font=("Helvetica",'15','bold'),bg='azure2')
lbl_txt.place(x=50,y=180)


lbl_txt = tk.Label(root,text="Lower Limit    :",font=("Helvetica",'15','bold'),bg='azure2')
lbl_txt.place(x=50,y=220)


thres_up = tk.Entry(root,font=('Helvetica','15','bold'),bg='white')
thres_up.place(x =220,y = 180,height=25,width = 200)


thres_down = tk.Entry(root,font=('Helvetica','15','bold'),bg='white')
thres_down.place(x =220,y = 220,height=25,width = 200)


#Creating label Converted amount 
lbl_txt=tk.Label(root,text="Exchange Rates:",font=("Helvetica",15,'bold'),bg='azure2')
lbl_txt.place(x=50,y=340) 
des_amount=Entry(root,font=('Helvetica','15','bold'),bg='white')
des_amount.place(x=220,y=340,height=25,width=200)


FromCurrency_option = tk.OptionMenu(root,variable1,*list)
ToCurrency_option = tk.OptionMenu(root, variable2,*list)
 

FromCurrency_option.place(x=270,y=105,height=25,width=150)
ToCurrency_option.place(x=270,y=140,height=25,width=150)


#Convert button
Btn1 = Button(root,text="OK",font=("Helvetica",'18','bold'),bg='darkslategray3',command= combined)
Btn1.place(x=160,y=280,height = 30,width = 120)


#Clear all button 
Btn2 = Button(root,text="Clear All",font=("Helvetica",'18','bold'),bg='darkslategray3',command=clear_all)
Btn2.place(x=160,y=380,height = 30,width = 120)

root.mainloop()

if __name__ == "__main__":
    # Start the uagents agent in a separate thread
    alert_thread = threading.Thread(target=alert.run)
    #alert_thread.daemon = True  # Set as a daemon thread so it exits when the main program exits
    alert_thread.start()
