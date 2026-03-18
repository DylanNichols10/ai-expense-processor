This project treats the LLM as an unreliable component, not a source of truth.

A small local model (llama3.2:3b via Ollama) is used to extract structured data from invoice text. Running locally removes API cost and highlights a key constraint: smaller models are less reliable and require tighter control.

The goal is not extraction itself, but building a pipeline that can safely consume and validate probabilistic outputs.

Lower model quality is intentional here — it exposes failure modes (invalid JSON, partial extraction, instruction drift) that need to be handled in real-world systems.

Similar use-cases: categorising unstructured free text into actions: emails, complaints, IT requests, etc


Next Steps
If this were to be extended further, the most valuable improvements would be:
- Adding a more advanced JSON repair/fallback layer before retrying the model with a stricter prompt / trying a different model
- Exposing the pipeline as an API (e.g. FastAPI)
- Expanding input as a PDF/OCR pipeline 
- Logging results and prompts fully, using LLM-based evaluation to iterate and compare prompt strategies