import os

# Cuenta el numeor de archivos con la extension del directorio
def count_files(directory, extension):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count

# Count the number of .c files in the 'fire14-source-code-training-dataset\c' directory
c_files = count_files('fire14-source-code-training-dataset\c', '.c')

# Count the number of .java files in the 'fire14-source-code-training-dataset\java' directory
java_files = count_files('fire14-source-code-training-dataset\java', '.java')

# Calculate the proportion of .c files to .java files
proportion = c_files / java_files

# Print the calculated proportion
print(f"The proportion of the number of .c files to .java files in the fire14 directory is: {proportion}")