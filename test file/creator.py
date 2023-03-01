import random

string1 = '###############################################################################\n'
  
file1 = open("test file/GPSR_Examples.txt", "r")
testFile = open("test file/testFile.py", "r")
code = open("code_test.py", "w")
  
index = 0
prevLine = ''

t = testFile.readlines()
x = file1.readlines()
xx = []

fullFile = False

for line in t[:192]:
    code.write(line)

code.write("\n\n")

for line in x:  
    
    if str(line) == string1 and str(prevLine) == '#\n':
        xx.append(x[index+2].replace('\n',''))
    
    prevLine = line
    index += 1 

if fullFile:
    for line in xx:
        code.write('\t\taction = nlp.classifier("'+line+'")\n'+'\t\tprint(action)\n'+'\t\t'+r'#assert action == "{}\n"'+'\n\n')
else:
    for i in range(50):
        r = random.randint(0,len(xx))
        code.write('\t\taction = nlp.classifier("'+xx[r]+'")\n'+'\t\tprint(action)\n'+'\t\t'+r'#assert action == "{}\n"'+'\n\n')

code.write("\n\n")

for line in t[192:]:
    code.write(line)

testFile.close()
file1.close() 
code.close()