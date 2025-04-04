import datetime
from project import Project


def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            next(file)  # Skip header
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    project = Project(*parts)
                    projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-delimited file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            line = (f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                    f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
            file.write(line)
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display projects grouped by completion and sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("\nIncomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")
    print("\nCompleted projects:")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Show projects starting after a user-specified date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered = [p for p in projects if p.start_date > filter_date]
        for project in sorted(filtered, key=lambda x: x.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy.")


def add_new_project():
    """Collect user input to add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: ")
    completion = input("Percent complete: ")
    try:
        return Project(name, date_str, priority, cost, completion)
    except ValueError:
        print("Invalid input. Project not added.")
        return None


def update_project(projects):
    """Update an existing project's completion and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)

        new_comp = input("New Percentage: ")
        new_prio = input("New Priority: ")

        if new_comp:
            project.completion_percentage = int(new_comp)
        if new_prio:
            project.priority = int(new_prio)
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():
    """Main program loop with menu interface."""
    projects = []
    current_file = "projects.txt"
    projects = load_projects(current_file)

    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

    while True:
        print(menu)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
            current_file = filename
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            new_project = add_new_project()
            if new_project:
                projects.append(new_project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Save to current file before quitting? (y/n): ").lower() == 'y':
                save_projects(current_file, projects)
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()