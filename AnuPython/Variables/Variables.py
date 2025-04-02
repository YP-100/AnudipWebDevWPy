
# variable demo 1***********************************************

first_var = 100
print(first_var)
first_var = first_var + 11 
print(first_var)
first_var *= 2
print(first_var)



second_var = 200
print(second_var)
second_var += 11
print(second_var)

third_var = 300
print(third_var)
third_var -= 10
print(third_var)

result= (third_var*first_var)/second_var
print(result)
result /= 10
print(result)



# variable demo 2***********************************************

first_var = 100
second_var = 200
first_var **= 3
print(first_var)

second_var //= 5
print(second_var)


# variable demo 3***********************************************

var1 = 5
var2 = 5
bitwiseand = var1 & var2
print(bitwiseand) 

bitwisenot = ~var1
print(bitwisenot)


# variable demo 4***********************************************

PI = 3.14
result = (PI == 3.14) if True else False
print(result)


# variable demo 5***********************************************

languages = ["c","C++","Python","Java","perl","ruby","script"]
is_java_av = "Java" in languages
print(is_java_av)
is_pas_av = "pascal" in languages
print(is_pas_av)
is_pas_av = "pascal" not in languages
print(is_pas_av)


