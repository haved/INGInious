#!/bin/inginious-ipython

import math

# 1
def demo():
    correct = 0
    id = "demo"
    
    random1 = int(get_input("@random")[0]*100)
    random2 = random1 + int(get_input("@random")[1]*100)
    # DEMO
    try:
        student = int(get_input(id))

    except:
        set_problem_result("failed", id)
        set_problem_feedback("Du har skrevet en ugyldig verdi.  Kun heltall aksepteres.", id)

    else:
        solution = random2 - random1

        if student == solution:
            set_problem_result("success", id)
            set_problem_feedback("**Riktig**", id)
            correct = 1
        else:
            set_problem_result("failed", id)
            set_problem_feedback("Feil - prøv igjen", id)
    
    finally:
        return correct
    

# 2
def cpi():
    id = "cpi"
    correct = 0
    
    t1 = int(get_input("@random")[0]*50) + 50
    t2 = int(t1 / (1 + get_input("@random")[1]))
    # CPI
    try:
        raw_input = get_input(id)
        student = float(raw_input)
        student_string = str(student)

    except:
        set_problem_result("failed", id)
        set_problem_feedback("Kun desimaltall aksepteres.", id)

    else:
        decimal_place_list = student_string.split('.')
        if len(decimal_place_list) < 2 or len(decimal_place_list[1]) != 1:
            set_problem_result("failed", id)
            set_problem_feedback("Feil format på desimaltall. Husk bare en desimal bak komma.", id)
            return 0
        
        solution = int(10 * t1 / t2) / 10
        ok = student == solution
        if ok:
            set_problem_result("success", id)
            set_problem_feedback("**Riktig**", id)
            correct = 1
        else:
            set_problem_result("failed", id)
            set_problem_feedback("Feil - prøv igjen", id)
    finally:
        return correct


# 3
def performance():
    id = "performance"
    correct = 0
    
    alice_t = int(get_input("@random")[2]*60) + 60
    bob_t = int(get_input("@random")[3]*60) + 180
    
    solution = int(10 * bob_t / alice_t) / 10
    #debug = "Bob: {}, Alice: {}, Sol: {}".format(alice_t, bob_t, solution)
    #print(debug)
    
    try:
        raw_input = get_input(id)
        student = float(raw_input)
        student_string = str(student)
    except:
        set_problem_result("failed", id)
        set_problem_feedback("Kun desimaltall aksepteres.", id)
    else:
        decimal_place_list = student_string.split('.')
        if len(decimal_place_list) < 2 or len(decimal_place_list[1]) > 1:
            set_problem_result("failed", id)
            set_problem_feedback("Feil format på desimaltall. Husk bare en desimal bak komma.", id)
            return 0
        
        ok = student == solution
        if ok:
            set_problem_result("success", id)
            set_problem_feedback("**Riktig**", id)
            correct = 1
        else:
            set_problem_result("failed", id)
            set_problem_feedback("Feil - prøv igjen", id)
    finally:
        return correct
    
# 4
def speedup():
    id = "speedup"
    correct = 0
    
    alice_t = int(get_input("@random")[4]*45) + 15
    
    solution = float(alice_t) / 2
    
    try:
        raw_input = get_input(id)
        student = float(raw_input)
        student_string = str(student)
    except:
        set_problem_result("failed", id)
        set_problem_feedback("Kun desimaltall aksepteres.", id)
    else:
        decimal_place_list = student_string.split('.')
        if len(decimal_place_list) < 2 or len(decimal_place_list[1]) > 1:
            set_problem_result("failed", id)
            set_problem_feedback("Feil format på desimaltall. Husk bare en desimal bak komma.", id)
            return 0
        
        ok = student == solution
        if ok:
            set_problem_result("success", id)
            set_problem_feedback("**Riktig**", id)
            correct = 1
        else:
            set_problem_result("failed", id)
            set_problem_feedback("Feil - prøv igjen", id)
    finally:
        return correct

# 5
def clock_f():
    id = "klokkefrekvens"
    correct = 0
    
    c = int(10 * (2 + get_input("@random")[5])) / 10.0
    solution = int(1000 / c)
    
    try:
        raw_input = get_input(id)
        student = int(raw_input)
    except:
        set_problem_result("failed", id)
        set_problem_feedback("Kun heltall aksepteres.", id)
    else:
        ok = student == solution
        if ok:
            set_problem_result("success", id)
            set_problem_feedback("**Riktig**", id)
            correct = 1
        else:
            set_problem_result("failed", id)
            set_problem_feedback("Feil - prøv igjen", id)
    finally:
        return correct
    
       
# 6
def time_t():
    id = "time"
    correct = 0
    
    old_c = int(10 * (1 + get_input("@random")[6])) / 10.0
    solution = int(old_c * 300 * 0.8 / 3)
    
    try:
        raw_input = get_input(id)
        student = int(raw_input)
    except:
        set_problem_result("failed", id)
        set_problem_feedback("Kun heltall aksepteres.", id)
    else:
        ok = student == solution
        if ok:
            set_problem_result("success", id)
            set_problem_feedback("**Riktig**", id)
            correct = 1
        else:
            set_problem_result("failed", id)
            set_problem_feedback("Feil - prøv igjen", id)
    finally:
        return correct    


# 7
def fastest():
    id = "fastest"
    correct = 0
    
    solution = ["BOB", 2.0]
                
    raw_input = get_input(id)
    tokens = raw_input.split('\n')
    if len(tokens) < 2:
        set_problem_result("failed", id)
        set_problem_feedback("Fyll ut minst to linjer", id)
        return 0
    
    name = tokens[0].strip().upper()
    try:
        raw_input = tokens[1]
        student = float(raw_input)
        student_string = str(student)
    except:
        set_problem_result("failed", id)
        message = "På linje 2 har du skrevet '{}', og dette er ikke et desimaltall".format(tokens[1])
        set_problem_feedback(message, id)
    else:
        decimal_place_list = student_string.split('.')
        if len(decimal_place_list) < 2 or len(decimal_place_list[1]) > 1:
            set_problem_result("failed", id)
            set_problem_feedback("Feil format på desimaltall. Husk bare en desimal bak komma.", id)
            return 0
        
        for (a, b) in zip([name, student], solution):
            if a != b:
                set_problem_result("failed", id)
                set_problem_feedback("Minst et svar er feil", id)
                return 0
        
        set_problem_result("success", id)
        set_problem_feedback("**Riktig**", id)
        correct = 1
    finally:
        return correct


# 8
def avg_cpi():
    id = "averagecpi"
    correct = 0
    
    twentyp = int(3 * get_input("@random")[7] + 2)
    
    solution = int(10 *(0.6 + 0.2 * twentyp + 0.15 * 5 + 0.05 * 100)) / 10.0
    
    try:
        raw_input = get_input(id)
        student = float(raw_input)
        student_string = str(student)
    except:
        set_problem_result("failed", id)
        set_problem_feedback("Kun desimaltall aksepteres.", id)
    else:
        decimal_place_list = student_string.split('.')
        if len(decimal_place_list) < 2 or len(decimal_place_list[1]) > 1:
            set_problem_result("failed", id)
            set_problem_feedback("Feil format på desimaltall. Husk bare en desimal bak komma.", id)
            return 0
        
        ok = student == solution
        if ok:
            set_problem_result("success", id)
            set_problem_feedback("**Riktig**", id)
            correct = 1
        else:
            set_problem_result("failed", id)
            set_problem_feedback("Feil - prøv igjen", id)
    finally:
        return correct


def main():
    n_correct = 0
    n_tasks = 8
    
    n_correct += demo()
    n_correct += cpi()
    n_correct += performance()
    n_correct += speedup()
    n_correct += clock_f()
    n_correct += time_t()
    n_correct += fastest()
    n_correct += avg_cpi()
    result = "failed"
    if n_correct >= n_tasks:
        result = "success"
    
    feedback = "Du fikk {} av {} riktige".format(n_correct, n_tasks)
    set_global_result(result)
    set_grade(100 * float(n_correct) / float(n_tasks))
    set_global_feedback(feedback)
    

if __name__ == "__main__":
    main()
