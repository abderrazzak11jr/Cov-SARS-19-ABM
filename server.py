
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter
from model import CovModel

def cov_draw(agent):
    portrayal = {"Shape": "circle", "r": 0.6, "Filled": "true"}
    if agent is None:
        return
    if agent.type == 0:
        portrayal["Color"] = ["#FFFF00", "#FFFFBB"]
        portrayal["Layer"] = 0
        if agent.port_mask==0:
            portrayal["r"] = 0.3
    if agent.type == 1 :
        portrayal["Color"] = ["#FF0000", "#FFBBBB"]
        portrayal["Layer"] = 0
        if agent.port_mask==0:
            portrayal["r"] = 0.3
    if  agent.type == -1 :
        portrayal["Color"] = ["#00FF00", "#BBFFBB"]
        portrayal["Layer"] = 0

    return portrayal


class Infecte(TextElement):
    def __init__(self):
        pass

    def render(self, model):
        return "agents infectes: " + str(model.infecte)

class Suceptible(TextElement):
    def __init__(self):
        pass

    def render(self, model):
        return "agents suceptibles: " + str(model.sucep)

class Retabli(TextElement):
    def __init__(self):
        pass

    def render(self, model):
        return "agents retablis: " + str(model.retab)

canvas_element = CanvasGrid(cov_draw, 20, 20, 500, 500)
infecte_element=Infecte()
sucep_element=Suceptible()
retab_element=Retabli()
all_chart = ChartModule([{"Label": "infecte", "Color": "red"},{"Label": "suceptible", "Color": "yellow"},{"Label": "retabli", "Color": "green"}], data_collector_name='datacollector')
model_params = {
                        "height": 20,
                        "width": 20,
                        "density": UserSettableParameter("slider", "Agent density", 0.8, 0.1, 1.0, 0.1),
                        "minority_pc": UserSettableParameter(
                            "slider", "Fraction des infectes", 0.2, 0.00, 1.0, 0.05),
                        "d_pm": UserSettableParameter("slider", "Fraction des porteurs du mask", 0.8, 0.1, 1.0, 0.1),
}
server = ModularServer(CovModel,
                       [canvas_element, infecte_element,sucep_element,retab_element,all_chart],
                       "Covid 19 Model",
                      model_params
                        )
