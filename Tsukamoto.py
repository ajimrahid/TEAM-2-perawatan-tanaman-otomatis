
# proses fuzzyfikasi : intensitas cahaya, kelembapan, temperatur

x_cahaya = input ("masukan nilai cahaya = ")
x_kelembapan = input ("masukan nilai kelembapan = ")
x_temp = input ("masukan nilai temperatur (C) = ")

cahaya = int (x_cahaya)
kele = int (x_kelembapan)
temp = int (x_temp)


# menghitung intensitas cahaya
if cahaya <= 40 :
    value_sedikit = 1
    value_banyak = 0
if cahaya > 40 and cahaya < 80 :
     value_sedikit = (80 - cahaya)/(80 - 40)
     value_banyak = (cahaya - 40)/(80 - 40)
if cahaya >= 80 :
     value_sedikit = 0
     value_banyak= 1

#print ('intensitas cahaya')

#print ('sedikit cahaya', value_sedikit)
#print ('banyak cahaya', value_banyak)



# menghitung nilai kelembapan
if kele <=30 :
    value_kering = 1
    value_ideal = 0
    value_lembab = 0
if kele > 30 and kele < 45 :
    value_kering = (45 - kele)/(45 - 30)
    value_ideal = (kele - 30)/(45 - 30)
    value_lembab = 0
if kele == 45 :
    value_kering = 0
    value_ideal = 1
    value_lembab = 0
if kele > 45 and kele < 60 :
    value_kering = 0
    value_ideal = (60 - kele)/(60 - 45)
    value_lembab = (kele - 45)/(60 - 45)
if kele >= 60 :
    value_kering = 0
    value_ideal = 0
    value_lembab = 1



#print ('kelembapan')

#print ('kering', value_kering)
#print ('ideal', value_ideal)
#print ('lembab', value_lembab)

# menghitung nilai temperatur
if temp <=20 :
    value_dingin = 1 
    value_hangat = 0
    value_panas = 0 
if temp > 20 and temp < 24 :
    value_dingin = (24 - temp)/(24- 20) 
    value_hangat = (temp - 20)/(24 - 20)
    value_panas = 0
if temp ==24:
    value_dingin = 0 
    value_hangat = 1
    value_panas = 0
if temp > 24 and temp < 30 :
    value_dingin = 0
    value_hangat = (30 - temp)/(30 - 24)
    value_panas = (temp - 24)/(30 - 24)
if temp >= 30 :
    value_dingin = 0
    value_hangat = 0
    value_panas = 1

#print ('kondisi suhu')

#print ('dingin', value_dingin)
#print ('hangat', value_hangat)
#print ('panas', value_panas)

# proses inferensi 
speed=[]
def fungsiinferensiterbuka (variabel_cahaya, variabel_kele, variabel_temp) :
    if variabel_cahaya != 0:
        if variabel_kele != 0:
            if variabel_temp !=0:
                hasil_output = min (variabel_cahaya, variabel_kele, variabel_temp)
                speed.append([hasil_output, 90])

def fungsiinferensitertutup (variabel_cahaya, variabel_kele, variabel_temp) :
    if variabel_cahaya != 0:
        if variabel_kele != 0:
            if variabel_temp !=0:
                hasil_output = min (variabel_cahaya, variabel_kele, variabel_temp)
                speed.append([hasil_output, 10])

fungsiinferensitertutup(value_banyak, value_lembab, value_panas)
fungsiinferensitertutup(value_banyak, value_ideal, value_panas)
fungsiinferensitertutup(value_banyak, value_ideal, value_hangat)
fungsiinferensitertutup(value_banyak, value_kering, value_panas)
fungsiinferensitertutup(value_banyak, value_kering, value_hangat)
fungsiinferensitertutup(value_banyak, value_kering, value_dingin)
fungsiinferensitertutup(value_sedikit, value_kering, value_panas)
fungsiinferensitertutup(value_sedikit, value_kering, value_hangat)

fungsiinferensiterbuka(value_banyak, value_lembab, value_hangat)
fungsiinferensiterbuka(value_banyak, value_lembab, value_dingin)
fungsiinferensiterbuka(value_banyak, value_ideal, value_dingin)
fungsiinferensiterbuka(value_sedikit, value_lembab, value_panas)
fungsiinferensiterbuka(value_sedikit, value_lembab, value_hangat)
fungsiinferensiterbuka(value_sedikit, value_lembab, value_dingin)
fungsiinferensiterbuka(value_sedikit, value_ideal, value_panas)
fungsiinferensiterbuka(value_sedikit, value_ideal, value_hangat)
fungsiinferensiterbuka(value_sedikit, value_ideal, value_dingin)
fungsiinferensiterbuka(value_sedikit, value_kering, value_dingin)

# print ('maka speed adalah', speed)

# proses defuzzyfikasi

perkalian_new = 0
pembagian_new = 0

for j in range (0, len(speed)):
    perkalian = speed[j][0]*speed[j][1]
    pembagian = speed[j][0]
    perkalian_new = perkalian_new + perkalian
    pembagian_new = pembagian_new + pembagian

z = perkalian_new/pembagian_new

print ('persentasi bukaan atap (z) = ', z, '[%]')