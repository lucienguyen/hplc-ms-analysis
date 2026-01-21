import csv

input_file = "data/MS_BA_18.dx"
output_file = "csv_data/converted_dx.csv"

title = ""
current_rt = None
rows = []

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()

        if line.startswith("##TITLE="):
            title = line.split("=", 1)[1].strip()

        elif line.startswith("##PAGE="):
            current_rt = float(line.split("T=")[1].strip())

        elif not line.startswith("##") and "," in line and ";" in line:
            pairs = line.split(";")
            for pair in pairs:
                pair = pair.strip()
                if not pair:
                    continue
                mz, intensity = pair.split(",")
                rows.append([
                    title,
                    current_rt,
                    float(mz),
                    float(intensity)
                ])

with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "title",
        "retention_time_sec",
        "mz",
        "intensity"
    ])
    writer.writerows(rows)

print("CSV file successfully created.")
