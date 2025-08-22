from services.portia_instance import portia_agent
prompt = """
You are a project assistant. 
Analyze this GitHub issue and break it down into actionable steps.

Issue Title: Add a README
Issue Body: Please create a README file that includes installation instructions, usage examples, and licensing info.
"""

print("Running prompt:", prompt)

try:
    plan = portia_agent.plan(prompt)
    print(plan)

    # run the full plan (not just planning)
    result = portia_agent.run(prompt)
    print("=== FINAL OUTPUT ===")
    print(result)

except Exception as e:
    print("Caught exception:", e)
