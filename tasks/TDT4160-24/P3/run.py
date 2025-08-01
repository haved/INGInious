#!/bin/inginious-ipython

import random
import tdt4160

tdt4160.setcode(get_input("thecode"))

regs = {}
answer = {}

numbers = random.sample(range(256), 6)

for i in range(6):
    regs[10+i] = numbers[i]
    answer[10+i] = sorted(numbers)[i]

success, errormsg = tdt4160.runtest(regs, answer)

if success:
    set_global_result("success")
    set_global_feedback("**Programmet fungerer.**")
else:
    set_global_result("failed")
    set_global_feedback(errormsg)
    
