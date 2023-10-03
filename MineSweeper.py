import random
import os
import time
import math


def Have_Profile():
    f = open("history.txt", "r")

    if len(f.readlines()) == 0:
        return False
    return True
# check have account


def nums(num):
    if num == 0:
        return zerohome

    elif num == 1:
        return "1️⃣ "

    elif num == 2:
        return "2️⃣ "

    elif num == 3:
        return "3️⃣ "

    elif num == 4:
        return "4️⃣ "

    elif num == 5:
        return "5️⃣ "

    elif num == 6:
        return "6️⃣ "

    elif num == 7:
        return "7️⃣ "

    elif num == 8:
        return "8️⃣ "
# number emojis


def Creat_Playground():

    l = []
    x = 1

    while True:

        l.append([home] * width)
        x += width

        if len(l) == height:
            return l


def bombing():

    column = [0] * width
    bomb = set()

    while True:
        r1 = random.randint(0, height-1)
        r2 = random.randint(0, width-1)

        if column[r2] < 3:
            bomb.add((r1, r2))
            column[r2] += 1

        if len(set(bomb)) == bumb_number:
            return bomb
# put the bombs in random house


def house_bombs(x, y):

    counter = 0

    for m in range(-1, 2):
        for n in range(-1, 2):
            if (x+m, y+n) in bombs:
                counter += 1

    return counter
# number of each house


def calculater(input):

    x = (input - 1) // width
    y = (input - 1) % width

    return (x, y)
# convert number to (x,y)


def clearing(x, y):

    for u in range(-1, 2, 2):
        if y+u == width or y+u < 0:
            continue

        if house_bombs(x, y+u) == 0:
            if Playground[x][y+u] == home:
                zero_home.append((x, y+u))
                Playground[x][y+u] = zerohome
            selected.add((x, y+u))

        else:
            if Playground[x][y+u] != "🚩":
                Playground[x][y+u] = nums(house_bombs(x, y+u))
            selected.add((x, y+u))
            continue

    for u in range(-1, 2, 2):
        if x+u == height or x+u < 0:
            continue

        if house_bombs(x+u, y) == 0:
            if Playground[x+u][y] == home:
                zero_home.append((x+u, y))
                Playground[x+u][y] = zerohome
            selected.add((x, y+u))

        else:
            if Playground[x+u][y] != "🚩":
                Playground[x+u][y] = nums(house_bombs(x+u, y))
            selected.add((x+u, y))
            continue
# Open the house next door zero house


def flaging(x, y):

    if Playground[x][y] == "🚩":
        Playground[x][y] = home

    else:
        Playground[x][y] = "🚩"
# put the flags in house


def valid_input(input):

    for x in input[0]:
        if ord(x) < 48 or ord(x) > 58:
            return False

    if int(input[0]) > (width * height) or int(input[0]) < 1:
        return False

    if len(input) > 1:
        if input[1].lower() != "f" and input[1].lower() != "flag":
            return False

    return True


def Password_Security(passw):

    if len(passw) < 7:
        return False

    low = passw.lower()
    up = passw.upper()

    if low == passw or up == passw:
        return False

    return True


def edit_file(line, new):
    f = open("history.txt", "r")
    information = f.readlines()
    before = ((information[line].replace("\n", "")).split(" : "))[1]
    information[line] = information[line].replace(before, str(new))
    f = open("history.txt", "w")
    f.write("".join(information))
    f.close()


def best_socer(t, s):
    f = open("history.txt", "r")
    information = f.readlines()
    socres = []
    if s == 10:
        for x in information[8:13]:
            socres.append(int(x.replace("\n", "")))
            y = 8

    if s == 20:
        for x in information[14:19]:
            socres.append(int(x.replace("\n", "")))
            y = 14

    if s == 40:
        for x in information[20:25]:
            socres.append(int(x.replace("\n", "")))
            y = 20

    socres.append(t)
    socres.sort(reverse=True)
    socres.pop()

    for x in range(y, y+5):
        information[x] = (str(socres[x-y]) + "\n")

    fw = open("history.txt", "w")
    fw.write("".join(information))


home = "⬜️"
zerohome = "🔘"
print("🎉 Hello,\n Welcome to this game🤍\n")
width, height, bumb_number = 9, 9, 10

if not (os.path.exists("history.txt")):
    f = open("history.txt", "x")

f = open("history.txt", "r")
information = f.readlines()

while True:

    if Have_Profile():
        if ((information[6].replace("\n", "")).split(" : "))[1] == "yes":
            break

    print("♨️  Please select the desired option :\n")
    print("📥 sign up : (1 or s)")
    print("▶️  log in : (2 or l)")
    print("⚠️  forget password : (3 or f)")
    print("❌ exit : (4 or e)\n")

    choice = input()
    os.system('cls')

    if choice == "1" or choice == "s":

        if not (Have_Profile()):

            username = input("🎁 Pleae enter your username :\n")
            password = input("\n📘 Pleae enter your password :\n")

            while not (Password_Security(password)):
                os.system('cls')
                print("🔓 Poor password")
                password = input("📘 Pleae enter safer password :\n")

            Repeat_password = input("\n📘 Pleae enter Repeat password :\n")

            while password != Repeat_password:
                print("\n🔐 The password and its repetition do not match❌")
                Repeat_password = input(
                    "↘️  Pleae enter true Repeat password password :\n")

            print("\n🎈Security Questions :")
            Security_question_one = input(
                "🎨 What is your Favourite Colour :\n")
            Security_question_two = input(
                "\n🔮 What is your year of birth? :\n")

            fa = open("history.txt", "a")
            fa.write("Username : " + username)
            fa.write("\nPassword : " + password)
            fa.write("\nFavourite Colour : " + Security_question_one)
            fa.write("\nyear of birth : " + Security_question_two)
            fa.write("\nwin game : " + "0")
            fa.write("\nlose game : " + "0")
            fa.write("\nLogin without password : " + "no")
            fa.write("\nsmall : " + 5 * "\n0")
            fa.write("\nmedium : " + 5 * "\n0")
            fa.write("\nlarge : " + 5 * "\n0" + "\n\n")
            fa.close()
            os.system('cls')
            print("Your account has been created ✅\nEnjoy playing this game ❤️  :)")
            break

        else:
            os.system('cls')
            print("You have an account✅\n")
            continue
    elif choice == "2" or choice == "l":

        if Have_Profile():
            user = input("📝 Pleae enter your username :\n")
            pasword = input("\n🔐 Pleae enter your password :\n")

            os.system('cls')
            if user == ((information[0].replace("\n", "")).split(" : "))[1] and pasword == ((information[1].replace("\n", "")).split(" : "))[1]:
                print("🌟 You have successfully logged in ✅")
                break

            else:
                print("Wrong username or password ❌\n")
                continue

        else:
            os.system('cls')
            print("\n♨️  You don’t have an account❌\n")
            continue
    elif choice == "3" or choice == "f":
        if Have_Profile():
            print("🔰 Please answer to Security Questions :\n")
            question_one = input("🎨 What is your Favourite Colour :\n")
            question_two = input("\n🔮 What is your year of birth? :\n")

            if question_one == ((information[2].replace("\n", "")).split(" : "))[1] and question_two == ((information[3].replace("\n", "")).split(" : "))[1]:

                os.system('cls')
                npassword = input("📂 Please enter new password :\n")
                while not (Password_Security(npassword)):
                    os.system('cls')
                    print("🔓 Poor password")
                    npassword = input("📘 Pleae enter safer password :\n")

                nRepeat_password = input(
                    "\n📂 Pleae enter Repeat new password :\n")

                while npassword != nRepeat_password:
                    print("\n🔐 The password and its repetition do not match❌")
                    nRepeat_password = input(
                        "↘️  Pleae enter true Repeat password password :\n")
                edit_file(1, npassword)
                print("\n♨️  Your password successfully edited ✅")
                break

            else:
                print("❌ Wrong answer ...")
                exit(0)

        else:
            os.system('cls')
            print("\n♨️  You don’t have an account❌\n")
            continue
    elif choice == "4" or choice == "e":
        exit(0)
    else:
        print("Invalid input ... ❌\n")
        continue
# option of account

n = 12
r = 12
x = 1
while (r >= 0):
    x += 1
    os.system('cls')
    print("⌛️ Loading " + x * "." + "\n")
    print("🟩" * (n - r) + r * "⬜️")
    time.sleep(random.random())
    r -= 1
    if x == 3:
        x = 0
os.system('cls')
x = 1

f = open("history.txt", "r")
information = f.readlines()

while True:

    print("--------------------------------------------\n")
    print("💌 Welcome " + ((information[0].split(" : "))
          [1]).replace("\n", "") + " to this game❤️\n")
    print("✅ Wins : " + ((information[4].split(" : "))[1]).replace("\n", ""))
    print("❌ Losses : " + ((information[5].split(" : "))[1]).replace("\n", ""))
    print("\n--------------------------------------------")
    print("\n💎  Please select the desired option :\n")
    print("🎯 Play : (1 or p)")
    print("💾 History : (2 or h)")
    print("⚠️  Best Scores : (3 or b)")
    print("⚙️  Settings : (4 or s)")
    print("🎀 About me : (5 or a)")
    print("❌ exit : (6 or e)\n")

    choice = input()

    if choice == "1" or choice == "p":
        break
    elif choice == "2" or choice == "h":

        os.system('cls')

        if information[-1] != "\n":
            print("⭕️  Latest game info :\n")
            maps = information[-2]
            u = (information[-3])
            if information[-3] == "1\n":

                maps = maps.replace("0", "🔘")
                maps = maps.replace("O", "⬜️")
            elif information[-3] == "2\n":

                maps = maps.replace("0", "🟡")
                maps = maps.replace("O", "🟨")
            elif information[-3] == "3\n":

                maps = maps.replace("0", "🔴")
                maps = maps.replace("O", "🟥")
            elif information[-3] == "4\n":

                maps = maps.replace("0", "🟠")
                maps = maps.replace("O", "🟧")
            elif information[-3] == "5\n":

                maps = maps.replace("0", "🟣")
                maps = maps.replace("O", "🟪")
            elif information[-3] == "6\n":

                maps = maps.replace("0", "🟢")
                maps = maps.replace("O", "🟩")

            maps = maps.replace("f", "🚩")
            maps = maps.replace("b", "💣")
            maps = maps.replace("1", "1️⃣")
            maps = maps.replace("2", "2️⃣")
            maps = maps.replace("3", "3️⃣")
            maps = maps.replace("4", "4️⃣")
            maps = maps.replace("5", "5️⃣")
            maps = maps.replace("6", "6️⃣")
            maps = maps.replace("7", "7️⃣")
            maps = maps.replace("8", "8️⃣")

            maps = maps.split("-")
            for x in maps:
                print("".join(x))

            print(f"💯 Result : {information[-4]}")
            print(f"⏰ Date and Time : {information[-1]}\n")

        else:
            print("⚠️  You have not played this game yet.\n")

        if input("🔜 Press b to back :\n") == "b":
            os.system('cls')
            continue
    elif choice == "3" or choice == "b":

        os.system('cls')
        print("🌐 Please enter the size of playground :\n")
        print("😁 Small (s or 1) \n☹️  Medium (m or 2) \n😑 Large (l or 3)\n\n")

        size = input()
        os.system('cls')
        if size == "s" or size == "1":
            print("📊 The best small land scores :\n")
            for x in range(8, 13):
                print(nums(x-7) + " " + (information[x]), end="")

        elif size == "m" or size == "2":
            print("📊 The best medium land scores :\n")
            for x in range(14, 19):
                print(nums(x-13) + " " + (information[x]), end="")

        elif size == "l" or size == "3":
            print("📊 The best large land scores :\n")
            for x in range(20, 25):
                print(nums(x-19) + " " + (information[x]), end="")

        else:
            print("Invalid input ... ❌\n")
            continue

        b = input("\n🔜 back : (b)\n")

        if b == "4" or b == "b":
            os.system('cls')
            continue
    elif choice == "4" or choice == "s":
        os.system('cls')

        print("⚙️   Welcome to the settings,❤️  \n⭐️ please select the desired option :\n")
        print("☑️   Login without password : (1 or l)")
        print("♨️   Change the difficulty level : (2 or d)")
        print("📝  Editing information : (3 or e)")
        print("🌈  Change Theme : (4 or c)\n")
        print("🔜  back : (5 or b)")
        choice = input()

        if choice == "1" or choice == "l":
            os.system('cls')
            print("⏺  Password is required to enter by default :)")
            print("❄️  Do you want to log in without password? (yes or no)")

            choice = input()

            if choice == "yes":
                pasword = input("\n🔐 Pleae enter your password :\n")
                if pasword == ((information[1].replace("\n", "")).split(" : "))[1]:
                    os.system('cls')
                    print("Changes made successfully✅\n")
                    edit_file(6, "yes")
                    continue

                else:
                    print("Password is wrong ❌\n")
                    exit(0)

            elif choice == "no":
                edit_file(6, "no")
        elif choice == "2" or choice == "d":
            os.system('cls')
            print("🌐 Please enter the size of playground :")
            print("📍 The playground is small by default :\n")
            print("😁 Small (s or 1) \n☹️  Medium (m or 2) \n😑 Large (l or 3)\n")
            size = input()

            if size == "s" or size == "1":
                width, height, bumb_number = 9, 9, 10

            elif size == "m" or size == "2":
                width, height, bumb_number = 12, 12, 20

            elif size == "l" or size == "3":
                width, height, bumb_number = 15, 20, 40
        elif choice == "3" or choice == "e":
            os.system('cls')
            print("📝  Which item to edit? :\n")
            print("🔸 Username (1) \n🔹 Password (2) \n🔸 The first security question (3)\n🔹 The last security question (4)\n")
            edit = input()

            if edit == "1":
                edit_file(0, input("\n🔘 Please Enter new name :\n"))
            elif edit == "2":
                newpass = input("\n📘 Pleae enter new password :\n")

                while not (Password_Security(newpass)):
                    os.system('cls')
                    print("🔓 Poor password")
                    newpass = input("📘 Pleae enter safer password :\n")

                Repeat_newpass = input(
                    "\n📘 Pleae enter Repeat new password :\n")

                while newpass != Repeat_newpass:
                    print("\n🔐 The password and its repetition do not match❌")
                    Repeat_newpass = input(
                        "↘️  Pleae enter true Repeat password password :\n")

                edit_file(1, newpass)
            elif edit == "3":
                edit_file(2, input("\n🎨 What is your Favourite Colour :\n"))
            elif edit == "4":
                edit_file(3, input("\n🔮 What is your year of birth? :\n"))
            else:
                print("Invalid input ... ❌\n")
                continue
        elif choice == "4" or choice == "c":
            os.system('cls')
            print(
                "♨️  Please select your favorite theme😍 :\n(The first theme is by default🎯)\n")
            print("---------------------------------------------\n")
            print("1️⃣ 1️⃣ 1️⃣ 💣1️⃣  " + " 🟨🟨🟨🟨🟨 " + " 💣1️⃣ 🔴1️⃣ 🟥 ")
            print("🔘🔘1️⃣ 1️⃣ 1️⃣  " + " 1️⃣ 1️⃣ 1️⃣ 1️⃣ 1️⃣  " + " 1️⃣ 1️⃣ 🔴1️⃣ 🟥 ")
            print("🔘🔘🔘1️⃣ ⬜️  " + "🟡🟡🟡1️⃣ 💣" + "  1️⃣ 1️⃣ 🔴1️⃣ 🟥")
            print("1️⃣ 1️⃣ 1️⃣ ⬜️⬜️ " + " 🟡🟡🟡1️⃣ 1️⃣ " + "  💣1️⃣ 🔴1️⃣ 🟥")
            print("\n     1           2           3")
            print("---------------------------------------------")
            print("\n💣1️⃣ 🟠1️⃣ 🟧 " + " 🟪🟪🟪🟪🟪 " + " 1️⃣ 💣1️⃣ 🟩1️⃣")
            print("1️⃣ 1️⃣ 🟠1️⃣ 🟧 " + " 1️⃣ 1️⃣ 1️⃣ 🟪🟪 " + " 1️⃣ 1️⃣ 1️⃣ 🟩🟩")
            print("🟠🟠🟠1️⃣ 🟧 " + " 🟣🟣🟣1️⃣ 1️⃣  " + " 🟢🟢🟢1️⃣ 🟩")
            print("1️⃣ 1️⃣ 1️⃣ 1️⃣ 🟧 " + " 🟣🟣🟣1️⃣ 💣 " + " 1️⃣ 1️⃣ 1️⃣ 🟩🟩\n")
            print("     4           5           6")
            print("---------------------------------------------")
            x = input("\n💎 Your Choise is : ")

            if x == "1":
                home = "⬜️"
                zerohome = "🔘"

            elif x == "2":
                home = "🟨"
                zerohome = "🟡"

            elif x == "3":
                home = "🟥"
                zerohome = "💢"

            elif x == "4":
                home = "🟧"
                zerohome = "🟠"

            elif x == "5":
                home = "🟪"
                zerohome = "🟣"

            elif x == "6":
                home = "🟩"
                zerohome = "🟢"

            else:
                print("Invalid input ... ❌\n")
                continue

        elif choice == "5" or choice == "b":
            os.system('cls')
            continue
        else:
            print("Invalid input ... ❌\n")
            continue

        os.system('cls')
        print("Changes made successfully✅\n")
        continue
    elif choice == "5" or choice == "a":

        os.system('cls')
        print("💎 This game is programmed by Amir Hossein Zandvani.")
        b = input("\n🔜 back : (b)\n")

        if b == "4" or b == "b":
            os.system('cls')
            continue
    elif choice == "6" or choice == "e":
        exit(0)
    else:
        print("Invalid input ... ❌\n")
        continue
# The main menu of the game

while True:
    Playground = Creat_Playground()
    flag_number = bumb_number
    numbers = [x for x in range(1, width*height, width)]
    bombs = bombing()
    zero_home = []
    flaged = set()
    isWinner = True
    selected = set()
    timetotal = width * height * 5
    f = open("history.txt", "a")

    while True:

        if timetotal <= 0:
            print("Time is over")
            isWinner = False
            timetotal = 0
            break
        start = time.time()

        if flaged == bombs:
            break

        os.system('cls')
        print("----------------------------------")
        print("        🚩 " + str(flag_number) + "      ⏰ " + str(timetotal))
        print("----------------------------------\n")

        for y in range(0, height):

            print((numbers[y] < 10) * " " + (numbers[y] < 100)
                  * " " + str(numbers[y]) + " --> ", end="")
            print("".join(Playground[y]))

        print("\n----------------------------------")

        inputs = input("\n📊 Your choice is : ").split()

        while not (valid_input(inputs)) or (calculater(int(inputs[0]))[0], calculater(int(inputs[0]))[1]) in selected:
            print("invalid or chosen input ...\nPlease enter the inputs again :")
            inputs = input().split()

        while len(inputs) == 2 and flag_number == 0 and (calculater(int(inputs[0]))[0], calculater(int(inputs[0]))[1]) not in flaged:
            print("flag is not enough\nPlease enter the inputs again :")
            inputs = input().split()

        while (calculater(int(inputs[0]))[0], calculater(int(inputs[0]))[1]) in flaged and len(inputs) == 1:
            print(
                "this home is flaged and can't select it\nPlease enter the inputs again :")
            inputs = input().split()

        number = int(inputs[0])
        Coordinates = (calculater(number)[0], calculater(number)[1])

        if len(inputs) == 1:

            selected.add((calculater(number)[0], calculater(number)[1]))

            if len(selected) == 1 and ((calculater(number)[0], calculater(number)[1])) in bombs:
                while ((calculater(number)[0], calculater(number)[1])) in bombs:
                    bombs = bombing()

            if Coordinates in bombs:
                isWinner = False
                for n in bombs:
                    if Playground[n[0]][n[1]] != "🚩":
                        Playground[n[0]][n[1]] = "💣"
                break

            else:
                home_num = house_bombs(Coordinates[0], Coordinates[1])
                if home_num == 0:
                    Playground[Coordinates[0]][Coordinates[1]] = zerohome
                    zero_home.append(Coordinates)

                else:
                    Playground[Coordinates[0]][Coordinates[1]] = nums(home_num)

                while len(zero_home):

                    zero_home = set(zero_home)
                    zero_home = list(zero_home)
                    clearing(zero_home[0][0], zero_home[0][1])
                    zero_home.remove((zero_home[0][0], zero_home[0][1]))

        else:
            if (Coordinates[0], Coordinates[1]) not in flaged:
                flaged.add((Coordinates[0], Coordinates[1]))
                flaging(Coordinates[0], Coordinates[1])
                flag_number -= 1

            else:
                flag_number += 1
                Playground[Coordinates[0]][Coordinates[1]] = home
                flaged.remove((Coordinates[0], Coordinates[1]))

        timetotal -= int(time.time() - start)

    f1 = open("history.txt", "r")
    information = f1.readlines()

    if isWinner:
        wins = int(((information[4].replace("\n", "")).split(" : "))[1])
        wins += 1
        f.write("\n\nwin" + "\n")
        edit_file(4, wins)

    else:
        losts = int(((information[5].replace("\n", "")).split(" : "))[1])
        losts += 1
        f.write("\n\nlose" + "\n")
        edit_file(5, losts)
    os.system('cls')
    print("----------------------------------")
    print("        🚩 " + str(flag_number) + "      ⏰ " + str(timetotal))
    print("----------------------------------\n")

    maps = ""
    f.write(str(x) + "\n")
    for y in range(0, height):

        maps += "".join(Playground[y])
        print((numbers[y] < 10) * " " + (numbers[y] < 100)
              * " " + str(numbers[y]) + " --> ", end="")
        print("".join(Playground[y]))
        maps += "-"

    maps = maps.replace(zerohome, "0")
    maps = maps.replace(home, "O")
    maps = maps.replace("🚩", "f")
    maps = maps.replace("💣", "b")
    maps = maps.replace("1️⃣", "1")
    maps = maps.replace("2️⃣", "2")
    maps = maps.replace("3️⃣", "3")
    maps = maps.replace("4️⃣", "4")
    maps = maps.replace("5️⃣", "5")
    maps = maps.replace("6️⃣", "6")
    maps = maps.replace("7️⃣", "7")
    maps = maps.replace("8️⃣", "8")

    f.write(maps + "\n")

    t = time.localtime()
    timee = time.strftime("%m/%d/%Y %H:%M:%S", t)
    f.write(timee)
    f.close()

    print("\n----------------------------------\n")
    if isWinner:
        best_socer(timetotal, bumb_number)
        print("         ✨ You Win ✨")

    else:
        print("        🔥 Game Over 🔥")

    print("\n----------------------------------\n")

    alert = input("♻️  Do you want to play again? (yes or no)\n")

    if alert == "yes":
        continue

    elif alert == "no":
        print("\n♨️  Goog bye 🖐")
        break
