from collections import deque
import sys
import GLOBAL_VARS as gv

def parse_input(queue : deque):
    # NUMPOINTS
    gv.NUMPOINTS = int(queue.popleft())

    # POINTS
    gv.POINTS = []
    for _ in range(gv.NUMPOINTS):
        x, y = map(int, queue.popleft().split())
        gv.POINTS.append((x,y))

    # PARAMETERS
    gv.PARAMETERS.LENGTH1 = int(queue.popleft())
    gv.PARAMETERS.RADIUS1 = int(queue.popleft())
    gv.PARAMETERS.EPSILON = int(queue.popleft())
    gv.PARAMETERS.AREA1 = int(queue.popleft())
    gv.PARAMETERS.Q_PTS = int(queue.popleft())
    gv.PARAMETERS.QUADS = int(queue.popleft())
    gv.PARAMETERS.DIST = int(queue.popleft())
    gv.PARAMETERS.N_PTS = int(queue.popleft())
    gv.PARAMETERS.K_PTS = int(queue.popleft())
    gv.PARAMETERS.A_PTS = int(queue.popleft())
    gv.PARAMETERS.B_PTS = int(queue.popleft())
    gv.PARAMETERS.C_PTS = int(queue.popleft())
    gv.PARAMETERS.D_PTS = int(queue.popleft())
    gv.PARAMETERS.E_PTS = int(queue.popleft())
    gv.PARAMETERS.F_PTS = int(queue.popleft())
    gv.PARAMETERS.G_PTS = int(queue.popleft())
    gv.PARAMETERS.LENGTH2 = int(queue.popleft())
    gv.PARAMETERS.RADIUS2 = int(queue.popleft())
    gv.PARAMETERS.AREA2 = int(queue.popleft())

    # LCM
    for j in range(15):
        row = queue.popleft().replace('\n','').split()
        gv.LCM.append([])
        for i in range(15):
            atom = row[i]

            if atom == "ANDD":
                gv.LCM[j].append(gv.Connectors.ANDD)
            elif atom == "ORR":
                gv.LCM[j].append(gv.Connectors.ORR)
            elif atom == "NOTUSED":
                gv.LCM[j].append(gv.Connectors.NOTUSED)
            else:
                raise ValueError

    # PUV
    row = queue.popleft().replace('\n','').split()
    for i in range(15):

        if row[i] == "TRUE":
            gv.FUV.append(True)
        elif row[i] == "FALSE":
            gv.FUV.append(False)
        else:
            raise ValueError


def read_input():
    if len(sys.argv) != 2:
        print("Usage: python3 decide.py input_file")

    file = sys.argv[1]
    
    try: 
        with open(file) as f:
            lines = f.readlines()

        assert len(lines) < 1000 # might move to global variable
        # filter ount comments and empty lines
        lines = filter( 
            lambda x : len(x) > 0 and x[0] != '#' and x[0] != '\n', 
            map(
                lambda x : x.replace('\n', ''), 
                lines
            )
        )
        parse_input(deque(lines))
    except OSError:
        print("Error: file not found")
    except UnboundLocalError:
        print("Error: Failed reading any data")

    gv.test_values()

    return 0

if __name__ == "__main__":
    read_input()
