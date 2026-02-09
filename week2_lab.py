import time

def test_list(func, para):
    num_trials = 100
    results = 0
    for n in range(num_trials):
        # list_ = list(range(para))
        list_ = []
        for i in range(para):
            list_.append(i)
        start = time.perf_counter()
        func(list_)
        end = time.perf_counter()
        duration_ms = (end - start) * (10 ** 6)

        results += duration_ms
    
    mean = results / num_trials
    print(mean)
    
    
def insert_to_beginning(list_):
    list_.insert(0, 10)

def pop_list(list_):
    list_.pop(0)
    
def append_list(list_):
    # list_.pop()
    list_.append("0")
    
def pop_end_list(list_):
    list_.pop()
    
def search_list(list_):
    if 0.123 in list_:
        return True

def test_dict(func, para):
    num_trials = 1000
    results = 0
    for n in range(num_trials):
        dict_ = {}
        for n in range(para):
            dict_[n] = ""
        start = time.perf_counter()
        func(dict_)
        end = time.perf_counter()
        duration_ms = (end - start) * (10 ** 6)
        results += duration_ms
    
    mean = results / num_trials
    result += str(mean) + "\n"
    print(mean)

def search_dict(dict_):
    if 0.123 in dict_:
        return True

result = ""

# test_list(insert_to_beginning, 10)
# test_list(insert_to_beginning, 1000)
# test_list(insert_to_beginning, 1000000)
# test_list(pop_list, 10)
# test_list(pop_list, 1000)
# test_list(pop_list, 1000000)
test_list(append_list, 10)
test_list(append_list, 1000)
test_list(append_list, 870020)
test_list(pop_end_list, 10)
test_list(pop_end_list, 1000)
test_list(pop_end_list, 870020)
# test_list(search_list, 10)
# test_list(search_list, 1000)
# test_list(search_list, 1000000)
# test_dict(search_dict, 10)
# test_dict(search_dict, 1000)
# test_dict(search_dict, 1000000)

with open("week2_lab.txt", "w") as f:
    f.write(result)
    
# def test_n_time(make_one, fn, n=1000):
#     inp = make_one()
#     start = time.perf_counter()
#     fn(inp)
#     end = time.perf_counter()
#     diff = end - start
    
# test_n_time(lambda i : list(range(i)), lambda i: i.append(0), 1000)