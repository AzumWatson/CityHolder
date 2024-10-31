[![Bot Link](https://img.shields.io/badge/Telegram-Bot_Link-blue?style=for-the-badge&logo=Telegram&logoColor=white)](https://t.me/cityholder/game?startapp=1197825376)
[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CyberToolz)

# Бот для CityHolder

# 🔥🔥 Используйте Python 3.11.5 🔥🔥

> 🇪🇳 README in english available [here](README-EN)

## Features  
| Feature                                                   				                                    |     Supported    |
|---------------------------------------------------------------------------------------------------|:----------------:|
| Многопоточность                                            			                                    |        ✔️        |
| Авто-регистрация аккаунта по вашей реф. ссылке                                                 		 |        ✔️        |
| Авто тап                                                   				                                   |        ✔️        |
| Авто улечшение строений                                                 				                      |        ✔️        |
| Поддержка pyrogram .session                     						                                            |        ✔️        |

## [Настройки](https://github.com/Cybertat1on/CityHolder.git/blob/main/.env-example)
| Настройки 				   	     	                      |                                    				 Описание                                    |
|----------------------------------------------|:-----------------------------------------------------------------------------------:|
| **API_ID / API_HASH**                        | Данные платформы, с которой будет запущена сессия Telegram (по умолчанию - android) |       
| **REF_ID**                                   |                                      Реф. ID		                                      |
| **SLEEP_TIME**                               |           Диапазон времени сна между циклами (по умолчанию: [1900, 2000])           |
| **RANDOM_DELAY**                             |               Диапазон случайных задержек (по умолчанию: [0.5, 3.0])                |
| **RETRY_DELAY**                              |                     Задержка между попытками (по умолчанию: 5)                      |
| **CYCLE_WAIT_TIME**                          |              Время ожидания между циклами (по умолчанию: 10 в минутах)              |
| **CITY_BUTTON_CLICK_DELAY**                  |        Диапазон задержки после нажатия кнопки города (по умолчанию: [3, 5])         |
| **BUILD_BUTTON_CLICK_DELAY**                 |        Диапазон задержки после нажатия кнопки сборки (по умолчанию: [2, 4])         |
| **USE_PROXY_FROM_FILE**                      |   Использовать ли прокси из файла `bot/config/proxies.txt` (по умолчанию: False)    |

## Быстрый старт 📚

Для быстрой установки и последующего запуска - запустите файл `run.bat` на **Windows** или `run.sh` на **Линукс**

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [**Python**](https://www.python.org/downloads/release/python-3115/) **ВАЖНО**: Убедись что используешь **3.11.5**

## Получение API ключей
1. Перейдите на сайт [**my.telegram.org**](https://my.telegram.org/auth) и войдите в систему, используя свой номер телефона.
2. Выберите `API development tools` и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `.env`, предоставленные после регистрации вашего приложения.

## Установка
Вы можете скачать [**Репозиторий**](https://github.com/Cybertat1on/CityHolder) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
git clone https://github.com/Cybertat1on/CityHolder.git
cd Boinkers
```

Затем для автоматической установки введите:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux ручная установка
```shell
sudo sh install.sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Здесь вы обязательно должны указать ваши API_ID и API_HASH , остальное берется по умолчанию
python3 main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/CityHolder >>> python3 main.py --action (1/2)
# Or
~/CityHolder >>> python3 main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```


# Windows ручная установка
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Указываете ваши API_ID и API_HASH, остальное берется по умолчанию
python main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/CityHolder >>> python main.py --action (1/2)
# Или
~/CityHolder >>> python main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```

