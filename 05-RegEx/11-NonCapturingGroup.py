import re

def main():
    text = "Reach me at 9742016472 or 9811112023. If I don't answer, you can leave a message at +9779801234567" 
    pattern = r"\b(?:\+977|977)?9[678]\d{8}\b"
    matches = re.findall(pattern, text)

    print(matches)


if __name__ == "__main__":
    main()