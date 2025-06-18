# tests for the get files info function
from functions.get_files_info import get_files_info

# Run the function with different parameters and print the results
print("Result for get_files_info('calculator', '.'):")
result1 = get_files_info("calculator", ".")
print(result1)

print("\nResult for get_files_info('calculator', 'pkg'):")
result2 = get_files_info("calculator", "pkg")
print(result2)

print("\nResult for get_files_info('calculator', '/bin'):")
result3 = get_files_info("calculator", "/bin")
print(result3)

print("\nResult for get_files_info('calculator', '../'):")
result4 = get_files_info("calculator", "../")
print(result4)