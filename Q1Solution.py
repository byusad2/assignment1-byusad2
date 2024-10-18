def findRent(start,end):
 # my code goes here 
 def findRent(start, end):
    # Check for invalid input
    if start >= end or start < 0 or end > 24 or start > 24 or end < 0:
        return "Invalid input"

    total_cost = 0
    
    for hour in range(start, end):
        if 0 <= hour < 7 or 21 <= hour <= 23:
            total_cost += 500
        elif 7 <= hour < 10 or 19 <= hour < 21:
            total_cost += 1000
        elif 10 <= hour < 19:
            total_cost += 1500

    return total_cost
start = int(input("Enter start time: "))
end = int(input("Enter end time: "))
print(findRent(start, end))

     