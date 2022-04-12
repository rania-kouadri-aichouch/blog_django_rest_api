def slugify(text):
    #replace special characters and spaces with "-"
    text = text.replace(" ", "-")
    text = text.replace(",", "-")
    text = text.replace("(", "-")
    text = text.replace(")", "")
    text = text.replace("؟", "")
    text = text.replace("?", "")
    text = text.replace("/", "")
    text = text.replace("!", "")
    text = text.replace(".", "")
    text = text.replace("،", "")
    text = text.replace(";", "")

    if text[len(text) - 1] == "-":
        text = text[:len(text) - 1]
    return text.lower()  #return the text lowercase
