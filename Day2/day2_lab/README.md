# Agentic AI — Day 2 Lab

## Overview

This lab explores three important techniques used in Agentic AI:

* ReAct (Reason + Act)
* Chain-of-Thought prompting
* Self-Consistency

The experiments were implemented in Python using the same agent setup and model environment from Day 1.

## Objectives

* Trace a multi-step ReAct agent manually and compare it with the actual agent trace.
* Compare model responses with and without Chain-of-Thought prompting.
* Understand how temperature affects repeated model responses.
* Implement self-consistency using majority voting.

## Project Structure

```text
day2_lab/
├── agent.py
├── config.py
├── tools.py
├── react_trace.py
├── cot_compare.py
├── self_consistency.py
├── observations.md
├── .gitignore
└── screenshots/
```

## Part A & B — ReAct

The question used for the ReAct experiment was:

> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? By how much?

The agent retrieved the three course fees and used the calculator tool to compare the discounted totals.

### Result

* CS101 + AI202 with 10% scholarship = **₹27,000**
* All three courses with 25% scholarship = **₹33,750**
* Difference = **₹6,750**
* Cheaper option = **CS101 + AI202 with 10% scholarship**

The actual agent completed the task correctly using 5 tool-call steps.

## Part C — Chain-of-Thought Comparison

Three questions were tested with:

1. A direct prompt without Chain-of-Thought
2. A step-by-step Chain-of-Thought prompt

All three questions were answered correctly in both conditions.

The Chain-of-Thought responses were longer because they included intermediate calculations or reasoning steps.

## Part D — Self-Consistency

The same problem was run five times using Chain-of-Thought prompting.

### Temperature 0.8

The runs produced equivalent correct answers, with minor differences in formatting.

Majority answer:

**₹9,562.5 per instalment**

### Temperature 0

All five runs produced the same answer:

**₹9,562.5 per instalment**

This demonstrates that temperature 0 produced highly consistent outputs for this experiment.

## Key Learnings

### ReAct

ReAct combines reasoning with actions and observations. Tools allow the agent to retrieve information or perform calculations that the language model cannot obtain from prompting alone.

### Chain-of-Thought

Chain-of-Thought prompting asks the model to work through a problem step by step. It can make intermediate calculations easier to inspect, but produces longer responses.

### Self-Consistency

Self-consistency runs the same reasoning task multiple times and uses the most common final answer. It is useful when different reasoning paths may produce different answers.

## Technologies Used

* Python
* OpenAI-compatible chat completion API
* Groq model endpoint
* ReAct agent pattern
* Chain-of-Thought prompting
* Self-Consistency
* Python tools and functions

## Files

| File                  | Purpose                                        |
| --------------------- | ---------------------------------------------- |
| `agent.py`            | ReAct agent implementation                     |
| `config.py`           | Model and API configuration                    |
| `tools.py`            | Course-fee and calculator tools                |
| `react_trace.py`      | Runs the ReAct experiment                      |
| `cot_compare.py`      | Compares direct and CoT prompting              |
| `self_consistency.py` | Runs multiple CoT attempts and majority voting |
| `observations.md`     | Lab observations and discussion answers        |

## Conclusion

This lab demonstrated how tool use, struct
