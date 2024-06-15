import csv
filename ="countries.csv"

def main():
    load_countries_data(filename)
    # country_data = load_countries_data(filename)
    # formatted_data = format_data(country_data)
    # format_data(country_data)
    # format_data(country_data)
    # print(country_data)
def load_countries_data(filename):
    country_dict = {}
    with open(filename,encoding='utf-8') as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            country = record[0]
            capital = record[1]
            population = int(record[2].replace(',',''))
            percentage = float(record[3].replace('%',''))
            country_dict[country] = {"capital":capital,"population":population,"percentage":percentage,}
            max_length_country = max(len(country) for country in country_dict.keys())
            max_length_capital = max(len(capital) for capital in country_dict.keys())
            max_length_population = max(len(population) for population in country_dict.keys())
            print(f"{country:{max_length_country}}  - {capital:{max_length_capital}} {population:{max_length_population}}( {percentage})")

         # return country_dict

# def format_data(country_data):
#     for country,population in country_data.items():
#         country_data[country] = population
#         max_length = max(len(country) for country in country_data.keys())
#         print(f"{country:{max_length}} - {population}")



main()


