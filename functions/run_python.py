import os
import subprocess

def run_python_file(working_directory, file_path):
    real_file_path = os.path.realpath(os.path.join(working_directory,file_path))
    real_working_dir = os.path.realpath(working_directory)

    if not real_file_path.startswith(real_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(real_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path[-3:]=='.py':
        return f'Error: "{file_path}" is not a Python file.'
    
    result = subprocess.run(
        ['python3', real_file_path],
        cwd=real_working_dir,
        capture_output=True,
        timeout=30
    )
    try:
        output= f"STDOUT:{result.stdout} STDERR: {result.stderr}"
        if result.returncode !=0:
            output.append(f"Process exited with code {result.returncode}")
        if not output:
            return "No output produced"
        return output
    except Exception as e:
        return f"Error: executing Python files: {e}"
    
    