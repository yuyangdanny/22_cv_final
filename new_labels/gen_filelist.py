import glob

train_targetPattern = "./train/*/*.txt"
train_dataset = glob.glob(train_targetPattern)
test_targetPattern = "./test/*/*.txt"
test_dataset = glob.glob(test_targetPattern)
val_targetPattern = "./val/*/*.txt"
val_dataset = glob.glob(val_targetPattern)


f= open("train.txt","w+")
for i in range(len(train_dataset)):
    f.write(train_dataset[i] + "\n")
f.close()

f= open("test.txt","w+")
for i in range(len(test_dataset)):
    f.write(test_dataset[i] + "\n")
f.close()

f= open("val.txt","w+")
for i in range(len(val_dataset)):
    f.write(val_dataset[i] + "\n")
f.close()
