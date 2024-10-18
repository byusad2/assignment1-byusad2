def findRent(start,end):
 # my code goes here
    if start < 0 or start > 24 or end < 0 or end > 24 or start >= end:
        return "Invalid input"

    total_amount = 0
    for hour in range(start, end):
        if 0 <= hour < 7 or 21 <= hour < 24:
            rate = 500
        elif 7 <= hour < 10 or 19 <= hour < 21:
            rate = 1000
        else:  
            rate = 1500
        total_amount += rate
    return f"The total amount to be paid is: RWF {total_amount}"
start = int(input("Enter start time: "))
end = int(input("Enter end time: "))
print(findRent(start, end))
