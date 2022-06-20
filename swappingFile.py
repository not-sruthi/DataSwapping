file1= input("Enter the first file name. ")
file2= input("Enter the second file name. ")

def swapFileData(file1, file2):
    #reading file 1 and file 2 data

    with open(file1, 'r') as data1:
        x = data1.read()

    with open(file2, 'r') as data2:
        y = data2.read()
        
    #writing file 1 data in file 2, and writing file 2 data in file 1

    with open(file1,'w') as data1:
        data1.write(y)

    with open(file2,'w') as data2:
        data2.write(x)

swapFileData(file1, file2)
