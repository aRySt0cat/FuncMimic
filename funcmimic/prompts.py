DEFAULT_PROMPT="""\
Below is the docstring for a Python function.
From its content, infer the function's intended behavior and return the value as the specified type.

First, output the step-by-step process to get the result.
You always need to call the result_parser function at last, no matter how results are simple.

# Docstring

{docstring}


# Input Argument

{args}

# Step-by-step Process
"""