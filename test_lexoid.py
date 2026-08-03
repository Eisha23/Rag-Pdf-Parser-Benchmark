from lexoid.api import parse
import time
start_time = time.time()  # start timer

# basic parsing
result = parse("filename.pdf", parser_type="STATIC_PARSE", model="pdfminer")
parsed_md = result["raw"]

# save to disk
with open("filename_lexoid.md", "w", encoding="utf-8") as myfile:
    myfile.write(parsed_md)

end_time = time.time()  # end timer
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")