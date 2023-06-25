
import random 

lower = "abcdefghijklmnopgrstuvwxyz" 
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
number = "0123456789" 
symbols = "[]{}()*;/,.-2"


all_combinations = lower + upper + number + symbols 
length = 12 
password = "".join(random.sample(all_combinations, length)) 

print(password) 
