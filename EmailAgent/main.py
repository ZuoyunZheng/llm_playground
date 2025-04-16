import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_community import GmailToolkit
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from pydantic import SecretStr


def main():
    load_dotenv()

    @tool
    def ask_human(question: str) -> str:
        """Directly get human input regarding email"""
        response = input(f"{question}")
        return response

    # Under Console/API&Services/OAuthConsentScreen
    # Clients -> add client for credentials.json
    # Audience -> add google account
    # Can review scopes here https://developers.google.com/gmail/api/auth/scopes
    # For instance, readonly scope is 'https://www.googleapis.com/auth/gmail.readonly'
    credentials = get_gmail_credentials(
        token_file="token.json",
        scopes=["https://mail.google.com/"],
        client_secrets_file="credentials.json",
    )
    api_resource = build_resource_service(credentials=credentials)
    toolkit = GmailToolkit(api_resource=api_resource)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp", api_key=SecretStr(os.getenv("GEMINI_API_KEY"))
    )

    agent = create_react_agent(llm, toolkit.get_tools() + [ask_human])

    example_query = "Draft an email to fake@fake.com thanking them for coffee. Get human input regarding email and send email upon approval."

    events = agent.stream(
        {"messages": [("user", example_query)]},
        stream_mode="values",
    )
    for event in events:
        event["messages"][-1].pretty_print()


if __name__ == "__main__":
    main()
