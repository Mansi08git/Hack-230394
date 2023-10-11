import uagents
from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
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
                        messagebox.showinfo("Exchange Rate Alert","More than upper limit")
   
                       
                elif current_rate < threshold_down:
                    @alert.on_interval(period=30)
                    async def warn(ctx: Context):
                        warnings = ctx.send(destination="destination_here", message=Message(message="Threshold limit exceeded"))
                        messagebox.showinfo("Exchange Rate Alert","Less than lower limit")
   

        except ValueError:
            pass  # Handle invalid threshold values gracefully
        time.sleep(300)
