import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Day_1')))

from config import client, MODEL, banner
from my_tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = (
    "You are a college assistant. Use read_webpage to read any page or file the user "
    "mentions, and use calculator for every arithmetic step. Never guess a number that "
    "should come from a page. If no tool is needed, answer directly."
)


def agent(question, max_steps=6, verbose=True):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )

        message = response.choices[0].message

        if message.tool_calls:

            messages.append({
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": message.tool_calls,
            })

            for call in message.tool_calls:
                name = call.function.name

                try:
                    arguments = __import__("json").loads(call.function.arguments)
                except Exception:
                    arguments = {}

                function = TOOL_FUNCTIONS.get(name)

                if function is None:
                    result = (
                        f"Unknown tool: {name}. "
                        f"Available: {list(TOOL_FUNCTIONS.keys())}"
                    )
                else:
                    try:
                        result = function(**arguments)
                    except Exception as e:
                        result = f"Tool error: {e}"

                if verbose:
                    print(f"step {step}: {name}({arguments}) -> {result}")

                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result),
                })

        else:
            if verbose:
                print(f"step {step}: final answer")

            return message.content

    return "Stopped: maximum steps reached without a final answer."


if __name__ == "__main__":

    banner("Day 3 - ReAct Agent")

    question = input("Q: ")

    answer = agent(question)

    print("\nA:", answer)
