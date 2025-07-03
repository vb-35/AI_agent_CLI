# tests for the get files info function
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

# Run the function with different parameters and print the results
#print("Result for get_files_info('calculator', '.'):")
#result1 = get_files_info("calculator", ".")
#print(result1)
#
#print("\nResult for get_files_info('calculator', 'pkg'):")
#result2 = get_files_info("calculator", "pkg")
#print(result2)
#
#print("\nResult for get_files_info('calculator', '/bin'):")
#result3 = get_files_info("calculator", "/bin")
#print(result3)
#
#print("\nResult for get_files_info('calculator', '../'):")
#result4 = get_files_info("calculator", "../")
#print(result4)



#print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
#print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))