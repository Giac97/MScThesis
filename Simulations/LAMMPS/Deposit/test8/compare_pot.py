from lammps_logfile import File
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

log_eam = File("./log.eam")
log_smatb = File("./log.smatb")

print(log_eam.get_keywords())
print(log_smatb.get_keywords())

step = log_eam.get("Step")

e_tot_eam = log_eam.get("TotEng")
e_tot_smatb = log_smatb.get("TotEng")

plt.plot(step, e_tot_eam, label = "EAM")
plt.plot(step, e_tot_smatb, label = "SMATB")
plt.legend()
plt.title("Comparison of the total energy for EAM and SMATB potentials")
plt.savefig("compare_etot.pdf")
plt.close()

e_pot_eam = log_eam.get("PotEng")
e_pot_smatb = log_smatb.get("PotEng")

plt.plot(step, e_pot_eam, label = "EAM")
plt.plot(step, e_pot_smatb, label = "SMATB")
plt.legend()
plt.title("Comparison of the potential energy for EAM and SMATB potentials")
plt.savefig("compare_epot.pdf")
plt.close()

diff_etot = abs(np.mean(e_tot_eam)) - abs(np.mean(e_tot_smatb))
print("The difference between the total energy eam and smatb is {:.2f} ev\n".format(diff_etot))

