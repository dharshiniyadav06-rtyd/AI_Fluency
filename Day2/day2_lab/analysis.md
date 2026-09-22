# Reasoning and Acting: Comparing Direct Prompting, Chain-of-Thought, and ReAct

## 1. Scenario

For this task, I used a course-fee comparison scenario. The available course fees are:

* CS101 = ₹12,000
* AI202 = ₹18,000
* DS303 = ₹15,000

The main question was:

**Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? And by how much?**

The first option requires retrieving the fees of CS101 and AI202 and calculating the discounted total. The second option requires retrieving all three fees and calculating the discounted total. This scenario therefore contains both a tool-use requirement and multi-step reasoning.

---

## 2. Direct Prompting

Direct prompting asks the language model to answer the question directly without giving it access to external tools.

The model receives the question and immediately produces an answer using the information available in its context or learned knowledge. There is no visible reasoning process and no tool call.

For simple questions, direct prompting can be fast and effective. It is also useful when all the required information is already provided in the prompt.

However, direct prompting cannot independently retrieve information from an external course-fee database in this scenario. If the required fees are not provided to the model, it cannot use the `get_course_fee` tool to obtain them.

The main limitation is therefore its lack of tool access. It may also be less reliable for questions requiring several calculations if the necessary information is not already available.

---

## 3. Chain-of-Thought

Chain-of-Thought prompting asks the model to reason through a problem step by step before producing its final answer.

For example, a multi-step calculation can be broken into smaller reasoning steps before reaching the final result. This can help the model handle problems that require several connected calculations.

In my experiment, I compared direct prompting with Chain-of-Thought on three reasoning questions. Both approaches produced correct answers for all three questions.

The limitation is that Chain-of-Thought does not automatically provide access to external information. It can reason about information it already has, but it cannot independently call the course-fee tool used in the ReAct experiment.

Therefore, Chain-of-Thought is useful for reasoning-heavy problems when the required information is already available, but it is not sufficient by itself when external information must be retrieved.

---

## 4. ReAct Agent

ReAct stands for **Reasoning and Acting**. It combines reasoning with actions performed through tools.

Instead of trying to answer immediately, the agent determines what information it needs, calls an appropriate tool, observes the result, and then continues reasoning.

The cycle can be represented as:

**Thought → Action → Observation → Thought → Action → Observation → Final Answer**

For my scenario, the ReAct agent used two tools:

* `get_course_fee(course_code)` to retrieve course fees
* `calculator(expression)` to perform calculations

The actual tool trace was:

1. `get_course_fee(CS101)` → ₹12,000
2. `get_course_fee(AI202)` → ₹18,000
3. `get_course_fee(DS303)` → ₹15,000
4. Calculator: `(12000 + 18000) × 0.9` → ₹27,000
5. Calculator: `33750 - 27000` → ₹6,750

The final comparison was:

* CS101 + AI202 with 10% scholarship = **₹27,000**
* CS101 + AI202 + DS303 with 25% scholarship = **₹33,750**
* Difference = **₹6,750**

Therefore, the first option costs ₹6,750 less.

ReAct was able to solve the complete scenario because it could retrieve the required facts and then use those results in calculations.

Its limitation is that it requires tool calls, which can increase execution time and cost compared with a simple direct response.

---

## 5. Comparison Table

| Basis for comparison                | Direct Prompting                              | Chain-of-Thought                                                     | ReAct Agent                                                               |
| ----------------------------------- | --------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Reasoning depth                     | Low for complex problems; answers directly    | Higher; breaks a problem into multiple reasoning steps               | High; combines reasoning with actions and observations                    |
| Tool usage                          | No tool usage                                 | No external tool usage in this experiment                            | Uses tools when external information or computation is required           |
| Reliability on multi-step questions | Can make mistakes on complex multi-step tasks | Better for multi-step reasoning when information is available        | Suitable when both reasoning and external information are required        |
| Transparency                        | No visible reasoning process                  | Shows/uses step-by-step reasoning before the answer                  | Tool actions and observations provide a trace of what the agent did       |
| Speed / cost                        | Usually fastest and lowest cost               | Usually slower than direct prompting because of additional reasoning | Usually slower and potentially more costly because of multiple tool calls |
| Consistency across repeated runs    | Can vary depending on temperature             | Can vary between runs at non-zero temperature                        | Depends on the model, tools, and temperature                              |

---

## 6. Self-Consistency Observation

I used the instalment calculation question for the self-consistency experiment.

The correct answer is:

**₹9,562.50 per instalment**

At a temperature of **0.8**, I ran the question five times. The wording and formatting of the answers varied slightly, but the numerical answer remained the same. The majority result was **3 out of 5** for the same extracted answer format.

I then changed the temperature to **0** and ran the same question five times again. All five runs produced the same numerical answer of **₹9,562.50**.

This shows that lowering the temperature made the outputs more consistent for this particular question. However, consistency alone does not guarantee correctness; the answer must still be checked against the actual calculation.

---

## 7. Suitability Analysis

For my chosen course-fee scenario, the ReAct approach is suitable because the problem requires both external information and reasoning.

Direct prompting can provide a quick answer when all the required information is already available. Chain-of-Thought is useful when the information is available but the problem requires several reasoning steps.

In this scenario, however, the agent needs to retrieve course fees before performing the calculations. ReAct handles this by calling the course-fee tool, observing the results, and then using the calculator tool.

The experiment also showed that self-consistency can improve output stability when the temperature is reduced to zero. Therefore, consistency can be useful when checking repeated reasoning outputs, but it should not replace verification of the actual answer.

---

## 8. Conclusion

The three approaches are useful for different types of problems.

**Direct prompting** is appropriate for simple questions where the model already has all the required information and no external tool is needed. It is generally fast and simple.

**Chain-of-Thought** is useful for problems that require multiple reasoning steps but can be solved using the information already available to the model. It can help organize complex calculations and logical reasoning.

**ReAct** is appropriate when a problem requires both reasoning and interaction with external tools or information sources. It follows a cycle of Thought, Action, and Observation and can use the results of tools before producing the final answer.

Overall, the main difference is that direct prompting answers directly, Chain-of-Thought focuses on deeper multi-step reasoning, and ReAct combines reasoning with actions and observations from tools.
