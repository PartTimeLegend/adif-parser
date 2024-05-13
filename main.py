import logging
import sys

from adif_parser import ADIFParser
from csv_exporter import CSVExporter

logging.basicConfig(level=logging.INFO)


def main():
    if len(sys.argv) != 3:
        logging.error("Usage: python main.py <path_to_adif_file> <output_csv_file>")
        sys.exit(1)

    adif_file = sys.argv[1]
    output_csv = sys.argv[2]

    parser = ADIFParser()
    try:
        parser.parse_file(adif_file)
    except Exception as e:
        logging.error(f"Error occurred while parsing the ADIF file: {e}")
        sys.exit(1)

    metrics = {
        "Bands": parser.bands,
        "Modes": parser.modes,
        "Countries": parser.countries,
        "Stations": parser.stations,
    }

    exporter = CSVExporter()
    try:
        exporter.export_to_csv(metrics, output_csv)
    except Exception as e:
        logging.error(f"Error occurred while exporting metrics to CSV: {e}")
        sys.exit(1)

    logging.info("Metrics exported successfully.")


if __name__ == "__main__":
    main()
