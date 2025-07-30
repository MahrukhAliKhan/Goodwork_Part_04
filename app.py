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
        model="gpt-4o",  # Or use "gpt-3.5-turbo" if preferred
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=1200
    )

    jd_output = response['choices'][0]['message']['content']
    
    # Display generated job descriptions
    print("\n✅ Generated Job Descriptions:\n")
    print(jd_output)

    # Step # 08: Output validation
    if not jd_output.strip():
        print("⚠️ Output was empty. Model may have misunderstood the prompt.")
    elif "Pakistan" not in jd_output or "Philippines" not in jd_output:
        print("⚠️ Regional tailoring may be missing from the output.")

except Exception as e:
    print("❌ API call failed:", str(e))


# Step # 09: Performance Analysis
print("\n--- 🧪 Performance Notes ---")
print("✓ Model: GPT-4o (Accurate, fast, cost-effective)")
print("✓ Approx. Cost: ~$0.01–$0.02 per call (based on tokens used)")
print("✓ Speed: Typically <3 seconds for this prompt size")
print("✓ Reliability: High with structured inputs, may vary with freeform employer briefs")


# Step # 10: Production Considerations
"""
🛠️ Production Improvements:
- Add input validation (e.g., required fields like skills/salary)
- Use retry logic & backoff for API errors or timeouts
- Connect to Airtable or Postgres to store input/output (see Part 1 data model)
- Support multilingual JD generation using language selector
- Include recruiter feedback loop to rate outputs and fine-tune prompts
"""

# Step # 11: Integration Note
"""
🔄 Integration with Part 1 Airtable TRM:
- Employer briefs submitted via Typeform → pushed to this JD generator
- Generated JDs saved back into Airtable and previewed in Stacker client portal
"""
