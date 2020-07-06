from twilio.rest import Client
import random
import time
import copy

# +14155238886
# join prove-serious


# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(
    "AC694a0a1bb4494297124460beb33a165a", "31e0622e6a8327b63f44201e8791b1f6"
)

win_condition = []


def send_info(number, message):
    # this is the Twilio sandbox testing number
    from_whatsapp_number = "whatsapp:+14155238886"
    # replace this number with your own WhatsApp Messaging number
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


def grudge(player, players):
    global win_condition
    print(
        player.name,
        " can get a new win condition, switch sides, or just simply gain information about another player.",
    )
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


def infatutation(player, players):
    global win_condition
    temporary = copy.deepcopy(players)
    print(
        player.name,
        " can get a new win condition, switch sides, or just simply gain information about another player.",
    )
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
    print(
        player.name,
        " can get a new win condition, switch sides, or just simply gain information about another player.",
    )
    message = "You are now the scapegoat. You win if you get imprisoned. ONLY you win."
    send_info(player.number, message)
    # print(message)
    win_condition.append(["scapegoat", player.name])


def switch(player, players):
    print(
        player.name,
        " can get a new win condition, switch sides, or just simply gain information about another player.",
    )
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
    print(
        player.name,
        " can get a new win condition, switch sides, or just simply gain information about another player.",
    )
    random.shuffle(temporary)
    if temporary[0].name == player.name:
        message = temporary[1].name + " works for " + temporary[1].role
    else:
        message = temporary[0].name + " works for " + temporary[0].role
    send_info(player.number, message)
    # print(message)


def photograph(player, players):
    temporary = copy.deepcopy(players)
    print(
        player.name,
        " has seen a photograph of two people and know they work for same agency.",
    )
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
    print(player.name, " is going to know the agency of another player.")
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
    print(player.name, " will get 2 names, one is virus and one is not.")
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


def confession(player, players):
    temporary = copy.deepcopy(players)
    print(player.name, "must show one player who they are working for.")
    name = input("Enter that players name:")
    for p in temporary:
        if p.name == name:
            message = player.name + " works for " + player.role
            send_info(p.number, message)
            # print(message)
            return


def choose_two(player, players):
    temporary = copy.deepcopy(players)
    print(
        player.name, "must choose two agents. They will know if one of them is virus."
    )
    name1 = input("Enter first name:")
    name2 = input("Enter second name:")
    for p in temporary:
        if p.name == name1 or p.name == name2:
            if p.role == "virus":
                message = "One of " + name1 + " and " + name2 + " is virus"
                send_info(player.number, message)
                # print(message)
                return
            else:
                pass
    message = "Both " + name1 + " and " + name2 + " are service"
    send_info(player.number, message)
    # print(message)


def dojob(player, players):
    j = player.job
    if j == 1:
        photograph(player, players)
    elif j == 2:
        reveal(player, players)
    elif j == 3:
        intelligence(player, players)
    elif j == 4:
        confession(player, players)
    elif j == 5:
        choose_two(player, players)
    elif j == 6:
        grudge(player, players)
    elif j == 7:
        infatutation(player, players)
    elif j == 8:
        scapegoat(player, players)
    elif j == 9:
        switch(player, players)
    else:
        info(player, players)
    return


def find_role(name, players):
    for player in players:
        if player.name == name:
            return player.role


def remove_player(name, players):
    for player in players:
        if player.name == name:
            players.remove(player)
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


if __name__ == "__main__":
    cont = input("Press enter to continue")
    print("Starting game......")
    fptr = open("info.txt", "r")
    f1 = fptr.readlines()
    players_number = int(f1[0])
    names = []
    players = []
    role = []
    numbers = []
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
    # to remove win condition comment this:::::::::::
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
        # name=input('Enter name of player:')
        # number=input('Enter number:')
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
    cont = input("Sent roles to everyone, press enter to continue.")

    for player in players:
        dojob(player, players)
        print()
        cont = input("Press enter to continue")

    lynched = input("Who did you vote:")
    print("")
    print_result(lynched, players)
    # print(win_condition)
    # if win_condition[0] == "normal":
    #     for player in players:
    #         if lynched == player.name:
    #             if player.role == "service":
    #                 print("V.I.R.U.S wins!")
    #                 break
    #             else:
    #                 print("Service wins!")
    #                 break
    # elif win_condition[0] == "scapegoat":
    #     if lynched == win_condition[1]:
    #         print(lynched, "wins!")
    # else:
    #     for player in players:
    #         if lynched == player.name:
    #             if player.role == "service":
    #                 print("V.I.R.U.S wins!")
    #                 break
    #             else:
    #                 print("Service wins!")
    #                 break
    #     if win_condition[0] == "infatuation":
    #         if lynched == win_condition[2]:
    #             print(win_condition[1], " loses as he/she was in love with", lynched)
    #         else:
    #             print(
    #                 win_condition[1],
    #                 " wins as he/she was in love with",
    #                 win_condition[2],
    #             )
    #     if win_condition[0] == "grudge":
    #         if lynched != win_condition[2]:
    #             print(win_condition[1], " loses as he/she had grudge with", lynched)
    #         else:
    #             print(win_condition[1], " wins as he/she had grudge with", lynched)
    # print("win_condition variable is", win_condition)
    # for player in players:
    #     print(player.name, player.role)
    fptr.close()
    # time.sleep(100)
