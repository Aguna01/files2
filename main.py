f = open( '1.txt' )
f2 = open('2.txt' )
f3 = open('3.txt' )
    count_1= 0
    text_1=[]
    for line in f:
            count_1+= 1
            text_1.append(f'строка номер {count_1} файла номер 1')
    count_2= 0
    text_2= []
    for line in f2:
            count_2+= 1
            text_2.append(f'строка номер {count_2} файла номер 2')
        a= count_1 > count_2
        if a == True:
            f.write(f"1.txt\n{count_1}\n")
            for a in text_1:
                f.write(f'{a}\n')
            f2.write(f"2.txt\n{count_2}\n")
            for b in text_2:
                f2.write(f'{b}\n')
        else:
            f2.write(f"2.txt\n{count_2}\n")
            for b in text_2:
                f2.write(f'{b}\n')
            f.write(f"1.txt\n{count_1}\n")
            for a in text_1:
                f.write(f'{a}\n')



