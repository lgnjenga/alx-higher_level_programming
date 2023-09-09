#!/usr/bin/python3
def text_indentation(text):
    """
    Print the text with 2 new lines after
    each of the characters: ., ? and :

    :param text: The input text to be processed.
    :type text: str
    :raises TypeError: If the input is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty result string
    result = ""

    # Iterate through each character in the input text
    for char in text:
        # Append the character to the result string
        result += char

        # Check if the character is one of ., ?, or :
        if char in ".?:":
            # Add two new lines after the character
            result += "\n\n"

    # Split the result into lines and remove leading and trailing spaces
    lines = [line.strip() for line in result.splitlines()]

    # Print each line in the result
    for line in lines:
        print(line)


if __name__ == "__main__":
    # Test case
    text_indentation("""Lorem ipsum dolor sit amet,
    consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi
    litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem.
    Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit,
    finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam,
    quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus.
    Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea.
    Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico.
    Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")
