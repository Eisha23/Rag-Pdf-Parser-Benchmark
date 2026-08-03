import nest_asyncio
nest_asyncio.apply()

from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader
import time

import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("LLAMAPARSE_KEY")

start_time = time.time()  # start timer

# set up parser
parser = LlamaParse(
    api_key=key, # insert your API key here
    result_type="markdown",
    verbose=True,
)

# use SimpleDirectoryReader to parse the file
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(
    input_files=["filename.pdf"], file_extractor=file_extractor
).load_data()

# save to disk
with open("filename_llamaparse.md", "w", encoding="utf-8") as myfile:
    for document in documents:
        myfile.write(document.text_resource.text)

end_time = time.time()  # end timer
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")