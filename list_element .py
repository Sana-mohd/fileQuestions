"""Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki file mein nayi line mein daalo.
 Aapki list yeh rahi:"""
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 

f=open("saral2.txt","a+")
for i in banks_list:
    print(i)
    f.write(i+"\n")
f.close()
