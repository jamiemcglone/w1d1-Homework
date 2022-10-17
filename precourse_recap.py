# A simple program that calculates how many years until you turn a certain age

def how_many_years(current_age, future_age):
    years = future_age - current_age
    return(f"You will be {future_age} in {years} years.")

print(how_many_years(22, 77))
print(how_many_years(19, 44))
print(how_many_years(65, 902))
