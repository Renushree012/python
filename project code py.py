# Initialize an empty dictionary to store championship history
championship_history = {}

# Function to create a new championship entry
def create_championship():
    championship_name = input("Enter the championship name: ")
    year = input("Enter the year of the championship: ")
    outcome = input("Enter the outcome of the championship: ")
    championship_history[championship_name] = {"Year": year, "Outcome": outcome}
    print("Championship entry created successfully.")

# Function to read the championship history
def read_championship():
    for championship, details in championship_history.items():
        print(f"Championship: {championship} - Year: {details['Year']} - Outcome: {details['Outcome']}")

# Function to update a championship entry
def update_championship():
    championship_name = input("Enter the championship name to update: ")
    if championship_name in championship_history:
        new_outcome = input("Enter the new outcome: ")
        new_year = input("Enter the new year: ")
        championship_history[championship_name]["Outcome"] = new_outcome
        championship_history[championship_name]["Year"] = new_year
        print("Championship entry updated successfully.")
    else:
        print("Championship not found in the history.")

# Function to delete a championship entry
def delete_championship():
    championship_name = input("Enter the championship name to delete: ")
    if championship_name in championship_history:
        del championship_history[championship_name]
        print("Championship entry deleted successfully.")
    else:
        print("Championship not found in the history.")

# Function to document outcomes (not implemented in this example)
def document_outcome():
    print("Document Outcome feature not implemented.")

# Function to analyze performance (not implemented in this example)
def analyze_performance():
    print("Performance analysis feature not implemented.")

# Main program loop
while True:
    print("\nChampionship History Tracker Menu:")
    print("1. Create Championship")
    print("2. Read Championship")
    print("3. Update Championship")
    print("4. Delete Championship")
    print("5. Document Outcome")
    print("6. Analyze Performance")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        create_championship()
    elif choice == '2':
        read_championship()
    elif choice == '3':
        update_championship()
    elif choice == '4':
        delete_championship()
    elif choice == '5':
        document_outcome()
    elif choice == '6':
        analyze_performance()
    elif choice == '7':
        print("Exiting the Championship History Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")