Project:
This project treats a small LLM model as an unreliable component, not a source of truth.

llama3.2:3b is used via Ollama to extract structured data from invoice text. Running locally removes API cost and allows experimentation with a variety of smaller models.

The goal is not extraction itself, but building a framework that can safely consume and validate probabilistic outputs.

Lower model quality is intentional here — it exposes failures (invalid JSON, partial extraction, instruction drift) that need to be handled in real-world systems.
Furthermore, it also proves that even small models can be made quite security aware if prompted correctly.

Results:
Typical success rates for llama3.2:3b is 10/12 cases passed. 
It normally ranges from 9/12 to 12/12, but the 12/12 is quite rare. 
It often over-fixates on returning a JSON, by adding in an amount as 0 when no amount is given, or not populating the vendor/category when none is given. e.g. {'vendor': '', 'amount': 0, 'category': '', 'decision': 'auto_approve'}.
I find it does remarkably well at defending against prompt injection for such a small model from 2024, with the worst case scenario being for a case like attack_2 where it outputs the JSON and ignores the injected prompt. But this outcome is suprisngly rare, with the model 95%+ outputting the required "exception": "attack detected" response instead.

Potential improvments / enhancements:
- Adding a more advanced JSON repair/fallback layer before retrying the model with a stricter prompt or trying a different local model
- Exposing the pipeline as an API (e.g. FastAPI)
- Expanding input as a PDF/OCR pipeline 
- Logging results and prompts fully, using LLM-based evaluation to iterate and compare prompt strategies

Similar use-cases: categorising unstructured free text into actions: emails, complaints, IT requests, etc