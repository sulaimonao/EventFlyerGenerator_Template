**Dynamic Project Generator: Generating a Codebase for an Event Flyer Creator**

Using the dynamic project generator template, we'll create a complete codebase for an application that receives text input for an event flyer and outputs a fully designed flyer. This application will utilize the OpenAI API to generate the flyer content and design elements.

---

### Overview

The project will:

- Accept textual input describing event details.
- Use the OpenAI API to generate a flyer design and content.
- Output a fully designed flyer in a chosen format (e.g., PDF or image).

---

#### 1. `config.json`

**Explanation**:

- **Project Details**:
  - `"project_name"`: Name of the project.
  - `"author"` and `"email"`: Your personal details.
- **Optional Modules**:
  - Enabled `"logging"` and `"cli"` for enhanced functionality.
- **Custom Directories**:
  - `"assets"`: For storing static files like images.
  - `"templates"`: For template files used in flyer generation.
- **Custom Files**:
  - `README.md`: Project overview.
  - `requirements.txt`: Lists project dependencies.
  - `.gitignore`: Files and directories to exclude from version control.

---

#### 2. `project_structure.json`

**Explanation**:

- **Directories**:
  - `"src"`: Source code files.
  - `"tests"`: Unit tests.
  - `"assets"` and `"templates"`: As specified in `custom_directories`.
- **Files**:
  - Core Python modules and scripts.
  - Configuration and setup files in the root directory.

---

#### 3. `file_contents.json`

**Explanation**:

- **`main.py`**:
  - Handles command-line arguments.
  - Calls `generate_flyer` function with input and output paths.
- **`flyer_generator.py`**:
  - Reads event details from the input file.
  - Calls OpenAI API via `openai_client.py`.
  - Generates the flyer using `utils.py`.
- **`openai_client.py`**:
  - Contains function to interact with the OpenAI API.
  - Retrieves flyer content based on event details.
- **`utils.py`**:
  - Contains `create_pdf` function to generate a PDF flyer.
- **`setup.py`**:
  - Configuration for packaging and installing the project.
  - Defines console script entry point.
- **`.env`**:
  - Placeholder for environment variables (e.g., OpenAI API key).
- **`README.md`**:
  - Provides project description, usage instructions, and installation steps.
- **`.gitignore`**:
  - Specifies files and directories to ignore in version control.
- **`requirements.txt`**:
  - Lists project dependencies.

---

### Step 1: Generate the Project

**Run the Project Generator Script**:

```bash
python generate_project.py
```

---

### Step 2: Set Up the Environment

Navigate to the project directory:

```bash
cd EventFlyerGenerator
```

**Create a Virtual Environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Install Dependencies**:

```bash
pip install -r requirements.txt
```

---

### Step 3: Configure the Application

**Set Up Environment Variables**:

- Open the `.env` file in the project root.
- Replace `your_openai_api_key_here` with your actual OpenAI API key.

Example `.env` file:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### Step 4: Prepare Input Data

Create a text file containing the event details.

Example `event_details.txt`:

```
Event Name: Summer Music Festival
Date: July 24, 2025
Time: 2 PM - 11 PM
Location: Central Park, New York City
Description: Join us for a day of live music, food trucks, and fun activities for all ages. Featuring performances by top artists and local bands.
```

---

### Step 5: Run the Application

Use the command-line interface to generate the flyer:

```bash
python src/main.py --input event_details.txt --output summer_music_festival_flyer.pdf
```

**Alternatively**, if you have installed the package:

```bash
eventflyergenerator --input event_details.txt --output summer_music_festival_flyer.pdf
```

---

### Step 6: View the Output

The generated flyer will be saved as `summer_music_festival_flyer.pdf` in the project directory.

---

### Additional Notes

- **Dependencies**:
  - **OpenAI SDK**: For interacting with the OpenAI API.
  - **ReportLab**: For creating PDF documents.
  - **python-dotenv**: For loading environment variables from the `.env` file.

- **Error Handling**:
  - Ensure that the OpenAI API key is correctly set in the `.env` file.
  - Handle exceptions in the code (you may want to add try-except blocks for robustness).

- **Customization**:
  - Modify the `get_flyer_content` function in `openai_client.py` to adjust the prompt sent to the OpenAI API for different styles or additional instructions.
  - Enhance `create_pdf` in `utils.py` to include images, styles, or different layouts.