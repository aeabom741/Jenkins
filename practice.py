from time import ctime
import random

class leetcode:

    def odd_even():
        while True:
            n = int(input("Enter a number to identify odd or even:"))
            if n > 1000 or n < 0:
                print('error')
            elif n % 2 == 1:
                print("odd")
                break
            else:
                print("even")
                break

    # def spell_game():
    #     list = []
    #     while True:
    #         string = input("Enter a word[q to quit]:")
    #         if string == "q":
    #             break
    #         list.append(string)
        
    def count_string():
        while True:
            string = input("Enter your string:")
            list = []
            for i in string:
                list.append(i)
            print(len(list))
            break
    
    # def choose_name():
    #     print("Enter a number to srart list (0)End (1)Start list")
    #     number = int(input("Enter a number:"))
    #     if number == 0:
    #         print("List out")
    #     elif number == 1:
    #         while number != 0:
    #             print("(0)exit (1)Leo (2)Coco (3)Anny")
    #             number = int(input("Choose a name:"))
    #             if number == 0:
    #                 break
    #             elif number == 1:
    #                 print("""
    #                     Name:Leo,
    #                     Age:26,
    #                     Girlfriend:Coco,
    #                     Address:Suao Town,
    #                     Career:Software engineer
    #                   """)            
    #             elif number == 2:
    #                 print("""
    #                     Name:Coco,
    #                     Age:24,
    #                     Boyfriend:Leo,
    #                     Address:Beto Town,
    #                     Career:Bank 
    #                   """)
    #             elif number == 3:
    #                 print("""
    #                     Name:Anny,
    #                     Age:24
    #                     Boyfriend:None,
    #                     Address:Jinmei,
    #                     Career:Bank
    #                 """)
    #             else:
    #                 print("Error")
    #     else:
    #         print("Error")


    def choose_number():
        ansewer = random.randint(1,50)
        yourAns =  int(input("guess a number:"))
        count = 0

        if ansewer != yourAns:
            print("Answer is not correct")
            print("Press 0 to quit game")
            count += 1
            while yourAns != ansewer:
                yourAns =  int(input("answer is not correct guess a number:"))
                count += 1
                if yourAns == 0:
                    break
                elif yourAns == ansewer:
                    print("Correct")
                    print("your guess times:",count)
                elif yourAns > 50 or yourAns < 0:
                    print("Error")
                elif yourAns > ansewer:
                    print("To High")
                else:
                    print("To low")
        elif yourAns > 50 or yourAns < 0:
            print("Error")

        else:
            print("Correct")
            print("your guess times",count)

    def is_parme():
        n = int(input("Enter a number:"))
        if n > 2:
            for i in range(2,n):
                if n % i == 0:
                    print("不是質數")
                    break
                else:
                    print("質數")
                    break
        elif n == 2:
            print("質數")
        else:
            print("不是質數")

    def three_number_combine():
        for i in range(1,5):
            for j in range(1,5):
                for k in range(1,5):
                        if (i != j) and (j != k) and (k != i):
                            print(i,j,k)

leetcode.three_number_combine()