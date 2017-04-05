# SUD-and-SAT
CSC320 Project Submission. For an easier to read README  please use the README.md as opposed to the README.txt

## Team Members
Samuel Allegretto-Smith | Eric Hedlin | Jasmine Yadeta | Richard Lui

University of Victoria | CSC 320 | Spring 2017

Professor: Bruce Kapron
Section: A01

## Contact Information
#### <i class="icon-pencil"></i> Samuel Allegretto-Smith (V#)
samueljohn@shaw.ca
#### <i class="icon-pencil"></i> Eric Hedlin (V#)
iamerichedlin@gmail.com
#### <i class="icon-pencil"></i> Jasmine Yadeta (V#)
jasmine.yadeta@gmail.com
#### <i class="icon-pencil"></i> Richard Lui (V#)
luir@uvic.ca


## Documents Submitted:


File Name             | Description
---------------       | ------------------
Sud2Sat.py            |  Reads a sudouku puzzle and converts it to CNF to be inputed into miniSAT           
Sat2Sud.py            |  Reads output produced by miniSAT and converts it back into a readable form              
/puzzles              |  Directory to all exemplar puzzles used
SudokuSatReport.pdf   |  The report and documentation of this project with output and time analysis

## Execution
Requires python 2.7.13 or higher and, miniSAT solver

An input of a partially unsolved sudouku puzzle

Gives an output of a solved board through the use of both sud2sat.py and sat2sud.py

Extended tasks enable the ability to solve "harder puzzles", attempt nxn boards, and compares extending encoding to the previously used minimal encoding
