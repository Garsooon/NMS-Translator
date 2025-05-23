import PyInstaller.__main__
import shutil
import os

# Clean previous builds
if os.path.exists('dist'):
    shutil.rmtree('dist')
if os.path.exists('build'):
    shutil.rmtree('build')

PyInstaller.__main__.run([
    'src/translator/gui.py',
    '--name=NMS_Translator',
    '--onefile',
    '--windowed',
    '--add-data=src/translator/data/translations.txt;translator/data',
    #'--icon=assets/icon.ico'  # Optional: add an icon file
])