import random

random.choice(["batu","gunting","kertas"])

def pilihan_komputer():
    return random.choice(["batu","gunting","kertas"])

def tentukan_pemenang(player,komputer):
    if player == komputer:
        return "seri"
    elif(player == "kertas" and komputer == "batu") or \
        (player == "batu" and komputer == "gunting") or \
        (player == "gunting" and komputer == "kertas"): return "anda menang"
    else : return "anda kalah" 
        
def main():
    player = input("masukkan pilihan anda (kertas/gunting/batu) =").lower()
    if player not in["batu","gunting","kertas"]:
        print("Pilihan tidak valid!")
        return
    
    komputer = pilihan_komputer()
    print(f"Komputer memilih: {komputer}")
    hasil = tentukan_pemenang(player, komputer)
    print(hasil)
    
if __name__ == "__main__":
    main()
    
