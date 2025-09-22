task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        response = "is a high priority task"
    case "medium":
        response = "is a medium priority task"
    case "low":
        response = "is a low priority task"

if time_bound == "yes":
    time = " that requires immediate attention today!"
elif time_bound == "no":
    time = ". Consider completing it when you have free time."

print(f"Reminder: '{task}' " + response + time)
