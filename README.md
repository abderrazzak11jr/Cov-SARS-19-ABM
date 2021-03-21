# Cov-SARS-19-ABM
covid sars 19 agent-based-model
## SUMMARY
<br>  The Covid Sars 19 dispersion model belong to classical pandemic dispersion agent-based model, demonstrating how even a mild infected fraction of agents can lead to a much higher numbers of infected peoples in case of lack of controlling procedures .
<br>

<br>
The model consists of agents on a square grid, where each grid cell can contain at most one agent. Agents come in three colors: red, yellow and green. 
  At the beginning, agents are either susceptible(green) or infected (red). A susceptible agent can become infected only if one of its neighbors is infected and its immune is less than probability of inection of the sick agent. The values of those two variables depends if whether the agent (green or red) is wearing a mask (big circles).
<br>

<br>
  The infected agents become recovered after a certain number of model runs (5 to 15), average days to get recovered from the virus. if the quarantine option is not applied all types of agents can move freely inside the grid.The model keeps running until all agents get recovered.<br>
  

## Files

<br> run.py: Launches a model visualization server.<br>
<br> model.py: Contains the agent class, and the overall model class.<br>
<br> server.py: Defines classes for visualizing the model in the browser via Mesa's modular server, and instantiates a visualization server.<br>

