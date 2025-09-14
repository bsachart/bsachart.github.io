import os
import json
from github import Github
from google import genai
from google.genai.errors import GenAiError
import sys

# Args
diff_file = sys.argv[1]

with open(diff_file) as f:
    diff_content = f.read()

# Environment variables
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO_NAME = os.environ["REPO"]
PR_NUMBER = int(os.environ["PR_NUMBER"])

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Prompt for nit-picky code review
prompt = f"""
You are a very nit-picky AI code reviewer. Review this PR diff carefully.
Focus on correctness, style, security, and performance.
Return JSON:
{{
  "approved": true/false,
  "comments": [
    {{ "file": "filename", "line": 12, "comment": "..." }}
  ]
}}
Diff:
{diff_content}
"""

# Try Pro model first, fallback to Flash
model_list = ["gemini-2.5-pro", "gemini-2.5-flash"]
response_text = None

for model in model_list:
    try:
        response = client.models.generate_content(model=model, contents=prompt)
        response_text = response.text
        break
    except GenAiError as e:
        print(f"Model {model} failed: {e}. Trying next model...")
        continue

if response_text is None:
    print("Both models failed.")
    sys.exit(1)

# Parse JSON
try:
    result_json = json.loads(response_text)
except Exception as e:
    print(f"Failed to parse AI output: {e}")
    sys.exit(1)

# Initialize GitHub
gh = Github(GITHUB_TOKEN)
repo = gh.get_repo(REPO_NAME)
pr = repo.get_pull(PR_NUMBER)

# Post comments
for comment in result_json.get("comments", []):
    pr.create_review_comment(
        body=comment["comment"],
        commit_id=pr.head.sha,
        path=comment["file"],
        position=comment["line"],
    )

# Approve or request changes
if result_json.get("approved"):
    pr.create_review(event="APPROVE", body="AI Code Review: Approved ✅")
else:
    pr.create_review(event="REQUEST_CHANGES", body="AI Code Review: Changes needed ❌")
    sys.exit(1)  # Fail workflow to block deployment
