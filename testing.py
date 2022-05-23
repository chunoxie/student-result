#test_file = open('record.txt')
# print(type(test_file))
#text_complete = test_file.read()
# text_line = test_file.readline()
# print("second line:\n ", test_file.readline())
# print("\ntext_line: ", text_line)

# for line in test_file:
#     print("Printing line...")
#     print(line)
    # for item in line:
    #     print(" ... ", end='')
    #     print(item, end='')
#test_file.close()

with open('record.txt') as test_file:
    text_complete = test_file.read()
    print("File still open...\n", text_complete)

additional_text = f"""
This is content from record.txt: \n{text_complete}
"""

with open('record2.txt', 'a') as record2:
    record2.write("New record is being created...")
    record2.write(additional_text)



