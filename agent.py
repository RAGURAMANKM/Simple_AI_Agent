import ast
import operator

# Tool 1: Calculator
def calculator(expression):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    def calculate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operators:
            return operators[type(node.op)](
                calculate(node.left),
                calculate(node.right)
            )

        raise ValueError("Unsupported expression")

    tree = ast.parse(expression, mode="eval")
    return calculate(tree.body)


# Tool 2: Knowledge Base
knowledge_base = {
    "python": "Python is a programming language.",
    "ai": "AI stands for Artificial Intelligence.",
    "machine learning": "Machine learning helps computers learn patterns from data.",
    "data analyst": "A data analyst examines data to find useful insights."
}


def knowledge_tool(question):
    question = question.lower().strip()

    if question in knowledge_base:
        return knowledge_base[question]

    return "I don't have enough information to answer this question."


# AI Agent
def ai_agent(question):
    question = question.strip()

    # Use the calculator tool for arithmetic
    try:
        tree = ast.parse(question, mode="eval")

        if isinstance(tree.body, ast.BinOp):
            result = calculator(question)
            return f"Answer: {result} | Tool: Calculator"

    except (SyntaxError, ValueError, TypeError, ZeroDivisionError):
        pass

    # Otherwise, use the knowledge base
    answer = knowledge_tool(question)

    return f"Answer: {answer} | Tool: Knowledge Base"


# Test the agent
def test_agent():
    questions = [
        "25 * 4",
        "python",
        "machine learning",
        "quantum computing"
    ]

    for question in questions:
        answer1 = ai_agent(question)
        answer2 = ai_agent(question)

        print("\nQuestion:", question)
        print("First answer:", answer1)
        print("Second answer:", answer2)

        if answer1 == answer2:
            print("Consistency check: PASSED")
        else:
            print("Consistency check: FAILED")


# Interactive mode
def main():
    print("AI Agent is ready! Type 'exit' to stop.")

    while True:
        question = input("\nEnter your question: ")

        if question.lower().strip() == "exit":
            print("Agent stopped.")
            break

        if not question.strip():
            print("Please enter a question.")
            continue

        print(ai_agent(question))


if __name__ == "__main__":
    test_agent()
    main()