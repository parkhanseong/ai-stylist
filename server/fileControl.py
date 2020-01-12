import os
import glob
import shutil

inputDirPath = '/users/hanseongpark/Documents/머신러닝_미니프로젝트/img/'
newDirPath = '/users/hanseongpark/Documents/머신러닝_미니프로젝트/fashion_dataset/'

# 폴더 생성
def makedir(dirname):
    os.makedirs(dirname)

# 해당 디렉토리 검색후 label에 맞는 디렉토리 생성 후 이동
def searchdir(path):
    folder_list = os.listdir(path)
    labelArr = ['Anorak', 'Blazer', 'Blouse', 'Bomber', 'Button-Down', 'Cardigan', 
    'Flannel', 'Halter', 'Henley', 'Hoodie', 'Jacket', 'Jersey', 'Parka', 'Peacoat', 
    'Poncho', 'Sweater', 'Tank', 'Tee', 'Top', 'Turtleneck', 'Capris', 'Chinos', 'Culottes',
    'Cutoffs', 'Gauchos', 'Jeans', 'Jeggings', 'Jodhpurs', 'Joggers', 'Leggings', 'Sarong',
    'Shorts', 'Skirt', 'Sweatpants', 'Sweatshorts', 'Trunks', 'Caftan', 'Cape', 'Coat',
    'Coverup', 'Dress', 'Jumpsuit', 'Kaftan', 'Kimono', 'Nightdress', 'Onesie', 'Robe', 'Romper',
    'Shirtdress', 'Sundress']

    if '.DS_Store' in folder_list:
        folder_list.remove('.DS_Store')

    for label in labelArr:
        print(' >> label')
        print(label)
        for folder in folder_list:
            print(' >> folder')
            print(folder)
            if label in folder.split('_')[-1]:
                if not os.path.exists(newDirPath + label):
                    os.makedirs(newDirPath + label)
                    shutil.move(path + folder, newDirPath + label)
                else:
                    shutil.move(path + folder, newDirPath + label)

if __name__ == '__main__':
    searchdir(inputDirPath)