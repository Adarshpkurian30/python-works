# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 01:27:58 2025

@author: adarshpkurian30

Assumptions:
    max time that can be set in a traffic signal timer =150seconds
    min time that can be set in a traffic signal timer =5 seconds
    average speed of vehicles while passing the junction =25 km/hr=6.94m/s
    assume no gaps b/w vehicles
    average vehicle length =4m
    distance=6.94*120=832.8
    max no of vehicles within 120seconds=832.8/4=208.2(but considering several factors no is limited to)
    =150
    so time(T) allotted for each vehicle=no.of vehicles/1.25=n/1.25
    
"""

import time

# The variable count is correctly initialized
count = 0

def traffic(count):
    # Initialize the dictionary to store IDs and their corresponding values
    arr = {
        "id": ['N', 'S', 'E', 'W'],
        "value": [0, 0, 0, 0]    
    }
    
    while True:
        count += 1  # Increment the counter to track system runs
        print("Number of times system run:", count)
        
        try:
            
            
            # Accept input values for IDs
            a = int(input("Enter value of N: "))
            b = int(input("Enter value of S: "))
            c = int(input("Enter value of E: "))
            d = int(input("Enter value of W: "))

            def signalchange(a, b, c, d):
                nonlocal arr  # Access the external arr variable
                
                
                # Adding the values to the corresponding IDs
                id_of_a = 'N'
                id_of_b = 'S'
                id_of_c = 'E'
                id_of_d = 'W'

                # Check if the ID exists in the dictionary and update its value
                if id_of_a in arr["id"]:
                    index = arr["id"].index(id_of_a)
                    arr["value"][index] += a
                    print(arr["value"][index])
                if id_of_b in arr["id"]:
                    index = arr["id"].index(id_of_b)
                    arr["value"][index] += b
                    print(arr["value"][index])
                if id_of_c in arr["id"]:
                    index = arr["id"].index(id_of_c)
                    arr["value"][index] += c
                    print(arr["value"][index])
                if id_of_d in arr["id"]:
                    index = arr["id"].index(id_of_d)
                    arr["value"][index] += d
                    print(arr["value"][index])

               
                
                sorted_pairs = sorted(zip(arr["value"], arr["id"]), reverse=True)  # Sort in descending order
                arr["value"], arr["id"] = zip(*sorted_pairs)  # Unzip the sorted pairs back into separate lists
                arr["value"] = list(arr["value"])  # Convert tuple back to list
                arr["id"] = list(arr["id"])  # Convert tuple back to list

                
                for i in range(len(arr["value"])):
                    if arr["value"][i] != 0:
                        T = arr["value"][i] / 1.25
                        if T > 120:
                            T = 120
                            temp = arr["value"][i]-150  
                            arr["value"][i] = temp
                        
                            print(f"Time for green signal is {T} seconds (ID: {arr['id'][i]})")
                            time.sleep(temp)
                        elif T >= 5:
                            temp1=arr["value"][i]
                            arr["value"][i] = 0
                            
                            print(f"Time for green signal is {T} seconds (ID: {arr['id'][i]})")
                            time.sleep(temp1)
                        else:
                            arr["value"][i] = 0
                            T = 5
                            print(f"Time for green signal is {T} seconds (ID: {arr['id'][i]})")
                            time.sleep(5)

            signalchange(a, b, c, d)

            # Allow the user to stop the simulation
            cont = input("Do you want to continue? (yes/no): ").strip().lower()
            if cont == "no":
                print("Exiting traffic signal simulation...")
                break

        # to handle interruptions
        except KeyboardInterrupt:
            print("\nTraffic signal simulation interrupted by user. Exiting...")
            break
        # to Handle invalid inputs
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

# Call the traffic function to start the simulation
traffic(count)
