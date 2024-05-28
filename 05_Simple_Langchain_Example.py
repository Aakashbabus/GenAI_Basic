from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser


messages = [
    SystemMessage(content="Translate the following from English into Kannada"),
    HumanMessage(content="how old are you ?"),
]

model = ChatOpenAI(model="gpt-4")
parser = StrOutputParser()



#Option 1 - Without LangChain

#result = model.invoke(messages)
#output = parser.invoke(result)

#Option 2 - With LangChain

chain = model | parser
output = chain.invoke(messages)

print(output)