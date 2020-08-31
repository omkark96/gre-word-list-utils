import csv

GREG_FILE = "Greg.csv"
PREPSCHOLAR_FILE = "Prepscholar357.csv"
MAGOOSH_BASIC_FILE = "Magoosh_Basic.csv"
MAGOOSH_COMMON_FILE = "Magoosh_Common.csv"
POWERSCORE_REPEAT_OFFENDERS = "PowerscoreRepeatOffenders.csv"


def cleaner_function(file_name, first_word_to_replace=None):
    """
    :param file_name:
    :param first_word_to_replace: too lazy too fix the encoding issue
    :return: filtered list of words
    """
    with open(file_name) as file:
        csv_reader = csv.reader(file)
        curated_list = []
        if first_word_to_replace is not None:
            curated_list.append(first_word_to_replace)
        for _ in csv_reader:
            curated_list.append(_[0].lower().rstrip().lstrip())

    if first_word_to_replace is not None:
        curated_list.pop(1)
    unique_list = list(dict.fromkeys(curated_list))

    # print(len(unique_list))
    # print(unique_list)

    return sorted(unique_list)


def filter_from_list(list_of_words, filter_from_list):

    new_list = []
    for word in list_of_words:
        if word not in filter_from_list:
            new_list.append(word)

    # print(new_list)
    # print(f"Word Count: {len(new_list)}\n")
    return new_list


if __name__ == '__main__':

    greg_list = cleaner_function(GREG_FILE)
    prep_scholar_list = cleaner_function(PREPSCHOLAR_FILE, "abate")
    magoosh_basic_list = cleaner_function(MAGOOSH_BASIC_FILE, "aboveboard") # to lazy too fix the encoding issue
    magoosh_common_list = cleaner_function(MAGOOSH_COMMON_FILE, "aberrant")
    repeat_offenders_list = cleaner_function(POWERSCORE_REPEAT_OFFENDERS)

    word_list_final = []

    word_list_final.extend(greg_list)
    # print("Filtering and adding unique words from PrepScholar 357 List: ")
    word_list_final.extend(filter_from_list(prep_scholar_list, word_list_final))
    # print("Filtering and adding unique words from Magoosh Basic List: ")
    word_list_final.extend(filter_from_list(magoosh_basic_list, word_list_final))
    # print("Filtering and adding unique words from Magoosh Common List: ")
    word_list_final.extend(filter_from_list(magoosh_common_list, word_list_final))
    # print("Filtering and adding unique words from Repeat Offenders List: ")
    word_list_final.extend(filter_from_list(repeat_offenders_list, word_list_final))

    print(sorted(word_list_final))
    print(len(word_list_final))
