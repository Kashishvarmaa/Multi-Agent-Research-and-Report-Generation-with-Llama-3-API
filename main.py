from dotenv import load_dotenv
import os
from researcher import researcher_agent_function
from writer import writer_agent_function
from editor import editor_agent_function

# Load the .env file containing the API key
load_dotenv()

# Main orchestration function
def main():
    topic = "Artificial Intelligence"  # Dynamic topic input
    print("Researching topic...")
    
    # Step 1: Researcher gathers information
    research_data = researcher_agent_function(topic)
    
    print("Writing report...")
    
    # Step 2: Writer generates the report
    report = writer_agent_function(research_data)
    
    print("Editing report...")
    
    # Step 3: Editor refines the report
    edited_report = editor_agent_function(report)
    
    print("Final Report:")
    print(edited_report)

if __name__ == "__main__":
    main()