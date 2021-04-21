file_to_write = open("/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/Merged "
                     "Results/Merged FUN/Merged FUN Total", "a")
for i in range(150, 200):
    file1 = open("/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/Merged "
                 "Results/Setting 4/FUN/FUN.NSGAII.Doctor Allocation Trial "+str(i), "r")
    while True:
        line = file1.readline()
        if not line:
            break
        #line = line.strip("\n")
        file_to_write.write(line)
    file1.close()
file_to_write.close()
