# [Loom Walkthrough](https://www.loom.com/share/10ae1efb0a224a579b62452b5325756e) 
---
# Mac OSX Instructions

## One time setup
### Install Google Drive

1. Mount the tablecloth Google Drive locally using https://www.google.com/drive/download/ if you have not already done so.
2. Create a destination directory in the Google Drive where you'd like all the dashboards to be saved. Ideally version this folder with a date and/or description.

### Install Pip
Open a new terminal and run the following:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### Install Homebrew
Run the following command in terminal:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install Dependencies

Install selenium first with the following command:
```
pip3 install tqdm tkinter selenium==4.2.0
```

Install chromedriver with the following commands:
```
brew install --cask chromedriver
```

Then install chromedriver:
```
brew install --cask chromedriver
xattr -d com.apple.quarantine `which chromedriver`
```

## Repeated each time
### Add list of dashboard ids
Add a list of dashboard ids to process into the `dashboard_ids.txt` file. Each of these dashboards will have new PDFs generated and extracted.

### Run program
In the folder with the code, run `python3 main.py`. Keep this terminal window open and follow the prompts.

First, the program will open a chrome window and prompt you for your tablecloth username and password. Please enter that information, it's not saved locally anywhere and is only used during the runtime of the program.

Next, a finder window will open. Navigate to your computer's Downloads folder and press open.

Next, another finder window will open. Navigate to your destination Google Drive folder and press open.

Now, allow the program to run. It may take up to 10 hours for ~863 dashboards. 

Once the PDF generation is finished, you may want to update records in Airtable according to your changes. If this is the case open the following link:
https://colab.research.google.com/drive/1GkQTL107D9MHyQhVInubyPsH5-jdhRfX?authuser=1

and follow the instructiosn there to generate a full backup.
