# Step # 01: Import libraries
import openai
import os

# Step # 02: Load API key from environment variable 
openai.api_key = os.getenv("OPENAI_API_KEY")  

# Step # 03: SYSTEM PROMPT
SYSTEM_PROMPT = (
    "You are an expert technical recruiter creating inclusive, concise, and compelling Job Descriptions for remote roles. "
    "Always localize to the target region. Highlight values such as diversity, flexibility, and fair compensation."
)

# Step # 04: USER PROMPT TEMPLATE
USER_PROMPT_TEMPLATE = """
Generate a job description based on the following employer brief:

- Role: {role}
- Experience Level: {experience}
- Key Skills: {skills}
- Location: {location}
- Company Description: {company}
- Salary Range: {salary}

Please generate 2 region-aware versions of this JD — one optimized for Pakistan and one for the Philippines.
"""

# Step # 05: SAMPLE INPUT
sample_input = {
    "role": "Remote Executive Assistant",
    "experience": "2+ years",
    "skills": "Calendar management, email handling, reporting",
    "location": "Remote",
    "company": "Goodwork, a global women-first hiring platform",
    "salary": "$800–$1200/month (USD)"
}

# Step # 06: FORMATTING USER PROMPT
user_prompt = USER_PROMPT_TEMPLATE.format(**sample_input)

# Step # 07: CALL OPENAI API
try:
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # "gpt-3.5-turbo" can also be used here
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=1200
    )

    jd_output = response['choices'][0]['message']['content']
    print("\n Generated Job Descriptions:\n")
    print(jd_output)

except Exception as e:
    print("API call failed:", str(e))

