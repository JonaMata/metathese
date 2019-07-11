import sys

with open(sys.argv[1]) as infile, open(sys.argv[2], 'w') as outfile:
    for line in infile:
        if not line.strip(): continue
        if '/' in line:
            outfile.write(line.split('/')[0])
        else:
            outfile.write(line)
