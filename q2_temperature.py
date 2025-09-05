import os
import csv
import math
 
FOLDER = "temperatures"
 
# Seasons mapping
SEASON_MONTHS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}
 
def average(values):
    clean = [v for v in values if v is not None]
    return sum(clean) / len(clean) if clean else None
 
def std_dev(values):
    clean = [v for v in values if v is not None]
    if not clean:
        return None
    m = average(clean)
    var = sum((x - m) ** 2 for x in clean) / len(clean)
    return math.sqrt(var)
 
# Storage
season_data = {"Summer": [], "Autumn": [], "Winter": [], "Spring": []}
station_data = {}
 
# Read all CSVs
for file in os.listdir(FOLDER):
 if file.endswith(".csv"):
        path = os.path.join(FOLDER, file)
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
 

            for row in reader:
                station = row["STATION_NAME"].strip()
 
                if station not in station_data:
                    station_data[station] = []
 
                # Loop through months
                for season, months in SEASON_MONTHS.items():
                    for month in months:
                        if month in row:
                            val = row[month].strip()
                            temp = float(val) if val not in ("", "NaN", "nan") else None
                            if temp is not None:
                                season_data[season].append(temp)
                                station_data[station].append(temp)
 
 
# 1. Seasonal averages
with open("average_temp.txt", "w", encoding="utf-8") as f:
    for season, temps in season_data.items():
        avg = average(temps)
        if avg is not None:
            f.write(f"{season}: {avg:.1f}°C\n")
 
# 2. Largest temperature range
ranges = {}
for st, temps in station_data.items():
    clean = [t for t in temps if t is not None]
    if clean:
        r = max(clean) - min(clean)
        ranges[st] = (r, max(clean), min(clean))
 
max_range = max(ranges.values(), key=lambda x: x[0])[0]
with open("largest_temp_range_station.txt", "w", encoding="utf-8") as f:
    for st, (r, hi, lo) in ranges.items():
        if abs(r - max_range) < 1e-6:
            f.write(f"{st}: Range {r:.1f}°C (Max: {hi:.1f}°C, Min: {lo:.1f}°C)\n")
 
# 3. Stability (standard deviation)
stdevs = {}
for st, temps in station_data.items():
    sd = std_dev(temps)
    if sd is not None:
        stdevs[st] = sd
 
min_sd = min(stdevs.values())
max_sd = max(stdevs.values())
with open("temperature_stability_stations.txt", "w", encoding="utf-8") as f:
    for st, sd in stdevs.items():
        if abs(sd - min_sd) < 1e-6:
            f.write(f"Most Stable: {st}: StdDev {sd:.1f}°C\n")
    for st, sd in stdevs.items():
        if abs(sd - max_sd) < 1e-6:
            f.write(f"Most Variable: {st}: StdDev {sd:.1f}°C\n")
 
print("Done... Results saved!!")
 
