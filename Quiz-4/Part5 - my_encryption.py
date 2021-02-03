def my_encryption(my_string):
     output_string=""
     index=0
     character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
     secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
     for character in my_string:
        index=character_set.find(character)
        output_string=output_string+secret_key[index]
     return output_string