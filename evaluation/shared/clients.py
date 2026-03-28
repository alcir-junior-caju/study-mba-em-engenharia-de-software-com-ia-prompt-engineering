"""LLM and observability platform clients."""
import os
from langsmith.wrappers import wrap_openai
from langsmith import Client as LangSmithClient
from openai import OpenAI
from langfuse import Langfuse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"


def get_openai_client():
    """
    Returns Google Gemini client (OpenAI-compatible) with LangSmith tracing.

    Model and temperature are configurable via environment variables:
    - LLM_MODEL (default: gemini-2.0-flash)
    - LLM_TEMPERATURE (default: 0)

    Returns:
        OpenAI-compatible Google client wrapped with LangSmith tracing
    """
    return wrap_openai(OpenAI(
        api_key=os.getenv("GOOGLE_API_KEY"),
        base_url=GOOGLE_BASE_URL,
    ))


def get_model_name() -> str:
    """
    Get configured model name from environment.

    Returns:
        Model name (default: gemini-2.0-flash)
    """
    return os.getenv("LLM_MODEL", "gemini-2.0-flash")


def get_temperature() -> float:
    """
    Get configured temperature from environment.

    Returns:
        Temperature value (default: 0)
    """
    return float(os.getenv("LLM_TEMPERATURE", "0"))


def get_langsmith_client():
    """
    Returns LangSmith client.

    Returns:
        LangSmith Client instance
    """
    return LangSmithClient()


def get_langfuse_client():
    """
    Returns Langfuse client.

    Returns:
        Langfuse client instance
    """
    return Langfuse()


def get_openai_client_langfuse():
    """
    Returns Google Gemini client (OpenAI-compatible) with Langfuse tracing.

    Model and temperature are configurable via environment variables:
    - LLM_MODEL (default: gemini-2.0-flash)
    - LLM_TEMPERATURE (default: 0)

    Returns:
        OpenAI-compatible Google client wrapped with Langfuse tracing
    """
    from langfuse.openai import OpenAI as LangfuseOpenAI # pyright: ignore[reportPrivateImportUsage]
    return LangfuseOpenAI(
        api_key=os.getenv("GOOGLE_API_KEY"),
        base_url=GOOGLE_BASE_URL,
    )
