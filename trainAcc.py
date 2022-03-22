import os
os.system("rm -rf train")
os.system("mkdir train")
K = 10
for k in range(-K,K+1):
    for d in range(1,6):  
        for s in range(1,6):          
            os.system("libsvm/svm-predict data/train.scaled.txt output/model.%d.%d.%d.txt output/dev.%d.%d.%d.prediction.txt > train/dev.%d.%d.%d.log.txt"%(k,d,s,k,d,s,k,d,s))

