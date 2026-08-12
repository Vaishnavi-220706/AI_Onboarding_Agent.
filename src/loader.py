import re
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Document:
    source: str
    section: str
    text: str


def load_documents(paths):
    documents = []

    for path in paths:
        path = Path(path)

        raw = path.read_text(encoding="utf-8")

        current_section = "1"
        buffer = []

        def flush():
            if buffer:
                text = " ".join(buffer).strip()

                if text:
                    documents.append(
                        Document(
                            source=path.name,
                            section=current_section,
                            text=text
                        )
                    )

                buffer.clear()

        for line in raw.splitlines():

            line = line.strip()

            if not line:
                continue

            match = re.match(r"^##\s*(.+)$", line)

            if match:
                flush()
                current_section = match.group(1).strip()

            else:
                buffer.append(line)

        flush()

    return documents