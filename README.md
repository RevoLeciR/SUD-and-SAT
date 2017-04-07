# SUD-and-SAT
CSC320 Project Submission. For an easier to read README  please use the README.md as opposed to the README.txt

## Team Members
Samuel Allegretto-Smith | Eric Hedlin | Jasmine Yadeta | Richard Lui

University of Victoria | CSC 320 | Spring 2017

Professor: Bruce Kapron

Section: A01

## Contact Information
#### <i class="icon-pencil"></i> Samuel Allegretto-Smith (V00822198)
samueljohn@shaw.ca
#### <i class="icon-pencil"></i> Eric Hedlin (V00744896)
iamerichedlin@gmail.com
#### <i class="icon-pencil"></i> Jasmine Yadeta (V00804739)
jasmine.yadeta@gmail.com
#### <i class="icon-pencil"></i> Richard Lui (V00221256)
luir@uvic.ca


## Documents Submitted:


File Name             | Description
---------------       | ------------------
Sud2Sat.py            |  Reads a sudouku puzzle and converts it to CNF to be inputed into miniSAT           
Sat2Sud.py            |  Reads output produced by miniSAT and converts it back into a readable form              
basic_grids.txt       |  Text file of the basic grids from projecteuler.net/project/resources/p096
hard_grids.txt        |  Text file of the "hard" inputs from magictour.free.fr/top95
4x4_board.txt         |  Text file of a 4x4 Sudoku board. For Extended Tasks.
SudokuSatReport.pdf   |  The report and documentation of this project with output and time analysis

## Execution
Requires python 2.7.13 or higher and, miniSAT solver that can be downloaded at http://minisat.se/MiniSat.html

An input of a partially unsolved sudouku puzzle

Gives an output of a solved board through the use of both sud2sat.py and sat2sud.py

Extended tasks enable the ability to solve "harder puzzles", attempt nxn boards, and compares extending encoding to the previously used minimal encoding

Sat2sud.py takes in a text file that contains the sudoku puzzle is the following n by n format

Grid 01

003020600

900305001

001806400

008102900

700000008

006708200

002609500

800203009

005010300

For more than one puzzle at a time - 

Grid 01

003020600

900305001

001806400

008102900

700000008

006708200

002609500

800203009

005010300


Grid 02

200080300

060070084

030500209

000105408

000000000

402706000

301007040

720040060

004010003

 
The 0's represent empty spots in the puzzle, and can be any other character except the integers between and including 1-9. To run sud2sat, type “python sud2sat.py p096_sudoku.txt > out.txt” into the command line. p096_sudoku.txt is the file containing the puzzles and out.txt is the file that will have the CNF formulas printed to it. Next, to solve the CNF in out.txt use the miniSAT solver by typing in “minisat out.txt solved.txt” into the command line. Solved.txt will be the txt file containing the CNFs for the solved sudoku puzzles. To convert back to a solved sudoku puzzle use the command line argument “python sat2sud.py solved.txt > solvedsudoku.txt”. This will make a text file named solvedsudoku which contains the solved sudoku puzzle(s). 

## BASIC TASK: How to Execute sud2sat.py and sat2sud.py
To execute sud2sat.py
$ python sud2sat.py [input file]
Attached to this zip file, basic_grids.txt is the provided input file. Upon executing the command line above, you will be prompt to name a folder where the miniSAT encodings will be stored. The file names of the miniSAT encodings are in the form "Gridxx_SATencoded.txt", where xx is a 2 digit number.
NOTE: You cannot name a folder that already exists in the directory.

To execute sat2sud.py
$ python sat2sud.py
Upon executing the command line above, you will be prompt to name a folder that has miniSAT encodings in it. The solutions to the boards will be stored into the same folder. the file names of the board solutions are in the form "Solutionxx.txt", where xx is a 2 digit number

## EXTENDED TASK 1 and 2: Alternative to minimal encoding: Extended encoding to hard inputs
To execute sud2sat_extended.py
$ python sud2sat_extended.py [input file]
Attach to this zip file, hard_grids is the provided input file. Upon executing the command line above, you will be prompt to name a folder where the miniSAT encodings will be stored. The file names of the miniSAT encodings are in the form "Gridxx_SATencoded.txt", where xx is a 2 digit number.
NOTE: You cannot name a folder that already exists in the directory.

## EXTENDED TASK 3: nxn-size boards
Use sud2sat_extended.py
$ python sud2sat_extended.py [input file]
Attach to this zip file, 4x4_board is the provided input file.Upon executing the command line above, you will be prompt to name a folder where the miniSAT encodings will be stored. The file names of the miniSAT encodings are in the form "Gridxx_SATencoded.txt", where xx is a 2 digit number.
NOTE: You cannot name a folder that already exists in the directory.
