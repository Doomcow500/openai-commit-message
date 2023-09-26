import openai
import os
import subprocess

openai.api_key = os.environ["OPENAI_API_KEY"]

changes = subprocess.check_output(["git", "diff", "--name-only"]).decode("utf-8").strip()

prompt = f("Please generate a commit message for the following changes:\n\n{changes}\n\n")
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=64,
    n=1,
    stop=None,
    temperature=0.5,
)
commit_message = response.choices[0].text.strip()

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", commit_message])