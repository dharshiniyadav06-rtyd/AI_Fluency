# Day 2 Lab Observations

## Part A & B — ReAct Trace

### Paper Trace vs Real Agent

| Item | Paper Trace | Real Agent |
|---|---:|---:|
| Fee lookups | 3 | 3 |
| Calculator calls | 3 | 2 |
| Total steps/tool calls | 6 | 5 |
| Parallel tool calls | No | No |
| Final answer | ₹6,750 cheaper | ₹6,750 cheaper |
| Correct | Yes | Yes |

The paper trace used three calculator calls, while the real agent used two calculator calls. The agent already had the value ₹33,750 when calculating the difference.

## Part C — Chain-of-Thought Comparison

| Question | Without CoT | With CoT | Longer Reply |
|---|---|---|---|
| Q1 Instalments | Correct | Correct | With CoT |
| Q2 Lab sittings | Correct | Correct | With CoT |
| Q3 Tallest/shortest | Correct | Correct | With CoT |

All three questions were answered correctly without Chain-of-Thought. The Chain-of-Thought responses were longer because they showed intermediate reasoning steps.

## Part D — Self-Consistency

### Temperature = 0.8

The five runs produced equivalent correct answers. The majority answer was ₹9,562.5 per instalment, appearing in 3 of the 5 extracted responses.

### Temperature = 0

All five runs produced the same answer: ₹9,562.5 per instalment.

This shows that temperature 0 makes the responses highly consistent, while a higher temperature allows different outputs.

## Discussion

### 1. Does a different order of steps make a trace wrong?

No. A different order of valid tool calls does not necessarily make a trace wrong, provided the required information is obtained and the final calculation is correct.

### 2. Why can step-by-step prompting improve answers?

Step-by-step prompting encourages the model to break a problem into smaller steps and perform intermediate calculations.

### 3. Why can't CoT retrieve course fees?

CoT cannot access external information by itself. A tool such as `get_course_fee()` is needed to retrieve the actual course fee.

### 4. Why use different temperatures?

Temperature 0 gives more deterministic responses. Self-consistency uses a non-zero temperature to generate different reasoning paths and compare their final answers.

### 5. How would Plan-and-Execute handle the question?

Plan-and-Execute would first create a sequence of tasks, such as retrieving fees, calculating both discounted totals, and comparing them. It would then execute that plan.

## Conclusion

The ReAct experiment showed how an agent combines tool calls and observations to solve a multi-step question. The Chain-of-Thought experiment showed that step-by-step prompting produces longer explanations while maintaining correct answers for these questions. Self-consistency demonstrated that multiple reasoning runs can be compared using majority voting.