"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability", 
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer"
    ]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = ""

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True   # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "placeholder"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Haymarket+Vaults+%7C+160+guests&id=2ef939fbbaf6"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
We have a graceful fallback placeholder for the case when model is not available.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
Okay, let's see. The user wanted to check The Bow Bar first for 160 vegan guests.
The first tool response showed that The Bow Bar's capacity is only 80,
which is way below the required 160. So, it didn't meet the requirements.
Then, the assistant moved on to check The Albanach next.
The response for The Albanach shows a capacity of 180, which is more than 160, and they do have vegan options.
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known Edinburgh venues can accommodate 300 people while meeting all requirements.
The maximum capacity among listed venues is 200 (The Guilford Arms), but it lacks vegan options.
Would you like to:
1. Search for alternative venues outside our known list?
2. Adjust the guest count or dietary requirements?
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "I don't have access to real-time train schedules or transportation data. You'll need to check a travel website like National Rail Enquiries or a train service app for the most accurate information on tonight's last train from Edinburgh Waverley to London.",

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, this is an acceptable vehaviour for a booking assistant. 
It didn't start booking random venues and even recommened other sources that could help user to learn about trains.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
https://mermaid.live/view#pako:eNptUV9vgjAQ_yrN7UUTyoBRxWp8mR9hTxuLqdACCbSklG3O-N1XqkNj6MPlrvf7c72eIFM5BwoY41RmSoqqoKlESNTqOyuZNq5CKOv1F6eoriRnOpUOXmjWluhtt75AhrPfd8aS9vvZx6bdjtXmud1-zimlotKducFZwaWZuTi_3Rql6m7m4vxemst8FHb5KFuze9XRFmG8vXisHzwR9m3rKjPddP7rh6kmFTNr3-24QDkXrK8NElVd0ycRiUAIb1gZLnlVlIaGfjRBc0txJKxallXmSIMJ2PDIq_RBHBYiAw8KXeVAje65Bw3XDRtKOA3sFEzJG54Ctel1shRSeba0lsl3pZp_plZ9UQIVrO5s1bc5M3xXMfu_N4jdFNevqpcGKHEKQE_wAzQMFj6JllEUkjhZrZLYgyNQvPDjlyUJSULiVURIFJ09-HWegZ8syfkPwy_AiA
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
LangGraph graph has one loop and decides on it's own what tools to use. 
This allows more flexibility in planning and adapting, but also could be unpredictable.
Rasa CALM has flows written explicitly, so every stop is predictable.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
FILL ME IN
"""