# -*- coding: utf-8 -*-
"""
Created on Tue May  2 13:02:19 2023

@author: becat
"""

import numpy as np
import matplotlib.pyplot as plt
import lammps_logfile
from scipy.optimize import curve_fit
import datetime
def time_left(step, total, tperstep):
    time = str(datetime.timedelta(seconds = (total-step)*1000/tperstep))
    print("Time left: {}".format(time))
def first(x, a, b):
    return a * x + b

def second(x, a, b, c):
    return a * x ** 2 + b * x + c

def third(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

def func(x, a, b, c, d):
    return a * x ** b + c * x + d

folder = "test5"

log = lammps_logfile.File("../{}/log.lammps".format(folder))
x = log.get("Step")
y = log.get("c_midtemp")

x *= 0.001


X = np.arange(0, 30000, 100)



pol1 = np.polyfit(x, y, 1)
pol2 = np.polyfit(x, y, 2)
pol3 = np.polyfit(x, y, 3)

popt, pcov = curve_fit(func, x, y)

T_ho = log.get("c_hotemp")
T_co = log.get("c_cotemp")

plt.figure(figsize = (12, 7))

#plt.plot(x, first(x, *pol1), color = "magenta", label = "First order fit")
# plt.plot(x, second(x, *pol2), "--", color = "green", label = "Second order fit")
# plt.plot(x, third(x, *pol3),color = "red", label = "Third order fit")
# plt.plot(x, np.polyval(np.polyfit(x, y, 4), x), "-.", color = "purple", label = "Fourth order fit")

plt.scatter(x, y, s = 0.1,marker = '*', label = "Sim data")
plt.plot(x, func(x, *popt))
plt.xlabel(r"time $\left[ps\right]$")
plt.ylabel("T [K]")
#plt.xticks(np.arange(0, 200+10, 10))
#plt.yticks(np.arange(140, 290+20, 20))
plt.legend()
plt.grid()
plt.title("Film average temperature (Kelvin) Vs. time", fontsize = 15)
plt.savefig("C:/Users/becat/Pictures/Chunks/mid_temp_evolution_{}_nosub.pdf".format(folder), dpi = 300)
plt.show()
plt.close()
time_left = 200 - x[-1]

tfin = 400

projected_final = y[0] + abs(y[-1] - y[0]) * tfin / (tfin - time_left)
print("The final expected temperature based on the current decrease is: {:.2f} K\n".format(projected_final))

fit_final = third(tfin, *pol3)

fit_fourth_fin = np.polyval(np.polyfit(x, y, 4), tfin)

print("The final temperature estimated with third degree polyfit is: {:.2f} K\n".format(fit_final))
print("The final temperature estimated with fourth degree polyfit is: {:.2f} K\n".format(fit_fourth_fin))

# Chunk, Coord1, Ncount, v_temp = np.loadtxt("../{}/finaltemp.profile".format(folder), unpack = True)

# x_max = 30 * 4.079

# bin_dx = x_max / 200 

# dist_x = Chunk * bin_dx

# plt.figure(figsize = (10, 5))
# plt.plot(dist_x[1:-2], v_temp[1:-2], color = "black", label = "Temperature")
# plt.axvline(20.395, color = "red")
# plt.axvline( 102.38 , color = "blue")
# #plt.ylim((80, 170))
# plt.xticks
# plt.xlim((bin_dx, x_max - bin_dx))
# plt.xticks(np.arange(0, 130, 10))

# plt.grid()
# plt.xlabel("x [nm]")
# plt.ylabel("T [K]")
# plt.axvspan(0, 20.395, facecolor='red', alpha=0.2, label = "Hot")
# plt.axvspan(102.38, x_max, facecolor='blue', alpha=0.2, label = "Cold")
# plt.axvspan(20.395, 102.38, facecolor='gold', alpha=0.2, label = "Mid")
# plt.legend(loc = "upper right", framealpha = 1)
# plt.savefig("C:/Users/becat/Pictures/Chunks/temp_profile_{}.png".format(folder), dpi = 300)
