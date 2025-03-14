# Simulation of the call API

def make_call(from_number: str, to_number: str, message: str):
    print(f"Calling from {from_number} to {to_number} with message: {message}")
    
# Example usage
if __name__ == "__main__":
    make_call("CustomNumber", "RecipientNumber", "Hello, this is a custom call!")
