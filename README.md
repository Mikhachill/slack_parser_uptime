

Установить драйвер для браузера Chrome если у вас  Linux:

Для получения ссылки перейдите в браузере на нужную вам версию драйвера по ссылке на https://sites.google.com/a/chromium.org/chromedriver/downloads. На открывшейся странице нажмите на файле для Linux правой кнопкой и скопируйте путь к файлу. Замените в примере ниже путь к файлу для команды wget вашей ссылкой:
wget https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
Проверьте, что chromedriver доступен, выполнив команду chromedriver в терминале, вы должны получить сообщение о том, что процесс успешно запущен:

Если вы получили сообщение "Command 'chromedriver' not found": 

То повторите установку драйвера по инструкциям выше. 


Установить драйвер для браузера Chrome если у вас  MacOS:
При установке Python вы уже, скорее всего, установили пакетный менеджер Homebrew. Если нет, то рекомендуем сделать это сейчас, а затем с его помощью установить программу wget для загрузки файлов по сети.
brew install wget
Для установки драйвера откройте сайт https://sites.google.com/a/chromium.org/chromedriver/downloads и скопируйте ссылку на ту версию ChromeDriver, которая соответствует версии вашего браузера. Чтобы узнать версию браузера, откройте новое окно в Chrome, в поисковой строке наберите: chrome://version/ — и нажмите Enter. В верхней строчке вы увидите информацию про версию браузера.
cd ~/Downloads
wget https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_mac64.zip
Разархивируйте скачанный файл и переместите его в папку /usr/local/bin, чтобы он был глобально доступен в вашей системе.
unzip chromedriver_mac64.zip
sudo mv chromedriver /usr/local/bin
Проверим, что нужная версия chromedriver установлена.
chromedriver --version
Мы должны увидеть ответ системы:
ChromeDriver 76.0.3809.68 (420c9498db8ce8fcd190a954d51297672c1515d5-refs/branch-heads/3809@{#864})

Создать виртуальное окружение:
!!! Перед этим зайти папку скачанного (полученного) теста !!!
Ввести в консоли:
Описание
$ python3 -m venv selenium_env
Создать виртуальное окружение
$ source selenium_env/bin/activate
Активировать виртуальное окружение


Подготовка окружения:
Установить зависимости из файла  requirements.txt:
Ввести в консоли: pip install -r requirements.txt

Запуск теста:
Ввести в консоли: pytest -s -v test_yandex_page.py


