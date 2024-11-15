n=int(input())
flight_data = {}
for i in range(1):
    flight_id, departure_airport_id, arrival_airport_id, departure_time, arrival_time = input().split()
    new_flight = {"departure_airport_id": departure_airport_id, "arrival_airport_id": arrival_airport_id, "departure_time":departure_time, 
                    "arrival_time":arrival_time}
    flight_data[str(flight_id)] = new_flight
    
print(flight_data)