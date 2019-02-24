"""
Homework01 part3  course-scheduling for CS 344 at Calvin College
@author: Chan kIm
@date: 02/22/2019
"""
from csp import CSP, parse_neighbors, min_conflicts, backtracking_search, AC3
from search import depth_first_graph_search

def scheduling(courses, faculties, times, rooms, assigned_faculty):
    domains = {}
    # to append all possible courses' cases to domains
    for course in courses:
        domains[course] = list()
        for faculty in faculties:
            for time in times:
                for room in rooms:
                    domains[course].append([faculty, time, room])

    # Pairing two courses each.
    neighbors = parse_neighbors("""cs108: cs112;
                cs112: cs212; cs212: cs214; cs214: cs384;
                cs384: cs232; cs232: cs344; cs344: cs108""", courses)
    for type in [courses]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    def scheduling_constraint(A, a, B, b, recurse=0):
        # each course should be offered exactly once by the assigned faculty member.
        if assigned_faculty[A] != a[0] and assigned_faculty[B] != b[0]:
            return False
        # a faculty member can only teach one thing at a time.
        if a[0] == b[0] and a[1] == b[1]:
            return False
        # a room can only have one class at each time.
        if a[1] == b[1] and a[2] == b[2]:
            return False
        return True
    return CSP(courses, domains, neighbors, scheduling_constraint)


courses = ['cs108', 'cs112', 'cs212', 'cs214', 'cs232', 'cs384', 'cs344']
faculty = ['Derek_Schuurman', 'Joel_Adams', 'Victor_Norman', 'Harry_Plantinga', 'Keith_Vander_Linden']
assigned_faculty = {'cs108': 'Derek_Schuurman', 'cs112': 'Joel_Adams', 'cs212': 'Harry_Plantinga',
                    'cs214': 'Joel_Adams', 'cs232': 'Victor_Norman', 'cs384': 'Derek_Schuurman',
                    'cs344': 'Keith_Vander_Linden'}
time = ['mwf0900', 'tth1030', 'mwf1430', 'tth1230', 'mwf1330']
room = ['nh253', 'sb382']


def print_solution(result):
    """A CSP solution printer copied from csp.py."""
    for h in courses:
        print('Course\t' + h)
        for (var, val) in result.items():
            if var == h: print('\t\t'+'\n\t\t'.join(val))


puzzle = scheduling(courses, faculty, time, room, assigned_faculty)

# result = depth_first_graph_search(puzzle)
# result = AC3(puzzle)
result = backtracking_search(puzzle)
# result = min_conflicts(puzzle, max_steps=1000)

if puzzle.goal_test(puzzle.infer_assignment()):
    print("Solution:\n")
    print_solution(result)
else:
    print("failed...")
    print(puzzle.curr_domains)
    puzzle.display(puzzle.infer_assignment())
