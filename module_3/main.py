import game as gm

def play():
    print("Welcome to the game!")
    so = gm.tao_so_ngau_nhien()
    so_lan_du_doan = 0
    gioi_han = 4
    for i in range(gioi_han):
        du_doan = int(input(f"Lượt {i+1} - Nhập dự đoán của bạn (1-20): "))
        so_lan_du_doan += 1
        ket_qua = gm.so_sanh(du_doan, so)
        print(ket_qua)
        if ket_qua == "Chính xác!":
            print(f"Bạn đã đoán đúng sau {so_lan_du_doan} lượt.")
            print(gm.danh_gia_nguoi_choi(so_lan_du_doan))
            break
    else:
        print(f"Bạn đã hết lượt! Số đúng là: {so}")
        print("Cần cải thiện!")

if __name__ == "__main__":
    play()