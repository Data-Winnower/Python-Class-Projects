# Kale Perry
# Programming Concepts and Applications
# CSC1570-4914 Fall 2020
# 10 October 2020
# Warp Speed

# This program will convert Warp Speed to metric or Standard/English units.
# We all know that Next Gen was way better than the original.

# Define constants for the speed of light
# speed is in meters/second
# light year is in meters
# distances are in light years
# Because no one who works with the speed of light
# would use the barbaric English/Standard units.
LIGHT_SPEED_METRIC = 299792458
LIGHT_YEAR = 9.461*(10**15)
DIST_PC = 4.24
DIST_V =16
SEC_PER_DAY = 86400

# Define constants for Warp Speed
# Speed of Light will be multiplied by
# this conversion factor to get warp speed
# in selected units
WARP_1 = 1
WARP_2 = 10
WARP_3 = 39
WARP_4 = 102
WARP_5 = 213
WARP_6 = 392
WARP_7 = 656
WARP_8 = 1024
WARP_9 = 1516

# List of available units
# If any additional units are added,
# It needs to be entered here in the position
# of its units number from the get_units function
avail_units = ["ft/sec", "mph", "ft/ns", "knots", "","m/s", "kph", "m/ns","",""]

# Define constants for unit conversions from m/s
# Speed of Light (in m/s) is to be multiplied by this factor to 
# convert to the speed of light in appropriate units
FT_PER_SEC = 3.280839892
MPH = 2.23693629
FT_PER_NANO = 3.280839892*(10**(-9))
KNOTS = 1.94384449#this is not working   
KPH = 3.6
METERS_PER_NANO = 1*(10**(-9))#this is not working
TEST = 0



# Def main function
def main():
    # Function: Annoucement to user
    announce()
    print ("")

    # Function: User chooses std or metric
    std_or_metric = get_std_metric()
    
    # Function: User chooses specific units
    units = get_units(std_or_metric)
    
    # Function: Run appropriate conversion on speed of light to selected units
    speed_of_light = convert_light_speed(units)

    # Function: User chooses warp speed
    warp_speed = get_warp_speed()
    #this is not working
    # Function: Convert Warp to selected units
    converted_warp = convert_warp(warp_speed,speed_of_light)
    
    # Function: Output the results
    print_result(warp_speed, converted_warp, units)

    # Function: Calc time to travel to
    # Proxima Centauri and Planet Vulcan
    extra_credit(warp_speed)

# Define opening annoucement function
def announce():
    print ("HELLO TREKKIES!")
    print ("Let's have some serious nerd fun.")
    print ("This program will convert Warp Speed")
    print ("to the units of your choice")
    go = input ("Hit any key to start.")

# Have user decide between English/Standard or Metric Units
def get_std_metric():
        std_or_metric = input ("Would you like to convert to Metric or English/Standard Units? M/E: ")
        print ("")
        return std_or_metric

# Have user decide the specific units they want
# This function call either the std or metric
# unit choices as appropriate
def get_units(std_or_metric):
    if std_or_metric == "M" or std_or_metric == "m":
        units = get_metric_units()
        
    elif std_or_metric == "E" or std_or_metric == "e":
        units = get_std_units()    

    print ("")
    return units

# Have user select the specific units they want  - English/Standard
def get_std_units():
    print ("You can choose to convert to any of the following:")
    print ("1. feet/second")
    print ("2. miles/hour (mph)")
    print ("3. feet/nanosecond")
    print ("4. knots (nautical miles per hour)")
    
    units_std = int(input("Please select by number. 1/2/3/4: "))
    return units_std

# Have user select the specific units they want  - Metric
def get_metric_units():
    print ("You can choose to convert to any of the following:")
    print ("1. meters/second")
    print ("2. kilometers/hour (kph)")
    print ("3. meters/nanosecond")
    metric_units = int(input("Please select by number. 1/2/3: "))                       

    # Add 3 to make the units differenciable from std
    units_metric = metric_units + 5
    return units_metric
    
# Function to perform the conversion of light speed
def convert_light_speed(units):
    # Convert speed of light to units selected
           
    # 1. Units are ft/sec
    if units == 1:
        speed =  LIGHT_SPEED_METRIC * FT_PER_SEC
    # 2. units are mph
    elif units == 2:
        speed =  LIGHT_SPEED_METRIC * MPH
    # 3. units are ft/ns
    elif units == 3:
        speed =  LIGHT_SPEED_METRIC * FT_PER_NANO
    # 4. units are knots
    elif units == 4:
        print (units)
        speed =  LIGHT_SPEED_METRIC * KNOTS #this is not working
    # 5. CURRENTLY UNDEFINED
    # add'l std units can be added here
    #elif units == 5:
        speed =  LIGHT_SPEED_METRIC
    # 6. units are m/s
    elif units == 6:
        speed =  LIGHT_SPEED_METRIC
    # 7. units are kph
    elif units == 7:
        speed =  LIGHT_SPEED_METRIC * KPH
    # 8. units are m/ns
    elif units == 8:
        print (units)
        speed =  LIGHT_SPEED_METRIC * METERS_PER_NANO #this is not working
    #9. CURRENTLY UNDEFINED
    # add'l metric units can be added here
    #elif units == 9:
        speed =  LIGHT_SPEED_METRIC
    #10. CURRENTLY UNDEFINED
    # add'l metric units can be added here
    #elif units == 10:

    return speed
    


# Have the user define the Warp Speed to be converted
def get_warp_speed():
    warp_speed = int(input("How fast is the Enterprise traveling, in Warp Speed? 1 thru 10: "))
    return warp_speed

# Function to convert warp speed to the selected units
def convert_warp(warp_speed,speed_of_light):
    if warp_speed == 1:
        converted_warp = WARP_1 * speed_of_light
    elif warp_speed == 2:
        converted_warp = WARP_2 * speed_of_light
    elif warp_speed == 3:
        converted_warp = WARP_3 * speed_of_light
    elif warp_speed == 4:
        converted_warp = WARP_4 * speed_of_light
    elif warp_speed == 5:
        converted_warp = WARP_5 * speed_of_light
    elif warp_speed == 6:
        converted_warp = WARP_6 * speed_of_light
    elif warp_speed == 7:
        converted_warp = WARP_7 * speed_of_light
    elif warp_speed == 8:
        converted_warp = WARP_8 * speed_of_light
    elif warp_speed == 9:
        converted_warp = WARP_9 * speed_of_light
    elif warp_speed == 10:
        converted_warp = 0
        print ("Are you crazy? Warp 10 is physically impossible!!!")
        print ("It's a suicide mission!")
    return converted_warp
   
# Function to present results
def print_result(warp_speed, converted_warp, units):
    
    if converted_warp != 0:
        print ("")
        print ("Warp", warp_speed, "converts to", format(converted_warp, ',.0f'), avail_units[units-1])
        print ("")
                    
    else: #in case of Warp 10
        print("")
        



#extra credit time Baby!
def extra_credit(warp_speed):
    if warp_speed == 1:
        travel_time_pc = (DIST_PC * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_1)
        travel_time_v = (DIST_V * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_1)
    elif warp_speed == 2:
        travel_time_pc = (DIST_PC * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_2)
        travel_time_v = (DIST_V * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_2)
    elif warp_speed == 3:
        travel_time_pc = (DIST_PC * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_3)
        travel_time_v = (DIST_V * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_3)
    elif warp_speed == 4:
        travel_time_pc = (DIST_PC * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_4)
        travel_time_v = (DIST_V * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_4)
    elif warp_speed == 5:
        travel_time_pc = (DIST_PC * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_5)
        travel_time_v = (DIST_V * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_5)
    elif warp_speed == 6:
        travel_time_pc = (DIST_PC * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_6)
        travel_time_v = (DIST_V * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_6)
    elif warp_speed == 7:
        travel_time_pc = (DIST_PC * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_7)
        travel_time_v = (DIST_V * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_7)
    elif warp_speed == 8:
        travel_time_pc = (DIST_PC * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_8)
        travel_time_v = (DIST_V * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_8)
    elif warp_speed == 9:
        travel_time_pc = (DIST_PC * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_9)
        travel_time_v = (DIST_V * LIGHT_YEAR) / (SEC_PER_DAY*LIGHT_SPEED_METRIC*WARP_9)


    print ("")
    print ("At that speed, it would take the Enterprise")
    print ("apx.",format(travel_time_pc,',.2f'), "Earth days to reach Proxima Centauri (4.24 light years away)")
    print ("apx.",format(travel_time_v,',.2f'), "Earth days to reach Planet Vulcan (16 light years away)")
    print ("")
    print ("Congrats....You are officially a nerd!")
    


#call the main function
main()
