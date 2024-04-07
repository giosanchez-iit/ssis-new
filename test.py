import csv
from crud_utils import CRUD_Data


if __name__ == "__main__":
    # Example usage: Print match scores for all rows in CSV with the name "Jane"
    Student = CRUD_Data(csv_name='Students', key='id_num', attributes=('id_num', 'full_name', 'course', 'yr_lvl', 'gender', 'status'))
    
    with open(Student.csv_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            match_score = Student._calculate_match_score("Jane Smoulder", row)
            print(f"Match Score for Row {row}: {match_score}")
