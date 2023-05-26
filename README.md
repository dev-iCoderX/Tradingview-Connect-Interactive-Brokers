I. Set up Discord Bot

1. Go to: https://discord.com/developers/applications

2. Create new application

3. Go OAuth2 > URL Generator > Chose "bot" > BOT PERMISSIONS  > Chose Administrator > Copy URL > Select Sever and add BOT

4. Go to BOT > Reset Token > Copy > Save to: token.txt

5. Go to your channel you was add the bot and copy your channel id after that, save it to: channel.txt

EX: https://discord.com/channels/866711400260173855/1024222839852781588

Channel ID is 1024222839852781588

II. Set up connection

1. Install ISS in Server Manager

2. Download and install RequestRouter and Rewrite 

https://www.iis.net/downloads/microsoft/application-request-routing

https://www.iis.net/downloads/microsoft/url-rewrite

3. Install Python 3.9: https://www.python.org/downloads/release/python-390/

Remember choose "Add Python 3.9 to PATH"

4. Download source code: https://github.com/haluu0902/Tradingview-Connect-Interactive-Brokers.git
Unzip and go to C:\inetpub

5. Install requirements: pip install -r requirements.txt

6. Run API: python run.py

7. Public API: 127.0.0.1:8000

8. Install IB: https://www.interactivebrokers.com/en/trading/ibgateway-latest.php

9. Open connection IB and change:
    Port to 7497
    Disable read mode

10. Test:

{   
    "symbol": "EURUSD",
    "typeOrder": "MARKET",
    "side": "BUY",
    "entry": "1.0814",
    "amount": "0.1"
}