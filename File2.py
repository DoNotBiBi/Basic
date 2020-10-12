import shutil, os


def test_shutil():
    os.chdir('d:\\')
    # copytree() 用来复制整个文件夹
    # shutil.copy('d:\\h1.txt', 'd:\\h2.txt')  # 复制后只是文件名改变而已，内容没有改变
    shutil.copy('d:\\h1.txt', 'C:\\Users\\wangkang\\Documents\\h1.txt')
    # shultil.rmtree(path) 将删除path处的文件夹（包括所有的子文件夹）
    # os.unlink(path) 将删除path处的文件
    # os.rmdir(path) 将删除path处的文件夹（必须保证path的是空文件）

def test_os():
    for folderName,subfolders,filenames in os.walk('D:\\1AVedios\\Tech Stack'):
        print(folderName+":")
        for subfolder in subfolders:
            print(subfolder)

        for filename in filenames:
                print(filename)
import zipfile
def test_zipfile_open():
    os.chdir('d:\\')
    exampleZip=zipfile.ZipFile('d:\\test.zip')
    print(exampleZip.namelist())
    h1_info=exampleZip.getinfo('h1.txt')
    print(h1_info.file_size)
    exampleZip.close()


def test_zipfile_extract():
    os.chdir('d:\\')
    exampleZip = zipfile.ZipFile('d:\\test.zip')
    # extract(oldfile,[newpath])
    # exampleZip.extract('h1.txt','d:\\test')
    # 不带文件夹的解压 extractall()
    exampleZip.extractall()
    exampleZip.close()

def test_zipfile_create():
    os.chdir('d:\\')
    newZip=zipfile.ZipFile('new.zip','w')
    for i in range(3,5):

        newZip.write('h'+str(i)+'.txt',compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()
# os.path.join(foldername,filename) # 返回的就是一个文件的完整路径加上文件名
# os.path.abspath(folder) 确保路径是完整的
# os.path.basename(folder) folder 所在当前的文件夹
# os.path.exists(filename) 判断该文件是否存在