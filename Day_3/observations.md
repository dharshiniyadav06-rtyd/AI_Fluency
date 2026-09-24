# Day 3 - Observation Table and Failure Log

## Observation Table

| Test | What Happened | Steps | Result |
|---|---|---:|---|
| CS101 + AI202, 10% scholarship | Read notice.html and calculated the total fee | 1 | ₹27,000 |
| Hostel + all 3 courses | Read notice.html and calculated the total with laboratory charges | 2 | ₹49,500 |
| AI202, 15% scholarship | Read notice.html and used calculator | 2 | ₹15,300 |
| Welcome message | Answered directly without using a tool | 1 | No tool needed |
| Missing fees.html | read_webpage returned an error because the file did not exist | 1 | Error handled safely |
| big.html without guards | Large webpage caused a context/large-output failure | - | Failure observed |
| big.html with guards | Repeated read_webpage calls were detected | 3 | Agent stopped safely |

## Failure Log

### Failure 1 - Missing File

**Question:**  
Read fees.html and tell me the fee for CS101.

**Problem:**  
The file fees.html does not exist.

**Observed result:**  
The read_webpage tool returned an error message instead of crashing.

**Fix:**  
The fixed agent uses repeat detection and safe tool error handling.

---

### Failure 2 - Unknown Tool

**Change made:**  
Added the following instruction to the system prompt:

"If the fee is above 25000, use send_email to inform the accounts department."

**Expected failure:**  
The model could call the nonexistent send_email tool.

**Observed result:**  
In my run, the model did not actually call send_email. It only stated that an email would be sent.

**Unsafe lookup test:**  
Changed:

function = TOOL_FUNCTIONS.get(name)

to:

function = TOOL_FUNCTIONS[name]

No crash occurred because send_email was not actually called.

**Conclusion:**  
The unknown-tool crash could not be reproduced with this model run.

---

### Failure 3 - Large Webpage

**File created:**  
big.html

**Size:**  
Approximately 360,067 characters.

**Change made:**  
Temporarily changed:

def read_webpage(url: str, max_chars: int = 2000):

to:

def read_webpage(url: str, max_chars: int = 200000):

**Question:**  
Read big.html and tell me how many students are listed.

**Observed result:**  
The large webpage caused a context/large-output failure.

**Fix:**  
Restored max_chars to 2000.

---

## Fixed Agent Guards

The fixed agent contains three guards:

1. **Repeat Detection**
   - Detects the same tool call repeated three times.
   - Stops the agent safely.

2. **Observation Truncation**
   - Maximum tool observation size is 1500 characters.
   - Prevents very large tool outputs from entering the model context.

3. **Character Budget**
   - Total character budget is 30000.
   - Stops the agent when the context becomes too large.

## Final Result

The Day 3 ReAct agent was tested with normal tasks and deliberate failure cases. The fixed version adds repeat detection, observation truncation, character budgeting, and safe tool lookup to make the agent more robust.