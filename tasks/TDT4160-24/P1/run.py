#!/bin/inginious-ipython

import random
import tdt4160

tdt4160.setcode(get_input("thecode"))

randomregs = {}
for reg in range(10,16):
    randomregs[reg] = random.randrange(10)

success = False

# test 10+11 is largest
regs = randomregs.copy()
regs[10] = random.randrange(100, 200)
answer = { 10: max([regs[10] + regs[11], regs[12] + regs[13], regs[14] + regs[15]]) }
testok, errormsg = tdt4160.runtest(regs, answer)

if testok:
    # test 12+13 is largest
    regs = randomregs.copy()
    regs[12] = random.randrange(100, 200)
    answer = { 10: max([regs[10] + regs[11], regs[12] + regs[13], regs[14] + regs[15]]) }
    testok, errormsg = tdt4160.runtest(regs, answer)

    if testok:
        # test 14+15 is largest
        regs = randomregs.copy()
        regs[14] = random.randrange(100, 200)
        answer = { 10: max([regs[10] + regs[11], regs[12] + regs[13], regs[14] + regs[15]]) }
        success, errormsg = tdt4160.runtest(regs, answer)

if success:
    set_global_result("success")
    set_global_feedback("**Programmet fungerer.**")
else:
    set_global_result("failed")
    set_global_feedback(errormsg)
    
