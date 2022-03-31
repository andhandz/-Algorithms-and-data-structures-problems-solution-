#Mamy dany zbiór zadań T = {t 1 , . . . , t n }. Każde zadanie t i
#dodatkowo posiada: (a) termin wykonania d(t i ) (liczba naturalna) oraz (b) zysk g(t i ) za wykonanie w
#terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie t i zostanie
#wykonane przed przekroczeniem swojego terminu d(t i ), to dostajemy za nie nagrodę g(t i ) (pierwsze wybrane
#zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
#Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi
#do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.

def task(A):
    n = len(A)
    A.sort(key=lambda a: a[2], reverse=True)

    maxDeadline = A[0][1]
    for i in range(1, n):
        if A[i][1] > maxDeadline:
            maxDeadline = A[i][1]

    t = [None] * maxDeadline

    for i in range(n):
        lastMoment = A[i][1] - 1

        for j in range(lastMoment, -1, -1):
            if t[j] == None:
                t[j] = A[i][0]
                break

    return t
