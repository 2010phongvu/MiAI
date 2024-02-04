import vatLy
import toanHoc

print("Xin moi lua chon:")
print("1: Toán")
print("2: Vat Ly")

chon = int(input("Nhap vao lua chon = "))

if chon==2:
    s = float(input("Nhap vao s = "))
    t = float(input("Nhap vao t = "))
    van_toc = vatLy.toc_do(s,t)
    print("Van toc = ", van_toc)
else:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    tam_giac_vuong = toanHoc.tam_giac_vuong(a, b, c)
    if tam_giac_vuong == True:
        print("Tam giac vuong")
    else:
        print("Tam giac khong vuong")