from graphics import *

# Function to calculate progression outcome based on credits
def calculate_progression_outcome(credits_at_pass, credits_at_defer, credits_at_fail):
    if credits_at_pass >= 100:
        if credits_at_pass > 100:
            return 1
        else:
            return 2
    elif credits_at_pass <= 40:
        if credits_at_fail >= 80:
            return 4
        else:
            return 3
    else:
        return 3

# Function to draw a histogram based on categories and values
def draw_histogram(categories, values):
    win = GraphWin("Histogram", 500, 300)
    win.setBackground("white")

    # Calculate parameters for drawing bars
    max_value = max(values)
    total_results = sum(values)
    bar_width = 60
    spacing = 20
    x = 100


    colors = ["lightblue", "lightgreen", "purple", "pink"]

    # Add title to the histogram
    title = Text(Point(win.getWidth() // 2, 20), "Histogram Results")
    title.setSize(14)
    title.setStyle("bold")
    title.draw(win)

    # Loop through categories, values, and colors to draw bars
    for category, value, color in zip(categories, values, colors):
        height = (value / max_value) * 200
        bar = Rectangle(Point(x, 250 - height), Point(x + bar_width, 250))
        bar.setFill(color)
        bar.draw(win)

        label = Text(Point(x + bar_width // 2, 260), category)
        label.draw(win)

        result_text = Text(Point(x + bar_width // 2, 250 - height - 10), int(value))
        result_text.draw(win)

        x += bar_width + spacing

    # Add total outcomes text to the window
    total_text = Text(Point(win.getWidth() // 2, 280), f"Total Outcomes: {total_results}")
    total_text.draw(win)

# Main program
list = []

progress = 0
trailer = 0
retriever = 0
excluded = 0

while True:
    while True:
        # Get input for credits at pass, ensuring it's an integer within a valid range
        credits_at_pass = input("Please enter your credits at pass: ")
        try:
            credits_at_pass = int(credits_at_pass)
            if credits_at_pass in (0, 20, 40, 60, 80, 100, 120):
                break
            else:
                print("Out of range")
                continue
        except:
            print("Integer required")
            continue
        
    while True:
        credits_at_defer = input("Please enter your credits at defer: ")
        try:
            credits_at_defer = int(credits_at_defer)
            if credits_at_defer in (0, 20, 40, 60, 80, 100, 120):
                break
            else:
                print("Out of range")
                continue
        except:
            print("Integer required")
            continue

    while True:
        credits_at_fail = input("Please enter your credits at fail: ")
        try:
            credits_at_fail = int(credits_at_fail)
            if credits_at_fail in (0, 20, 40, 60, 80, 100, 120):
                break
            else:
                print("Out of range")
                continue
        except:
            print("Integer required")
            continue
        
    if credits_at_pass + credits_at_defer + credits_at_fail == 120:

        # Determine progression outcome and update counters
        if calculate_progression_outcome(credits_at_pass, credits_at_defer, credits_at_fail) == 1:
            progression_outcome = "Progress"
            print(progression_outcome)
            list.append(f"{progression_outcome} - {credits_at_pass}, {credits_at_defer}, {credits_at_fail}")
            progress += 1
        elif calculate_progression_outcome(credits_at_pass, credits_at_defer, credits_at_fail) == 2:
            progression_outcome = "Progress (module trailer)"
            print(progression_outcome)
            list.append(f"{progression_outcome} - {credits_at_pass}, {credits_at_defer}, {credits_at_fail}")
            trailer += 1
        elif calculate_progression_outcome(credits_at_pass, credits_at_defer, credits_at_fail) == 3:
            progression_outcome = "Do not progress - module retriever"
            print(progression_outcome)
            list.append(f"{progression_outcome} - {credits_at_pass}, {credits_at_defer}, {credits_at_fail}")
            retriever += 1
        elif calculate_progression_outcome(credits_at_pass, credits_at_defer, credits_at_fail) == 4:
            progression_outcome = "Exclude"
            print(progression_outcome)
            list.append(f"{progression_outcome} - {credits_at_pass}, {credits_at_defer}, {credits_at_fail}")
            excluded += 1

        # Prompt user to continue or quit and view results
        while True:
            continue_or_no = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
            print()
            try:
                if continue_or_no == "y":
                    continue_or_no = True
                    break
                elif continue_or_no == "q":
                    continue_or_no = False
                    break
            except:
                continue


        if continue_or_no == True:
            continue
        else:
            # If user wants to quit, draw histogram, print results, and write to a file
            x = ["Progress", "Trailer", "Retriever", "Excluded"]
            y = [progress, trailer, retriever, excluded]

            draw_histogram(x, y)

            print("\nResults: ")
            for result in list:
                print(result)
                
            # Function to save progression data to a file
            with open("progression_outcome.txt", "w") as file:
                for value in list:
                    file.write(value + "\n")

            # Exit the outer loop
            break

    else:
        print("Total incorrect")
        continue
