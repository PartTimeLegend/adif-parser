# ADIF Parser

This is a Python script for parsing ADIF (Amateur Data Interchange Format) files and extracting metrics on bands, modes, countries, and stations.

## Features
- Parses an ADIF file and extracts metrics on bands, modes, countries, and stations.
- Outputs the metrics to a CSV file.
- Supports alphabetical sorting of metrics for better readability.

## Usage
1. Clone the repository:

```bash
git clone https://github.com/PartTimeLegend/adif-parser.git
```

2. Navigate to the project directory:

```bash
cd adif-parser
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python main.py <path_to_adif_file> <output_csv_file>
```

Replace `<path_to_adif_file>` with the path to your ADIF file and `<output_csv_file>` with the desired filename for the CSV output.

## Requirements
- Python 3.x
- pycountry library

## License
This project is licensed under the MIT License. See the LICENSE file for details.
