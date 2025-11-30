# Multi-Agent System for Customer Support Routing

A production-ready multi-agent orchestration system that intelligently routes customer inquiries to specialized RAG (Retrieval-Augmented Generation) agents based on query intent. Built with LangChain and fully instrumented with Langfuse for observability.

## 🎯 Project Overview

This system solves the real-world problem of misrouted customer support tickets by automatically classifying user queries and routing them to domain-specific AI agents (HR, Tech, Finance) that provide accurate, context-aware answers using company documentation.

### Key Features

- **Intent Classification**: Automatically classifies queries into HR, Tech, or Finance categories
- **Specialized RAG Agents**: Three domain-specific agents with their own knowledge bases
- **Full Observability**: Complete workflow tracing with Langfuse
- **Quality Evaluation**: Automated response scoring (Bonus feature)
- **Production-Grade**: Built with LangChain components for maintainability

## 📁 Repository Structure

```
assignment_3/
├── multi_agent_system.ipynb    # Main notebook with all implementation
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── test_queries.json           # Test queries with expected intents
├── README.md                   # This file
├── data/
│   ├── hr_docs/               # HR domain documents (10 files, 50+ chunks)
│   ├── tech_docs/             # Tech domain documents (10 files, 50+ chunks)
│   └── finance_docs/          # Finance domain documents (10 files, 50+ chunks)
└── chroma_db/                 # Vector store persistence (created at runtime)
```

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```env
# OpenAI API Key (via OpenRouter)
OPENAI_API_KEY=your-openrouter-api-key-here
OPENAI_API_BASE=https://openrouter.ai/api/v1

# Langfuse Configuration
LANGFUSE_PUBLIC_KEY=pk-lf-xxx
LANGFUSE_SECRET_KEY=sk-lf-xxx
LANGFUSE_HOST=https://cloud.langfuse.com
```

**Important**: 
- Get your OpenRouter API key from [openrouter.ai](https://openrouter.ai)
- Get your Langfuse keys from [cloud.langfuse.com](https://cloud.langfuse.com) (sign up for free account)

### 3. Verify Document Collections

Ensure you have documents in:
- `data/hr_docs/` (minimum 50 chunks)
- `data/tech_docs/` (minimum 50 chunks)
- `data/finance_docs/` (minimum 50 chunks)

The repository includes 10 sample documents per domain, which will create 50+ chunks when processed.

## 📓 Running the Notebook

### Cell Execution Order

Execute cells **sequentially from top to bottom**:

1. **Setup & Imports** (Cell 1-2): Load libraries and initialize Langfuse
2. **Document Loading** (Cell 3-5): Load documents and create vector stores
3. **Agent Definitions** (Cell 6-7): Create specialized RAG agents
4. **Orchestrator** (Cell 8-10): Set up routing logic
5. **Testing** (Cell 11-13): Run test queries
6. **Langfuse Integration** (Cell 14): Verify tracing
7. **Evaluator** (Cell 15-17): Test quality evaluation (Bonus)

### Usage Examples

#### Basic Query Routing

```python
# Simple query
result = orchestrator("How many vacation days do I get per year?")
print(result['classified_intent'])  # HR
print(result['answer'])
```

#### Query with Evaluation

```python
# Query with automatic quality scoring
result = orchestrator_with_evaluation("What is the expense reimbursement process?")
print(result['evaluation']['scores'])  # Quality scores
```

#### Running Test Suite

```python
# Load and run all test queries
import json
with open("test_queries.json", "r") as f:
    test_queries = json.load(f)

for test_case in test_queries:
    result = orchestrator(test_case["query"])
    print(f"Query: {test_case['query']}")
    print(f"Classified: {result['classified_intent']}")
    print(f"Expected: {test_case['expected_intent']}")
    print("---")
```

## 🔧 Configuration Notes

### Model Configuration

The system uses OpenAI models via OpenRouter:
- **LLM**: `openai/gpt-4o-mini` (for cost efficiency)
- **Embeddings**: `text-embedding-3-small`

To change models, modify the `llm` and `embeddings` initialization in the notebook.

### Chunking Strategy

- **Chunk Size**: 1000 characters
- **Overlap**: 200 characters
- **Retrieval**: Top 4 most relevant chunks per query

### Vector Store

- **Database**: ChromaDB (persisted to `chroma_db/` directory)
- **Embedding Model**: OpenAI text-embedding-3-small
- **Persistence**: Vector stores are saved and can be reloaded

## 📊 Observability with Langfuse

All operations are automatically traced using the `@observe()` decorator. View traces at your Langfuse dashboard:

1. Go to [cloud.langfuse.com](https://cloud.langfuse.com)
2. Navigate to "Traces"
3. See complete execution paths including:
   - Intent classification
   - Agent routing
   - RAG retrieval
   - Response generation
   - Quality evaluation scores

### Trace Structure

Each query creates a trace with:
- **Orchestrator**: Main entry point
  - **Classify Intent**: Classification step
  - **Route to Agent**: Routing decision
    - **RAG Agent**: Domain-specific agent
      - **Retrieval**: Document retrieval
      - **Generation**: LLM response
  - **Evaluator** (if enabled): Quality scoring

## 🎓 Technical Decisions Explained

### Why LangChain?

- **Production-Grade**: Battle-tested components for RAG
- **Maintainability**: Standard patterns, not custom code
- **Extensibility**: Easy to add new agents or modify existing ones
- **Integration**: Built-in support for vector stores, chains, and callbacks

### Why ChromaDB?

- **Simplicity**: Easy to set up and use
- **Persistence**: Saves vector stores to disk
- **Performance**: Fast similarity search
- **No External Dependencies**: Runs locally

### Why Classification-Based Routing?

- **Accuracy**: LLM-based classification is more accurate than keyword matching
- **Flexibility**: Handles edge cases and ambiguous queries
- **Observability**: Classification decisions are logged and traceable
- **Fallback**: Default routing prevents system failures

### Why 1000-Character Chunks?

- **Balance**: Large enough for context, small enough for precision
- **Token Limits**: Fits within LLM context windows
- **Retrieval Quality**: Optimal for semantic search
- **Overlap**: 200-char overlap prevents context loss at boundaries

## ⚠️ Known Limitations

1. **OpenRouter Dependency**: Requires OpenRouter API key and internet connection
2. **Langfuse Dependency**: Traces require Langfuse account (free tier available)
3. **Document Format**: Currently supports `.txt` files only (can be extended)
4. **Classification Fallback**: Unclear queries default to HR agent
5. **Single Language**: Optimized for English queries
6. **No Conversation Memory**: Each query is independent (no chat history)

## 🐛 Troubleshooting

### Vector Store Not Found

If you see "vector store not found" errors:
1. Run the document loading cells again
2. Check that `data/` folders contain `.txt` files
3. Verify ChromaDB persistence directory exists

### Langfuse Connection Errors

If Langfuse tracing fails:
1. Verify `.env` file has correct keys
2. Check internet connection
3. System will still work without Langfuse (just no tracing)

### API Key Issues

If you get authentication errors:
1. Verify `OPENAI_API_KEY` in `.env` is your OpenRouter key
2. Check that `OPENAI_API_BASE` is set to OpenRouter URL
3. Ensure you have credits in your OpenRouter account

### Low Classification Accuracy

If queries are misclassified:
1. Review classification prompt in `classify_intent()` function
2. Add more examples to the prompt
3. Consider fine-tuning or using a more powerful model

## 📈 Future Enhancements

- [ ] Support for PDF and other document formats
- [ ] Conversation memory for multi-turn dialogues
- [ ] Confidence scores for classifications
- [ ] Multi-language support
- [ ] Custom agent creation interface
- [ ] Performance metrics dashboard

## 📝 License

This project is created for educational purposes as part of an AI engineering assignment.

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Observability powered by [Langfuse](https://langfuse.com/)
- Models accessed via [OpenRouter](https://openrouter.ai/)

