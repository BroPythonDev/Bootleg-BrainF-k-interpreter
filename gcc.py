from sys import *

def Interpreter(filename):

    pointer_pos = 0
    reg_0 = 0
    reg_1 = 0
    reg_2 = 0
    reg_3 = 0
    reg_4 = 0
    reg_5 = 0
    reg_6 = 0
    reg_7 = 0

    min_reg_value = 0
    max_reg_value = 16
    max_registers = 8


    try:
        with open(filename, 'r') as file:
            
            lines = file.readlines()
            lines = list(map(lambda s: s.strip(), lines))
            
            for line in lines:
                if line == "mov %r <++>":
                    if pointer_pos < max_reg_value:
                        pointer_pos += 1
                    else:
                        print("ERROR: Trying to overwrite the max value of the register")
                elif line == "mov %r <-->":
                    if pointer_pos > min_reg_value:
                        pointer_pos -= 1
                    else:
                        print("ERROR: Trying to overwrite the min value of the register")
                elif line == "DEF_OUT <prgm.debug>":
                    print("Brain Fuck Program Debug Stats: ")
                    print("----------------------------------")
                    print("Pointer Position: " + str(pointer_pos))
                    print("MAX REGISTERS: " + str(max_registers))
                    print("MIN VALUE: " + str(min_reg_value) + " / MAX VALUE: " + str(max_reg_value))
                    print("Register 0: " + str(reg_0))
                    print("Register 1: " + str(reg_1))
                    print("Register 2: " + str(reg_2))
                    print("Register 3: " + str(reg_3))
                    print("Register 4: " + str(reg_4))
                    print("Register 5: " + str(reg_5))
                    print("Register 6: " + str(reg_6))
                    print("Register 7: " + str(reg_7))
                    print("Press ENTER to continue...")
                    input()
                elif line == "jmp<incr>":
                    if pointer_pos == 0:
                        if reg_0 < max_reg_value:
                            reg_0 += 1
                        else:
                            print("Trying to overwrite value (+1 more than allowed)")
                    elif pointer_pos == 1:
                        if reg_1 < max_reg_value:
                            reg_1 += 1
                        else:
                            print("Trying to overwrite value (+1 more than allowed)")
                    elif pointer_pos == 2:
                        if reg_2 < max_reg_value:
                            reg_2 += 1
                        else:
                            print("Trying to overwrite value (+1 more than allowed)")
                    elif pointer_pos == 3:
                        if reg_3 < max_reg_value:
                            reg_3 += 1
                        else:
                            print("Trying to overwrite value (+1 more than allowed)")
                    elif pointer_pos == 4:
                        if reg_4 < max_reg_value:
                            reg_4 += 1
                        else:
                            print("Trying to overwrite value (+1 more than allowed)")
                    elif pointer_pos == 5:
                        if reg_5 < max_reg_value:
                            reg_5 += 1
                        else:
                            print("Trying to overwrite value (+1 more than allowed)")
                    elif pointer_pos == 6:
                        if reg_6 < max_reg_value:
                            reg_6 += 1
                        else:
                            print("Trying to overwrite value (+1 more than allowed)")
                    elif pointer_pos == 7:
                        if reg_7 < max_reg_value:
                            reg_7 += 1
                        else:
                            print("Trying to overwrite value (+1 more than allowed)")
                    else:
                        print("ERROR: Internal Compiler Error")


                

                elif line == "jmp<decr>":
                    if pointer_pos == 0:
                        if reg_0 > max_reg_value:
                            reg_0 -= 1
                        else:
                            print("Trying to overwrite value (-1 more than allowed)")
                    elif pointer_pos == 1:
                        if reg_1 > max_reg_value:
                            reg_1 -= 1
                        else:
                            print("Trying to overwrite value (-1 more than allowed)")
                    elif pointer_pos == 2:
                        if reg_2 > max_reg_value:
                            reg_2 -= 1
                        else:
                            print("Trying to overwrite value (-1 more than allowed)")
                    elif pointer_pos == 3:
                        if reg_3 > max_reg_value:
                            reg_3 -= 1
                        else:
                            print("Trying to overwrite value (-1 more than allowed)")
                    elif pointer_pos == 4:
                        if reg_4 > max_reg_value:
                            reg_4 -= 1
                        else:
                            print("Trying to overwrite value (-1 more than allowed)")
                    elif pointer_pos == 5:
                        if reg_5 > max_reg_value:
                            reg_5 -= 1
                        else:
                            print("Trying to overwrite value (-1 more than allowed)")
                    elif pointer_pos == 6:
                        if reg_6 > max_reg_value:
                            reg_6 -= 1
                        else:
                            print("Trying to overwrite value (-1 more than allowed)")
                    elif pointer_pos == 7:
                        if reg_7 >= min_reg_value:
                            reg_7 -= 1
                        else:
                            print("Trying to overwrite value (-1 more than allowd)")
                    else:
                        print("ERROR: Internal Compiler Error")
                
                
                
                
                elif line == "for[-]":
                    reg_0 = min_reg_value
                    reg_1 = min_reg_value
                    reg_2 = min_reg_value
                    reg_3 = min_reg_value
                    reg_4 = min_reg_value
                    reg_5 = min_reg_value
                    reg_6 = min_reg_value
                    reg_7 = min_reg_value
                elif line == "for[+]":
                    reg_0 = max_reg_value
                    reg_1 = max_reg_value
                    reg_2 = max_reg_value
                    reg_3 = max_reg_value
                    reg_4 = max_reg_value
                    reg_5 = max_reg_value
                    reg_6 = max_reg_value
                    reg_7 = max_reg_value
                else:
                    print("Command not found!")



    except:
        print("ERROR: File not found")


def GetInput():
    Interpreter(argv[1])


GetInput()
