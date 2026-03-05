import requests

print("====================================")
print(" TfL AI Travel Assistant ")
print(" Ask about London Underground lines ")
print(" type 'exit' to stop ")
print("====================================")


def get_line_status(line):
    url = f"https://api.tfl.gov.uk/Line/{line}/Status"

    try:
        response = requests.get(url)
        data = response.json()

        status = data[0]["lineStatuses"][0]["statusSeverityDescription"]
        return status

    except:
        return "Unable to retrieve data."


tube_lines = [
    "central",
    "northern",
    "jubilee",
    "victoria",
    "piccadilly",
    "district",
    "circle",
    "metropolitan",
    "bakerloo"
]


while True:

    user_input = input("\nYou: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    found_line = None

    for line in tube_lines:
        if line in user_input:
            found_line = line
            break

    if found_line:

        status = get_line_status(found_line)

        print(f"Bot: The {found_line.capitalize()} line currently has {status}.")

    else:

        print("Bot: Please ask about a London Underground line (e.g., Central line).")
