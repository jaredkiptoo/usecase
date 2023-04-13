# Create an instance of the Glissade engine with a last service date of 2022-01-01, current mileage of 5000, and last service mileage of 0
glissade_engine = Glissade(datetime(2022, 1, 1), 5000, 0)

# Check if the engine needs service - this should return False since the last service date is less than 2 years ago and the mileage is less than 30,000
print(glissade_engine.needs_service()) # False

# Update the current mileage to 28000
glissade_engine.current_mileage = 28000

# Check if the engine needs service - this should return False since the last service date is less than 2 years ago but the mileage is more than 30,000
print(glissade_engine.needs_service()) # False

# Update the last service date to 2020-01-01
glissade_engine.last_service_date = datetime(2020, 1, 1)

# Check if the engine needs service - this should return True since the last service date is more than 2 years ago
print(glissade_engine.needs_service()) # True

# Update the last service mileage to 25000
glissade_engine.last_service_mileage = 25000

# Check if the engine needs service - this should return True since the last service date is more than 2 years ago and the mileage is more than 30,000
print(glissade_engine.needs_service()) # True

