# MILP-Flowshop
MILP approach for flowshop scheduling optimization with Sequence dependent changeover

This is a submission for IE503 group assignment. 

Requirements - Pyomo, Cbc, plotly

This code develops an MILP model for a flow shop with sequence dependent changeover. It uses Pyomo to model MILP and Cbc solver to optimize it. It is necessary to have these both installed in order to successfully run the code. It also needs plotly to be installed to create a gantt chart.

Now, the flow of the code is explained. The code python file FlowshopOptimization.py creates an abstract model which is instantiated using the data.dat file. The data.dat file contains the parameters of the model such as the jobs, the machines, processing times and the changeover times. These are written in AMPL format. 

After the model has been instantiated, it uses constraints written in constraints.py python file and generates a concrete model. The model is then optimized using Cbc solver and the results are visualized in a gantt chart which is produced using plotly. 

To run the code, update the data.dat file and run the python file FlowshopOptimization.py.

