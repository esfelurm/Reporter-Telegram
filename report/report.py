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
t.add_row([f'{lgn}2{lrd}',f'{gn}Report Pornography{lrd}'])
t.add_row([f'{lgn}3{lrd}',f'{gn}Report Violence{lrd}'])
t.add_row([f'{lgn}4{lrd}',f'{gn}Report Child Abuse{lrd}'])
t.add_row([f'{lgn}5{lrd}',f'{gn}Report Other{lrd}'])
t.add_row([f'{lgn}6{lrd}',f'{gn}Report CopyRith{lrd}'])
t.add_row([f'{lgn}7{lrd}',f'{gn}Report Fake{lrd}'])
t.add_row([f'{lgn}8{lrd}',f'{gn}Report Geo Irrelevant{lrd}'])
t.add_row([f'{lgn}9{lrd}',f'{gn}Report Illegal Drugs{lrd}'])
t.add_row([f'{lgn}10{lrd}',f'{gn}Report Personal Details{lrd}'])
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
                                                                 
                    .---:                :---.                   
               .=++*+=+#+                +#*=+*++=.              
             =#*+++=++-=#                #==++=+++*#=            
           =%++**==**-*+#=   {rd}Reporter{k}   =#+*-**==**++%=          
         .#*+***=+**-*+##+.   {gn}Account{k}   .+*%+*-**+=***+*%:        
        -%=****-***=+*=%@+=            =+@%=*+=***-****=%-       
       -%=****-****-***++@#.          .#@++***-****-****=%-      
      .%=****=+***+=****-=%@=*:=#%=.*=@%=-****=+***+=****=%.     
      *+*****-****=*****-+=#%*%#@@#%*%#=+-*****=****-*****=#     
     .%=****=+****-*-..::%@@@+@@@@@@*@@@%-:..-*-****+=****=#.    
     ++*****-*+-:::.    @@@@@*%@@@@%*@@@@@    .:::-+*-*****++    
     *=***++-=         :@@@@@@##@@##@@@@@@:         =-++***=#    
     *=+:               %@@%#@@@##@@@##@@%               :+=#    
     +-            .... =@@@+@@@@@@@@+@@@= ....            -*    
     =          *@@@@@@@+@@@=@@@@@@@@=@@@+@@@@@@@*          =    
               :@@@@@@@@+@@%##%@@@@@###@@+@@@@@@@@:              
               .@@@@##%@+@@%*@@@@@@@@*%@@+@%##@@@@.              
                .*@@@@%#*+@@#%@@@@@@%#@@+*#%@@@@#:               
                  .=#@@@@*%@@-*+--+*-@@%*@@@@#=.                 
                      :=*@+@@:.    .-@@+@#=:                     
                          #*@=      =@*#                         
                         :%=@+      +@=%:                        
                       +****%*+=  =+*%****+                      
                        .-.=-        -=.-.                       


	{lrd}[{lgn}+{lrd}] {gn}Channel : {lgn}@Esfelurm	
			"""	 
class TelegramReporter:
    def __init__(self):
        self.api_id = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter Api id account: {g}")
        self.api_hash = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter Api hash account: {g}")
        self.phone_number = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter phone account:{g} ")
        self.password = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter password account: (If you don't have it, enter it) {g}")
        clear()
        re(account)
        print (f"{lrd}")
        print (t)
        self.method = input(f"{lrd}[{lgn}?{lrd}] {gn}Choose a method : {k}")
        self.scammer_id = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter Username of the target: {k}")
        self.number = input(f"{lrd}[{lgn}+{lrd}] {gn}Number of reports: {k}")

    def report_spam(self):
        with TelegramClient('reporter', self.api_id, self.api_hash) as client:
            client.start(self.phone_number, self.password)

            try:
                user = client.get_entity(self.scammer_id)
                scammer_input_peer = types.InputPeerUser(user_id=user.id, access_hash=user.access_hash)
            except ValueError:
                print(f'{lrd}[{rd}!{lrd}] {k}No such person was found')
                client.disconnect()
                return
            if self.method == "1":
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
                peer=scammer_input_peer,
                reason=types.InputReportReasonSpam(),
                message=''
            ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}A spam report has been sent : {i}")

            elif self.method == "2":
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
        peer=scammer_input_peer,
        reason=types.InputReportReasonPornography(),
        message=''
    ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}A Pornogaphy report has been sent : {i}")
                    
            elif self.method == "3":
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
        peer=scammer_input_peer,
        reason=types.InputReportReasonViolence(),
        message=''
    ))
                    print (f"\n{lrd}[{lgn}+{lrd}] {gn}A Violence report has been sent : {i}")                                        
            elif self.method == "4":
            	report_message = 'This user is suspected of child abuse'
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
        peer=scammer_input_peer,
        reason=types.InputReportReasonChildAbuse(),
        message=report_message
    ))
                    print (f"\n{lrd}[{lgn}+{lrd}] {gn}A Child Abuse report has been sent : {i}")                                        
            elif self.method == "5":
            	message = input(f"{lrd}[{lgn}?{lrd}] {gn}Enter the report message : {k}")
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
        peer=scammer_input_peer,
        reason=types.InputReportReasonOther(),
        message=message
    ))
                    print (f"\n{lrd}[{lgn}+{lrd}] {gn}A Other report has been sent : {i}")                                                
                    
            elif self.method == "6":
            	report_message = 'This user is suspected of Copyright'
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
        peer=scammer_input_peer,
        reason=types.InputReportReasonCopyright(),
        message=report_message
    )) 
                    print (f"\n{lrd}[{lgn}+{lrd}] {gn}A CopyRight report has been sent : {i}")           
            elif self.method == "7":
            	report_message = 'This user is suspected of fake'
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
        peer=scammer_input_peer,
        reason=types.InputReportReasonFake(),
        message=report_message
    ))
                    print (f"\n{lrd}[{lgn}+{lrd}] {gn}A Fake report has been sent : {i}")                                                                                                                                                                                                                                                                                                                                                                                                  
            elif self.method == "8":
            	report_message = 'This user is suspected of Geo Irrelevant'
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
        peer=scammer_input_peer,
        reason=types.InputReportReasonGeoIrrelevant(),
        message=report_message
    )) 
                    print (f"\n{lrd}[{lgn}+{lrd}] {gn}A Geo Irrelevant report has been sent : {i}")                                                                                                                                                                                                                                                                                                                                                                                       
            elif self.method == "9":
            	report_message = 'This user is suspected of Illegal Drugs'
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
        peer=scammer_input_peer,
        reason=types.InputReportReasonIllegalDrugs(),
        message=report_message
    ))                           
                    print (f"\n{lrd}[{lgn}+{lrd}] {gn}A Illegal Drugs report has been sent : {i}")                                      
            elif self.method == "10":
            	report_message = 'This user is suspected of Personal Details'
            	for i in range(0,int(self.number)):
                    client(functions.account.ReportPeerRequest(
        peer=scammer_input_peer,
        reason=types.InputReportReasonPersonalDetails(),
        message=report_message
    ))   
                    print (f"\n{lrd}[{lgn}+{lrd}] {gn}A Personal Details report has been sent : {i}")                                                                                                                        
            client.disconnect()

        print(f'\n\n{lrd}[{rd}-{lrd}] {k}Your reports are finished !')

reporter = TelegramReporter()
reporter.report_spam()
