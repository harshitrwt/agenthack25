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

if not GOOGLE_API_KEY:
    raise ValueError("No GOOGLE_API_KEY found in environment.")

config = Config.from_default(
    llm_provider=LLMProvider.GOOGLE,
    google_api_key=GOOGLE_API_KEY,
    portia_api_key=PORTIA_API_KEY,         
    default_model="google/gemini-2.5-pro", 
    default_log_level=LogLevel.INFO,
    storage_class=StorageClass.CLOUD,
)

portia_agent = Portia(config=config, tools=example_tool_registry)
