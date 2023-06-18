def main():
    yell(["This", "is", "CS50"])

def yell(words):
    """Print each word in words, followed by an exclamation mark."""
    uppercase = []

    for word in words:
        uppercase.append(word.upper())
    
    print(*uppercase) # unpacking list

if __name__ == "__main__":
    main()