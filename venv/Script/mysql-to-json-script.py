#!"C:\Users\adity\Desktop\python face\OpenCV-Face-Recognition-master\FacialRecognition\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'mysql-to-json==1.0.0','console_scripts','mysql-to-json'
__requires__ = 'mysql-to-json==1.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('mysql-to-json==1.0.0', 'console_scripts', 'mysql-to-json')()
    )
