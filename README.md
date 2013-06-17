Fairu is a python library to handle files easily using a chain pattern like
the jQuery framework.

Select a set of files and do batch actions like extract, delete, move, etc.

Installation
---

For now, you need clone the project from github:

    git clone git://github.com/dfleury/fairu.git

If you want to contribute with fairu, make sure that you have all requirements
needed to work:

    cd fairu
    pip install -r requirements.txt

Usage example
---

Unfortunately, the project is in development of pre-alpha. It means that right
now, while I'm writting this readme, nothing is working. But I imagine the
method's interface would be something like that:

    from fairu import Fairu

    Fairu()
        .goTo('~/Downloads') # assumes $HOME/Download as work folder
        .select('*.rar')     # selects all rar files in work folder
            .extract(result) # try to extract these rar files and save a list of extracted files
            .delete()        # deletes these rar files

    result                            # uses the set of files extracted
        .select('fairu_[0-9]{3}.avi') # of this set, selects files that match this pattern
            .move('~/Movies/fairu/')  # moves them to other folder
            .rename('fairu_([0-9]{3}).avi', '$1.avi') # renames using a regular expression
            .done()                   # uses the previous set before filtering
        .remove()                     # removes all files remaing (except moved files)

This is just a draft. Suggestions are welcome.

Thank's for spend your time reading until here.