print("hello world")
print("helo world " * 3)

g = "selamat pagi semua"
h = "pagi"
j = len(h)

print(h in g) #untuk bertanya apakah variable h ada diadalam variable g
print(g.replace("pagi", "siang")) #untuk menggati suatu kata pada kalimat
print(g.upper()) #untuk membuat kalimat menjadi huruf besar semua
print(g.lower()) #untuk membuat kalimat menjadi huruf kecil semua
print(g.capitalize()) #untuk membuat kalimat pertama menjadi huruf besar
print(g.title()) #untuk membuat kalimat pertama  setiap awal sebuah kata menjadi huruf besar
print(j) #meghitung berapa jumlah huruf/veluae pada kalimat
print(len(g))
print(g[5]) #untuk memangil satu kata dalam sebuah kalimat
print(g[0:7])# untuk memanggil kata dari 0 sampai 7 pada kata di kalimat
print(g[7:9])
print(g[7:])

ges = f'{g} [{h}]'
print(ges)

# ge = input("nama mu siapa ")
# setnce = ge + " bismila expert python"
# print(setnce)

# umur = input("kamu lahir tahun berapa ")
# umur = int(umur)
# age = 2023 - umur
# print("umurku sekarang adalah ", age)




# ==========variable tempat untuk menampung value

a = 5
b = 10

print('variable a = ', a)
print('variable b = ', b)

a = b

print('variable a = ', a)

# ==============tipe data pada python
tipe_integer = 10

print(tipe_integer)
print(type(tipe_integer))

tipe_char = "python"

print(tipe_char)
print(type(tipe_char))

import math

tipe_float = 1.34
tipe_pemanggilan_math_ceil = math.ceil(tipe_float)
tipe_pemanggilan_math_floor = math.floor(tipe_float)

print(tipe_pemanggilan_math_ceil) # paksa untuk pembulatan atas
print(tipe_pemanggilan_math_floor) #paksa untuk pembulatan bawah
print(math.ceil(tipe_float))
print(round(tipe_float)) #untuk pembulatan 

print(tipe_float)
print(type(tipe_float))

tipe_boolean = True

print(tipe_boolean)
print(type(tipe_boolean))

# =============tipe data khusus

tipe_complex = complex(4,7)

print(tipe_complex)
print(type(tipe_complex))

# ================input data user

# data = int(input("input data = "))

# print(data)

#====================operasi aritmatika
'''kurung()
eksponen **
perkalian pembagian dll * / % //
pertambahan perkalian'''


x = 4
y = 3

# pertambahan
z = x + y
t = z + 2
t += 2
print(z)
print(t)
# pengurangan
z = x - y
print(z)

# perkalian
z = x * y
print(z)

# pembagian
z = x / y
print('hasil bagi main tadi sama temen = ', z)

# modulus / sisa bagi
z = x % y
print(z)

# eksponen / pangkat
z = x ** y
print(z)

# pembagian pembulatan / floor division
z = x // y
print(z)

# ================operasi komparasi (<, >, <=, >=, ==, !=, is, is not)

# <
q = 2
w = 4

e = q < w
print(e)

# >
e = q > w
print(e)

# ==
e = q == w
print(e)

# !=
e = q != w
print(e)

# is
e = q is w
print(e)

# is not
e = q is not w
print(e)

# print("GABUNGAN")
# InputData = float(input("Masukkan Data : "))

# Angka1 = (InputData >= 0 and InputData <= 5)
# print(Angka1)

# Angka2 = (InputData >= 8 and InputData <= 11)
# print(Angka2)

# Hasilnya = Angka1 or Angka2
# print("Answer :",Hasilnya)

# print("IRISAN")
# InputData = float(input("Masukkan Data : "))

# Angka1 = (InputData <= 0 or InputData >= 5)
# print(Angka1)

# Angka2 = (InputData <= 8 or InputData >= 11)
# print(Angka2)

# Hasilnya = Angka1 and Angka2
# print("Answer :",Hasilnya)


print("pengkodisian if else")

morning = False
afternon = True

if morning:
    print("good morning")
elif afternon :
    print("good afternoon")
else :
    print("have nice day")
    

"""false or true = true
true or false = true
true and true = true
true and false = false
false and true = true"""

name = "adi"
paksa = True

if len(name) > 3 or paksa:
    print("nama sesuai")
else :
    print("nama teralalu sedikit")
    
print("perulangannnnnnnnnnnnnn menggunakan while")

perulangan = 1

while perulangan <= 5 :
    print("*" * perulangan)
    perulangan += 1
    
print("finish")


#list
print("listtttttttttttttttttt")

item = [123, "galang", True]

print(item)
print(item[0:2])

for isi in item :
    print("isinya = ",isi) #untuk menampilakan isi yang apasa yang didalam item menggunakan perulangan
    
item.append("penambahan") #append digunakan untuk menbahakan item di dalam list
print(item)

item.insert(2, False) # insert ini juga untuk menbahakan item didalam list dengan memasukan bisa ditengah tengah
print(item)

item.pop(2) # pop untuk menghilakan item pada list dengan menggunakan index
print(item)

item.remove("galang") # remove untuk menghilakan item pada list langsung pada objeknya
print(item)

item2 = [2,1,4,3,7,6,5]
item2.sort()  #untuk mengurutkan item di list
print(item2)

init_item2 = 0

for number in item2 :
    init_item2 = init_item2 + number # untuk menjumlakan item dalam list secara manual
    # print(number)
    
print(init_item2)

total = sum(item2) #menjumlahkan otem dalam list menggunkan fungsi python
print(total)

print(item2[-1]) # untuk mengetahui jumlah item palaing besar

max_item2 = max(item2) # untuk mengetahui jumlah item palaing besar mnggunkan fungsi python
print(max_item2)

max2_item2 = item2[0]

for number2 in item2 :
    # print(number2)
    if number2 > max2_item2 :
        # print(number2)
        # print(max2_item2)
        max2_item2 = number2  
        
print(max2_item2)

# tuppple itu permanen tidak dapat diubah

item3 = (1,2,3)


#dictonary

user = {
    "name" : "galang adi yoga",
    "age" : 22,
    "is_admin" : True
}

user["name"] = "adiossss"
name = user["name"]
temp = user.get("username", "yogsss")
# name = user["user"]

print("")
print(name)
print(temp)

