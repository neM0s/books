'''
Write a function named "reverse_dictionary" that receives a dictionary as input argument and returns a reverse of the input dictionary,
where the values of the original dictionary are used as keys for the returned dictionary and the keys of the original dictionary are used as value for the returned dictionary as explained below
'''


def _reverse_dictionary(input_dict):
    output_dict={}
    for key in input_dict:
        for value in input_dict[key]:
            key_low = key.lower()
            value_low = value.lower()
            if output_dict.get(value_low):
                if key not in output_dict[value_low]:
                    output_dict[value_low].append(key_low)
                    output_dict[value_low].sort()
            else:
                output_dict[value_low]=[key_low]
    return output_dict


print(_reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}))