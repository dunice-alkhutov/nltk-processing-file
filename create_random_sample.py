import random
import sys, getopt

def main(argv):
    source_file = None
    destination_file = None
    num_lines = 100
    try:
        opts, _ = getopt.getopt(argv, "s:d:n:h", ["source=", "dest=", "help="])
    except getopt.GetoptError as ex:
        print(ex)
        print("See help by 'python app.py -h'")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            message = '''You can use next flags:
            -s  path to source file(required)
            -d  path to destination file(required)
            -n  number of lines to put into destination file
            Example: "python create_random_sample.py -s /path/to/file1 -d /path/to/file2'''
            print(message)
            sys.exit()
        elif opt == '-s':
            source_file = arg
        elif opt == '-d':
            destination_file = arg
        elif opt == '-n':
            num_lines = int(arg)
        else:
            sys.exit()

    if not source_file:
        print('Source file is missed')
        sys.exit()
    if not destination_file:
        print('Destination file is missed')
        sys.exit()

    rnd_lines = []
    while len(rnd_lines) < num_lines:
        rnd = random.randint(1, 612000)
        if rnd not in rnd_lines:
            rnd_lines.append(rnd)

    dst = open(destination_file, 'w')

    with open(source_file) as fp:
        for i, line in enumerate(fp):
            if i in rnd_lines:
                dst.write(line)
    dst.close

if __name__ == "__main__":
    main(sys.argv[1:])
