from langchain_core.runnables import RunnableLambda

def parse_number(text:int) -> int:
    return int(text.strip())

parse_runnable = RunnableLambda(parse_number)

number = parse_runnable.invoke("  42  ")
print(number)  # Output: 42