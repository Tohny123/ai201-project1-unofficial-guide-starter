from config import DATA_PATH
import os
import chromadb
from config import N_RESULTS

class vectorDB:

    
    def __init__(self):
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.create_collection(name="windows_collection")
        self.documents = self.load_documents()
        self.allChunks = []
        for document in self.documents:
            self.allChunks.extend(self.chunk_document(document['text'], document['article']))
        print("Initializing DB...")
        metadatas = []
        for chunk in self.allChunks:
            metadatas.append(
                {"article_name:": "Wikipedia article source: " + chunk["name"]}
            )

        self.collection.add(
            ids=[chunk["chunk_id"] for chunk in self.allChunks],
            documents=[chunk["text"] for chunk in self.allChunks],
            metadatas=metadatas
        )
    def query(self, query:str):
        return self.collection.query(
            query_texts=[query],
            n_results=N_RESULTS
        )

    def load_documents(self):
        """Load all .md rule documents from the docs folder."""
        documents = []
        for filename in sorted(os.listdir(DATA_PATH)): # we sort this so the document list is nicer 
            if filename.endswith(".md"):
                filepath = os.path.join(DATA_PATH, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()
                article = filename.replace(".md", "").replace("_", " ").title() # converts the name to the proper format, e.g. (Windows_7.md -> Windows 7)
                documents.append({
                    "article": article,
                    "filename": filename,
                    "text": text,
                })
        print(f"Loaded {len(documents)} document(s): {[d['article'] for d in documents]}")
        return documents


    def chunk_document(self, text: str, article: str):
        """
        Split a article into chunks with overlap 

        Returns a list of dicts, each with:
        - "text"     : the chunk text (str)
        - "name"     : the article name, e.g. "Windows_7" (str) (this is metadata)
        - "chunk_id" : a unique identifier, e.g. "windows_7_0", "windows_7_1" (str)
        """
        chunk_size = 512
        overlap = 64
        min_length = 10

        chunks = []
        prefix = article.lower().replace(" ", "_")
        counter = 0

        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end].strip()

            if len(chunk_text) >= min_length:
                chunks.append({
                    "text": chunk_text,
                    "name": article,
                    "chunk_id": f"{prefix}_{counter}",
                })
                counter += 1

            # Advance by (chunk_size - overlap) so the next chunk shares
            # `overlap` characters with the tail of this one.
            start += chunk_size - overlap
        print(article + " has been chunked")
        return chunks
    
    def queryText(self, query: str) -> str:
        retVal = ""
        output = self.query(query)
        for document in output['documents'][0]:
            retVal += document
        return retVal
    




