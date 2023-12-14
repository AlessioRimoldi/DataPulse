from pandas import read_csv, read_excel,DataFrame

class CsvRetrieval:
    ''' Class used to deal with CSV files and xlsx. '''
    
    def __init__(self, path_to_file) -> None:
        
        self.path = path_to_file
        self.extension = self.path.split('/')[-1].split('.')[-1]
        
        if self.extension == 'csv':
            try:
                self.data = read_csv(self.path)
            except:
                print('Error reading CSV file.')
        elif self.extension == 'xlsx':
            try:
                self.data = read_excel(self.path)
            except:
                print('Error reading xlsx file.')
        else:
            print(f'File extension {self.extension} not supported, please check if the path is correct.')
        
    def get_data(self):
        ''' Return the data from the file. '''
        return self.data
    
    def display_data(self):
        ''' Display the data from the file. '''
        print(self.data)