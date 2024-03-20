sayi1=int(input("Birinci sayıyı girin:"))
sayi2=int(input("ikinci sayıyı girin:"))
sayi3=int(input("Üçüncü sayıyı girin:"))

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
   enBuyukSayı = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
   enBuyukSayı = sayi2
else:
   enBuyukSayı = sayi3
 
print("En büyük sayı: ", enBuyukSayı)