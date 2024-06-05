import os

def count_files(directory, extension):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count

c_files = count_files('fire14-source-code-training-dataset\c', '.c')
java_files = count_files('fire14-source-code-training-dataset\java', '.java')

proportion = c_files / java_files
print(f"The proportion of the number of .c files to .java files in the fire14 directory is: {proportion}")