# import operator
#
# name_to_number = {'Derek':7, 'Xaviar':80,'Bob':612,'Chantanelle':9}
# sorted_dict = sorted(name_to_number.items(),key=operator.itemgetter(1),reverse=True)
# for name,number in sorted_dict:
#     name_to_number[name] = number
#     max_length = max(len(name) for name in list(name_to_number.keys()))
#     print(f"{name:{max_length}} = {number}")

# word_to_count = {"apple": 8, "Kiwi": 4}
# words = ["apple","orange"]
# for word in words:
#     try:
#         word_to_count[word] += 1
#         words = print(word,word_to_count[word])
#     except KeyError:
#         word_to_count[word] = 1
#         print(word,word_to_count[word])
# print(word_to_count)

# word_to_count = {"apple": 8, "Kiwi": 4}
# words = ["apple","orange"]
# for word in words:
#     word_to_count[word] = word_to_count.get(word,0) +1
#     print(word,word_to_count[word])
# print(word_to_count)

"""languages = ["python","java","json"]

languages to length = {"python":6,"java":4,"json":4}"""

"""languages = ["python","java","json"]
values = [6,4,4]
language_to_count = zip(languages,values)
print(f"languages to length = {dict(language_to_count)}")"""
def list_of_languages(language):
    length_of_dict = {}
    languages =["python","java","json"]
    for language in languages:
        length_of_dict[language] = len(languages)
    return length_of_dict



# languages = ["python","java","json"]
# values = [6,4,4]
# language_to_count = zip(languages,values)
# print(f"languages to length = {dict(language_to_count)}")



