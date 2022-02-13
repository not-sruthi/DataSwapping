#Write a custom defined function in Python.
#Write code for swapping the data in the files.

#Create a swappingFile.py file.
#Create 2 sample text files and name them sample1.txt and sample2.txt
#Define a swapFileData function using def
#Use inputs to take the names of the files to swap.
#Open file1 and read it’s data and save it in a variable called data_a.
#Open file2 and read its data and save it in a variable called data_b.
#Open file 1 in writing mode and write data_b to it.
#Open file 2 in writing mode and write data_a to it.
#Call the function.
#Save the code.

file1= input("Enter the first file name. ")
file2= input("Enter the second file name. ")

def swapFileData(file1, file2):
    with open(file1, 'r') as data1:
        x = data1.read()

    with open(file2, 'r') as data2:
        y = data2.read()
        

    with open(file1,'w') as data1:
        data1.write(y)

    with open(file2,'w') as data2:
        data2.write(x)

swapFileData(file1, file2)
