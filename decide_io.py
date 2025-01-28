import GLOBAL_VARS as gv
from collections import deque
import re
import sys


def parse_input(queue : deque):
    # NUMPOINTS
    line = queue.popleft()
    print(gv.NUMPOINTS)
    gv.NUMPOINTS = int(line)
    print(gv.NUMPOINTS)
    # POINTS
    gv.POINTS = []
    for _ in range(gv.NUMPOINTS):
        line = queue.popleft()
        x, y = map(int, line.split())
        gv.POINTS.append((x,y))

    # PARAMETERS
    gv.PARAMETERS.LENGTH1 = float(queue.popleft())
    assert 0 <= gv.PARAMETERS.LENGTH1

    gv.PARAMETERS.RADIUS1 = float(queue.popleft())
    assert 0 <= gv.PARAMETERS.RADIUS1

    gv.PARAMETERS.EPSILON = float(queue.popleft())
    assert 0 <= gv.PARAMETERS.EPSILON and gv.PARAMETERS.EPSILON < gv.PI

    gv.PARAMETERS.AREA1 = float(queue.popleft())
    assert 0 <= gv.PARAMETERS.AREA1

    gv.PARAMETERS.Q_PTS = int(queue.popleft())
    assert 2 <= gv.PARAMETERS.Q_PTS <= gv.NUMPOINTS

    gv.PARAMETERS.QUADS = int(queue.popleft())
    assert 1 <= gv.PARAMETERS.QUADS <= 3

    gv.PARAMETERS.DIST = float(queue.popleft())
    assert 0 <= gv.PARAMETERS.DIST

    gv.PARAMETERS.N_PTS = int(queue.popleft())
    assert 3 <= gv.PARAMETERS.N_PTS <= gv.NUMPOINTS

    gv.PARAMETERS.K_PTS = int(queue.popleft())
    assert 1 <= gv.PARAMETERS.K_PTS <= gv.NUMPOINTS - 2

    gv.PARAMETERS.A_PTS = int(queue.popleft())
    gv.PARAMETERS.B_PTS = int(queue.popleft())
    assert 1 <= gv.PARAMETERS.A_PTS
    assert 1 <= gv.PARAMETERS.B_PTS
    assert gv.PARAMETERS.A_PTS + gv.PARAMETERS.B_PTS <= gv.NUMPOINTS - 3

    gv.PARAMETERS.C_PTS = int(queue.popleft())
    gv.PARAMETERS.D_PTS = int(queue.popleft())
    assert 1 <= gv.PARAMETERS.C_PTS
    assert 1 <= gv.PARAMETERS.D_PTS
    assert gv.PARAMETERS.C_PTS + gv.PARAMETERS.D_PTS <= gv.NUMPOINTS - 3

    gv.PARAMETERS.E_PTS = int(queue.popleft())
    gv.PARAMETERS.F_PTS = int(queue.popleft())
    assert 1 <= gv.PARAMETERS.E_PTS
    assert 1 <= gv.PARAMETERS.F_PTS
    assert gv.PARAMETERS.E_PTS + gv.PARAMETERS.F_PTS <= gv.NUMPOINTS - 3

    gv.PARAMETERS.G_PTS = int(queue.popleft())
    assert 1 <= gv.PARAMETERS.G_PTS <= gv.NUMPOINTS - 2 

    gv.PARAMETERS.LENGTH2 = float(queue.popleft())
    assert 0 <= gv.PARAMETERS.LENGTH2

    gv.PARAMETERS.RADIUS2 = float(queue.popleft())
    assert 0 <= gv.PARAMETERS.RADIUS2

    gv.PARAMETERS.AREA2 = float(queue.popleft())
    assert 0 <= gv.PARAMETERS.AREA2

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


def read_input(file):

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
        print("After parse_input:")
        print(f"NUMPOINTS: {gv.NUMPOINTS}")
        print(f"POINTS: {gv.POINTS}")
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

if __name__ == "__main__":
    if read_input() == 0:
        gv.test_values()
