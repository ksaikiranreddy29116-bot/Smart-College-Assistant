from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

from tools import (
    attendance_calculator,
    result_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator,
    student_information
)

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

tools = [
    attendance_calculator,
    result_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator,
    student_information
]

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are Smart College Assistant.

Your responsibilities:

1. Help students with attendance calculations.
2. Calculate examination results.
3. Calculate fee balances.
4. Calculate library fines.
5. Calculate hostel fee balances.
6. Provide student information when requested.

Rules:

- Always choose the correct tool whenever a calculation is needed.
- Never perform calculations manually if a tool exists.
- If multiple requests are asked, invoke multiple tools.
- Explain results clearly and professionally.
- Ask follow-up questions if required inputs are missing.
"""
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)
print("===== Smart College Assistant =====")

while True:

    query = input("\nEnter Query (or type exit): ")

    if query.lower() == "exit":
        break

    response = agent_executor.invoke(
        {"input": query}
    )

    print("\nResponse:")
    print(response["output"])