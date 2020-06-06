import requests
import click
@click.command()
@click.argument('url')
@click.argument('filename', type=click.Path())
def download_file(url, filename):
   print('Downloading from {} to {}'.format(url, filename))
   response = requests.get(url)
   with open(filename,  'wb') as ofile:
       ofile.write(response.content)

#train_url = 'https://s3.ap-south-1.amazonaws.com/datahack-prod/train_file/Train_UWu5bXk.csv'
#train_filename = 'data/raw/train.csv'
#downloadAndSave(train_url, train_filename)


#test_url ='https://s3.ap-south-1.amazonaws.com/datahack-prod/test_file/Test_u94Q5KV.csv'
#test_filename = 'data/raw/test.csv'
#downloadAndSave(test_url, test_filename)

if __name__ == '__main__':
	downloadAndSave()

