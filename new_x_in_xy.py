import pandas as pd
import os
import numpy as np

class new_x_in_xy():
 
    def __init__(self, *args,**kwargs):
        Directory = kwargs.get('Directory',False)
        x_value_file = kwargs.get('x_value_file',False)

        if Directory == False:
            self.Dict = r'C:\Users\bjorngso\OneDrive - Universitetet i Oslo\03 Codes\Izar'
            raise  RuntimeError('No Directory given')
        else:
            self.Dict = Directory
          
        if x_value_file == False:
            self.x_file = r'C:\Users\bjorngso\OneDrive - Universitetet i Oslo\03 Codes\Izar\twotheta.xy'
            raise  RuntimeError('No X value file given')
        else:
            self.x_file = x_value_file
        

        self.create_new_folder()
        self.convert_data()
        pass



    def create_new_folder(self, *args, **kwargs):
        #making a folder for the result int the same folder as the original data
        for root, dirs, files in os.walk(self.Dict, topdown=False):
            for name in files:
                if name[-3:] == '.qI':
                    joint = (os.path.join(root,name))
                    
        self.new_path = os.path.join(root,'Converted')
        isExist = os.path.exists(self.new_path)
        
        
        Error_1 ='''Folder allready exist. Make sure that the data does not overwrite and try again.
        
        
        
                        Do you want to continue anyway (y/n)?''' 
        Error_2 = '''Folder allready exist. Make sure that the data does not overwrite and try again.
        
                            ****   OPERATION ABORTED   **** '''
        Error_3 = '''New folder created, overwriting the existing.
        
        '''
        Error_4 = '''Invalid answer... its a Yes/No question.
        
        
        
                            Do you want to continue anyway (y/n)?''' 


        if not isExist:
            os.makedirs(self.new_path)
            print('New folder created')
            print('')
            print('')
            print('')
        else:
            while True:
                inp = input(Error_1)
                if inp.lower() not in ('n','y'):
                    print(Error_4)
                else:
                    break
            if inp == 'n':
                raise  RuntimeError(Error_2)
            else:
                print(Error_3)                
                pass
                


    def convert_data(self, *args, **kwargs):
        #the code...
        print('''The following files have been converted witht the new x-value
        
        ''')


        for root, dirs, files in os.walk(self.Dict, topdown=False):
            for name in files:
                if name[-3:] == '.qI':
                    joint = (os.path.join(root,name))
                    print('name')
                    #read and create the new x y match
                    df = pd.read_csv(joint,sep='   ',engine='python')
                    df.columns=['x','y']
                    self.df = df
                    y = df['y']
                    df_2 = pd.read_csv(self.x_file)
                    df_2.columns = ['x']
                    x = df_2['x']
                    self.x = x
                    
                    #create new .xy files with new x value
                    new_name = name[:-3]+'.xy'

                    New_file_dict_1 = os.path.join(self.new_path,new_name)
                    New_file_dict_1
                    print(New_file_dict_1)
                    np.savetxt(New_file_dict_1, np.vstack((x,y)).T, delimiter='   ')

        pass



    def __str__(self):
        nr = 0
        for root, dirs, files in os.walk(self.new_path, topdown=False):
            for name in files:
                nr += 1                    
                self.nr = nr
        return f'number of files converted : {self.nr}'

