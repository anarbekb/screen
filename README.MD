Screen
========================

**Doc**:

Work only in Ubuntu 14.04 Unity and depends on command notify-send <br>

Take screen: press Scroll Lock <br>
Exit script: press Pause <br>

doc YandexDisk:<br>
http://yadisk.readthedocs.io/ru/latest/intro.html#receiving-token-with-confirmation-code <br>

doc pyscreenhot:<br>
http://pyscreenshot.readthedocs.io/en/latest/<br>

**Requirements**:

sudo apt-get install xclip <br>
use python 3.5 <br>

**Install**:

git clone git@bitbucket.org:anarbekAB/screen.git <br>
cd project/name <br>
virtualenv -p python3 venv <br>
source venv/bin/activate <br>
pip install -r requirements.txt <br>
python src/main.py #for enter in the configs <br>
    * Go to link for authorizations in Yandex Disk <br>
    * Copy code in console <br>
    * Enter path to folder for save image(simple: /home/anarbek/Images/screen/) <br>
    * Enter path to folder for save image in Yandex Disk(simple: Image/screen/) <br>
        **The folder must exist on the Yandex Disk <br>
    * Press ctrl + c <br>
    
add run.sh to autoload in you OS <br>
