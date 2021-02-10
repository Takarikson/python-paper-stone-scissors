print("Zagrajmy w kamień, papier, nożyce :D")
user_1 = input('User1 :')
user_2 = input('User2 :')

if user_1=='papier':
    if user_2 =='kamien':
        print("wygrywa User1")
    else:
        print("wygrywa User2")

if user_1 =='kamien':
    if user_2 =='nozyce':
        print("wygrywa User1")
    else:
        print("wygrywa User2")

if user_1 =='nozyce':
    if user_2 =='papier':
        print("wygrywa User1")
    else:
        print("wygrywa User2")
        
if user_1 == user_2:
    print("remis")

