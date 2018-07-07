import time

start = time.time()

aaa = 100
aaa = aaa + 1
print(aaa)

str_temp = "hashimoto\n,aaa\tbbb"
print (str_temp)

str_temp2 = """hashimoto
					sfsfadfsa"""
print (str_temp2)


str_temp2 = """hashimoto ' , ",,,,"""
print (str_temp2)


print("/* Method to bury data in character string */")
myscore = 1000
message = ' I scored %s points'
print(message % myscore)

print("/* Multiplication of the character string */")
print ('a'*10)

elapsed_per = (time.time()-start)
print (elapsed_per)