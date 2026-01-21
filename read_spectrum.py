import csv

input_file = "data/MS_BA_18_BD6_01_4598.d.spectrum"  
output_file = "csv_data/converted_spectrum.csv"

metadata = {}
peaks = []

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if ":" in line and not line[0].isdigit():
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()

        elif line[0].isdigit():
            values = line.split()
            for i in range(0, len(values), 2):
                mz = values[i]
                intensity = values[i + 1]
                peaks.append((mz, intensity))

with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["ret_time", "ion_mode", "instrument", "base_peak", "base_peak_intensity", "mz", "intensity"])

    for mz, intensity in peaks:
        writer.writerow([
            metadata.get("RetTime", ""),
            metadata.get("IonPol", ""),
            metadata.get("InstName", ""),
            metadata.get("BasePeak", ""),
            metadata.get("BasePeakIntensity", ""),
            mz,
            intensity
        ])