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
/puzzles              |  Directory to all exemplar puzzles used
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

