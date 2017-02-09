#!/usr/bin/python
import os
import re
import commands
import sys
import shutil
import math
import random
import tarfile
import subprocess



path = sys.argv[1]

# Files and Folders for LPGDPR:

# ake domains for LPGDPR



listOfFiles = os.listdir(path+"/ForLPGDPR/")

print "list of  Files %d", listOfFiles

listOfGoalFiles = [f for f in listOfFiles if f.find("goal-") != -1]

print "list of goalFile Files %d", listOfGoalFiles

# For Each goal

for goalFile in listOfGoalFiles:

    listofFiles = os.listdir(path + "/ForLPGDPR/" + goalFile)
    
    listofPlanFiles = [f for f in listofFiles if f.find(".txt") == -1 and f.find("LPGDPR") == -1  and f.find("RG-10") == -1 and f.find("DS_Store") == -1 and f.find(".tar.bz2") == -1]
    
    listofProblemFiles = [f for f in listofFiles if f.find(".txt") == -1 and f.find("-goal-") != -1 and f.find("DS_Store") == -1 and f.find(".tar.bz2") == -1]
    
    
    print "list of plan Files %d", listofPlanFiles
    print "listofProblemFiles %d", listofProblemFiles
    
    for plan in listofPlanFiles:
        
        print "plan name is %d", plan
        
        planfile = file(path +  "/ForLPGDPR/" + goalFile + "/" + plan, "r")
    
        theplancontent = planfile.read()
        planfile.close()
        
        p = re.compile('\([\w\s-]+\)')
        actions = p.findall(theplancontent)
        
        print "actions is %d", actions
        
        
        listofProblemFilesForthisPlan = [f for f in listofProblemFiles if f.find(plan) != -1]
        
        
        print "list of problem Files for this plan %d", listofProblemFilesForthisPlan
    
        for problem in listofProblemFilesForthisPlan:
            
            print "problem %d", problem
            newproblemname = problem.replace("RG-10", "LPGDPR")
            
            print "new problem %d", newproblemname
            
            print "goalFile is %d", goalFile
            
            problempath =  path + "/ForLPGDPR/" + goalFile + "/" +  problem
            #print "problem path is not there %d", problempath
            
            os.rename(path + "/ForLPGDPR/" + goalFile + "/" +  problem, path + "/ForLPGDPR/" + goalFile + "/" + newproblemname)
            
            
            directoryname = path +  "/ForLPGDPR/" + goalFile + "/" +  newproblemname + "/"
            
            print "directory name is %d", directoryname
            
            if not os.path.exists(directoryname + "obs-with-occurs.dat"):
                observationfile = file(directoryname + "obs.dat", "r")
                observations = observationfile.readlines()
                observations = [l.strip() for l in observations if l.strip()]
            
                observationfilewithOccur = file(directoryname + "obs-with-occurs.dat", "w")
            
                for obs in observations:
                    observationfilewithOccur.write(obs.replace("(", "(occur_"))
                    observationfilewithOccur.write("\n")
                
                observationfile.close()
                observationfilewithOccur.close()
            
                                                 
            if not os.path.exists(directoryname + "real_plan.dat"):
                                     
                planfileoutput = file(directoryname + "real_plan.dat", "w")
            
                for action in actions :
                    planfileoutput.write(action)
                    planfileoutput.write("\n")
                           
                planfileoutput.close()
                                                 
                                 
            if not os.path.exists(directoryname + "real_ordering.dat"):
                planfileordering = file(directoryname+ "real_ordering.dat", "w")
            
                numofActions = len(actions)
                  
                  # pick 30 % of the actions
                percentagenum = int(math.ceil(float(numofActions) * (30.0 /100.0)))
                numselected = 0
                toselectList = []
        
                while numselected != percentagenum:
                    toselect = random.randint(0, numofActions-1)
                    if not toselect in toselectList:
                        numselected += 1
                        toselectList.append(toselect)
                    
                print "num of actions %d", numofActions, "percentagenum %d", percentagenum
                print "list selected %d", toselectList
                
                toselectList.sort()
            
                print "list selected after sorting %d", toselectList
                for index in toselectList :
                    planfileordering.write(actions[index])
                    planfileordering.write("\n")
                
                                                 
                planfileordering.close()
               
            if not os.path.exists(directoryname + "domain.pddl_added_goal_actions.pddl"):
                shutil.copy( path +  "/ForLPGDPR/" + "domain.pddl_added_goal_actions.pddl", directoryname)
            
            if not os.path.exists(directoryname + "problem.pddl_added_goal_actions.pddl"):
                shutil.copy( path +  "/ForLPGDPR/" + "problem.pddl_added_goal_actions.pddl", directoryname)
            
            domainfile = path +  "/ForLPGDPR/" + goalFile + "/" + newproblemname + "/domain.pddl_added_goal_actions.pddl"
            problemfile = path + "/ForLPGDPR/" + goalFile + "/" + newproblemname + "/problem.pddl_added_goal_actions.pddl"
            observationfile = directoryname + "obs-with-occurs.dat"
            
            print "domainfile is % ", domainfile
            print "problem file is %",  problemfile
            print "observation file is %d", observationfile

            if not os.path.exists(domainfile):
                print "domain is not there"

            if not os.path.exists(problemfile):
                print "problem is not there"
        
            if not os.path.exists(observationfile):
                print "obs is not there"


            if not os.path.exists(directoryname + "problem.pddl_added_goal_actions.pddl_converted.pddl"):
                sys.argv = ['/Users/shirin/Desktop/Desktop/FSP/Domain/plan_recognition_in_SVN/make-pddl.py', domainfile, problemfile, observationfile]
#subprocess.call(['./Users/shirin/Desktop/Desktop/FSP/Domain/plan_recognition_in_SVN/makepddl.py', domainfile, problemfile, observationfile])
                execfile('/Users/shirin/Desktop/Desktop/FSP/Domain/plan_recognition_in_SVN/make-pddl.py')

        


    # For each plan file
    
        # For each folder that is for this plan (have to match its name with the name of the plan)

            # 0) change its name to be RG-10 -> LPGDPR
    
            #1) update obs.dat to put occur in it
    
            #2) run makepddl.py domain problem obs.dat and put the results in that folder
        
            #3) read the plan and put it in real_plan.dat
        
            #4) pick some ordering and put it in real_order.dat
    
    
    
    
    
    
    
    
    
    
    
    
    
    








