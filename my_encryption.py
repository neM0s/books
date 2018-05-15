# Type your code here
def my_encryption(some_string):

    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    encrypted = ""

    for i in some_string:
        chr_index = character_set.index(i)
        encrypted=encrypted + secret_key[chr_index]
    return encrypted




print(my_encryption("test"))