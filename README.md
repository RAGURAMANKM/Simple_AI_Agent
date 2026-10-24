# Simple_AI_Agent
This implementation is a basic tool-using agent, not an LLM-powered agent. It uses predefined rules to select tools and cannot generate new answers to arbitrary questions.
This project is a simple AI agent developed using Python. It uses two tools: a Calculator Tool to perform mathematical calculations and a Knowledge Base Tool to retrieve stored information. If the requested information is unavailable, the agent returns a message instead of making up an answer. It also checks consistency by asking the same question twice and comparing the results.

Limitations
The knowledge base contains only predefined questions and answers.
It cannot answer general questions that are not stored in its knowledge base.
It does not use an actual AI language model (LLM).
The calculator supports only basic arithmetic operations.
