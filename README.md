infection_risk_calculator
In this project, We propose an infection risk algorithm which accepts building data and a set of parameters regarding occupants and infection rates of the surrounding community. Code and assumptions made in the algorithm will be clearly explained to users for transparency. The resulting algorithm will be referenced in our quarter 2 project.

Opening up the project
The source codes for the calculator are located in /src/calculator. To see the notebook containing the underlying logic and sample runnings for the calculator, open report in /notebooks. Note there are actual codes in the notebook, because the purpose of this project is to create an infection estimation algorithm that's clear to users and easily understanable by users. It's important to show what the algorithm does for each steps.

To use run.py in command line, input python run.py [targets].

We currently have the following targets available:

test: which runs the calculator using sample parameters.
More information about those sample runs can be found in the report notebooks mentioned above.

Responsibilities
Etienne Doidic built the structure and underlying logic of the calculator, and also the notebooks for walk through.
Nicholas Kho helped developing the calculator and migrated the codes to src and project structure.
Zhexu Li helped migrating the codes, updated the project structure and developed configs and run.py.
