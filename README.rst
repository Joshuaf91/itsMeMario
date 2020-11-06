# Its Me Mario!
I'm Here to Kill Bowser and save Princess Peach!

Lets start by setting up the project.

## Set up

After installing python 3.8

    ``git clone https://github.com/Joshuaf91/itsMeMario.git``

    ``pip install virtualenv``

    ``cd itsMeMario #go to project folder``

    ``virtualenv itsMeMario #create the folder projectname``

    ``source itsMeMario/bin/activate``

    ``python save_princess_peach/entry.py``

## test case in the directory

    Test documents can be updated
    `here <https://github.com/Joshuaf91/itsMeMario/tree/main/tests/test_grids>`_ and the unit test
    for those files can be ran from
    `this location <https://github.com/Joshuaf91/itsMeMario/blob/main/tests/test.py>`_

Oh no! Bowser has Princess Peach! You must navigate the castle, defeat Bowser first and then rescue
the Princess while avoiding any hazards.

Input format:
The first line will contain an integer N (3<= N<= 100) that denotes the size of the matrix
Followed by an NxN grid. The Princess will be shown as a 'p', Bowser will be shown as a 'b',
the unnamed hero will be shown as an 'm'. '*' spaces are hazards and '-' spaces are clear to move into.

Output format:
The moves can be printed out to standard out and human readable, however you want to represent
them.
There are 4 valid moves, LEFT, RIGHT, UP, and DOWN

Task:
The input will come from STDIN(this will require reading in N+1 lines
from STDIN), and the output should be print to STDOUT.

Sample Input:

    ``7``

    ``-----p-``

    ``-*****-``

    ``--b----``

    ``**-----``

    ``-------``

    ``-******``

    ``--m----``

Sample Output:
LEFT, LEFT, UP, UP, RIGHT, RIGHT, UP, UP, RIGHT, RIGHT, RIGHT,
RIGHT, UP, UP, LEFT
