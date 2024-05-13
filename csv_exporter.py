# csv_exporter.py
import csv

class CSVExporter:
    def export_to_csv(self, metrics, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for metric_name, metric_data in metrics.items():
                sorted_items = sorted(metric_data.items(), key=lambda x: x[0])
                writer.writerow([metric_name])
                for item, count in sorted_items:
                    writer.writerow([item, count])
                writer.writerow([])  # Blank line between different metrics
