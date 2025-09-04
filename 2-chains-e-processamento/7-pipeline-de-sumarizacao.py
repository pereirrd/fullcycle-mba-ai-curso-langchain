from multiprocessing import context
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()

long_text = """ The Lord of the Rings movie series is a set of three epic fantasy adventure movies: 
The Fellowship of the Ring (2001), The Two Towers (2002) and The Return of the King (2003).
The movies were based on J. R. R. Tolkien's book The Lord of the Rings.
Set in the fictional world of Middle-earth, the plot of The Lord of the Rings is about the war of
the peoples of the fantasy world Middle-earth against a dark lord known as Sauron. At the same time
they try to destroy a ring which would give Sauron a lot of power if he got it, but the only place to 
destroy the ring is deep into Sauron's land Mordor.The movie trilogy was directed by Peter Jackson. 
The screenplay was written by Fran Walsh, Philippa Boyens, and Peter Jackson. It was distributed by New Line Cinema.
These were the first live-action Lord of the Rings movies made. 
They were filmed in New Zealand from October 1999 to December 2000, and released separately in December 2001-2003 by Warner Bros.
Jackson returned for a prequel The Hobbit trilogy and two more movies are in development:
an animated The Lord of the Rings: The War of the Rohirrim prequel movie and a live-action The Hunt for Gollum movie. """

spliter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
parts = spliter.create_documents([long_text])

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

# LCEL map stage: summarize each chunk
map_prompt = PromptTemplate.from_template("Write a concise summary of the following text:\n{context}")
map_chain = map_prompt | llm | StrOutputParser()

prepare_map_inputs = RunnableLambda(lambda docs: [{"context": d.page_content} for d in docs])
map_stage = prepare_map_inputs | map_chain.map()

# LCEL reduce stage: combine summaries into one final summary
reduce_prompt = PromptTemplate.from_template("Combine the following summaries into a single concise summary:\n{context}")
reduce_chain = reduce_prompt | llm | StrOutputParser()

prepare_reduce_input = RunnableLambda(lambda summaries: {"context": "\n".join(summaries)})
pipeline = map_stage | prepare_reduce_input | reduce_chain

result = pipeline.invoke(parts)
print(result)