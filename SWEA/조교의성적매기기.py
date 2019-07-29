testcase = int(input())


for case in range(testcase):
    grade = []
    # 학생의 성적을 중간, 기말, 수행으로 나눠서 저장
    students, k = map(int, input().split())
    k_total = 0
    for student in range(students):
        midterm, finals, performance = map(int,input().split())

        # 저장한 점수들을 가지고 총점을 계산
        total = midterm * 0.35 + finals * 0.45 + performance * 0.20

        # 계산한 총점을 빈 리스트에 저장
        grade.append(total)

        # 총점들을 저장한 리스트를 정렬하고, k의 성적이 몇번째인지 확인한다.
        if student + 1 == k:
            k_total = total

    grade = sorted(grade)[::-1]
    k_score = grade.index(k_total)

    if k_score < students / 10:
        k_grade = 'A+'
    elif k_score < 2 * students / 10:
        k_grade = 'A0'
    elif k_score < 3 * students / 10:
        k_grade = 'A-'
    elif k_score < 4 * students / 10:
        k_grade = 'B+'
    elif k_score < 5 * students / 10:
        k_grade = 'B0'
    elif k_score < 6 * students / 10:
        k_grade = 'B-'
    elif k_score < 7 * students / 10:
        k_grade = 'C+'
    elif k_score < 8 * students / 10:
        k_grade = 'C0'
    elif k_score < 9 * students / 10:
        k_grade = 'C-'
    else:
        k_grade = 'D0'

    print(f'#{case+1} {k_grade}')