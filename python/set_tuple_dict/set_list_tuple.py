arr1 = ["a","a","b","a","c","d","e"]
arr2 = {"a","a","b","a","c","d","e"}
arr3 = ("a","a","b","a","c","d","e")

print( type( arr3 ) )

print(arr3)

arr3 = list(arr3)

arr3[ 1 ] = "z"

arr3 = tuple(arr3)

print( type( arr3 ) )
print(arr3)

