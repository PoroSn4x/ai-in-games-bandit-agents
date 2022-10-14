Implement your agent in the file "agent.py".

------------------------------------------------
usage: main.py 
------------------------------------------------

[--size SIZE]  (boardsize)
[--games GAMES]  (number of games)
[--iterations ITERATIONS] (number of iterations allowed by the agent)
[--print-board {all,final}] 
[--parallel PARALLEL]

and objectives files, like "shapes1.txt".

example

python main.py --size 5 --games 100 --iterations 88 shapes1.txt

------------------------------------------------
test cases 
------------------------------------------------

    main.py --games 100 --size 5 --iterations 100 --parallel 8 shapes1.txt >> results.txt   # two in a row
    main.py --games 100 --size 10 --iterations 100 --parallel 8 shapes1.txt >> results.txt  # two in a row large
    main.py --games 100 --size 3 --iterations 1000 --parallel 8 shapes2.txt >> results.txt  # tic-tac-toe
    main.py --games 100 --size 8 --iterations 1000 --parallel 8 shapes3.txt >> results.txt  # plus
    main.py --games 100 --size 8 --iterations 1000 --parallel 8 shapes4.txt >> results.txt  # circle
    main.py --games 100 --size 8 --iterations 100 --parallel 8 shapes4.txt >> results.txt   # circle fast
    main.py --games 100 --size 10 --iterations 1000 --parallel 8 shapes5.txt >> results.txt # disjoint

------------------------------------------------
grading
------------------------------------------------

If the agent that was implemented is not a Bandit agent, we give a grade of a zero.
If only some of the rules are violated
(say the depth of the roll out is used.) 
we half the grade, i.e. a 7 becomes a 3.5 etc.
Try to make your own judgement.
In case of complaints, the teacher is ultimately responsible.

In total 700 games are played.
We give 1 point for each win, 0.5 points for each draw and zero points for each loss.
THe score are all points together. (0<=score<=700)
If the score is below 400, we give a grade of a zero.
If the score is 400, we give a grade of a 6.
If the score is above 650, we give a grade of a 10.
Between 400 and 650, we interpolate linearly:

grade = 6 + 4*(score - 400)/250 





