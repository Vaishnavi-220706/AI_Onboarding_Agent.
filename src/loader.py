import os
from typing import List

from src.models import DocumentChunk


def load_documents(directory: str) -> List[DocumentChunk]:
    chunks = []

    if not os.path.exists(directory):
        raise FileNotFoundError(
            f"Document directory not found: {directory}"
        )

    chunk_number = 1

    for filename in sorted(os.listdir(directory)):

        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(directory, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        sections = content.split("\n\n")

        for index, section in enumerate(sections):

            section = section.strip()

            if not section:
                continue

            chunk = DocumentChunk(
                chunk_id=f"chunk_{chunk_number}",
                document=filename,
                section=f"Section {index + 1}",
                text=section
            )

            chunks.append(chunk)
            chunk_number += 1

    return chunks