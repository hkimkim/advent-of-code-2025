"""
DAY TWO Y'ALL

Approach for Part One:

1. Split the ranges (",") and store each range into an array
2. Iterate over the array 
3. For each element, split the range by "-" 
4. Create a while loop for the first id and last id 
5. Define two poitners where first pointer points to the first element of number and second pointer is lenght of number / 2
6. If first element and second pointer is the same move both pointer to right (condition p1 < p2)
7. If p1 reaches p2 -> convert the number into integer and add to sum
8. return the over all sum.
"""

INPUT = "194-253,81430782-81451118,7709443-7841298,28377-38007,6841236050-6841305978,2222204551-2222236166,2623-4197,318169-385942,9827-16119,580816-616131,646982-683917,147-181,90-120,3545483464-3545590623,4304-5747,246071-314284,8484833630-8484865127,743942-795868,42-53,1435-2086,50480-60875,16232012-16441905,94275676-94433683,61509567-61686956,3872051-4002614,6918792899-6918944930,77312-106847,282-387,829099-1016957,288251787-288311732,6271381-6313272,9877430-10095488,59-87,161112-224439,851833788-851871307,6638265-6688423,434-624,1-20,26-40,6700-9791,990-1307,73673424-73819233" 
EXAMPLE_INPUT = "11-22, 95-115, 998-1012, 1188511880-1188511890, 222220-222224, 1698522-1698528, 446443-446449, 38593856-38593862, 565653-565659, 824824821-824824827, 2121212118-2121212124"

def partOne():
    sum = 0

    # ranges = INPUT.split(",")
    ranges = EXAMPLE_INPUT.split(",")
    
    for range in ranges:
        id_range = range.split("-")
        first_id = int(id_range[0])
        second_id = int(id_range[1])

        num = first_id
        while (num <= second_id):

            # When length is even
            if (len(str(num))) % 2 == 0:
                p1 = 0
                p2 = len(str(num)) // 2
                mid_point = len(str(num)) // 2

                while (p1 < mid_point):
                    if (str(num)[p1] == str(num)[p2]):
                        p1 += 1
                        p2 += 1

                    else:
                        break
                
                    if (p1 == mid_point):
                        sum += num
            
            num += 1

    return sum


def partTwo():
    sum = 0

    #ranges = EXAMPLE_INPUT.split(",")
    ranges = INPUT.split(",")

    
    for range in ranges:
        id_range = range.split("-")
        first_id = int(id_range[0])
        second_id = int(id_range[1])

        num = first_id
        while (num <= second_id):

            num_length = len(str(num))
            # For a number sequence to repeat at least twice, length of sequence needs to be equal or smaller than length / 2 
            mid_point = num_length // 2
            mod = mid_point

            count = 0
            while (mod > 0):
                # For a sequence of number to be repeated, length of repeating number has to be a factor of length of number
                if (num_length % mod == 0):
                    p1 = 0
                    p2 = mod 

                    while (p2 < num_length):
                        if (str(num)[p1] == str(num)[p2]):

                            if (p2 == num_length - 1):
                                count += 1
                            
                            p1 += 1
                            p2 += 1

                        # if not repeating, skip
                        else:
                            break 

                mod -= 1

            if (count > 0):
                print(num)
                sum += num

            num += 1

    return sum

if __name__ == "__main__":
    #result = partOne()
    result = partTwo()
    print(result)