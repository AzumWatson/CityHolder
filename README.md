[![Bot Link](https://img.shields.io/badge/Telegram-Bot_Link-blue?style=for-the-badge&logo=Telegram&logoColor=white)](https://t.me/cityholder/game?startapp=1197825376)
[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CyberToolz)

#  Bot for CityHolder
![start-cityholder](https://github.com/user-attachments/assets/a3e7314b-9afd-4566-a7f3-0dab746c0d44)

# 🔥🔥 PYTHON version must be 3.11.5 🔥🔥

> 🇷 🇺 README in russian available [here](README-RU.md)

## Features  
| Feature                                                   				              |     Supported    |
|-----------------------------------------------------------------------------|:----------------:|
| Multithreading                                            			               |        ✔️        |
| Auto Referral                                                  		           |        ✔️        |
| Auto Tap                                                   				             |        ✔️        |
| Auto Building upgrades                                                 				 |        ✔️        |
| Support for pyrogram .session                     						                    |        ✔️        |

## [Settings](https://github.com/Cybertat1on/CityHolder.git/blob/main/.env-example)
| Settings 				   	     	                      |                           							 Description                            |
|----------------------------------------------|:------------------------------------------------------------------------:|
| **API_ID / API_HASH**                        | Platform data from which to run the Telegram session (default - android) |       
| **REF_ID**                                   |                            Put your ref ID			                            |
| **SLEEP_TIME**                               |         Sleep time range between cycles (default: [1900, 2000])          |
| **RANDOM_DELAY**                             |                 Random delay range (default: [0.5, 3.0])                 |
| **RETRY_DELAY**                              |                   Delay between attempts (default: 5)                    |
| **CYCLE_WAIT_TIME**                          |            Wait time between cycles (default: 10 in minutes)             |
| **CITY_BUTTON_CLICK_DELAY**                  |       Delay range after clicking the city button (default: [3, 5])       |
| **BUILD_BUTTON_CLICK_DELAY**                 |      Delay range after clicking the build button (default: [2, 4])       |
| **USE_PROXY_FROM_FILE**                      |                   Use proxy from file (default: False)                   |

## Quick Start

To install libraries and run bot - open run.bat on Windows

## Prerequisites
Before you begin, make sure you have the following installed:
- [**Python**](https://www.python.org/downloads/release/python-3115/) **IMPORTANT**: Make sure to use **3.11.5**. 

## Obtaining API Keys
1. Go to [**my.telegram.org**](https://my.telegram.org/auth) and log in using your phone number.
2. Select `API development tools` and fill out the form to register a new application.
3. Record the `API_ID` and `API_HASH` provided after registering your application in the `.env` file.

## Installation
You can download the [**repository**](https://github.com/Cybertat1on/CityHolder) by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/Cybertat1on/CityHolder.git
cd CityHolder
```

Then you can do automatic installation by typing:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/CityHolder >>> python3 main.py --action (1/2)
# Or
~/CityHolder >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```
You can also use arguments for quick start, for example:
```shell
~/CityHolder >>> python3 main.py --action (1/2)
# Or
~/CityHolder >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```


