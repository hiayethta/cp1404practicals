"""
CP1404/CP5632 Practical
File reading, data processing and formatting output
Data based on Wimbledon gentleman's singles champions
"""

FILENAME = "wimbledon.csv"

records = []
with open(FILENAME, "r", encoding="utf-8") as in_file:
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        records.append(parts)
