# File storing functionality to read values from file into global variables

from collections import deque
import re
import GLOBAL_VARS as gv

'''
Parses input file according to input specification and set global variables.
'''
def parse_input(queue : deque):
    # NUMPOINTS
    line = queue.popleft()
    gv.NUMPOINTS = int(line)

    # POINTS
    gv.POINTS = []
    for _ in range(gv.NUMPOINTS):
        line = queue.popleft()
        x, y = map(int, line.split())
        gv.POINTS.append((x,y))

    # PARAMETERS
    gv.PARAMETERS.LENGTH1 = float(queue.popleft())  

    gv.PARAMETERS.RADIUS1 = float(queue.popleft())

    gv.PARAMETERS.EPSILON = float(queue.popleft())

    gv.PARAMETERS.AREA1 = float(queue.popleft())

    gv.PARAMETERS.Q_PTS = int(queue.popleft())

    gv.PARAMETERS.QUADS = int(queue.popleft())

    gv.PARAMETERS.DIST = float(queue.popleft())

    gv.PARAMETERS.N_PTS = int(queue.popleft())

    gv.PARAMETERS.K_PTS = int(queue.popleft())

    gv.PARAMETERS.A_PTS = int(queue.popleft())
    gv.PARAMETERS.B_PTS = int(queue.popleft())

    gv.PARAMETERS.C_PTS = int(queue.popleft())
    gv.PARAMETERS.D_PTS = int(queue.popleft())

    gv.PARAMETERS.E_PTS = int(queue.popleft())
    gv.PARAMETERS.F_PTS = int(queue.popleft())

    gv.PARAMETERS.G_PTS = int(queue.popleft())

    gv.PARAMETERS.LENGTH2 = float(queue.popleft())

    gv.PARAMETERS.RADIUS2 = float(queue.popleft())

    gv.PARAMETERS.AREA2 = float(queue.popleft())

    # LCM
    for j in range(gv.LIC_COUNT):
        row = queue.popleft().split()
        if len(row) != gv.LIC_COUNT:
            raise ValueError

        gv.LCM.append([])
        for i in range(gv.LIC_COUNT):
            atom = row[i]

            if re.fullmatch("ANDD", atom):
                gv.LCM[j].append(gv.Connectors.ANDD)
            elif re.fullmatch("ORR", atom):
                gv.LCM[j].append(gv.Connectors.ORR)
            elif re.fullmatch("NOTUSED", atom):
                gv.LCM[j].append(gv.Connectors.NOTUSED)
            else:
                raise ValueError

    # PUV
    row = queue.popleft().split()
    if len(row) != gv.LIC_COUNT:
        raise ValueError

    for i in range(gv.LIC_COUNT):

        if re.fullmatch("TRUE", row[i]):
            gv.PUV.append(True)
        elif re.fullmatch("FALSE", row[i]):
            gv.PUV.append(False)
        else:
            raise ValueError

    # Make sure all input is parsed
    if len(queue) > 0:
        raise ValueError


''' 
Read content of a specific input file, parse it and set global variables.
'''
def read_input(file):

    try: 
        with open(file) as f:
            lines = f.readlines()

        # filter out comments, empty lines and remove newline characters
        lines = filter(
            lambda x : len( x.strip() ) > 0 and x[0] != '#', 
            map(
                lambda x : x.replace('\n', ''), 
                lines
            )
        )
        parse_input(deque(lines))
        
    except OSError:
        print("Error: failed to open file.")
        return -1
    except (ValueError, IndexError):
        print("Error: invalid input format.")
        return -1
    except (AssertionError):
        print("Error: entered values do not conform to requirements.")
        return -1

    return 0
