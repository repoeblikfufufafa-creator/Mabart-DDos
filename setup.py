import os
c = input("Choose your environment: [0] pip / [1] pip3 : ")

if c == "0":
    os.system("pip install colorama")
    os.system("pip install click")
    os.system("pip install fake_headers")
elif c == "1":
    os.system("pip3 install colorama")
    os.system("pip3 install click")
    os.system("pip3 install fake_headers")
print("Done.")
