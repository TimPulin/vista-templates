import os
import webbrowser
from time import sleep
import platform
import subprocess


def get_template():
    with open('/home/user/CODE/templates/test3.html', 'r') as f:
        content = f.read()
    return content


def open_in_browser(file_path):
    # to absolute path
    abs_path = os.path.abspath(file_path)
    try:
        if platform.system() == 'Windows':
            os.startfile(abs_path)
        else:  # Linux
            cmd = 'xdg-open "{}"'.format(abs_path)
            os.system(cmd)
            # subprocess.call(['xdg-open', abs_path])
    except Exception as e:
        print(e)

    # add file:// and shield whitespace
    url = 'file://' + abs_path.replace(' ', '%20')

    chrome = webbrowser.get('/usr/bin/google-chrome-stable %s')
    print(chrome)
    # chrome.open(url)
    # webbrowser.open(url)
    sleep(2)


def generate_template(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # create HTML-file
    template = get_template()
    with open(file_path, "w") as f:
        f.write(template)

    return


FILE_PATH = "/home/user/CODE/templates/index.html"
try:
    generate_template(FILE_PATH)
    open_in_browser(FILE_PATH)
except Exception as e:
    print(e)
