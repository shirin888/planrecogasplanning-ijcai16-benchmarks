#!/usr/bin/python
import os
import re
import commands
import sys
import shutil
import math
import random
import tarfile



path = sys.argv[1]

# Files and Folders for RG10:

# Take the domain folder
# Go to the RG10 folder

listOfFiles = os.listdir(path+"/ForRG10/")

#print "list of goal Files %d", listOfFiles

listOfGoalFiles = [f for f in listOfFiles if f.find("goal-") != -1]

#print "list of goal Files %d", listOfGoalFiles

# For Each goal
# For each plan

totalObsNum = 0
countObsTotal = 0

for goal in listOfGoalFiles:
    
    goalname = goal
    p = re.compile('-\d')
    goalnum = p.findall(goalname)
    goalnum = goalnum[0]
    
    #print "goal num %d", goalnum

    goalint = int(goalnum.replace("-", ""))
    
    #print "goal int %d", goalint
    
    realHypsFile = file(path +  "/ForRG10/hyps.dat", "r")
    hypotheses = realHypsFile.read()
    hypothsisForGoal = hypotheses.splitlines()[goalint-1]
    
    #print "realhypotheses is %d", hypothsisForGoal
    realHypsFile.close()
    
    
    
    
    
    listofPlanFiles = os.listdir(path + "/ForRG10/" + goal)
    
    listofPlanFiles = [f for f in listofPlanFiles if f.find(".txt") == -1 and f.find("RG-10") == -1 and f.find("DS_Store") == -1 and f.find(".tar.bz2") == -1]
    
    #print "list of plan Files %d", listofPlanFiles
    for plan in listofPlanFiles:
        #print "plan name is %d", plan
                
        planfile = file(path +  "/ForRG10/" + goal + "/" + plan, "r")
        
        #planfileout  = file(path +  "/ForRG10/" + goal + "/" + plan + ".txt", "w")
        theplancontent = planfile.read()
        
    
    #print "the plan content %d", theplancontent
        
        p = re.compile('\([\w\s-]+\)')
        actions = p.findall(theplancontent)
                
                # print "actions is %d", actions
        
   
        
        #pick some observations randomly and make sure they are not in the original action list, and add them somewhere to the observations. It is possible that this observation may still be explainable, but it was not in the original plan, so either needs to be discarded or a new plan must be created. In the mutual exclusive cases, you may see more dicard cases.
        
        
        
        percentageList = [25, 50, 75, 100]
        discardlist = [0, 1, 2]
            
        for y in percentageList:
            for z in discardlist:
                directoryname = path +  "/ForRG10/" + goal + "/" + "RG-10-" + goal + "_" + plan + "_" + str(y) + "_" + str(z) +"/"
                #print "directory name is %d", directoryname

                newdirectory = os.path.dirname(directoryname)
                
                #print "os.path.exists(newdirectory) %d", os.path.exists(newdirectory)
                if not os.path.exists(newdirectory):
                    os.makedirs(newdirectory)
    
                if not os.path.exists(directoryname + "hyps.dat"):
                    shutil.copy( path +  "/ForRG10/" + "hyps.dat", directoryname)

                if not os.path.exists(directoryname + "domain.pddl"):
                    shutil.copy( path +  "/ForRG10/" + "domain.pddl", directoryname)

                if not os.path.exists(directoryname + "template.pddl"):
                    shutil.copy( path +  "/ForRG10/" + "template.pddl", directoryname)
    
                # create real_hyp.dat (what the goal was)
                if not os.path.exists(directoryname + "real_hyp.dat"):
                    realHypsFileOut = file(directoryname + "real_hyp.dat", "w")
                    realHypsFileOut.write(hypothsisForGoal +"\n")
                    realHypsFileOut.close()
                
                # create 12 obs.dat - count how many observations it has, then take 25%, 50%, 75%, 100%
                # have a version for each where you add 1 extra and 2 extra observations (unobserved), so these are observations that are possible, and not appear in the original observations.


                if not os.path.exists(directoryname + "obs.dat"):

                    observationfile = file(path +  "/ForRG10/tmpfile.txt", "r")
                    observationAll = observationfile.read()
                    observationAll = observationAll.split("\n")
                    observationAll = [f.lower() for f in observationAll]
                    
                    # print "observationAll %d", observationAll
                    observationfile.close()
                    
                    
                    observationfileSelected = file(path +  "/ForRG10/tmpfile-subset.txt", "r")
                    observationAlleSelected = observationfileSelected.read()
                    observationAlleSelected = observationAlleSelected.split("\n")
                    observationAlleSelected = [f.lower() for f in observationAlleSelected]
                    
                    # print "observationAlleSelected %d", observationAlleSelected
                    observationfileSelected.close()
                    
                    
                    print "lower case of action %d", actions[0].lower()
                    observations = [f for f in actions if f.lower() in observationAll]
            
                    numofObs = len(observations)
                    percentagenum = int(math.ceil(float(numofObs) * (float(y) /100.0)))
                                
                    countObsTotal += 1
                    totalObsNum  += numofObs
                    
                    print "numOfObs %d", numofObs, "percentage %d",  percentagenum

                    print "countObsTotal = %d", countObsTotal
                    print "totalObsNum = %d", totalObsNum

                    chosenObs = []
                    donen = 0
                    
                    if y == 100:
                        donen = percentagenum
                        observationsSelected = [f.lower() for f in observations]
                    
                    
                    observationsToSelect = list(observations)
                    
                    while donen != percentagenum:
                        obs = random.choice(observationsToSelect)
                        observationsToSelect.remove(obs)
                        # print "observations %d", observations
                        # print "observations after %d", observationsToSelect
                        # print "observationAll %d", observationAll
                        # print "goal is %d", goal, "plan is %d", plan
        
        #print "picking another obs %d", obs, "numofObs %d", numofObs, "donen is %d", donen, " percentagenum is %d", percentagenum
                            #if (not obs in chosenObs):
                        donen += 1
                        chosenObs.append(obs)
                        #print "chosenObs not the right order %d", chosenObs
                        
                        chosenObsCopy = list(chosenObs)
                        observationsCopy = list(observations)
                            
                    if y != 100:
                        observationsSelected = []

                        while observationsCopy != [] and chosenObsCopy != []:
                            f = observationsCopy[0]
                            # print "f right now is %d", f
                            # print "current obsCopy is %d", chosenObsCopy
                            # # print "current observationscopy %d", observationsCopy
                            #print "observationsSelected right now %d", observationsSelected
                            if f in chosenObsCopy:
                                observationsSelected.append(f.lower())
                                chosenObsCopy.remove(f)
                            observationsCopy.remove(f)
                                
                            
                                
                        #old version does not work if observations have repeats
                        #observationsSelected = [f.lower() for f in observations if f in chosenObs]
                        
                        # print "chosenObs not the right order %d", chosenObs
                        # print " obs selected - should be right order %d", observationsSelected


                    # This works if there are no repeats in the observation sequence
                    #while donen != percentagenum:
                    #    obs = random.choice(observations)
                    #    # print "observationAll %d", observationAll
                    #    print "goal is %d", goal, "plan is %d", plan
                    #    print "observations %d", observations
                    #    print "picking another obs %d", obs, "numofObs %d", numofObs, "donen is %d", donen, " percentagenum is %d", percentagenum
                    #    if (not obs in chosenObs):
                    #        donen += 1
                    #        chosenObs.append(obs)
                    #        observationsSelected = [f.lower() for f in observations if f in chosenObs]
                    # print " obs selected %d", observationsSelected
                                                            
                                                            
                    obsExtra = []
                    doneExtra = 0
                    while doneExtra != z:
                        obs = random.choice( observationAlleSelected)
                        # print "picking another obs extra %d", obs
                        if (obs != "" and not obs in obsExtra and not obs.upper() in observations):
                            doneExtra += 1
                            obsExtra.append(obs)
                #print "obs extra %d", obsExtra
    
            
                    obsFileOut = file(directoryname + "obs.dat", "w")
                    for obs in observationsSelected:
                        obsFileOut.write(obs +"\n")

                    for obs in obsExtra:
                        obsFileOut.write(obs + "\n")

                    obsFileOut.close()


                tarname =  path +  "/ForRG10/tarfiles/" + "RG-10-" + goal + "_" + plan + "_" + str(y) + "_" + str(z) +".tar.bz2"
                if not os.path.exists(tarname):
                    #print "I am here %d", goal, " y is %d", y, " z is %d", z, "tar name is ", tarname
        
                    tFile = tarfile.open(tarname, "w:bz2")
                    files = os.listdir(directoryname)
                    #print "files is %d", files
                    for f in files:
                        tFile.add(directoryname + f, arcname = f)
                    
                    #tFile.add(directory, arcname=os.path.basename(directoryname))
                    tFile.close()





        planfile.close()








