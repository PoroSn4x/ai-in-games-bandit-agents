===========================
score agent (2 points)
---------------------------
The score agent should work with arbitrary winning shapes and return a move that maximizes the score.
To this end you should generalize the score function explained in the lecture.

 

=====grading criteria======
The score agent should win essentially all games against a random agent.
We use the same test cases as for the bandit agent.
If this is the case, we give 2 points.
A sanity check to the code should check to the code should be provided.
If the code is to slow to be executed, or does not run at all, ask if there is a very easy fix. 
Otherwise, we give 0 points for this assignment.

 

===========================
mcts agent (8 points)
---------------------------
Implement an mcts-agent based on the lecture given by Sarita.
Use the same framework as for the bandit agent.
Implement a method that does a simulation. 
The simulation should be based on a roll-out with two random agents.
Ties need to be broken randomly.

 

Below are the test cases. 
Note that the bandit agent performs better than the mcts-agent.
(This means mcts-agents are not better in all situations.)

 

./main.py --games 100 --size 5 --iterations 250 --parallel 8 shapes1.txt >> results.txt   # two in a row
./main.py --games 100 --size 3 --iterations 250 --parallel 8 shapes2.txt >> results.txt   # tic-tac-toe fast
./main.py --games 100 --size 8 --iterations 250 --parallel 8 shapes3.txt >> results.txt   # plus fast
./main.py --games 100 --size 8 --iterations 250 --parallel 8 shapes4.txt >> results.txt   # L shapes fast
./main.py --games 100 --size 10 --iterations 250 --parallel 8 shapes5.txt >> results.txt  # disjoint fast

 
under files/mcts-test-cases/ all the shape files can be found.
 

=====grading criteria======
The main grading criteria is a comparison to a benchmark.
The agent is testes an gets a SCORE based on the above testcases between 0 and 500.

 

LOW  = 300 
HIGH = 480 

 

If the score is below LOW, we give 0 points for the assignment as the agent is not significantly better than random.
If the agent is above 300 points the grade is computed as follows:

 

GRADE = 6 + 4[(SCORE - 300)/(HIGH - LOW)].

 

Furthermore, there should be a sanity check that indeed a mcts agent is implemented.
If the agent is just a bandit agent, we give 0points.
If the mcts agent is not implemented correctly, one might need to decide on a case to case basis.
As a rule of thump, the points will be halved.