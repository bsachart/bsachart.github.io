import os
import sys
from github import Github, Auth
from google import genai
from pydantic import BaseModel
from typing import List


# -----------------------------
# Pydantic model for code review
# -----------------------------
class ReviewComment(BaseModel):
    file: str
    line: int
    comment: str


class CodeReviewResponse(BaseModel):
    approved: bool
    comments: List[ReviewComment]


# -----------------------------
# Args and environment
# -----------------------------
diff_file = sys.argv[1]
with open(diff_file) as f:
    diff_content = f.read()

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO_NAME = os.environ["REPO"]
PR_NUMBER = int(os.environ["PR_NUMBER"])

# -----------------------------
# Initialize Gemini client
# -----------------------------
client = genai.Client(api_key=GEMINI_API_KEY)

prompt = f"""
You are a very nit-picky AI code reviewer. Review this PR diff carefully.
Focus on correctness, style, security, and performance.
Return JSON strictly matching the schema with:
- approved: true/false
- comments: list of objects with file, line, comment
Diff:
{diff_content}
"""

# -----------------------------
# Generate structured response
# -----------------------------
model_list = ["gemini-2.5-pro", "gemini-2.5-flash"]
response_parsed: CodeReviewResponse | None = None

for model in model_list:
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": CodeReviewResponse,
            },
        )
        response_parsed = response.parsed  # Already a CodeReviewResponse object
        break
    except Exception as e:
        print(f"Model {model} failed: {e}. Trying next model...")
        continue

if response_parsed is None:
    print("Both models failed.")
    sys.exit(1)

# -----------------------------
# Initialize GitHub
# -----------------------------
gh = Github(auth=Auth.Token(GITHUB_TOKEN))
repo = gh.get_repo(REPO_NAME)
pr = repo.get_pull(PR_NUMBER)

# -----------------------------
# Post comments
# -----------------------------
# Fetch the HEAD commit object for the PR
head_commit = repo.get_commit(pr.head.sha)

for comment in response_parsed.comments:
    pr.create_review_comment(
        body=comment.comment,
        commit=head_commit,
        path=comment.file,
        position=comment.line,
    )

# Approve or request changes
if response_parsed.approved:
    pr.create_review(event="APPROVE", body="AI Code Review: Approved ✅")
else:
    pr.create_review(event="REQUEST_CHANGES", body="AI Code Review: Changes needed ❌")
    sys.exit(1)  # Fail workflow to block deployment
