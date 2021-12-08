def remove_duplicates(some_list):
    without_duplicates = []
    [without_duplicates.append(element) for element in some_list if element not in without_duplicates]
    return without_duplicates


def rm_with_set(some_list):
    return(set(some_list))


def run():
    random_list = [1, 1, 2, 2 , 4]
    print(remove_duplicates(random_list))
    print(rm_with_set(random_list))


if __name__ == '__main__':
    run()