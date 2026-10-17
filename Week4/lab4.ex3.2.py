# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:38:40 2022

@author: minut
"""

def get_data():
    label = ["0","1","2","3","4","5","6","6+"]
    result = []
    for lab in label:
        h = int(input("Please enter the number of houses with %s occupants: " % lab))
        result.append(h)
    return result

def cal_percentage(h0,h1,h2,h3,h4,h5,h6,h7):
    total = h0+h1+h2+h3+h4+h5+h6+h7
    p0 = (h0/total)*100
    p1 = (h1/total)*100 
    p2 = (h2/total)*100
    p3 = (h3/total)*100
    p4 = (h4/total)*100
    p5 = (h5/total)*100
    p6 = (h6/total)*100
    p7 = (h7/total)*100
    return p0,p1,p2,p3,p4,p5,p6,p7

def display_result(h0, h1, h2, h3, h4, h5, h6, h7,
                   p0, p1, p2, p3, p4, p5, p6, p7):
    h = [h0, h1, h2, h3, h4, h5, h6, h7]
    p = [p0, p1, p2, p3, p4, p5, p6, p7]
    print(f"{'Occupants:':>12}" + "".join(f"{x:>7}" for x in ["0", "1", "2", "3", "4", "5", "6", ">6"]))
    print(f"{'No. houses:':>12}" + "".join(f"{x:>7}" for x in h))
    print(f"{'Percentage:':>12}" + "".join(f"{x:>6.1f}%" for x in p))

if __name__ == "__main__":
    h0, h1, h2, h3, h4, h5, h6, h7 = get_data()
    p0, p1, p2, p3, p4, p5, p6, p7 = cal_percentage(h0, h1, h2, h3, h4, h5, h6, h7)
    display_result(h0, h1, h2, h3, h4, h5, h6, h7, p0, p1, p2, p3, p4, p5, p6, p7)