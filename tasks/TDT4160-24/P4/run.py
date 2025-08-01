#!/bin/inginious-ipython

import random
import tdt4160

def mswl32(seed, seq):
    seed *= seed
    seq = (seq + 0xb5ad4ece) & 0xffffffff
    seed = (seed + seq) & 0xffffffff
    seed = ((seed << 16) | (seed >> 16)) & 0xffff
    return (seed, seq)

tdt4160.setcode(get_input("thecode"))

regs = {}
answer = {}

seed = random.randrange(256, 32768)
seq = 0

size = random.randrange(4, 32)

regs[10] = seed
regs[11] = size

maxnum = 0

for i in range(size):
    seed, seq = mswl32(seed, seq)
    if seed > maxnum:
        maxnum = seed

answer[10] = maxnum

success, errormsg = tdt4160.runtest(regs, answer)

if success:
    set_global_result("success")
    set_global_feedback("**Programmet fungerer.**")
else:
    set_global_result("failed")
    set_global_feedback(errormsg)
    
