# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def name_star(targets):
	for key in targets:
		print(key)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def spectral_type(targets):
	for key in targets:
		print(targets[key]["Spectral Type"])
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def mag_measure(targets):
	for key in targets:
		if targets[key]["Magnitude"]>=1:
			print(targets[key]["Magnitude"])
# 4) Look up another target, add all the necessary information to the targets list.
Arcturus= {
	"RA": "14h 15m 40s",
	"Dec": "+19deg 10' 57''",
	"Magnitude": -0.04,
	"Spectral Type": "K1.fIII"
}

targets["Arcturus"] = Arcturus

# 5) Write a function that finds the brightest star
def brightest_star(targets):
	value = 0
	for key in targets:
		if targets[key]["Magnitude"]<= value:
			value = targets[key]["Magnitude"]
			print(key)

# 6) What's your favorite constellation

name_star(targets)
spectral_type(targets)
mag_measure(targets)
print(targets)
brightest_star(targets)
