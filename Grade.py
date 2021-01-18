scoreInput = int(input("คะแนนของคุณ : "))
if scoreInput < 0:
    print("เกิดข้อผิดพลาด!!!")
elif scoreInput < 50:
    print("คุณติด 0")
elif 50 <= scoreInput < 55:
    print("คุณได้เกรด 1")
elif 55 <= scoreInput < 60:
    print("คุณได้เกรด 1.5")
elif 60 <= scoreInput < 65:
    print("คุณได้เกรด 2")
elif 65 <= scoreInput < 70:
    print("คุณได้เกรด 2.5")
elif 70 <= scoreInput < 75:
    print("คุณได้เกรด 3")
elif 75 <= scoreInput < 80:
    print("คุณได้เกรด 3.5")
elif 80 <= scoreInput <= 100:
    print("คุณได้เกรด 4")
else:
    print("เกิดข้อผิดพลาด!!!")


