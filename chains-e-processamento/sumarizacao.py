from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
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

splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=50)
parts = splitter.create_documents([long_text])

#for part in parts:
#    print(part.page_content)
#    print("-" * 30)

llm = ChatOpenAI(temperature=0, model="gpt-5-nano")

chain_summarize = load_summarize_chain(llm, chain_type="stuff", verbose=False)

result = chain_summarize.invoke({"input_documents": parts})
print(result["output_text"])