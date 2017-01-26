"""Parse email from .eml files in a particular folder.

Tested in Python 3.5. You can run this script by:
    $ python parse_eml.py
"""
import argparse
import email
import logging
import os
import re
import sys

from tqdm import tqdm

logging.basicConfig(level=logging.INFO)


def make_filename(s):
    """Create a safe-to-use filename from an input email address.

    Works by leaving only alphanumeric characters ( a-z, A-Z, 0-9 ) and
    underscore.

    Example:
        input: '"O\'Donnell, Kathryn" <Kathryn.O\'Donnell@capitalone.com>'
        output: ODonnellKathryn

    Source: http://stackoverflow.com/questions/7406102/create-sane-safe-filename-from-any-unsafe-string

    Args:
        s (str): input string

    Returns:
        a string that is safe as file name.
    """
    name = s.split(' <')[0]
    return "".join([c for c in name if re.match(r'\w', c)])


if __name__ == '__main__':
    # Exit the script if not using Python 3
    if sys.version_info[0] < 3:
        raise EnvironmentError('Must be using Python 3')

    # Add a argparse argument to specify working dir from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--workdir', type=str, default='./_emails',
        help='Working directory that contains the email (.eml) files')

    args = parser.parse_args()
    work_dir = args.workdir

    # Loop through each .eml file in the working folder
    file_list = os.listdir(work_dir)
    for f in tqdm(file_list):
        if f.endswith('.eml'):
            input_file = os.path.join(work_dir, f)
            # Read email
            logging.debug('Reading email %s', input_file)
            with open(input_file) as eml:
                msg = email.message_from_file(eml)

            # Get the lower case author. We'll use this as the folder name.
            author = make_filename(msg['From'])

            # Construct the folder and file path.
            # We'll save output as .md file
            folder_path = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), 'corpus')

            if not os.path.isdir(folder_path):
                os.makedirs(folder_path)
            file_path = os.path.join(folder_path, author + '.txt')

            # Read the raw text (non-HTML version) of the email.
            # Raw text payload
            if isinstance(msg.get_payload(), str):
                text = msg.get_payload()

            # No attachments
            elif msg.get_payload(1).get_content_maintype() == 'text':
                text = (msg
                        .get_payload(0)
                        .get_payload(decode=True)
                        .decode('utf-8'))

            # Has attachments: need to go another layer deeper in payload
            else:
                text = (msg
                        .get_payload(0)
                        .get_payload(0)
                        .get_payload(decode=True)
                        .decode('utf-8'))

            # Get only the main message, not the quotes from other
            # people's email.
            text = text.split('\nFrom: ')[0]

            # Additional regex splitting to match patterns like:
            # On Dec 2, 2016
            p = re.compile(r'\nOn\s(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2}\,\s(199[0-9]|20[0-9]{2})')
            text = p.split(text)[0]

            # Append the lines into the file (specific to the author)
            with open(file_path, 'a') as output_file:
                output_file.write(text)
                output_file.write('\n')

            logging.debug('%s saved to %s. Deleting the input email file.',
                          input_file, file_path)

            # Delete the original email file
            os.remove(input_file)
