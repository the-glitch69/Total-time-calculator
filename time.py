from datetime import datetime, timedelta
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def calculate_time(start, end):
    try:
        # Check if the input lengths are correct
        if len(start) != 4 or len(end) != 4:
            raise ValueError("Time should be in HHMM format.")
        
        # Convert HHMM format strings to HH:MM format
        start_time = datetime.strptime(f"{start[:2]}:{start[2:]}", '%H:%M')
        end_time = datetime.strptime(f"{end[:2]}:{end[2:]}", '%H:%M')
        
        # Calculate the difference
        if end_time < start_time:
            end_time += timedelta(days=1)  # Add 1 day to end time if it's before start time
        
        time_diff = end_time - start_time
        
        # Extract hours and minutes
        total_minutes = time_diff.total_seconds() / 60
        total_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        total_hours_decimal = total_minutes / 60
        
        return total_hours, remaining_minutes, total_hours_decimal, total_minutes
    
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
        return None

def main():
    while True:
        print(Fore.CYAN + "Time Calculator")
        print(Fore.CYAN + "=====================")
        
        # Input times in HHMM format
        start_time = input(Fore.YELLOW + "Enter the start time (HHMM): ")
        end_time = input(Fore.YELLOW + "Enter the end time (HHMM): ")
        
        print(Fore.CYAN + "\n=====================")
        print(Fore.MAGENTA + "Calculating...")
        print(Fore.CYAN + "=====================\n")
        
        # Calculate total time
        result = calculate_time(start_time, end_time)
        
        if result is not None:
            total_hours, remaining_minutes, total_hours_decimal, total_minutes = result
            
            # Display results
            print(Fore.CYAN + "Results")
            print(Fore.CYAN + "=====================")
            print(Fore.GREEN + f"Start Time: {start_time[:2]}:{start_time[2:]}")
            print(Fore.GREEN + f"End Time: {end_time[:2]}:{end_time[2:]}")
            print(Fore.GREEN + f"Total Time: {int(abs(total_hours))} hours and {int(abs(remaining_minutes))} minutes")
            print(Fore.GREEN + f"Total Time (Decimal): {abs(total_hours_decimal):.2f} hours")
            print(Fore.GREEN + f"Total Time (Minutes): {int(abs(total_minutes))} minutes")
            print(Fore.CYAN + "=====================")
        
        # Ask user if they want to recalculate
        while True:
            choice = input(Fore.YELLOW + "\nDo you want to calculate again? (y/n): ").strip().lower()
            if choice in ('y', 'n'):
                break
            else:
                print(Fore.RED + "Invalid input! Please enter 'y' or 'n'.")
        
        if choice == 'n':
            break
        elif choice == 'y':
            continue

if __name__ == "__main__":
    main()
