str1 = input("Input the filename:  ")
str2= str1[-3]
str3 = str1[-4]
str4 = str1[:-3: -1]
str5 = str1[:-4:-1]
str6=str4[: :-1]
str6=str6.lower()
str7=str5[: :-1]
str7=str7.lower()

if str2 == ".":
    if str6 == "py":

        print(" The extension of the file is : 'python'")
if str3 == ".":
    if str7 == "exe":
        print("The extension of the file is :'Executable'")
    if str7 == "jar":
        print("The extension of the file is :'Java Archive'")
    if str7 == "wsf":
        print("The extension of the file is :'Windows Script'")
    if str7 == "apk":
        print("The extension of the file is :'Android package'")
    if str7 == "bat":
        print("The extension of the file is :'Batch'")
    if str7 == "bin":
        print("The extension of the file is :'Binary'")
    if str7 == "cgi":
        print("The extension of the file is :'Common gateaway interface script'")
    if str7 == "com":
        print("The extension of the file is :'MS- DOS command'")
    if str7 == "txt":
        print("The extension of the file is :'Text'")
