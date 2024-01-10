import sys

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        grades = []

        for _ in range(N):
            paper_grade, interview_grade = map(int, sys.stdin.readline().split())
            grades.append((paper_grade, interview_grade))
        
        sorted_by_paper_grade = sorted(grades, key = lambda x: x[0])
        criteria_interview_grade = sorted_by_paper_grade[0][1]
        count = 1
        for (_, interview_grade) in sorted_by_paper_grade:
            if interview_grade < criteria_interview_grade:
                criteria_interview_grade = interview_grade
                count += 1
        
        print(count)

solution()