import os,time,platform
try:from telethon.sync import TelegramClient
except:os.system("pip install telethon")
from telethon.tl import types
from telethon import functions
from prettytable import PrettyTable
def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)  
        
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'
print (f"{lrd}")
t = PrettyTable([f'{cn}Number{lrd}',f'{cn}Method{lrd}'])
t.add_row([f'{lgn}1{lrd}',f'{gn}Report Spam{lrd}'])
t.add_row([f'{lgn}2{lrd}',f'{gn}Reporter Other{lrd}'])
t.add_row([f'{lgn}3{lrd}',f'{gn}Reporter Violence{lrd}'])
t.add_row([f'{lgn}4{lrd}',f'{gn}Reporter Pornography{lrd}'])
t.add_row([f'{lgn}5{lrd}',f'{gn}Reporter Copyright{lrd}'])
t.add_row([f'{lgn}6{lrd}',f'{gn}Reporter Fake{lrd}'])
t.add_row([f'{lgn}7{lrd}',f'{gn}Reporter Geo Irrelevant{lrd}'])
t.add_row([f'{lgn}8{lrd}',f'{gn}Reporter Illegal Drugs{lrd}'])
t.add_row([f'{lgn}9{lrd}',f'{gn}Reporter Personal Details{lrd}'])
def clear():
    if 'Windows' in platform.uname():
    	try:from colorama import init
    	except:os.system("pip install colorama")
    	init()
    	os.system("cls")
    elif 'Windows' not in platform.uname():
        os.system("clear")
clear()
re(f"""{g}
  _____      __      _   _________     ____    
 (_   _)    /  \    / ) (_   _____)   / __ \   
   | |     / /\ \  / /    ) (___     / /  \ \  
   | |     ) ) ) ) ) )   (   ___)   ( ()  () ) 
   | |    ( ( ( ( ( (     ) (       ( ()  () ) 
  _| |__  / /  \ \/ /    (   )       \ \__/ /  
 /_____( (_/    \__/      \_/         \____/
""")
account = f"""{k}
 ____                             _               
|  _ \   ___  _ __    ___   _ __ | |_   ___  _ __ 
| |_) | / _ \| '_ \  / _ \ | '__|| __| / _ \| '__|
|  _ < |  __/| |_) || (_) || |   | |_ |  __/| |    {cn}Channel{k}
|_| \_\ \___|| .__/  \___/ |_|    \__| \___||_|   
             |_|	

	{lrd}[{lgn}+{lrd}] {gn}Channel : {lgn}@Esfelurm	
			"""	 
			
class TelegramReporter:
    def __init__(self):
        self.api_id = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter Api id account: {g}")
        self.api_hash = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter Api hash account: {g}")
        self.phone_number = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter phone account:{g} ")
        clear()
        re(account)
        print (f"{lrd}")
        print (t)
        self.method = input(f"{lrd}[{lgn}?{lrd}] {gn}Choose a method : {k}")
        self.channel_username = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter username channel {k}")
        self.number = input(f"{lrd}[{lgn}+{lrd}] {gn}Number of reports: {k}")
        self.client = TelegramClient('session', self.api_id, self.api_hash)
    def report_channel(self):
        with self.client as client:
            client.connect()
            if not client.is_user_authorized():
                client.send_code_request(self.phone_number)
                client.sign_in(self.phone_number, input('Enter the code: '))
            try:channel_entity = client.get_entity(self.channel_username)
            except:print (f"{lrd}Username does not exist")
            if self.method == "1":
                message = "This channel contains spam content."
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonSpam(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}A spam report has been sent")            
            elif self.method == "2":
                message = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter your message: {g}")
                for _ in range(0,int(self.number)): 
                     result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonOther(),
                    message=message
                ))
                     print (f"\{lrd}[{lgn}+{lrd}] {gn}A Other report has been sent")
            elif self.method == "3":
                message = "This channel contains violent content."            
                for _ in range(0,int(self.number)): 
                     result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonViolence(),
                    message=message
                ))
                     print (f"\{lrd}[{lgn}+{lrd}] {gn}A Violence report has been sent") 
            elif self.method == "4":
                message = "This channel has pornographic content"
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonPornography(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}A Pornogaphy report has been sent")
            elif self.method == "5":
                message = "Block this channel due to copyright"            
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonCopyright(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}A Copy right report has been sent")
            elif self.method == "6":
                message = "Block this channel due to scam and impersonation"            
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonFake(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}A Fake report has been sent ")
            elif self.method == "7":
                message = "Block this channel due to irrelevant geo "            
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonGeoIrrelevant(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}A Geo Irrelevant report has been sent")
            elif self.method == "8":
                message = "Block this channel because of IllegalDrugs "            
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonIllegalDrugs(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}A Illegal Drugs report has been sent")
            elif self.method == "9":
                message = "Block this channel because of PersonalDetails "            
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonPersonalDetails(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}A Personal Details report has been sent")
                print (f"\n\n{k}End of reports !")
reporter = TelegramReporter()
reporter.report_channel()
