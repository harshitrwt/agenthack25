from services.portia_instance import portia_agent

prompt = """
You are a project assistant.
Analyze this GitHub issue and break it down into actionable steps.

Issue Title: Add a README
Issue Body: Please create a README file that includes installation instructions, usage examples, and licensing info.
"""

try:
    plan = portia_agent.plan(prompt)
    print("\n--- CLEANED STEPS ---")
    for idx, step in enumerate(plan.steps, 1):
        print(f"{idx}. {step.task}")
except Exception as e:
    print("Plan generation failed, falling back to chat. Error:", e)
    response = portia_agent.chat(prompt)
    print("\n--- FALLBACK RESPONSE ---")
    print(response.output_text)
