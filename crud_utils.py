import csv
import os
import re
from fuzzywuzzy import fuzz
import difflib

class CRUD_Data:
    def __init__(self, csv_name, key, attributes):
        self.csv_name = csv_name
        self.key = key
        self.attributes = attributes
        self.csv_path = f"{csv_name}.csv"

    def create(self, **kwargs):
        # Check if CSV file exists, create if not
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.attributes)
                writer.writeheader()

        # Check for duplication
        if self._exists(kwargs[self.key]):
            print(f"Error: {kwargs[self.key]} already exists.")
            return

        # Read existing data from CSV
        existing_data = []
        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_data.append(row)

        # Find the correct position to insert the new row based on the key
        index_to_insert = 0
        for idx, row in enumerate(existing_data):
            if row[self.key] > kwargs[self.key]:
                index_to_insert = idx
                break
        else:
            index_to_insert = len(existing_data)

        # Insert the new row at the correct position
        existing_data.insert(index_to_insert, kwargs)

        # Write updated data to CSV
        with open(self.csv_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.attributes)
            writer.writeheader()
            writer.writerows(existing_data)
        print("Data created successfully.")

    def read(self, key):
        # Read data from CSV
        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[self.key] == key:
                    print(row)
                    return
        print(f"No data found with key {key}.")

    def update(self, key, **kwargs):
        # Check for key in attributes
        if self.key not in kwargs:
            print("Error: Key attribute is missing.")
            return

        # Read data from CSV
        data = []
        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[self.key] == key:
                    row.update(kwargs)
                data.append(row)

        # Write updated data to CSV
        with open(self.csv_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.attributes)
            writer.writeheader()
            writer.writerows(data)
        print("Data updated successfully.")

    def delete(self, key):
        # Read data from CSV and filter out the row with the given key
        data = []
        found = False
        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[self.key] != key:
                    data.append(row)
                else:
                    found = True

        # Write filtered data back to CSV
        with open(self.csv_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.attributes)
            writer.writeheader()
            writer.writerows(data)

        if found:
            print(f"Data with key {key} deleted successfully.")
        else:
            print(f"No data found with key {key}.")

    def search(self, query, min_match=0, max_match=100):
        # Read data from CSV and perform fuzzy search
        matched_rows = []
        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match_score = self._calculate_match_score(query, row)
                if min_match <= match_score <= max_match:
                    matched_rows.append(row)
        
        # Return matched rows
        return matched_rows

    def _calculate_match_score(self, query, row):
        # Remove punctuation and special characters, and convert to lowercase
        query_processed = re.sub(r'[^\w\s]', '', query).lower()
        row_values_processed = [re.sub(r'[^\w\s]', '', value).lower() for value in row.values()]

        # Tokenize query and row values into words
        query_tokens = query_processed.split()
        row_tokens = ' '.join(row_values_processed).split()

        # Calculate full token set ratio using fuzzywuzzy
        token_set_ratio = fuzz.token_set_ratio(query_tokens, row_tokens)

        return token_set_ratio


    def _exists(self, key):
        # Check if key already exists in CSV
        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[self.key] == key:
                    return True
        return False
