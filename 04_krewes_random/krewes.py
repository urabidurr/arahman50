'''<Abidur> <Rahman>
<Python Pigs>
SoftDev
K<04> -- <Python dictionaries and random selection>
<2024>-<09>-<16>
Time Spent: .3'''
import random

krewes = {
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'  #33
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' #32
              ]
         }

a = random.randint(0, len(krewes.get(4)) + len(krewes.get(5)) - 1)
print(f"Total amount of students: {len(krewes.get(4)) + len(krewes.get(5)) - 1}")
print(f"Index: {a}")
if (a<len(krewes.get(4))):
    b = krewes.get(4)[a]
else:
    b = krewes.get(5)[a-len(krewes.get(4))]
print(f"Name: {b}")
