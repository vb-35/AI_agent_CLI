import os

def write_file(working_directory, file_path, content):
    real_file_path = os.path.realpath(os.path.join(working_directory,file_path))
    real_working_dir = os.path.realpath(working_directory)

    if not real_file_path.startswith(real_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    

    try:
        if not os.path.exists(real_file_path):
            with open(real_file_path, "x") as f:
                f.write(content)
        else:
            with open(real_file_path, "w") as f:
                f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' 
    except Exception as e:
        return f'Error: An unexpected error occurred: {str(e)}'