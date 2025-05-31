# s = input('Nhap 3 so:')
# a = s.split()
# print(a)
# # Bước 3 sử dụng map để ép các phần từ trong list sang kiểu dữ liệu mong muốn

# x,y,z=map(int,a)
# print(x+y+z)

# x ,y, z, t = map(int, input('Nhap 4 so: ').split())
# print('tong 4 so la : ',x+y+z+t)
#yeu cau nguoi dung nhap so duong, nhap so am hoac so 0 thi bat nhap lai
# while True:
#     n=int(input('Nhap so duong: '))
#     if n>0: break
#     print('Nhap lai so duong')
# print(n)
# n//=10(n chia nguyên cho 10 )
# Bảng cửu chương
n,m=9,9
for i in range(1,n+1):
    for j in range(1,m+1):
        print(f"{i} x {j} = {i*j}")
    #     j+=1
    # i+=1
