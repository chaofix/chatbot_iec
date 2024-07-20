import json

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def display_plans(data):
    for plan in data['תוכניות_חשמל']:
        print(f"שם: {plan['שם']}, מחיר: {plan['מחיר']}, הנחה: {plan['הנחה']}%")

def main():
    print("ברוכים הבאים לצ'אט בוט!")
    
    data = load_data('data.json')
    
    while True:
        user_input = input("אנא הקלד הודעה ('תוכניות' להצגת תוכניות, 'צא' לסיום): ")
        if user_input.lower() == 'צא':
            print("תודה ולהתראות!")
            break
        elif user_input.lower() == 'תוכניות':
            display_plans(data)
        else:
            print(f"קיבלתי את ההודעה שלך: {user_input}")

if __name__ == "__main__":
    main()
