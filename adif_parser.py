# adif_parser.py
import re
from collections import Counter
import pycountry

class ADIFParser:
    def __init__(self):
        self.bands = Counter()
        self.modes = Counter()
        self.countries = Counter()
        self.stations = Counter()

    def parse_file(self, file_path):
        # Regular expressions for extracting necessary information
        band_pattern = re.compile(r'<BAND:(\d+)>(\w+)')
        mode_pattern = re.compile(r'<MODE:(\d+)>(\w+)')
        country_pattern = re.compile(r'<COUNTRY:(\d+)>([\w\s]+)')
        callsign_pattern = re.compile(r'<CALL:(\d+)>(\w+)')

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = band_pattern.search(line)
                if match:
                    self.bands[match.group(2)] += 1
                
                match = mode_pattern.search(line)
                if match:
                    self.modes[match.group(2)] += 1
                
                match = country_pattern.search(line)
                if match:
                    country_name = match.group(2).strip()
                    # Check if the country name is actually a country code
                    if len(country_name) == 2:
                        try:
                            country_obj = pycountry.countries.get(alpha_2=country_name)
                            country_name = country_obj.name
                        except AttributeError:
                            # Country code not found, ignore
                            pass
                    self.countries[country_name] += 1
                
                match = callsign_pattern.search(line)
                if match:
                    self.stations[match.group(2)] += 1
