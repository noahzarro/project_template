# Modeling and Simulation of Social Systems Fall 2018 – Research Plan (Template)
(text between brackets to be removed)

> * Group Name: JosuNo
> * Group participants names: Josua Graf, Noah Zarro
> * Project Title: desert ant navigation
> * Programming language: Python

## General Introduction

Humans would get completly lost if you let them walk in the desert for some time, but ants with a only 0.1 mg brain solve the task of finding home with ease. It would be great if we could adapt parts of their navigation skills.

## The Model

With our model we want to measure how much an ant relies on known landmarks for it's orientation in relation to its 'global vector' an estimation of its position based on its movement. We want to program the behaviour of a desert ant, and implement the model of Wehner, proposed in his thesis. Than we can compare our simulated results to his experimental data.

## Fundamental Questions

Is the model proposed by Wehner correct?
What dominates the ants navigation, the global or local vector?

## Expected Results

We suppose that our simulated data will be similar to the experimental data of Wehner. We expect, that the ants mainly use the 'global vector' as a base for their orientation.

## References 

https://www.ethz.ch/content/dam/ethz/special-interest/gess/computational-social-science-dam/documents/education/Fall2015/matlab/projects/21-Desert_Ant_Behavior.zip


## Research Methods

Agent-Based Model, but we are not yet sure

## Other


# Reproducibility

0. git clone https://github.com/noahzarro/project_template
1. install numphy and matplotlib: python -m pip install numpy matplotlib
2. run code/Main.py, a graph opens, showing the path several ants took with the testcase Ba as described in the report:
   python project_template/code/Main.py
3. (full Test) If you want to change the testcase, just change line 12 in code\Config.py to whatever testfile you want. All possible testfiles lay in the folder code.

