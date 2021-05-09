import codecs
import json
import time

from faker import Faker
lines = 1000
write_lines = []


def generate_data():
    count = 0
    for line in range(lines):
        stat = time.time()
        with open('a.txt','w', encoding='utf-8') as  f:
            fake=Faker(locale='zh_CN')
            data = fake.simple_profile()
            data['birthdate'] =str(data['birthdate'])
            data = json.dumps(data).encode().decode('unicode-escape')
            write_lines.append(data + '\n')
            f.writelines(write_lines)
            count = count + 1
            print(count)
            stop = time.time()
            print(stop - stat)
            f.close()


if __name__ == '__main__':
    generate_data()
