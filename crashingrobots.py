dirs = (     "N",    "W",     "S",     "E")
dirs_dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)] # yes, they match


def vis(robots, w, h):
    print(w, h, robots)
    for y in range(h, 0, -1):
        for x in range(1, w+1):
            robot = None
            for r in robots:
                if r[0] == [x, y]:
                    robot = r
                    break
            if robot:
                print(dirs[robot[1]], end=" ")
            else:
                print(".", end=" ")
        print("")


"""
The first line of input contains an integer 1≤K≤50, the number of test
cases. Each test case starts with one line consisting of two integers,
1≤A,B≤100, giving the size of the warehouse in meters. A is the length
in the EW-direction, and B in the NS-direction.
"""
for _ in range(int(input())):
    a, b = [int(s) for s in input().split()]
    """
    The second line contains two integers, 1≤N,M≤100, denoting the numbers
    of robots and instructions respectively.
    """
    n, m = [int(s) for s in input().split()]
    robots = []  # contains ((x, y), d)
    """
    Then follow N lines with two integers, 1≤Xi≤A,1≤Yi≤B and one letter
    (N, S, E or W), giving the starting position and direction of each
    robot, in order from 1 through N. No two robots start at the same
    position.
    """
    for robot in range(n):
        x, y, d = input().split()
        robots.append([[int(x), int(y)], dirs.index(d)])
    """
    Finally there are M lines, giving the instructions in sequential
    order. An instruction has the following format:
    <robot #> <action> <repeat>
    """
    crash = False
    for inst in range(m):
        i, action, repeat = input().split()
        if crash:
            continue
        i = int(i) - 1
        repeat = int(repeat)
        """
        Where <action> is one of L: turn left 90 degrees, R: turn right 90
        degrees, or F: move forward one meter, and 1≤<repeat>≤100 is the
        number of times the robot should perform this single move.
        """
        #vis(robots, a, b)
        if action == "L":
            robots[i][1] = (robots[i][1] + repeat) % 4
        elif action == "R":
            robots[i][1] = (robots[i][1] - repeat) % 4
        else:
            dxy = dirs_dxy[robots[i][1]]
            for step in range(repeat):
                robots[i][0][0] += dxy[0]
                robots[i][0][1] += dxy[1]
                for j, other_robot in enumerate(robots):
                    if i != j and robots[i][0] == other_robot[0]:
                        print(f"Robot {i+1} crashes into robot {j+1}")
                        crash = True
                        break
            x, y = robots[i][0]
            if not crash and (x < 1 or x > a or y < 1 or y > b):
                print(f"Robot {i+1} crashes into the wall")
                crash = True
        #vis(robots, a, b)
    if not crash:
        print("OK")

