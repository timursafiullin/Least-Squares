from processor import *

file_name = input("Enter file name: ")

try:
    data = get_data(file_name=file_name) # Get values (x, y) from text file
except Exception as e:
    print('Something went wrong when reading data file.')
    print(f"Error: {e}")
    raise SystemExit(1) # Exit program, if data does not exist


"""
// In progress

try:
    config = get_config(file_name='config.ini') # Get settings from 'config.ini'
except Exception as e:
    print('Something went wrong when reading config file.')
    print('Error:', e)
    raise SystemExit(2) # Exit from program

"""


# Check if needs to show data in console
if True:
    print("Your data:", data)


try:
    print("Starting calculations...")
    calculated_result = calculate(data) # Calculate result
    make_plot(data=calculated_result, file_name=file_name)
except Exception as e:
    print('Error:', e)
    raise SystemExit(3)