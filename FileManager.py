import csv
class FileManager:
    def __init__(self,fileName,log=None):
        self.fileName = fileName
        self.log = log
    def read(self):
        with open(self.fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            data = []
            for row in csv_reader:
                if line_count == 0:
                    #print('row ', row)
                    #content=row.split(",")
                    print(row)
                    data.append(row)
                    line_count+=1
                else:
                    #content=" ".join(row)
                    data.append(row)
                    print(row)
                    line_count+=1
            print(f'Processed {line_count} lines.')
            return data
    def raw(self):
        print("raw log:", self.fileName)
        try:
            f = open(self.fileName)
            File = f.read()
        except:
            File = "Does not exist"
        print("\n\n\n\nFile",File)
        return File
    def logged(self,write=None):
        f=open(self.fileName, "a+")
        written = f.write(f'{write}')
        print(write)
        f.close()
        things = "send"
        print("log class compelete")
        #return things
    def writing(self,write=None):
        f=open(self.fileName, "w")
        written = f.write(f'{write}')
        print(write)
        f.close()
        things = "send"
        print("log class compelete")
    def test():
        print("hmm")