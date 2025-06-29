import pandas as pd
from smolagents import CodeAgent, InferenceClientModel

def run_agent_prompt(user_prompt, dataframe):
    context = f"""
You are a Python assistant working with a pandas DataFrame named `df`.
It contains skincare product information with these columns:

- 'Product Name'
- 'Views Last Month'
- 'Volume Sold Last Month'

Sample rows:
{dataframe.head(100).to_dict(orient='records')}

TASK:
Write a single line of Python code that defines a variable named `result`
containing a list of product names based on this instruction:

"{user_prompt}"

IMPORTANT:
- Return ONLY executable Python code — no markdown, no <code> tags, no explanation.
- Your response MUST define a variable `result = [...]`
- The value of `result` must be a list of strings.
"""

    
    agent = CodeAgent(
        tools=[],  
        model=InferenceClientModel(),  
        additional_authorized_imports=['pandas', 'numpy']
    )

    output = agent.run(context)
    return str(output).strip()  
