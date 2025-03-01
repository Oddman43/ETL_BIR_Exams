# ETL from pdf files 👷🏼 (WIP)
Avg exam -> 8 mins

Total 34 pdfs

## Motivation

Last year when I began to study to become an Internal Resident in Biology by myself I knew I needed a way to review exam questions 

Faced with that dilema i began brainstorming and i ended up woth the idea of designing an ETL pipeline to extract the questions from the pdfs and using some kind of Python script and uploading then to Anki using Anki Connect addon so i can review them efficiently.


## Technologies and Tools Used

* Python 3.xx
* JupyterNotebooks
* PyPdf librabry to extract the text from Pdf files
* Pandas librabry for data cleaning and maniputaltion
* Anki Connect for loading into anki
* SQLite3 for saving to a databass

## Project Architecture

### Extract

Using the oper source library PyPdf reads the exam pdf and the output is piped into a dataframe

For the answers sheet can be either in tsv format, or txt with spaces as separator. The extraccion is done with Pandas directly using the .read_table function

Depending if the answers sheet is in tsv or txt format the type 1 or 2 will be used.

### Transform

The questions using pandas will remove all the artifacts, like page numbers or others, and white spaces. Once all artifacts are gone a function to deal with multines will be used, it checks if a line ends with "-" for truncated words and to detect if the next line is a question or options the function checks if the first element of the next line can be converted into an integer.

Once this script is done it counts the number of lines that do not end with a dot, comma or interrogation and generates a list of ids to fix. The length lf this list will be compared with the theoretical number of incorrect rows that is calculated with the following formula number of questions * number of options - length of the dataframe. If the number of expected errors matches with the length of ids to fix it applies a second function to fix them, if there are more or less than expected prints +/- 2 rows for context and raises a Warning, so i could manualy check for the rows to fix.

Another check is done once the fix is applied and if the number of rows is not equal to the expected it raises a Warning to check it manually.

Once all the checks are done the dataframe is pivoted to get the following columns: 

* Question
* Option 1
* Option 2
* Option 3
* Option 4
* Option 5 if needed

For the anwers dataframe the transform step it will depend if it comes from tsv file or txt.



### Load

#### SQLite3

#### csv files

#### Anki

## Instalation and Usage

## Example output

## Potential Improvments

