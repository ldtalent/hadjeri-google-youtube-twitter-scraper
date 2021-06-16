import csv


def save_to_csv(description,date, title, url,source):
    with open('scrapedData.csv', mode='w') as csv_file:
        fieldnames = ['description', 'date', 'title', 'url', 'source']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'description': description, 'date': date, 'title': title, 'url':url, 'source':source})


