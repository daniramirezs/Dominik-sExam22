import csv


class FundingRaised:
    @staticmethod
    def where(options={}):
        with open("C:\\Users\\JARS\\Documents\\DIT\\3rd Semester\\Innovation and Complexity\\EXAM22\\startup_funding (1).csv", "rt") as csvfile:
            data = csv.reader(csvfile, delimiter=",", quotechar='"')
            csv_data = []
            for row in data:
                csv_data.append(row)

        headers = csv_data[0]
        csv_data = [FundingRaised.column_name(options, csv_data, 'company_name', 1), FundingRaised.column_name(options, csv_data, 'city', 4), 
                    FundingRaised.column_name(options, csv_data, 'state', 5), FundingRaised.column_name(options, csv_data, 'round', 9)]

        output = []
        for row in csv_data:
            mapped = dict(zip(headers, row))
            output.append(mapped)
        return output

    @staticmethod
        def column_name(options, csv_data, titles, place):
            if titles in options:
                result = []
                for row in csv_data:
                    if row[place] == options[titles]:
                        result.append(row)
                csv_data = result
                return csv_data

    @staticmethod
    def find_by(options):
        with open("C:\\Users\\JARS\\Documents\\DIT\\3rd Semester\\Innovation and Complexity\\EXAM22\\startup_funding (1).csv", "rt") as csvfile:
            data = csv.reader(csvfile, delimiter=",", quotechar='"')
            # skip header
            next(data)
            csv_data = []
            for row in data:
                csv_data.append(row)

    def mapping(options, csv_data, titles, place):
        if titles in options:
            for row in csv_data:
                if row[place] == options[titles]:
                    mapped = {}
                    mapped["permalink"] = row[0]
                    mapped["company_name"] = row[1]
                    mapped["number_employees"] = row[2]
                    mapped["category"] = row[3]
                    mapped["city"] = row[4]
                    mapped["state"] = row[5]
                    mapped["funded_date"] = row[6]
                    mapped["raised_amount"] = row[7]
                    mapped["raised_currency"] = row[8]
                    mapped["round"] = row[9]
                    return mapped


class RecordNotFound(Exception):
    pass
