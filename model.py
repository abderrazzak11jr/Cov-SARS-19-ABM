from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
import random

class CovAgent(Agent):

    def __init__(self, pos, model, agent_type,port_mask,immune,prob_inf=None,temps_inf=None):
        #agent_type: Indicator for the agent's type (suceptible=0, infecte=1,retabli=-1)
        super().__init__(pos, model)
        self.pos = pos
        self.type = agent_type
        self.port_mask = port_mask
        self.immune = immune
        self.prob_inf = prob_inf
        self.temps_inf = temps_inf

    def step(self):
        self.sucep2infect()
        self.infect2retab()
        if self.type== 1:
            self.model.infecte+=1
            self.model.grid.move_to_empty(self)
        if self.type== 0:
            self.model.grid.move_to_empty(self)
            self.model.sucep+=1
        if self.type== -1:
            self.model.retab+=1



    def sucep2infect(self):
        prob_inff=self.prob_inf
        if self.type==1 :
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                if neighbor.type==0:
                    if self.port_mask==1 and neighbor.port_mask==1 :
                        prob_inff-=prob_inff*0.985
                    if self.port_mask==1 and neighbor.port_mask==0 :
                        prob_inff-=prob_inff*0.95
                    if self.port_mask==0 and neighbor.port_mask==1 :
                        prob_inff-=prob_inff*0.3
                    if prob_inff>neighbor.immune:
                        neighbor.type=1
                        neighbor.immune=None
                        neighbor.prob_inf=random.uniform(0,1)
                        neighbor.temps_inf=random.randint(5,15)
    def infect2retab(self):
        if self.type==1:
            if self.model.runs>self.temps_inf:
                self.type=-1
                self.immune=1



class CovModel(Model):

    def __init__(self, height=5, width=5, density=0.8, minority_pc=0.2,d_pm=0.8):
        self.height = height
        self.width = width
        self.density = density
        self.minority_pc = minority_pc
        self.d_pm = d_pm
        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(width, height, torus=True)
        self.infecte = 0
        self.sucep=0
        self.retab=0
        self.runs=0
        self.datacollector = DataCollector(model_reporters={"infecte": "infecte","suceptible": "sucep","retabli": "retab"})
        for cell in self.grid.coord_iter():
            cell_content, x, y = cell
            if self.random.random() < self.density:
                if self.random.random() < self.minority_pc:
                    agent = CovAgent((x, y), self, 1,0,None,random.uniform(0,1),random.uniform(5,15))
                    self.infecte+=1
                else:
                    agent = CovAgent((x, y), self, 0,0,random.uniform(0,1))
                    self.sucep+=1
                if self.random.random() < self.d_pm:
                    agent.port_mask=1

                self.grid.position_agent(agent, (x, y))
                self.schedule.add(agent)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.runs+=1
        self.infecte = 0
        self.sucep = 0
        self.retab = 0
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)
        if self.infecte == 0:
            self.running = False
