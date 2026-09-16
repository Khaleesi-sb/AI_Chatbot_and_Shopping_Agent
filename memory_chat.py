from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly tutor."),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])

model = ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.3)

chain = prompt | model 

history = []

print("Welcome to the AI Tutor! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    answer = chain.invoke({"question": user_input, "history": history}).content
    print(f"Tutor: {answer}")

    history.append(HumanMessage(user_input))
    history.append(AIMessage(answer))

    print(f"history now has {len(history)} messages.")
