import openai
import json

from funcmimic.prompts import DEFAULT_PROMPT

function_dict = {
    "name": "result_parser",
    "description": "The function to print the result. You always need to call this function.",
    "parameters": {
        "type": "object",
        "properties": {
            "result": {
                "type": "object",
                "description": "the result",
            }
        },
        "required": ["result"],
    },
}

def mimic(return_type, prompt=DEFAULT_PROMPT):
    def _mimic(func):
        def wrapper(*args, **kwargs):
            docstring = func.__doc__

            arg_names = func.__code__.co_varnames
            args = dict(zip(arg_names, list(args) + list(func.__defaults__)))
            args.update(kwargs)
            # return_type = func.__annotations__.get("return", None)
            function_dict["parameters"]["properties"]["result"]["type"] = return_type
            content = prompt.format(docstring=docstring, args=args)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": content},
                ],
                functions=[function_dict],
                function_call="auto",
            )
            message = response["choices"][0]["message"]
            if "function_call" in message:
                return json.loads(message["function_call"]["arguments"])["result"]
            else:
                print("ChatGPT did not call the function.")
                print("-"*20)
                print(message["content"])
                print("-"*20)
        return wrapper
    return _mimic
