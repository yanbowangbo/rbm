import json
import matplotlib.pyplot as plt

with open("./details/rbm___hid_128___ep_20", "rb") as f:
    rbm_results = json.loads(f.read())

with open("./details/frbm___hid_128___ep_20", "rb") as ff:
    frbm_results = json.loads(ff.read())

rbm_errors = rbm_results.get("errors")
frbm_errors = frbm_results.get("errors")

plt.plot(list(range(len(rbm_errors))), rbm_errors)
# plt.clf()
plt.plot(list(range(len(rbm_errors))), frbm_errors)
plt.show()