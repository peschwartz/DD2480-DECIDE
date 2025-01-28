from collections import deque
import re
import sys
import GLOBAL_VARS as gv


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
            gv.FUV.append(True)
        elif re.fullmatch("FALSE", row[i]):
            gv.FUV.append(False)
        else:
            raise ValueError

    # Make sure all input is parsed
    if len(queue) > 0:
        raise ValueError


def read_input():
    if len(sys.argv) != 2:
        print("Usage: python3 decide.py input_file")
        return -1

    file = sys.argv[1]

    try: 
        with open(file) as f:
            lines = f.readlines()

        # Seems safe to check input length, maybe unnecessary?
        assert len(lines) < gv.INPUT_LINE_MAX
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
        print("Error: failed to open file")
        return -1
    except (ValueError, IndexError):
        print("Error: invalid input")
        return -1


    return 0

if __name__ == "__main__":
    if read_input() == 0:
        gv.test_values()
