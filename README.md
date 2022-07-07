# chess-tournament
### Flag
	FLAG-{ch3ss-W1Ll-rUn-Th3-W0rld}
You may change the flag in [chess-tournament/src/config.py](./chess/src/config.py)
### Description FR
Connaissez-vous les échecs? Il n'est jamais trop tard pour apprendre. Serez-vous en mesure de vaincre le champion lors du tournoi annuel d'échecs rapide? Vous receverez une très belle récompense si vous y arrivez. Bonne chance!

### Description EN
Do you know the game of chess? It's never too late to learn. Will you be able to beat the champion in the Annual Speed Chess Tournament? You will receive a very nice reward if you succeed. Good luck!

### Writeup
**For the solver to work, you absolutely need to download stockfish from this [website](https://stockfishchess.org/download/) and put it in the solver folder**

**You also need the stockfish python library : pip install stockfish**

You can find the solver [here](./solver/solver.py)

The goal of the challenge is to find :
* a way to interact with a remote challenge programmatically;
* a way to analyze the 3 chessboards and solve them.

#### Explanation of the solver :
##### **Variables :**
stockfish

    after installing stockfish on your machine, reference to it here

host

    the host of the container
    
port

    the port of the container (supposed to be 8164)


##### **Functions :**
SendAnswer(answer)

    parameter : answer => Text to send to the remote challenge and do Enter

SolveBoard(ignoredLine)

    parameter : ignoredLine => Number of lines ignored before the board

##### **Steps :**
1. Get data from remote challenge
2. Send name
3. Parse and solve first board
4. Parse and solve second board
5. Parse and solve last board
6. Get data from remote challenge containing the flag

### Hints FR
1. Format de réponse pour résoudre l'échiquier dans le tournoi. (e4e5)
2. Vous devez programmer un outil permettant la résolution rapide de l'échiquier.
3. Poisson.

### Hints EN
1. Answer format to solve the board in the tournament. (e4e5)
2. You need to program a tool for fast chess board resolution.
3. Fish

### Author
Vincent De Cooman

Discord : **Homniaxor#1771**

### Changelog
#### 0.1 Initial release
Everything is included, should work out of the box. Run [start.sh](./start.sh) to build and run the container. It binds on 0.0.0.0:8164 by default.
