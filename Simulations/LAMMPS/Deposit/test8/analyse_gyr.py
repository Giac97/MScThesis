import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def shape_par(gyr_tens):
    val, vec = np.linalg.eig(gyr_tens)
    l1, l2, l3 = val
    lx, ly, lz = np.sort([l1, l2, l3])
    R2 = lx + ly + lz
    aspher = lz - 0.5 * (lx + ly)
    acyl = ly - lx
    anisoshape = 1.5 * (lx * lx + ly * ly + lz * lz) / ((lx + ly + lz) *  (lx + ly + lz)) - 0.5
    return aspher, acyl, anisoshape

def read_gyr(fname, N_step, N_freq):
    infile = open(fname, "r")
    N_calc = int(N_step / N_freq)
    out = np.zeros((int(N_calc), 7))
    for i in range(3):
        desc = infile.readline()
        
    for i in range(int(N_calc)):
        first_line = infile.readline()
        data = infile.readline()
        
        
        out[i, :] = data.split()
    infile.close()
    return out
v_min   = 0.05
v_max   = 0.15
dv      = 0.01

vz = np.arange(v_min, v_max, dv)
N_steps = 15_000
dt = 0.001

t = np.arange(0, N_steps * dt, 0.1)
asph_max = []
aniso_max = []
for v in vz:
    print("./gyration/gyration_{:.2f}.out".format(v))
    out = read_gyr("./gyration/gyration_{:.2f}.out".format(v), N_steps, 100)
    
    row= out[:, 0]
    xx = out[:, 1]
    yy = out[:, 2]
    zz = out[:, 3]
    xy = out[:, 4]
    xz = out[:, 5]
    yz = out[:, 6]

    asph = []
    aniso = []
    for i in range(int(15000 / 100)):
        row= out[i, 0]
        xx = out[i, 1]
        yy = out[i, 2]
        zz = out[i, 3]
        xy = out[i, 4]
        xz = out[i, 5]
        yz = out[i, 6]
        G = np.array([[xx, xy, xz], [xy, yy, yz], [xz, yz, zz]])
        b, c, d = shape_par(G)
        asph.append(b)
        aniso.append(d)

    fig, ax1 = plt.subplots(figsize = (10, 7))

    color = 'tab:red'
    ax1.set_xlabel('time (ps)')
    ax1.set_xlim((0, 20))
    ax1.set_ylabel('Asphericity', color=color)
    ax1.plot(t, asph, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Anisotropy', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, aniso, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.suptitle(r"Asphericity and shape anisotrpy with $v_z(0) = -{:.2f}$".format(v))

    fig.tight_layout()
    fig.savefig("./plots/sus_{:.2f}.pdf".format(v))
    plt.close()
    asph_max.append(max(asph))
    aniso_max.append(max(aniso))


fig, ax1 = plt.subplots(figsize = (15, 7))
for v in vz:
    plt.axvline(v, linewidth = 0.75, linestyle = "--", color = "k")
color = 'tab:red'
ax1.set_xlabel(r'$-v_0 \left[ \frac{\AA}{ps} \right]$')
ax1.set_ylabel('Max asphericity', color=color)
ax1.set_xticks(vz)
ax1.plot(vz, asph_max, color=color, marker = "^", label = "Asphericity")
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Max anisotropy', color=color)  # we already handled the x-label with ax1
ax2.plot(vz, aniso_max, color=color, marker = "d", label = "Anisotropy")
ax2.tick_params(axis='y', labelcolor=color)

fig.suptitle("Maximum of asphericity and shape anisotropy")

fig.tight_layout()
fig.savefig("./max_vals.pdf")
fig.clear()