import html
from docling.document_converter import DocumentConverter
import time
start_time = time.time()  # start timer

converter = DocumentConverter()
result = converter.convert("filename.pdf")
docling_text = result.document.export_to_markdown()

# unescape HTML entities
docling_text = html.unescape(docling_text)

# save to disk
with open("filename_docling.md", "w", encoding="utf-8") as myfile:
    myfile.write(docling_text)

end_time = time.time()  # end timer
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")