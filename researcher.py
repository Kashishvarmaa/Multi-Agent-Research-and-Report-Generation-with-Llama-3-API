from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client with the Llama API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Create a prompt template
researcher_prompt = "Research and provide detailed information on the topic: {topic}"

# Function to get research data
def researcher_agent_function(topic):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": researcher_prompt.format(topic=topic)},
        ],
        model="llama-3.3-70b-versatile",  # Replace with the correct model
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    
    # Extract and return the completion response
    return chat_completion.choices[0].message.content

# Example usage
if __name__ == "__main__":
    topic = "Artificial Intelligence"
    print("Researching topic...")
    research_data = researcher_agent_function(topic)
    print("Research data:", research_data)