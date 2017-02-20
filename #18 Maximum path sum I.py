r1=[75]
r2=[95,64]
r3=[17,47,82]
r4=[18,35,87,10]
r5=[20,4,82,47,65]
r6=[19,1,23,75,3,34]
r7=[88,2,77,73,7,63,67]
r8=[99,65,4,28,6,16,70,92]
r9=[41,41,26,56,83,40,80,70,33]
r10=[41,48,72,33,47,32,37,16,94,29]
r11=[53,71,44,65,25,43,91,52,97,51,14]
r12=[70,11,33,28,77,73,17,78,39,68,17,57]
r13=[91,71,52,38,17,14,91,43,58,50,27,29,48]
r14=[63,66,4,68,89,53,67,30,73,16,69,87,40,31]
r15=[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
ans ,maxans= 0,0
for a1 in range(0,1):
    aa1=r1[a1]
    for a2 in range(0,2):
        aa2=r2[a2]
        for a3 in range(a2+0,a2+2):
            aa3=r3[a3]
            for a4 in range(a3+0,a3+2):
                aa4=r4[a4]
                for a5 in range(a4+0,a4+2):
                    aa5=r5[a5]
                    for a6 in range(a5+0,a5+2):
                        aa6=r6[a6]
                        for a7 in range(a6+0,a6+2):
                            aa7=r7[a7]
                            for a8 in range(a7+0,a7+2):
                                aa8=r8[a8]
                                for a9 in range(a8+0,a8+2):
                                    aa9=r9[a9]
                                    for a10 in range(a9+0,a9+2):
                                        aa10=r10[a10]
                                        for a11 in range(a10+0,a10+2):
                                            aa11=r11[a11]
                                            for a12 in range(a11+0,a11+2):
                                                aa12=r12[a12]
                                                for a13 in range(a12+0,a12+2):
                                                    aa13=r13[a13]
                                                    for a14 in range(a13+0,a13+2):
                                                        aa14=r14[a14]
                                                        for a15 in range(a14+0,a14+2):
                                                            aa15=r15[a15]
                                                            ans = aa1+aa2+aa3+aa4+aa5+aa6+aa7+aa8+aa9+aa10+aa11+aa12+aa13+aa14+aa15
                                                            if ans > maxans:
                                                                maxans = ans
print(maxans)
