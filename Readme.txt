


October 14, 2015 (update Jan 2017)
————————

The purpose of this script is to generate new plan recognition experiments, where I can modify the observations to be unreliable and select plans that are not necessary optimal.

I made new problems for the plan recognition experiments. While these are for the most part the same domains as in previous work, the ground truth is different, hence the whole problem set is different. 
 
Reason:
1) Their ground truth was only for goals and not plans or ordering of actions in a plan.
2) Their ground truth for the most part came from optimal plans



I created folders and tar.bz2 file for RG10 approach - script (GenerateGroundTruth-RG10.py). The ground truth was created based on the result of the LPG plan. 

	- I took the LPG plan and created a list of potential observations. Note, LPG does not always return optimal plans. So there are several non-optimal plans for each goal, which is what we want.
	- I created several versions where some percentage of these were missing and kept some observations by randome. For example if there are 10 observations in the plan (observations are actions), for the 50% case, I took 5 of these observations by random (keeping the original ordering). I used the ./solver —grndpred to get all the possible observations and used that to get extra observations not previously in the observation 
sequence.
	ran: solver —grndpred tmpfile.txt domain.sppl problem.sppl


	- I also created version where some extra observations are added. These potentially can mess things up, specially in cases where they need to be discarded because there are out of place/context. You can change the script to generate the extra observations based on the length of the plan, or number of observations, for now I set this to either 1 or 2.



- I am including the scripts to generate problems for RG10 and LPGD. You may run the scripts for any problems, look at the original folder to see what is needed there in order to run the script.


- there is also a script that would deal with goals (addGoalActions, where it would add a predicate for each goal). This is needed in order to run LPG, which generates the ground truth plans and observations.


-**IMPORTANT** you need to run GenerateGroundTruth-RG10.py first and then copy the problem folders to the ForLPGDPR, and then run GenerateGroundTruthLPGD.py

The script to compile away the observations is in make-pddl.py.

I have scripts for verification, which looks at each folder which tells what is the ground truth goal or plan for this folder and finds out if the plan/goal that was found meets it, or has a high probably. See the IJCAI-17 paper for more details in  this.

Plan Recognition as Planning Revisited - IJCAI2016

