# 3 請觀察以下程式碼後解釋兩種 import 的差異
path = ""

from os import path
import os

print(os.path.abspath("main.py"))
print(path.abspath("main.py"))
