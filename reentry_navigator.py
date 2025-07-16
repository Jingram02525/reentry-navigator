import csv


def load_resources(filename):
    resources = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            resources.append(row)
    return resources

def find_resources(resources, need):
    results = [r for r in resources if need.lower() in r['category'].lower()]
    return results

def main():
    print("Welcome to Reentry Navigator 🌱")
    print("What type of support are you looking for?")
    print("Options: housing, job training, legal aid, education, mental health")

    need = input("Enter your need: ").strip()
    resources = load_resources('resources.csv')
    matches = find_resources(resources, need)

    if matches:
        print(f"\nFound {len(matches)} resources for '{need}':\n")
        for r in matches:
            print(f"- {r['name']} ({r['location']}): {r['contact']}")
    else:
        print(f"\nSorry, no resources found for '{need}'.")

if __name__ == "__main__":
    main()

