from datetime import datetime

from engine.capulet_engine import Calliope

# Create a Calliope engine instance with the last service date, current mileage, and last service mileage
calliope_engine = Calliope(last_service_date=datetime(2022, 1, 1).date(), current_mileage=20000, last_service_mileage=10000)

# Determine if the engine needs service
if calliope_engine.needs_service():
    print("The engine needs to be serviced.")
else:
    print("The engine does not need to be serviced yet.")

# Update the engine's mileage after driving for a few thousand miles
calliope_engine.current_mileage = 25000

# Determine if the engine needs service again
if calliope_engine.needs_service():
    print("The engine needs to be serviced.")
else:
    print("The engine does not need to be serviced yet.")
