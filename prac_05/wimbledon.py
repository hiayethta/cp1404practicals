"""
CP1404/CP5632 Practical
File reading, data processing and formatting output
Data based on Wimbledon gentleman's singles champions
"""

FILENAME = "wimbledon.csv"
INDEX_OF_COUNTRY = 1
INDEX_OF_CHAMPION = 2


def get_records():
    global records
    records = []
    with open(FILENAME, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)


def main():
    global record, champion_to_count, countries
    record = get_records[FILENAME]
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


main()


def process_records():
    global champion_to_count, countries, record
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_OF_COUNTRY])
        try:
            champion_to_count[record[INDEX_OF_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_OF_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\n These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))
