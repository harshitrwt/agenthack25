# from services.portia_instance import portia_agent
# from models import Incident, Analysis

# def generate_plan(incident: Incident, analysis: Analysis):
#     plan = portia_agent.plan(
#         goal=f"Fix incident: {analysis.summary}",
#         context={
#             "incident_source": incident.source,
#             "error_message": incident.error_message,
#             "root_cause": analysis.root_cause
#         }
#     )
#     return plan


# from portia import Portia
# from config import GEMINI_API_KEY

# # Create a singleton instance of Portia, with API key
# # (if Portia does not accept api_key directly, change to token=... or remove arg)
# try:
#     portia_agent = Portia(api_key=GEMINI_API_KEY)
# except TypeError:
#     # Fallback: maybe Portia auto-loads from env, so just init without args
#     portia_agent = Portia()

import os
from dotenv import load_dotenv
from portia import (
    Config,
    LLMProvider,
    Portia,
    StorageClass,
    LogLevel,
    example_tool_registry,
)

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PORTIA_API_KEY = os.getenv("PORTIA_API_KEY")

if GOOGLE_API_KEY:
    config = Config.from_default(
        llm_provider=LLMProvider.GOOGLE,
        google_api_key=GOOGLE_API_KEY,
        portia_api_key=PORTIA_API_KEY,
        default_model="google/gemini-2.5-flash",
        default_log_level=LogLevel.DEBUG,
        storage_class=StorageClass.CLOUD,  # optional, but enables cloud-based planning
    )
else:
    raise ValueError("❌ No valid LLM API key found. Please set GOOGLE_API_KEY in .env")

portia_agent = Portia(config=config, tools=example_tool_registry)
