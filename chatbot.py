from services.line_status import get_line_status
from services.arrivals import get_next_train
from utils.detect import detect_line, detect_station

print("========================================")
print(" TfL AI Travel Assistant")
print(" Ask about tube status or next trains")
print(" Example: 'central line status'")
print(" Example: 'next train at oxford circus'")
print(" Type 'exit' to quit")
print("========================================") 

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye 👋")
        break

    # Check train arrival request
    if "train" in user_input or "arrival" in user_input:
        station = detect_station(user_input)

        if station:
            print("Bot:", get_next_train(station))
        else:
            print("Bot: Please specify a station (e.g., Oxford Circus).")

        continue

    # Check line status
    line = detect_line(user_input)

    if line:
        print("Bot:", get_line_status(line))
        continue

    print("Bot: I can check tube status or next train times.")
