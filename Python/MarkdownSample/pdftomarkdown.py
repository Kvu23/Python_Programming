import pymupdf4llm
import pathlib

# Convert the PDF to Markdown text
md_text = pymupdf4llm.to_markdown("AUTOSAR_SWS_COM.pdf")

# Save the output
pathlib.Path("output.md").write_bytes(md_text.encode("utf-8"))
print("Completed converting the pdf to narkdown files")
