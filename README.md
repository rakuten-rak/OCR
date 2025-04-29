A Litter Setup for the Optical Character Recognition
Make sure to check the installation for tesseract base on on your OS specification


#macos

brew install tesseract


#windows

check this documentation https://github.com/UB-Mannheim/tesseract/wiki

However some instance on windows you need to add the tesseract path to the current path of the project
you can do by setting it up by adding the varaiables below or create a sperate class and import it to the main.py

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
