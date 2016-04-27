# Skeleton for a FSM
#Last edited 4/13 11:20 A.M

from random import randint
from time import clock
from time import gmtime, strftime
from binascii import a2b_qp,hexlify

##==================================================================
##Transitions
global currentime
global month
global day
global hour
global minute

global January
global April
global May
global July
global October
global December

global HIGH
global LOW

#global DesiredNextState

January=1
April=4
May=5
July=7
October=10
December=12

currentime=strftime("%m-%d %H:%M:%S")
month=int(currentime[0:2])
day=int(currentime[3:5])
hour=int(currentime[6:8])
minute=int(currentime[9:11])

HIGH=1
LOW=0

#DesiredNextState=""


"""This class takes in a toState which is the string that says what state is next.

It has 2 functions. One does the actual transitioning, and an execute to visually see that a transition is happening.

*__init__ has
"""
def ASCII2BI(message):
    x=[]
    counter=0
    message_length=int(len(message))
    bi_code= bin(int(hexlify(message), 16))
    while counter!=message_length:
        x.append(bi_code[((message_length-1-counter)*8) : ((message_length-counter)*8)])
        counter+=1
    x.reverse()
    return x

def Battery_Life():
    """Psuedo-code:
            1) Read bits(37:40) of mate3 USB
            2) if above certain threshold return True
                if not return False
    """
    if randint(1, 50) >= 20:
        return HIGH
    else:
        return LOW
def GRID_HEALTHY():
    """ This will read bits(16:20) of the mate 3 USB"""
    if randint(1, 50) >= 20:
        return HIGH
    else:
        return LOW


class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print "Transitioning..."


##==================================================================
##States

"""
First we are going to create a state object.
This will govern the basic layout of each subsequent state object.


*__init__ is used as the arguments which a every state will need
*This way we can call State(FSM), and have this state be added to
*that specific instance of FSM
*@param FSM The finite state machine that this state will be a part of

*The enter function takes care of any event which we would want to occur
*when this state is initially transitioned into, such as turning on certain things

*The execute function takes care of any continous action which we want to continously check
*Like monitoring certain aspects of our system, and seeing if a transfer condition is met.
*and initiate the state transfer

*The Exit function serves the same purpose as the Enter function.
*This function takes care of any events which will need to be done during the
*exiting of a state transition.

In these we have a basic State, each state can alter the basic functions
to fit their needs, but all states will have these functions.

"""


class State(object):  # defines a state. Classes are analogous to "structs" in C.


    def __init__(self, FSM):  # initializes all state objects we create
        self.FSM = FSM
        self.timer = 0
        self.myTimer =0
        self.startTime = 0


    def Enter(self):  # if the command"
       # self.timer = randint(0, 5)
        #self.startTime = int(clock())
        print currentime
        print ASCII2BI('297')

    def Execute(self):
        global DesiredNextState
        DesiredNextState = ''

        if GRID_HEALTHY() == 0:
            print "Islanding"
            DesiredNextState="toState_3"
            #FSM1.ToTransition("toState_3")

        elif (month>=May and month<=October):
            print "It's Summer"
            if(hour==17 and Battery_Life()): #if it's 5:00 to 5:59(17=5pm)
                DesiredNextState="toState_5"
                #FSM1.ToTransition("toState_5")
            else:
                DesiredNextState="toState_6"
                #FSM1.ToTransition("toState_6")
        elif((month>October and month<=December) or (month>=January and month<=April)):
            print "It's Winter"
            if((hour==9) and Battery_Life()): # time is 9:00-9:30
                print "PG&E is $$$ and we have enough BAT"
                DesiredNextState="toState_5"
                #FSM1.ToTransition("toState_5")
            else:
                print "PG&E is not $$$ or bat is too low"
                DesiredNextState="toState_6"
                #FSM1.ToTransition("toState_6")
        else:
            print "battery is too low"
            FSM1.ToTransition("toState_6")

    def Exit(self):
        pass

"""
Skeleton state

This state serves as the skeleton for any State which is wished to be implemented.
Print statements are currently used to visibly see how this method works.

*The __init__ of these subclasses don't need anything different than what is
*provided in the State superclass described above. the call to super in the function
*Ensures that it merely inherits what the superclass has.
*@param FSM The finite state machine that this state will be a part of

*The Enter function also wants to inherit from the superclass, but you can add more to it,
*since each state is unique from the superclass which it comes from.
*In our case we announce that this is the entrance of a state.

*In the execute state we are going to put any continous actions, which include conditions checks.
*Here we also check if a transfer from a state to another is needed or not.
*To illustrate this we have an always true if statement, although this can be any condition you need

*The Exit() function is simply like the Enter() function, which you give commands in,
*To illustrate this I simply put in the put a message to indicate the exit of the state.

To make unique states, this skeleton must simply be copied, and renamed to the correct state.
Instead of being named "State_0" you could name it whatever you need for it to named.
Each function can also be altered.
This can be done for as many states as are necessary.
Make sure these get defined in the FSM later, or else they will never be used!

"""
class State_0(State):
    def __init__(self, FSM):
        super(State_0, self).__init__(FSM)

    def Enter(self):
        print "Entered State_0"
        super(State_0, self).Enter()

    def Execute(self):
        print "Executing State_0"
        super(State_0,self).Execute()
        FSM1.ToTransition("toState_6")

    def Exit(self):
        print "Exiting State_0"


class State_1(State):
    def __init__(self, FSM):
        super(State_1, self).__init__(FSM)

    def Enter(self):
        print "Entered State_1"
        super(State_1, self).Enter()

    def Execute(self):
        print "Executing State 1"
        super(State_1, self).Execute()
        FSM1.ToTransition("toState_6")
    def Exit(self):
        print "Exiting State_1"


class State_2(State):
    def __init__(self, FSM):
        super(State_2, self).__init__(FSM)

    def Enter(self):
        print "Entered State_2"
        super(State_2, self).Enter()

    def Execute(self):
        print "Executing State_2"
        super(State_2, self).Execute()
        FSM1.ToTransition("toState_6")

    def Exit(self):
        print "Exiting State_2"


class State_3(State):
    def __init__(self, FSM):
        super(State_3, self).__init__(FSM)

    def Enter(self):
        print "Entered State_3"
        super(State_3, self).Enter()

    def Execute(self):
        print "Executing State_3"
        while DesiredNextState == "toState_3":
            super(State_3, self).Execute()
        FSM1.ToTransition(DesiredNextState)
        # example transitions using the time which was made in the enter condition

    def Exit(self):
        print "Exiting State_3"


class State_4(State):
    def __init__(self, FSM):
        super(State_4, self).__init__(FSM)

    def Enter(self):
        print "Entered State_4"
        super(State_4, self).Enter()

    def Execute(self):
        print "Executing State_4"
        super(State_4, self).Execute()
        FSM1.ToTransition("toState_6")
        # example transitions using the time which was made in the enter condition

    def Exit(self):
        print "Exiting State_4"


class State_5(State):
    def __init__(self, FSM):
        super(State_5, self).__init__(FSM)

    def Enter(self):
        print "Entered State_5"
        super(State_5, self).Enter()

    def Execute(self):
        print "Executing State_5"
        # example transitions using the time which was made in the enter condition
        while DesiredNextState == "toState_5":
            super(State_5, self).Execute()
        FSM1.ToTransition(DesiredNextState)

    def Exit(self):
        print "Exiting State_5"


class State_6(State):
    def __init__(self, FSM):
        super(State_6, self).__init__(FSM)

    def Enter(self):
        print "Entered State_6"
        super(State_6, self).Enter()

    def Execute(self):
        print "Executing State_6"
        while DesiredNextState=="toState_6":
            super(State_6, self).Execute()
        if DesiredNextState == 'toState_3':
            print "About to go from S6 to S3" #this is where i will include code that changes state of switches.

        # example transitions using the time which was made in the enter condition
        FSM1.ToTransition(DesiredNextState)

    def Exit(self):
        print "Exiting State_6"


class State_7(State):
    def __init__(self, FSM):
        super(State_7, self).__init__(FSM)

    def Enter(self):
        print "Entered State_7"
        super(State_7, self).Enter()

    def Execute(self):
        print "Executing State_7"
        super(State_7, self).Execute()
        FSM1.ToTransition("toState_6")
        # example transitions using the time which was made in the enter condition

    def Exit(self):
        print "Exiting State_7"


##==================================================================
##FSM Implementation


"""
The FSM is completely defined in this class, and everything you need to step between states

*The __init__ function takes in a charachter class variable. This is not as important as everything else
*that happens in this function.
*First it declares the dictionaries which will hold all the names of the states, and all transitions.
*Then it initializes the variables which will hold the current state, and possibly the previous state if needed.
*And finally a variable which tells us when there is a transition which must be carried out
*@param charachter ???

*The AddTransition() function serves as a way to add to the transition dictionary, since we don't want the outside
*to control the variables in our class, and this makes it much cleaner when doing so.
*It takes in the transition name, as well as to where it is transitioning to.
*This way the name becomes the key in the dictionary for the state.
*@Param transName A string which names the transition, should be descriptive like "ToStateOne"
*@Param transition The name of the state to be transitioned to. We input this as Transition("StateName")
*                  so that it has access to some of the functions which are inside the Transition class.

*The AddState() function works in the same way as the AddTransition() does. It takes in a state name, as well as the actual state.
*Since each state is a class, we input that class in the state. This way the dictionary for states has a key
*which is the name of this state, and it points to the actual occurence of this state.
*@param stateName The string which describes the name of the state being input, Very important to match this up with the name
*                 Used in transition.
*@param transition This takes in a State Class corresponding to the string. An example would be the one used in this skeleton
*                  ThisState(FSM1), where FSM1 is the name of the FSM class instance we have created.

*The SetState() function is used to set a state, which means there is no transition. It simply is the first state,
*Which can be used for the initial state. It also saves the previous state. Used mostly during the Execute() function
*@Param stateName The string corresponding to the state which you want to set to. This will use the dictionary to point to correct place.

*The ToTransition() function set the trans variable to have a transition ready.
*It uses the name of a transition, to grab the correct transition from the dictionary holding this info.
*@Param toTrans A string which holds which transition is going to occur. Descriptive like "toThisState.

*The Execute() function is really important for our purposes. It first checks if there is a transition ready.
*If there is, then we execute the current state's exit function, then we execute the transition Execute() function
*Then we set the state to be the the state we are transitioning to. Then we execute the new states Enter() function
*And finally we clear the trans variable, so during subsequent executes, we dont do this transition unless it's what we want.
*Outside of this if statement we execute the Execute() function of the current state. So we execute() the state regardless of transition
"""

class FSM(object):
    def __init__(self, charachter):
        self.char = charachter
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None
        self.trans = None

    def AddTransition(self, transName, transition):
        self.transitions[transName] = transition

    def AddState(self, stateName, state):
        self.states[stateName] = state

    def SetState(self, stateName):
        self.prevState = self.curState
        self.curState = self.states[stateName]

    def ToTransition(self, toTrans):
        self.trans = self.transitions[toTrans]

    def Execute(self):
        if (self.trans):
            self.curState.Exit()
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.curState.Enter()
            self.trans = None
        self.curState.Execute()


##==================================================================
##Implementation

"""
This is equivalent to when we made the State superclass, but this time we didn't need the subclassess to inherit anything
Other than the fact that it is an oject. So we have a Char superclass, which inherits the traits of an object.
This is mostly to clean up the code, and know that this class is used to charachterize the FSM.
"""

Char = type("Char",(object,),{})



"""
This is a weird problem I have not yet solved. Usually this would be defined inside of the FSMApplication class,
But for some reason the code breaks at that point. It has something to do with unbounded functions.
My solution is to make the FSM class instance a global variable, instead of self contained, and this solves the problem.
As of now no problems have risen.
"""
FSM1=FSM(Char)

"""
In this class you charachterize the FSM, by defining the transitions, and the states.
It usually has the above code inside of the class, but an error, forced me to put it outside.
This class can be renamed to better fit the subject.

*In the __init__() function is where you define the states and transitions. Since this only occurs when a new
*class object is create.
*In this example you see the how to add a STATE, and a TRANSITION, and we will set the initial state.
*Keeping with this format, more states and transitions can be added

*Execute() function just is a wrapper function which calls the execute inside of the FSM.
*This is where all the magic happens, and states are run.
"""


class FSMApplication(Char):
    def __init__(self):
        #  self.FSM=FSM(self)

        ##STATES
        FSM1.AddState("State_0", State_0(FSM1))
        FSM1.AddState("State_1", State_1(FSM1))
        FSM1.AddState("State_2", State_2(FSM1))
        FSM1.AddState("State_3", State_3(FSM1))
        FSM1.AddState("State_4", State_4(FSM1))
        FSM1.AddState("State_5", State_5(FSM1))
        FSM1.AddState("State_6", State_6(FSM1))
        FSM1.AddState("State_7", State_7(FSM1))

        ##Transitions
        FSM1.AddTransition("toState_0", Transition("State_0"))
        FSM1.AddTransition("toState_1", Transition("State_1"))
        FSM1.AddTransition("toState_2", Transition("State_2"))
        FSM1.AddTransition("toState_3", Transition("State_3"))
        FSM1.AddTransition("toState_4", Transition("State_4"))
        FSM1.AddTransition("toState_5", Transition("State_5"))
        FSM1.AddTransition("toState_6", Transition("State_6"))
        FSM1.AddTransition("toState_7", Transition("State_7"))

        # Initial State
        FSM1.SetState("State_1")

    def Execute(self):
        # FSM1.ToTransition("toThisState")
        FSM1.Execute()


##==================================================================
##Implementation

if __name__ == '__main__':
    s = FSMApplication()
    s.Execute()
    s.Execute()
    while (1):
        s.Execute()
        pass

