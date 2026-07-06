def power_sum(arr, power):
    def helper_function(arr, power):
        sum = 0
        for item in arr:
            if type(item) == list:
                sum += helper_function(item, power + 1)
            else:
                sum += item
              
        return sum ** power
    print(helper_function(arr, power))

arr, power = [1, 2, [3, 4], [[2]]], 1
power_sum(arr, power)
