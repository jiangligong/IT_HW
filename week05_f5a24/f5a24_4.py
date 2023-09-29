print("f5a24黎家暉")

import my_unit_change as muc

feet = float(input("請輸入你想從吋轉換成呎的長度："))
print(f"{feet}吋相當於：{muc.feet_to_inch(feet)}呎\n")

kg = float(input("請輸入你想從公斤轉換成公噸的大小："))
print(f"{kg}公斤相當於：{muc.kg_to_tonne(kg)}公噸")