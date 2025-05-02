print("模組正在被匯入...")

def say_hi(name):
    print(f"Hi，{name}！")

def say_hello(name):
    print(f"Hello，{name}！")

def how_are_you(name):
    print(f"How are you，{name}？")


print("模組的頂層程式碼執行完畢。")

if __name__ == "__main__":
    say_hello("預設使用者")
    how_are_you("預設使用者")
else:
    print("這個模組被其他程式 or 模組匯入")
