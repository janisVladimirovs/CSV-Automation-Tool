import csv

def file_check(file_path):
    try:
        with open(file_path, "r"):
            return True
    except FileNotFoundError:
        print("dalbajob ieliec istu failu")
        return False

def duplicate(file_path):
    with open(file_path, "r") as input_file:
        reader = csv.reader(input_file, skipinitialspace= True)
        seen = set()
        updated_lines = []
        total_lines = 0
        new_lines = 0
        empty_lines = 0
        removed_duplicates = 0
        with open("cleaned.csv", "w", newline= "")as output_file:
            writer = csv.writer(output_file)
        

            for row in reader:
                cleaned_row = []
                
                for cell in row:
                    cell = cell.strip()
                    cleaned_row.append(cell)
                total_lines += 1
                row_key = tuple(cleaned_row)
                if len(cleaned_row) == 0:
                    empty_lines +=1
                        
                else:
                    if row_key in seen:
                        print("Duplicate line: ", row)
                        removed_duplicates += 1   
                    else:
                        seen.add(row_key) 
                        updated_lines.append(cleaned_row)
                        new_lines += 1
        
            print("Lines: ", seen)
            
            report = open("report.txt", "w")
            for i in updated_lines:
                writer.writerow(i)
            report.write(f"Rows before : {total_lines} \n" 
                        f"Duplicates removed : {removed_duplicates} \n"
                        f"Empty rows removed : {empty_lines} \n"
                        f"Rows after : {new_lines} " )
            print("update saved in Cleaned.csv")
            print("Report in report.txt")
            report.close()

def analyze(file_path):
    with open(file_path, "r") as input_file:
        reader = csv.reader(input_file, skipinitialspace= True)
        seen = set()
        total_lines = 0
        empty_lines = 0
        duplicates = 0
        max_columns = 0
        expected_columns = None
        incorrect_column_count = 0
        empty_cells = 0
        

        for row in reader:
            total_lines += 1

            if len(row) == 0:
                empty_lines +=1
                continue
            cleaned_row = []
            for cell in row:
                cell = cell.strip()
                if cell == "":
                    empty_cells += 1
                cleaned_row.append(cell)
        
            row_key = tuple(cleaned_row)
            columns = len(cleaned_row)
            
            if expected_columns is None:
                expected_columns = columns
            if columns != expected_columns:
                incorrect_column_count += 1

            if columns > max_columns:
                max_columns = columns
                
            if row_key in seen:
                duplicates += 1   
            else:
                seen.add(row_key)
                    
        print(f"Rows : {total_lines} \n"
            f"Expected columns : {expected_columns} \n"
            f"Max columns : {max_columns} \n"
            f"Rows with incorrect column count : {incorrect_column_count} \n"
            f"Empty cells : {empty_cells} \n"
            f"Duplicates : {duplicates} \n"
            f"Empty rows : {empty_lines}")
              
def main():
    while True:
        while True:
            file_path = input("Enter csv file path: ")

            if file_path == "exit":
                return

            if file_check(file_path):
                print("File found!")
                break

        while True:

                print("Current commands: \n" \
                    "clean up \n" \
                    "analyze \n"
                    "exit" )

                user_input = input("input csv action: ")
                command = user_input.lower()

                if len(command) == 0:
                    print("Please input a command")
                    continue

                if command == "clean up":
                    duplicate(file_path)

                elif command == "analyze":
                    analyze(file_path)

                elif command == "exit":
                    return
                else:
                    print("nu tu lohs")

main()


