# How to Test the Multi-Agent System

## Quick Answer

**The test code is in the Jupyter notebook: `multi_agent_system.ipynb`**

Specifically, the test cells are:
- **Cell 14**: Loads test queries from `test_queries.json`
- **Cell 15**: Tests individual sample queries
- **Cell 16**: Runs all test queries and shows accuracy summary

## Step-by-Step Testing Instructions

### 1. Setup (First Time Only)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` file** with your API keys:
   ```env
   OPENAI_API_KEY=your-openrouter-api-key
   OPENAI_API_BASE=https://openrouter.ai/api/v1
   LANGFUSE_PUBLIC_KEY=pk-lf-xxx
   LANGFUSE_SECRET_KEY=sk-lf-xxx
   LANGFUSE_HOST=https://cloud.langfuse.com
   ```

3. **Verify data files exist:**
   - `data/hr_docs/` (10 files)
   - `data/tech_docs/` (10 files)
   - `data/finance_docs/` (10 files)

### 2. Run the Tests

1. **Open the notebook:**
   ```bash
   jupyter notebook multi_agent_system.ipynb
   ```
   Or use VS Code, JupyterLab, or any Jupyter-compatible editor.

2. **Run all cells sequentially:**
   - Click "Run All" or run cells one by one from top to bottom
   - The cells must be run in order:
     - Cells 1-2: Setup and imports
     - Cells 3-5: Load documents and create vector stores
     - Cells 6-7: Create specialized agents
     - Cells 8-12: Create orchestrator
     - **Cells 14-16: Run tests** ← This is where testing happens!

3. **View results:**
   - Cell 15 shows individual test results
   - Cell 16 shows a summary with accuracy metrics

### 3. Test Queries

The test queries are defined in `test_queries.json`. You can:

- **View test queries:**
  ```bash
  python test_application.py --list
  ```

- **Add your own test queries** by editing `test_queries.json`

### 4. Manual Testing

After running all setup cells, you can test individual queries in the notebook:

```python
# Test a single query
result = orchestrator("How many vacation days do I get per year?")
print(f"Intent: {result['classified_intent']}")
print(f"Answer: {result['answer']}")
```

## Test Output Example

When you run Cell 16, you'll see output like:

```
============================================================
RUNNING ALL TEST QUERIES
============================================================

[1/15] Testing: How many vacation days do I get per year?
Classified Intent: HR
Answer: [Answer from HR documentation]

[2/15] Testing: My laptop won't connect to WiFi...
Classified Intent: Tech
Answer: [Answer from Tech documentation]

...

============================================================
TEST SUMMARY
============================================================
Correct classifications: 14/15
Accuracy: 93.3%
```

## Troubleshooting

### "Orchestrator not defined" error
- **Solution**: Run all cells from the beginning. The orchestrator is defined in Cell 12.

### "Vector store not found" error
- **Solution**: Run Cells 3-5 to load documents and create vector stores.

### "API key not found" error
- **Solution**: Create a `.env` file with your API keys (see Setup step 2).

### Tests not running
- **Solution**: Make sure you've run Cells 1-12 before running test cells (14-16).

## Alternative: View Test Queries

To see what queries will be tested:

```bash
python test_application.py --list
```

This shows all test queries from `test_queries.json` without running the actual tests.

## Summary

- **Test code location**: `multi_agent_system.ipynb` Cells 14-16
- **Test data**: `test_queries.json`
- **How to run**: Execute all notebook cells sequentially
- **Expected output**: Classification results and accuracy metrics

