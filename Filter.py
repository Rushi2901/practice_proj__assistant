import re

def extract_code_block(text):
    # Regular expression to find the code block
    code_block_pattern = re.compile(r'```[\s\S]*?```')
    match = re.search(code_block_pattern, text)
    if match:
        remove=  match.group(0) 
        final= remove.replace("python","").replace("```","")
        return final  # Return the matched code block
    else:
        return "No code block found"