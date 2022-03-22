import os
import random
os.system("rm -rf output")
os.system("mkdir output")


#Shuffle and Spilt
with open("data/train.scaled.txt", 'r') as f:
    lines = []
    for line in f:
        lines.append(line)
    random.shuffle(lines)
    for i in range(5):
        trainOut = open("output/train%d.txt"%(i+1),"w")
        valOut = open("output/val%d.txt"%(i+1),"w")
        for j in range(len(lines)):
            if j < 3133*i/10 or j >= 3133*(i+1)/10:
                trainOut.write(lines[j]) 
            if j >= 3133*i/10 and j < 3133*(i+1)/10:
                valOut.write(lines[j])             
        valOut.close()
        trainOut.close()
    f.close()
# Train models.
K = 10
for k in range(-K,K+1):
    for d in range(1,6):
        for s in range(1,6):
            print("d=%d,c=%f,s=%d"%(d,3 ** k,s))
            C = 3 ** k
            os.system("libsvm/svm-train -t 1 -d %d -c %f output/train%d.txt output/model.%d.%d.%d.txt > output/train.%d.%d.%d.log.txt"%(d,C,s,k,d,s,k,d,s))
            os.system("libsvm/svm-predict output/val%d.txt output/model.%d.%d.%d.txt output/dev.%d.%d.%d.prediction.txt > output/dev.%d.%d.%d.log.txt"%(s,k,d,s,k,d,s,k,d,s))


