from markitdown import MarkItDown
import time
start_time = time.time()  # start timer

md = MarkItDown()
result = md.convert("filename.pdf")

# save to disk
with open("filename_markitdown.md", "w", encoding="utf-8") as myfile:
    myfile.write(result.text_content)

end_time = time.time()  # end timer
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")
