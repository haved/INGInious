#!/bin/inginious-ipython

n_correct = 0
n_tasks = 5

def check_matches(ids, answers):
    for (id, answer) in zip(ids, answers):
        try:
            student_input_string = get_input(id)
            student_input = int(student_input_string)
        except:
            set_problem_feedback("Feil format - ikke et heltall", id)
            correct = False
        else:
            correct = student_input == answer
        finally:
            if correct:
                set_problem_result("success", id)
                global n_correct
                n_correct += 1
            else:
                set_problem_result("failed", id)
        

def reflection():
    id = "reflection"
    character_limit = 20
    
    score = 1
    student_reflection = get_input(id)
    result = "success"
    if len(student_reflection) < character_limit:
        result = "failed"
        set_problem_feedback("Skriv litt mer :)", id)
        score = 0
        
    set_problem_result(result, id)
    global n_correct
    n_correct += score
    return


def main():
    check_matches(
        ["no_hazard_logic", "no_hazard_run", "hazard_check", "hazard_run"],
        [5, 5, 10, 55]
    )
    reflection()
    result = "failed"
    if n_correct >= n_tasks:
        result = "success"
    
    feedback = "Du fikk {} av {} riktige".format(n_correct, n_tasks)
    set_global_result(result)
    set_grade(100 * float(n_correct) / float(n_tasks))
    set_global_feedback(feedback)

    
if __name__ == "__main__":
    main()
