import os
import json
from pathlib import Path

def load_json(file_path):
    """Load a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def load_config(config_path):
    """Load and validate the config file."""
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Validate required fields
    required_fields = ["project_name", "author", "email"]
    for field in required_fields:
        if field not in config or not config[field].strip():
            raise ValueError(f"Missing or empty required field: {field}")
    
    # Add defaults if optional fields are missing
    config.setdefault("version", "0.1.0")
    config.setdefault("license", "MIT")
    config.setdefault("github_repo", f"https://github.com/{config['author']}/{config['project_name']}")
    config.setdefault("optional_modules", {"logging": False, "cli": False})
    config.setdefault("custom_directories", [])
    config.setdefault("custom_files", {})
    
    return config

def replace_placeholders(content, placeholders):
    """Replace placeholders in content with actual values."""
    for key, value in placeholders.items():
        # Convert non-string values to JSON strings for replacement
        if not isinstance(value, str):
            value = json.dumps(value, indent=4)  # Serialize as JSON string
        content = content.replace(f"{{{{ {key} }}}}", value)
    return content

def create_file(file_path, content):
    """Create a file with the given content."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(content)

def create_project(project_structure, file_contents, config):
    """Create project files and directories based on the structure and contents."""
    for directory, files in project_structure.items():
        resolved_directory = directory.replace("{{ project_name }}", config["project_name"])
        for file_name in files:
            file_path = os.path.join(resolved_directory, file_name)
            content = file_contents.get(file_name, "")
            content = replace_placeholders(content, config)
            create_file(file_path, content)

def extend_project_structure(structure, additional_dirs, additional_files):
    """Dynamically extend the project structure."""
    for dir_name in additional_dirs:
        structure[dir_name] = []

    for file_path, content in additional_files.items():
        dir_name = os.path.dirname(file_path)
        if dir_name not in structure:
            structure[dir_name] = []
        structure[dir_name].append(os.path.basename(file_path))
    
    return structure

def add_optional_modules(file_contents, placeholders, optional_features):
    """Add optional feature snippets to file contents."""
    project_name = placeholders['project_name']

    # Ensure the utils.py file exists in file_contents
    utils_key = f"{project_name}/src/utils.py"
    if utils_key not in file_contents:
        file_contents[utils_key] = '"""Utility Functions"""\n'

    if optional_features.get("logging"):
        file_contents[utils_key] += """
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)
"""

    # Ensure the main.py file exists in file_contents
    main_key = f"{project_name}/src/main.py"
    if main_key not in file_contents:
        file_contents[main_key] = '"""Main entry point"""\n'

    if optional_features.get("cli"):
        file_contents[main_key] += """
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='{{ project_name }} CLI')
    parser.add_argument('--example', type=str, help='Example argument')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print(f"Example argument: {args.example}")
"""
    return file_contents

def main():
    print("Welcome to the Configurable Dynamic Project Generator!")

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct paths to config.json and templates
    config_path = os.path.join(script_dir, 'config.json')
    project_structure_path = os.path.join(script_dir, 'project_structure.json')
    file_contents_path = os.path.join(script_dir, 'file_contents.json')

    # Load and validate config.json
    try:
        config = load_config(config_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading config.json: {e}")
        return

    # Load project structure and file contents templates
    try:
        project_structure = load_json(project_structure_path)["structure"]
        file_contents = load_json(file_contents_path)
    except FileNotFoundError as e:
        print(f"Error loading project template files: {e}")
        return

    # Extend structure with custom directories and files from config
    project_structure = extend_project_structure(
        project_structure, 
        config.get("custom_directories", []), 
        config.get("custom_files", {})
    )

    # Add optional modules based on config
    file_contents = add_optional_modules(file_contents, config, config["optional_modules"])
    
    # Create project files and structure
    create_project(project_structure, file_contents, config)
    
    print(f"\nProject '{config['project_name']}' has been created successfully!")
    print("Customize your new project as needed. Happy coding!")

if __name__ == "__main__":
    main()
