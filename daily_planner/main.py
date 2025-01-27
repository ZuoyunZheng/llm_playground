import argparse

from llama_cpp import Llama
from llama_cpp_agent import LlamaCppAgent, MessagesFormatterType
from llama_cpp_agent.providers import LlamaCppPythonProvider, LlamaCppServerProvider
from dotenv import load_dotenv
import os


def main(args):
    if args.backend == "python":
        load_dotenv()
        MODEL_PATH = os.environ.get("MODEL_PATH")
        if args.model:
            MODEL_PATH = args.model

        llama_model = Llama(MODEL_PATH, n_batch=1024, n_threads=4, n_gpu_layers=2)
        provider = LlamaCppPythonProvider(llama_model)
    else:
        provider = LlamaCppServerProvider("http://127.0.0.1:8080")

    agent = LlamaCppAgent(
        provider,
        system_prompt="You are a helpful assistant.",
        predefined_messages_formatter_type=MessagesFormatterType.CHATML,
    )

    settings = provider.get_provider_default_settings()
    settings.temperature = 0.65

    while True:
        user_input = input(">")
        if user_input == "exit":
            break
        agent_output = agent.get_chat_response(
            user_input, llm_sampling_settings=settings
        )
        print(f"Agent: {agent_output.strip()}")


if __name__ == "__main__":
    argparse = argparse.ArgumentParser("Daily Planner Agent")
    argparse.add_argument("--backend", default="cpp", choices=["cpp", "python"])
    argparse.add_argument("--model", help="Path to llama model", required=False)

    args = argparse.parse_args()
    main(args)
