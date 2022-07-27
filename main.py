from ya_uploader import YaUploader

TOKEN = ""

if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    ya.upload_file_to_disk("netology/test_27_07.txt", "test.txt")
