from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
import time

start_time = time.time()  # start timer

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)
rendered = converter("filename.pdf")

# save to disk
with open("filename_marker.md", "w", encoding="utf-8") as myfile:
    myfile.write(rendered.markdown)

end_time = time.time()  # end timer
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")