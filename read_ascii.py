import csv

input_file = "data/MS_BA_18.ascii"
output_file = "csv_data/converted_ascii.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)

    writer.writerow(["rt", "polarity", "source", "ms_level", "scan_type", "mz_range", "peak_count", "mz", "intensity"])

    for line in infile:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")

        rt = parts[0]
        polarity = parts[1]
        source = parts[2]
        ms_level = parts[3]
        scan_type = parts[5]
        mz_range = parts[6]
        peak_count = parts[7]

        peak_fields = parts[8:]

        for peak in peak_fields:
            peak = peak.strip()
            if not peak:
                continue

            mz, intensity = peak.split()
            writer.writerow([ rt, polarity, source, ms_level, scan_type, mz_range, peak_count, mz, intensity])

        