🏥 AI-Powered Healthcare: Access and Alternatives for Indian Medications

📖 Introduction

Medicine shortages in India often leave patients waiting while pharmacists manually search for substitutes. This project automates the process using OCR, semantic search, and containerized web services, making substitution faster and more reliable.

⸻

❗ Problem Statement

The system solves three challenges:
	1.	Extract prescribed medicines from scanned prescriptions.
	2.	Recommend therapeutic substitutes automatically.
	3.	Enable Access via a deployed web API with potential UI integration.

⸻

🛠️ Key Technologies
	•	Backend Framework → FastAPI / Flask
	•	OCR → Gemini Vision Pro API
	•	NLP → Sentence Transformers for embeddings
	•	Similarity Search → Cosine similarity on vector representations
	•	Containerization → Docker for reproducible builds
	•	Deployment → Cloud-ready via Docker (GCP, Render, Railway, or Cloud Run)
	•	Frontend (optional extension) → Basic HTML interface for pharmacists/patients

⸻

🚀 Features & Benefits
	•	Automated substitute search → reduces manual lookup time.
	•	REST API with docs → /predict, /healthz, /batch.
	•	Portable deployment → containerized with Docker, runs on any cloud.
	•	Scalable design → can integrate pharmacies, online retailers, or dashboards.
	•	User-friendly layer → extendable with HTML/JS frontend for non-technical use.

⸻

✅ Project Outcomes
	•	Working API that extracts prescriptions and suggests substitutes.
	•	Containerized and deployable with a single docker run.
	•	Demonstrated ability to combine ML pipelines with production-style software practices.

⸻

🔮 Future Roadmap
	•	HTML/JS Web Dashboard for pharmacists/patients.
	•	Real-time inventory check via pharmacy APIs.
	•	CI/CD pipeline with GitHub Actions + Cloud Run/Fly.io.
	•	Feedback loop to improve substitute recommendations.
