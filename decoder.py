#wip, gonna finish after comming from my uncles farm

import sys, os, random, string
os.system("cls")
key = input("Type your key: \n")
os.system("cls")
ut = input("Type your encoded text: \n")
dic = { #im sleepy, i dont remember if there is a way to turn numbers into letters and viceversa using a builtin function, gotta check that before my travel to my uncle's farm tomorrow
    "a" : 1, #i really should use 0 as a start
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8,
    "i" : 9,
    "j" : 10,
    "k" : 11,
    "l" : 12,
    "m" : 13,
    "n" : 14,
    "o" : 15,
    "p" : 16,
    "q" : 17,
    "r" : 18,
    "s" : 19,
    "t" : 20,
    "u" : 21,
    "v" : 22,
    "w" : 23,
    "x" : 24,
    "y" : 25,
    "z" : 26,
    "1" : "a",
    "2" : "b",
    "3" : "c",
    "4" : "d",
    "5" : "e",
    "6" : "f",
    "7" : "g",
    "8" : "h",
    "9" : "i",
    "10" : "j",
    "11" : "k",
    "12" : "l",
    "13" : "m",
    "14" : "n",
    "15" : "o",
    "16" : "p",
    "17" : "q",
    "18" : "r",
    "19" : "s",
    "20" : "t",
    "21" : "u",
    "22" : "v",
    "23" : "w",
    "24" : "x",
    "25" : "y",
    "26" : "z",
}
def decode():
    r = ""
    for combo in ut.split("."):
        for letter in combo:
            for k in key:
                n = int(dic.get(k)) - int(dic.get(letter))
                while n<1:
                    n+=26
                n = str(n)
                print(str(dic.get(k)) + " - " + str(dic.get(letter)) + " = " + n)
                r += dic.get(n)
        r += "."
    return r # jl
result = decode() # rt.oq.vx.vx.ya.
print("result = " + result)