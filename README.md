# Deception

Deception is a game similar to the commonly played roleplay game called Mafia.

The players are divided into two teams, Service and Virus.
The Virus team knows who they are, whereas Service do not.
After the roles are assigned, there is one round in which every person gets some information. After this, voting is held based in this information, and the team member who gets lynched makes his/her team lose.
As the Virus team is always in minority, they need to be more convincing than the service team.

The game works with whatsapp, and the instructions and role infomation are sent on whatsapp to the respective players.

# Compilation

1. In info.txt, update the number of players (n) on line 1.
2. In the next n lines, add n player names.
3. In the next n lines, add n player phone numbers in same order as above.
4. In the next line, add number of virus players needed (>=2).
5. In the next line, add number of service players needed (>=2).
6. Install twilio using :
          pip install twilio
7. Set up sandbox on twilio and update credentials.txt
8. Add players to sandbox
9. Run agent_gui.py from command prompt

# Screenshots
![Alt text](ss1.png?raw=true )
![Alt text](ss2.png?raw=true )
![Alt text](ss3.png?raw=true )
![Alt text](ss4.png?raw=true )



