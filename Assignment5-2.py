import sys
try:
    input_file = open(sys.argv[1],'r+')
except:
    input_file = open(sys.argv[1],'a+')
output_file = open("output.txt", 'w+')
read = input_file.readline()
input_list = []
input_list3 = []
input_list4 = []
command_list = []
liste = ["Price","Name","Genre","Director"]
while read != "":
    output_file.write(read)
    input_list.append(read.split(","))
    read = input_file.readline()
output_list = input_list
print("Serial\tPrice\tName\t\tGenre\tDirector\t\tState")
print("-----  ------- ----------- --------\t-----------\t\t----")
for sayi in range(len(input_list)):
    print(input_list[sayi][0] + "\t\t" + input_list[sayi][1] + "\t\t" + input_list[sayi][2] + "\t" + input_list[sayi][3]
          + "\t" + input_list[sayi][4] + "\t" + input_list[sayi][5])
print("\n----HUBM DVD----")
print("A:\tAdd new dvd")
print("R:\tRemove dvd")
print("S\tSearch dvd")
print("L:\tList  dvd")
print("E:\tEdit  dvd")
print("H\tHire  dvd")
print("Q:\tQuit")
command = ""
string = ""
string2 = ""
string3 = ""
string4 = ""
string5 = ""
string6 = ""
spy = 0
a = ""
listee = []
listee2 = []
listee3 = []
listee4 = []
inv = "Inv;\n"
inv2 = "Inv;"
hired = "Hired;\n"
hired2 = "Hired;"
while command != "Q":
    command = input("Enter Command:")
    if command != "Q":
        command_list.append(command.split(","))
        if command_list[0][0] == 'A':
            for sayi in range(len(input_list)):
                if command_list[0][1] == input_list[sayi][0]:
                    print("Warning! This serial number is already exist.")
                    command_list.clear()
                    spy = 1
                    break
            if spy != 1:
                for isim in liste:
                    isimler = input("{}:".format(isim))
                    command_list.append(isimler)
                string = command_list[0][1]
                string2 = ",".join(command_list[1:len(command_list)])
                string3 = string + "," + string2
                output_file.close()
                output_file = open("output.txt", 'a+')
                output_file.write("\n"+ string3 + "," + inv2)
                string6 ="\n" + string3 + "," + inv2
                output_list.append(string6.split(","))
                string = ""
                string2 = ""
                string3 = ""
                command_list.clear()
            spy = 0
        elif command_list[0][0] == 'R':
            for sayi in range(len(input_list)):
                if command_list[0][1] == input_list[sayi][0]:
                    print("Serial\tPrice\tName\t\tGenre\tDirector\t\tState")
                    print("-----  ------- ----------- --------\t-----------\t\t----")
                    print(input_list[sayi][0]+"\t\t"+input_list[sayi][1]+"\t\t"+input_list[sayi][2]+"\t"+input_list[sayi][3]+"\t"+input_list[sayi][4]+"\t"+input_list[sayi][5])
                    if input_list[sayi][5] == "Hired;\n":
                        print("You can't remove this dvd because of in hired inventory.")
                        command_list.clear()
                        break
                    else:
                        yes_or_no = input("Do you want to remove this DVD ? (Y/N) :")
                        if yes_or_no == 'Y':
                            input_list2 = output_list
                            input_list2.remove(input_list[sayi])
                            output_file.close()
                            output_file = open("output.txt", 'w+')
                            for harf in input_list2:
                                string4 = ",".join(harf)
                                output_file.write(string4)
                            string4 = ""
                            print("This dvd has been removed.")
                            break
                        else:
                            command_list.clear()
                            break
            command_list.clear()
        elif command_list[0][0] == 'S':
            kelime = command_list[0][1]
            for sayi in range(len(input_list)):
                if input_list[sayi][2].find(kelime) == -1:
                    command_list.clear()
                else:
                    print("Serial\tPrice\tName\t\tGenre\tDirector\t\tState")
                    print("-----  ------- ----------- --------\t-----------\t\t----")
                    print(input_list[sayi][0] + "\t\t" + input_list[sayi][1] + "\t\t" + input_list[sayi][2] + "\t" +input_list[sayi][3] + "\t" + input_list[sayi][4] + "\t" + input_list[sayi][5])
                    command_list.clear()
                    a = "a"
                    break
            if a == "":
                print("Not Found!!")
            a = ""
        elif command_list[0][0] == 'E':
            if len(command_list[0]) == 3:
                listee.append(command_list[0][2].split("="))
                for sayi in range(len(input_list)):
                    if command_list[0][1] == input_list[sayi][0]:
                        if listee[0][0] == 'Name':
                            input_list3 = output_list
                            input_list3[sayi][2] = listee[0][1]
                            break
                        elif listee[0][0] == 'Price':
                            input_list3 = output_list
                            input_list3[sayi][1] = listee[0][1]
                            break
                        elif listee[0][0] == 'Genre':
                            input_list3 = output_list
                            input_list3[sayi][3] = listee[0][1]
                            break
                        elif listee[0][0] == 'Director':
                            input_list3 = output_list
                            input_list3[sayi][4] = listee[0][1]
                            break
            elif len(command_list[0]) == 4:
                listee.append(command_list[0][2].split("="))
                listee2.append(command_list[0][3].split("="))
                listee3.append(command_list[0][4].split("="))
                for sayi in range(len(input_list)):
                    if command_list[0][1] == input_list[sayi][0]:
                        input_list3 = output_list
                        if listee[0][0] == 'Name':
                            input_list3[sayi][2] = listee[0][1]
                        elif listee[0][0] == 'Price':
                            input_list3[sayi][1] = listee[0][1]
                        elif listee[0][0] == 'Genre':
                            input_list3[sayi][3] = listee[0][1]
                        elif listee[0][0] == 'Director':
                            input_list3[sayi][4] = listee[0][1]
                        if listee2[0][0] == 'Name':
                            input_list3[sayi][2] = listee2[0][1]
                        elif listee2[0][0] == 'Price':
                            input_list3[sayi][1] = listee2[0][1]
                        elif listee2[0][0] == 'Genre':
                            input_list3[sayi][3] = listee2[0][1]
                        elif listee2[0][0] == 'Director':
                            input_list3[sayi][4] = listee2[0][1]
                        break
            elif len(command_list[0]) == 5:
                listee.append(command_list[0][2].split("="))
                listee2.append(command_list[0][3].split("="))
                listee3.append(command_list[0][4].split("="))
                for sayi in range(len(input_list)):
                    if command_list[0][1] == input_list[sayi][0]:
                        input_list3 = output_list
                        if listee[0][0] == 'Name':
                            input_list3[sayi][2] = listee[0][1]
                        elif listee[0][0] == 'Price':
                            input_list3[sayi][1] = listee[0][1]
                        elif listee[0][0] == 'Genre':
                            input_list3[sayi][3] = listee[0][1]
                        elif listee[0][0] == 'Director':
                            input_list3[sayi][4] = listee[0][1]
                        if listee2[0][0] == 'Name':
                            input_list3[sayi][2] = listee2[0][1]
                        elif listee2[0][0] == 'Price':
                            input_list3[sayi][1] = listee2[0][1]
                        elif listee2[0][0] == 'Genre':
                            input_list3[sayi][3] = listee2[0][1]
                        elif listee2[0][0] == 'Director':
                            input_list3[sayi][4] = listee2[0][1]
                        if listee3[0][0] == 'Name':
                            input_list3[sayi][2] = listee3[0][1]
                        elif listee3[0][0] == 'Price':
                            input_list3[sayi][1] = listee3[0][1]
                        elif listee3[0][0] == 'Genre':
                            input_list3[sayi][3] = listee3[0][1]
                        elif listee3[0][0] == 'Director':
                            input_list3[sayi][4] = listee3[0][1]
                        break
            elif len(command_list[0]) == 6:
                listee.append(command_list[0][2].split("="))
                listee2.append(command_list[0][3].split("="))
                listee3.append(command_list[0][4].split("="))
                listee4.append(command_list[0][5].split("="))
                for sayi in range(len(input_list)):
                    if command_list[0][1] == input_list[sayi][0]:
                        input_list3 = output_list
                        if listee[0][0] == 'Name':
                            input_list3[sayi][2] = listee[0][1]
                        elif listee[0][0] == 'Price':
                            input_list3[sayi][1] = listee[0][1]
                        elif listee[0][0] == 'Genre':
                            input_list3[sayi][3] = listee[0][1]
                        elif listee[0][0] == 'Director':
                            input_list3[sayi][4] = listee[0][1]
                        if listee2[0][0] == 'Name':
                            input_list3[sayi][2] = listee2[0][1]
                        elif listee2[0][0] == 'Price':
                            input_list3[sayi][1] = listee2[0][1]
                        elif listee2[0][0] == 'Genre':
                            input_list3[sayi][3] = listee2[0][1]
                        elif listee2[0][0] == 'Director':
                            input_list3[sayi][4] = listee2[0][1]
                        if listee3[0][0] == 'Name':
                            input_list3[sayi][2] = listee3[0][1]
                        elif listee3[0][0] == 'Price':
                            input_list3[sayi][1] = listee3[0][1]
                        elif listee3[0][0] == 'Genre':
                            input_list3[sayi][3] = listee3[0][1]
                        elif listee3[0][0] == 'Director':
                            input_list3[sayi][4] = listee3[0][1]
                        if listee4[0][0] == 'Name':
                            input_list3[sayi][2] = listee4[0][1]
                        elif listee4[0][0] == 'Price':
                            input_list3[sayi][1] = listee4[0][1]
                        elif listee4[0][0] == 'Genre':
                            input_list3[sayi][3] = listee4[0][1]
                        elif listee4[0][0] == 'Director':
                            input_list3[sayi][4] = listee4[0][1]
                        break
            listee = []
            listee2 = []
            listee3 = []
            listee4 = []
            output_file.close()
            output_file = open("output.txt", 'w+')
            for harf in input_list3:
                string4 = ",".join(harf)
                output_file.write(string4)
            string4 = ""
            command_list.clear()
        elif command_list[0][0] == 'H':
            for sayi in range(len(input_list)):
                if command_list[0][1] == input_list[sayi][0]:
                    print("Serial\tPrice\tName\t\tGenre\tDirector\t\tState")
                    print("-----  ------- ----------- --------\t-----------\t\t----")
                    print(input_list[sayi][0] + "\t\t" + input_list[sayi][1] + "\t\t" + input_list[sayi][2] + "\t" +
                          input_list[sayi][3] + "\t" + input_list[sayi][4] + "\t" + input_list[sayi][5])
                    input_list4 = output_list
                    input_list4[sayi][5]=input_list4[sayi][5].replace(inv,hired)
                    input_list4[sayi][5] = input_list4[sayi][5].replace(inv2, hired2)
            output_file.close()
            output_file = open("output.txt", 'w+')
            for harf in input_list4:
                string4 = ",".join(harf)
                output_file.write(string4)
            string4 = ""
            command_list.clear()
        elif command_list[0][0] == 'L':
            print("Serial\tPrice\tName\t\tGenre\tDirector\t\tState")
            print("-----  ------- ----------- --------\t-----------\t\t----")
            for sayi in range(len(output_list)):
                print(output_list[sayi][0] + "\t\t" + output_list[sayi][1] + "\t\t" + output_list[sayi][2] + "\t" +
                      output_list[sayi][3] + "\t" + output_list[sayi][4] + "\t" + output_list[sayi][5])
    command_list.clear()
input_file.close()
input_file = open(sys.argv[1],'w+')
for harf in output_list:
    string4 = ",".join(harf)
    input_file.write(string4)
string4 = ""
input_file.close()
output_file.close()