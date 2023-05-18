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