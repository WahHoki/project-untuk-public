import random
# membuat project tebak tebakan angka
print('=============================')
print("Selamat datang di tebak angka")
print('=============================')

angka = random.randint(1,6)

username = input(str("masukkan nama anda :"))

print(f"hai {username}, coba pilih salah satu gua ini")
print("|1| |2| |3| |4| |5| |6|")
bermain = int(input("coba tebak di gua mana capybara berada? 1/2/3/4/5/6 = "))

if bermain == angka:
    print(f"selamat {username} menang, capybara berada di gua nomor {angka}")
else:
    print(f"maaf {username} coba lagi, capybara berada di gua nomor {angka}")


                
