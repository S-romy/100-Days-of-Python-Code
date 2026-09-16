class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, origin_airport_name="N/A",
                 destination_airport_name="N/A", stops=0, layover_location="N/A", airline="N/A"):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.origin_airport_name = origin_airport_name
        self.destination_airport_name = destination_airport_name
        self.stops = stops
        self.layover_location = layover_location
        self.airline = airline


def find_cheapest_flight(data, return_date):
    flights = data.get("best_flights", []) + data.get("other_flights", [])
    if not flights:
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A"
        )

    cheapest = None

    for flight in flights:
        try:
            if cheapest is None or flight["price"] < cheapest["price"]:
                cheapest = flight
        except KeyError:
            pass

    if cheapest is None:
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
        )

    nr_stops = len(cheapest["flights"]) - 1

    if nr_stops == 1:
        layover_location = cheapest["flights"][0]["arrival_airport"]["name"]
    else:
        layover_location = "N/A"

    return FlightData(
        price=cheapest["price"],
        origin_airport=cheapest["flights"][0]["departure_airport"]["id"],
        destination_airport=cheapest["flights"][-1]["arrival_airport"]["id"],
        out_date=cheapest["flights"][0]["departure_airport"]["time"].split(" ")[0],
        return_date=return_date,
        origin_airport_name=cheapest["flights"][0]["departure_airport"]["name"],
        destination_airport_name=cheapest["flights"][-1]["arrival_airport"]["name"],
        stops=nr_stops,
        layover_location=layover_location,
        airline=cheapest["flights"][0]["airline"]
    )
