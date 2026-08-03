import pymupdf4llm
import pathlib
import time
start_time = time.time()  # start timer

md_text = pymupdf4llm.to_markdown("filename.pdf")

# save to disk
pathlib.Path("filename.md").write_bytes(md_text.encode())

end_time = time.time()  # end timer
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")