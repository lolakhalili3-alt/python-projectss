
mo1 = input("math moadel:")
mo1 = float(mo1)

mo2 = input("moadel fiziks:")
mo2 = float(mo2)

mo3 = input("moadel farsi:")
mo3 = float(mo3)

mo4 = input("moadel ejtemaii:")
mo4 = float(mo4)

mo5 = input("moadel english:")
mo5 = float(mo5)

mo6 = input("moadel shimi:")
mo6 = float(mo6)

mo7 = input("moadel arabic:")
mo7 = float(mo7)

finalmo = (mo1 + mo2 + mo3 + mo4 + mo5 + mo6 + mo7)/ 7 
if finalmo > 18:
    print("your moadel",finalmo," so good")
elif finalmo > 15:
    print("ok",finalmo,"good")
elif finalmo > 10:
    print("realy",finalmo,"its ok")
else:
    print("your moadel",finalmo,"so so bad")
