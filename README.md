# LLM Research Assistant

This project uses Groq's API to build a research assistant system that can research a given topic, generate a detailed report, and allow for editing and finalizing the report.

## Features

- **Researching**: Retrieves detailed information on a given topic.
- **Writing**: Generates a comprehensive report based on research data.
- **Editing**: Provides functionality to edit and refine the generated report.

## Installation

### Prerequisites

- Python 3.7+
- Install required libraries using `pip`:
```bash
pip install -r requirements.txt
```
- Create a .env file in the root directory and add your GROQ_API_KEY.
```bash
GROQ_API_KEY=your_api_key_here
```
## Files
1.	researcher.py: Retrieves detailed research data on a topic using the Groq API.
2.	writer.py: Generates a report from the research data.
3.	editor.py: Provides editing capabilities for the generated report.
4.	main.py: Main script to run the research, writing, and editing sequence.

## Usage 
Run the main.py file to initiate the sequence
```bash
python main.py
```
## Steps
- The script will first research the topic.
- Then, it will generate a report.
- Finally, the report will be edited.

## Example
When you run main.py with the topic "Artificial Intelligence", it will:
1.	Research the topic.
2.	Generate a report with the findings.
3.	Output the final report.

 ```bash
Researching topic...
Writing report...
Report: [Generated report content]
```



