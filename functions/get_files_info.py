import os 

def get_files_info(working_directory, directory=None):
    if directory:
        # Path to the subdirectory to inspect
        target_path = os.path.join(working_directory, directory)
    else:
        # Default to the root of the working directory
        target_path = working_directory
    
    # Security check: Resolve real paths to prevent traversal attacks (e.g., '..')
    real_working_dir = os.path.realpath(working_directory)
    real_target_path = os.path.realpath(target_path)

    if not real_target_path.startswith(real_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Validation check: Ensure the target is a directory
    if not os.path.isdir(real_target_path):
        # Use the original 'directory' name for a more user-friendly error
        dir_name_for_error = directory if directory else working_directory
        return f'Error: "{dir_name_for_error}" is not a directory'

    try:
        response = ''
        for item_name in sorted(os.listdir(real_target_path)):
            item_path = os.path.join(real_target_path, item_name)

            is_dir = os.path.isdir(item_path)
            # For directories, size can be misleading, but we'll show what the OS reports.
            file_size = os.path.getsize(item_path)
            response += f'- {item_name}: file_size={file_size} bytes, is_dir={is_dir}\n'
        
        if not response:
            return "Directory is empty."
            
        return response
    except Exception as e:
        return f'Error: An unexpected error occurred: {str(e)}'