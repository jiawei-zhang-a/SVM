import os
os.system("rm -rf data")
os.system("mkdir data")

sex = {}
sex["M"] = "1:1 2:0 3:0";
sex["F"] = "1:0 2:1 3:0";
sex["I"] = "1:0 2:0 3:1";
fname = "abalone.data"
ftrain=open("data/train.txt","w")
ftest=open("data/test.txt","w")
cntLine = 0
with open(fname,'r+',encoding='utf-8') as f:
	for line in f.readlines():
            arr = line.split(',')
            if(int(arr[len(arr) - 1]) <= 9):
                label = "-1"
            else:
                label = "1"
            str = label + " %s"%sex[arr[0]]
            for i in range(1,8):
                str += " %d:%s"%(i+3,arr[i])
            
            cntLine += 1
            if cntLine <= 3133:
                ftrain.write(str+"\n")
            else:
                ftest.write(str+"\n")
ftrain.close()
ftest.close()
f.close()
os.system("libsvm/svm-scale -s data/scale.txt data/train.txt > data/train.scaled.txt")
os.system("libsvm/svm-scale -r data/scale.txt data/test.txt > data/test.scaled.txt")