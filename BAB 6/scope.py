x = 10 #variabel GLOBAL

def fungsi_a():
    x = 99 #variabel LOKAL - berbeda dari x global!
    print("Di dalam fungsi_a, x =", x) # 99
    
def fungsi_b(): 
    print("Di dalam fungsi_b, x =", x) # 10 (pakai global)
    
fungsi_a()
fungsi_b()
print("Di luar fungsi, x =", x) # 10 (tidak berubah)