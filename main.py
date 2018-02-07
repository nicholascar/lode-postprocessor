import sys

if sys.argv[1] == '-i':
    print('reading & writing file ' + sys.argv[2])
    read_file = sys.argv[2]
    write_file = sys.argv[2]
else:
    print('writing file ' + sys.argv[1])
    print('writing file ' + sys.argv[2])
    read_file = sys.argv[1]
    write_file = sys.argv[2]

with open(read_file, 'r') as f:
    f_new = f.read()
    f.seek(0)
    for line in f.readlines():
        if '<li><a href="#d4' in line:
            d = 'd' + line.split('#d')[1].split('"')[0]
            # cater for onts that have additional things defined that don't have # in them (like registers)
            if len(line.split('#')) > 2:
                uri = line.split('#')[2].split('"')[0]
                print('{} --> {}'.format(d, uri))
                f_new = f_new.replace(d, uri)

    with open(write_file, 'w') as n:
        print('writing file ' + sys.argv[2])
        n.write(f_new)
