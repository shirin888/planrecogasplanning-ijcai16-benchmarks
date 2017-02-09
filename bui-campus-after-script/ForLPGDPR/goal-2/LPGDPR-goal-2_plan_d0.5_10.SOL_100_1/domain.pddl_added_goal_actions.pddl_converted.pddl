(define (domain campus)
(:requirements :strips :typing :action-costs)
(:types place)
(:constants
bank watson_theater hayman_theater davis_theater jones_theater
bookmark_cafe library cbs psychology_bldg angazi_cafe tav - place
)
(:predicates (considered_occur_init)(considered_occur_move_davis_theater_bank_0)
(considered_occur_move_bank_psychology_bldg_1)
(considered_occur_move_psychology_bldg_davis_theater_2)
(considered_occur_move_davis_theater_watson_theater_3)
(considered_occur_move_watson_theater_jones_theater_4)
(considered_occur_move_jones_theater_bookmark_cafe_5)
(considered_occur_move_bookmark_cafe_psychology_bldg_6)
(considered_occur_move_hayman_theater_jones_theater_7)

(occur_move ?src - place ?dst - place)
(done) (notdone)
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
(:functions (total-cost))
(:action Goal_breakfast__lecture-1-taken__group-meeting-1__lecture-2-taken__coffee_
:parameters ()
:precondition (and (notdone) (breakfast)(lecture-1-taken)(group-meeting-1)(lecture-2-taken)(coffee))
:effect (and  (not (notdone)) (done) (increase (total-cost) 11)))
(:action Goal_group-meeting-2__banking__lecture-3-taken__lecture-4-taken__group-meeting-3__lunch_
:parameters ()
:precondition (and (notdone) (group-meeting-2)(banking)(lecture-3-taken)(lecture-4-taken)(group-meeting-3)(lunch))
:effect (and  (not (notdone)) (done) (increase (total-cost) 11)))
(:action MOVE
:parameters( ?src - place ?dst - place )
:precondition (and (notdone)  (at ?src ) )
:effect ( and 
(occur_move ?src ?dst)
(at ?dst)
(increase (total-cost) 11)
(not (at ?src))
)
)
(:action ACTIVITY-BANKING
:parameters()
:precondition (and (notdone)  (at bank))
:effect (and 
(banking)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-TAKE-LECTURE-1
:parameters()
:precondition (and (notdone)  (at watson_theater))
:effect (and 
(lecture-1-taken)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-TAKE-LECTURE-2
:parameters()
:precondition (and (notdone)  (at hayman_theater) (breakfast) (lecture-1-taken))
:effect (and 
(lecture-2-taken)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-TAKE-LECTURE-3
:parameters()
:precondition (and (notdone)  (at davis_theater) (group-meeting-2) (banking))
:effect	(and 
(lecture-3-taken)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-TAKE-LECTURE-4
:parameters()
:precondition (and (notdone)  (at jones_theater) (lecture-3-taken))
:effect (and 
(lecture-4-taken)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-GROUP-MEETING-1-1
:parameters()
:precondition (and (notdone)  (at bookmark_cafe) (lecture-1-taken) (breakfast))
:effect (and 
(group-meeting-1)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-GROUP-MEETING-1-2
:parameters()
:precondition (and (notdone)  (at library) (lecture-1-taken) (breakfast))
:effect (and 
(group-meeting-1)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-GROUP-MEETING-1-3
:parameters()
:precondition (and (notdone)  (at cbs) (lecture-1-taken) (breakfast))
:effect (and 
(group-meeting-1)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-GROUP-MEETING-2-4
:parameters()
:precondition (and (notdone)  (at library))
:effect (and 
(group-meeting-2)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-GROUP-MEETING-2-1
:parameters()
:precondition (and (notdone)  (at cbs))
:effect (and 
(group-meeting-2)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-GROUP-MEETING-2-2
:parameters()
:precondition (and (notdone)  (at psychology_bldg))
:effect (and 
(group-meeting-2)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-GROUP-MEETING-3-1
:parameters()
:precondition (and (notdone)  (at angazi_cafe) (lecture-4-taken))
:effect (and 
(group-meeting-3)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-GROUP-MEETING-3-2
:parameters()
:precondition (and (notdone)  (at psychology_bldg) (lecture-4-taken))
:effect (and 
(group-meeting-3)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-COFFEE-1
:parameters()
:precondition (and (notdone)  (at tav) (lecture-2-taken) (group-meeting-1))
:effect (and 
(coffee)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-COFFEE-2
:parameters ()
:precondition (and (notdone)  (at angazi_cafe) (lecture-2-taken) (group-meeting-1))
:effect (and 
(coffee)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-COFFEE-3
:parameters ()
:precondition (and (notdone)  (at bookmark_cafe) (lecture-2-taken) (group-meeting-1))
:effect (and 
(coffee)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-BREAKFAST-1
:parameters()
:precondition (and (notdone)  (at tav))
:effect (and 
(breakfast)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-BREAKFAST-2
:parameters ()
:precondition (and (notdone)  (at angazi_cafe))
:effect (and 
(breakfast)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-BREAKFAST
:parameters ()
:precondition (and (notdone)  (at bookmark_cafe))
:effect (and 
(breakfast)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-LUNCH-1
:parameters ()
:precondition (and (notdone)  (at tav))
:effect (and 
(lunch)
(increase (total-cost) 11)
)
)
(:action ACTIVITY-LUNCH-2
:parameters ()
:precondition (and (notdone)  (at bookmark_cafe))
:effect (and 
(lunch)
(increase (total-cost) 11)
)
)

(:action hidden-explain-obs-occur_move_davis_theater_bank_0
     :parameters ()
     :precondition (and  (considered_occur_init) (occur_move davis_theater bank))
     :effect (and (not  (considered_occur_init)) (considered_occur_move_davis_theater_bank_0) (increase (total-cost) 1)))  

(:action hidden-explain-obs-occur_move_bank_psychology_bldg_1
     :parameters ()
     :precondition (and (considered_occur_move_davis_theater_bank_0)(occur_move bank psychology_bldg))
     :effect (and (not (considered_occur_move_davis_theater_bank_0)) (considered_occur_move_bank_psychology_bldg_1) (increase (total-cost) 1)))  

(:action hidden-explain-obs-occur_move_psychology_bldg_davis_theater_2
     :parameters ()
     :precondition (and (considered_occur_move_bank_psychology_bldg_1)(occur_move psychology_bldg davis_theater))
     :effect (and (not (considered_occur_move_bank_psychology_bldg_1)) (considered_occur_move_psychology_bldg_davis_theater_2) (increase (total-cost) 1)))  

(:action hidden-explain-obs-occur_move_davis_theater_watson_theater_3
     :parameters ()
     :precondition (and (considered_occur_move_psychology_bldg_davis_theater_2)(occur_move davis_theater watson_theater))
     :effect (and (not (considered_occur_move_psychology_bldg_davis_theater_2)) (considered_occur_move_davis_theater_watson_theater_3) (increase (total-cost) 1)))  

(:action hidden-explain-obs-occur_move_watson_theater_jones_theater_4
     :parameters ()
     :precondition (and (considered_occur_move_davis_theater_watson_theater_3)(occur_move watson_theater jones_theater))
     :effect (and (not (considered_occur_move_davis_theater_watson_theater_3)) (considered_occur_move_watson_theater_jones_theater_4) (increase (total-cost) 1)))  

(:action hidden-explain-obs-occur_move_jones_theater_bookmark_cafe_5
     :parameters ()
     :precondition (and (considered_occur_move_watson_theater_jones_theater_4)(occur_move jones_theater bookmark_cafe))
     :effect (and (not (considered_occur_move_watson_theater_jones_theater_4)) (considered_occur_move_jones_theater_bookmark_cafe_5) (increase (total-cost) 1)))  

(:action hidden-explain-obs-occur_move_bookmark_cafe_psychology_bldg_6
     :parameters ()
     :precondition (and (considered_occur_move_jones_theater_bookmark_cafe_5)(occur_move bookmark_cafe psychology_bldg))
     :effect (and (not (considered_occur_move_jones_theater_bookmark_cafe_5)) (considered_occur_move_bookmark_cafe_psychology_bldg_6) (increase (total-cost) 1)))  

(:action hidden-explain-obs-occur_move_hayman_theater_jones_theater_7
     :parameters ()
     :precondition (and (considered_occur_move_bookmark_cafe_psychology_bldg_6)(occur_move hayman_theater jones_theater))
     :effect (and (not (considered_occur_move_bookmark_cafe_psychology_bldg_6)) (considered_occur_move_hayman_theater_jones_theater_7) (increase (total-cost) 1)))  



(:action hidden-discard-obs-occur_move_davis_theater_bank_0
     :parameters ()
     :precondition (and  (considered_occur_init) (not (occur_move davis_theater bank)))
     :effect (and (not  (considered_occur_init)) (considered_occur_move_davis_theater_bank_0) (increase (total-cost) 2000)))

(:action hidden-discard-obs-occur_move_bank_psychology_bldg_1
     :parameters ()
     :precondition (and (considered_occur_move_davis_theater_bank_0)(not (occur_move bank psychology_bldg)))
     :effect (and (not (considered_occur_move_davis_theater_bank_0)) (considered_occur_move_bank_psychology_bldg_1) (increase (total-cost) 2000)))

(:action hidden-discard-obs-occur_move_psychology_bldg_davis_theater_2
     :parameters ()
     :precondition (and (considered_occur_move_bank_psychology_bldg_1)(not (occur_move psychology_bldg davis_theater)))
     :effect (and (not (considered_occur_move_bank_psychology_bldg_1)) (considered_occur_move_psychology_bldg_davis_theater_2) (increase (total-cost) 2000)))

(:action hidden-discard-obs-occur_move_davis_theater_watson_theater_3
     :parameters ()
     :precondition (and (considered_occur_move_psychology_bldg_davis_theater_2)(not (occur_move davis_theater watson_theater)))
     :effect (and (not (considered_occur_move_psychology_bldg_davis_theater_2)) (considered_occur_move_davis_theater_watson_theater_3) (increase (total-cost) 2000)))

(:action hidden-discard-obs-occur_move_watson_theater_jones_theater_4
     :parameters ()
     :precondition (and (considered_occur_move_davis_theater_watson_theater_3)(not (occur_move watson_theater jones_theater)))
     :effect (and (not (considered_occur_move_davis_theater_watson_theater_3)) (considered_occur_move_watson_theater_jones_theater_4) (increase (total-cost) 2000)))

(:action hidden-discard-obs-occur_move_jones_theater_bookmark_cafe_5
     :parameters ()
     :precondition (and (considered_occur_move_watson_theater_jones_theater_4)(not (occur_move jones_theater bookmark_cafe)))
     :effect (and (not (considered_occur_move_watson_theater_jones_theater_4)) (considered_occur_move_jones_theater_bookmark_cafe_5) (increase (total-cost) 2000)))

(:action hidden-discard-obs-occur_move_bookmark_cafe_psychology_bldg_6
     :parameters ()
     :precondition (and (considered_occur_move_jones_theater_bookmark_cafe_5)(not (occur_move bookmark_cafe psychology_bldg)))
     :effect (and (not (considered_occur_move_jones_theater_bookmark_cafe_5)) (considered_occur_move_bookmark_cafe_psychology_bldg_6) (increase (total-cost) 2000)))

(:action hidden-discard-obs-occur_move_hayman_theater_jones_theater_7
     :parameters ()
     :precondition (and (considered_occur_move_bookmark_cafe_psychology_bldg_6)(not (occur_move hayman_theater jones_theater)))
     :effect (and (not (considered_occur_move_bookmark_cafe_psychology_bldg_6)) (considered_occur_move_hayman_theater_jones_theater_7) (increase (total-cost) 2000)))
)
