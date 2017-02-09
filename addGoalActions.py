#!/usr/bin/python
import os
import re
import commands
import sys




# Take the domain, problem, and hyps.txt file, should work for both pddl and sppl
# generate one action per each goal where the precondition is the goal predicate and effect is the done predicate.
# Add the done predicate to the problem
# we will use the pddl version for LPG and sppl for top-k

#if the problem has <Hypothesis>, then juse remove it



#domain problem obs steps

inputdomain = sys.argv[1]
inputproblem = sys.argv[2]
inputhyp = sys.argv[3]



inProblemFile  = file(inputproblem, "r")
inDomainFile  = file(inputdomain, "r")
inHypsFile  = file(inputhyp, "r")

if (inputdomain.find("sppl") != -1 ):
    outDomain = file(inputdomain+"_added_goal_actions.sppl", "w")
    outProblem  = file(inputproblem+"_added_goal_actions.sppl", "w")
else :
    outDomain = file(inputdomain+"_added_goal_actions.pddl", "w")
    outProblem  = file(inputproblem+"_added_goal_actions.pddl", "w")




hypothesis = inHypsFile.readlines()
cleanhypothesis = [l.replace(", ", "").strip() for l in hypothesis if l.strip()]  #original obs (use for precondition)

#cleanhypothesis = cleanhypothesis.replace(",", " ")

print "clean hypothesis %d", cleanhypothesis

lines = inDomainFile.readlines()
cleanLines = [l.strip() for l in lines if l.strip()]

notAddedGoalActions = True

for line in cleanLines:
    org = line
    if (inputdomain.find("sppl") != -1  and line.find("predicates") != -1 and line.find("orlogic") != -1):
        org = line.replace(":orlogic", ":orlogic \n (done) (notdone)")
    elif (inputdomain.find("sppl") == -1 and line.find("predicates") != -1):
        org = line.replace(":predicates", ":predicates \n (done) (notdone)")

    elif (line.find(":precondition") != -1):
        org = line.replace("and", "and (notdone) ")


    elif (line.find("(:action") != -1 and notAddedGoalActions):
        notAddedGoalActions = False
        goalActions = ""

        for hyp in cleanhypothesis:

            actionname = hyp.replace(" ", "_")
            actionname = actionname.replace("(", "_")
            actionname = actionname.replace(")", "_")
        
            print "actionname %d", actionname
            
            goalActions = goalActions + "(:action Goal" + actionname + "\n :parameters () \n"
             
            if (inputdomain.find("sppl") != -1) :
                goalActions = goalActions + ":cost (1 1)  \n"
                goalActions = goalActions + ":precondition (and (notdone) " + hyp + ") \n" + ":effect (and (not (notdone)) (done))) \n"
             
            if (inputdomain.find("sppl") == -1) :
                goalActions = goalActions + ":precondition (and (notdone) " + hyp + ") \n" + ":effect (and (not (notdone)) (done) (increase (total-cost) 1))) \n"
             
        org = goalActions + "\n" + line

    outDomain.write(org)
    outDomain.write("\n")



#### Problem Related
lines = inProblemFile.readlines()
cleanLines = [l.strip() for l in lines if l.strip()]

for line in cleanLines:
    org =  line
    if (line != "" and line.find("(and") != -1):
        org = line.replace("(and", "(and (done)")

    if (line != "" and line.find("<") != -1):
        org = ""

    if (line.find("(:init") != -1) :
        org = line.replace("(:init", "(:init (notdone)")

    outProblem.write(org)
    outProblem.write("\n")





inProblemFile.close()
outProblem.close()
inDomainFile.close()
outDomain.close()



