#!/bin/inginious-ipython

import random
import tdt4160

tdt4160.setcode(get_input("thecode"))

regs = {}
answer = {}

success = True

for num in [random.randrange(32)**2, (random.randrange(32)**2)+1]:
    # random input in x10
    regs[10] = num

    # find all divisors
    divisors = [x for x in range(1, regs[10]) if regs[10] % x == 0]

    # set x10 to max divisor
    answer[10] = max(divisors)

    # check if any of the divisors squared equals x10
    answer[11] = 0
    for div in divisors:
        if div * div == regs[10]:
            answer[11] = 1
            break

    success, errormsg = tdt4160.runtest(regs, answer)

    if not success:
        break

if success:
    set_global_result("success")
    set_global_feedback("**Programmet fungerer.**")
else:
    set_global_result("failed")
    set_global_feedback(errormsg)
    
