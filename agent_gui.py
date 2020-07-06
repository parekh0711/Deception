from tkinter import *
from PIL import ImageTk, Image
from twilio.rest import Client
import random
import time
import copy

flag = 0
task = 1

# Enter your client ID and client password on first two lines of credentials.txt
fptr = open("credentials.txt", "r")
f1 = fptr.readlines()
client = Client(f1[0].strip("\n"), f1[1].strip("\n"))
fptr.close()

win_condition = []
names = []
players = []
role = []
numbers = []


def send_info(number, message):
    from_whatsapp_number = "whatsapp:+14155238886"
    to_whatsapp_number = "whatsapp:" + number
    client.messages.create(
        body=message, from_=from_whatsapp_number, to=to_whatsapp_number
    )
    # print(message)


class player:
    def __init__(self, name, number, role, job):
        self.name = name
        self.number = number
        self.role = role
        self.job = job


class StartPage:
    def __init__(self, window):
        def callback(event):
            global flag
            if 71 <= event.x <= 332 and 461 <= event.y <= 535:
                flag = 1
                C.destroy()
                LoadPage(window)
            elif 239 <= event.x <= 319 and 410 <= event.y <= 444:
                flag = -1
                window.destroy()
            elif 79 <= event.x <= 213 and 399 <= event.y <= 444:
                flag = 2
            else:
                flag = 0

        C = Canvas(window, height=608, width=400)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/start.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("Deception")
        C.pack()
        window.mainloop()


class LoadPage:
    def __init__(self, window):
        D = Canvas(window, height=608, width=400)

        def callback(event):
            global flag
            if 107 <= event.x <= 293 and 207 <= event.y <= 269:
                D.destroy()
                print("Starting game......")
                global players, numbers, role, names, player
                fptr = open("info.txt", "r")
                f1 = fptr.readlines()
                players_number = int(f1[0])
                ind = 1
                for _ in range(players_number):
                    names.append(f1[ind].strip("\n"))
                    ind += 1
                for _ in range(players_number):
                    numbers.append(f1[ind].strip("\n"))
                    ind += 1
                v = int(f1[ind].strip("\n"))
                ind += 1
                s = int(f1[ind].strip("\n"))
                count = 0
                for _ in range(v):
                    role.append("virus")
                for _ in range(s):
                    role.append("service")
                random.shuffle(role)
                if players_number > 5:
                    jobs = [0, 1, 2, 3, 4, 5]
                else:
                    jobs = [1, 2, 3, 4, 5]
                hidden = [6, 7, 8, 9, 10]
                random.shuffle(jobs)
                random.shuffle(hidden)
                index = 0
                extra = 0
                for _ in range(players_number):
                    name = names.pop()
                    number = numbers.pop()
                    if _ > 5:
                        job = jobs[extra]
                        extra += 1
                    else:
                        job = jobs[_]
                    if job == 0:
                        job = hidden[0]
                        random.shuffle(hidden)
                    players.append(player(name, number, role.pop(), job))
                    index += 1
                random.shuffle(players)
                viruses = []
                for player in players:
                    if player.role == "virus":
                        viruses.append(player)
                for player in players:
                    if player.role == "service":
                        message = (
                            "Welcome to Deception!\n You are working for "
                            + player.role
                            + ".\n Your mission is to find all the V.I.R.U.S Agents."
                        )
                        send_info(player.number, message)
                    else:
                        message = (
                            "Welcome to Deception!\n You are working for "
                            + player.role
                            + ".\n Your team is:\n"
                        )
                        for v in viruses:
                            message += v.name
                            message += "\n"
                        message += "All the best!"
                        send_info(player.number, message)
                GamePage(window)

        D.bind("<Button-1>", callback)
        background = PhotoImage(file="images/names.png")
        D.create_image(0, 0, image=background, anchor="nw")
        D.pack()
        window.mainloop()


class HelpPage:
    def __init__(self, window):
        D = Canvas(window, height=608, width=400)
        background = PhotoImage(file="names.png")
        D.create_image(0, 0, image=background, anchor="nw")
        D.pack()
        window.mainloop()


class GamePage:
    def __init__(self, window):
        option = StringVar(window)

        def callback(event):
            global flag
            if 230 <= event.x <= 305 and 386 <= event.y <= 424:
                C.destroy()
                global player, players
                for player in players:
                    j = player.job
                    if j == 1:
                        TaskPage(window, 2, player)
                    elif j == 2:
                        TaskPage(window, 3, player)
                    elif j == 3:
                        TaskPage(window, 4, player)
                    elif j == 4:
                        TaskPage(window, 5, player)
                    elif j == 5:
                        TaskPage(window, 6, player)
                    elif j == 6:
                        TaskPage(window, 1, player)
                    elif j == 7:
                        TaskPage(window, 1, player)
                    elif j == 8:
                        TaskPage(window, 1, player)
                    elif j == 9:
                        TaskPage(window, 1, player)
                    else:
                        TaskPage(window, 1, player)
                VotePage(window)

        C = Canvas(window, height=608, width=400)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/game_1.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("Deception")
        C.pack()
        window.mainloop()


def find_role(name, players):
    for player in players:
        if player.name == name:
            return player.role


def remove_player(name, players):
    for player in players:
        if player.name == name:
            players.remove(player)
            return


class TaskPage:
    def __init__(self, window, task, player):
        option = StringVar(window)
        option2 = StringVar(window)

        def grudge(player, players):
            global win_condition
            # print(
            #     player.name,
            #     " can get a new win condition, switch sides, or just simply gain information about another player.",
            # )
            temporary = copy.deepcopy(players)
            random.shuffle(temporary)
            if temporary[0].name == player.name:
                player2 = temporary[1]
            else:
                player2 = temporary[0]
            message = (
                "You now have a grudge against "
                + player2.name
                + ". You will only win if he/she dies."
            )
            send_info(player.number, message)
            win_condition.append(["grudge", player.name, player2.name])

        def infatuation(player, players):
            global win_condition
            temporary = copy.deepcopy(players)
            # print(
            #     player.name,
            #     " can get a new win condition, switch sides, or just simply gain information about another player.",
            # )
            random.shuffle(temporary)
            if temporary[0].name == player.name:
                player2 = temporary[1]
            else:
                player2 = temporary[0]
            message = (
                "You now feel a lot of love for "
                + player2.name
                + ". You will only win if he/she survives"
            )
            send_info(player.number, message)
            # print(message)
            win_condition.append(["infatuation", player.name, player2.name])

        def scapegoat(player, players):
            global win_condition
            # print(
            #     player.name,
            #     " can get a new win condition, switch sides, or just simply gain information about another player.",
            # )
            message = "You are now the scapegoat. You win if you get imprisoned. ONLY you win."
            send_info(player.number, message)
            # print(message)
            win_condition.append(["scapegoat", player.name])

        def switch(player, players):
            # print(
            #     player.name,
            #     " can get a new win condition, switch sides, or just simply gain information about another player.",
            # )
            if player.role == "virus":
                player.role = "service"
                old = "virus"
                new = "service"
            else:
                player.role = "virus"
                old = "service"
                new = "virus"
            message = "You were " + old + ", but you are now " + new + ";)"
            send_info(player.number, message)
            # print(message)

        def info(player, players):
            temporary = copy.deepcopy(players)
            # print(
            #     player.name,
            #     " can get a new win condition, switch sides, or just simply gain information about another player.",
            # )
            random.shuffle(temporary)
            if temporary[0].name == player.name:
                message = temporary[1].name + " works for " + temporary[1].role
            else:
                message = temporary[0].name + " works for " + temporary[0].role
            send_info(player.number, message)
            # print(message)

        def photograph(player, players):
            temporary = copy.deepcopy(players)
            # print(
            #     player.name,
            #     " has seen a photograph of two people and know they work for same agency.",
            # )
            random.shuffle(temporary)
            i = 1
            # comment this if there are only 2 virus::::::
            if len(players) > 6:
                for t in temporary:
                    if t.name == player.name:
                        temporary.remove(t)
                        break
            while temporary[i].role != temporary[0].role:
                i += 1
            player2 = temporary[i]
            player1 = temporary[0]
            message = (
                "Right now, "
                + player1.name
                + " and "
                + player2.name
                + " work for the same agency."
            )
            send_info(player.number, message)
            # print(message)

        def reveal(player, players):
            temporary = copy.deepcopy(players)
            # print(player.name, " is going to know the agency of another player.")
            for t in temporary:
                if t.name == player.name:
                    temporary.remove(t)
            player1 = temporary[0]
            message = "Right now, " + player1.name + " is working for " + player1.role
            send_info(player.number, message)
            # print(message)

        def intelligence(player, players):
            temporary = copy.deepcopy(players)
            # comment this if there are only 2 virus::::::
            if len(players) > 6:
                for t in temporary:
                    if t.name == player.name:
                        temporary.remove(t)
                        break
            # print(player.name, " will get 2 names, one is virus and one is not.")
            for p in temporary:
                if p.role == "service":
                    player1 = p.name
                    break
            for p in temporary:
                if p.role == "virus":
                    player2 = p.name
                    break
            message = (
                player1
                + " and "
                + player2
                + " are the two names. One is Virus, One is service."
            )
            send_info(player.number, message)
            # print(message)

        def confession(player, players, name):
            temporary = copy.deepcopy(players)
            for p in temporary:
                if p.name == name:
                    message = player.name + " works for " + player.role
                    send_info(p.number, message)
                    # print(message)
                    return

        def choose_two(player, players, name1, name2):
            temporary = copy.deepcopy(players)
            for p in temporary:
                if p.name == name1 or p.name == name2:
                    if p.role == "virus":
                        message = (
                            "Atleast one of " + name1 + " and " + name2 + " is virus"
                        )
                        send_info(player.number, message)
                        # print(message)
                        return
                    else:
                        pass
            message = "Both " + name1 + " and " + name2 + " are service"
            send_info(player.number, message)
            # print(message)

        def callback(event):
            global flag
            if 263 <= event.x <= 342 and 518 <= event.y <= 547:
                C.destroy()
                label.destroy()
                window.quit()

        global players
        if task == 1:
            background_image = PhotoImage(file="images/hidden_agenda.png")
            if player.job == 6:
                grudge(player, players)
            elif player.job == 7:
                infatuation(player, players)
            elif player.job == 8:
                scapegoat(player, players)
            elif player.job == 9:
                switch(player, players)
            else:
                info(player, players)
        elif task == 2:
            photograph(player, players)
            background_image = PhotoImage(file="images/photograph.png")
        elif task == 3:
            reveal(player, players)
            background_image = PhotoImage(file="images/reveal.png")
        elif task == 4:
            intelligence(player, players)
            background_image = PhotoImage(file="images/transmission.png")
        elif task == 5:
            # confession
            background_image = PhotoImage(file="images/confession.png")
        elif task == 6:
            # choose_two
            background_image = PhotoImage(file="images/choose_2.png")

        C = Canvas(window, height=608, width=400)
        C.bind("<Button-1>", callback)
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("Deception")
        C.pack()
        label = Label(window, text=player.name, font="Arial 18 bold")
        label.pack()
        label.place(x=150, y=100)
        if task == 5:
            names = [p.name for p in players if p.name != player.name]
            option.set(names[0])
            menu = OptionMenu(window, option, *names)
            menu.config(font="Arial 17 bold")
            m = window.nametowidget(menu.menuname)
            m.config(font="Arial 17 bold")
            menu.pack()
            menu.place(x=138, y=325)
            btn = Button(
                window,
                text="OK",
                command=lambda: confession(player, players, option.get()),
                width=5,
                font="Arial 14 bold",
                bd=2,
            )
            btn.pack()
            btn.place(x=58, y=517)
        elif task == 6:
            names = [p.name for p in players if p.name != player.name]
            option.set(names[0])
            option2.set(names[1])

            menu = OptionMenu(window, option, *names)
            menu.config(font="Arial 14 bold")
            m = window.nametowidget(menu.menuname)
            m.config(font="Arial 14 bold")

            menu2 = OptionMenu(window, option2, *names)
            menu2.config(font="Arial 14 bold")
            m2 = window.nametowidget(menu2.menuname)
            m2.config(font="Arial 14 bold")

            menu.pack()
            menu2.pack()
            menu.place(x=263, y=372)
            menu2.place(x=263, y=422)

            btn = Button(
                window,
                text="OK",
                command=lambda: choose_two(
                    player, players, option.get(), option2.get()
                ),
                width=5,
                font="Arial 11 bold",
                bd=2,
            )
            btn.pack()
            btn.place(x=273, y=476)

        window.mainloop()
        # print("hello")
        return


def print_result(lynched, players):
    global win_condition
    win_list = []
    if win_condition == []:
        print("Nobody got a win condition.")
    else:
        for condition in win_condition:
            if condition[0] == "scapegoat":
                print(condition[1], "was a scapegoat.")
                if lynched == condition[1]:
                    print(lynched, " wins!")
                    return
                else:
                    remove_player(condition[1], players)
        for condition in win_condition:
            if condition[0] == "infatuation":
                print(condition[1], "was in love with", condition[2])
                if lynched != condition[2]:
                    win_list.append(condition[1])
                else:
                    remove_player(condition[1], players)
            if condition[0] == "grudge":
                print(condition[1], "had a grudge against", condition[2])
                if lynched == condition[2]:
                    win_list.append(condition[1])
                else:
                    remove_player(condition[1], players)
    role = find_role(lynched, players)
    for player in players:
        if player.role != role:
            win_list.append(player.name)
    win_list = set(win_list)
    print("Winners are:")
    for player in players:
        if player.name in win_list:
            print(player.name, player.role)
    return


class VotePage:
    def __init__(self, window):
        def callback(event):
            global flag
            if 239 <= event.x <= 302 and 404 <= event.y <= 435:
                lynched = option.get()
                global players
                print_result(lynched, players)
                window.destroy()

        global players
        C = Canvas(window, height=608, width=400)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/voting.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("Deception")
        C.pack()
        names = [player.name for player in players]
        names.append("nobody")
        option = StringVar(window)
        option.set("nobody")
        menu = OptionMenu(window, option, *names)
        menu.config(font="Arial 18 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Arial 18 bold")
        menu.pack()
        menu.place(x=150, y=245)
        window.mainloop()


if __name__ == "__main__":
    window = Tk()
    StartPage(window)
    print("Thanks for Playing ;)")
