
import subprocess

def run_newman_command(collection_file, environment_file):
    try:
        # Construct the newman command with reporters cli
        command = f"newman run {collection_file} -g {environment_file} -r json"

        # Execute the newman command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 1:
            # Print the captured summary output
            print("Summary:", result.stdout)
        else:
            # Print error message
            print("Error:", result.stderr)
    except Exception as e:
        # Handle any exceptions
        print("An error occurred:", e)

# Example usage
collection_file = "/Users/niraj/Downloads/Locate_new_automation.postman_collection.json"
environment_file = "/Users/niraj/Downloads/locate_environment_automation_parent.postman_environment.json"
run_newman_command(collection_file, environment_file)
