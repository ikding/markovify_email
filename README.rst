================================================
# markovify_email
================================================

Building sentences using markovify package and outlook .eml files


Installing python packages
------------------------------------------------

We use `conda environment <http://conda.pydata.org/docs/using/envs.html>`_ to manage the python packages we use.

To do it:

#.  Clone Github repo to your laptop

    Inside your terminal (Gitbash for Windows or Terminal app for Mac), navigate to the folders you want, and clone this Github repo from the desktop. After running the commands above, you should be able to see a new folder ``markovify_email`` in the previous folder you specified.

    .. code:: bash

        # The leading # sign means that this is a comment line,
        # not meant to be an actual command.
        # The dollar sign, '$', is command prompt; it is not part of the
        # command you should type.

        # You can use any folder you want to save the script.
        # example: cd Documents/analytical_solutions/

        $ cd <folder_to_save_this_script>

        # This command will clone the repo into your folder. If you get
        # "Permission denied" error, check the Set-up Instructions section
        # to see if you set up github access correctly.
        $ git clone git@github.kdc.capitalone.com:ikang/markovify_email.git

        # After git clone is done, the script will be downloaded into
        # a new folder called markovify_email.

        $ cd markovify_email/

#.  Create a new conda environment. This will allow you to have a "sandbox" of sorts that has correct version of packages, without affecting your main Anaconda install. (Remember to turn proxy on before running the command below.)

    .. code:: bash

        $ conda env create -f environment.yml
        # .......
        # .......
        # To activate this environment, use:
        # $ source activate markov_py3
        #
        # To deactivate this environment, use:
        # $ source deactivate

    If you think you have an older version of the conda environment, you can manually delete the environment as follows:

    .. code:: bash

        $ source deactivate
        $ conda env remove --name markov_py3

    Then, run through the conda environment creation process again.


Running Python Script
------------------------------------------------

#.  Activate the conda environment

    .. code:: bash

        $ source activate markov_py3

#.  Copy email files to the right folders

    The ``parse_eml.py`` script will read all the .eml files from a specified folder. The script by default will look for a subfolder called ``_emails``.

    You will need to drag the emails you want from Outlook move them to the folder. The script will only look for .eml files inside the folder.

    Here is an example folder structure inside ``markovify_email/`` folder:

    .. code:: bash

        markovify_email/
        ├── README.rst
        ├── _emails
        │   ├── Declined-\ Friday\ Lunches.eml
        │   ├── Dinner\ tonight?.eml
        │   ├── Re-\ Almost\ there....eml
        │   ├── Re-\ Almost\ there...[1].eml
        │   ├── Re-\ Almost\ there...[2].eml
        │   ├── Re-\ Almost\ there...[3].eml
        │   ├── Re-\ Dinner\ tonight?.eml
        │   └── Tentative-\ Friday\ Lunches.eml
        ├── corpus
        ├── environment.yml
        ├── markovify_text.py
        └── parse_eml.py

#.  Run script to parse eml into corpus

    .. code:: bash

        $ python parse_eml.py
        100%|██████████████████████████████| 1528/1528 [00:06<00:00, 240.84it/s]

    If the folder containing the emails is in a different location, you can also use the ``--workdir`` flag to point to the correct location, such as the following example:

    .. code:: bash

        python parse_eml.py -d ../secret_emails/


#. Run script to generate random sentences from corpus

    .. code:: bash

        $ python markovify_text.py --file corpus/DingIKang.txt

        You mentioned that Daniel will be traveling on Friday.
        I know we have been the main driver for the detailed response!
        BTW, do you mind sending me more information about the data week?
        Best, I-Kang It is very helpful for debugging.
        Hi all, It turned out that you don’t see any attachments?
        Could you provide me with some examples, either for this submission.
        Hi Mohammad, Sorry, my phone had some reports from Dan already.
        I know we were discussing whether there could be some potential for moving forward.
        We only need to watch him at home.
        Link for the extremely late-minute question, I totally understand if you don’t have a use, or just forget about this tomorrow.

