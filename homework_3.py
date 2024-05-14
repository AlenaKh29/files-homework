result = {}
def count_lines(file_name):
	with open(file_name, 'r', encoding='utf-8') as file:
		line_list = file.readlines()
		count = len(line_list)
		counter = 0
		for i in range(count):
			counter += 1
			line_list[i] = f'Строка номер {counter} файла номер {file_name[0]}   {line_list[i][:-1]}'
		line_list.insert(0, file_name)
		line_list.insert(1, str(count))
	result[count] = line_list

def write_to_file(result):
	with open('text_result.txt', 'w', encoding='utf-8') as output:
		for i in sorted(result):
			for j in result[i]:
				print(j, file=output)

	with open('text_result.txt','r', encoding='utf-8') as file:
		for line in file:
			print(line.strip())

count_lines('1.txt')
count_lines('2.txt')
count_lines('3.txt')

write_to_file(result)