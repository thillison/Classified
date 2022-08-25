#Export to CSV
import csv 

def save_as_csv(csvpath):

# csv_path = Path('stock_data_output.csv')
    with open(csvpath, 'w', newline='') as csv_file:
        header = []
        data =[]
        csvwriter = csv.writer(csv_file, delimiter = ",")

        csvwriter.writerow(header)
        csvwriter.writerow(data)

    return csvwriter