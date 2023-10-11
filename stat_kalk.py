import sys
sys.path.append('/Users/fredericstrand/Desktop/python_intro/')
import inf120stat.py

def choose_action():
    print("Hovedmeny:")
    print("1. Les inn verdier")
    print("2. Fjern alle verdier")
    print("3. Vis gjennomsnitt og standardavvik")
    print("4. Liste ut alle verdier")
    print("5. Avslutt")    
    
    while True:
        choice = input("Velg en handling (1-5): ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return int(choice)
        else:
            print("Ugyldig valg. Prøv igjen.")
            
def read_values(values):
    while True:
        input_value = input("Skriv inn et tall (trykk Enter for å avslutte):")
        if not input_value:
            break
        try:
            value = float(input_value)
            values.append(value)
        except ValueError:
            print("Ugyldig tall. Prøv igjen.")
            
def print_statistics(values):
    if not values:
        print("Ingen verdier å beregne statistikk for.")
        return
    
    mean = inf120stat.mean(values)
    std = inf120stat.std(values)
    
    if mean is None or std is None:
        print("Kan ikke beregne statistikk for disse verdiene.")
    else:
        print(f"Gjennomsnitt: {mean}")
        print(f"Standardavvik: {std}")
        
def main():
    values = []
    
    while True:
        action = choose_action()
        
        if action == 1:
            read_values(values)
        elif action == 2:
            values.clear()
        elif action == 3:
            print_statistics(values)
        elif action == 4:
            if not values:
                print("Det er ingen verdier i denne listen")
            else:
                for value in values:
                    print(value)
        elif action == 5:
            print("Avslutter programmet")
            break
            
if __name__ == "__main__":
    main()
        