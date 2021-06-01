''' A BASIC REINFORCEMENT LEARNING PROBLEM DEPECTING A SNAKE - RACE PROBLEM
Outputs: 
1. Observation = [ x , y , z ] where x , y, z are the float values depecting the behaviour of the probability of transation function.
2. Action= [a,b,c] where a=1 -> LEFT TURN ,  b=1 depict-> NO TURN , c=1-> RIGHT TURN. 
3. TOTAL REWARD GAINED AT THE END OF RACE. 

'''
import random 
from typing import List 

class SampleEnvironment: 
        def __init__ (self) : 
            self. steps_left = 10

        def get_observations(self)->List[float] : 
            self.my_observation= random.randint(1, 100)
            observed_value=float(self.my_observation)
            if(self.my_observation<=33):
                return[observed_value,0.0,0.0]
            elif (self.my_observation>=33 and self.my_observation<=66):
                return[0.0,observed_value,0.0]
            else:
                return [0.0, 0.0, observed_value] 


        def get_actions(self)->List[int]: 
            if(self.my_observation<=33):
                return [1,0,0]
            elif (self.my_observation>=33 and self.my_observation<=66):
                return[0,1,0]
            else:
                return [0,0,1]

        def is_done(self) -> bool: 
            return self. steps_left == 0
 
        def action(self, action: int)-> float: 
            if self. is_done(): 
                raise Exception("Game is over") 
            self. steps_left -=1 
            return random. random() 

class Agent:
    def __init__(self) -> None:
        self.total_reward=0.0

    def step(self,env: SampleEnvironment):
        current_obs=env.get_observations()
        print("Current Observation :  {} ".format(current_obs))
        actions= env.get_actions()
        if(actions==[0,1,0]):
            print("Current Action :  {} : NO TURN ".format(actions))
        elif(actions==[1,0,0]):
            print("Current Action :  {} : LEFT TURN ".format(actions))
        else:
            print("Current Action :  {} : RIGHT TURN ".format(actions))
        reward= env.action(random.choice(actions))
        self.total_reward += reward
        print("Reward collected...")
        print("State Changed... \n")


if __name__=="__main__":
    env = SampleEnvironment()
    agent=Agent()
    i=1
    while not env.is_done():
        print("STEP : ",i)
        i+=1
        agent.step(env)

    print("TOTAL REWARD AT THE END OF GAME IS : %.4f" %agent.total_reward)