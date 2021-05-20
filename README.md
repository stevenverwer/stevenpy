# stevenpy
 Parallel pooling pdf scraper

# stevenpy

stevenpy is a powerful Python library for Parallel pooling document processing (Currently only PDF)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install stevenpy
```

## Usage

```python
import stevenpy

"""
IMPORTANT: if: if __name__== '__main__': is not used, the code will not work!!!
multiprocessing will not be able to function properly without it.
"""
if __name__ == '__main__':

# first create a task which is done for each document in your selected document folder
# in this example 'tags' such as AB-123-23 are found and reported to a summary file
    task1 = stevenpy.task(search_type='regex',
                    expression='^(\d{1,2}[ -]{,1}[A-Z]{1,3}[ -]{,1}\d{4}[A-Z]*).*$',
                    title='regex1',
                    label='tags')

# create a list of the task you want the searcher to perform
    tasks = [task1]

# create the searcher object and give it the tasks we just created
# the default 'dat_loc' = 'data', but this can be changed.
    searcher = stevenpy.searcher(tasks=tasks)

# then we run the searcher, this may take a while depending on the number of files to process
# (next versions should be able to check if some files are already processed)
    searcher.run()

# after all the files are processed a summary is made using the summary object
    summarizer = stevenpy.summarizer(searcher=searcher)
    summarizer.run()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
