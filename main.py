import json

print("=" * 40)
print("📄 JSON Formatter")
print("=" * 40)

filename = input("Enter JSON file name (e.g. sample.json): ")

try:
    with open(filename, "r") as file:
        data = json.load(file)

    print("\nFormatted JSON:\n")
    print(json.dumps(data, indent=4))

except FileNotFoundError:
    print("\n❌ File not found!")

except json.JSONDecodeError:
    print("\n❌ Invalid JSON file!")
