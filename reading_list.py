# Books read tracker and a way to organise a 'to read' list, specifically for fasntasy book series
books_list = ["The Hunger Games series", "Throne of Glass series", "ACOTAR series", "Fourth Wing series", "Harry Potter series", "Divergent series", "Lord of the Rings book", "A Song of Ice and Fire", "The Wheel of Time",
              "The Witcher", "The Chronicles of Narnia", "The Stormlight Archive",
              "Mistborn", "The Kingkiller Chronicle", "The Dark Tower",
              "The Malazan Book of the Fallen", "Percy Jackson",
              "Discworld", "The First Law",
              "The Broken Earth",]
# Empty to be read (tbr) list
tbr_list = []

# Create a counter starting at zero, to be added when a book series has been read
total_read = 0

print(
    "---Welcome! Do you enjoy reading fantasy novels?! If so, please answer the following questions to find out what series to add to your "
    "reading list!---"
)
# practicing using a loop
for book in books_list:

    answer = input(f"Have you read the {book}? (yes/no): ").lower()

    # If they say yes, add 1 to the total
    if answer == "yes":
        total_read = total_read + 1
        print("Nice! That's a great series.")
    # If they haven't read it the book will be added to the To Be Read list
    else:
        tbr_list.append(book)
        print("Adding it to the TBR list!")

# Summarise findings
print(f"\n--- Reading Summary ---")
print(
    f"You have read {total_read} out of {len(books_list)} book series on this list!")

print("\nYour New TBR List:")
for tbr_item in tbr_list:
    print(f"- {tbr_item}")
