import sys

import matplotlib.pyplot as plt
import numpy as np

from lal import git_version
import bilby

parameters = {
    "a_1": 0.9363075905791275,
    "a_2": 0.29842284281836257,
    "tilt_1": 0.08245299399601491,
    "tilt_2": 1.4267948555050711,
    "phi_12": 4.296329265980699,
    "phi_jl": 2.5349460938281925,
    "theta_jn": 0.9679487130230104,
    "phase": 0.027657481036832493,
    "luminosity_distance": 7937.007905508532,
    "mass_1": 260.198766485256,
    "mass_2": 14.333365815353579,
    "reference_frequency": 20.0,
    "waveform_approximant": "IMRPhenomXPHM",
    "catch_waveform_errors": True,
    "pn_spin_order": -1,
    "pn_tidal_order": -1,
    "pn_phase_order": -1,
    "pn_amplitude_order": 1,
    #"PhenomXPHMThresholdMband": 0
}


frequency_array = np.linspace(0, 2048, 2048 * 8 + 1)

wf = bilby.gw.source.lal_binary_black_hole(frequency_array, **parameters)

#plt.loglog()
test = bilby.gw.source.lal_binary_black_hole(frequency_array, **parameters)
plt.loglog(frequency_array, abs(test["plus"]), label="Original")
plt.axvline(x=103.5, color='red')
perturbation = 1e-15
parameters["a_1"] += perturbation
# test = bilby.gw.source.lal_binary_black_hole(frequency_array, **parameters)
# plt.semilogy(
#     frequency_array, abs(test["plus"]), label=f"$\\Delta a_1 = {perturbation:.0e}$"
# )
parameters["a_1"] -= perturbation
plt.xlabel("Frequency [Hz]")
plt.ylabel("Waveform Amplitude")
plt.xlim(10, 250)
plt.ylim(1e-30)
plt.xlim(20, 256)
plt.ylim(1e-28)
plt.legend(loc="upper left")
plt.savefig("waveform.png")
plt.close()

print("Versions")
print("Python")
print(sys.executable)
print("LALSuite")
print(git_version.verbose_msg)
print("Bilby")
print(bilby.__version__)
