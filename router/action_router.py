# router/action_router.py

from agents.classifier_agent import classify_and_process

def route_action(file_path):
    print(f"Routing action for file: {file_path}")
    result = classify_and_process(file_path)
    return result

# Quick test
if __name__ == "__main__":
    sample_file = "../static/sample_email.txt"
    output = route_action(sample_file)
    print("Router output:")
    print(output)
