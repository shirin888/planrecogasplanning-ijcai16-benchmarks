(define (domain campus)
(:requirements :strips :typing)
(:types place)
(:constants
bank watson_theater hayman_theater davis_theater jones_theater
bookmark_cafe library cbs psychology_bldg angazi_cafe tav - place
)
(:predicates 
 (done) (notdone) (done-goal-1) (done-goal-2)
(at ?p - place )
(banking)
(lecture-1-taken)
(lecture-2-taken)
(lecture-3-taken)
(lecture-4-taken)
(group-meeting-1)
(group-meeting-2)
(group-meeting-3)
(coffee)
(breakfast)
(lunch)
)

(:action Goal_breakfast__lecture-1-taken__group-meeting-1__lecture-2-taken__coffee_
 :parameters () 
:precondition (and (notdone) (breakfast)(lecture-1-taken)(group-meeting-1)(lecture-2-taken)(coffee)) 
:effect (and (not (notdone)) (done) (done-goal-1) )) 
(:action Goal_group-meeting-2__banking__lecture-3-taken__lecture-4-taken__group-meeting-3__lunch_
 :parameters () 
:precondition (and (notdone) (group-meeting-2)(banking)(lecture-3-taken)(lecture-4-taken)(group-meeting-3)(lunch)) 
:effect (and (not (notdone)) (done) (done-goal-2) )) 

(:action MOVE
:parameters( ?src - place ?dst - place )
:precondition (and (notdone)  (at ?src ) )
:effect ( and
(at ?dst)

(not (at ?src))
)
)
(:action ACTIVITY-BANKING
:parameters()
:precondition (and (notdone)  (at bank))
:effect (and
(banking)

)
)
(:action ACTIVITY-TAKE-LECTURE-1
:parameters()
:precondition (and (notdone)  (at watson_theater))
:effect (and
(lecture-1-taken)

)
)
(:action ACTIVITY-TAKE-LECTURE-2
:parameters()
:precondition (and (notdone)  (at hayman_theater) (breakfast) (lecture-1-taken))
:effect (and
(lecture-2-taken)

)
)
(:action ACTIVITY-TAKE-LECTURE-3
:parameters()
:precondition (and (notdone)  (at davis_theater) (group-meeting-2) (banking))
:effect	(and
(lecture-3-taken)

)
)
(:action ACTIVITY-TAKE-LECTURE-4
:parameters()
:precondition (and (notdone)  (at jones_theater) (lecture-3-taken))
:effect (and
(lecture-4-taken)

)
)
(:action ACTIVITY-GROUP-MEETING-1-1
:parameters()
:precondition (and (notdone)  (at bookmark_cafe) (lecture-1-taken) (breakfast))
:effect (and
(group-meeting-1)

)
)
(:action ACTIVITY-GROUP-MEETING-1-2
:parameters()
:precondition (and (notdone)  (at library) (lecture-1-taken) (breakfast))
:effect (and
(group-meeting-1)

)
)
(:action ACTIVITY-GROUP-MEETING-1-3
:parameters()
:precondition (and (notdone)  (at cbs) (lecture-1-taken) (breakfast))
:effect (and
(group-meeting-1)

)
)
(:action ACTIVITY-GROUP-MEETING-2-4
:parameters()
:precondition (and (notdone)  (at library))
:effect (and
(group-meeting-2)

)
)
(:action ACTIVITY-GROUP-MEETING-2-1
:parameters()
:precondition (and (notdone)  (at cbs))
:effect (and
(group-meeting-2)

)
)
(:action ACTIVITY-GROUP-MEETING-2-2
:parameters()
:precondition (and (notdone)  (at psychology_bldg))
:effect (and
(group-meeting-2)

)
)
(:action ACTIVITY-GROUP-MEETING-3-1
:parameters()
:precondition (and (notdone)  (at angazi_cafe) (lecture-4-taken))
:effect (and
(group-meeting-3)

)
)
(:action ACTIVITY-GROUP-MEETING-3-2
:parameters()
:precondition (and (notdone)  (at psychology_bldg) (lecture-4-taken))
:effect (and
(group-meeting-3)

)
)
(:action ACTIVITY-COFFEE-1
:parameters()
:precondition (and (notdone)  (at tav) (lecture-2-taken) (group-meeting-1))
:effect (and
(coffee)

)
)
(:action ACTIVITY-COFFEE-2
:parameters ()
:precondition (and (notdone)  (at angazi_cafe) (lecture-2-taken) (group-meeting-1))
:effect (and
(coffee)

)
)
(:action ACTIVITY-COFFEE-3
:parameters ()
:precondition (and (notdone)  (at bookmark_cafe) (lecture-2-taken) (group-meeting-1))
:effect (and
(coffee)

)
)
(:action ACTIVITY-BREAKFAST-1
:parameters()
:precondition (and (notdone)  (at tav))
:effect (and
(breakfast)

)
)
(:action ACTIVITY-BREAKFAST-2
:parameters ()
:precondition (and (notdone)  (at angazi_cafe))
:effect (and
(breakfast)

)
)
(:action ACTIVITY-BREAKFAST
:parameters ()
:precondition (and (notdone)  (at bookmark_cafe))
:effect (and
(breakfast)

)
)
(:action ACTIVITY-LUNCH-1
:parameters ()
:precondition (and (notdone)  (at tav))
:effect (and
(lunch)

)
)
(:action ACTIVITY-LUNCH-2
:parameters ()
:precondition (and (notdone)  (at bookmark_cafe))
:effect (and
(lunch)

)
)
)
