counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#print(counties_dict.values())

#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

#print("\n")

#for county_dict in voting_data:    
#   for value in county_dict:      
#       print(value)

#print("\n")

#for county_dict in voting_data:
#     for key, value in county_dict.items():
#         print(value)
#
#print("\n")
#
#for county_dict in voting_data:
 #    print(county_dict['registered_voters'])

#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voters.")
    #print(f"{county} county has {voters:,} registered voters.")
    
for county_dict in voting_data: 
    print(f"{county_dict['county']} county has registered voters.")