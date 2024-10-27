import csv

#csv contains MorseCode, csv to dict
def getMorseTable():
    reader = csv.reader(open('morse.csv', 'r'))
    d = {}
    for row in reader:
        #print(row)
        k, v = row
        d[k] = v
    return d


#convert text to MorseCode
def morseCode(txt, tableMorse):
    converted_text=""
    morseCodeTable = tableMorse
    text_Upper = str(txt).upper()
    for alp in text_Upper:
        if alp==' ':
            converted_text+=' '
        else:
            converted_text += morseCodeTable[alp]
    print(converted_text)
    return converted_text

#check if text contains autorized AlhaNumeric caractere
def isValidTExt(entrd_txt, lstAlfNum):
    tbl = set(lstAlfNum)
    txt = str(entrd_txt).upper()
    for ltr in txt:
        if ((ltr in tbl)==False and ltr!=' '):
            return 0
    return 1


#build a dict of codeMorse and a list of accepted AlphaNUmeric caractere 
morsecodeTable = getMorseTable()
valideAlphNum = [k for k in morsecodeTable]




while True:

    print("Enter yout text to convert it into Morse Code : ")
    entrd_txt = input()
    check = isValidTExt(entrd_txt, valideAlphNum)
    print(check)
    if check:
        mrsCdTxt = morseCode(entrd_txt, morsecodeTable)
        print("\nThe converted text is:\n"+mrsCdTxt+'\n')
    else:
        print("Le message doit contenir des lettre de 'a' a 'z' "+
              "+/- des chiffre de '0' a '9' +/- les espaces") 