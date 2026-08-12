import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

transcript_path = r"C:\Users\HP\.gemini\antigravity-ide\brain\32e3a523-15fb-4242-bbdf-55f1b0b92f84\.system_generated\logs\transcript.jsonl"

total_lines = 0
tool_calls_count = 0
errors_count = 0
user_inputs = []
tools_used = {}

if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            total_lines += 1
            try:
                data = json.loads(line)
                step_type = data.get("type", "")
                status = data.get("status", "")
                if step_type == "USER_INPUT":
                    content = data.get("content", "")
                    user_inputs.append(content[:100])
                if status == "ERROR":
                    errors_count += 1
                t_calls = data.get("tool_calls", [])
                if t_calls:
                    tool_calls_count += len(t_calls)
                    for tc in t_calls:
                        name = tc.get("name", tc.get("toolName", "unknown"))
                        tools_used[name] = tools_used.get(name, 0) + 1
            except Exception as e:
                pass

print(f"Total Transcript Steps: {total_lines}")
print(f"User Inputs Count: {len(user_inputs)}")
print(f"Tool Calls Count: {tool_calls_count}")
print(f"Errors Count: {errors_count}")
print("Tools Frequency:")
for k, v in sorted(tools_used.items(), key=lambda x: x[1], reverse=True):
    print(f"  {k}: {v}")
