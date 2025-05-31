import random
def tao_so_ngau_nhien():
    return random.randint(1,20)  
def so_sanh(a,b):
    if a < b:
        return "Số bạn đoán quá thấp."
    elif a > b:
        return "Số bạn đoán quá cao."
    else:
        return "Chính xác!"
def danh_gia_nguoi_choi(so_lan):
    if so_lan <= 3:
        return "Rất giỏi!"
    elif so_lan <= 6:
        return "Giỏi!"
    elif so_lan <= 9:
        return "Khá!"
    else:
        return "Cần cải thiện!"