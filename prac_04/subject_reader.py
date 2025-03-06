FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []

    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')

            if len(parts) == 3:
                try:
                    parts[2] = int(parts[2].strip('.'))
                    data_list.append(parts)
                except ValueError:
                    print(f"Error converting '{parts[2]}' to integer.")
            else:
                print(f"Incorrect format: {line}")

    return data_list

def display_subject_details(data):
    """Display the subject details in a formatted way."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()

