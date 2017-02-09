#!/usr/bin/python
import os
import re
import commands
import sys



#For Problem file:

# 1. add the obs-type from the obs.txt  (you don't need this step)
# 2. if total-order not there (add it)
# 3. add considered predicate to the goal state
##	- if no future is given, this is the last observation (considered_lastObs)
##	- if future step is given, this is (considered_o_future_step)
# 4. if minimize total-cost not there add it

#For Domain file:
# 1. add type obs-type (you don't need this step)
# 2. check requirements (should have typing adl and action-costs)
# 3. add the following predicates:
##	- (o-future)
##	- (considered_..) for each obs in the obs.txt file
##	- (consdiered_o_future) for each future step observation
#4. for each of the original actions:
##	- if future step is given: add (o-future) predicate effect
##	- add total-cost 10 
#5. for each of the observations from obs.txt file
##	- add discard actions
##	- add explain actions
#6. If future step is given, create explain future observations
#7. add total-cost if not written




#domain problem obs steps

inputdomain = sys.argv[1]
inputproblem = sys.argv[2]
inputobs = sys.argv[3]

hasFuture = False

if len(sys.argv) > 4:
    hasFuture = True
    inputfuture = sys.argv[4]

inProblemFile  = file(inputproblem, "r")
inDomainFile  = file(inputdomain, "r")
inObsFile  = file(inputobs, "r")


outDomain = file(inputdomain+"_converted.pddl", "w")
outProblem  = file(inputproblem+"_converted.pddl", "w")

hasCost = False


observations = inObsFile.readlines()
preobservations = [l.strip() for l in observations if l.strip()]  #original obs (use for precondition)

consideredobservation = []

#replace all space with underscore and remove all paranthesis
for i, o in enumerate(preobservations):
    o = o.replace(" ", "_")
    o = o.replace("(", "")
    o = o.replace(")", "_" + str(i))
    consideredobservation.insert(i, o)

inObsFile.close()


#### Problem Related
lines = inProblemFile.readlines()
cleanLines = [l.strip() for l in lines if l.strip()]


for line in cleanLines:
    if (line.find("total-cost") != -1):
	hasCost = True
	break;

#inProblemFile.seek(0)

atLine = 0

for line in cleanLines:
    atLine += 1
    org =  line
    if (hasCost and line != ""):
        if (line.find("goal") != -1):
            if  hasFuture:
                goal = "and" + " (considered_o_future_" + inputfuture + ")"
            else:
                goal = "and" + " (considered_" + consideredobservation[len(consideredobservation)-1] + ")"
            org = line.replace("and", goal)
    if (not hasCost and line!= ""):
        if (line.find("init") != -1):
            org = line.replace("init", "init (= (total-cost) 0) (considered_occur_init)")
        elif (line.find("goal") != -1):
            if  hasFuture:
                goal = "and" + " (considered_o_future_" + inputfuture + ")"
            else:
                goal = "and" + " (considered_" + consideredobservation[len(consideredobservation)-1] + ")"
            org = line.replace("and", goal)
        elif atLine == len(cleanLines) :
            org = line[0:len(line)-1] + "(:metric minimize (total-cost)) \n)"
                     
    outProblem.write(org)
    outProblem.write("\n")





###Domain Related

lines = inDomainFile.readlines()
cleanLines = [l.strip() for l in lines if l.strip()]




explainactions = ""
discardactions = ""
futureactions = ""
prevobs = ""

atObs = 0
for i, obs in enumerate(consideredobservation):
    atObs += 1
    explainactions = explainactions + "\n" + "(:action hidden-explain-obs-" + obs
    discardactions = discardactions + "\n" + "(:action hidden-discard-obs-" + obs
    explainactions = explainactions + "\n" + "     :parameters ()"  + "\n"
    discardactions = discardactions + "\n" + "     :parameters ()"  + "\n"
    if (atObs == 1):
        explainactions = explainactions + "     :precondition (and  (considered_occur_init) " + preobservations[i] + ")"  + "\n"
        discardactions = discardactions + "     :precondition (and  (considered_occur_init) (not " + preobservations[i] + "))"  + "\n"
    
        if hasFuture:
            explainactions = explainactions + "     :effect (and (not  (considered_occur_init))(considered_" + obs + ") (not (o-future))  (increase (total-cost) 1)))  "+ "\n"
            discardactions = discardactions + "     :effect (and (not  (considered_occur_init))(considered_" + obs + ") (not (o-future))  (increase (total-cost) 2000)))"+ "\n"
    
        else:
            explainactions = explainactions + "     :effect (and (not  (considered_occur_init)) (considered_" + obs + ") (increase (total-cost) 1)))  "+ "\n"
            discardactions = discardactions + "     :effect (and (not  (considered_occur_init)) (considered_" + obs + ") (increase (total-cost) 2000)))"+ "\n"

    
    else:
        explainactions = explainactions + "     :precondition (and (considered_" + prevobs + ")" + preobservations[i] + ")" + "\n"
        discardactions = discardactions + "     :precondition (and (considered_" + prevobs + ")" +"(not " + preobservations[i] + "))" + "\n"

        if hasFuture:
            explainactions = explainactions + "     :effect (and (not (considered_" + prevobs + ")) (considered_" + obs + ") (not (o-future))  (increase (total-cost) 1)))  "+ "\n"
            discardactions = discardactions + "     :effect (and (not (considered_" + prevobs + ")) (considered_" + obs + ") (not (o-future))  (increase (total-cost) 2000)))"+ "\n"
        
        else:
            explainactions = explainactions + "     :effect (and (not (considered_" + prevobs + ")) (considered_" + obs + ") (increase (total-cost) 1)))  "+ "\n"
            discardactions = discardactions + "     :effect (and (not (considered_" + prevobs + ")) (considered_" + obs + ") (increase (total-cost) 2000)))"+ "\n"



    prevobs = obs

if  hasFuture:
    for i in xrange(1, int(inputfuture)+1):
        futureactions = futureactions + "\n" + "(:action hidden-explain-obs-future_" + str(i)
        futureactions = futureactions + "\n" + "     :parameters ()"  + "\n"
        if (i == 1):
            futureactions = futureactions + "     :precondition (and (considered_occur_init) (considered_" + prevobs + ")(o-future))" + "\n"
            futureactions = futureactions + "     :effect (and (not  (considered_occur_init)) (considered_o_future_" + str(i)+ ") (not (o-future))  (increase (total-cost) 1)))"+ "\n"
        else:
            futureactions = futureactions + "     :precondition (and (considered_o_future_" + str(i-1) + ")(o-future))" + "\n"
            futureactions = futureactions + "     :effect (and not (considered_" + prevobs + "))(considered_o_future_" + str(i)+ ") (not (o-future))  (increase (total-cost) 1)))"+ "\n"




atLine = 0
for line in cleanLines:
    org = line
    atLine += 1
    if (line.find("requirements") != -1 and line.find("cost") == -1):
        org = line.replace("requirements", "requirements :action-costs ")
    elif (line.find("predicates") != -1):
        if not hasCost:
            newpredicates = "(:functions (total-cost)) \n (:predicates (considered_occur_init)"
        else:
            newpredicates = "(:predicates (considered_occur_init)"
        for obs in consideredobservation:
            newpredicates = newpredicates + "(considered_" + obs + ")\n"
        if  hasFuture:
            newpredicates = newpredicates + "(o-future)\n"
            for i in xrange(1, int(inputfuture)+1):
                newpredicates = newpredicates + "(considered_o_future_" + str(i) + ")\n"
        org = line.replace("(:predicates", newpredicates)
    elif (line.find("effect") != -1 and not hasCost and hasFuture):
        org = line.replace("and", "and (o-future) (increase (total-cost) 10)")
    elif (line.find("effect") != -1 and not hasCost):
        org = line.replace("and", "and (increase (total-cost) 10)")
    elif (line.find("effect") != -1 and hasCost and line.find("increase ") != -1 and hasFuture):
        p = re.compile('[\d]+')
        oldcost = p.findall(line)
        oldcost = oldcost[0]
        org = line.replace(oldcost, str(int(oldcost)+10))
        org = org.replace("and", "and (o-future)")
    elif (line.find("effect") != -1 and hasCost and line.find("increase ") != -1):
        p = re.compile('[\d]+')
        oldcost = p.findall(line)
        oldcost = oldcost[0]
        org = line.replace(oldcost, str(int(oldcost)+10))
        org = org.replace("and", "and ")
    elif (line.find("effect") != -1 and hasCost and line.find("increase ") == -1 and hasFuture):
        org = line.replace("and", "and (o-future)")
    elif (line.find("effect") != -1 and hasCost and line.find("increase ") == -1):
        org = line.replace("and", "and ")
    elif (line.find("increase ") != -1 and hasCost):
        p = re.compile('[\d]+')
        oldcost = p.findall(line)
        oldcost = oldcost[0]
        org = line.replace(oldcost, str(int(oldcost)+10))
    elif atLine == len(cleanLines) :
        org = line[0:len(line)-1] +  explainactions + "\n" + futureactions + "\n" + discardactions +")"
    
    outDomain.write(org)
    outDomain.write("\n")


inProblemFile.close()
outProblem.close()
inDomainFile.close()
outDomain.close()



