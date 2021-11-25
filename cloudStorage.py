import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, "rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = "sl.A887GXQSCKajQGYmisYNmDhtRJmWxnNFZQZ6l6SEirrcMkOUoRoqdSYBcMIJausW3537NE-2A0l1eoJDljgroRNjtQYA4aN4jLW-L4qAOL5zANOPxZ8ibIDl5XGdowBdJMF9Piaqo8aU"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to be transfer :- ")
    file_to = input("Enter the full path to upload to Dropbox :- ")

    transferData.upload_file(file_from, file_to)
    print("File has been moved to Dropbox. ")

main()


