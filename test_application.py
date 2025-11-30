#!/usr/bin/env python3
"""
Test script for the Multi-Agent System.

HOW TO TEST THE APPLICATION:
=============================

Option 1: Using Jupyter Notebook (Recommended)
-----------------------------------------------
1. Open multi_agent_system.ipynb in Jupyter
2. Run all cells from top to bottom (Cell 1 through Cell 16)
3. The test code is in Cells 14-16, which will automatically run

Option 2: Using this script (after notebook is set up)
-------------------------------------------------------
1. First, run the notebook once to initialize the system
2. Then you can use this script to run tests

Option 3: Quick manual test in notebook
----------------------------------------
After running all setup cells, test with:
    result = orchestrator("How many vacation days do I get per year?")
    print(result)

The test queries are in: test_queries.json
"""

import os
import json
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("="*60)
print("MULTI-AGENT SYSTEM TEST SCRIPT")
print("="*60)
print("\nNOTE: This application is designed to run in a Jupyter notebook.")
print("The test code is located in: multi_agent_system.ipynb (Cells 14-16)")
print("\nTo test the application:")
print("1. Open multi_agent_system.ipynb in Jupyter")
print("2. Run all cells sequentially from top to bottom")
print("3. The test cells (14-16) will automatically execute")
print("\n" + "="*60)
print()


def load_test_queries():
    """Load test queries from JSON file."""
    test_file = Path("test_queries.json")
    if not test_file.exists():
        print(f"ERROR: {test_file} not found!")
        return []
    
    with open(test_file, "r") as f:
        return json.load(f)


def test_single_query(query_text: str, expected_intent: str = None):
    """Test a single query and display results."""
    print(f"\n{'='*60}")
    print(f"Query: {query_text}")
    if expected_intent:
        print(f"Expected Intent: {expected_intent}")
    print(f"{'='*60}")
    
    try:
        result = orchestrator(query_text)
        
        print(f"Classified Intent: {result['classified_intent']}")
        if expected_intent:
            match = "✓" if result['classified_intent'].upper() == expected_intent.upper() else "✗"
            print(f"Match: {match}")
        
        print(f"\nAnswer:")
        print(result['answer'])
        
        if result.get('sources'):
            print(f"\nSources (first 2):")
            for i, source in enumerate(result['sources'][:2], 1):
                print(f"  {i}. {source[:100]}...")
        
        return {
            "query": query_text,
            "expected": expected_intent,
            "classified": result['classified_intent'],
            "correct": expected_intent is None or result['classified_intent'].upper() == expected_intent.upper()
        }
    except Exception as e:
        print(f"ERROR: {e}")
        return None


def show_test_queries():
    """Display the test queries that are available."""
    test_queries = load_test_queries()
    if not test_queries:
        print("No test queries found in test_queries.json")
        return
    
    print(f"\nFound {len(test_queries)} test queries in test_queries.json:\n")
    for i, test_case in enumerate(test_queries, 1):
        query = test_case.get("query") or test_case
        expected = test_case.get("expected_intent", "N/A")
        print(f"{i:2d}. Query: {query}")
        print(f"    Expected Intent: {expected}\n")
    
    print("\nTo run these tests, execute the notebook cells 14-16 in Jupyter.")


def run_quick_test():
    """Run a quick test with 3 sample queries."""
    print("="*60)
    print("QUICK TEST - Sample Queries")
    print("="*60)
    
    sample_queries = [
        ("How many vacation days do I get per year?", "HR"),
        ("My laptop won't connect to WiFi", "Tech"),
        ("What is the expense reimbursement process?", "Finance")
    ]
    
    for query, expected in sample_queries:
        test_single_query(query, expected)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Test helper for Multi-Agent System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_application.py              # Show instructions
  python test_application.py --list       # List all test queries
  
Note: To actually run the tests, you need to:
1. Open multi_agent_system.ipynb in Jupyter
2. Run all cells from top to bottom
3. The test cells (14-16) will execute automatically
        """
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all test queries from test_queries.json"
    )
    
    args = parser.parse_args()
    
    if args.list:
        show_test_queries()
    else:
        # Check API key only if not just listing
        if not os.getenv("OPENAI_API_KEY"):
            print("NOTE: OPENAI_API_KEY not found in environment variables.")
            print("This is okay if you just want to see test queries.")
            print("To run tests, you'll need to create a .env file with your API keys.")
            print("\nSee README.md or TESTING_GUIDE.md for setup instructions.")
            print("\n" + "="*60)
        
        print("\nThis script helps you understand how to test the application.")
        print("\nThe actual test code is in the Jupyter notebook.")
        print("\nTo see available test queries, run: python test_application.py --list")
        print("\nTo run tests:")
        print("  1. Open multi_agent_system.ipynb")
        print("  2. Run all cells sequentially")
        print("  3. Tests will execute in cells 14-16")
        print("\nSee TESTING_GUIDE.md for detailed instructions.")
        print("\n" + "="*60)

